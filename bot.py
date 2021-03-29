import discord, os

from discord import Embed
from discord.ext import commands

prefix = "!"

bot = commands.Bot(command_prefix=prefix, help_command=None)

@bot.event
async def on_ready():
    print("Pac bot est prêt !")

def bot_owner(ctx):
    owner_bot = [
        722589024820264971,  # Yuukineko
        274600678951747584,  # Pacman_fan
        346035824439328782  # Kaak
    ]

    if ctx.message.author.id in owner_bot:
        return ctx.message.author.id

@bot.command(name="shutdown")
@commands.check(bot_owner)
async def shutdown(ctx):
    await ctx.send("GoodBye")
    await bot.logout()

@bot.command(name="load")
@commands.check(bot_owner)
async def loadcog(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.message.add_reaction("✅")

@bot.command(name="unload")
@commands.check(bot_owner)
async def unloadcog(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.message.add_reaction("✅")

@bot.command(name="reload")
@commands.check(bot_owner)
async def reloadcog(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.message.add_reaction("✅")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command(name="coglist")
@commands.check(bot_owner)
async def list_cog(ctx):
    list_cogs_bot = []
    embed = Embed(title="List des cogs", colour=ctx.author.colour)

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            list_cogs_bot.append(filename)

    sans_py = [s.replace(".py", "") for s in list_cogs_bot]


    embed.add_field(name="liste des cog", value=", ".join(sans_py), inline=False)
    await ctx.send(embed=embed)

bot.run("TOKEN")
