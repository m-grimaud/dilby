from discord.ext import commands
from Dilbot import Dilbot
import asyncio
import os


class TextManager(commands.Cog, name="Text Processing"):
    """ Does various things with text. """
    def __init__(self, bot: Dilbot) -> None:
        self.bot = bot

    @commands.command(name="text",
                      brief="Processes text attachment and reposts to channel.",
                      usage="<paste text from clipboard as attachment>")
    @commands.is_owner()
    async def split_text(self, ctx: commands.context.Context) -> None:
        """ Takes a text pasted as an attachment from the same message and
            posts it to the channel at one line per second. """
        message = ctx.message
        if message.attachments:
            await ctx.message.attachments[0].save("temp.txt")
            self.bot.append_info_log(f"Downloading {message.attachments[0]} as temp.txt")
            with open("temp.txt", "rt", encoding="utf8") as res:
                for line in res:
                    line = line.strip()
                    line_len = len(line)
                    if line_len <= 1:
                        # newline
                        continue
                    elif line_len > self.bot.max_message_len:
                        chunks = [line[i: i + self.bot.max_message_len] for i in
                                  range(0, line_len, self.bot.max_message_len)]
                        for chunk in chunks:
                            await message.channel.send(chunk)
                    else:
                        await message.channel.send(line)
                    await asyncio.sleep(1)
            self.bot.append_info_log(f"Deleting {message.attachments[0]}")
            os.remove("temp.txt")


def setup(bot: Dilbot) -> None:
    bot.add_cog(TextManager(bot))
