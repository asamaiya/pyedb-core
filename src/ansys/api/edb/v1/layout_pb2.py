# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: layout.proto

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
import edb_iterator_pb2 as edb__iterator__pb2
import layer_collection_pb2 as layer__collection__pb2
import refs_pb2 as refs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='layout.proto',
  package='ansys.api.edb.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0clayout.proto\x12\x10\x61nsys.api.edb.v1\x1a\x12\x65\x64\x62_messages.proto\x1a\x12\x65\x64\x62_iterator.proto\x1a\x16layer_collection.proto\x1a\nrefs.proto\"\x87\x01\n\x19SetLayerCollectionMessage\x12/\n\x06layout\x18\x01 \x01(\x0b\x32\x1f.ansys.api.edb.v1.EDBObjMessage\x12\x39\n\x10layer_collection\x18\x02 \x01(\x0b\x32\x1f.ansys.api.edb.v1.EDBObjMessage\"\x85\x01\n\x1dSetLayerCollectionTypeMessage\x12/\n\x06layout\x18\x01 \x01(\x0b\x32\x1f.ansys.api.edb.v1.EDBObjMessage\x12\x33\n\x04mode\x18\x02 \x01(\x0e\x32%.ansys.api.edb.v1.LayerCollectionMode\"w\n\x12LayerLookupMessage\x12/\n\x06layout\x18\x01 \x01(\x0b\x32\x1f.ansys.api.edb.v1.EDBObjMessage\x12\x30\n\x05layer\x18\x02 \x01(\x0b\x32!.ansys.api.edb.v1.LayerRefMessage2\xdf\x03\n\rLayoutService\x12M\n\x07GetCell\x12\x1f.ansys.api.edb.v1.EDBObjMessage\x1a\x1f.ansys.api.edb.v1.EDBObjMessage\"\x00\x12X\n\x12GetLayerCollection\x12\x1f.ansys.api.edb.v1.EDBObjMessage\x1a\x1f.ansys.api.edb.v1.EDBObjMessage\"\x00\x12_\n\x12SetLayerCollection\x12+.ansys.api.edb.v1.SetLayerCollectionMessage\x1a\x1a.google.protobuf.BoolValue\"\x00\x12g\n\x16SetLayerCollectionType\x12/.ansys.api.edb.v1.SetLayerCollectionTypeMessage\x1a\x1a.google.protobuf.BoolValue\"\x00\x12[\n\x10GetPrimitiveIter\x12\x1f.ansys.api.edb.v1.EDBObjMessage\x1a$.ansys.api.edb.v1.EDBIteratorMessage\"\x00\x62\x06proto3')
  ,
  dependencies=[edb__messages__pb2.DESCRIPTOR,edb__iterator__pb2.DESCRIPTOR,layer__collection__pb2.DESCRIPTOR,refs__pb2.DESCRIPTOR,])




_SETLAYERCOLLECTIONMESSAGE = _descriptor.Descriptor(
  name='SetLayerCollectionMessage',
  full_name='ansys.api.edb.v1.SetLayerCollectionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layout', full_name='ansys.api.edb.v1.SetLayerCollectionMessage.layout', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layer_collection', full_name='ansys.api.edb.v1.SetLayerCollectionMessage.layer_collection', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=111,
  serialized_end=246,
)


_SETLAYERCOLLECTIONTYPEMESSAGE = _descriptor.Descriptor(
  name='SetLayerCollectionTypeMessage',
  full_name='ansys.api.edb.v1.SetLayerCollectionTypeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layout', full_name='ansys.api.edb.v1.SetLayerCollectionTypeMessage.layout', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='ansys.api.edb.v1.SetLayerCollectionTypeMessage.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=249,
  serialized_end=382,
)


_LAYERLOOKUPMESSAGE = _descriptor.Descriptor(
  name='LayerLookupMessage',
  full_name='ansys.api.edb.v1.LayerLookupMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layout', full_name='ansys.api.edb.v1.LayerLookupMessage.layout', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layer', full_name='ansys.api.edb.v1.LayerLookupMessage.layer', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=384,
  serialized_end=503,
)

_SETLAYERCOLLECTIONMESSAGE.fields_by_name['layout'].message_type = edb__messages__pb2._EDBOBJMESSAGE
_SETLAYERCOLLECTIONMESSAGE.fields_by_name['layer_collection'].message_type = edb__messages__pb2._EDBOBJMESSAGE
_SETLAYERCOLLECTIONTYPEMESSAGE.fields_by_name['layout'].message_type = edb__messages__pb2._EDBOBJMESSAGE
_SETLAYERCOLLECTIONTYPEMESSAGE.fields_by_name['mode'].enum_type = layer__collection__pb2._LAYERCOLLECTIONMODE
_LAYERLOOKUPMESSAGE.fields_by_name['layout'].message_type = edb__messages__pb2._EDBOBJMESSAGE
_LAYERLOOKUPMESSAGE.fields_by_name['layer'].message_type = refs__pb2._LAYERREFMESSAGE
DESCRIPTOR.message_types_by_name['SetLayerCollectionMessage'] = _SETLAYERCOLLECTIONMESSAGE
DESCRIPTOR.message_types_by_name['SetLayerCollectionTypeMessage'] = _SETLAYERCOLLECTIONTYPEMESSAGE
DESCRIPTOR.message_types_by_name['LayerLookupMessage'] = _LAYERLOOKUPMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetLayerCollectionMessage = _reflection.GeneratedProtocolMessageType('SetLayerCollectionMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETLAYERCOLLECTIONMESSAGE,
  '__module__' : 'layout_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.edb.v1.SetLayerCollectionMessage)
  })
_sym_db.RegisterMessage(SetLayerCollectionMessage)

SetLayerCollectionTypeMessage = _reflection.GeneratedProtocolMessageType('SetLayerCollectionTypeMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETLAYERCOLLECTIONTYPEMESSAGE,
  '__module__' : 'layout_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.edb.v1.SetLayerCollectionTypeMessage)
  })
_sym_db.RegisterMessage(SetLayerCollectionTypeMessage)

LayerLookupMessage = _reflection.GeneratedProtocolMessageType('LayerLookupMessage', (_message.Message,), {
  'DESCRIPTOR' : _LAYERLOOKUPMESSAGE,
  '__module__' : 'layout_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.edb.v1.LayerLookupMessage)
  })
_sym_db.RegisterMessage(LayerLookupMessage)



_LAYOUTSERVICE = _descriptor.ServiceDescriptor(
  name='LayoutService',
  full_name='ansys.api.edb.v1.LayoutService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=506,
  serialized_end=985,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCell',
    full_name='ansys.api.edb.v1.LayoutService.GetCell',
    index=0,
    containing_service=None,
    input_type=edb__messages__pb2._EDBOBJMESSAGE,
    output_type=edb__messages__pb2._EDBOBJMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLayerCollection',
    full_name='ansys.api.edb.v1.LayoutService.GetLayerCollection',
    index=1,
    containing_service=None,
    input_type=edb__messages__pb2._EDBOBJMESSAGE,
    output_type=edb__messages__pb2._EDBOBJMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetLayerCollection',
    full_name='ansys.api.edb.v1.LayoutService.SetLayerCollection',
    index=2,
    containing_service=None,
    input_type=_SETLAYERCOLLECTIONMESSAGE,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetLayerCollectionType',
    full_name='ansys.api.edb.v1.LayoutService.SetLayerCollectionType',
    index=3,
    containing_service=None,
    input_type=_SETLAYERCOLLECTIONTYPEMESSAGE,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPrimitiveIter',
    full_name='ansys.api.edb.v1.LayoutService.GetPrimitiveIter',
    index=4,
    containing_service=None,
    input_type=edb__messages__pb2._EDBOBJMESSAGE,
    output_type=edb__iterator__pb2._EDBITERATORMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LAYOUTSERVICE)

DESCRIPTOR.services_by_name['LayoutService'] = _LAYOUTSERVICE

# @@protoc_insertion_point(module_scope)
