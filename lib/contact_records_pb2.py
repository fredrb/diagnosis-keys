# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contact_records.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contact_records.proto',
  package='gms.en',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x63ontact_records.proto\x12\x06gms.en\":\n\nScanRecord\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x0c\n\x04rssi\x18\x03 \x01(\x03\x12\x0b\n\x03\x61\x65m\x18\x04 \x01(\x0c\"8\n\x0e\x43ontactRecords\x12&\n\nscanrecord\x18\x01 \x03(\x0b\x32\x12.gms.en.ScanRecord'
)




_SCANRECORD = _descriptor.Descriptor(
  name='ScanRecord',
  full_name='gms.en.ScanRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='gms.en.ScanRecord.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='gms.en.ScanRecord.rssi', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aem', full_name='gms.en.ScanRecord.aem', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=91,
)


_CONTACTRECORDS = _descriptor.Descriptor(
  name='ContactRecords',
  full_name='gms.en.ContactRecords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scanrecord', full_name='gms.en.ContactRecords.scanrecord', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=149,
)

_CONTACTRECORDS.fields_by_name['scanrecord'].message_type = _SCANRECORD
DESCRIPTOR.message_types_by_name['ScanRecord'] = _SCANRECORD
DESCRIPTOR.message_types_by_name['ContactRecords'] = _CONTACTRECORDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanRecord = _reflection.GeneratedProtocolMessageType('ScanRecord', (_message.Message,), {
  'DESCRIPTOR' : _SCANRECORD,
  '__module__' : 'contact_records_pb2'
  # @@protoc_insertion_point(class_scope:gms.en.ScanRecord)
  })
_sym_db.RegisterMessage(ScanRecord)

ContactRecords = _reflection.GeneratedProtocolMessageType('ContactRecords', (_message.Message,), {
  'DESCRIPTOR' : _CONTACTRECORDS,
  '__module__' : 'contact_records_pb2'
  # @@protoc_insertion_point(class_scope:gms.en.ContactRecords)
  })
_sym_db.RegisterMessage(ContactRecords)


# @@protoc_insertion_point(module_scope)
