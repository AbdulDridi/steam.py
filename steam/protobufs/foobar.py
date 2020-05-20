# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: gc.proto
# plugin: python-betterproto

from dataclasses import dataclass

import betterproto


class GCProtoBufMsgSrc(betterproto.Enum):
    GCProtoBufMsgSrc_Unspecified = 0
    GCProtoBufMsgSrc_FromSystem = 1
    GCProtoBufMsgSrc_FromSteamID = 2
    GCProtoBufMsgSrc_FromGC = 3
    GCProtoBufMsgSrc_ReplySystem = 4


@dataclass
class CMsgProtoBufHeader(betterproto.Message):
    client_steam_id: float = betterproto.fixed64_field(1)
    client_session_id: int = betterproto.int32_field(2)
    source_app_id: int = betterproto.uint32_field(3)
    job_id_source: float = betterproto.fixed64_field(10)
    job_id_target: float = betterproto.fixed64_field(11)
    target_job_name: str = betterproto.string_field(12)
    eresult: int = betterproto.int32_field(13)
    error_message: str = betterproto.string_field(14)
    gc_msg_src: "GCProtoBufMsgSrc" = betterproto.enum_field(200)
    gc_dir_index_source: int = betterproto.uint32_field(201)
