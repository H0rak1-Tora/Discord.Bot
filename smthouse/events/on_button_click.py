import disnake

import smthouse


def __init__(bot):
    buttons(bot)


def buttons(bot):
    @bot.listen("on_button_click")
    async def reg_activation_buttons(inter):
        if inter.component.custom_id not in ["fun1", "fun2"]:
            return
        elif inter.component.custom_id == "fun1":
            embed_fun1 = disnake.Embed(
                title="ММММмммммм......",
                color=0x18f2b2,
            )
            embed_fun1.add_field(name="", value=smthouse.config.embed_fan1, inline=True)
            await inter.response.send_message(embed=embed_fun1)
        elif inter.component.custom_id == "fun2":
            embed_fun2 = disnake.Embed(
                description="GIGACHAD",
                color=0x18f2b2,
            )
            embed_fun2.add_field(name="", value=smthouse.config.embed_fan2, inline=True)
            await inter.response.send_message(embed=embed_fun2)

    #    elif inter.component.custom_id == "fun3":
    #       await inter.response.send_message(embed_fun3)
    #    elif inter.component.custom_id == "fun4":
    #        await inter.response.send_message(embed_fun4)
