# APA MONYET?
# COPAS TERIAK COPAS BLOK
# GAY TERIAK GAY IDIOT DASAR
# APA? MIKIR LAH IDIOT

import asyncio

from pyrogram import idle

from ArUbot import *


async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
        # JANGAN DI GANTI ANJINH, KALO MAU TAMBAHIN AJA PUNYA LU DISINI.
        # JANGAN IDIOT YA NGENTOT
        await ubot_.join_chat("nathsupport")
        await ubot_.join_chat("nathupdate")
        await ubot_.join_chat("nthstore")

    except asyncio.TimeoutError:
        await remove_ubot(user_id)
        await add_prem(user_id)
        await sending_user(user_id)
        print(f"[INFO] - ({user_id}) TIDAK DAPAT MERESPPON")
    except:
        await remove_ubot(user_id)
        await rm_all(user_id)
        await remove_all_vars(user_id)
        await rem_pref(user_id)
        await rem_expired_date(user_id)
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        print(f"✅ {user_id} BERHASIL DI HAPUS")


async def main():
    tasks = [
        asyncio.create_task(start_ubot(int(_ubot["name"]), _ubot))
        for _ubot in await get_userbots()
    ]
    await asyncio.gather(*tasks, bot.start())
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
