import disnake

import smthouse.config


# import smthouse


def create_search_embed(row, user_id):
    if row:
        embed = disnake.Embed(
            description=f"Информация о: <@{row[0]}>",
            color=0x18f2b2,
        )
        if row[5]:
            embed.add_field(name="Предупреждение №1:", value=row[2], inline=True)
            if row[3]:
                embed.add_field(name="Предупреждение №2:", value=row[3], inline=True)
                if row[4]:
                    embed.add_field(name="Предупреждение №3:", value=row[4], inline=True)
            embed.add_field(name="Когда было выдано последнее предупреждение:", value=row[5], inline=True)

        if row[9]:
            embed.add_field(name="Наказание №1:", value=row[6], inline=True)
            if row[7]:
                embed.add_field(name="Наказание №2:", value=row[7], inline=True)
                if row[8]:
                    embed.add_field(name="Наказание №3:", value=row[8], inline=True)
            embed.add_field(name="Когда было выдано последнее наказание:", value=row[9], inline=True)
        return embed

    else:
        embed = disnake.Embed(
            description=f"Информация о: <@{user_id}>",
            color=0x18f2b2,
        )
        embed.add_field(name="Нарушений не найдено.", value="", inline=True)

        return embed


def embed_output_to_user(row, user_id):

    if row:
        embed = disnake.Embed(
            description=f"Все ваши нарушения и их время.",
            color=0x18f2b2,
        )
        if row[5]:
            embed.add_field(name="Предупреждение №1:", value=row[2], inline=True)
            if row[3]:
                embed.add_field(name="Предупреждение №2:", value=row[3], inline=True)
                if row[4]:
                    embed.add_field(name="Предупреждение №3:", value=row[4], inline=True)
            embed.add_field(name="Когда было выдано последнее предупреждение:", value=row[5], inline=True)

        if row[9]:
            embed.add_field(name="Наказание №1:", value=row[6], inline=True)
            if row[7]:
                embed.add_field(name="Наказание №1:", value=row[7], inline=True)
                if row[8]:
                    embed.add_field(name="Наказание №3:", value=row[8], inline=True)
            embed.add_field(name="Когда было выдано последнее наказание:", value=row[9], inline=True)

        return embed


def create_warn_embed(action, member, reason):
    actions = {
        "warn1": "получил предупреждение",
        "warn2": "получил предупреждение",
        "warn3": "получил предупреждение",
        "punishment1": "получил наказание",
        "punishment2": "получил наказание",
        "punishment3": "получил наказание",
        "BAN": "бан",
    }
    action_text = actions.get(action, "Что-то не так.")

    embed = disnake.Embed(
        description=f"<@{member.id}> {action_text}.",
        color=0x18f2b2,
    )
    embed.add_field(name="Причина:", value=str(reason), inline=True)
    if smthouse.config.debug:
        print(action)
        print(member)
        print(reason)

    return embed
