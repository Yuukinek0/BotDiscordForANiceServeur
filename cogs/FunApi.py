import discord
from discord import Embed
from discord.ext import commands

from aiohttp import request

class FunApi(commands.Cog):

	@commands.command(name="meme")
	async def meme(self, ctx):
		image_meme_url = "https://some-random-api.ml/meme"

		async with request("GET", image_meme_url, headers={}) as response:
			if response.status == 200:
				data = await response.json()
				image_link = data["image"]
				meme_link = data["caption"]

				embed = Embed(colour=ctx.author.colour,description=meme_link)
				embed.set_image(url=image_link)
				await ctx.send(embed=embed)

	@commands.command(name="cat")
	async def pac_ref(self, ctx):
		image_url = f"https://some-random-api.ml/img/cat"

		async with request("GET", image_url, headers={}) as response:
			if response.status == 200:
				data = await response.json()
				image_link = data["link"]

				embed = Embed(colour=ctx.author.colour)
				embed.set_image(url=image_link)
				await ctx.send(embed=embed)

	@commands.command(name="dog")
	async def dog_api(self, ctx):
		image_url = "https://some-random-api.ml/img/dog"

		async with request("GET", image_url, headers={}) as response:
			if response.status == 200:
				data = await response.json()
				image_link = data["link"]

				embed = Embed(colour=ctx.author.colour)
				embed.set_image(url=image_link)
				await ctx.send(embed=embed)

	@commands.command(name="waifu")
	async def omg_waifu(self, ctx, categorie: str):
		if (waifu:= categorie.lower()) in ("waifu", "neko", "cry", "hug", "kiss", "pat", "blush", "happy", "wink", "dance"):
			image_url = f"https://waifu.pics/api/sfw/{waifu}"

			async with request("GET", image_url, headers={}) as response:
				if response.status == 200:
					data = await response.json()
					image_link = data["url"]

					embed = Embed(title=f"{categorie.title()}", colour=ctx.author.colour)
					embed.set_image(url=image_link)
					await ctx.send(embed=embed)

	@omg_waifu.error
	async def omg_waifu_error(self, ctx, error):
		description = ""
		title = ""
		if isinstance(error, commands.MissingRequiredArgument):
			title = "Argument Error"
			description = "Vous n'avez pas mis d'argument. Voici les argument autoriser :\n`waifu, neko, cry, hug, kiss, pat, blush, happy, wink, dance`"
		elif isinstance(error, commands.BadArgument):
			title = "Argument Error"
			description = "Vous avez pas renseigner le bon argument. Voici les argument autoriser :\n`waifu, neko, cry, hug, kiss, pat, blush, happy, wink, dance`"

		embed = Embed(title=title, description=description)
		await ctx.send(embed=embed)			

def setup(bot):
	bot.add_cog(FunApi(bot))