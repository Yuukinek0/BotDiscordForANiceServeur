import discord
from discord.ext import commands

from bot import bot_owner

class PostAction(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="post")
	@commands.check(bot_owner)
	async def post_channel(self, ctx, channel: discord.TextChannel, nombre: int, *, msg):
		if nombre == None:
			nombre = 1

		idk = 0
		while idk != nombre:
			await channel.send(msg)
			idk += 1
			if idk == nombre:
				break
				
		await ctx.message.add_reaction("✅")

	@commands.command(name="botdm")
	@commands.check(bot_owner)
	async def botdm(self, ctx, user: discord.User, nombre: int, msg: str):
		idk = 0
		while idk != nombre:
			await user.send(msg)
			idk += 1
			if idk == nombre:
				break

		await ctx.message.add_reaction("✅")

def setup(bot):
	bot.add_cog(PostAction(bot))
