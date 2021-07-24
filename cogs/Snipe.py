import discord, asyncio
from discord import Embed
from discord.ext import commands

message_snipe_content = None
message_snipe_user = None

message_editsnipe_content = None
message_editsnipe_user = None

class Snipe(commands.Cog):

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        global message_snipe_content
        global message_snipe_user

        message_snipe_content = message.content
        message_snipe_user = message.author.id
        await asyncio.sleep(300)
        message_snipe_content = None
        message_snipe_user = None

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        global message_editsnipe_content
        global message_editsnipe_user

        message_editsnipe_content = before.content
        message_editsnipe_user = before.author.id
        await asyncio.sleep(120)
        message_editsnipe_content = None
        message_editsnipe_user = None

    @commands.command(name="snipe")
    async def snipe(self, ctx):
        if message_snipe_content is not None and message_snipe_user is not None:
            embed = Embed(title="Snipe message", colour=ctx.author.colour, description=f"Snipe by {ctx.author.display_name}\n<@{message_snipe_user}> :\n{message_snipe_content}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Theres nothing to snipe.")

    @commands.command(name="editsnipe")
    async def editsnipe(self, ctx):
        if message_editsnipe_content is not None and message_editsnipe_user is not None:
            embed = Embed(title="Edit Snipe Message",description=f"Snipe edit by {ctx.author.display_name}\n<@{message_editsnipe_user}> :\n{message_editsnipe_content}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Theres nothing to snipe.")

def setup(bot):
    bot.add_cog(Snipe(bot))
