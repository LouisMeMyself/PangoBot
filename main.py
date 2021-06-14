# import typing
# import discord
# from pangoBot import Constants
from discord.ext import commands
from pangoBot.PangoBot import PangoBot

# intents = discord.Intents.all()
# intents.members = True
#
# bot = commands.Bot(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!')

pangoBot = PangoBot


@bot.event
async def on_ready():
    """starts pangobot"""
    global pangoBot
    pangoBot = PangoBot(bot)
    await pangoBot.on_ready()


@bot.command()
async def pangopic(ctx):
    """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
    await pangoBot.pangopic(ctx)
#
#
# @bot.command()
# async def suggest(ctx):
#     """command for suggestions"""
#     await pangoBot.suggest(ctx)
#
#
#
# @bot.command()
# async def play(ctx, msg):
#     """command for suggestions"""
#     await pangoBot.play(ctx, msg)
#
#
# @bot.command(pass_context=True)
# @commands.has_role(Constants.ROLE_FOR_CMD)
# async def give_all(ctx, role):
#     """Gives everyone in the server a given role
#     Warning : It can be slow (10 members every 8 seconds) but the bot keeps working even if this command is proceeding"""
#     await pangoBot.give_all(ctx, role)
#
#
# @bot.command(pass_context=True)
# @commands.has_role(Constants.ROLE_FOR_CMD)
# async def remove_all(ctx, role):
#     """Removes a given role to everyone in the server
#     Warning : It can be slow (10 members every 8 seconds) but the bot keeps working even if this command is proceeding"""
#     await pangoBot.remove_all(ctx, role)
#
#
# @bot.command(pass_context=True)
# @commands.has_role(Constants.ROLE_FOR_CMD)
# async def save_server(ctx):
#     await pangoBot.save_server(ctx)
#
#
# @bot.command(pass_context=True)
# @commands.has_role(Constants.ROLE_FOR_CMD)
# async def clear(ctx, number):
#     await pangoBot.clear(ctx, number)
#
#
# @bot.command(pass_context=True)
# @commands.has_role(Constants.ROLE_FOR_CMD)
# async def ban(ctx, members: commands.Greedy[discord.Member],
#               delete_days: typing.Optional[int] = 0, *,
#               reason: str):
#     await pangoBot.ban(ctx, members, delete_days, reason=reason)
#
#
# @bot.event
# async def on_raw_reaction_add(payload):
#     """Add pango role when a reaction is added on a particular message (not a message from pangobot or a
#     reaction of pangobot) """
#     await pangoBot.on_raw_reaction_add(payload)
#
#
# @bot.event
# async def on_raw_reaction_remove(payload):
#     """harder to remove than add a role, to do"""
#     await pangoBot.on_raw_reaction_remove(payload)
#
#
@bot.event
async def on_command_error(ctx, error):
    await pangoBot.on_command_error(ctx, error)


if __name__ == '__main__':
    with open(".key", "r") as f:
        key = f.read().replace("\n", "")
    bot.run(key)
