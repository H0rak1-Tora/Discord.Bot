import disnake
from disnake.ext import commands

import smthouse


class CreateEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="create_event", description="Создание события.")
    async def create_event(self, ctx):
        if isinstance(ctx.channel, disnake.TextChannel):
            # Если команда вызвана на сервере
            await ctx.send("Эта команда работает только в личных сообщениях.", ephemeral=True)
        else:
            select_options = [
                disnake.SelectOption(label="SMTHouse - Умный Дом", value="ID_SERVER_1"),
                disnake.SelectOption(label="Chill zone", value="ID_SERVER_2"),
                disnake.SelectOption(label="BAnNicK YTGo", value="ID_SERVER_3"),
            ]
            select = disnake.ui.Select(placeholder="Выберите сервер", options=select_options)
            view = disnake.ui.View()
            view.add_item(select)

            embed_test = disnake.Embed(
                title="Панель упровления.",
                description="Тестовый вариант панели выбора сервера.",
                color=0x18f2b2,
            )
            await ctx.send(embed=embed_test, view=view)
            smthouse.tools.debug(ctx, self.bot, command="create_event")


def setup(bot: commands.Bot):
    bot.add_cog(CreateEvent(bot))
