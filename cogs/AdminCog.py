import discord

from discord import Embed
from discord.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def createMutedRole(self, ctx):
        mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mutedRole, send_messages = False, speak = False)
        return mutedRole

    async def getMutedRole(self, ctx):
        roles = ctx.guild.roles
        for role in roles:
            if role.name == "Muted":
                return role

        return await self.createMutedRole(ctx)

    @commands.command(name="mute")
    @commands.has_permissions(administrator=True)
    async def mute_member(self, ctx, user: discord.User, *, reason):
        mute_role = await self.getMutedRole(ctx)

        await user.add_roles(mute_role, reason=reason)
        await ctx.message.add_reaction("✅")

    @commands.command(name="unmute")
    @commands.has_permissions(administrator=True)
    async def unmute_user(self, ctx, user: discord, *, reason):
        mute_role = await self.getMutedRole(ctx)

        await user.remove_roles(mute_role, reason=reason)
        await ctx.message.add_reaction("✅")

    @commands.command(name="ban")
    @commands.has_permissions(administrator=True)
    async def ban_member(self, ctx, user: discord.User, *, reason):
        await ctx.guild.ban(user, reason)
        await ctx.message.add_reaction("✅")

    @commands.command(name="unban")
    @commands.has_permissions(administrator=True)
    async def unban_user(self, ctx, user:discord.User, *, reason):
        userName, userId = user.split("#")
        bannedUsers = await ctx.guild.bans()

        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(i.user, reason = reason)
                await ctx.send(f"{user} à été unban.")

                description = f"{ctx.author.mention} a unban {user.display_name}"
                embed = Embed(title="Unban User", description=description)
                return

        # Ici on sait que lutilisateur na pas ete trouvé
        await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

    @commands.command(name="kick")
    @commands.has_permissions(administrator=True)
    async def kick_member(self, ctx, user: discord.User, *, reason):
        await ctx.guild.kick(user, reason=reason)
        await ctx.message.add_reaction("✅")

    @commands.command(name="clear")
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, nombre: int):
        messages = await ctx.channel.history(limit=nombre + 1).flatten()
        for message in messages:
            await message.delete()

    @mute_member.error
    async def mute_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]mute <user>`"
        elif isinstance(error, commands.MemberNotFound):
            title = "Member not found"
            description = "Je ne trouve pas cette utilisateur"
        elif isinstance(error, commands.MissingPermissions):
            title = "Permission Error"
            description = "Vous n'avez pas les permission pour utiliser cette commande"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @unmute_user.error
    async def unmute_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]unmute <user>`"
        elif isinstance(error, commands.MemberNotFound):
            title = "Member not found"
            description = "Je ne trouve pas cette utilisateur"
        elif isinstance(error, commands.MissingPermissions):
            title = "Permission Error"
            description = "Vous n'avez pas les permission pour utiliser cette commande"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @ban_member.error
    async def ban_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]ban <user>`"
        elif isinstance(error, commands.MemberNotFound):
            title = "Member not found"
            description = "Je ne trouve pas cette utilisateur"
        elif isinstance(error, commands.MissingPermissions):
            title = "Permission Error"
            description = "Vous n'avez pas les permission pour utiliser cette commande"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @unban_user.error
    async def unban_error(self,ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]unban <user>`"
        elif isinstance(error, commands.MemberNotFound):
            title = "Member not found"
            description = "Je ne trouve pas cette utilisateur"
        elif isinstance(error, commands.MissingPermissions):
            title = "Permission Error"
            description = "Vous n'avez pas les permission pour utiliser cette commande"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @kick_member.error
    async def kick_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]kick <user>`"
        elif isinstance(error, commands.MemberNotFound):
            title = "Member not found"
            description = "Je ne trouve pas cette utilisateur"
        elif isinstance(error, commands.MissingPermissions):
            title = "Permission Error"
            description = "Vous n'avez pas les permission pour utiliser cette commande"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

    @clear.error
    async def clear_error(self, ctx, error):
        title = ""
        description = ""
        if isinstance(error, commands.MissingRequiredArgument):
            title = "Argument Error"
            description = "`[p]clear <nombre>`"
        elif isinstance(error, commands.MissingPermissions):
            title = "Permission Error"
            description = "Vous n'avez pas les permission pour utiliser cette commande"

        embed = Embed(title=title, description=description)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AdminCog(bot))