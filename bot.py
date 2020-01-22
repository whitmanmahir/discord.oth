import discord
import random
import time
from discord.ext import commands
from discord.ext import tasks 
from itertools import cycle




client = commands.Bot(command_prefix = '.')
status = cycle(["status 1", "status 2"])



@client.event 
async def on_ready():
    change_status.start()
    print("Bot is ready. ")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
    print(f'{member} has joined. ')

@client.event 
async def on_member_remove(member):
    print(f'{member} has left the server. ')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')



@client.event
async def on_message(message):
    if message.content.startswith('hi'):
        channel = message.channel
        await channel.send(f'Hello {message.author.mention} !')

    if "fuck" in message.content.lower():
        channel = message.channel
        await channel.send(f'No swearing :rage:')

    if message.content.startswith("i'm"):
        name = message.content.split()[1]
        await message.channel.send("Hi " + name + ", I'm dad!")

    if "how are you botyyy" in message.content.lower():
        await message.channel.send(f'I am good thanks, for asking')

    if "nigga" in message.content.lower():
        await message.channel.send(f"DON'T SAY THAT WORD :face_with_symbols_over_mouth:")
        

    
        


        
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('8')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return 







client.run('NjY4MDU4Nzk2NzY5NDExMDgy.XiWWBQ.IdZSU532BXvZ2__oRfepW-ykBJM')
