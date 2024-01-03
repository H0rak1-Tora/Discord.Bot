import datetime

import smthouse


async def debug(ctx, bot, command):
    if smthouse.config.debug:
        author_name = ctx.author.name
        guild_name = ctx.guild.name if ctx.guild else "Direct Message"
        channel_name = ctx.channel.name if ctx.guild else "Direct Message"
        current_time = datetime.datetime.now().strftime("%m.%d.%Y %H:%M:%S")
        debug_info = (f"{current_time}: \"{guild_name}\"|{channel_name}|{author_name}|{command}|"
                      f"Ping:{float(bot.latency * 1000)}ms")
        print(debug_info)
    else:
        pass
