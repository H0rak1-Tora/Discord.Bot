import disnake
from disnake.ext import commands

import smthouse


class ServerInformation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="info", description="Отправляет краткую информацию о сервере.")
    async def info(self, ctx):
        if isinstance(ctx.channel, disnake.TextChannel):
            embed_info = disnake.Embed(
                title="Information",
                description="This is some information.",
                color=0x18f2b2,
            )
            # embed_info.set_thumbnail(file=disnake.File(r"photo\list.png"))
            embed_info.set_image(url="https://i.playground.ru/p/SWFyLtCnYduJ-KsOL5Tqag.png")
            embed_info.add_field(name="<t:1704056399:R>", value="Обычное значение", inline=False)
            embed_info.add_field(name="Встроенный заголовок", value='Встроенное значение', inline=True)
            embed_info.add_field(name='Встроенный заголовок', value="Встроенное значение", inline=True)
            embed_info.add_field(name="Встроенный заголовок", value="Встроенное значение", inline=True)
            await ctx.send(embed=embed_info)
            smthouse.tools.debug(ctx, self.bot, command="info")
        else:
            # Если команда вызвана в личных сообщениях
            await ctx.send("Эта команда работает только на сервере.", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(ServerInformation(bot))
