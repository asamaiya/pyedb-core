"""Layout Object."""

import ansys.api.edb.v1.layout_obj_pb2 as layout_obj_pb2

from ansys.edb.core import ObjBase
import ansys.edb.core.messages as messages
from ansys.edb.edb_defs import LayoutObjType
from ansys.edb.layout import layout
from ansys.edb.session import LayoutObjServiceStub, StubAccessor, StubType


class _QueryBuilder:
    @staticmethod
    def layout_obj_target_msg(layout_obj, layout_type):
        return layout_obj_pb2.LayoutObjTargetMessage(target=layout_obj.msg, type=layout_type.value)

    @staticmethod
    def get_product_property_type_msg(obj, prod_id, attr_it, layout_type):
        return layout_obj_pb2.GetProductPropertyTypeMessage(
            target=messages.get_product_property_message(obj, prod_id, attr_it),
            type=layout_type.value,
        )

    @staticmethod
    def set_product_property_type_msg(obj, prod_id, att_id, value, layout_type):
        return layout_obj_pb2.SetProductPropertyTypeMessage(
            target=messages.set_product_property_message(obj, prod_id, att_id, value),
            type=layout_type.value,
        )

    @staticmethod
    def get_product_property_ids_type_msg(obj, prod_id, layout_type):
        return layout_obj_pb2.GetProductPropertyIdsTypeMessage(
            target=messages.get_product_property_ids_message(obj, prod_id),
            type=layout_type.value,
        )


class LayoutObj(ObjBase):
    """Layout Object class."""

    __stub: LayoutObjServiceStub = StubAccessor(StubType.layout_obj)
    layout_obj_type = LayoutObjType.INVALID_LAYOUT_OBJ

    @property
    def obj_type(self):
        """:class:`LayoutObjType <ansys.edb.edb_defs.LayoutObjType>`: Layout object type.

        Read-Only.
        """
        return self.layout_obj_type

    @property
    def layout(self):
        """:class:`Layout <ansys.edb.layout.Layout>`: Owning layout of the object.

        Read-Only.
        """
        return layout.Layout(
            self.__stub.GetLayout(_QueryBuilder.layout_obj_target_msg(self, self.layout_obj_type))
        )

    def delete(self):
        """Delete the layout object."""
        self.__stub.Delete(_QueryBuilder.layout_obj_target_msg(self, self.layout_obj_type))

    def get_product_property(self, prod_id, attr_id):
        """Get the product property of the layout object with the given product and attribute ids.

        Parameters
        ----------
        prod_id : :class:`ProductIdType <ansys.edb.database.ProductIdType>`
        attr_id : int

        Returns
        -------
        str
        """
        return self.__stub.GetProductProperty(
            _QueryBuilder.get_product_property_type_msg(
                self, prod_id, attr_id, self.layout_obj_type
            )
        ).value

    def set_product_property(self, prod_id, attr_id, prop_value):
        """Set the product property of the layout object associated with the given product and attribute ids.

        Parameters
        ----------
        prod_id : :class:`ProductIdType <ansys.edb.database.ProductIdType>`
        attr_id : int
        prop_value : str
        """
        self.__stub.SetProductProperty(
            _QueryBuilder.set_product_property_type_msg(
                self, prod_id, attr_id, prop_value, self.layout_obj_type
            )
        )

    def get_product_property_ids(self, prod_id):
        """Get a list of attribute ids corresponding to the provided product id for the layout object.

        Parameters
        ----------
        prod_id : :class:`ProductIdType <ansys.edb.database.ProductIdType>`

        Returns
        -------
        list[int]
        """
        attr_ids = self.__stub.GetProductPropertyIds(
            _QueryBuilder.get_product_property_ids_type_msg(self, prod_id, self.layout_obj_type)
        ).ids
        return [attr_id for attr_id in attr_ids]
