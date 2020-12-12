from twitchio.ext import commands
import random
import os


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=os.getenv("irc_token"),
            client_id=os.getenv("client_id"),
            nick="vimbott",
            prefix="!",
            initial_channels=["#doctorvim"],
        )

    async def event_ready(self):
        print(f"Ready | {self.nick}")

    async def event_message(self, message):
        await self.handle_commands(message)

    @commands.command(name="dot")
    async def dot(self, ctx):
        await ctx.send("")

    @commands.command(name="cproject")
    async def cproject(self, ctx):
        try:
            if ctx.author.is_mod:
                text = str(ctx.message.content)
                if len(text) > 1:
                    with open("./project.txt", "w") as f:
                        a = text.strip("!cproject")
                        f.write(a)
                    if len(text) < 1:
                        await ctx.send("Changed")
                    f.close()
                else:
                    await ctx.send("Project was unchanged or empty")
            else:
                await ctx.send(f"You are not able to do this {ctx.author.name}")
        except Exception as err:
            print(err)

    @commands.command(name="project")
    async def project(self, ctx):
        with open("./project.txt", "r") as f:
            await ctx.send(str(f.read()))
        f.close()

    @commands.command(name="roll")
    async def roll(self, ctx):
        r = random.randint(0, 20)
        await ctx.send(r)

    @commands.command(name="dan")
    async def dan(self, ctx):
        await ctx.send("Dan Likes Men")

    @commands.command(name="github")
    async def git(self, ctx):
        await ctx.send("https://github.com/justnat3")


if __name__ == "__main__":
    bot = Bot()
    bot.run()
