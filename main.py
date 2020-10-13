from pathlib import Path
from pytube import YouTube
from youtube_search import YoutubeSearch
from discord.ext import commands
import discord
import os
from WebServer import keep_alive
song_bot = commands.Bot(command_prefix='.')
save_directory = Path.home() / 'Desktop'
TOKEN = 'YOUR_DISCORD_BOT_TOKEN_HERE'

@song_bot.event
async def on_ready():
    print('Song Bot ready')

@song_bot.command()
async def download(ctx, *, song):
    song_new = song+' lyrics'
    results = YoutubeSearch(song_new, max_results=1).to_dict()
    vid = results[0]
    vid_url = 'https://www.youtube.com/' + vid['url_suffix']
    video = YouTube(url=vid_url)
    stream = video.streams.filter(only_audio=True).first()
    await ctx.send('The file is now sent to you, Thanks!')
    await ctx.send(file=discord.File(stream.download(filename=song)))
    os.remove(song+'.mp4')

@song_bot.command()
async def info(ctx):
    await ctx.send('This is Mr.SongDownloader by Ahaan and this bot can download any song you want. Thanks!')

keep_alive()
song_bot.run(TOKEN)

