import discord, random
from discord import File, Embed
from discord.ext import commands

ssbu_character_list = [
    "Mario", "Donkey Kong", "Link", "Samus",
    "Dark Samus", "Yoshi", "Kirby", "Fox",
    "Pikachu", "Luigi", "Ness", "Captain Falcon",
    "Jigglypuff", "Peach", "Daisy", "Bowser",
    "Ice Climbers", "Sheik", "Zelda", "Dr. Mario",
    "Pichu", "Falco", "Marth", "Lucina",
    "Young Link", "Ganondorf", "Mewtwo", "Roy",
    "Chrom", "Mr. Game & Watch", "Meta Knight", "Pit",
    "Dark Pit", "Zero Suit Samus", "Wario", "Snake",
    "Squirtle", "Ivysaur", "Charizard", "Diddy Kong",
    "Lucas", "Sonic", "King Dedede", "Olimar",
    "Lucario", "R.O.B", "Toon Link", "Wolf",
    "Villager", "Mega Man", "Wii Fit Trainer", "Rosaline and Luma",
    "Little Mac", "Greninja", "Mii Brawler", "Mii Swordfighter",
    "Mii Gunner", "Palutena", "Pac-Man", "Robin",
    "Shulk", "Bowser Jr.", "Duck Hunt", "Ryu",
    "Ken", "Cloud", "Corrin", "Bayonetta",
    "Inkling", "Ridley", "Simon", "Richter",
    "King K.Rool", "Isabelle", "Incineroar", "Piranha Plant",
    "Joker", "Hero", "Banjo & Kazooie", "Terry",
    "Byleth", "Min Min", "Steve", "Sephiroth", "Pyra",
    "Myhtra"
]

class Random_Character_SSBU(commands.Cog):

    @commands.command(name="randomssbu")
    async def get_random_personnage_ssbu(self, ctx):
        await ctx.send(random.choice(ssbu_character_list))


def setup(bot):
    bot.add_cog(Random_Character_SSBU(bot))