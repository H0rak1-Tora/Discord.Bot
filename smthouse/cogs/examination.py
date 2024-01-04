# import disnake
from disnake.ext import commands

import smthouse


class Examination(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="examination", description="Показывает разрешения бота на сервере.")
    async def examination(self, ctx):
        permissions = ctx.guild.get_member(self.bot.user.id).guild_permissions
        permission_list = [perm for perm, value in permissions if value]
        smthouse.tools.debug(ctx, self.bot, command="examination")
        await ctx.send(f"Разрешения бота на сервере:\n{', '.join(permission_list)}", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Examination(bot))
