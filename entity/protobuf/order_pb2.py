# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PATH/order.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PATH/order.proto',
  package='mapping',
  serialized_pb=_b('\n\x10PATH/order.proto\x12\x07mapping\"\xe7\x01\n\x05Order\x12\x12\n\nidentifier\x18\x01 \x02(\t\x12\x15\n\rcurrency_pair\x18\x02 \x02(\t\x12\x11\n\tdirection\x18\x03 \x02(\t\x12\x0e\n\x06status\x18\x04 \x02(\t\x12\x11\n\ttimestamp\x18\x05 \x02(\x03\x12\x15\n\rinitial_price\x18\x06 \x02(\x02\x12\x14\n\x0c\x66illed_price\x18\x08 \x02(\x02\x12\x16\n\x0einitial_volume\x18\x07 \x02(\x02\x12\x15\n\rfilled_volume\x18\t \x02(\x02\x12\x13\n\x0b\x64\x65scription\x18\n \x02(\t\x12\x0c\n\x04tags\x18\x0b \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='mapping.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='mapping.Order.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_pair', full_name='mapping.Order.currency_pair', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='mapping.Order.direction', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='mapping.Order.status', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='mapping.Order.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_price', full_name='mapping.Order.initial_price', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filled_price', full_name='mapping.Order.filled_price', index=6,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_volume', full_name='mapping.Order.initial_volume', index=7,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filled_volume', full_name='mapping.Order.filled_volume', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='mapping.Order.description', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='mapping.Order.tags', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=261,
)

DESCRIPTOR.message_types_by_name['Order'] = _ORDER

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
  DESCRIPTOR = _ORDER,
  __module__ = 'PATH.order_pb2'
  # @@protoc_insertion_point(class_scope:mapping.Order)
  ))
_sym_db.RegisterMessage(Order)


# @@protoc_insertion_point(module_scope)