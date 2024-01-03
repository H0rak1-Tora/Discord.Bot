import disnake
from disnake.ext import commands
from dotenv import dotenv_values

import smthouse

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
config_dotenv = dotenv_values("secret.env")
TOKEN = config_dotenv["SECRET_TOKEN"]

print(f"Режим отладки: {smthouse.config.debug}")


@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="ChatGPT"))
    print(f'Готов к работе как - {bot.user}')
#    permission_info = {}
#    for guild_id in smthouse.config.servers_to_check:
#        guild = bot.get_guild(guild_id)
#        if guild:
#            permissions = guild.get_member(bot.user.id).guild_permissions
#            permission_list = [perm for perm, value in permissions if value]
#            permission_info[guild.name] = permission_list
#    response = "\n".join([f"{guild}: {', '.join(permissions)}" for guild, permissions in permission_info.items()])
#    print(f"Разрешения бота на серверах:\n{response}")
    bot.load_extension("smthouse.cogs.event")
    bot.load_extension("smthouse.cogs.examination")
    bot.load_extension("smthouse.cogs.fun")
    bot.load_extension("smthouse.cogs.info")
    bot.load_extension("smthouse.cogs.role")
    smthouse.events.on_button_click.__init__(bot)
    smthouse.events.log_message.__init__(bot)
    smthouse.events.dropdown_event.setup(bot)


# @bot.event
# async def on_error():
#     import traceback
#     traceback.print_exc()


bot.run(TOKEN)
