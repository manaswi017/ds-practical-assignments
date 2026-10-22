from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    7,
    35,
    1,
    '',
    'chat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\"!\n\x0eMessageRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1d\n\x0cMessageReply\x12\r\n\x05reply\x18\x01 \x01(\t2<\n\x0b\x43hatService\x12-\n\x0bSendMessage\x12\x0f.MessageRequest\x1a\r.MessageReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEREQUEST']._serialized_start=14
  _globals['_MESSAGEREQUEST']._serialized_end=47
  _globals['_MESSAGEREPLY']._serialized_start=49
  _globals['_MESSAGEREPLY']._serialized_end=78
  _globals['_CHATSERVICE']._serialized_start=80
  _globals['_CHATSERVICE']._serialized_end=140
# @@protoc_insertion_point(module_scope)
