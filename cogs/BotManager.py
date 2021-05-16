from discord.ext import commands
from Dilbot import Dilbot


class BotManager(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot: Dilbot) -> None:
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def goodbye(self, ctx: commands.context.Context) -> None:
        """ Disconnects the bot from Discord. """
        await self.bot.close()


def setup(bot: Dilbot) -> None:
    bot.add_cog(BotManager(bot))
