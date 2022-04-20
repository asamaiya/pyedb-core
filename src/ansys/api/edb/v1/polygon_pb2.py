# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: polygon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import edb_messages_pb2 as edb__messages__pb2
try:
  google_dot_protobuf_dot_wrappers__pb2 = edb__messages__pb2.google_dot_protobuf_dot_wrappers__pb2
except AttributeError:
  google_dot_protobuf_dot_wrappers__pb2 = edb__messages__pb2.google.protobuf.wrappers_pb2
try:
  google_dot_protobuf_dot_empty__pb2 = edb__messages__pb2.google_dot_protobuf_dot_empty__pb2
except AttributeError:
  google_dot_protobuf_dot_empty__pb2 = edb__messages__pb2.google.protobuf.empty_pb2
import point_data_pb2 as point__data__pb2
import refs_pb2 as refs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='polygon.proto',
  package='ansys.api.edb.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rpolygon.proto\x12\x10\x61nsys.api.edb.v1\x1a\x12\x65\x64\x62_messages.proto\x1a\x10point_data.proto\x1a\nrefs.proto\"\xda\x01\n\x16PolygonCreationMessage\x12/\n\x06layout\x18\x01 \x01(\x0b\x32\x1f.ansys.api.edb.v1.EDBObjMessage\x12\x30\n\x05layer\x18\x02 \x01(\x0b\x32!.ansys.api.edb.v1.LayerRefMessage\x12,\n\x03net\x18\x03 \x01(\x0b\x32\x1f.ansys.api.edb.v1.NetRefMessage\x12/\n\x06points\x18\x04 \x01(\x0b\x32\x1f.ansys.api.edb.v1.PointsMessage2g\n\x0ePolygonService\x12U\n\x06\x43reate\x12(.ansys.api.edb.v1.PolygonCreationMessage\x1a\x1f.ansys.api.edb.v1.EDBObjMessage\"\x00\x62\x06proto3')
  ,
  dependencies=[edb__messages__pb2.DESCRIPTOR,point__data__pb2.DESCRIPTOR,refs__pb2.DESCRIPTOR,])




_POLYGONCREATIONMESSAGE = _descriptor.Descriptor(
  name='PolygonCreationMessage',
  full_name='ansys.api.edb.v1.PolygonCreationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layout', full_name='ansys.api.edb.v1.PolygonCreationMessage.layout', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layer', full_name='ansys.api.edb.v1.PolygonCreationMessage.layer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='net', full_name='ansys.api.edb.v1.PolygonCreationMessage.net', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='ansys.api.edb.v1.PolygonCreationMessage.points', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=304,
)

_POLYGONCREATIONMESSAGE.fields_by_name['layout'].message_type = edb__messages__pb2._EDBOBJMESSAGE
_POLYGONCREATIONMESSAGE.fields_by_name['layer'].message_type = refs__pb2._LAYERREFMESSAGE
_POLYGONCREATIONMESSAGE.fields_by_name['net'].message_type = refs__pb2._NETREFMESSAGE
_POLYGONCREATIONMESSAGE.fields_by_name['points'].message_type = point__data__pb2._POINTSMESSAGE
DESCRIPTOR.message_types_by_name['PolygonCreationMessage'] = _POLYGONCREATIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolygonCreationMessage = _reflection.GeneratedProtocolMessageType('PolygonCreationMessage', (_message.Message,), {
  'DESCRIPTOR' : _POLYGONCREATIONMESSAGE,
  '__module__' : 'polygon_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.edb.v1.PolygonCreationMessage)
  })
_sym_db.RegisterMessage(PolygonCreationMessage)



_POLYGONSERVICE = _descriptor.ServiceDescriptor(
  name='PolygonService',
  full_name='ansys.api.edb.v1.PolygonService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=306,
  serialized_end=409,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='ansys.api.edb.v1.PolygonService.Create',
    index=0,
    containing_service=None,
    input_type=_POLYGONCREATIONMESSAGE,
    output_type=edb__messages__pb2._EDBOBJMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_POLYGONSERVICE)

DESCRIPTOR.services_by_name['PolygonService'] = _POLYGONSERVICE

# @@protoc_insertion_point(module_scope)
