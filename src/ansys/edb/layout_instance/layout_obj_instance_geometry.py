"""Layout Obj Instance Geometry."""

from ansys.api.edb.v1.layout_obj_instance_geometry_pb2 import LayoutObjInstanceGeometryMessage

from ansys.edb.core import ObjBase
from ansys.edb.core.messages import edb_obj_message
from ansys.edb.session import LayoutObjInstanceGeometryServiceStub, StubAccessor, StubType


class LayoutObjInstanceGeometry(ObjBase):
    """Class representing layout obj instance geometry."""

    __stub: LayoutObjInstanceGeometryServiceStub = StubAccessor(
        StubType.layout_obj_instance_geometry
    )

    def __init__(self, geometry, owning_drawing, placement_lyr):
        """Initialize layout obj instance geometry object.

        Parameters
        ----------
        geometry : EDBObjMessage
        owning_drawing : EDBObjMessage
        placement_lyr : EDBObjMessage
        """
        super().__init__(geometry)
        self._owning_drawing_id = owning_drawing.id
        self._placement_layer_id = placement_lyr.id

    @ObjBase.msg.getter
    def msg(self):
        """Return protobuf message that represents this object's ID.

        Returns
        -------
        LayoutObjInstanceGeometryMessage
        """
        return LayoutObjInstanceGeometryMessage(
            geometry=super().msg,
            owning_drawing=edb_obj_message(self._owning_drawing_id),
            placement_layer=edb_obj_message(self._placement_layer_id),
        )

    @property
    def material(self):
        """Get the material of the layout obj instance geometry.

        Returns
        -------
        str
        """
        return self.__stub.GetMaterial(self.msg).value

    @property
    def color(self):
        """Get the color of the layout obj instance geometry.

        Returns
        -------
        int
        """
        return self.__stub.GetColor(self.msg).value