# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_gameservers.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CGameServers_GetServerList_Request(betterproto.Message):
    filter: str = betterproto.string_field(1)
    limit: int = betterproto.uint32_field(2)


@dataclass
class CGameServers_GetServerList_Response(betterproto.Message):
    servers: List[
        "CGameServers_GetServerList_ResponseServer"
    ] = betterproto.message_field(1)


@dataclass
class CGameServers_GetServerList_ResponseServer(betterproto.Message):
    addr: str = betterproto.string_field(1)
    gameport: int = betterproto.uint32_field(2)
    specport: int = betterproto.uint32_field(3)
    steamid: float = betterproto.fixed64_field(4)
    name: str = betterproto.string_field(5)
    appid: int = betterproto.uint32_field(6)
    gamedir: str = betterproto.string_field(7)
    version: str = betterproto.string_field(8)
    product: str = betterproto.string_field(9)
    region: int = betterproto.int32_field(10)
    players: int = betterproto.int32_field(11)
    max_players: int = betterproto.int32_field(12)
    bots: int = betterproto.int32_field(13)
    map: str = betterproto.string_field(14)
    secure: bool = betterproto.bool_field(15)
    dedicated: bool = betterproto.bool_field(16)
    os: str = betterproto.string_field(17)
    gametype: str = betterproto.string_field(18)


@dataclass
class CGameServers_GetServerSteamIDsByIP_Request(betterproto.Message):
    server_ips: List[str] = betterproto.string_field(1)


@dataclass
class CGameServers_IPsWithSteamIDs_Response(betterproto.Message):
    servers: List[
        "CGameServers_IPsWithSteamIDs_ResponseServer"
    ] = betterproto.message_field(1)


@dataclass
class CGameServers_IPsWithSteamIDs_ResponseServer(betterproto.Message):
    addr: str = betterproto.string_field(1)
    steamid: float = betterproto.fixed64_field(2)


@dataclass
class CGameServers_GetServerIPsBySteamID_Request(betterproto.Message):
    server_steamids: List[float] = betterproto.fixed64_field(1)


class GameServersStub(betterproto.ServiceStub):
    async def get_server_list(
        self, *, filter: str = "", limit: int = 0
    ) -> CGameServers_GetServerList_Response:
        request = CGameServers_GetServerList_Request()
        request.filter = filter
        request.limit = limit

        return await self._unary_unary(
            "/.GameServers/GetServerList", request, CGameServers_GetServerList_Response,
        )

    async def get_server_steam_ids_by_ip(
        self, *, server_ips: List[str] = []
    ) -> CGameServers_IPsWithSteamIDs_Response:
        request = CGameServers_GetServerSteamIDsByIP_Request()
        request.server_ips = server_ips

        return await self._unary_unary(
            "/.GameServers/GetServerSteamIDsByIP",
            request,
            CGameServers_IPsWithSteamIDs_Response,
        )

    async def get_server_ips_by_steam_id(
        self, *, server_steamids: List[float] = []
    ) -> CGameServers_IPsWithSteamIDs_Response:
        request = CGameServers_GetServerIPsBySteamID_Request()
        request.server_steamids = server_steamids

        return await self._unary_unary(
            "/.GameServers/GetServerIPsBySteamID",
            request,
            CGameServers_IPsWithSteamIDs_Response,
        )
