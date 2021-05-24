import aiohttp
import asyncio
from typing import Optional

BRIME_API: str = "https://api-staging.brimelive.com/v1"


class API:

    def __init__(self, base_url: str, client_auth: str, loop: Optional[str] = None):
        self.base_url = base_url
        self.client_auth = client_auth
        self._loop = asyncio.get_event_loop() if loop is None else loop
        self.session = aiohttp.ClientSession(loop=self._loop)

    async def _get(self, url):
        async with self.session.get(url) as response:
            resp = await response.json()
            return resp

    async def _post(self, url):
        async with self.session.get(url) as response:
            resp = await response.json()
            return resp

    async def user(self, username):
        url = BRIME_API + f'/user/{username}?client_id={self.client_auth}'
        return await self._get(url)

    async def user_following(self, username):
        url = BRIME_API + f'/user/{username}/following?client_id={self.client_auth}'
        return await self._get(url)

    async def user_clips(self, username):
        url = BRIME_API + f'/user/{username}/clips?client_id={self.client_auth}'
        return await self._get(url)

    async def users(self):
        url = BRIME_API + f'/users?client_id={self.client_auth}'
        return await self._get(url)

    async def channel(self, channel):
        url = BRIME_API + f'/channel/{channel}?client_id={self.client_auth}'
        return await self._get(url)

    async def channel_subs(self, channel):
        url = BRIME_API + f'/channel/{channel}/subcheck?client_id={self.client_auth}'
        return await self._get(url)

    async def streams(self):
        url = BRIME_API + f'/streams?client_id={self.client_auth}'
        return await self._get(url)

    async def stream(self, channel):
        url = BRIME_API + f'/stream/{channel}?client_id={self.client_auth}'
        return await self._get(url)

    async def clip_info(self, clip_id):
        url = BRIME_API + f'/clip/{clip_id}?client_id={self.client_auth}'
        return await self._get(url)

    async def channel_clips(self, channel_id, since, limit, skip, sort):
        url = BRIME_API + f'/channel/{channel_id}/clips?client_id={self.client_auth}' \
                          f'&since={since}&limit={limit}&skip={skip}&sort={sort}'
        return await self._get(url)

    async def create_clip(self, channel):
        url = BRIME_API + f'/clip/{channel}/create?client_id={self.client_auth}'
        return await self._post(url)

    async def vod_info(self, vod_id):
        url = BRIME_API + f'channel/{vod_id}?client_id={self.client_auth}'
        return await self._post(url)

    async def channel_vod(self, channel_id, limit, skip, sort):
        url = BRIME_API + f'/channel/{channel_id}/vods?client_id={self.client_auth}' \
                          f'&limit={limit}&skip={skip}&sort={sort}'
        return await self._get(url)
