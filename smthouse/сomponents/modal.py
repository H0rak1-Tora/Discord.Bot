import disnake
import datetime
import pytz

from disnake import ModalInteraction
from disnake import TextInputStyle


async def event_modal(inter, channel):
    class EventModal(disnake.ui.Modal):
        def __init__(self):
            components = [
                disnake.ui.TextInput(
                    label="Как называется соботие.",
                    placeholder="Название события.",
                    custom_id="EventName",
                    style=TextInputStyle.short,
                    max_length=35,
                ),
                disnake.ui.TextInput(
                    label="Через сколько начнётся",
                    placeholder="Писать в минутах, только число.",
                    custom_id="Time",
                    style=TextInputStyle.short,
                    max_length=3,
                ),
                disnake.ui.TextInput(
                    label="Сколько будет продолжаться",
                    placeholder="Писать в минутах, только число.",
                    custom_id="ThenTime",
                    style=TextInputStyle.short,
                    max_length=5,
                ),
                disnake.ui.TextInput(
                    label="Описание.",
                    placeholder="Описание того что буден происходить во время события.",
                    custom_id="EventDescription",
                    style=TextInputStyle.paragraph,
                    max_length=1000,
                ),
            ]
            super().__init__(
                title="Создание ивента.",
                custom_id="event",
                timeout=300,
                components=components,
            )

        async def callback(self, interactoin: ModalInteraction) -> None:
            time_even = interactoin.text_values["Time"]
            eventname = interactoin.text_values["EventName"]
            thentime = interactoin.text_values["ThenTime"]
            eventdescription = interactoin.text_values["EventDescription"]
            tz = pytz.timezone('Europe/Moscow')
            # Вычисляем время события относительно текущего времени и вычисляем конец события
            event_time = (datetime.datetime.now(tz) +
                          datetime.timedelta(minutes=int(time_even)))
            event_time_last = (datetime.datetime.now(tz) +
                               datetime.timedelta(minutes=int(time_even)) +
                               datetime.timedelta(minutes=int(thentime)))
            # Генерируем строки в формате <t:timestamp:R>
            timestamp = int(event_time.timestamp())
            timestamplast = int(event_time_last.timestamp())
            time_string = f'<t:{timestamp}:R>'
            time_string_last = f'<t:{timestamplast}:R>'
            # Формируем embed
            embed_event = disnake.Embed(
                title="Внимание!!! Событие на подходе.",
                description=f"{interactoin.author.mention} объявляет событие:",
                color=0x18f2b2,
            )
            embed_event.add_field(name=f"{eventname}:", value=f"Начало: {time_string}.\n"
                                                              f"Продолжительность: {int(thentime)} минут.\n"
                                                              f"Конец: {time_string_last}.\n", inline=False)
            embed_event.add_field(name="Описание события:", value=f'{eventdescription} ', inline=True)
            #                embed_sending_user_information_about_the_created_event = disnake.Embed()
            await channel.send(embed=embed_event)
    await inter.response.send_modal(modal=EventModal())
