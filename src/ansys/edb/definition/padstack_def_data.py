"""Padstack Definition Data."""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

import ansys.api.edb.v1.padstack_def_data_pb2 as pb
from ansys.api.edb.v1.padstack_def_data_pb2_grpc import PadstackDefDataServiceStub
import google.protobuf.empty_pb2 as empty_pb2

from ansys.edb.core import ObjBase, messages
from ansys.edb.session import StubAccessor, StubType
from ansys.edb.utility import Value


class _PadstackDefDataQueryBuilder:
    """Class for creating padstack def data grpc messages."""

    if TYPE_CHECKING:
        from padstack_def_data import PadstackDefData

    @staticmethod
    def padstack_def_data_set_material_message(target, material):
        return pb.PadstackDefDataSetMaterialMessage(target=target.msg, name=material)

    @staticmethod
    def padstack_def_data_get_layer_names_message(names):
        return pb.PadstackDefDataGetLayerNamesMessage(names=names)

    @staticmethod
    def padstack_def_data_get_layer_ids_message(ids):
        return pb.PadstackDefDataGetLayerIdsMessage(ids=ids)

    @staticmethod
    def padstack_def_data_add_layers_message(target, names):
        return pb.PadstackDefDataAddLayersMessage(
            target=target.msg,
            layer_names=_PadstackDefDataQueryBuilder.padstack_def_data_get_layer_names_message(
                names
            ),
        )

    @staticmethod
    def padstack_def_data_get_pad_parameters_message(target, layer, pad_type):
        return pb.PadstackDefDataGetPadParametersMessage(
            target=target.msg,
            layer_name=layer if isinstance(layer, str) else None,
            layer_id=layer if isinstance(layer, int) else None,
            pad_type=pad_type.value,
        )

    @staticmethod
    def padstack_def_data_get_pad_parameters_parameters_message(
        geometry_type: PadstackDefData.PadGeometryType, sizes, offset_x, offset_y, rotation
    ):
        return pb.PadstackDefDataGetPadParametersParametersMessage(
            geometry_type=geometry_type.value,
            sizes=[messages.value_message(val) for val in sizes],
            offset_x=messages.value_message(offset_x),
            offset_y=messages.value_message(offset_y),
            rotation=messages.value_message(rotation),
        )

    @staticmethod
    def padstack_def_data_set_pad_parameters_message(
        target, layer, pad_type, type_geom, sizes, offset_x, offset_y, rotation
    ):
        p1 = _PadstackDefDataQueryBuilder.padstack_def_data_get_pad_parameters_message(
            target, layer, pad_type
        )
        p2 = _PadstackDefDataQueryBuilder.padstack_def_data_get_pad_parameters_parameters_message(
            type_geom, sizes, offset_x, offset_y, rotation
        )
        return pb.PadstackDefDataSetPadParametersMessage(
            params1=p1,
            params2=p2,
        )

    @staticmethod
    def padstack_def_data_get_polygonal_pad_parameters_parameters_message(
        fp, offset_x, offset_y, rotation
    ):
        return pb.PadstackDefDataGetPolygonalPadParametersParametersMessage(
            fp=fp.msg,
            offset_x=offset_x,
            offset_y=offset_y,
            rotation=rotation,
        )

    @staticmethod
    def padstack_def_data_set_polygonal_pad_parameters_message(
        target, layer, pad_type, fp, offset_x, offset_y, rotation
    ):
        return pb.PadstackDefDataSetPolygonalPadParametersMessage(
            params1=_PadstackDefDataQueryBuilder.padstack_def_data_get_pad_parameters_message(
                target, layer, pad_type
            ),
            fp=messages.polygon_data_message(fp),
            offset_x=messages.value_message(offset_x),
            offset_y=messages.value_message(offset_y),
            rotation=messages.value_message(rotation),
        )

    @staticmethod
    def padstack_def_data_padstack_hole_range_message(hole_range):
        return pb.PadstackDefDataPadstackHoleRangeMessage(hole_range=hole_range.value)

    @staticmethod
    def padstack_def_data_set_hole_range_message(target, hole_range):
        return pb.PadstackDefDataSetHoleRangeMessage(target=target.msg, hole_range=hole_range.value)

    @staticmethod
    def padstack_def_data_set_plating_percentage(target, plating_percentage):
        return pb.PadstackDefDataSetPlatingPercentage(
            target=target.msg, plating_percentage=messages.value_message(plating_percentage)
        )

    @staticmethod
    def padstack_def_data_solderball_shape_message(solderball_shape):
        return pb.PadstackDefDataSolderballShapeMessage(solderball_shape=solderball_shape)

    @staticmethod
    def padstack_def_data_set_solderball_shape_message(target, solderball_shape):
        return pb.PadstackDefDataSetSolderballShapeMessage(
            target=target.msg, solderball_shape=solderball_shape.value
        )

    @staticmethod
    def padstack_def_data_solderball_placement_message(target, solderball_placement):
        return pb.PadstackDefDataSolderballPlacementMessage(
            target=target.msg, solderball_placement=solderball_placement
        )

    @staticmethod
    def padstack_def_data_set_solderball_placement_message(target, solderball_placement):
        return pb.PadstackDefDataSetSolderballPlacementMessage(
            target=target.msg, solderball_placement=solderball_placement
        )

    @staticmethod
    def padstack_def_data_get_solder_ball_param_message(d1, d2):
        return pb.PadstackDefDataGetSolderBallParamMessage(
            d1=messages.value_message(d1), d2=messages.value_message(d2)
        )

    @staticmethod
    def padstack_def_data_set_solder_ball_param_message(target, d1, d2):
        return pb.PadstackDefDataSetSolderBallParamMessage(
            target=target.msg, d1=messages.value_message(d1), d2=messages.value_message(d2)
        )

    @staticmethod
    def padstack_def_data_set_solder_ball_material_message(target, material):
        return pb.PadstackDefDataSetSolderBallMaterialMessage(target=target.msg, material=material)


class PadstackDefData(ObjBase):
    """Class representing a padstack data definition."""

    __stub: PadstackDefDataServiceStub = StubAccessor(StubType.padstack_def_data)

    class PadType(Enum):
        """Enum representing Pad types.

        - REGULAR_PAD
        - ANTI_PAD
        - THERMAL_PAD
        - HOLE
        - UNKNOWN_GEOM_TYPE
        """

        REGULAR_PAD = pb.REGULAR_PAD
        ANTI_PAD = pb.ANTI_PAD
        THERMAL_PAD = pb.THERMAL_PAD
        HOLE = pb.HOLE
        UNKNOWN_GEOM_TYPE = pb.UNKNOWN_GEOM_TYPE

    class PadGeometryType(Enum):
        """Enum representing Pad Geometry types.

        - PADGEOMTYPE_NO_GEOMETRY
        - PADGEOMTYPE_CIRCLE
        - PADGEOMTYPE_SQUARE
        - PADGEOMTYPE_OVAL
        - PADGEOMTYPE_BULLET
        - PADGEOMTYPE_NSIDED_POLYGON
        - PADGEOMTYPE_POLYGON
        - PADGEOMTYPE_ROUND45
        - PADGEOMTYPE_ROUND90
        - PADGEOMTYPE_SQUARE45
        - PADGEOMTYPE_SQUARE90
        - PADGEOMTYPE_INVALID_GEOMETRY
        """

        PADGEOMTYPE_NO_GEOMETRY = pb.PADGEOMTYPE_NO_GEOMETRY
        PADGEOMTYPE_CIRCLE = pb.PADGEOMTYPE_CIRCLE
        PADGEOMTYPE_SQUARE = pb.PADGEOMTYPE_SQUARE
        PADGEOMTYPE_OVAL = pb.PADGEOMTYPE_OVAL
        PADGEOMTYPE_BULLET = pb.PADGEOMTYPE_BULLET
        PADGEOMTYPE_NSIDED_POLYGON = pb.PADGEOMTYPE_NSIDED_POLYGON
        PADGEOMTYPE_POLYGON = pb.PADGEOMTYPE_POLYGON
        PADGEOMTYPE_ROUND45 = pb.PADGEOMTYPE_ROUND45
        PADGEOMTYPE_ROUND90 = pb.PADGEOMTYPE_ROUND90
        PADGEOMTYPE_SQUARE45 = pb.PADGEOMTYPE_SQUARE45
        PADGEOMTYPE_SQUARE90 = pb.PADGEOMTYPE_SQUARE90
        PADGEOMTYPE_INVALID_GEOMETRY = pb.PADGEOMTYPE_INVALID_GEOMETRY

    class PadstackHoleRange(Enum):
        """Enum representing Pad Hole ranges.

        - THROUGH
        - BEGIN_ON_UPPER_PAD
        - END_ON_LOWER_PAD
        - UPPER_PAD_TO_LOWER_PAD
        - UNKNOWN_RANGE
        """

        THROUGH = pb.THROUGH
        BEGIN_ON_UPPER_PAD = pb.BEGIN_ON_UPPER_PAD
        END_ON_LOWER_PAD = pb.END_ON_LOWER_PAD
        UPPER_PAD_TO_LOWER_PAD = pb.UPPER_PAD_TO_LOWER_PAD
        UNKNOWN_RANGE = pb.UNKNOWN_RANGE

    class SolderballShape(Enum):
        """Enum representing Solderball shapes.

        - NO_SOLDERBALL
        - SOLDERBALL_CYLINDER
        - SOLDERBALL_SPHEROID
        - UNKNOWN_SOLDERBALL_SHAPE
        """

        NO_SOLDERBALL = pb.NO_SOLDERBALL
        SOLDERBALL_CYLINDER = pb.SOLDERBALL_CYLINDER
        SOLDERBALL_SPHEROID = pb.SOLDERBALL_SPHEROID
        UNKNOWN_SOLDERBALL_SHAPE = pb.UNKNOWN_SOLDERBALL_SHAPE

    class SolderballPlacement(Enum):
        """Enum representing Solderball placement.

        - ABOVE_PADSTACK
        - BELOW_PADSTACK
        - UNKNOWN_PLACEMENT
        """

        ABOVE_PADSTACK = pb.ABOVE_PADSTACK
        BELOW_PADSTACK = pb.BELOW_PADSTACK
        UNKNOWN_PLACEMENT = pb.UNKNOWN_PLACEMENT

    @classmethod
    def create(cls):
        """
        Create a padstack data definition.

        Returns
        -------
        PadstackDefData
            Padstack data definition created.
        """
        return PadstackDefData(cls.__stub.Create(empty_pb2.Empty()))

    @property
    def material(self):
        """
        Get the hole material of the PadstackDefData object.

        Returns
        -------
        str
            Material name.
        """
        return self.__stub.GetMaterial(self.msg)

    @material.setter
    def material(self, name: str):
        """
        Set the hole material of the PadstackDefData object.

        Parameters
        ----------
        name : str
            Material name.
        """
        self.__stub.SetMaterial(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_material_message(self, name)
        )

    @property
    def layer_names(self):
        """
        Get a list of layer names in the PadstackDefData object.

        Returns
        -------
        List[str]
            List of layer names.
        """
        layer_names_msg = self.__stub.GetLayerNames(self.msg).names
        return layer_names_msg

    @property
    def layer_ids(self):
        """
        Get a list of layer ids in the PadstackDefData object.

        Returns
        -------
        List[int]
            List of layer ids.
        """
        layer_ids_msg = self.__stub.GetLayerIds(self.msg)
        return layer_ids_msg.ids

    def add_layers(self, names):
        """
        Add a list of layers of given names into the PadstackDefData object.

        Parameters
        ----------
        names : List[str]
            List of layer names.
        """
        return self.__stub.AddLayers(
            _PadstackDefDataQueryBuilder.padstack_def_data_add_layers_message(self, names)
        )

    def get_pad_parameters(self, layer, pad_type):
        """
        Get a pad's parameters by layer name and pad type in its original value in database.

        Parameters
        ----------
        layer : Union[str, int]
        pad_type : PadstackDefData.PadType

        Returns
        -------
        tuple[
            PadstackDefData.PadGeometryType,
            List[:class:`Value <ansys.edb.utility.Value>`],
            :class:`Value <ansys.edb.utility.Value>`,
            :class:`Value <ansys.edb.utility.Value>`,
            :class:`Value <ansys.edb.utility.Value>`
        ]
            Returns a tuple of the following format:
            (pad_type, sizes, offset_x, offset_y, rotation)
            pad_type : Pad type.
            sizes : Pad parameters.
            offset_x : X offset.
            offset_y : Y offset.
            rotation : Rotation.
        """
        params = self.__stub.GetPadParameters(
            _PadstackDefDataQueryBuilder.padstack_def_data_get_pad_parameters_message(
                self, layer, pad_type
            )
        )
        return (
            PadstackDefData.PadGeometryType(params.geometry_type),
            [Value(s) for s in params.sizes],
            Value(params.offset_x),
            Value(params.offset_y),
            Value(params.rotation),
        )

    def set_pad_parameters(self, layer, pad_type, type_geom, sizes, offset_x, offset_y, rotation):
        """
        Set a pad's parameters by layer name and pad type in its original value in database.

        Parameters
        ----------
        layer : Union[str, int]
            Layer name.
        pad_type : PadstackDefData.PadType
            Pad type.
        type_geom : PadstackDefData.PadGeometryType
            Pad geometry type.
        sizes : List[:class:`Value <ansys.edb.utility.Value>`]
            Pad parameters.
        offset_x : :class:`Value <ansys.edb.utility.Value>`
            X offset.
        offset_y : :class:`Value <ansys.edb.utility.Value>`
            Y offset.
        rotation : :class:`Value <ansys.edb.utility.Value>`
            Rotation.
        """
        self.__stub.SetPadParameters(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_pad_parameters_message(
                self, layer, pad_type, type_geom, sizes, offset_x, offset_y, rotation
            )
        )

    def get_polygonal_pad_parameters(self, layer, pad_type):
        """
        Get polygonal pad parameters by layer name and pad type in its original value in database.

        Parameters
        ----------
        layer : Union[str, int]
        pad_type : PadstackDefData.PadType

        Returns
        -------
        tuple[
            :class:`PolygonData <ansys.edb.geometry.PolygonData>`,
            :class:`Value <ansys.edb.utility.Value>`,
            :class:`Value <ansys.edb.utility.Value>`,
            :class:`Value <ansys.edb.utility.Value>`
        ]
            Returns a tuple of the following format:
            (fp, offset_x, offset_y, rotation)
            fp : Polygon geometry.
            offset_x : X offset.
            offset_y : Y offset.
            rotation : Rotation.
        """
        params = self.__stub.GetPolygonalPadParameters(
            _PadstackDefDataQueryBuilder.padstack_def_data_get_pad_parameters_message(
                self, layer, pad_type
            )
        )
        return (
            params.fp,
            Value(params.offset_x),
            Value(params.offset_y),
            Value(params.rotation),
        )

    def get_hole_parameters(self):
        """
        Get hole parameter in its original value in database.

        Returns
        -------
        tuple[
            :class:`PolygonData <ansys.edb.geometry.PolygonData>`,
            :class:`Value <ansys.edb.utility.Value>`,
            :class:`Value <ansys.edb.utility.Value>`,
            :class:`Value <ansys.edb.utility.Value>`
        ]
            Returns a tuple of the following format:
            (fp, offset_x, offset_y, rotation)
            fp : Polygon geometry.
            offset_x : X offset.
            offset_y : Y offset.
            rotation : Rotation.
        """
        return self.get_pad_parameters(None, PadstackDefData.PadType.HOLE)

    def set_hole_parameters(self, type_geom, sizes, offset_x, offset_y, rotation):
        """
        Set hole parameters.

        Parameters
        ----------
        type_geom : PadstackDefData.PadGeometryType
            Pad geometry type.
        sizes : List[:class:`Value <ansys.edb.utility.Value>`]
            Pad parameters.
        offset_x : :class:`Value <ansys.edb.utility.Value>`
            X offset.
        offset_y : :class:`Value <ansys.edb.utility.Value>`
            Y offset.
        rotation : :class:`Value <ansys.edb.utility.Value>`
            Rotation.
        """
        return self.set_pad_parameters(
            -1, PadstackDefData.PadType.HOLE, type_geom, sizes, offset_x, offset_y, rotation
        )

    def set_polygonal_pad_parameters(self, layer, pad_type, fp, offset_x, offset_y, rotation):
        """
        Set polygonal pad parameters by layer id and pad type in its original value in database.

        Parameters
        ----------
        layer : Union[str, int]
            Layer id.
        pad_type : PadstackDefData.PadType
            Pad type.
        fp : :class:`PolygonData <ansys.edb.geometry.PolygonData>`
            Polygon geometry.
        offset_x : :class:`Value <ansys.edb.utility.Value>`
            X offset.
        offset_y : :class:`Value <ansys.edb.utility.Value>`
            Y offset.
        rotation : :class:`Value <ansys.edb.utility.Value>`
            Rotation.
        """
        self.__stub.SetPolygonalPadParameters(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_polygonal_pad_parameters_message(
                self, layer, pad_type, fp, offset_x, offset_y, rotation
            )
        )

    @property
    def hole_range(self):
        """
        Get the hole range of the PadstackDefData.

        Returns
        -------
        PadstackDefData.PadstackHoleRange
            Hole range.
        """
        return PadstackDefData.PadstackHoleRange(self.__stub.GetHoleRange(self.msg).hole_range)

    @hole_range.setter
    def hole_range(self, hole_range):
        """
        Set hole range type.

        Parameters
        ----------
        hole_range : PadstackDefData.PadstackHoleRange
            Hole range.
        """
        self.__stub.SetHoleRange(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_hole_range_message(self, hole_range)
        )

    @property
    def plating_percentage(self):
        """
        Get hole plating percentage.

        Returns
        -------
        :class:`Value <ansys.edb.utility.Value>`
            Hole plating percentage.
        """
        return Value(self.__stub.GetPlatingPercentage(self.msg))

    @plating_percentage.setter
    def plating_percentage(self, plating_percentage):
        """
        Set hole plating percentage.

        Parameters
        ----------
        plating_percentage : :class:`Value <ansys.edb.utility.Value>`
            Hole plating percentage.
        """
        self.__stub.SetPlatingPercentage(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_plating_percentage(
                self, plating_percentage
            )
        )

    @property
    def solder_ball_shape(self):
        """
        Get solder ball shape.

        Returns
        -------
        PadstackDefData.SolderballShape
            Solder ball shape.
        """
        return PadstackDefData.SolderballShape(
            self.__stub.GetSolderBallShape(self.msg).solderball_shape
        )

    @solder_ball_shape.setter
    def solder_ball_shape(self, solderball_shape):
        """
        Set solder ball shape.

        Parameters
        ----------
        solderball_shape : PadstackDefData.SolderballShape
            Solder ball shape.
        """
        self.__stub.SetSolderBallShape(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_solderball_shape_message(
                self, solderball_shape
            )
        )

    @property
    def solder_ball_placement(self):
        """
        Get solder ball placement position/orientation.

        Returns
        -------
        PadstackDefData.SolderballPlacement
            Specifies solderball placement/orientation.
        """
        return PadstackDefData.SolderballPlacement(self.__stub.GetSolderBallPlacement(self.msg))

    @solder_ball_placement.setter
    def solder_ball_placement(self, solderball_placement):
        """
        Set solder ball placement position.

        Parameters
        ----------
        solderball_placement : PadstackDefData.SolderballPlacement
            Specifies solderball placement/orientation.
        """
        self.__stub.SetSolderBallPlacement(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_solderball_placement_message(
                self, solderball_placement
            )
        )

    @property
    def solder_ball_param(self):
        """
        Get solder ball parameters in its original value in database.

        Returns
        -------
        tuple [:class:`Value <ansys.edb.utility.Value>`, :class:`Value <ansys.edb.utility.Value>`]
            Returns a tuple of the following format:
            (d1, d2)
            d1 : Diameter for cylinder solder ball or Top diameter for spheroid solder ball.
            d2 : Middle diameter for spheroid solder ball. Not used for cylinder solder ball.
        """
        params = self.__stub.GetSolderBallParam(self.msg)
        return (
            Value(params.d1),
            Value(params.d2),
        )

    @solder_ball_param.setter
    def solder_ball_param(self, params):
        """
        Set solder ball parameters.

        Parameters
        ----------
        tuple [:class:`Value <ansys.edb.utility.Value>`, :class:`Value <ansys.edb.utility.Value>`]
            Returns a tuple of the following format:
            (d1, d2)
            d1 : Diameter for cylinder solder ball or Top diameter for spheroid solder ball.
            d2 : Middle diameter for spheroid solder ball. Not used for cylinder solder ball.
        """
        self.__stub.SetSolderBallParam(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_solder_ball_param_message(
                self, params[0], params[1]
            )
        )

    @property
    def solder_ball_material(self):
        """
        Get solder ball material.

        Returns
        -------
        str
            Solderball material name.
        """
        return self.__stub.GetSolderBallMaterial(self.msg)

    @solder_ball_material.setter
    def solder_ball_material(self, material):
        """
        Set solder ball material.

        Parameters
        ----------
        material : str
            Solderball material name.
        """
        self.__stub.SetSolderBallMaterial(
            _PadstackDefDataQueryBuilder.padstack_def_data_set_solder_ball_material_message(
                self, material
            )
        )
