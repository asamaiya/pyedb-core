# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: adaptive_settings.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='adaptive_settings.proto',
  package='ansys.api.edb.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x61\x64\x61ptive_settings.proto\x12\x10\x61nsys.api.edb.v1\x1a\x12\x65\x64\x62_messages.proto\"a\n\x1c\x41\x64\x61ptiveFrequencyDataMessage\x12\x1a\n\x12\x61\x64\x61ptive_frequency\x18\x01 \x01(\t\x12\x11\n\tmax_delta\x18\x02 \x01(\t\x12\x12\n\nmax_passes\x18\x03 \x01(\x03\"s\n AdaptiveFrequencyDataListMessage\x12O\n\x17\x61\x64\x61ptive_frequency_data\x18\x01 \x03(\x0b\x32..ansys.api.edb.v1.AdaptiveFrequencyDataMessage\"\xbb\x01\n#SetAdaptiveFrequencyDataListMessage\x12:\n\x11\x61\x64\x61ptive_settings\x18\x01 \x01(\x0b\x32\x1f.ansys.api.edb.v1.EDBObjMessage\x12X\n\x1c\x61\x64\x61ptive_frequency_data_list\x18\x02 \x01(\x0b\x32\x32.ansys.api.edb.v1.AdaptiveFrequencyDataListMessage2\x8a\x02\n\x17\x41\x64\x61ptiveSettingsService\x12u\n\x1cGetAdaptiveFrequencyDataList\x12\x1f.ansys.api.edb.v1.EDBObjMessage\x1a\x32.ansys.api.edb.v1.AdaptiveFrequencyDataListMessage\"\x00\x12x\n\x1cSetAdaptiveFrequencyDataList\x12\x35.ansys.api.edb.v1.SetAdaptiveFrequencyDataListMessage\x1a\x1f.ansys.api.edb.v1.EDBObjMessage\"\x00\x62\x06proto3')
  ,
  dependencies=[edb__messages__pb2.DESCRIPTOR,])




_ADAPTIVEFREQUENCYDATAMESSAGE = _descriptor.Descriptor(
  name='AdaptiveFrequencyDataMessage',
  full_name='ansys.api.edb.v1.AdaptiveFrequencyDataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adaptive_frequency', full_name='ansys.api.edb.v1.AdaptiveFrequencyDataMessage.adaptive_frequency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_delta', full_name='ansys.api.edb.v1.AdaptiveFrequencyDataMessage.max_delta', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_passes', full_name='ansys.api.edb.v1.AdaptiveFrequencyDataMessage.max_passes', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=65,
  serialized_end=162,
)


_ADAPTIVEFREQUENCYDATALISTMESSAGE = _descriptor.Descriptor(
  name='AdaptiveFrequencyDataListMessage',
  full_name='ansys.api.edb.v1.AdaptiveFrequencyDataListMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adaptive_frequency_data', full_name='ansys.api.edb.v1.AdaptiveFrequencyDataListMessage.adaptive_frequency_data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=164,
  serialized_end=279,
)


_SETADAPTIVEFREQUENCYDATALISTMESSAGE = _descriptor.Descriptor(
  name='SetAdaptiveFrequencyDataListMessage',
  full_name='ansys.api.edb.v1.SetAdaptiveFrequencyDataListMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adaptive_settings', full_name='ansys.api.edb.v1.SetAdaptiveFrequencyDataListMessage.adaptive_settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adaptive_frequency_data_list', full_name='ansys.api.edb.v1.SetAdaptiveFrequencyDataListMessage.adaptive_frequency_data_list', index=1,
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
  serialized_start=282,
  serialized_end=469,
)

_ADAPTIVEFREQUENCYDATALISTMESSAGE.fields_by_name['adaptive_frequency_data'].message_type = _ADAPTIVEFREQUENCYDATAMESSAGE
_SETADAPTIVEFREQUENCYDATALISTMESSAGE.fields_by_name['adaptive_settings'].message_type = edb__messages__pb2._EDBOBJMESSAGE
_SETADAPTIVEFREQUENCYDATALISTMESSAGE.fields_by_name['adaptive_frequency_data_list'].message_type = _ADAPTIVEFREQUENCYDATALISTMESSAGE
DESCRIPTOR.message_types_by_name['AdaptiveFrequencyDataMessage'] = _ADAPTIVEFREQUENCYDATAMESSAGE
DESCRIPTOR.message_types_by_name['AdaptiveFrequencyDataListMessage'] = _ADAPTIVEFREQUENCYDATALISTMESSAGE
DESCRIPTOR.message_types_by_name['SetAdaptiveFrequencyDataListMessage'] = _SETADAPTIVEFREQUENCYDATALISTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdaptiveFrequencyDataMessage = _reflection.GeneratedProtocolMessageType('AdaptiveFrequencyDataMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADAPTIVEFREQUENCYDATAMESSAGE,
  '__module__' : 'adaptive_settings_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.edb.v1.AdaptiveFrequencyDataMessage)
  })
_sym_db.RegisterMessage(AdaptiveFrequencyDataMessage)

AdaptiveFrequencyDataListMessage = _reflection.GeneratedProtocolMessageType('AdaptiveFrequencyDataListMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADAPTIVEFREQUENCYDATALISTMESSAGE,
  '__module__' : 'adaptive_settings_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.edb.v1.AdaptiveFrequencyDataListMessage)
  })
_sym_db.RegisterMessage(AdaptiveFrequencyDataListMessage)

SetAdaptiveFrequencyDataListMessage = _reflection.GeneratedProtocolMessageType('SetAdaptiveFrequencyDataListMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETADAPTIVEFREQUENCYDATALISTMESSAGE,
  '__module__' : 'adaptive_settings_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.edb.v1.SetAdaptiveFrequencyDataListMessage)
  })
_sym_db.RegisterMessage(SetAdaptiveFrequencyDataListMessage)



_ADAPTIVESETTINGSSERVICE = _descriptor.ServiceDescriptor(
  name='AdaptiveSettingsService',
  full_name='ansys.api.edb.v1.AdaptiveSettingsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=472,
  serialized_end=738,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdaptiveFrequencyDataList',
    full_name='ansys.api.edb.v1.AdaptiveSettingsService.GetAdaptiveFrequencyDataList',
    index=0,
    containing_service=None,
    input_type=edb__messages__pb2._EDBOBJMESSAGE,
    output_type=_ADAPTIVEFREQUENCYDATALISTMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetAdaptiveFrequencyDataList',
    full_name='ansys.api.edb.v1.AdaptiveSettingsService.SetAdaptiveFrequencyDataList',
    index=1,
    containing_service=None,
    input_type=_SETADAPTIVEFREQUENCYDATALISTMESSAGE,
    output_type=edb__messages__pb2._EDBOBJMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADAPTIVESETTINGSSERVICE)

DESCRIPTOR.services_by_name['AdaptiveSettingsService'] = _ADAPTIVESETTINGSSERVICE

# @@protoc_insertion_point(module_scope)
