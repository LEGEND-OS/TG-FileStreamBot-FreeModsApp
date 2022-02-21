import aiohttp

from urllib3 import Retry

async def user_in_streaam(id: int):

    async with aiohttp.ClientSession() as session:
        url = f'https://streaam.net/dash/check.php?id={id}'
        async with session.get(url) as resp:
            text_resp = await resp.text()
            if text_resp == 'ok':
                return True
            else:
                return False