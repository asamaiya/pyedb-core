"""Component Model Definition."""
from ansys.api.edb.v1.component_model_pb2_grpc import (
    ComponentModelServiceStub,
    DynamicLinkComponentModelServiceStub,
    NPortComponentModelServiceStub,
)
import google.protobuf.wrappers_pb2 as proto_wrappers

from ansys.edb.core import ObjBase, messages
from ansys.edb.session import StubAccessor, StubType


class ComponentModel(ObjBase):
    """Class representing a Component Model."""

    __stub: ComponentModelServiceStub = StubAccessor(StubType.component_model)

    @property
    def reference_file(self):
        """Get reference file associated with this component model.

        This attribute is also used to set the reference file.

        Returns
        -------
        str
            Name of the reference file.
        """
        return self.__stub.GetReferenceFile(self.msg).value

    @reference_file.setter
    def reference_file(self, value):
        """Set reference file for this component model."""
        self.__stub.SetReferenceFile(messages.string_property_message(self, value))


class NPortComponentModel(ComponentModel):
    """Class representing a NPort component model."""

    __stub: NPortComponentModelServiceStub = StubAccessor(StubType.nport_component_model)

    @classmethod
    def create(cls, name):
        """Create a NPort component model.

        Parameters
        ----------
        name: str
            Name of the nport component model.

        Returns
        -------
        NPortComponentModel
            Newly created nport component model.

        Notes
        -----
        The component model will not belong to a specific database until it is added to a
        :class:`ComponentDef <ansys.edb.definition.ComponentDef>`.
        """
        return NPortComponentModel(cls.__stub.Create(proto_wrappers.StringValue(value=name)))


class DynamicLinkComponentModel(ComponentModel):
    """Class representing a Dynamic link component model."""

    __stub: DynamicLinkComponentModelServiceStub = StubAccessor(StubType.dyn_link_component_model)

    @classmethod
    def create(cls, name):
        """Create a Dynamic link component model.

        Parameters
        ----------
        name: str
            Name of the dynamic link component model.

        Returns
        -------
        DynamicLinkComponentModel
            Newly created dynamic link component model.

        Notes
        -----
        The component model will not belong to a specific database until it is added to a
        :class:`ComponentDef <ansys.edb.definition.ComponentDef>`.
        """
        return DynamicLinkComponentModel(cls.__stub.Create(proto_wrappers.StringValue(value=name)))

    @property
    def design_name(self):
        """Get design name associated with the dynamic link component model.

        This attribute is also used to set the design name.

        Returns
        -------
        str
            Name of the design.
        """
        return self.__stub.GetDesignName(self.msg).value

    @design_name.setter
    def design_name(self, value):
        """Set the design name for the dynamic link component model."""
        self.__stub.SetDesignName(messages.string_property_message(self, value))