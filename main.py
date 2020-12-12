from twitchio.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token="oauth:gqtncaviovcz1qumzy1qmozinqlh7y",
            client_id="wersfmv0rihk1rq4hondy6yygudjvg",
            nick="vimbott",
            prefix="!",
            initial_channels=["#doctorvim"],
        )

    # Events don't need decorators when subclassed
    async def event_ready(self): print(f"Ready | {self.nick}")

    async def event_message(self, message): await self.handle_commands(message)

    # Commands use a decorator...
    @commands.command(name="dot")
    async def my_command(self, ctx): await ctx.send(f"https://github.com/justnat3")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
