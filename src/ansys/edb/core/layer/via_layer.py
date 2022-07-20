"""Via Layer."""

import ansys.api.edb.v1.via_layer_pb2 as via_layer_pb2

from ansys.edb.core.core import handle_grpc_exception
from ansys.edb.core.layer import StackupLayer
from ansys.edb.core.session import get_via_layer_stub


def _via_lyr_ref_lyr_id_msg(lyr, is_upper_ref):
    """Convert to ViaLayerRefLayerIdMessage."""
    return via_layer_pb2.ViaLayerRefLayerIdMessage(via_layer=lyr.msg, is_upper_ref=is_upper_ref)


class ViaLayer(StackupLayer):
    """Via layer."""

    @staticmethod
    @handle_grpc_exception
    def create(name, lr_layer, ur_layer, material):
        """Create a via layer.

        Parameters
        ----------
        name : str
        lr_layer : str
        ur_layer : str
        material : str

        Returns
        -------
        ViaLayer
        """
        params = {
            "via_layer_name": name,
            "lower_ref_layer_name": lr_layer,
            "upper_ref_layer_name": ur_layer,
            "material_name": material,
        }
        via_layer = ViaLayer(
            get_via_layer_stub().Create(via_layer_pb2.ViaLayerCreationMessage(**params))
        )
        return via_layer

    @handle_grpc_exception
    def get_ref_layer_name(self, upper_ref):
        """Get the name of the reference layer of the via layer.

        Parameters
        ----------
        upper_ref : bool
            Flag indicating whether to retrieve the name of the upper or lower reference layer

        Returns
        -------
        str
        """
        return get_via_layer_stub().GetRefLayerName(_via_lyr_ref_lyr_id_msg(self, upper_ref)).value

    @handle_grpc_exception
    def set_ref_layer(self, ref_layer, upper_ref):
        """Set the reference layer of the via layer.

        Parameters
        ----------
        ref_layer : StackupLayer
            Layer that will be set as the new reference layer of the via layer
        upper_ref : bool
            Flag indicating whether to set the new reference layer as the
            upper or lower reference layer
        """
        get_via_layer_stub().SetRefLayer(
            via_layer_pb2.SetViaLayerRefLayerMessage(
                via_layer_ref_layer_id=_via_lyr_ref_lyr_id_msg(self, upper_ref),
                new_ref_layer=ref_layer.msg,
            )
        )
