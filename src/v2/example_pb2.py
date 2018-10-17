# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2/example.proto',
  package='devision.example.v2',
  syntax='proto3',
  serialized_pb=_b('\n\x10v2/example.proto\x12\x13\x64\x65vision.example.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"#\n\x13ListCbrRatesRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"C\n\x14ListCbrRatesResponse\x12+\n\x05rates\x18\x01 \x03(\x0b\x32\x1c.devision.example.v2.CbrRate\"F\n\x07\x43\x62rRate\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x11\n\tchar_code\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x02\x12\x0c\n\x04name\x18\x04 \x01(\t\" \n\rGetMeResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x32\x97\x01\n\x0c\x43urrencyRate\x12\x86\x01\n\x0cListCbrRates\x12(.devision.example.v2.ListCbrRatesRequest\x1a).devision.example.v2.ListCbrRatesResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/v2/currency-rates/get:\x01*2c\n\x04User\x12[\n\x05GetMe\x12\x16.google.protobuf.Empty\x1a\".devision.example.v2.GetMeResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0b/v2/user/me:\x01*BA\n\x16io.devision.example.v2B\x0c\x45xampleProtoP\x01\x88\x01\x01\xca\x02\x13\x44\x65vision\\Example\\V2b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_LISTCBRRATESREQUEST = _descriptor.Descriptor(
  name='ListCbrRatesRequest',
  full_name='devision.example.v2.ListCbrRatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='devision.example.v2.ListCbrRatesRequest.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=135,
)


_LISTCBRRATESRESPONSE = _descriptor.Descriptor(
  name='ListCbrRatesResponse',
  full_name='devision.example.v2.ListCbrRatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rates', full_name='devision.example.v2.ListCbrRatesResponse.rates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=204,
)


_CBRRATE = _descriptor.Descriptor(
  name='CbrRate',
  full_name='devision.example.v2.CbrRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='devision.example.v2.CbrRate.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='char_code', full_name='devision.example.v2.CbrRate.char_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate', full_name='devision.example.v2.CbrRate.rate', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='devision.example.v2.CbrRate.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=276,
)


_GETMERESPONSE = _descriptor.Descriptor(
  name='GetMeResponse',
  full_name='devision.example.v2.GetMeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='devision.example.v2.GetMeResponse.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=310,
)

_LISTCBRRATESRESPONSE.fields_by_name['rates'].message_type = _CBRRATE
DESCRIPTOR.message_types_by_name['ListCbrRatesRequest'] = _LISTCBRRATESREQUEST
DESCRIPTOR.message_types_by_name['ListCbrRatesResponse'] = _LISTCBRRATESRESPONSE
DESCRIPTOR.message_types_by_name['CbrRate'] = _CBRRATE
DESCRIPTOR.message_types_by_name['GetMeResponse'] = _GETMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListCbrRatesRequest = _reflection.GeneratedProtocolMessageType('ListCbrRatesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCBRRATESREQUEST,
  __module__ = 'v2.example_pb2'
  # @@protoc_insertion_point(class_scope:devision.example.v2.ListCbrRatesRequest)
  ))
_sym_db.RegisterMessage(ListCbrRatesRequest)

ListCbrRatesResponse = _reflection.GeneratedProtocolMessageType('ListCbrRatesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTCBRRATESRESPONSE,
  __module__ = 'v2.example_pb2'
  # @@protoc_insertion_point(class_scope:devision.example.v2.ListCbrRatesResponse)
  ))
_sym_db.RegisterMessage(ListCbrRatesResponse)

CbrRate = _reflection.GeneratedProtocolMessageType('CbrRate', (_message.Message,), dict(
  DESCRIPTOR = _CBRRATE,
  __module__ = 'v2.example_pb2'
  # @@protoc_insertion_point(class_scope:devision.example.v2.CbrRate)
  ))
_sym_db.RegisterMessage(CbrRate)

GetMeResponse = _reflection.GeneratedProtocolMessageType('GetMeResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETMERESPONSE,
  __module__ = 'v2.example_pb2'
  # @@protoc_insertion_point(class_scope:devision.example.v2.GetMeResponse)
  ))
_sym_db.RegisterMessage(GetMeResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026io.devision.example.v2B\014ExampleProtoP\001\210\001\001\312\002\023Devision\\Example\\V2'))

_CURRENCYRATE = _descriptor.ServiceDescriptor(
  name='CurrencyRate',
  full_name='devision.example.v2.CurrencyRate',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=313,
  serialized_end=464,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListCbrRates',
    full_name='devision.example.v2.CurrencyRate.ListCbrRates',
    index=0,
    containing_service=None,
    input_type=_LISTCBRRATESREQUEST,
    output_type=_LISTCBRRATESRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\033\"\026/v2/currency-rates/get:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CURRENCYRATE)

DESCRIPTOR.services_by_name['CurrencyRate'] = _CURRENCYRATE


_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='devision.example.v2.User',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=466,
  serialized_end=565,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMe',
    full_name='devision.example.v2.User.GetMe',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETMERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\020\"\013/v2/user/me:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)
