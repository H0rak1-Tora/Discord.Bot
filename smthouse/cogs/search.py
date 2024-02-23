import disnake
from disnake.ext import commands

import smthouse


class SearchUser(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="search", description="Поиск записи о нарушениях выбраного пользователя.")
    async def search(self, ctx, member: disnake.Member):
        search_input = smthouse.managers.database.search(user_id=member.id)
        embed = smthouse.сomponents.embed.create_search_embed(search_input, user_id=member.id)
        smthouse.tools.debug_info.debug(ctx, self.bot, command="search")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(SearchUser(bot))
