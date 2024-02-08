from discord.ext import commands
import discord
import responses
import random

TOKEN = *
CHANNEL = 1173149464417022022
OWNER = 235236034101772289


bot = commands.Bot(command_prefix="}", intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

user_counter = {} # counter = 0
user_join_timestamps = {} # Dictionary to store the message count since joining for each user
user_message_counts = {} # creates a dictionary to store counter for unique users

@bot.event
async def on_ready():
    print("Police is on duty.")
    channel = bot.get_channel(CHANNEL)
    await channel.send("I am on duty.")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello there.")

@bot.command()
async def roll(ctx):
    await ctx.send(random.randint(1, 100))

@bot.command()
async def creator(ctx):
    member = bot.get_user(OWNER)
    await ctx.send(f"{member.mention} created me.")

@bot.command()
async def me(ctx):
    user_id = ctx.author.id
    user = bot.get_user(user_id)
    embed = discord.Embed(
        title = f'User Information | {ctx.author.name}',
        color = discord.Color.dark_purple()
    )
    embed.set_thumbnail(url = user.avatar.url)
    embed.add_field(name = 'Joined Server', value = ctx.author.joined_at.strftime('%Y-%m-%d %H:%M:%S'), inline = False)

    # no way to count total messages w/o blowing up pc 
    # if user_id in user_join_timestamps:

    #     total_messages = 0

    #     async for message in ctx.channel.history(limit=None):
    #         if message.author.id == user_id:
    #             total_messages += 1

    #     embed.add_field(name='Total Messages', value=total_messages, inline=False)


    await ctx.send(embed = embed)

@bot.event
async def on_member_join(member):
    welcome_channel_id = 583512696423448577
    welcome_channel = member.guild.get_channel(welcome_channel_id)

    rules_channel_id = 583514050080669697
    rules_channel = member.guild.get_channel(rules_channel_id)

    if welcome_channel:
        embed = discord.Embed(
            title = f'Welcome to {member.guild.name}!',
            description = f'We hope you enjoy your stay, {member.mention}.\nHead over to {rules_channel.mention} to see our server rules!',
            color = discord.Color.dark_purple()
        )
        embed.set_thumbnail(url = member.avatar.url)
        await welcome_channel.send(embed = embed)


@bot.event
async def on_message(message):

    if message.author == client.user: # infinite loop check bc client user will be bot     
        return

    global counter 
    user_id = message.author.id

    if user_id not in user_counter:
            user_counter[user_id] = 0

    if 'fuck' in message.content.lower():
        user_counter[user_id] += 1
        await message.channel.send("Watch your profanity!")

        if user_counter[user_id] == 3:
            await message.author.send("Stop saying that word.")
        
        if user_counter[user_id] == 5:
            await message.author.send("I already warned you once, don't let it happen again.")


    if 'ethan' in message.content.lower():
        await message.channel.send("<:squadR:770517495500898314>")

    if 'james' in message.content.lower():
        await message.channel.send("<:behemoth:1173883269901733929>")

    await bot.process_commands(message)

bot.run(TOKEN)

