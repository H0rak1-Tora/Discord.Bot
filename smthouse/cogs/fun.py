import disnake
from disnake.ext import commands

# import smthouse


class FunPanel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="fun", description="Очень фановая команда!")
    async def fun_panel(self, inter: disnake.ApplicationCommandInteraction):
        embed_fun_panel = disnake.Embed(
            title="Фан панелька.",
            description="Тут ты выбераешь фановую кнопочку.",
            color=0x18f2b2,
        )
        await inter.response.send_message(
            embed=embed_fun_panel,
            components=[
                disnake.ui.Button(label="UwU", style=disnake.ButtonStyle.success, custom_id="fun1"),
                disnake.ui.Button(label="Gigachad", style=disnake.ButtonStyle.success, custom_id="fun2"),
            ],
        )

    @commands.slash_command(name="nah", description="Элегантно посылает человека!")
    async def nah(self, ctx, member: disnake.Member):
        if isinstance(ctx.channel, disnake.TextChannel):
            embed_nah1 = disnake.Embed(
                description=f"{ctx.author.mention} элегантно посылает тебя",
                color=0x18f2b2,
            )
            embed_nah1.add_field(name="НАФИГ", value="Иди и не спотыкайся.", inline=False)
            await ctx.send(f"Хей, {member.mention}!")
            await ctx.send(embed=embed_nah1)
            await ctx.send(f"Гордитесь собой, вы элегантно послали {member.mention}", ephemeral=True)
#            await debug(ctx, bot, command="nah")
        else:
            # Если команда вызвана в личных сообщениях
            await ctx.send("Эта команда работает только на сервере.", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(FunPanel(bot))
