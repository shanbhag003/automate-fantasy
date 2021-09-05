import asyncio
import aiohttp
import os
from datetime import datetime, timedelta
import pandas as pd
from fpl import FPL

from update_team import update

os.environ['EMAIL'] = 'kshanbhag231@gmail.com'
os.environ['PASSWORD'] = 'leomessi*01'
os.environ['USER_ID'] = '1462218'


async def check_update():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        gw = await fpl.get_gameweeks(return_json=True)
        df = pd.DataFrame(gw)
        today = datetime.now()
        tomorrow=(today + timedelta(days=3)).timestamp()
        today = today.timestamp()
        df = df.loc[df.deadline_time_epoch>today]
        deadline = df.iloc[0].deadline_time_epoch
        return deadline<tomorrow

if __name__ == "__main__":
    if asyncio.run(check_update()):
        email=os.environ.get('EMAIL')
        password=os.environ.get('PASSWORD')
        user_id=os.environ.get('USER_ID')
        asyncio.run(update(email, password,user_id))