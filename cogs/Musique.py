import discord, random, youtube_dl, asyncio, json

from discord import Embed, PCMVolumeTransformer
from discord.ext import commands, tasks
from discord.utils import get

musics = {}
ytdl = youtube_dl.YoutubeDL()

list_track = []


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]


class cmd_musique(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def play_song(self, client, queue, song):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url, before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

        def next(_):
            if len(queue) > 0:
                new_song = queue[0]
                del queue[0]
                self.play_song(client, queue, new_song)
                del list_track[0]
            else:
                asyncio.run_coroutine_threadsafe(client.disconnect(), self.bot.loop)
                list_track.clear()

        client.play(source, after=next)

    
    @commands.command()
    async def leave(self, ctx):
        client = ctx.guild.voice_client
        await client.disconnect()
        musics[ctx.guild] = []
        list_track.clear()

    @commands.command()
    async def resume(self, ctx):
        client = ctx.guild.voice_client
        if client.is_paused():
            client.resume()

    @commands.command()
    async def pause(self, ctx):
        client = ctx.guild.voice_client
        if not client.is_paused():
            client.pause()

    @commands.command()
    async def skip(self, ctx):
        client = ctx.guild.voice_client
        client.stop()

    @commands.command()
    async def play(self, ctx, url):
        print("play")
        client = ctx.guild.voice_client

        #Si le bot est déjà dans un salon voc
        if client and client.channel:
            video = Video(url)
            musics[ctx.guild].append(video)
            await ctx.send("Je ajoute votre musique a la list !")
            list_track.append(url)
        else:
            channel = ctx.author.voice.channel
            video = Video(url)
            musics[ctx.guild] = []
            client = await channel.connect()
            await ctx.send(f"Je lance votre musique")
            self.play_song(client, musics[ctx.guild], video)
            list_track.append(url)

    @commands.command(name="tracklist")
    async def track_list(self, ctx):
        client = ctx.guild.voice_client
        if not list_track:
            await ctx.send("Il n'y a pas de musique en cours")
        else:
            embed = Embed(title="List en cours", colour=ctx.author.colour)
            embed.add_field(name="List de chanson", value=list_track, inline=False)
            await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(cmd_musique(bot))