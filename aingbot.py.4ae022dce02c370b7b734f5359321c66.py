##아잉봇 메인코드
import asyncio
import discord
import random
from discord.ext import commands
import time
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token = os.environ.get("AING_PSW")

client = commands.Bot(command_prefix= '~')


@client.event
async def bt(games):
    await client.wait_until_ready()
    while not client.is_closed():
        for g in games:
            await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(4)

@client.event
async def on_ready():
    await bt(['아잉', '암유발자 최고','기모띠'])



@client.event
async def on_message(message): 
    msg = message.content
    
    
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.
    else:
        author = str(message.author.nick)
        #or_author = str(message.author)

        if author == "None":
            author = str(message.author)
            author = author[:-5]

        else:
            None
        #print(author + ': ' + msg)

        #m_msg = str(input('입력'))
        #print(m_msg)
    #if author == '암유발자비없는사람':
        #await message.channel.send(msg)
    

    if '아잉' == msg:
        await message.channel.send(file=discord.File('./pic/aing_{}.png'.format(str(random.randint(0,6)))))
        await message.channel.send("아잉") 
        channel = message.author.voice.channel
        audio_source = discord.FFmpegPCMAudio("./pic/toong.mp3")
        try:
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="./pic/toong.mp3"))
        except:
            #discord.VoiceClient.play(discord.FFmpegPCMAudio(source="./pic/toong.mp3"))
            #discord.VoiceClient.play(discord.FFmpegPCMAudio(source="./pic/toong.mp3"))
            voice_client = discord.VoiceClient = discord.utils.get(client.voice_clients)
            audio_source = discord.FFmpegPCMAudio("./pic/toong.mp3")
            if not voice_client.is_playing():
                voice_client.play(audio_source)

    elif '사랑해요 아이유' == msg:
        #await message.channel.send(file=discord.File('./pic/aing_{}.png'.format(str(random.randrange(0,6)))))
        await message.channel.send("나도아잉유") 
        channel = message.author.voice.channel
        try:
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="./pic/music.mp3"))
        except:
            #discord.VoiceClient.play(discord.FFmpegPCMAudio(source="./pic/toong.mp3"))
            #discord.VoiceClient.play(discord.FFmpegPCMAudio(source="./pic/toong.mp3"))
            voice_client = discord.VoiceClient = discord.utils.get(client.voice_clients)
            audio_source = discord.FFmpegPCMAudio("./pic/music.mp3")
            if not voice_client.is_playing():
                voice_client.play(audio_source, after=None)
    else:
        None

        #await asyncio.sleep(4)
        #await vc.disconnect()
        
        
        #voice_channel = message.author.voice.voice_channel
        #await bot.join_voice_channel(voice_channel)
        
         
client.run(token,bot = True)
            

             


