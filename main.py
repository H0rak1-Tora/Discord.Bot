import disnake
from disnake.ext import commands
from dotenv import dotenv_values
import time

import smthouse

cogs_loaded = False
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
config_dotenv = dotenv_values("secret.env")
TOKEN = config_dotenv["SECRET_TOKEN"]

print(f"Режим отладки: {smthouse.config.debug}")


@bot.event
async def on_ready():
    global cogs_loaded

    if not cogs_loaded:
        await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="ChatGPT"))
        start_time = time.time()
        print("Загрузка когов...")

        smthouse.cogs.clear.setup(bot)
        smthouse.cogs.event.setup(bot)
        smthouse.cogs.examination.setup(bot)
        smthouse.cogs.fun.setup(bot)
        smthouse.cogs.info.setup(bot)
        smthouse.cogs.punish.setup(bot)
        smthouse.cogs.role.setup(bot)
        smthouse.cogs.search.setup(bot)
        smthouse.events.dropdown_event.setup(bot)
        smthouse.events.log_message.__init__(bot)
        smthouse.events.on_button_click.__init__(bot)

        total_loading_time = time.time() - start_time
        print(f"На загрузку когов ушло: {total_loading_time: .3f} мс.")
        print(f'Готов к работе как - {bot.user}')
        cogs_loaded = True

    else:
        print("Была предотвращена повторная загрузка когов.")

bot.run(TOKEN)
