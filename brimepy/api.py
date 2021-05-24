import aiohttp
import asyncio
from asyncio import ProactorEventLoop
from typing import Optional

BRIME_API: str = "https://api-staging.brimelive.com/v1"


class API:

    def __init__(self, client_auth: str, loop: Optional[ProactorEventLoop] = None):
        """
        Brime API client

        :param str client_auth: Secret client token (ID) required to access the API.
        :param ProactorEventLoop loop: Asyncio event loop, defaults to None if not set and created upon initialization.
        """
        self.client_auth = client_auth
        self._loop = asyncio.get_event_loop() if loop is None else loop
        self.session = aiohttp.ClientSession(loop=self._loop)

    async def _get(self, url: str) -> dict:
        """
        Sends a GET request to the specified URL.

        :param str url: The target URL to send GET request.
        :return: Returns the json response received.
        :rtype: dict
        """
        async with self.session.get(url) as response:
            resp = await response.json()
            return resp

    async def _post(self, url: str) -> dict:
        """
        Sends a POST request to the specified URL.

        :param str url: The target URL to send GET request.
        :return: Returns the json response received.
        :rtype: dict
        """
        async with self.session.get(url) as response:
            resp = await response.json()
            return resp

    async def user(self, username: str) -> dict:
        """
        Returns the users information. Requires special access.

        :param str username: Username of the account.
        :rtype: dict
        """
        url = BRIME_API + f'/user/{username}?client_id={self.client_auth}'
        return await self._get(url)

    async def user_following(self, username: str) -> dict:
        """
        Returns a users followers. Requires special access.

        :param str username: Username of the account.
        :rtype: dict
        """
        url = BRIME_API + f'/user/{username}/following?client_id={self.client_auth}'
        return await self._get(url)

    async def user_clips(self, username: str) -> dict:
        """
        Returns a users clips. Requires special access.

        :param str username: Username of the account.
        :rtype: dict
        """
        url = BRIME_API + f'/user/{username}/clips?client_id={self.client_auth}'
        return await self._get(url)

    async def users(self) -> dict:
        """
        Returns the total number of registered users.

        :rtype: dict
        """
        url = BRIME_API + f'/users?client_id={self.client_auth}'
        return await self._get(url)

    async def channel(self, channel: str) -> dict:
        """
        Returns the channel's information.

        :param str channel: Username of the channel.
        :rtype: dict
        """
        url = BRIME_API + f'/channel/{channel}?client_id={self.client_auth}'
        return await self._get(url)

    async def channel_subs(self, channel: str) -> dict:
        """
        Returns the channel's subscribers.

        :param str channel: Username of the channel.
        :rtype: dict
        """
        url = BRIME_API + f'/channel/{channel}/subcheck?client_id={self.client_auth}'
        return await self._get(url)

    async def streams(self) -> dict:
        """
        Queries for all streams that are currently live and returns them.
        :rtype: dict
        """
        url = BRIME_API + f'/streams?client_id={self.client_auth}'
        return await self._get(url)

    async def stream(self, channel: str) -> dict:
        """
        Queries for a stream by the given channel and returns the data for that stream.

        :param str channel: Username of the channel.
        :rtype: dict
        """
        url = BRIME_API + f'/stream/{channel}?client_id={self.client_auth}'
        return await self._get(url)

    async def clip_info(self, clip_id: str) -> dict:
        """
        Returns information about the specified clip.

        :param str clip_id: Alphanumeric ID of the clip.
        :rtype: dict
        """
        url = BRIME_API + f'/clip/{clip_id}?client_id={self.client_auth}'
        return await self._get(url)

    async def channel_clips(self, channel_id: str, since: float = 0, limit: int = 50, skip: int = 0, sort: str = 'desc') -> dict:
        """
        Queries a channel for clips and returns them.

        :param str channel_id: Alphanumeric ID of the channel.
        :param float since: Epoch timestamp. Default: 0
        :param int limit: Number of vods to return. Default: 50, Max: 150
        :param int skip: Number of clips to skip over. Default: 0
        :param str sort: Method of sorting to use. asc: Old -> New, desc: New -> Old
        :rtype: dict
        """
        url = BRIME_API + f'/channel/{channel_id}/clips?client_id={self.client_auth}' \
                          f'&since={since}&limit={limit}&skip={skip}&sort={sort}'
        return await self._get(url)

    async def create_clip(self, channel: str) -> dict:
        """
        Creates a clip for the specified channel.

        :param str channel: Username of the channel.
        :rtype: dict
        """
        url = BRIME_API + f'/clip/{channel}/create?client_id={self.client_auth}'
        return await self._post(url)

    async def vod_info(self, vod_id: str) -> dict:
        """
        Queries the specified vod id and returns its information.

        :param str vod_id: Alphanumeric ID of the vod.
        :rtype: dict
        """
        url = BRIME_API + f'channel/{vod_id}?client_id={self.client_auth}'
        return await self._post(url)

    async def channel_vod(self, channel_id: str, limit: int = 50, skip: int = 0, sort: str = 'desc') -> dict:
        """
        Queries for vods associated with the channel id.

        :param str channel_id: Alphanumeric ID of the channel.
        :param int limit: Number of vods to return. Default: 50, Max: 150
        :param int skip: Number of clips to skip over. Default: 0
        :param str sort: Method of sorting to use. asc: Old -> New, desc: New -> Old
        :rtype: dict
        """
        url = BRIME_API + f'/channel/{channel_id}/vods?client_id={self.client_auth}' \
                          f'&limit={limit}&skip={skip}&sort={sort}'
        return await self._get(url)

    async def categories(self) -> dict:
        """
        Returns all streams that are live sorted into categories.

        :rtype: dict
        """
        url = BRIME_API + f'/categories/live?client_id={self.client_auth}'
        return await self._get(url)

    async def category(self, category: str) -> dict:
        """
        Returns all streams that are live in a specified category.

        :param str category: Name of the category.
        :rtype: dict
        """
        url = BRIME_API + f'/category/{category}/live?client_id={self.client_auth}'
        return await self._get(url)

    async def cateogry_info(self, category: str) -> dict:
        """
        Returns information about the specific category.

        :param str category: Name of the category.
        :rtype: dict
        """
        url = BRIME_API + f'/category/{category}?client_id={self.client_auth}'
        return await self._get(url)

    async def global_emotes(self) -> dict:
        """
        Returns all emotes enabled globally.

        :rtype: dict
        """
        url = BRIME_API + f'/emotesets?client_id={self.client_auth}'
        return await self._get(url)

    async def emote_sets(self, emote_set: str) -> dict:
        """
        Returns emotes associated with a specific set.

        :param str emote_set: Name of the emote set.
        :rtype: dict
        """
        url = BRIME_API + f'/emotesets/{emote_set}?client_id={self.client_auth}'
        return await self._get(url)

    async def channel_emotes(self, channel: str) -> dict:
        """
        Returns emotes associated with the specified channel.

        :param str channel: Username of the channel.
        :rtype: dict
        """
        url = BRIME_API + f'/channel/{channel}/emotes?client_id={self.client_auth}'
        return await self._get(url)

    async def close(self):
        self.session.close()
