"""Hierarchy Obj."""

from ansys.edb.core import conn_obj, messages
from ansys.edb.definition import component_def
from ansys.edb.layer import Layer
from ansys.edb.session import StubAccessor, StubType
from ansys.edb.utility import Transform, Value


class HierarchyObj(conn_obj.ConnObj):
    """Base class representing hierarchy object."""

    __stub = StubAccessor(StubType.hierarchy_obj)

    @property
    def transform(self):
        """Get transform.

        Returns
        -------
        Transform
        """
        transform_msg = self.__stub.GetTransform(self.msg)
        return Transform(
            transform_msg.scale,
            transform_msg.angle,
            transform_msg.mirror,
            transform_msg.offset_x,
            transform_msg.offset_y,
        )

    @transform.setter
    def transform(self, value):
        """Set transform.

        Parameters
        ----------
        value : Transform
        """
        return self.__stub.SetTransform(messages.transform_property_message(self, value))

    @property
    def name(self):
        """Get name of the hierarchy object.

        Returns
        -------
        str
        """
        return self.__stub.GetName(self.msg).value

    @name.setter
    def name(self, value):
        """Set name of the hierarchy object.

        Parameters
        ----------
        value : str
        """
        return self.__stub.SetName(messages.edb_obj_name_message(self, value))

    @property
    def component(self):
        """Get underlying component on the hierarchy object.

        Returns
        -------
        ComponentDef
        """
        return component_def.ComponentDef(self.__stub.GetComponent(self.msg))

    @property
    def placement_layer(self):
        """Get placement layer.

        Returns
        -------
        layer
        """
        return Layer(self.__stub.GetPlacementLayer(self.msg))

    @placement_layer.setter
    def placement_layer(self, value):
        """Set placement layer.

        Parameters
        ----------
        value : Layer
        """
        return self.__stub.SetPlacementLayer(messages.pointer_property_message(self, value))

    @property
    def location(self):
        """Get location.

        Returns
        -------
        [value x, value y]
        """
        pnt_msg = self.__stub.GetLocation(self.msg)
        return [Value(pnt_msg.x), Value(pnt_msg.y)]

    @location.setter
    def location(self, value):
        """Set location.

        Parameters
        ----------
        value : [value x, value y]
        """
        return self.__stub.SetLocation(messages.point_property_message(self, value))

    @property
    def solve_independent_preference(self):
        """Get solve independent preference.

        Returns
        -------
        bool
        """
        return self.__stub.GetSolveIndependentPreference(self.msg).value

    @solve_independent_preference.setter
    def solve_independent_preference(self, value):
        """Set solve independent preference.

        Parameters
        ----------
        value : bool
        """
        return self.__stub.SetSolveIndependentPreference(
            messages.bool_property_message(self, value)
        )
