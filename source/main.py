import discord
from discord.ext import commands
import logging
import asyncio
import json
import website_integration

# BOT LOGGING

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='picklerickbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

description = '''I'm Pickle Rickbot!!'''

# this specifies what extensions to load when the bot starts up
startup_extensions = ["general", "moderator", "music", "admin"]

bot = commands.Bot(command_prefix='!', description="I'm Pickle Rickbot!")

async def auto_bump_hound():
    await bot.wait_until_ready()
    channel = bot.get_channel('341966943768805376')
    while not bot.is_closed:
        await bot.send_message(channel, "=bump")
        await asyncio.sleep(14400)  # task runs every 60 seconds

async def website_integration():
    await bot.wait_until_ready()
    while not bot.is_closed:
        # Check here for messages
        with open("pickle.json", "r") as f:
            com = json.loads(f.read())
        if len(com['queue']) > 0:
            # We have new tasks
            for task in com['queue']:
                website_integration.handle(task)
        com['queue'] = []
        with open("pickle.json", "w") as f:
            f.write(json.dumps(com))
        await asyncio.sleep(0.2)

async def auto_bump_dlm():
    await bot.wait_until_ready()
    channel = bot.get_channel('341966943768805376')
    while not bot.is_closed:
        await bot.send_message(channel, "dlm!bump")
        await asyncio.sleep(21600)  # task runs every 60 seconds


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='Science and Stuff'))


# Welcome Message
@bot.event
async def on_member_join(member):
    # Define Channels
    channel_general = bot.get_channel('341377562192248854')
    channel_info = bot.get_channel('341377717297610763')
    channel_updates = bot.get_channel('341377770741432330')

    wmsg = "Hey everyone, get a load of {0.mention} over here. ***burp*** They're new and stuff.".format(member)

    wpm = "Hey, ***burp*** hey you. Welcome to **codeHOME**. Good to have you here (so far). First things " \
          "first, take a look at the {0.mention} channel; it has lots of information about our community. " \
          "Important news will be posted in {1.mention}. Finally, we have a friendly bot, me, Pickle Rickbot! " \
          " If you have any questions, feel free to ask in the server; and again " \
          "welcome and thanks for joining. Wubalubadubdub!".format(channel_info, channel_updates)

    # Send Welcome Message to general channel
    await bot.send_message(channel_general, wmsg)

    # Send Private Welcome Message
    await bot.send_message(member, wpm)


# Allow Events to be processed on message, then process commands.
@bot.event
async def on_message(message):

    # Process the rest of the Commands
    await bot.process_commands(message)


# Goodbye Message
# @bot.event
# async def on_member_remove(member):
#    channel = bot.get_channel('108369515502411776')
#    fmt = ":wave: Goodbye {0}, we're sad to see you go!".format(member.name)
#    await bot.send_message(channel, fmt)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.loop.create_task(auto_bump_hound())
    bot.loop.create_task(auto_bump_dlm())
    bot.loop.create_task(website_integration())
    bot.run('')
