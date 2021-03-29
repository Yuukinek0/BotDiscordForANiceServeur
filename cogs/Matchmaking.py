import discord
from discord.ext import commands
from discord import Embed

channel_name = "mm-quickplay"
category_ssb = 824439289352945666

class matchmaking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="matchmaking")
    async def matchmaking(self, ctx, user: discord.User):
        #Variable
        guild = ctx.message.guild

        #création du salon
        category = discord.utils.get(ctx.guild.categories, id=category_ssb)
        quickplay_channel = await category.create_text_channel(channel_name)

        #Set permission
        await quickplay_channel.set_permissions(ctx.author, send_messages=True, read_messages=True)
        await quickplay_channel.set_permissions(user, send_messages=True, read_messages=True)
        await quickplay_channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)

        #Labagar
        await quickplay_channel.send(f"{ctx.author.mention} Vs {user.mention}\nLABAGAR")

    @commands.command(name="adminMatchmaking")
    @commands.has_permissions(administrator = True)
    async def admin_matchmaking(self, ctx, user_one: discord.User, user_two: discord.User):
        #Variable
        guild = ctx.message.guild
        category = discord.utils.get(ctx.guild.categories, id=category_ssb)

        #Crée le salon
        quickplay_channel = await category.create_text_channel(channel_name)

        #Set Permissions
        await quickplay_channel.set_permissions(user_one, send_messages=True, read_messages=True)
        await quickplay_channel.set_permissions(user_two, send_messages=True, read_messages=True)
        await quickplay_channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)

        #Labagar
        await quickplay_channel.send(f"{user_one.mention} Vs {user_two.mention}\nLABAGAR")

    @commands.command(name="finishFight")
    async def close_mm_channel(self, ctx):
        channel = discord.TextChannel
        if ctx.channel.name == channel_name:
            await ctx.channel.delete()

    @commands.command(name="adduser")
    async def add_member_to_qp_channel(self, ctx, user_to_add: discord.User):
        channel = discord.TextChannel
        if ctx.channel.name == channel_name:
            await ctx.channel.set_permissions(user_to_add, send_messages=True, read_messages=True)

    @matchmaking.error
    async def matchmaking_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]matchmaking <user>`"
        elif isinstance(error, commands.UserNotFound):
            title = "User Not Found"
            description = "Je ne trouve pas cette utilisateur"
        
        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)
    
    @admin_matchmaking.error
    async def admin_matchmaking_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]matchmaking <user_one> <user_two>`"
        elif isinstance(error, commands.UserNotFound):
            title = "User Not Found"
            description = "Je ne trouve pas un des deux utilisateur"
        
        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @close_mm_channel.error
    async def close_mm_channel_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.ChannelNotFound):
            title = "Channel Error"
            description = "Vous n'êtes pas dans le salon. Cette commande a été conçus pour les salon de matchmaking"
        
        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @add_member_to_qp_channel.error
    async def add_member_to_qp_channel_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]adduser <user>`"
        elif isinstance(error, commands.UserNotFound):
            title = "User Not Found"
            description = "Je ne trouve pas cette utilisateur"
        elif isinstance(error, commands.ChannelNotFound):
            title = "Channel Error"
            description = "Vous n'êtes pas dans le salon. Cette commande a été conçus pour les salon de matchmaking"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(matchmaking(bot))