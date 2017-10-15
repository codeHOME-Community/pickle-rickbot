# Coldly stolen from https://github.com/Rapptz/RoboDanny/blob/master/cogs/admin.py

# Copyright (c) 2015 Rapptz
# Copyright (c) 2017 codeHOME
# Licensed under MIT.

from discord.ext import commands
import discord
import inspect

class Admin:
    """Admin-only commands that make the bot dynamic."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.has_role("Administrator")
    async def loadcog(self, *, module : str):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await self.bot.say('Wow, great job, _Morty_. Your dumb {} cog blew up in my face.'
                               .format(module))
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('WUBBA LUBBA DUB DUB! {} was, uh, loaded successfully, Morty.'
                               .format(module))

    @commands.command(hidden=True)
    @commands.has_role("Administrator")
    async def unloadcog(self, *, module : str):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await self.bot.say('Wow, great job, _Morty_. Your dumb {} cog can\'t even unload properly.'
                               .format(module))
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('I shoved that {} cog waaaaay up inside your butthole, Morty.'
                               .format(module))

    @commands.command(name='reloadcog', hidden=True)
    @commands.has_role("Administrator")
    async def _reload(self, *, module : str):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await self.bot.say('Wow, great job, _Morty_. Your dumb cog blew up in my face.')
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('WUBBA LUBBA DUB DUB! {} was, uh, reloaded successfully, Morty.'
                               .format(module))

    # Eval is pretty risky, disable this.
    # @commands.command(pass_context=True, hidden=True)
    # @checks.is_owner()
    # async def debug(self, ctx, *, code : str):
    #     """Evaluates code."""
    #     code = code.strip('` ')
    #     python = '```py\n{}\n```'
    #     result = None
    #
    #     env = {
    #         'bot': self.bot,
    #         'ctx': ctx,
    #         'message': ctx.message,
    #         'server': ctx.message.server,
    #         'channel': ctx.message.channel,
    #         'author': ctx.message.author
    #     }
    #
    #     env.update(globals())
    #
    #     try:
    #         result = eval(code, env)
    #         if inspect.isawaitable(result):
    #             result = await result
    #     except Exception as e:
    #         await self.bot.say(python.format(type(e).__name__ + ': ' + str(e)))
    #         return
    #
    #     await self.bot.say(python.format(result))

def setup(bot):
    bot.add_cog(Admin(bot))
