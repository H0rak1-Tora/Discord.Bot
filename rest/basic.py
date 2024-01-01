import disnake
import datetime
# import time
import pytz

from rest import config

from disnake import (Intents, ModalInteraction)
from disnake import TextInputStyle

intents = disnake.Intents(messages=True, guilds=True)
Intents.message_content = True
# Здесь находятся все габоритные блоки кода.


async def debug(ctx, bot, command):
    if config.debug:
        author_name = ctx.author.name
        guild_name = ctx.guild.name if ctx.guild else "Direct Message"
        channel_name = ctx.channel.name if ctx.guild else "Direct Message"
        current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        debug_info = (f"{current_time}: \"{guild_name}\"|{channel_name}|{author_name}|{command}|"
                      f"Ping:{float(bot.latency * 1000)}ms")
        print(debug_info)
    else:
        pass


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
                color=0x18f2b2
            )
            embed_event.add_field(name=f"{eventname}:", value=f"Начало: {time_string}.\n"
                                                              f"Продолжительность: {int(thentime)} минут.\n"
                                                              f"Конец: {time_string_last}.\n", inline=False)
            embed_event.add_field(name="Описание события:", value=f'{eventdescription} ', inline=True)
#            embed_sending_user_information_about_the_created_event = disnake.Embed()
            await channel.send(embed=embed_event)
    await inter.response.send_modal(modal=EventModal())


async def main_event(ctx, bot):
    command_name = "create_event"
    if isinstance(ctx.channel, disnake.TextChannel):
        # Если команда вызвана на сервере
        await ctx.send("Эта команда работает только в личных сообщениях.", ephemeral=True)
    else:
        select_options = [
            disnake.SelectOption(label="SMTHouse - Умный Дом", value="ID_SERVER_1"),
            disnake.SelectOption(label="Chill zone", value="ID_SERVER_2"),
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
        await debug(ctx, bot, command=command_name)


async def main_on_dropdown_event(inter, bot):
    # Получение значения, выбранного в меню
    selected_value = inter.data['values'][0]

    # Сообщение, отправляемое в определенный канал сервера в зависимости от выбранного значения
    if selected_value == "ID_SERVER_1":
        guild = bot.get_guild(config.server1)
        channel = guild.get_channel(config.channel1)
        await event_modal(inter, channel)

    elif selected_value == "ID_SERVER_2":
        guild = bot.get_guild(config.server2)
        channel = guild.get_channel(config.channel2)
        await event_modal(inter, channel)

        async for message in inter.author.history(limit=None):
            try:
                await message.delete()
            except disnake.NotFound:
                pass  # Обрабатываем случай, если сообщение уже было удалено или не найдено


async def conclusion_info(ctx, bot):
    command_name = "info"
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
        await debug(ctx, bot, command=command_name)
    else:
        # Если команда вызвана в личных сообщениях
        await ctx.send("Эта команда работает только на сервере.", ephemeral=True)


async def command_buttons(inter):
    await inter.response.send_message("Need help?", components=[
            disnake.ui.Button(label="Info", style=disnake.ButtonStyle.secondary, custom_id="yes")
        ],
    )


async def main_give_role(ctx, role, member, bot):
    command_name = "give_role"
    if isinstance(ctx.channel, disnake.TextChannel):
        try:
            await member.add_roles(role)
            await ctx.send(f'{member.mention}, Вы получили роль {role.name}')
        except disnake.Forbidden:
            await ctx.send("У меня нет прав для выдачи этой роли.")
        await debug(ctx, bot, command=command_name)
    else:
        # Если команда вызвана в личных сообщениях
        await ctx.send("Эта команда работает только на сервере.", ephemeral=True)


async def fun_panel(inter):
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


#    if inter.component.custom_id == "fun3":
#       await inter.response.send_message(embed_fun3)

#    if inter.component.custom_id == "fun4":
#        await inter.response.send_message(embed_fun4)


async def reg_activation_buttons(inter):
    if inter.component.custom_id not in ["fun1", "fun2"]:
        return

    if inter.component.custom_id == "fun1":
        embed_fun1 = disnake.Embed(
            title="ММММмммммм......",
            color=0x18f2b2,
        )
        embed_fun1.add_field(name="", value=config.embed_fan1, inline=True)
        await inter.response.send_message(embed=embed_fun1)

    if inter.component.custom_id == "fun2":
        embed_fun2 = disnake.Embed(
            description="GIGACHAD",
            color=0x18f2b2,
        )
        embed_fun2.add_field(name="", value=config.embed_fan2, inline=True)
        await inter.response.send_message(embed=embed_fun2)


async def nah1(ctx, member, bot):
    command_name = "nah"
    if isinstance(ctx.channel, disnake.TextChannel):
        embed_nah1 = disnake.Embed(
            description=f"{ctx.author.mention} элегантно посылает тебя",
            color=0x18f2b2,
        )
        embed_nah1.add_field(name="НАФИГ", value="Иди и не спотыкайся.", inline=False)
        await ctx.send(f"Хей, {member.mention}!")
        await ctx.send(embed=embed_nah1)
        await ctx.send(f"Гордитесь собой, вы элегантно послали {member.mention}", ephemeral=True)
        await debug(ctx, bot, command=command_name)
    else:
        # Если команда вызвана в личных сообщениях
        await ctx.send("Эта команда работает только на сервере.", ephemeral=True)


async def log_message(message, bot):
    # Получаем информацию о сообщении
    channel = bot.get_channel(message.channel.id)  # Здесь ID канала в котором было написано сообщение
    msg = await channel.fetch_message(message.id)  # ID сообщения которое было нап
    # Теперь у вас есть доступ к содержимому сообщения
    content = msg.content
    channel_ids_to_delete = [1172410995008868392,  # ┌⟨📢⟩∘⇒⌠ᴏбъяʙᴧᴇния⌡
                             1172233921036034179,  # ├⟨📑⟩∘⇒⌠ᴄᴇᴩʙᴇᴩ⌡
                             1191297592819191828,  # └⟨📑⟩∘⇒⌠ᴩᴏᴧи⌡
                             1190306058409869352,  # vip txt общение
                             1190306713841184850,  # vip voice общение
                             1172420571145961504,  # ┌⟨💻⟩∘⇒⌠команды⌡
                             1003082436156080188,  # └⟨📷⟩∘⇒⌠ᴦᴀᴧᴇᴩᴇя⌡
                             972898062802493491,   # ┌⟨🎧⟩∘⇒⌠ᴏбщᴇниᴇ⌡
                             1172262824387559565,  # ├⟨🎮⟩∘⇒⌠иᴦᴩы 1⌡
                             1172262874710818896,  # └⟨🎮⟩∘⇒⌠иᴦᴩы 2⌡
                             1172263844253544480,  # ├⟨🚬⟩∘⇒⌠ᴋᴀнᴀʙᴀ⌡
                             1188486772821336157]  # Параша
#                            Список ID каналов для удаления

    categories_ids_to_delete = [1172222957603528815,  # INFORMATION ZONE
                                1190305891220721694,  # VIP ZONE
                                972592717949456414,   # CHILL ZONE1
                                1190301309539188798,  # CHILL ZONE2
                                1172263799001190551]  # AFK ZONE
#                               Список ID категорий для удаления

    role_ids_to_delete = [1191192395870646362,  # Хозяин Кати
                          1191192259593511032,  # Игрушка Артёма
                          1191140074927177800,  # Авганец
                          1189174243527774259,  # НАЁБЩИК
                          1188958816595873813,  # 115кг/час пик
                          1188760288376410152,  # Хозяин Кости
                          1188494907090939925,  # Абушка
                          1188494767684857948,  # Альтушка
                          1188494666761519174,  # Страх Радиантов
                          1188493980619513977,  # Сигма
                          1188493930606637167,  # Тащер
                          1188493748137627770,  # Работа играть в Доту 2
                          1188493705305391174,  # Коммунист
                          1188493628071481375,  # хуй на асфальте
                          1188493474803224656,  # Слово дотера
                          1188493103921905664,  # Ёбанный Санёк
                          1188491786801397821,  # Суй глубже
                          1188491701929639966,  # Тащит без монитора
                          1188491144150134907,  # Должен 500 руб
                          1188490999081738271,  # где ты нахуй?
                          1188490876499021885,  # Саня,ёбанный твой рот
                          1188491209581273172,  # Игрок команды NAVI
                          1188489596498087946,  # Тренер команды NAVI
                          1188488081788117002,  # Дед инсайд
                          1188487998996750386,  # Чушпан
                          1188487773922005133,  # Костя
                          1188489390780063744,  # Акакий
                          1188487602723115120,  # Разработчик
                          1186550125825376376,  # Медико-социальный психолог
                          1188486799337726064,  # Смотрящий Параши
                          1188486294511308880,  # Смотрящий сервера Мармока
                          1188490483945713726,  # Самый сексуальный мужчина в мире
                          1190266338892062770,  # Чиллик
                          1180824567455952899,  # Disco
                          972941404273795116,   # MEE6 🆘
                          1176232365622829098,  # SMTHouse
                          1011716988705452083,  # Бот 👾
                          1010642248368664647,  # SQUAD
                          972886886681047080]   # GIGACHAD

    if content == "Запускай протокол \"Чистый лист\"":
        await message.channel.send("Протокол \"Чистый лист\" запущен")

#       Удаление каналов
        await message.channel.send("Удаление каналов:")
        for channel_id in channel_ids_to_delete:
            channel = bot.get_channel(channel_id)
            if channel:
                try:
                    await channel.delete()
                    await message.channel.send(f"Канал '{channel.name}' был удалён.")
                except Exception as e:
                    await message.channel.send(f"Ошибка при удалении канала: {e}")
            else:
                await message.channel.send(f"Канал с ID {channel_id} не найден.")

#       Удаление категорий
        await message.channel.send("Удаление категорий:")
        for categories_id in categories_ids_to_delete:
            categories = bot.get_channel(categories_id)
            if categories:
                try:
                    await categories.delete()
                    await message.channel.send(f"Категория '{categories.name}' была удалена.")
                except Exception as e:
                    await message.channel.send(f"Ошибка при удалении кантегории: {e}")
            else:
                await message.channel.send(f"Канал с ID {categories_id} не найден.")

#       Удаление ролей
        await message.channel.send("Удаление ролей:")
        for role_id in role_ids_to_delete:
            role = message.channel.guild.get_role(role_id)
            if role:
                await role.delete()
                await message.channel.send(f"Роль {role.name} была удалена.")
            else:
                await message.channel.send(f"Роль с ID {role_id} не найдена.")

    # Выводим информацию о авторе и о сообщении
    print(f"{message.author.name}: {content}")

# https://discord.new/CtUDG3QWDE72
