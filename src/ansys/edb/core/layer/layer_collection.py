"""Layer Collection."""

from enum import Enum

import ansys.api.edb.v1.layer_collection_pb2 as layer_collection_pb2

from ansys.edb.core.core import ObjBase
from ansys.edb.core.core.messages import (
    get_product_property_ids_message,
    get_product_property_message,
    set_product_property_message,
)
from ansys.edb.core.layer.layer import Layer, LayerType
from ansys.edb.core.layer.stackup_layer import StackupLayer
from ansys.edb.core.session import get_layer_collection_stub


class LayerCollectionMode(Enum):
    """Enum representing possible modes of layer collection."""

    LAMINATE = layer_collection_pb2.LAMINATE
    OVERLAPPING = layer_collection_pb2.OVERLAPPING
    MULTIZONE = layer_collection_pb2.MULTIZONE


class LayerTypeSet(Enum):
    """Enum representing layer type sets used for filtering layers."""

    STACKUP_LAYER_SET = 0
    SIGNAL_LAYER_SET = 1
    DIELECTRIC_LAYER_SET = 2
    NON_STACKUP_LAYER_SET = 3
    ALL_LAYER_SET = 4


class DielectricMergingMethod(Enum):
    """Enum representing dielectric merging method options."""

    WEIGHTED_AVERAGE = layer_collection_pb2.WEIGHTED_AVERAGE
    KRASZEWSKI = layer_collection_pb2.KRASZEWSKI
    WEIGHTED_CAPACITANCE = layer_collection_pb2.WEIGHTED_CAPACITANCE


def _layer_collection_zone_message(layer_collection, zone):
    """Convert to LayerCollectionZoneMessage."""
    return layer_collection_pb2.LayerCollectionZoneMessage(
        layer_collection=layer_collection.msg, zone=zone
    )


class LayerCollection(ObjBase):
    """Layer Collection."""

    @staticmethod
    def create(mode=LayerCollectionMode.LAMINATE):
        """Create a layer collection.

        Parameters
        ----------
        mode : LayerCollectionMode, optional

        Returns
        -------
        LayerCollection
        """
        return LayerCollection(
            get_layer_collection_stub().Create(
                layer_collection_pb2.LayerCollectionModeMessage(mode=mode.value)
            )
        )

    def clone(self):
        """Create a clone of the layer collection.

        Returns
        -------
        LayerCollection
        """
        return LayerCollection(get_layer_collection_stub().Clone(self.msg))

    @property
    def mode(self):
        """Get the mode the layer collection.

        Returns
        -------
        LayerCollectionMode
        """
        return LayerCollectionMode(get_layer_collection_stub().GetMode(self.msg).mode)

    @mode.setter
    def mode(self, mode):
        """Set the mode the layer collection.

        Parameters
        ----------
        mode : LayerCollectionMode
        """
        get_layer_collection_stub().SetMode(
            layer_collection_pb2.SetLayerCollectionModeMessage(
                layer_collection=self.msg, mode=mode.value
            )
        )

    def add_layers(self, layers):
        """Add layers to a layer collection.

        Parameters
        ----------
        layers : list[Layer]
        """
        layer_msgs = [lyr.msg for lyr in layers]
        get_layer_collection_stub().AddLayers(
            layer_collection_pb2.AddLayersMessage(layer_collection=self.msg, layers=layer_msgs)
        )

    def import_from_control_file(self, control_file_path, schema_file_path=None):
        """Import layers from the provided control file and optional XML schema.

        Parameters
        ----------
        control_file_path : str
        schema_file_path : str, optional
        """
        import_msg = layer_collection_pb2.ImportFromControlFileMessage(
            layer_collection=self.msg, control_file_path=control_file_path
        )
        if schema_file_path is not None:
            import_msg.schema_path = schema_file_path
        get_layer_collection_stub().ImportFromControlFile(import_msg)

    def _add_layer(self, layer, above_below=None, add_top=None):
        """Pack layer addition arguments into AddLayersMessage and send to server."""
        add_layer_msg = layer_collection_pb2.AddLayerMessage(
            layer_collection=self.msg, layer=layer.msg
        )
        if above_below is not None:
            above_below_msg = layer_collection_pb2.AddLayerAboveBelowMessage(
                above_below_layer_name=above_below[0], add_above=above_below[1]
            )
            add_layer_msg.above_below_msg.CopyFrom(above_below_msg)
        elif add_top is not None:
            add_layer_msg.add_top = add_top
        return Layer._create(get_layer_collection_stub().AddLayer(add_layer_msg))

    def _add_layer_relative(self, layer, relative_layer_name, add_above):
        """Add a layer above or below another layer."""
        return self._add_layer(layer, (relative_layer_name, add_above))

    def add_layer_above(self, layer_to_add, layer_to_add_above_name):
        """Add a new layer above the specified layer.

         Adjusts existing layers as needed to maintain stackup consistency.

        Parameters
        ----------
        layer_to_add : Layer
        layer_to_add_above_name : str

        Returns
        -------
        Layer
        """
        return self._add_layer_relative(layer_to_add, layer_to_add_above_name, True)

    def add_layer_below(self, layer_to_add, layer_to_add_below_name):
        """Add a new layer below the specified layer.

         Adjusts existing layers as needed to maintain stackup consistency.

        Parameters
        ----------
        layer_to_add : Layer
        layer_to_add_below_name : str

        Returns
        -------
        Layer
        """
        return self._add_layer_relative(layer_to_add, layer_to_add_below_name, False)

    def add_layer_top(self, layer_to_add):
        """Add a new layer to the top of the LayerCollection.

         Adjusts existing layers as needed to maintain stackup consistency.

        Parameters
        ----------
        layer_to_add : Layer

        Returns
        -------
        Layer
        """
        return self._add_layer(layer_to_add, add_top=True)

    def add_layer_bottom(self, layer_to_add):
        """Add a new layer to the bottom of the LayerCollection.

         Adjusts existing layers as needed to maintain stackup consistency.

        Parameters
        ----------
        layer_to_add : Layer

        Returns
        -------
        Layer
        """
        return self._add_layer(layer_to_add, add_top=False)

    def add_stackup_layer_at_elevation(self, stackup_layer_to_add):
        """Add a stackup layer at user specified elevation.

         Doesn't change other stackup layer's elevation.

        Parameters
        ----------
        stackup_layer_to_add : StackupLayer

        Returns
        -------
        StackupLayer
        """
        return self._add_layer(stackup_layer_to_add)

    def add_via_layer(self, via_layer_to_add):
        """Add a via layer to the layer collection.

        Parameters
        ----------
        via_layer_to_add : ViaLayer

        Returns
        -------
        ViaLayer
        """
        return self._add_layer(via_layer_to_add)

    def is_valid(self):
        """Check if the layer collection is  in a valid state.

        Check whether there is layer overlapping or gap for laminate stackup.
        Check whether there is dielectric layer overlapping or gap for overlapping stackup.

        Returns
        -------
        bool
        """
        return get_layer_collection_stub().IsValid(self.msg).value

    def find_by_name(self, layer_name):
        """Find a layer in the layer collection.

        Parameters
        ----------
        layer_name : str

        Returns
        -------
        Layer
        """
        return Layer._create(
            get_layer_collection_stub().FindByName(
                layer_collection_pb2.FindLayerByNameMessage(
                    layer_collection=self.msg, name=layer_name
                )
            )
        )

    @staticmethod
    def _get_layer_filter(layer_types):
        """Convert a list of layer types to an integer representation of a layer filter."""
        layer_filter = 0
        for layer_type in layer_types:
            layer_type_value = layer_type.value
            if layer_type_value >= 0:
                layer_filter = layer_filter | (1 << layer_type_value)
        return layer_filter

    @staticmethod
    def _get_layer_filter_from_layer_type_set(layer_type_set):
        def _get_layer_type_list():
            if layer_type_set == LayerTypeSet.STACKUP_LAYER_SET:
                return [
                    LayerType.DIELECTRIC_LAYER,
                    LayerType.CONDUCTING_LAYER,
                    LayerType.SIGNAL_LAYER,
                ]
            elif layer_type_set == LayerTypeSet.SIGNAL_LAYER_SET:
                return [LayerType.CONDUCTING_LAYER, LayerType.SIGNAL_LAYER]
            elif layer_type_set == LayerTypeSet.DIELECTRIC_LAYER_SET:
                return [LayerType.DIELECTRIC_LAYER]
            elif layer_type_set == LayerTypeSet.NON_STACKUP_LAYER_SET:
                return list(LayerType)[LayerType.AIRLINES_LAYER.value : -2]
            else:
                return []

        return LayerCollection._get_layer_filter(_get_layer_type_list())

    def get_top_bottom_stackup_layers(self, layer_type_set):
        """Get the top and bottom stackup layers of specific type and their elevations.

        Parameters
        ----------
        layer_type_set : LayerTypeSet
            LayerTypeSet indicating which layer types to retrieve

        Returns
        -------
        tuple[Layer, float, Layer, float]
            Returns a tuple of the following format:
            (upper_layer, upper_layer_top_elevation, lower_layer, lower_layer_lower_elevation)
        """
        request = layer_collection_pb2.GetTopBottomStackupLayersMessage(
            layer_collection=self.msg,
            layer_type_set=LayerCollection._get_layer_filter_from_layer_type_set(layer_type_set),
        )
        response = get_layer_collection_stub().GetTopBottomStackupLayers(request)
        return (
            Layer._create(response.top_layer),
            response.top_layer_elevation,
            Layer._create(response.bottom_layer),
            response.bottom_layer_elevation,
        )

    def get_layers(self, layer_filter):
        """Retrieve a list of layer in the LayerCollection filtered by the given layer filter.

        Parameters
        ----------
        layer_filter : LayerTypeSet, list[LayerType]

        Returns
        -------
        list[Layer]
        """
        layer_filter_int = (
            LayerCollection._get_layer_filter_from_layer_type_set(layer_filter)
            if isinstance(layer_filter, LayerTypeSet)
            else LayerCollection._get_layer_filter(layer_filter)
        )

        response = get_layer_collection_stub().GetLayers(
            layer_collection_pb2.GetLayersMessage(
                layer_collection=self.msg, layer_filter=layer_filter_int
            )
        )

        return [Layer._create(msg) for msg in response.items]

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
        return (
            get_layer_collection_stub()
            .GetProductProperty(get_product_property_message(self, prod_id, attr_it))
            .value
        )

    def set_product_property(self, prod_id, attr_it, prop_value):
        """Set the product property of the layer associated with the given product and attribute ids.

        Parameters
        ----------
        prod_id : ProductIdType
        attr_it : int
        prop_value : str
        """
        get_layer_collection_stub().SetProductProperty(
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
        attr_ids = (
            get_layer_collection_stub()
            .GetProductPropertyIds(get_product_property_ids_message(self, prod_id))
            .ids
        )
        return [attr_id for attr_id in attr_ids]

    def merge_dielectrics(
        self,
        layout,
        start_layer_name,
        end_layer_name,
        merging_method,
        merged_layer_name,
        merged_mat_name,
    ):
        """Merge the dielectric layers in a range of layers into one large dielectric layer.

        Parameters
        ----------
        layout : Layout
        start_layer_name : str
        end_layer_name : str
        merging_method : DielectricMergingMethod
        merged_layer_name : str
        merged_mat_name : str

        Returns
        -------
        StackupLayer
        """
        return StackupLayer(
            get_layer_collection_stub().MergeDielectrics(
                layer_collection_pb2.MergeDielectricsMessage(
                    layer_collection=self.msg,
                    layout=layout.msg,
                    start_layer_name=start_layer_name,
                    end_layer_name=end_layer_name,
                    merging_method=merging_method.value,
                    merged_layer_name=merged_layer_name,
                    merged_mat_name=merged_mat_name,
                )
            )
        )

    @property
    def zone_ids(self):
        """Get a list of all zones in the LayerCollection.

        Returns
        -------
        list[int]
        """
        zones = get_layer_collection_stub().GetZoneIds(self.msg).zones
        return [zone for zone in zones]

    def get_zone_name(self, zone):
        """Get the name corresponding to the specified zone.

        Parameters
        ----------
        zone : int

        Returns
        -------
        str
        """
        return (
            get_layer_collection_stub()
            .GetZoneName(_layer_collection_zone_message(self, zone))
            .value
        )

    def set_zone_name(self, zone, name):
        """Set the name corresponding to the specified zone.

        Parameters
        ----------
        zone : int
        name : str
        """
        request = layer_collection_pb2.SetZoneNameMessage(
            layer_collection=self.msg, zone=zone, zone_name=name
        )
        get_layer_collection_stub().SetZoneName(request)

    def insert_zone(self, copy_zone=-1):
        """Insert a new zone.

        Parameters
        ----------
        copy_zone : int, optional
            If valid the new zone is inserted as a copy of the specified
            zone, otherwise the new zone is empty

        Returns
        -------
        int
            If successful, the id of the newly added zone is returned
        """
        request = layer_collection_pb2.InsertZoneMessage(
            layer_collection=self.msg, copy_zone=copy_zone
        )
        return get_layer_collection_stub().InsertZone(request).value

    def remove_zone(self, zone):
        """Remove the specified zone.

        Parameters
        ----------
        zone : int
        """
        get_layer_collection_stub().RemoveZone(_layer_collection_zone_message(self, zone))

    def simplify_dielectrics_for_phi(
        self,
        database,
        layer_thickness_thresh=-1,
        merging_method=DielectricMergingMethod.WEIGHTED_CAPACITANCE,
    ):
        """Split dielectric layers at the boundaries of signal layers and merges them.

        Parameters
        ----------
        database : Database
        layer_thickness_thresh : float, optional
        merging_method : DielectricMergingMethod, optional

        Returns
        -------
        List[StackupLayer]
            returns a list of dielectric layers created during the dielectric simplification process
        """
        simplified_lyrs = (
            get_layer_collection_stub()
            .SimplifyDielectricsForPhi(
                layer_collection_pb2.SimplifyDielectricsForPhiMessage(
                    layer_collection=self.msg,
                    database=database.msg,
                    layer_thickness_thresh=layer_thickness_thresh,
                    merging_method=merging_method.value,
                )
            )
            .items
        )
        return [StackupLayer(simplified_lyr) for simplified_lyr in simplified_lyrs]

    def add_zone_to_layer(self, layer, zone, in_zone):
        """Set the zone to the layer and update the layer in the collection.

        Parameters
        ----------
        layer : Layer
        zone : int
        in_zone : bool
        """
        request = layer_collection_pb2.AddZoneToLayerMessage(
            layer_collection=self.msg, layer=layer.msg, zone=zone, in_zone=in_zone
        )
        get_layer_collection_stub().AddZoneToLayer(request)
