"""Net."""

from ansys.edb.core import layout_obj, messages
from ansys.edb.edb_defs import LayoutObjType
from ansys.edb.net.extended_net import ExtendedNet
from ansys.edb.net.net_class import NetClass
from ansys.edb.primitive import PadstackInstance, Primitive
from ansys.edb.session import NetServiceStub, StubAccessor, StubType
from ansys.edb.terminal import Terminal, TerminalInstance


class Net(layout_obj.LayoutObj):
    """Class representing net."""

    layout_obj_type = LayoutObjType.NET
    no_net_name = "<NO-NET>"
    __stub: NetServiceStub = StubAccessor(StubType.net)

    def _layout_objs(self, obj_type):
        """Get layout objects on a net."""
        return self.__stub.GetLayoutObjects(
            messages.net_get_layout_obj_message(self, obj_type)
        ).items

    @classmethod
    def create(cls, layout, name):
        """Create a net.

        Parameters
        ----------
        layout : :class:`Layout <ansys.edb.layout.Layout>`
            Layout containing new net.
        name : str
            Name of new net

        Returns
        -------
        Net
            Newly created net.
        """
        return Net(cls.__stub.Create(messages.string_property_message(layout, name)))

    @classmethod
    def find_by_name(cls, layout, name):
        """Find a net in a layout by name.

        Parameters
        ----------
        layout : :class:`Layout <ansys.edb.layout.Layout>`
            Layout being searched for net
        name : str
            Name of net being searched for.

        Returns
        -------
        Net
            Net matching the requested name. Check the returned net's \
            :obj:`is_null <ansys.edb.net.Net.is_null>` property to see if it exists.
        """
        return Net(cls.__stub.FindByName(messages.string_property_message(layout, name)))

    @property
    def name(self):
        """:class:`str`: Name of this net."""
        return self.__stub.GetName(self.msg).value

    @name.setter
    def name(self, value):
        self.__stub.SetName(messages.string_property_message(self, value))

    @property
    def is_power_ground(self):
        """:class:`bool`: True if net belongs to Power/Ground :class:`NetClass`.

        Read-Only.
        """
        return self.__stub.GetIsPowerGround(self.msg).value

    @is_power_ground.setter
    def is_power_ground(self, value):
        self.__stub.SetIsPowerGround(messages.bool_property_message(self, value))

    @property
    def primitives(self):
        r""":obj:`list`\[:class:`Primitive <ansys.edb.primitive.Primitive>`\]: List of all primitives on this net.

        Read-Only.
        """
        return [Primitive(lo).cast() for lo in self._layout_objs(LayoutObjType.PRIMITIVE)]

    @property
    def padstack_instances(self):
        r"""
        :obj:`list`\[:class:`PadstackInstance <ansys.edb.primitive.PadstackInstance>`\]: List of padstacks on this net.

        Read-Only.
        """
        return [PadstackInstance(lo) for lo in self._layout_objs(LayoutObjType.PADSTACK_INSTANCE)]

    @property
    def terminals(self):
        r""":obj:`list`\[:class:`Terminal <ansys.edb.terminal.Terminal>`\]: List of all terminals on this net.

        Read-Only.
        """
        return [Terminal(lo).cast() for lo in self._layout_objs(LayoutObjType.TERMINAL)]

    @property
    def terminal_instances(self):
        r""":obj:`list`\[:class:`TerminalInstance <ansys.edb.terminal.TerminalInstance>`\]: terminal instances on net.

        Read-Only.
        """
        return [TerminalInstance(lo) for lo in self._layout_objs(LayoutObjType.TERMINAL_INSTANCE)]

    @property
    def net_classes(self):
        r""":obj:`list`\[:class:`NetClass`\]: List of all net classes on this net.

        Read-Only.
        """
        return [NetClass(lo) for lo in self._layout_objs(LayoutObjType.NET_CLASS)]

    @property
    def extended_net(self):
        """:class:`ExtendedNet` or :class:`None`: The extended net that this net belongs to.

        :class:`None` means the net doesn't belong to an extended net.

        Read-Only.
        """
        en = ExtendedNet(self._layout_objs(LayoutObjType.NET_CLASS)[0])
        return None if en.is_null else en
