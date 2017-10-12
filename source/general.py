import discord
from discord.ext import commands
import random


class General:
    def __init__(self, bot):
        self.bot = bot

    # ********************************************** #
    # UN-GROUPED BOT COMMANDS ********************** #
    # ********************************************** #

    # Load Extension
    @commands.command(pass_context=True)
    @commands.has_role("Administrator")
    async def load(self, ctx, extension_name: str):
        """Loads an extension."""

        try:
            self.bot.load_extension(extension_name)
        except (AttributeError, ImportError) as ex:
            await self.bot.say("```py\n{}: {}\n```".format(type(ex).__name__, str(ex)))
            return
        await self.bot.say("{} loaded.".format(extension_name))

    # Unload Extension
    @commands.command(pass_context=True)
    @commands.has_role("Administrator")
    async def unload(self, ctx, extension_name: str):
        """Unloads an extension."""

        self.bot.unload_extension(extension_name)
        await self.bot.say("{} unloaded.".format(extension_name))

    # COMMAND: !hello
    @commands.command(pass_context=True)
    async def hello(self, ctx):
        """Say hello to Pickle Rickbot, and he might take the time to acknowledge you exist."""
        # we do not want the bot to reply to itself
        if ctx.message.author == self.bot.user:
            return
        else:
            msg = "What up {0.message.author.mention}? I'm Pickle Rickbot!".format(ctx)
            await self.bot.send_message(ctx.message.channel, msg)

    # COMMAND: !ask
    @commands.command(pass_context=True)
    async def ask(self, ctx):
        """A simple reminder to ask questions in appropriate places."""

        msg = "Hey *Morty*. Be sure to ask your question straight away, and in the appropriate channel. You don't " \
              "need permission to ask a question. ***burp*** So go ahead and ask away, but be sure it's in the best " \
              "#channel for the question. You'll be more likely to get an answer that way."

        await self.bot.send_message(ctx.message.channel, msg)
        
    # COMMAND: !markdown
    @commands.command()
    async def markdown(self):
        """Get the lowdown about Discord markdown."""
        
        msg = "Read up about ***burp*** Discord's markdown here genius. " \
              "https://support.discordapp.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-"
        
        await self.bot.say(msg)

    # COMMAND: !profile
    @commands.command(pass_context=True)
    async def profile(self, ctx):
        """The profile template for new staff."""

        msg = "Here's the template for the staff profile, you *Morty*.\n" \
               "```\n" \
               "**Name/Alias**:\n" \
              "**Best-Known Language**:\n" \
              "**Proficient Languages**:\n" \
              "**Familiar Frameworks**:\n" \
              "**Areas of Interest**:\n" \
              "**Fun Fact**:\n" \
              "```"

        await self.bot.send_message(ctx.message.channel, msg)

    # COMMAND: !pickle
    @commands.command()
    async def pickle(self):
        """Let me explain to you why I turned myself into a pickle, Morty."""

        # Answers List
        answers = ["I don't do magic *Morty*, I do science. One takes brains, the other takes dark eyeliner.",
                   "Stop digging for hidden layers and just be impressed. I'm a pickle.",
                   "The reason anyone would do this, if they could, which they can't, would be because they could, which they can't."]

        # Send the Answer
        await self.bot.say(random.choice(answers))

    # COMMAND: !rick
    @commands.command()
    async def rick(self):
        """Read some of the amazing things I've said, which is everything."""

        quotes = [
            "Listen, Morty, I hate to break it to you, but what people call *love* is just a chemical reaction that compels animals to breed. It hits hard, Morty, then it slowly fades, leaving you stranded in a failing marriage. I did it. Your parents are gonna do it. Break the cycle, Morty. Rise above. Focus on science.",
            "Sometimes science is more art than science, Morty. Lot of people don't get that.",
            "Stupid-ass fart-saving carpet store motherfucker.",
            "Uncertainty is inherently unsustainable. Eventually, everything either is or isn't.",
            "Listen, I'm not the nicest guy in the universe, because I'm the smartest, and being nice is something stupid people do to hedge their bets.",
            "The first rule of space travel kids is always check out distress beacons. Nine out of ten times it's a ship full of dead aliens and a bunch of free shit! One out of ten times it's a deadly trap, but... I'm ready to roll those dice!",
            "Don't break an arm jerking yourself off, Morty.",
            "Great, now I have to take over a whole planet because of your stupid boobs.",
            "Oh, great adventure, buddy. Rick and Morty go to a giant prison. You know if someone drops the soap it's going to land on our heads and crush our spines, Morty. You know, it'll be really easy to rape us after that."
        ]

        # Send the Quote
        await self.bot.say(random.choice(quotes))

    # COMMAND: !8ball
    @commands.command(name='8ball', pass_context=True)
    async def eightball(self, ctx, question: str):
        """Rolls a magic 8-ball to answer any question you have."""

        if not question:
            await self.bot.say("Umm, hello {0.message.author.mention}? You didn't ask a question.".format(ctx))
            return

        # Answers List (Classic 8-Ball, 20 Answers)
        answers = ['It is certain.',
                   'It is decidedly so',
                   'Without a doubt.',
                   'Yes, definitely.',
                   'You may rely on it.',
                   'As I see it, yes.',
                   'Most likely.',
                   'Outlook good.',
                   'Yes.',
                   'Signs point to yes.',
                   'Reply hazy; try again.',
                   'Ask again later.',
                   'Better not tell you now.',
                   'Cannot predict now.',
                   'Concentrate, then ask again.',
                   'Do not count on it.',
                   'My reply is no.',
                   'My sources say no.',
                   'Outlook not so good.',
                   'Very doubtful.']

        # Send the Answer
        await self.bot.say('{0.message.author.mention}, '.format(ctx) + random.choice(answers))

    # COMMAND: !roll
    @commands.command()
    async def roll(self, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    # COMMAND: !serverinfo
    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """Displays Information about the Server."""

        # Regions Dictionary
        region_dictionary = {"us-west": "US West",
                             "us-east": "US East",
                             "us-central": "US Central",
                             "eu-west": "EU West",
                             "eu-central": "EU Central",
                             "singapore": "Singapore",
                             "london": "London",
                             "syndey": "Sydney",
                             "amsterdam": "Amsterdam",
                             "frankfurt": "Frankfurt",
                             "brazil": "Brazil"}

        # Online Status
        online_statuses = ["online", "idle", "dnd", "do_not_disturb"]

        # GET EMBED INFO
        server = ctx.message.server
        server_name = server.name
        server_region = region_dictionary[str(server.region)]
        server_date = server.created_at.strftime('%B %d, %Y')
        server_icon = server.icon_url
        server_total_members = server.member_count
        server_id = server.id
        server_owner = server.owner
        server_online_members = sum(1 for member in server.members if str(member.status) in online_statuses)
        server_text_channels = sum(1 for channel in server.channels if str(channel.type) == "text")
        server_voice_channels = sum(1 for channel in server.channels if str(channel.type) == "voice")
        server_roles = sorted(server.roles, key=lambda role: role.position, reverse=True)
        server_roles_list = ", ".join(role.name for role in server_roles if role.hoist is True)

        # Create Embed Table
        embed = discord.Embed(title=server_name, colour=1149215,
                              description="Created on " + server_date)
        embed.set_thumbnail(url=server_icon)
        embed.set_footer(text="Server ID: " + server_id)
        embed.add_field(name="Owner", value="{0.mention}".format(server_owner), inline=True)
        embed.add_field(name="Location", value=server_region, inline=True)
        embed.add_field(name="Online Members", value=server_online_members, inline=True)
        embed.add_field(name="Total Members", value=server_total_members, inline=True)
        embed.add_field(name="Text Channels", value=server_text_channels, inline=True)
        embed.add_field(name="Voice Channels", value=server_voice_channels, inline=True)
        embed.add_field(name="Roles", value=server_roles_list, inline=False)

        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
