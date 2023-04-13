"""Point Data."""
from functools import reduce
import math
import operator
import sys

from ansys.api.edb.v1 import point_data_pb2_grpc

from ansys.edb import session, utility
from ansys.edb.core import messages, parser
from ansys.edb.utility import conversions


class PointData:
    """Represent arbitrary (x, y) coordinates that exist on 2D space."""

    __stub: point_data_pb2_grpc.PointDataServiceStub = session.StubAccessor(
        session.StubType.point_data
    )

    def __init__(self, *data):
        """Initialize a point data from list of coordinates.

        Parameters
        ----------
        data : Iterable[Iterable[ansys.edb.typing.ValueLike], ansys.edb.typing.ValueLike]
        """
        self._x = self._y = self._arc_h = None

        if len(data) == 1:
            # try to expand the argument.
            try:
                iter(data[0])
                data = data[0]
            except TypeError:
                pass

        if len(data) == 1:
            self._x = self._arc_h = conversions.to_value(data[0])
            self._y = sys.float_info.max
        elif len(data) == 2:
            self._x = conversions.to_value(data[0])
            self._y = conversions.to_value(data[1])
            if not self._y.is_parametric and self._y == sys.float_info.max:
                self._arc_h = self._x
        else:
            raise TypeError(
                "PointData must receive either one value representing arc height or "
                f"two values representing x and y coordinates. - Received '{data}'"
            )

    def __eq__(self, other):
        """Compare if two objects represent the same coordinates.

        Parameters
        ----------
        other : PointData

        Returns
        -------
        bool
        """
        return self.equals(other)

    def __len__(self):
        """Return the number of coordinates present.

        Returns
        -------
        int
        """
        return len(self._matrix_values)

    def __add__(self, other):
        """Perform matrix addition of two points.

        Parameters
        ----------
        other : ansys.edb.typing.PointLike

        Returns
        -------
        PointData
        """
        return self.__class__(self._map_reduce(other, operator.__add__))

    def __sub__(self, other):
        """Perform matrix subtraction of two points.

        Parameters
        ----------
        other : ansys.edb.typing.PointLike

        Returns
        -------
        PointData
        """
        return self.__class__(self._map_reduce(other, operator.__sub__))

    def __str__(self):
        """Generate unique name for point object.

        Returns
        -------
        str
        """
        coord = ",".join([str(v) for v in self._matrix_values])
        return f"<{coord}>" if self.is_arc else f"({coord})"

    def equals(self, other, tolerance=0.0):
        """Get if two points are located at the same coordinates.

        Parameters
        ----------
        other : ansys.edb.typing.PointLike
        tolerance : float, optional

        Returns
        -------
        bool
        """

        def value_equals(a, b):
            return a.equals(b, tolerance)

        try:
            return all(self._map_reduce(other, value_equals))
        except TypeError:
            return False

    @property
    def _matrix_values(self):
        """Return coordinates of this point as a list of Value.

        Returns
        -------
        list of utility.Value
        """
        return [self.arc_height] if self.is_arc else [self.x, self.y]

    def _map_reduce(self, other, op):
        other = conversions.to_point(other)
        return [reduce(op, values) for values in zip(self._matrix_values, other._matrix_values)]

    @property
    def is_arc(self):
        """Return if the point represents an arc.

        Returns
        -------
        bool
        """
        return self._arc_h is not None

    @property
    def arc_height(self):
        """Return the height of arc.

        Returns
        -------
        utility.Value
        """
        return self._arc_h

    @property
    def x(self):
        """Return the x coordinate.

        Returns
        -------
        utility.Value
        """
        return self._x

    @property
    def y(self):
        """Return the y coordinate.

        Returns
        -------
        utility.Value
        """
        return self._y

    @property
    def is_parametric(self):
        """Return if this point contains parametric values (variable expressions).

        Returns
        -------
        bool
        """
        return any(val.is_parametric for val in self._matrix_values)

    def magnitude(self):
        """Return the magnitude of point vector.

        Returns
        -------
        float
        """
        if self.is_arc:
            return 0
        return math.sqrt(sum([v**2 for v in self._matrix_values], utility.Value(0)).value)

    def normalized(self):
        """Normalize the point vector.

        Returns
        -------
        PointData
        """
        mag = self.magnitude()
        n = [0] * len(self) if mag == 0 else [v / mag for v in self._matrix_values]
        return self.__class__(n)

    @parser.to_point_data
    def closest(self, start, end):
        """Return the closest point on the line segment [start, end] from the point.

        Return None if either point is an arc.

        Parameters
        ----------
        start : ansys.edb.typing.PointLike
        end : ansys.edb.typing.PointLike

        Returns
        -------
        typing.Optional[PointData]
        """
        if not self.is_arc:
            return self.__stub.ClosestPoint(messages.point_data_with_line_message(self, start, end))

    def distance(self, start, end=None):
        """Compute the shortest distance from the point to the line segment [start, end] when end point is given, \
        otherwise the distance between the point and another.

        Parameters
        ----------
        start : ansys.edb.typing.PointLike
        end : ansys.edb.typing.PointLike, optional

        Returns
        -------
        float
        """
        if end is None:
            return (self - start).magnitude()
        else:
            return self.__stub.Distance(
                messages.point_data_with_line_message(self, start, end)
            ).value

    def cross(self, other):
        """Compute the cross product of the point vector with another.

        Return None if either point is an arc.

        Parameters
        ----------
        other : ansys.edb.typing.PointLike

        Returns
        -------
        typing.Optional[utility.Value]
        """
        other = conversions.to_point(other)
        if not self.is_arc and not other.is_arc:
            return self.x * other.y - self.y * other.x

    def move(self, vector):
        """Move the point by a vector.

        Return None if either point is an arc.

        Parameters
        ----------
        vector : ansys.edb.typing.PointLike

        Returns
        -------
        typing.Optional[PointData]
        """
        vector = conversions.to_point(vector)
        if not self.is_arc and not vector.is_arc:
            return self + vector

    @parser.to_point_data
    def rotate(self, angle, center):
        """Rotate a point at the specified center by the specified angle.

        Return None if either point is an arc.

        Parameters
        ----------
        angle : float
            in radians.
        center : ansys.edb.typing.PointLike

        Returns
        -------
        typing.Optional[PointData]
        """
        if not self.is_arc:
            return self.__stub.Rotate(messages.point_data_rotate_message(self, center, angle))

    def dot(self, other):
        """Perform per-component multiplication (dot product) of two points.

        Parameters
        ----------
        other : ansys.edb.typing.PointLike

        Returns
        -------
        float
        """
        return sum(self._map_reduce(other, operator.__mul__), utility.Value(0)).value

    def angle(self, other):
        """Get the angle between another vector.

        Parameters
        ----------
        other : ansys.edb.typing.PointLike

        Returns
        -------
        float
            angle in radian.
        """
        other = conversions.to_point(other)
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))
