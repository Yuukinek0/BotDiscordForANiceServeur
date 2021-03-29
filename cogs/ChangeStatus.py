import discord
from discord import Embed
from discord.ext import commands

from bot import bot_owner

class Change_Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Group commande
    @commands.group()
    @commands.check(bot_owner)
    async def changestatus(self, ctx):
        if ctx.invoked_subcommand is None:
            description = ""
            embed = Embed(description=description, colour=ctx.author.colour)
            await ctx.send(embed=embed)


    #Status None
    @changestatus.group(name="none")
    @commands.check(bot_owner)
    async def custom_activity_none(self, ctx):
        await self.bot.change_presence(activity=None)
        await ctx.message.add_reaction("✅")

    #Changer le statu comme : Joue a ...
    @changestatus.group(name="playing")
    @commands.check(bot_owner)
    async def change_playing_status(self, ctx, statut: str):
        await self.bot.change_presence(activity=discord.Game(name=statut))
        await ctx.message.add_reaction("✅")

    #Change le Statue d'écoute : écoute ....
    @changestatus.group(name="listening")
    @commands.check(bot_owner)
    async def change_listening_status(self, ctx, song: str):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=song))
        await ctx.message.add_reaction("✅")

    #Change le status de regard comme : Regarde ....
    @changestatus.group(name="watching")
    @commands.check(bot_owner)
    async def change_watching_status(self, ctx, watch: str):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watch))
        await ctx.message.add_reaction("✅")

    @change_playing_status.error
    async def change_playing_status_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Missing Argument"
            description = "`[p]changestatus playing <activity>`"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @change_listening_status.error
    async def change_listening_status_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]changestatus listening <activity>`"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @change_watching_status.error
    async def change_watching_status_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]changestatus watching <activity>`"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Change_Status(bot))
