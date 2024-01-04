from disnake.ext import commands

import smthouse


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="clear", description="Удаляет сообщения.")
    async def clear(self, inter, amount: int):
        smthouse.tools.debug_info.debug_inter(inter, self.bot, command="clear")
        await inter.channel.purge(limit=amount)
        await inter.response.send_message(f"Удалено {amount} сообщений", ephemeral=True)


def setup(bot):
    bot.add_cog(Clear(bot))
