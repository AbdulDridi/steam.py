# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_cloud.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto

from .steammessages_unified_base import NoResponse


@dataclass
class CCloud_GetUploadServerInfo_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)


@dataclass
class CCloud_GetUploadServerInfo_Response(betterproto.Message):
    server_url: str = betterproto.string_field(1)


@dataclass
class CCloud_BeginHTTPUpload_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    file_size: int = betterproto.uint32_field(2)
    filename: str = betterproto.string_field(3)
    file_sha: str = betterproto.string_field(4)
    is_public: bool = betterproto.bool_field(5)
    platforms_to_sync: List[str] = betterproto.string_field(6)
    request_headers_names: List[str] = betterproto.string_field(7)
    request_headers_values: List[str] = betterproto.string_field(8)


@dataclass
class CCloud_BeginHTTPUpload_Response(betterproto.Message):
    ugcid: float = betterproto.fixed64_field(1)
    timestamp: float = betterproto.fixed32_field(2)
    url_host: str = betterproto.string_field(3)
    url_path: str = betterproto.string_field(4)
    use_https: bool = betterproto.bool_field(5)
    request_headers: List[
        "CCloud_BeginHTTPUpload_ResponseHTTPHeaders"
    ] = betterproto.message_field(6)


@dataclass
class CCloud_BeginHTTPUpload_ResponseHTTPHeaders(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CCloud_CommitHTTPUpload_Request(betterproto.Message):
    transfer_succeeded: bool = betterproto.bool_field(1)
    appid: int = betterproto.uint32_field(2)
    file_sha: str = betterproto.string_field(3)
    filename: str = betterproto.string_field(4)


@dataclass
class CCloud_CommitHTTPUpload_Response(betterproto.Message):
    file_committed: bool = betterproto.bool_field(1)


@dataclass
class CCloud_GetFileDetails_Request(betterproto.Message):
    ugcid: int = betterproto.uint64_field(1)
    appid: int = betterproto.uint32_field(2)


@dataclass
class CCloud_UserFile(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    ugcid: int = betterproto.uint64_field(2)
    filename: str = betterproto.string_field(3)
    timestamp: int = betterproto.uint64_field(4)
    file_size: int = betterproto.uint32_field(5)
    url: str = betterproto.string_field(6)
    steamid_creator: float = betterproto.fixed64_field(7)
    flags: int = betterproto.uint32_field(8)
    platforms_to_sync: List[str] = betterproto.string_field(9)
    file_sha: str = betterproto.string_field(10)


@dataclass
class CCloud_GetFileDetails_Response(betterproto.Message):
    details: "CCloud_UserFile" = betterproto.message_field(1)


@dataclass
class CCloud_EnumerateUserFiles_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    extended_details: bool = betterproto.bool_field(2)
    count: int = betterproto.uint32_field(3)
    start_index: int = betterproto.uint32_field(4)


@dataclass
class CCloud_EnumerateUserFiles_Response(betterproto.Message):
    files: List["CCloud_UserFile"] = betterproto.message_field(1)
    total_files: int = betterproto.uint32_field(2)


@dataclass
class CCloud_Delete_Request(betterproto.Message):
    filename: str = betterproto.string_field(1)
    appid: int = betterproto.uint32_field(2)


@dataclass
class CCloud_Delete_Response(betterproto.Message):
    pass


@dataclass
class CCloud_GetClientEncryptionKey_Request(betterproto.Message):
    pass


@dataclass
class CCloud_GetClientEncryptionKey_Response(betterproto.Message):
    key: bytes = betterproto.bytes_field(1)
    crc: int = betterproto.int32_field(2)


@dataclass
class CCloud_CDNReport_Notification(betterproto.Message):
    steamid: float = betterproto.fixed64_field(1)
    url: str = betterproto.string_field(2)
    success: bool = betterproto.bool_field(3)
    http_status_code: int = betterproto.uint32_field(4)
    expected_bytes: int = betterproto.uint64_field(5)
    received_bytes: int = betterproto.uint64_field(6)
    duration: int = betterproto.uint32_field(7)


@dataclass
class CCloud_ExternalStorageTransferReport_Notification(betterproto.Message):
    host: str = betterproto.string_field(1)
    path: str = betterproto.string_field(2)
    is_upload: bool = betterproto.bool_field(3)
    success: bool = betterproto.bool_field(4)
    http_status_code: int = betterproto.uint32_field(5)
    bytes_expected: int = betterproto.uint64_field(6)
    bytes_actual: int = betterproto.uint64_field(7)
    duration_ms: int = betterproto.uint32_field(8)
    cellid: int = betterproto.uint32_field(9)
    proxied: bool = betterproto.bool_field(10)
    ipv6_local: bool = betterproto.bool_field(11)
    ipv6_remote: bool = betterproto.bool_field(12)


@dataclass
class CCloud_ClientBeginFileUpload_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    file_size: int = betterproto.uint32_field(2)
    raw_file_size: int = betterproto.uint32_field(3)
    file_sha: bytes = betterproto.bytes_field(4)
    time_stamp: int = betterproto.uint64_field(5)
    filename: str = betterproto.string_field(6)
    platforms_to_sync: int = betterproto.uint32_field(7)
    cell_id: int = betterproto.uint32_field(9)
    can_encrypt: bool = betterproto.bool_field(10)
    is_shared_file: bool = betterproto.bool_field(11)
    realm: int = betterproto.uint32_field(12)


@dataclass
class ClientCloudFileUploadBlockDetails(betterproto.Message):
    url_host: str = betterproto.string_field(1)
    url_path: str = betterproto.string_field(2)
    use_https: bool = betterproto.bool_field(3)
    http_method: int = betterproto.int32_field(4)
    request_headers: List[
        "ClientCloudFileUploadBlockDetailsHTTPHeaders"
    ] = betterproto.message_field(5)
    block_offset: int = betterproto.uint64_field(6)
    block_length: int = betterproto.uint32_field(7)
    explicit_body_data: bytes = betterproto.bytes_field(8)
    may_parallelize: bool = betterproto.bool_field(9)


@dataclass
class ClientCloudFileUploadBlockDetailsHTTPHeaders(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CCloud_ClientBeginFileUpload_Response(betterproto.Message):
    encrypt_file: bool = betterproto.bool_field(1)
    block_requests: List[
        "ClientCloudFileUploadBlockDetails"
    ] = betterproto.message_field(2)


@dataclass
class CCloud_ClientCommitFileUpload_Request(betterproto.Message):
    transfer_succeeded: bool = betterproto.bool_field(1)
    appid: int = betterproto.uint32_field(2)
    file_sha: bytes = betterproto.bytes_field(3)
    filename: str = betterproto.string_field(4)


@dataclass
class CCloud_ClientCommitFileUpload_Response(betterproto.Message):
    file_committed: bool = betterproto.bool_field(1)


@dataclass
class CCloud_ClientFileDownload_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    filename: str = betterproto.string_field(2)
    realm: int = betterproto.uint32_field(3)


@dataclass
class CCloud_ClientFileDownload_Response(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    file_size: int = betterproto.uint32_field(2)
    raw_file_size: int = betterproto.uint32_field(3)
    sha_file: bytes = betterproto.bytes_field(4)
    time_stamp: int = betterproto.uint64_field(5)
    is_explicit_delete: bool = betterproto.bool_field(6)
    url_host: str = betterproto.string_field(7)
    url_path: str = betterproto.string_field(8)
    use_https: bool = betterproto.bool_field(9)
    request_headers: List[
        "CCloud_ClientFileDownload_ResponseHTTPHeaders"
    ] = betterproto.message_field(10)
    encrypted: bool = betterproto.bool_field(11)


@dataclass
class CCloud_ClientFileDownload_ResponseHTTPHeaders(betterproto.Message):
    name: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass
class CCloud_ClientDeleteFile_Request(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    filename: str = betterproto.string_field(2)
    is_explicit_delete: bool = betterproto.bool_field(3)


@dataclass
class CCloud_ClientDeleteFile_Response(betterproto.Message):
    pass


@dataclass
class CCloud_ClientConflictResolution_Notification(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    chose_local_files: bool = betterproto.bool_field(2)


@dataclass
class CCloud_EnumerateUserApps_Request(betterproto.Message):
    pass


@dataclass
class CCloud_EnumerateUserApps_Response(betterproto.Message):
    apps: List["CCloud_EnumerateUserApps_ResponseApps"] = betterproto.message_field(1)


@dataclass
class CCloud_EnumerateUserApps_ResponseApps(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    totalcount: int = betterproto.int32_field(2)
    totalsize: int = betterproto.int64_field(3)


class CloudStub(betterproto.ServiceStub):
    async def get_upload_server_info(
        self, *, appid: int = 0
    ) -> CCloud_GetUploadServerInfo_Response:
        request = CCloud_GetUploadServerInfo_Request()
        request.appid = appid

        return await self._unary_unary(
            "/.Cloud/GetUploadServerInfo", request, CCloud_GetUploadServerInfo_Response,
        )

    async def begin_http_upload(
        self,
        *,
        appid: int = 0,
        file_size: int = 0,
        filename: str = "",
        file_sha: str = "",
        is_public: bool = False,
        platforms_to_sync: List[str] = [],
        request_headers_names: List[str] = [],
        request_headers_values: List[str] = [],
    ) -> CCloud_BeginHTTPUpload_Response:
        request = CCloud_BeginHTTPUpload_Request()
        request.appid = appid
        request.file_size = file_size
        request.filename = filename
        request.file_sha = file_sha
        request.is_public = is_public
        request.platforms_to_sync = platforms_to_sync
        request.request_headers_names = request_headers_names
        request.request_headers_values = request_headers_values

        return await self._unary_unary(
            "/.Cloud/BeginHTTPUpload", request, CCloud_BeginHTTPUpload_Response,
        )

    async def commit_http_upload(
        self,
        *,
        transfer_succeeded: bool = False,
        appid: int = 0,
        file_sha: str = "",
        filename: str = "",
    ) -> CCloud_CommitHTTPUpload_Response:
        request = CCloud_CommitHTTPUpload_Request()
        request.transfer_succeeded = transfer_succeeded
        request.appid = appid
        request.file_sha = file_sha
        request.filename = filename

        return await self._unary_unary(
            "/.Cloud/CommitHTTPUpload", request, CCloud_CommitHTTPUpload_Response,
        )

    async def get_file_details(
        self, *, ugcid: int = 0, appid: int = 0
    ) -> CCloud_GetFileDetails_Response:
        request = CCloud_GetFileDetails_Request()
        request.ugcid = ugcid
        request.appid = appid

        return await self._unary_unary(
            "/.Cloud/GetFileDetails", request, CCloud_GetFileDetails_Response,
        )

    async def enumerate_user_files(
        self,
        *,
        appid: int = 0,
        extended_details: bool = False,
        count: int = 0,
        start_index: int = 0,
    ) -> CCloud_EnumerateUserFiles_Response:
        request = CCloud_EnumerateUserFiles_Request()
        request.appid = appid
        request.extended_details = extended_details
        request.count = count
        request.start_index = start_index

        return await self._unary_unary(
            "/.Cloud/EnumerateUserFiles", request, CCloud_EnumerateUserFiles_Response,
        )

    async def delete(
        self, *, filename: str = "", appid: int = 0
    ) -> CCloud_Delete_Response:
        request = CCloud_Delete_Request()
        request.filename = filename
        request.appid = appid

        return await self._unary_unary(
            "/.Cloud/Delete", request, CCloud_Delete_Response,
        )

    async def get_client_encryption_key(self) -> CCloud_GetClientEncryptionKey_Response:
        request = CCloud_GetClientEncryptionKey_Request()

        return await self._unary_unary(
            "/.Cloud/GetClientEncryptionKey",
            request,
            CCloud_GetClientEncryptionKey_Response,
        )

    async def cdn_report(
        self,
        *,
        steamid: float = 0,
        url: str = "",
        success: bool = False,
        http_status_code: int = 0,
        expected_bytes: int = 0,
        received_bytes: int = 0,
        duration: int = 0,
    ) -> NoResponse:
        request = CCloud_CDNReport_Notification()
        request.steamid = steamid
        request.url = url
        request.success = success
        request.http_status_code = http_status_code
        request.expected_bytes = expected_bytes
        request.received_bytes = received_bytes
        request.duration = duration

        return await self._unary_unary("/.Cloud/CDNReport", request, NoResponse,)

    async def external_storage_transfer_report(
        self,
        *,
        host: str = "",
        path: str = "",
        is_upload: bool = False,
        success: bool = False,
        http_status_code: int = 0,
        bytes_expected: int = 0,
        bytes_actual: int = 0,
        duration_ms: int = 0,
        cellid: int = 0,
        proxied: bool = False,
        ipv6_local: bool = False,
        ipv6_remote: bool = False,
    ) -> NoResponse:
        request = CCloud_ExternalStorageTransferReport_Notification()
        request.host = host
        request.path = path
        request.is_upload = is_upload
        request.success = success
        request.http_status_code = http_status_code
        request.bytes_expected = bytes_expected
        request.bytes_actual = bytes_actual
        request.duration_ms = duration_ms
        request.cellid = cellid
        request.proxied = proxied
        request.ipv6_local = ipv6_local
        request.ipv6_remote = ipv6_remote

        return await self._unary_unary(
            "/.Cloud/ExternalStorageTransferReport", request, NoResponse,
        )

    async def client_begin_file_upload(
        self,
        *,
        appid: int = 0,
        file_size: int = 0,
        raw_file_size: int = 0,
        file_sha: bytes = b"",
        time_stamp: int = 0,
        filename: str = "",
        platforms_to_sync: int = 0,
        cell_id: int = 0,
        can_encrypt: bool = False,
        is_shared_file: bool = False,
        realm: int = 0,
    ) -> CCloud_ClientBeginFileUpload_Response:
        request = CCloud_ClientBeginFileUpload_Request()
        request.appid = appid
        request.file_size = file_size
        request.raw_file_size = raw_file_size
        request.file_sha = file_sha
        request.time_stamp = time_stamp
        request.filename = filename
        request.platforms_to_sync = platforms_to_sync
        request.cell_id = cell_id
        request.can_encrypt = can_encrypt
        request.is_shared_file = is_shared_file
        request.realm = realm

        return await self._unary_unary(
            "/.Cloud/ClientBeginFileUpload",
            request,
            CCloud_ClientBeginFileUpload_Response,
        )

    async def client_commit_file_upload(
        self,
        *,
        transfer_succeeded: bool = False,
        appid: int = 0,
        file_sha: bytes = b"",
        filename: str = "",
    ) -> CCloud_ClientCommitFileUpload_Response:
        request = CCloud_ClientCommitFileUpload_Request()
        request.transfer_succeeded = transfer_succeeded
        request.appid = appid
        request.file_sha = file_sha
        request.filename = filename

        return await self._unary_unary(
            "/.Cloud/ClientCommitFileUpload",
            request,
            CCloud_ClientCommitFileUpload_Response,
        )

    async def client_file_download(
        self, *, appid: int = 0, filename: str = "", realm: int = 0
    ) -> CCloud_ClientFileDownload_Response:
        request = CCloud_ClientFileDownload_Request()
        request.appid = appid
        request.filename = filename
        request.realm = realm

        return await self._unary_unary(
            "/.Cloud/ClientFileDownload", request, CCloud_ClientFileDownload_Response,
        )

    async def client_delete_file(
        self, *, appid: int = 0, filename: str = "", is_explicit_delete: bool = False
    ) -> CCloud_ClientDeleteFile_Response:
        request = CCloud_ClientDeleteFile_Request()
        request.appid = appid
        request.filename = filename
        request.is_explicit_delete = is_explicit_delete

        return await self._unary_unary(
            "/.Cloud/ClientDeleteFile", request, CCloud_ClientDeleteFile_Response,
        )

    async def client_conflict_resolution(
        self, *, appid: int = 0, chose_local_files: bool = False
    ) -> NoResponse:
        request = CCloud_ClientConflictResolution_Notification()
        request.appid = appid
        request.chose_local_files = chose_local_files

        return await self._unary_unary(
            "/.Cloud/ClientConflictResolution", request, NoResponse,
        )

    async def enumerate_user_apps(self) -> CCloud_EnumerateUserApps_Response:
        request = CCloud_EnumerateUserApps_Request()

        return await self._unary_unary(
            "/.Cloud/EnumerateUserApps", request, CCloud_EnumerateUserApps_Response,
        )
