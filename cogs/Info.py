from datetime import datetime
from typing import Optional

from discord import Embed, Member
from discord.ext.commands import Cog
from discord.ext import commands

import discord

class Info(Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="userinfo", aliases=["memberinfo", "ui", "mi"])
	async def user_info(self, ctx, target: Optional[Member]):
		target = target or ctx.author

		embed = Embed(title="User information",
					  colour=target.colour,
					  timestamp=datetime.utcnow())

		embed.set_thumbnail(url=target.avatar_url)

		fields = [("Nom", str(target), True),
				  ("ID", target.id, True),
				  ("Bot?", target.bot, True),
				  ("Top role", target.top_role.mention, True),
				  ("Statut", str(target.status).title(), True),
				  ("Activité", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
				  ("Crée le", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("A rejoin le", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Boost", bool(target.premium_since), True)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed=embed)

	@commands.command(name="avatar")
	async def user_avatar(self, ctx, target: Optional[Member]):
		target = target or ctx.author

		embed = Embed(title="User Avatar", colour=ctx.author.colour)
		embed.set_image(url=target.avatar_url)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Info(bot))