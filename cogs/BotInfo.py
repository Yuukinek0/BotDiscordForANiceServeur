import discord
from discord.ext import commands

class BotInfo(commands.Cog):

    @commands.command(name="github")
    async def github(self, ctx):
        await ctx.send("https://github.com/Yuukinek0/BotDiscordForANiceServeur")

def setup(bot):
    bot.add_cog(BotInfo(bot))
