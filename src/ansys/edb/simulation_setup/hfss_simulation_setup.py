"""HFSS Simulation Setup."""

import ansys.api.edb.v1.hfss_simulation_setup_pb2 as pb

from ansys.edb.core import messages, parser
from ansys.edb.core.utils import map_list
from ansys.edb.session import HfssSimulationSetupServiceStub, StubAccessor, StubType
from ansys.edb.simulation_setup.hfss_simulation_settings import HFSSSimulationSettings
from ansys.edb.simulation_setup.simulation_setup import SimulationSetup, SimulationSetupType


class HfssSimulationSetup(SimulationSetup):
    """Class representing hfss simulation setup data."""

    __stub: HfssSimulationSetupServiceStub = StubAccessor(StubType.hfss_sim_setup)

    @classmethod
    def create(cls, cell, name):
        """Create a HfssSimulationSetup.

        Parameters
        ----------
        cell : :class:`Cell <ansys.edb.layout.Cell>`
            Cell containing new simulation setup.
        name : str
            Name of new simulation setup

        Returns
        -------
        HfssSimulationSetup
            Newly created simulation setup.
        """
        return super()._create(cell, name, SimulationSetupType.HFSS)

    @property
    def mesh_operations(self):
        """:obj:`list` of :class:`MeshOperation`: Mesh operations of the hfss simulation setup."""
        return map_list(self.__stub.GetMeshOperations(self.msg).mesh_ops, parser.to_mesh_op)

    @mesh_operations.setter
    def mesh_operations(self, new_mesh_ops):
        self.__stub.SetMeshOperations(
            pb.MeshOperationsPropertyMessage(
                target=self.msg,
                mesh_ops=pb.MeshOperationsMessage(
                    mesh_ops=map_list(new_mesh_ops, messages.mesh_operation_message)
                ),
            )
        )

    @property
    def settings(self):
        """:class:`HfssSimulationSettings`: Simulation settings of the hfss simulation setup."""
        return HFSSSimulationSettings(self)
