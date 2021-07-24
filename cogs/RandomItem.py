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
    "Villager", "Mega Man", "Wii Fit Trainer", "Rosalina and Luma",
    "Little Mac", "Greninja", "Mii Brawler", "Mii Swordfighter",
    "Mii Gunner", "Palutena", "Pac-Man", "Robin",
    "Shulk", "Bowser Jr.", "Duck Hunt", "Ryu",
    "Ken", "Cloud", "Corrin", "Bayonetta",
    "Inkling", "Ridley", "Simon", "Richter",
    "King K.Rool", "Isabelle", "Incineroar", "Piranha Plant",
    "Joker", "Hero", "Banjo & Kazooie", "Terry",
    "Byleth", "Min Min", "Steve", "Sephiroth", "Pyra",
    "Mythra", "Kazuya"
]

ssbm_character_list = [
    "Mario", "Luigi", "Donkey Kong", "Link", "Samus",
    "Yoshi", "Kirby", "Fox", "Pikachu", "Jigglypuff",
    "Captain Falcon", "Ness", "Peach", "Bowser", "Dr. Mario",
    "Zelda", "Sheik", "Young Link", "Ganondorf", "Falco",
    "Pichu", "Mewtwo", "Ice Climbers", "Marth", "Roy",
    "Mr. Game & Watch"
]

class Random_Character_SSBU(commands.Cog):

    @commands.command(name="randomssbu")
    async def get_random_personnage_ssbu(self, ctx):
        await ctx.send(random.choice(ssbu_character_list))

    @commands.command(name="randomssbm")
    async def get_random_personnage_ssbm(self, ctx):
        await ctx.send(random.choice(ssbm_character_list))

    @commands.command(name="quiaimetu")
    async def qui_aime_tu_entre_user_et_user(self, ctx, user_one: discord.User, user_two: discord.User):
        idk = random.randint(1, 100)
        user_un = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49,51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97,99]
        user_deux = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

        if idk in user_un:
            await ctx.send(f"Je préfère {user_one.display_name}")
        if idk in user_deux:
            await ctx.send(f"Je préfère {user_two.display_name}")
    
    @commands.command(name="soutiens")
    async def soutien_a_user(self, ctx):
        soutiens_sentence = [
            "Tu es génial",
            "Courage tu vas y arriver",
            "Tu es incroyable",
            f"Tu es beau/belle {ctx.author.display_name}",
            "Même quand c’est dur et que cela représente un vrai défi, tu peux puiser dans tes ressources pour y arriver, à ton rythme",
            "Tu es capable de réaliser bien plus que ce que tu crois.",
            "Cela prend du temps pour que le potentiel fleurisse. Tu n’as pas besoin d’être parfait tout de suite.",
            "Un échec ou une erreur ne signifie pas être nul.",
            "Une action (j’ai échoué) n’est pas une identité (je suis nul(le)).",
            "Ton humanité compte plus que tes erreurs.",
            "Tu ne rates pas et tu n ‘es pas un raté, tu oses essayer.",
            "Combien de temps as-tu mis pour apprendre à marcher ? Es-tu tombé ? Es-tu resté par terre ou as-tu recommencé ?",
            "La joie n’est pas l’inverse du sérieux : tu as le droit de t’éclater dans ce que tu fais.",
            "Que dirais-tu à un ami qui aurait autant peur/ qui se sent aussi découragé que toi, qui douterait de lui ? Dis-toi ces phrases à toi-même.",
            "Tu en es capable : peut-être pas aujourd’hui ni demain, peut-être pas de la manière dont tu penses le faire aujourd’hui.",
            "Tu n’as pas en train d’échouer, tu es en train d’apprendre.",
            "Quelle est la pire chose qui pourrait arriver si tu essayes ? Quelles sont les preuves qui te laissent penser que le pire arrivera ? Es-tu absolument sûr que c’est vrai ? Trouve au moins trois idées pour que cela n’arrive pas.",

        ]
        await ctx.send(random.choice(soutiens_sentence))

def setup(bot):
    bot.add_cog(Random_Character_SSBU(bot))
