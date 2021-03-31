import discord, os

from discord import Embed
from discord.ext import commands

prefix = "!"

bot = commands.Bot(command_prefix=prefix, help_command=None)

load = []
unload = []

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
    unload.remove(f"{extension}.py")
    load.append(f"{extension}.py")

    await ctx.message.add_reaction("✅")

@bot.command(name="unload")
@commands.check(bot_owner)
async def unloadcog(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    load.remove(f"{extension}.py")
    unload.append(f"{extension}.py")

    await ctx.message.add_reaction("✅")

@bot.command(name="reload")
@commands.check(bot_owner)
async def reloadcog(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    load.remove(f"{extension}.py")
    unload.append(f"{extension}.py")

    bot.load_extension(f'cogs.{extension}')
    unload.remove(f"{extension}.py")
    load.append(f"{extension}.py")

    await ctx.message.add_reaction("✅")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        load.append(filename)

@bot.command(name="coglist")
@commands.check(bot_owner)
async def list_cog(ctx):
    embed_load = Embed(colour=discord.Colour.green())
    embed_unload = Embed(colour=discord.Colour.red())

    load_sans_py = [s.replace(".py", "") for s in load]
    load_sans_py.sort()
    
    unload_sans_py = [s.replace(".py", "") for s in unload]
    unload_sans_py.sort()

    embed_load.add_field(name="Chargé", value=", ".join(load_sans_py), inline=False)
    embed_unload.add_field(name="Déchargé", value=", ".join(unload_sans_py), inline=False)

    await ctx.send(embed=embed_load)
    await ctx.send(embed=embed_unload)


bot.run("TOKEN")
