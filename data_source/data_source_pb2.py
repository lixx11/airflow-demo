# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_source.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data_source.proto',
  package='data_source',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11\x64\x61ta_source.proto\x12\x0b\x64\x61ta_source\"\x1b\n\x0b\x44\x61taRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\tDataReply\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\x32M\n\nDataSource\x12?\n\tFetchData\x12\x18.data_source.DataRequest\x1a\x16.data_source.DataReply\"\x00\x62\x06proto3'
)




_DATAREQUEST = _descriptor.Descriptor(
  name='DataRequest',
  full_name='data_source.DataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='data_source.DataRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=34,
  serialized_end=61,
)


_DATAREPLY = _descriptor.Descriptor(
  name='DataReply',
  full_name='data_source.DataReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='data_source.DataReply.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='data_source.DataReply.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=63,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['DataRequest'] = _DATAREQUEST
DESCRIPTOR.message_types_by_name['DataReply'] = _DATAREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATAREQUEST,
  '__module__' : 'data_source_pb2'
  # @@protoc_insertion_point(class_scope:data_source.DataRequest)
  })
_sym_db.RegisterMessage(DataRequest)

DataReply = _reflection.GeneratedProtocolMessageType('DataReply', (_message.Message,), {
  'DESCRIPTOR' : _DATAREPLY,
  '__module__' : 'data_source_pb2'
  # @@protoc_insertion_point(class_scope:data_source.DataReply)
  })
_sym_db.RegisterMessage(DataReply)



_DATASOURCE = _descriptor.ServiceDescriptor(
  name='DataSource',
  full_name='data_source.DataSource',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=98,
  serialized_end=175,
  methods=[
  _descriptor.MethodDescriptor(
    name='FetchData',
    full_name='data_source.DataSource.FetchData',
    index=0,
    containing_service=None,
    input_type=_DATAREQUEST,
    output_type=_DATAREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASOURCE)

DESCRIPTOR.services_by_name['DataSource'] = _DATASOURCE

# @@protoc_insertion_point(module_scope)
