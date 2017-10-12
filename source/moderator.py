import discord
from discord.ext import commands
from helpers import db


# ********************************************** #
# MODERATOR COMMANDS *************************** #
# ********************************************** #

class Moderator:
    def __init__(self, bot):
        self.bot = bot

    # COMMAND: !set_game
    @commands.command()
    @commands.has_any_role("Administrator", "Moderator")
    async def set_game(self, *, game_name: str):
        """Sets Clifford's currently playing game.."""

        await self.bot.change_presence(game=discord.Game(name=game_name))

    # COMMAND: !kick
    @commands.command(name='kick', pass_context=True)
    @commands.has_any_role("Administrator", "Moderator")
    async def mod_kick(self, ctx, username: str, *, reason: str):
        """Kicks a user from the server."""

        # Add to DB and Post Message
        try:
            # Variables Needed
            member = discord.utils.get(ctx.message.server.members, name=username)
            staffer = ctx.message.author

            # Handle Database
            sql = "INSERT INTO mod_log (`action`,`user`, `user_id`, `staff`, `staff_id`, `reason`) " \
                  "VALUES ('kick', %s, %s, %s, %s, %s)"
            cur = db.cursor()
            cur.execute(sql, (str(member), member.id, str(staffer), staffer.id, reason))

            # Save Last Row ID
            case_id = cur.lastrowid

            # Insert Message
            log_channel = self.bot.get_channel('346481061452316672')
            msg_text = "**Case #{0}** | Kick :boot: \n**User**: {1} ({2}) " \
                       "\n**Moderator**: {3} ({4}) \n**Reason**: {5}"

            # Add Message to Events Channel and Save Message ID
            case_message = await self.bot.send_message(log_channel, msg_text.format(case_id, str(member), member.id,
                                                                                    str(staffer), staffer.id, reason))
            cur.execute("UPDATE mod_log SET `message_id` = %s WHERE `case_id` = %s", (case_message.id, case_id))

            # Finish Database Stuff and Commit
            db.commit()
            cur.close()

            # Kick the Member
            await self.bot.kick(member)
        except Exception as e:
            await self.bot.send_message(ctx.message.channel, "{0.mention}, there was an error when kicking the user."
                                                             " ".format(ctx.message.author) + str(e))

        await self.bot.say("{0.mention}, the user was successfully kicked. A log entry has been added."
                           .format(ctx.message.author))

    # COMMAND: !ban
    @commands.command(name='ban', pass_context=True)
    @commands.has_any_role("Administrator", "Moderator")
    async def mod_ban(self, ctx, username: str, *, reason: str):
        """Bans a user from the server."""

        # Add to DB and Post Message
        try:
            # Variables Needed
            member = discord.utils.get(ctx.message.server.members, name=username)
            staffer = ctx.message.author

            # Handle Database
            sql = "INSERT INTO mod_log (`action`,`user`, `user_id`, `staff`, `staff_id`, reason) " \
                  "VALUES ('ban', %s, %s, %s, %s, %s)"
            cur = db.cursor()
            cur.execute(sql, (str(member), member.id, str(staffer), staffer.id, reason))

            # Save Last Row ID
            case_id = cur.lastrowid

            # Insert Message
            log_channel = self.bot.get_channel('346481061452316672')
            msg_text = "**Case #{0}** | Ban :hammer: \n**User**: {1} ({2}) " \
                       "\n**Moderator**: {3} ({4}) \n**Reason**: {5}"

            # Add Message to Events Channel and Save Message ID
            case_message = await self.bot.send_message(log_channel, msg_text.format(case_id, str(member), member.id,
                                                                                    str(staffer), staffer.id, reason))
            cur.execute("UPDATE mod_log SET `message_id` = %s WHERE `case_id` = %s", (case_message.id, case_id))

            # Finish Database Stuff and Commit
            db.commit()
            cur.close()

            # Kick the Member
            await self.bot.ban(member, 0)
        except Exception as e:
            await self.bot.send_message(ctx.message.channel, "{0.mention}, there was an error when banning the user."
                                                        " ".format(ctx.message.author) + str(e))

        await self.bot.say("{0.mention}, the user was successfully banned. A log entry has been added."
                           .format(ctx.message.author))

    # COMMAND: !unban
    @commands.command(name='unban', pass_context=True)
    @commands.has_any_role("Administrator", "Moderator")
    async def mod_unban(self, ctx, username: str, *, reason: str):
        """Unbans a user from the server."""

        # Add to DB and Post Message
        try:
            # Variables Needed
            member = discord.utils.get(self.bot.get_bans(ctx.message.server), name=username)
            staffer = ctx.message.author

            # Handle Database
            sql = "INSERT INTO mod_log (`action`,`user`, `user_id`, `staff`, `staff_id`, reason) " \
                  "VALUES ('unban', %s, %s, %s, %s, %s)"
            cur = db.cursor()
            cur.execute(sql, (str(member), member.id, str(staffer), staffer.id, reason))

            # Save Last Row ID
            case_id = cur.lastrowid

            # Insert Message
            log_channel = self.bot.get_channel('346481061452316672')
            msg_text = "**Case #{0}** | Unban :peace: \n**User**: {1} ({2}) " \
                       "\n**Moderator**: {3} ({4}) \n**Reason**: {5}"

            # Add Message to Events Channel and Save Message ID
            case_message = await self.bot.send_message(log_channel, msg_text.format(case_id, str(member), member.id,
                                                                                    str(staffer), staffer.id, reason))
            cur.execute("UPDATE mod_log SET `message_id` = %s WHERE `case_id` = %s", (case_message.id, case_id))

            # Finish Database Stuff and Commit
            db.commit()
            cur.close()

            # Kick the Member
            await self.bot.ban(member, 0)
        except Exception as e:
            await self.bot.send_message(ctx.message.channel, "{0.mention}, there was an error when unbanning the user."
                                                             " ".format(ctx.message.author) + str(e))

        await self.bot.say("{0.mention}, the user was successfully unbanned. A log entry has been added."
                           .format(ctx.message.author))


def setup(bot):
    bot.add_cog(Moderator(bot))
