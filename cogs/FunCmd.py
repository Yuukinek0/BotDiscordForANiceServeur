import discord, asyncio
from discord import Embed, Forbidden
from discord.ext import commands
from discord.utils import get

import random

class FunCmd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="tk")
	async def tk(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/680516432529719326/710519080943353866/YMlY4pG3AEL0nxtv.mp4")

	@commands.command(name="johns")
	async def johns(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/680500442777518160/713013537156497508/IMG_20200517_021027.jpg")

	@commands.command(name="cafe")
	async def caisse_cafe(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/598829376259358751/730752024748228639/Caisse_Cafe.mp4")

	@commands.command(name="ptdrtki")
	async def ptdrtki(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/690315433949266050/707931542269329508/ptdr-t-ki.mp4")

	@commands.command(name="wallah")
	async def wallah(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/680516432529719326/710212687782739999/wallah-il-a-dit-wallah-mister-v-meme.mp4")

	@commands.command(name="bigflo")
	async def bigflo(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/680516432529719326/711996709785567292/VID_20200518_194026.mp4")

	@commands.command(name="allah")
	async def allah(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/690315433949266050/817460292824727612/Quand_je_seche_le_Bac_Blanc_car_seul_Dieu_peut_me_mettre_a_lepreuve.mp4")

	@commands.command(name="rng")
	async def def_rng(self, ctx):
		await ctx.send("RNG :\nRegardez comment le jeu nous\nNargue avec des\nGros coups de chance quand pas besoin et inversement")

	@commands.command(name="weeb")
	async def weeb_theorie(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/611967163028209693/780157226375053332/twitter_20201110_005446.mp4")

	@commands.command(name="kaak")
	async def kaak_ntr(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/815076683283038238/818747682536947762/IMG_20210309_082632.png")

	@commands.command(name="daisuke")
	async def daisuke_gamepad(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/815076683283038238/818969826524397608/IMG_20210309_162007.png")

	@commands.command(name="paak")
	async def paak(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/815076683283038238/818969830039748628/IMG_20210307_014131.jpg")

	@commands.command(name="yume")
	async def yume(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/815076683283038238/819130168337498132/IMG_20210310_071658.png")

	@commands.command(name="paa")
	async def paa_baton(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/815076683283038238/819359843848290304/20210310_204624.jpg")

	@commands.command(name="quenini")
	async def que_ni_ni_everyone(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/815076683283038238/819360318324211742/IMG_20210310_201758.jpg")

	@commands.command(name="darkshark")
	async def dark_shark_flood_warnings(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/815076683283038238/819360535421124628/IMG_20210310_203723.jpg")

	@commands.command(name="prayLoS")
	async def go_los(self, ctx):
		await ctx.send("https://media.discordapp.net/attachments/698556826400194681/823586668061392916/LOSSUPPORT.png?width=381&height=472")

	@commands.command(name="callthepolice")
	async def fun_call_police(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/815076683283038238/826934303853248522/sdfsdfsdfsdfsdfetyuijhgfbdsfgd.png")

	@commands.command(name="oof")
	async def oof_reaction(self, ctx):
		emoji_one = "🇴"
		emoji_two = "🅾️"
		emoji_troi = "🇫"

		messages = await ctx.channel.history(limit=1).flatten()
		for message in messages:
			await message.delete()
			msgs = await ctx.channel.history(limit=1).flatten()
			for msg in msgs:
				await msg.add_reaction(emoji_one)
				await msg.add_reaction(emoji_two)
				await msg.add_reaction(emoji_troi)

	@commands.command(name="flip")
	async def flip(self, ctx):
		idk = random.randint(1, 100)

		pile_numbers = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99]
		face_numbers = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100]
		if idk in pile_numbers:
			await ctx.send("*Lance une pièce et... PILE !*")
		if idk in face_numbers:
			await ctx.send("*Lance une pièce et... FACE !*")

def setup(bot):
	bot.add_cog(FunCmd(bot))
