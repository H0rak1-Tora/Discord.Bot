import disnake
from disnake.ext import commands
from dotenv import dotenv_values
import time

import smthouse

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
config_dotenv = dotenv_values("secret.env")
TOKEN = config_dotenv["SECRET_TOKEN"]

print(f"Режим отладки: {smthouse.config.debug}")


@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="ChatGPT"))
    start_time = time.time()
    print("Загрузка когов...")
    bot.load_extension("smthouse.cogs.clear")
    bot.load_extension("smthouse.cogs.event")
    bot.load_extension("smthouse.cogs.examination")
    bot.load_extension("smthouse.cogs.fun")
    bot.load_extension("smthouse.cogs.info")
    bot.load_extension("smthouse.cogs.role")
    smthouse.events.dropdown_event.setup(bot)
    smthouse.events.log_message.__init__(bot)
    smthouse.events.on_button_click.__init__(bot)
    total_loading_time = time.time() - start_time
    print(f"На загрузку когов ушло: {total_loading_time: .3f} мс.")
    print(f'Готов к работе как - {bot.user}')

bot.run(TOKEN)
