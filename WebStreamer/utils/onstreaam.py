import aiohttp

async def user_in_streaam(id: int):
    async with aiohttp.ClientSession() as session:
        url = f'https://streaam.net/dash/check.php'
        params = {'id': id}

        async with session.get(url, params=params) as resp:
            text_resp = await resp.text()
            if text_resp == 'ok':
                return True
            else:
                return False