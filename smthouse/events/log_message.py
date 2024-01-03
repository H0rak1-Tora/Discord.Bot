import disnake
import datetime

import smthouse


def __init__(bot):
    message(bot)


def message(bot):
    @bot.event
    async def on_message(msg):
        # Получаем информацию о сообщении
        current_time = datetime.datetime.now().strftime("%m.%d.%Y %H:%M:%S")
        guild_name = msg.guild.name
        channel_name = msg.channel.name
        content = msg.content
        print(f"{current_time} \"{guild_name}\" \"{channel_name}\" {msg.author.name}: {content}")
        if content == "Запускай протокол \"Чистый лист\"":
            await msg.channel.send("Протокол \"Чистый лист\" запущен")

#           Удаление каналов
            await msg.channel.send("Удаление каналов:")
            for channel_id in smthouse.config.channel_ids_to_delete:
                channel = bot.get_channel(channel_id)
                if channel:
                    try:
                        await channel.delete()
                        await msg.channel.send(f"Канал '{channel.name}' был удалён.")
                    except Exception as e:
                        await msg.channel.send(f"Ошибка при удалении канала: {e}")
                else:
                    await msg.channel.send(f"Канал с ID {channel_id} не найден.")

#           Удаление категорий
            await msg.channel.send("Удаление категорий:")
            for categories_id in smthouse.config.categories_ids_to_delete:
                categories = bot.get_channel(categories_id)
                if categories:
                    try:
                        await categories.delete()
                        await msg.channel.send(f"Категория '{categories.name}' была удалена.")
                    except Exception as e:
                        await msg.channel.send(f"Ошибка при удалении кантегории: {e}")
                else:
                    await msg.channel.send(f"Канал с ID {categories_id} не найден.")

#           Удаление ролей
            await msg.channel.send("Удаление ролей:")
            for role_id in smthouse.config.role_ids_to_delete:
                role = msg.channel.guild.get_role(role_id)
                if role:
                    await role.delete()
                    await msg.channel.send(f"Роль {role.name} была удалена.")
                else:
                    await msg.channel.send(f"Роль с ID {role_id} не найдена.")

        elif content == "мне нужен список всех ролей":
            role_list = disnake.Embed(
                description="Список всех ролей уже в консоле",
                color=0x18f2b2,
            )
            await msg.channel.send(embed=role_list)
            roles = msg.guild.roles
            for role in roles:
                print(f"{role.id},  # {role.name}")

        await bot.process_commands(msg)

# https://discord.new/CtUDG3QWDE72
# https://discord.new/zyaytKKJ4swN
