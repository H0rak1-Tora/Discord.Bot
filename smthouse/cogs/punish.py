import disnake
from disnake.ext import commands

import smthouse


class PunishUser(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="punish", description="Выдаёт придупреждение или наказание, в зависимости от истории.")
    async def punish(self, ctx, member: disnake.Member, reason):
        if reason in smthouse.config.violations:
            punish_input = smthouse.managers.database.punish_user(member, reason)
            embed = smthouse.сomponents.embed.create_warn_embed(punish_input, member, reason=reason)
            smthouse.tools.debug_info.debug(ctx, self.bot, command="punish")
            await ctx.send(embed=embed)

        else:
            await ctx.send(embed=disnake.Embed(description=f"Введите корректную причину.", color=0x18f2b2,))


def setup(bot: commands.Bot):
    bot.add_cog(PunishUser(bot))


# 1.1.1 - Начал конфликт.
# 1.1.2 - Поддался на провокацию.
# 1.2 - Пиар.
# 1.3 - Торговля.
# 1.4 - Говорил плохие шутки.
# 1.5 - Плохая аватарка.
# 1.6 - Плохой ник.
# 1.7 - Выдавал себя за другое лицо.
