"""Extended Net."""

import ansys.api.edb.v1.extended_net_pb2 as enet_pb2

from ansys.edb.edb_defs import LayoutObjType
from ansys.edb.net import net_class
from ansys.edb.session import StubAccessor, StubType, get_extended_net_stub


class _ExtendedNetQueryBuilder:
    @staticmethod
    def extnet_create_msg(layout, name):
        return enet_pb2.ExtendedNetCreationMessage(layout=layout.msg, name=name)

    @staticmethod
    def extenet_find_by_name_msg(layout, name):
        return enet_pb2.ExtendedNetLookupMessage(layout=layout.msg, name=name)

    def extnet_modify_net_msg(ext_net, net):
        return enet_pb2.ExtendedNetModifyMessage(ext_net=ext_net.msg, net=net.msg)


class ExtendedNet(net_class.NetClass):
    """ExtendedNet class."""

    __stub = StubAccessor(StubType.extended_net)
    layout_obj_type = LayoutObjType.EXTENDED_NET

    @staticmethod
    def create(layout, name):
        """Create an extended net.

        Parameters
        ----------
        layout : :class:`Layout <ansys.edb.layout.Layout>`
            Layout containing new extended net.
        name : str
            Name of the new extended net

        Returns
        -------
        ExtendedNet
            Newly created extended net
        """
        return ExtendedNet(
            get_extended_net_stub().Create(_ExtendedNetQueryBuilder.extnet_create_msg(layout, name))
        )

    @staticmethod
    def find_by_name(layout, name):
        """Find an extended net in a layout by name.

        Parameters
        ----------
        layout : :class:`Layout <ansys.edb.layout.Layout>`
            Layout being searched for extended net
        name : str
            Name of the extended net to find

        Returns
        -------
        ExtendedNet
            The extended net that was found. Check the returned extended net's \
            :obj:`is_null <ansys.edb.net.ExtendedNet.is_null>` property to see if it exists.
        """
        return ExtendedNet(
            get_extended_net_stub().FindByName(
                _ExtendedNetQueryBuilder.extenet_find_by_name_msg(layout, name)
            )
        )

    def add_net(self, net):
        """Add net to this extended net.

        Parameters
        ----------
        net : Net
            The net to be added.
        """
        self.__stub.AddNet(_ExtendedNetQueryBuilder.extnet_modify_net_msg(self, net))

    def remove_net(self, net):
        """Remove net from this extended net.

        Parameters
        ----------
        net : Net
            The net to be removed.
        """
        self.__stub.RemoveNet(_ExtendedNetQueryBuilder.extnet_modify_net_msg(self, net))

    def remove_all_nets(self):
        """Remove all nets from this extended net."""
        self.__stub.RemoveAllNets(self.msg)
