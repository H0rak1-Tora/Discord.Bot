import smthouse
from disnake.ext import commands


class DropdownEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_dropdown(self, inter):
        # Получение значения, выбранного в меню
        selected_value = inter.data['values'][0]
        # Сообщение, отправляемое в определенный канал сервера в зависимости от выбранного значения
        if selected_value == "ID_SERVER_1":
            guild = self.bot.get_guild(smthouse.config.server1)
            channel = guild.get_channel(smthouse.config.channel1)
            await smthouse.сomponents.modal.event_modal(inter, channel)

        elif selected_value == "ID_SERVER_2":
            guild = self.bot.get_guild(smthouse.config.server2)
            channel = guild.get_channel(smthouse.config.channel2)
            await smthouse.сomponents.modal.event_modal(inter, channel)

        elif selected_value == "ID_SERVER_3":
            guild = self.bot.get_guild(smthouse.config.server3)
            channel = guild.get_channel(smthouse.config.channel3)
            await smthouse.сomponents.modal.event_modal(inter, channel)

        # async for message in inter.author.history(limit=None):
        #     try:
        #         await message.delete()
        #     except disnake.NotFound:
        #         pass  # Обрабатываем случай, если сообщение уже было удалено или не найдено


def setup(bot: commands.Bot):
    bot.add_cog(DropdownEvent(bot))
