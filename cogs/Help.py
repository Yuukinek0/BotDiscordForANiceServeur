import discord

from discord import Embed

from discord.ext import commands

from bot import bot_owner

class Help(commands.Cog):

    @commands.group()
    async def help(self, ctx) -> None:
        if ctx.invoked_subcommand is None:
            description = "`[p]help staff`: Commande staff\n`[p]help fun`\n`[p]help musique`\n`[p]help owner` : Commande Owner bot Yuukineko, Kaak, Pacman_fan\n`[p]github` : Si vous voulez voir le code source du bot"

            embed = Embed(title="Help", description=description, colour=ctx.author.colour)
            await ctx.send(embed=embed)


    #Bot Owner :
    #Yuukineko
    #Kaak
    #Pacman_fan
    @help.group(name="owner")
    @commands.check(bot_owner)
    async def help_owner(self, ctx):
        if ctx.invoked_subcommand is None:
            #Yuukineko, Pac, kaak
            description = "COMMANDE RESERVER AU UTILISATEUR EN DESSOUS :\n<@722589024820264971> <@274600678951747584> <@346035824439328782>\n`[p]help owner changestatus`\n`[p]help owner postaction`\n`[p]load <cog_name>` : Charge un cog\n`[p]unload <cog_name>` : Décharge un cog\n`[p]reload <cog_name>` : Recharge un cog\n`[p]shutdown` : Ferme le bot\n`[p]coglist` : Affiche la list des cog dispo"
            embed = Embed(title="Help Owner", description=description, colour=ctx.author.colour)
            await ctx.send(embed=embed)

    #Owner change status
    @help_owner.command(name="changestatus")
    @commands.check(bot_owner)
    async def help_owner_changestatus(self, ctx):
        description = "`[p]changestatus none` : Set l'activité du bot a rien\n`[p]changestatus playing <activity>` : Change l'activité du bot\n`[p]changestatus listening <activity>` : Change l'activité du bot\n`[p]changestatus watching <activity>` : Change l'activité du bot"
        embed = Embed(title="Change Status Help", description=description, colour=ctx.author.colour)
        await ctx.send(embed=embed)

    #Owner post Action
    @help_owner.command(name="postaction")
    @commands.check(bot_owner)
    async def help_owner_postaction(self, ctx):
        description = "`[p]post <channel> <nombre> <message>` : Envoie un message dans un salon avec un nombre défini\n`[p]botdm <user> <nombre> <message>` : Envoie un mp avec un nombre défini"
        embed = Embed(title="Post Action Help", description=description, colour=ctx.author.colour)
        await ctx.send(embed=embed)

    #Staff commande
    @commands.has_permissions(administrator=True)
    @help.group(name="staff")
    async def help_staff(self, ctx) -> None:
        description = "COMMANDE RESERVER AU STAFF\n`[p]mute <user> [reason]` : Mute un utilisateur\n`[p]unmute <user> [reason]` : Unmute un utilisateur\n`[p]ban <user> [reason]` : Ban un utilisateur\n`[p]unban <user> [reason]` : Unban un utilisateur\n`[p]kick <user> [reason]` :  kick un utilisateur du serveur"
        embed = Embed(title="Help Staff", description=description, colour=ctx.author.colour)
        await ctx.send(embed=embed)

    #Fun choice Api or Fun
    @help.group(name="fun")
    async def help_fun(self, ctx):
        if ctx.invoked_subcommand is None:
            description = "`[p]help fun api`\n`[p]help fun cmd`"
            embed = Embed(title="Fun Choice Help", description=description, colour=ctx.author.colour)
            await ctx.send(embed=embed)

    #Fun api
    @help_fun.command(name="api")
    async def help_fun_api(self, ctx):
        description = "`[p]meme` : Pour afficher un meme(En anglais)\n`[p]cat` : Montre une photo de chat random\n`[p]dog` : Affiche une photo d'un chien random\n`[p]waifu <waifu_neko_cry_hug_kiss_pat_blush_happy_wink_dance`"
        embed = Embed(title="Fun Api Help", description=description, colour=ctx.author.colour)
        await ctx.send(embed=embed)

    #Fun cmd
    @help_fun.command(name="cmd")
    async def help_fun_cmd(self, ctx):
        description = "`[p]tk [p]johns [p]cafe [p]ptdrtki [p]wallah`\n`[p]bigflo [p]allah [p]rng [p]weeb [p]kaak`\n`[p]daisuke [p]paak [p]yume [p]paa [p]quenini`\n`[p]darkshark [p]callthepolice`\n`[p]randomssbu` : Prends un personnage de Super Smash Bros. Ultimate au hasard\n`[p]randomssbm` : Prends un personnage de Super Smash Bros. Melee au hasard\n`[p]flip` : Pile ou Face\n`[p]oof` : oof un message\n`[p]quiaimetu <user_one> <user_two>` : Le bot choisi qui il préfère entre 2 utilisateur"
        embed = Embed(title="Fun Command Help", description=description, colour=ctx.author.colour)
        await ctx.send(embed=embed)

    #Musique
    @help.group(name="musique")
    async def help_musique(self, ctx):
        description = "`[p]play <link>` : Lancer une musique dans un vocal\n`[p]leave` : Fait quitté le bot du vocal\n`[p]pause` : Mets en pause votre musique\n`[p]resume` : Reprends votre musique en cours\n`[p]skip` : Change de piste\n`[p]tracklist` : Affiche la liste des musique en cours et prochaine"
        embed = Embed(title="Help Musique", description=description, colour=ctx.author.colour)
        await ctx.send(embed=embed)

    #Matchmaking
    @help.group(name="matchmaking")
    async def help_matchmaking(self, ctx):
        description = "`[p]matchmaking <user>` : Ouvre un Salon de Matchmaking pour 2 personne\n`[p]finishFight` : Ferme le salon de matchmaking que vous utiliser\n`[p]adduser <user>` : Ajoute un joueur a votre salon\n\n ADMIN UNIQUEMENT :\n`[p]adminMatchmaking <user_one> <user_two>` : Ouvre un salon matchmaking pour les 2 joueur"
        embed = Embed(title="Help Matchmaking", description=description, colour=ctx.author.colour)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
