import logging
from discord.ext import commands


class Dilbot(commands.Bot):
    def __init__(self, token, **options) -> None:
        super().__init__(**options)
        self.logger = logging.getLogger("discord")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
        self.token = token
        # discord's max length for a message
        self.max_message_len = 2000
        self.load_extension("cogs.BotManager")
        self.load_extension("cogs.TextManager")

    async def on_ready(self) -> None:
        self.append_info_log(f"Logged in as {self.user}")

    async def on_command_error(self, context: commands.context.Context, exception: commands.CommandError) -> None:
        self.append_info_log(f"Can't run - {context.command}")
        self.append_info_log(f"Exception - {exception}")

    def start_session(self) -> None:
        try:
            self.run(self.token)
        except Exception as e:
            self.logger.log(logging.ERROR, e)

    def append_info_log(self, text) -> None:
        self.logger.log(logging.INFO, "INFO: " + text)
