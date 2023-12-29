from rest.basic import *
import disnake
from disnake.ext import commands
from dotenv import dotenv_values
from rest import config
intents = disnake.Intents(messages=True, guilds=True)
Intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

config_dotenv = dotenv_values("secret.env")
TOKEN = config_dotenv["SECRET_TOKEN"]

print(f"Режим отладки: {config.debug}")


@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="ChatGPT"))
    print(f'Готов к работе как - {bot.user}')


@bot.slash_command(guild_ids=None)
async def choose_server(ctx):
    await main_choose_server(ctx)


@bot.slash_command(name="buttons", description="Проверка работы кнопок.")
async def buttons(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message("Need help?", components=[
            disnake.ui.Button(label="Info", style=disnake.ButtonStyle.secondary, custom_id="yes")
        ],
    )


@bot.slash_command(name="info", description="Отправляет краткую информацию о сервере.")
async def info(ctx):
    await conclusion_info(ctx, bot)


@bot.slash_command()
async def give_role(ctx, role: disnake.Role, member: disnake.Member):
    await main_give_role(ctx, role, member)


@bot.slash_command(name="fun", description="Очень фановая команда!")
async def fun(inter: disnake.ApplicationCommandInteraction):
    await fun_panel(inter)


@bot.listen("on_button_click")
async def help_listener(inter: disnake.MessageInteraction):
    await reg_activation_buttons(inter)


@bot.slash_command(name="nah", description="Элегантно посылает человека!")
async def nah(ctx, member: disnake.Member):
    await nah1(ctx, member)


@bot.event
async def on_dropdown(inter):
    await main_on_dropdown(inter, bot)


# @bot.event
# async def on_error():
#     import traceback
#     traceback.print_exc()


bot.run(TOKEN)
