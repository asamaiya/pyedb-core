"""Layout."""

from ansys.api.edb.v1 import layout_pb2
from ansys.api.edb.v1.layout_pb2_grpc import LayoutServiceStub

from ansys.edb.core.edb_defs import LayoutObjType
from ansys.edb.core.hierarchy import CellInstance, Group, PinGroup
from ansys.edb.core.inner import ObjBase, messages, parser, utils, variable_server
from ansys.edb.core.layer import LayerCollection
import ansys.edb.core.layout as layout
from ansys.edb.core.layout.mcad_model import McadModel
from ansys.edb.core.layout_instance import LayoutInstance
from ansys.edb.core.net import DifferentialPair, ExtendedNet, Net, NetClass
from ansys.edb.core.primitive import BoardBendDef, PadstackInstance, Primitive
from ansys.edb.core.session import StubAccessor, StubType
from ansys.edb.core.terminal import Terminal


class Layout(ObjBase, variable_server.VariableServer):
    """Layout."""

    __stub: LayoutServiceStub = StubAccessor(StubType.layout)

    def __init__(self, msg):
        """Initialize a new layout.

        Parameters
        ----------
        msg : EDBObjMessage
        """
        ObjBase.__init__(self, msg)
        variable_server.VariableServer.__init__(self, msg)

    @property
    def cell(self):
        """:class:`Cell <ansys.edb.core.layout.Cell>`: Owning cell for this layout.

        Read-Only.
        """
        from ansys.edb.core.layout.cell import Cell

        return Cell(self.__stub.GetCell(self.msg))

    @property
    def layer_collection(self):
        """:class:`LayerCollection <ansys.edb.core.layer.LayerCollection>` : Layer collection of this layout."""
        return LayerCollection(self.__stub.GetLayerCollection(self.msg))

    @layer_collection.setter
    def layer_collection(self, layer_collection):
        """Set layer collection."""
        self.__stub.SetLayerCollection(
            layout_pb2.SetLayerCollectionMessage(
                layout=self.msg, layer_collection=layer_collection.msg
            )
        )

    def _get_items(self, obj_type, lyt_obj_type_enum, do_cast=False):
        """Get list of layout objects."""
        items = utils.map_list(
            self.__stub.GetItems(messages.layout_get_items_message(self, lyt_obj_type_enum)).items,
            obj_type,
        )
        return items if not do_cast else [item.cast() for item in items]

    @property
    def primitives(self):
        """:obj:`list` of :class:`Primitive <ansys.edb.core.primitive.Primitive>` : List of all the primitives in this \
        layout.

        Read-Only.
        """
        return self._get_items(Primitive, LayoutObjType.PRIMITIVE, True)

    @property
    def padstack_instances(self):
        """:obj:`list` of :class:`PadstackInstance <ansys.edb.core.primitive.PadstackInstance>` : List of all padstack \
        instances in this layout.

        Read-Only.
        """
        return self._get_items(PadstackInstance, LayoutObjType.PADSTACK_INSTANCE)

    @property
    def terminals(self):
        """:obj:`list` of :class:`Terminal <ansys.edb.core.terminal.Terminal>` : \
        List of all the terminals in this layout.

        Read-Only.
        """
        return self._get_items(Terminal, LayoutObjType.TERMINAL, True)

    @property
    def cell_instances(self):
        """:obj:`list` of :class:`CellInstance <ansys.edb.core.hierarchy.CellInstances>` : \
        List of the cell instances in this layout.

        Read-Only.
        """
        return self._get_items(CellInstance, LayoutObjType.CELL_INSTANCE)

    @property
    def nets(self):
        """:obj:`list` of :class:`Net <ansys.edb.core.net.Net>` : List of all the nets in this layout.

        Read-Only.
        """
        return self._get_items(Net, LayoutObjType.NET)

    @property
    def groups(self):
        """:obj:`list` of :class:`Group <ansys.edb.core.hierarchy.Group>` : List of all the groups in this layout.

        Read-Only.
        """
        return self._get_items(Group, LayoutObjType.GROUP, True)

    @property
    def net_classes(self):
        """:obj:`list` of :class:`NetClass <ansys.edb.core.net.NetClass>` : List of all the netclassses in this layout.

        Read-Only.
        """
        return self._get_items(NetClass, LayoutObjType.NET_CLASS)

    @property
    def differential_pairs(self):
        """:obj:`list` of :class:`DifferentialPair <ansys.edb.core.net.DifferentialPair>` : \
        List of all the differential pairs in this layout.

        Read-Only.
        """
        return self._get_items(DifferentialPair, LayoutObjType.DIFFERENTIAL_PAIR)

    @property
    def pin_groups(self):
        """:obj:`list` of :class:`PinGroup <ansys.edb.core.hierarchy.PinGroup>` : List of all the pin groups in this \
        layout.

        Read-Only.
        """
        return self._get_items(PinGroup, LayoutObjType.PIN_GROUP)

    @property
    def voltage_regulators(self):
        """:obj:`list` of :class:`VoltageRegulator <ansys.edb.core.hierarchy.VoltageRegulator>` : \
        List of all the voltage regulators in this layout.

        Read-Only.
        """
        return self._get_items(layout.VoltageRegulator, LayoutObjType.VOLTAGE_REGULATOR)

    @property
    def extended_nets(self):
        """:obj:`list` of :class:`ExtendedNet <ansys.edb.core.net.ExtendedNet>` : \
        List of all the extended nets in this layout.

        Read-Only.
        """
        return self._get_items(ExtendedNet, LayoutObjType.EXTENDED_NET)

    @parser.to_polygon_data
    def expanded_extent(
        self, nets, extent, expansion_factor, expansion_unitless, use_round_corner, num_increments
    ):
        """Get an expanded polygon for the Nets collection.

        Parameters
        ----------
        nets : list[:class:`Net <ansys.edb.core.net.Net>`]
            A list of nets.
        extent : :class:`ExtentType <ansys.edb.core.geometry.ExtentType>`
            Geometry extent type for expansion.
        expansion_factor : float
            Expansion factor for the polygon union. No expansion occurs if the `expansion_factor` is less than or \
            equal to 0.
        expansion_unitless : bool
            When unitless, the distance by which the extent expands is the factor multiplied by the longer dimension\
            (X or Y distance) of the expanded object/net.
        use_round_corner : bool
            Whether to use round or sharp corners.
            For round corners, this returns a bounding box if its area is within 10% of the rounded expansion's area.
        num_increments : int
            Number of iterations desired to reach the full expansion.

        Returns
        -------
        :class:`PolygonData <ansys.edb.core.geometry.PolygonData>`

        Notes
        -----
        Method returns the expansion of the contour, so any voids within expanded objects are ignored.
        """
        return self.__stub.GetExpandedExtentFromNets(
            messages.layout_expanded_extent_message(
                self,
                nets,
                extent,
                expansion_factor,
                expansion_unitless,
                use_round_corner,
                num_increments,
            )
        )

    def convert_primitives_to_vias(self, primitives, is_pins=False):
        """Convert a list of primitives into vias or pins.

        Parameters
        ----------
        primitives : list[:class:`Primitive <ansys.edb.core.primitive.Primitive>`]
            List of primitives to convert.
        is_pins : bool, optional
            True for pins, false for vias (default).
        """
        self.__stub.ConvertPrimitivesToVias(
            messages.layout_convert_p2v_message(self, primitives, is_pins)
        )

    @property
    def port_reference_terminals_connected(self):
        """:obj:`bool`: Determine if port reference terminals are connected, applies to lumped ports and circuit ports.

        True if they are connected, False otherwise.
        Read-Only.
        """
        return self.__stub.ArePortReferenceTerminalsConnected(self.msg).is_connected

    @property
    def zone_primitives(self):
        """:obj:`list` of :class:`Primitive <ansys.edb.core.primitive.Primitive>` : List of all the primitives in \
        :term:`zones <Zone>`.

        Read-Only.
        """
        return [Primitive(msg) for msg in self.__stub.GetZonePrimitives(self.msg)]

    @property
    def fixed_zone_primitive(self):
        """:class:`Primitive <ansys.edb.core.primitive.Primitive>` : Fixed :term:`zones <Zone>` primitive."""
        msg = self.__stub.GetFixedZonePrimitive(self.msg)
        return None if msg is None else Primitive(msg).cast()

    @fixed_zone_primitive.setter
    def fixed_zone_primitive(self, value):
        self.__stub.SetFixedZonePrimitives(messages.pointer_property_message(self, value))

    @property
    def board_bend_defs(self):
        """:obj:`list` of :class:`BoardBendDef <ansys.edb.core.primitive.BoardBendDef>` : List of all the board bend \
        definitions in this layout.

        Read-Only.
        """
        return [BoardBendDef(msg) for msg in self.__stub.GetBoardBendDefs(self.msg)]

    def synchronize_bend_manager(self):
        """Synchronize bend manager."""
        self.__stub.SynchronizeBendManager(self.msg)

    @property
    def layout_instance(self):
        """:class:`LayoutInstance <ansys.edb.core.layout_instance.LayoutInstance>` : Layout instance of this layout.

        Read-Only.
        """
        return LayoutInstance(self.__stub.GetLayoutInstance(self.msg))

    def create_stride(self, filename):
        """Create a stride model from a Mcad file.

        Parameters
        ----------
        filename : str
            absolute path of Mcad file.

        Returns
        -------
        McadModel
        """
        return McadModel.create_stride(layout=self, filename=filename)

    def create_hfss(self, filename, design):
        """Create a HFSS model from a Mcad file.

        Parameters
        ----------
        filename : str
            absolute path of Mcad file.
        design : str
            design name.

        Returns
        -------
        McadModel
        """
        return McadModel.create_hfss(connectable=self, filename=filename, design=design)

    def create_3d_comp(self, filename):
        """Create a 3dComp model from a Mcad file.

        Parameters
        ----------
        filename : str
            absolute path of Mcad file.

        Returns
        -------
        McadModel
        """
        return McadModel.create_3d_comp(layout=self, filename=filename)