import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
bot.remove_command("help")

@bot.command()
async def help(ctx):
    await ctx.reply("Hey Sheefan, I'm SheehanBot.\n\nHere are the things I can do:\n\n.topic - conversation starter\n\nthat's it.")

async def topic(ctx):
    questions = [
    "Have you done anything exciting lately?", 
    "Have you done anything exciting lately?", 
    "What’s your favorite form of social media?", 
    "What was the last good book you read?", 
    "Do you listen to any podcasts? Which is your favorite?", 
    "What do you think is the best show on Netflix right now?", 
    "Have you been on any interesting trips lately?", 
    "What do you think has been the best movie of the year so far?", 
    "What song do you wish you could put on right now?"
    , "Are you a cat person or a dog person?",
    "Are you a cat person or a dog person?",
    "If you didn’t have the job you have now, what would you be?",
    "What’s your strangest hidden talent?",
    "What is something people are always surprised to learn about you?",
    "What is the most rewarding part of your career?",
    "Where do you want to be in five years?",
    "What superpower do you wish you could have?",
    "Where would you go on vacation if you had no budget?",
    "If you could travel back in time, what decade would you choose to live in?",
    "What’s the best thing you’ve ever bought off Amazon?",
    "What’s the last concert you went to?",
    "What is one thing you can’t live without?",
    "What’s the strangest dream you’ve had recently?",
    "What is your favorite book of all time?",
    "How many countries have you been to?",
    "What’s your favorite city you’ve visited?",
    "Would you rather travel via plane or boat?",
    "Would you rather be really hot or really cold?",
    "What are your thoughts on the British royal family?"
    ]
    await ctx.reply(random.choice(questions))

bot.run("OTQyMjYxMjIwMTU1NzQ4NDMz.Ygh7JQ.jhmcBCUnYOaBhHfwEoV2t26DN7M")
