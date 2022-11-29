"""This module parses message back to client data types."""

import functools

from ansys.edb import geometry, utility


def to_point_data(fn):
    """Decorate a function that returns a message to return as PointData."""
    return _wraps(fn, _to_point_data)


def to_point_data_list(fn):
    """Decorate a function that returns a message to return as list[PointData]."""
    return _wraps(fn, _to_point_data_list)


def to_point3d_data(fn):
    """Decorate a function that returns a message to return as Point3DData."""
    return _wraps(fn, _to_point3d_data)


def to_polygon_data(fn):
    """Decorate a function that returns a message to return as PolygonData."""
    return _wraps(fn, _to_polygon_data)


def to_polygon_data_list(fn):
    """Decorate a function that returns a message to return as list[PolygonData]."""
    return _wraps(fn, _to_polygon_data_list)


def to_rlc(fn):
    """Decorate a function that returns a message to return as RLC."""
    return _wraps(fn, _to_rlc)


def to_box(fn):
    """Decorate a function that returns a message to return as (lower_left, upper_right)."""
    return _wraps(fn, _to_box)


def to_circle(fn):
    """Decorate a function that returns a message to return as (center, radius)."""
    return _wraps(fn, _to_circle)


def _wraps(fn, wrapper_fn):
    if callable(fn):

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return wrapper_fn(fn(*args, **kwargs))

        return wrapper
    else:
        return wrapper_fn(fn)


def _to_point_data(message):
    """Convert PointMessage to PointData.

    Parameters
    ----------
    message : ansys.api.edb.v1.point_data_pb2.PointMessage

    Returns
    -------
    geometry.PointData
    """
    return geometry.PointData([utility.Value(message.x), utility.Value(message.y)])


def _to_point_data_list(message):
    """Convert a message to list of PointData.

    Parameters
    ----------
    message : list[ansys.api.edb.v1.point_data_pb2.PointMessage]

    Returns
    -------
    list[geometry.PointData]
    """
    return [_to_point_data(m) for m in message]


def _to_point3d_data(message):
    """Convert Point3DMessage to PointData.

    Parameters
    ----------
    message : ansys.api.edb.v1.point_data_pb2.Point3DMessage

    Returns
    -------
    geometry.Point3DData
    """
    return geometry.Point3DData(
        utility.Value(message.x), utility.Value(message.y), utility.Value(message.z)
    )


def _to_polygon_data(message):
    """Convert arbitrary message to PolygonData if possible.

    Parameters
    ----------
    message : ansys.api.edb.v1.point_data_pb2.BoxMessage or ansys.api.edb.v1.polygon_data_pb2.PolygonDataMessage

    Returns
    -------
    geometry.PolygonData
    """
    from ansys.api.edb.v1.point_data_pb2 import BoxMessage

    if isinstance(message, BoxMessage):
        b = _to_box(message)
        return geometry.PolygonData(lower_left=b[0], upper_right=b[1])
    else:
        return geometry.PolygonData(
            points=_to_point_data_list(message.points),
            holes=_to_polygon_data_list(message.holes),
            sense=message.sense,
            closed=message.closed,
        )


def _to_polygon_data_list(message):
    """Convert arbitrary messages to list of PolygonData if possible.

    Returns
    -------
    list[geometry.PolygonData]
    """
    if hasattr(message, "polygons"):
        return [_to_polygon_data(m) for m in message.polygons]
    elif hasattr(message, "points"):
        return [_to_polygon_data(m) for m in message.points]
    else:
        return [_to_polygon_data(m) for m in message]


def _to_box(message):
    """Convert message to box.

    Parameters
    ----------
    message : ansys.api.edb.v1.point_data_pb2.BoxMessage

    Returns
    -------
    tuple[geometry.PointData, geometry.PointData]
    """
    if hasattr(message, "lower_left") and hasattr(message, "upper_right"):
        return _to_point_data(message.lower_left), _to_point_data(message.upper_right)


def _to_circle(message):
    """Convert message to circle containing center point and radius.

    Parameters
    ----------
    message : ansys.api.edb.v1.point_data_pb2.CircleMessage

    Returns
    -------
    tuple[geometry.PointData, utility.Value]
    """
    if hasattr(message, "center") and hasattr(message, "radius"):
        return _to_point_data(message.center), utility.Value(message.radius)


def _to_rlc(message):
    """Convert message to rlc containing values related to resistance inductance capacitance.

    Parameters
    ----------
    message : ansys.api.edb.v1.rlc_pb2.RlcMessage

    Returns
    -------
    Rlc
    """
    return utility.Rlc(
        utility.Value(message.r),
        message.r_enabled.value,
        utility.Value(message.l),
        message.l_enabled.value,
        utility.Value(message.c),
        message.c_enabled.value,
        message.is_parallel.value,
    )
