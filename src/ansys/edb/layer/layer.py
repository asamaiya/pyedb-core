"""Layer."""

from enum import Enum

import ansys.api.edb.v1.layer_pb2 as layer_pb2
from ansys.api.edb.v1.layer_pb2_grpc import LayerServiceStub

from ansys.edb.core import ObjBase
from ansys.edb.core.messages import (
    get_product_property_ids_message,
    get_product_property_message,
    set_product_property_message,
)
from ansys.edb.edb_defs import LayoutObjType
from ansys.edb.session import StubAccessor, StubType


# Message creation helper method
def _is_in_zone_message(lyr, zone):
    """Convert to IsInZoneMessage."""
    return layer_pb2.ZoneMessage(layer=lyr.msg, zone=zone)


class LayerType(Enum):
    """Enum representing types of layers."""

    SIGNAL_LAYER = layer_pb2.SIGNAL_LAYER
    DIELECTRIC_LAYER = layer_pb2.DIELECTRIC_LAYER
    CONDUCTING_LAYER = layer_pb2.CONDUCTING_LAYER
    AIRLINES_LAYER = layer_pb2.AIRLINES_LAYER
    ERRORS_LAYER = layer_pb2.ERRORS_LAYER
    SYMBOL_LAYER = layer_pb2.SYMBOL_LAYER
    MEASURE_LAYER = layer_pb2.MEASURE_LAYER
    ASSEMBLY_LAYER = layer_pb2.ASSEMBLY_LAYER
    SILKSCREEN_LAYER = layer_pb2.SILKSCREEN_LAYER
    SOLDER_MASK_LAYER = layer_pb2.SOLDER_MASK_LAYER
    SOLDER_PASTE_LAYER = layer_pb2.SOLDER_PASTE_LAYER
    GLUE_LAYER = layer_pb2.GLUE_LAYER
    WIREBOND_LAYER = layer_pb2.WIREBOND_LAYER
    USER_LAYER = layer_pb2.USER_LAYER
    SIWAVE_HFSS_SOLVER_REGIONS = layer_pb2.SIWAVE_HFSS_SOLVER_REGIONS
    POST_PROCESSING_LAYER = layer_pb2.POST_PROCESSING_LAYER
    OUTLINE_LAYER = layer_pb2.OUTLINE_LAYER
    LAYER_TYPES_COUNT = layer_pb2.LAYER_TYPES_COUNT
    UNDEFINED_LAYER_TYPE = layer_pb2.UNDEFINED_LAYER_TYPE


class TopBottomAssociation(Enum):
    """Enum representing the top-bottom association of layers."""

    TOP_ASSOCIATED = layer_pb2.TOP_ASSOCIATED
    NO_TOP_BOTTOM_ASSOCIATED = layer_pb2.NO_TOP_BOTTOM_ASSOCIATED
    BOTTOM_ASSOCIATED = layer_pb2.BOTTOM_ASSOCIATED
    TOP_BOTTOM_ASSOCIATION_COUNT = layer_pb2.TOP_BOTTOM_ASSOCIATION_COUNT
    INVALID_TOP_BOTTOM_ASSOCIATION = layer_pb2.INVALID_TOP_BOTTOM_ASSOCIATION


class DrawOverride(Enum):
    """Enum representing draw override options for layers."""

    NO_OVERRIDE = layer_pb2.NO_OVERRIDE
    FILL = layer_pb2.FILL
    WIREFRAME = layer_pb2.WIREFRAME


class LayerVisibility(Enum):
    """Enum representing visibility options for layers."""

    PRIMITIVE_VISIBLE = layer_pb2.PRIMITIVE_VISIBLE
    PATH_VISIBLE = layer_pb2.PATH_VISIBLE
    PAD_VISIBLE = layer_pb2.PAD_VISIBLE
    HOLE_VISIBLE = layer_pb2.HOLE_VISIBLE
    COMPONENT_VISIBLE = layer_pb2.COMPONENT_VISIBLE
    ALL_VISIBLE = layer_pb2.ALL_VISIBLE


class Layer(ObjBase):
    """Base class representing a layer."""

    layout_obj_type = LayoutObjType.LAYER
    __stub: LayerServiceStub = StubAccessor(StubType.layer)

    def cast(self):
        """Cast the layer object to correct concrete type.

        Returns
        -------
        Layer
        """
        from ansys.edb.layer import StackupLayer, ViaLayer

        lyr = Layer(self.msg)
        if lyr.is_stackup_layer():
            if lyr.is_via_layer():
                return ViaLayer(self.msg)
            else:
                return StackupLayer(self.msg)
        else:
            return lyr

    @staticmethod
    def create(name, lyr_type):
        """Create a non-stackup layer.

        Parameters
        ----------
        name : string
        lyr_type : LayerType

        Returns
        -------
        Layer
        """
        return Layer(
            Layer.__stub.Create(layer_pb2.LayerCreationMessage(name=name, type=lyr_type.value))
        )

    @property
    def type(self):
        """Get layer type.

        Returns
        -------
        LayerType
        """
        return LayerType(self.__stub.GetLayerType(self.msg).type)

    @type.setter
    def type(self, lyr_type):
        """Set layer type.

        Parameters
        ----------
        lyr_type : LayerType
        """
        self.__stub.SetLayerType(layer_pb2.SetLayerTypeMessage(layer=self.msg, type=lyr_type.value))

    def is_stackup_layer(self):
        """Determine if the layer is a stackup layer.

        Returns
        -------
        bool
        """
        layer_type = self.type
        return (
            layer_type == LayerType.DIELECTRIC_LAYER
            or layer_type == LayerType.CONDUCTING_LAYER
            or layer_type == LayerType.SIGNAL_LAYER
        )

    def is_via_layer(self):
        """Determine if the layer is via layer.

        Returns
        -------
        bool
        """
        return self.__stub.IsViaLayer(self.msg).value

    @property
    def name(self):
        """Get the name of the layer.

        Returns
        -------
        str
        """
        return self.__stub.GetName(self.msg).value

    @name.setter
    def name(self, name):
        """Set the layer name.

        Parameters
        ----------
        name : str
        """
        self.__stub.SetName(layer_pb2.SetNameMessage(layer=self.msg, name=name))

    def clone(self, copy_id=True):
        """Create a clone of the layer.

        Parameters
        ----------
        copy_id : bool

        Returns
        -------
        Layer
        """
        return Layer(self.__stub.Clone(layer_pb2.CloneMessage(layer=self.msg, copy_id=copy_id)))

    @property
    def layer_id(self):
        """Get the layer id of the layer.

        Returns
        -------
        int
        """
        return self.__stub.GetLayerId(self.msg).value

    @property
    def top_bottom_association(self):
        """Get the top-bottom association of the layer.

        Returns
        -------
        TopBottomAssociation
        """
        return TopBottomAssociation(
            self.__stub.GetTopBottomAssociation(self.msg).top_bottom_association
        )

    @top_bottom_association.setter
    def top_bottom_association(self, top_bottom_association):
        """Set the top-bottom association of the layer.

        Parameters
        ----------
        top_bottom_association : TopBottomAssociation
        """
        self.__stub.SetTopBottomAssociation(
            layer_pb2.SetTopBottomAssociationMessage(
                layer=self.msg, top_bottom_association=top_bottom_association.value
            )
        )

    @property
    def color(self):
        """Get the color of the layer.

        Returns
        -------
        tuple[int, int, int]
            Tuple containing the color RGB values in the format (R,G,B)
        """
        color_int = self.__stub.GetColor(self.msg).value
        r = color_int & 0x000000FF
        g = (color_int & 0x0000FF00) >> 8
        b = (color_int & 0x00FF0000) >> 16
        return r, g, b

    @color.setter
    def color(self, rgb):
        """Set the color of the layer.

        Parameters
        ----------
        tuple[int, int, int]
            Tuple containing the color RGB values in the format (R,G,B)
        """
        r = rgb[0] & 0x000000FF
        g = (rgb[1] << 8) & 0x0000FF00
        b = (rgb[2] << 16) & 0x00FF0000
        self.__stub.SetColor(layer_pb2.SetColorMessage(layer=self.msg, color=b | g | r))

    @property
    def visibility_mask(self):
        """Get the visibility mask of the layer.

        Returns
        -------
        int
        """
        return self.__stub.GetVisibilityMask(self.msg).value

    @visibility_mask.setter
    def visibility_mask(self, visibility_mask):
        """Set the visibility mask of the layer.

        Parameters
        ----------
        visibility_mask : int or LayerVisibility

        Returns
        -------
        int
        """
        vis_mask_int = (
            visibility_mask.value
            if isinstance(visibility_mask, LayerVisibility)
            else visibility_mask
        )
        self.__stub.SetVisibilityMask(
            layer_pb2.SetVisibilityMaskMessage(layer=self.msg, visibility_mask=vis_mask_int)
        )

    @property
    def locked(self):
        """Check if the layer is locked.

        Returns
        -------
        bool
        """
        return self.__stub.GetLocked(self.msg).value

    @locked.setter
    def locked(self, locked):
        """Set the locked status of the layer.

        Parameters
        ----------
        locked : bool
        """
        self.__stub.SetLocked(layer_pb2.SetLockedMessage(layer=self.msg, is_locked=locked))

    @property
    def transparency(self):
        """Get the transparency value of the layer.

        Returns
        -------
        int
        """
        return self.__stub.GetTransparency(self.msg).value

    @transparency.setter
    def transparency(self, transparency):
        """Set the transparency value of the layer.

        Parameters
        ----------
        transparency : int
        """
        self.__stub.SetTransparency(
            layer_pb2.SetTransparencyMessage(layer=self.msg, transparency=transparency)
        )

    @property
    def draw_override(self):
        """Get the draw override of the layer.

        Returns
        -------
        DrawOverride
        """
        return DrawOverride(self.__stub.GetDrawOverride(self.msg).draw_override)

    @draw_override.setter
    def draw_override(self, draw_override):
        """Set the draw override of the layer.

        Parameters
        ----------
        draw_override : DrawOverride
        """
        self.__stub.SetDrawOverride(
            layer_pb2.SetDrawOverrideMessage(layer=self.msg, draw_override=draw_override.value)
        )

    def get_product_property(self, prod_id, attr_it):
        """Get the product property of the layer associated with the given product and attribute ids.

        Parameters
        ----------
        prod_id : ProductIdType
        attr_it : int

        Returns
        -------
        str
        """
        return self.__stub.GetProductProperty(
            get_product_property_message(self, prod_id, attr_it)
        ).value

    def set_product_property(self, prod_id, attr_it, prop_value):
        """Set the product property of the layer associated with the given product and attribute ids.

        Parameters
        ----------
        prod_id : ProductIdType
        attr_it : int
        prop_value : str
        """
        self.__stub.SetProductProperty(
            set_product_property_message(self, prod_id, attr_it, prop_value)
        )

    def get_product_property_ids(self, prod_id):
        """Get a list of attribute ids corresponding to the provided product id for the layer.

        Parameters
        ----------
        prod_id : ProductIdType

        Returns
        -------
        list[int]
        """
        attr_ids = self.__stub.GetProductPropertyIds(
            get_product_property_ids_message(self, prod_id)
        ).ids
        return [attr_id for attr_id in attr_ids]

    def is_in_zone(self, zone):
        """Check if the layer exists in the provided zone.

        Parameters
        ----------
        zone : int

        Returns
        -------
        bool
        """
        return self.__stub.IsInZone(_is_in_zone_message(self, zone)).value

    def set_is_in_zone(self, zone, in_zone=True):
        """Set whether the layer exists in the specified zone.

        Parameters
        ----------
        zone : int
        in_zone : bool
        """
        return self.__stub.SetIsInZone(
            layer_pb2.SetIsInZoneMessage(zone_msg=_is_in_zone_message(self, zone), in_zone=in_zone)
        )

    @property
    def zones(self):
        """Retrieve the zone ids of all zones containing the layer.

        Returns
        -------
        list[int]
        """
        return [zone for zone in self.__stub.GetZones(self.msg).zones]

    @property
    def zone(self):
        """Return the zone index associated with owning layer collection.

        If owner is invalid the index is 0, if owner is multizone the index is -1.

        Returns
        -------
        int
        """
        return self.__stub.GetZone(self.msg).value
