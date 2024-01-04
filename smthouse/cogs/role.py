import disnake
from disnake.ext import commands

import smthouse


class Role(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def giverole(self, ctx, role: disnake.Role, member: disnake.Member):
        if isinstance(ctx.channel, disnake.TextChannel):
            try:
                await member.add_roles(role)
                await ctx.send(f'{member.mention}, Вы получили роль {role.name}')
            except disnake.Forbidden:
                await ctx.send("У меня нет прав для выдачи этой роли.")
            smthouse.tools.debug(ctx, self.bot, command="giverole")
        else:
            # Если команда вызвана в личных сообщениях
            await ctx.send("Эта команда работает только на сервере.", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Role(bot))
