"""This module parses message back to client data types."""


def to_point_data(point_message):
    """Convert PointMessage to PointData.

    Parameters
    ----------
    point_message : ansys.api.edb.v1.point_data_pb2.PointMessage

    Returns
    -------
    ansys.edb.core.models.geometries.point_data.PointData
    """
    return ansys.edb.core.geometry.point_data.PointData([point_message.x, point_message.y])
