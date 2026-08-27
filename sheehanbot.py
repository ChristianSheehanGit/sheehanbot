# import discord
# import random
# from discord.ext import commands

# bot = commands.Bot(command_prefix='.')
bot.remove_command("help")

@bot.command()
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
    "What song do you wish you could put on right now?",
    "Are you a cat person or a dog person?",
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
    "What are your thoughts on the British royal family?",
    "What was the last funny video you saw?",
    "What do you do to get rid of stress?",
    "What is something you are obsessed with?",
    "What three words best describe you?",
    "What would be your perfect weekend?",
    "What’s your favorite number? Why?",
    "What are you going to do this weekend?",
    "What’s the most useful thing you own?",
    "What’s your favorite way to waste time?",
    "What do you think of tattoos? Do you have any?",
    "Do you have any pets? What are their names?",
    "Where did you go last weekend? / What did you do last weekend?",
    "What is something popular now that annoys you?",
    "What did you do on your last vacation?",
    "When was the last time you worked incredibly hard?",
    "Are you very active, or do you prefer to just relax in your free time?",
    "What do you do when you hang out with your friends?",
    "Who is your oldest friend? Where did you meet them?",
    "What’s the best / worst thing about your work/school?",
    "If you had intro music, what song would it be? Why?",
    "What were you really into when you were a kid?",
     "What’s the funniest TV series you have seen?",
     "What cartoons did you watch as a child?",
        "Which TV show do you want your life to be like?",
    "How have TV shows changed over the years?",
    "If you could bring back one TV show that was canceled, which one would you bring back?",
    "What do you think about game shows? Do you have a favorite one?",
   "What’s the most underrated or overrated TV show?",
     "What do you think about reality TV? Why do you think it’s so popular?",
     "Which do you prefer? Books or movies?",
    "How are you consciously practicing sustainability?",
    "Do you have any tattoos?",
     "What are you most grateful for in this season of life?",
     "Do you give back or volunteer with any organizations?",
     "What do you look for and need in your friendships?",
     "How do you feel that you best offer love and support to your friends?",
     "When do you feel most authentically yourself?",
     "Tell me about your childhood best friend.",
     "What's one form of self-expression you've been too hesitant to explore?",
      "What's one habit you want to get rid of and one habit you want to keep? ",
      "If you were to perform a duet with a famous musician, who would it be and why?",
      "Do you have any recurring dreams? If so, what do you think they are trying to tell you?",
    "Who do you most admire, and how has that impacted the way you live your life?",
      "What’s your earliest memory?",
      "What do you love most about school?",
        "Who are your best friends?",
        "What is your favorite season?"
    ]
    await ctx.send(random.choice(questions))

@bot.command()
#async def help(ctx):
    await ctx.reply("Hey Sheefan, I am SheehanBot.\n\nHere are the things I can do:\n\n.topic - conversation starter\n.frogfact - frog fact\n\nthat's it.")
    
@bot.command()
#async def toth(ctx):
    await ctx.reply("I love Dustin Toth! :lmao54:")
    
@bot.command()
#async def version(ctx):
    await ctx.reply("1.02") 

@bot.command()
#async def poll(ctx, *, text):
    message = await ctx.send(text)
    for emoji in ('👍', '👎'):
        await message.add_reaction(emoji)
    

    
@bot.command()
async def frogfact(ctx):
    frogfacts = [
      "Did you know that frogs absorb water through their skin so they don't need to drink?",
      "Did you know that frogs can lay as many as 4,000 eggs in frogspawn?",
      "Did you know that the eyes and nose of a frog are on top of its head so it can breathe and see when most of its body is under the water?",
      "Did you know that frogs have long back legs and webbed feet for jumping and swimming?",
      "Did you know that there are over 4,700 species of frogs?",
      "Did you know that every year that a frog goes into hibernation, a new layer of bone forms?",
      "Did you know that many frogs can jump 20 times their own height?",
      "Did you know that frogs come in all sorts of colours?",
      "Did you know that the study of amphibians and reptiles is called Herpetology, and those who study them are called Herpetologists?",
      "Did you know that frogs cannot live in the sea or any salt water?",
     "Did you know that frogs moult? This is the process where they shed their skin.",
      "Did you know that croaking is used by male frogs as a way to attract females?",
      "Did you know that frogs have teeth on their upper jaw, which they use to keep their prey in one place until they can swallow it?",
      "Did you know that frogs don’t drink water with their mouths; they “drink” by absorbing water through their skin?",
      "Did you know that one gram of the toxin produced by the skin of the golden poison dart frog could kill 100,000 people?",
      "Did you know that when a frog swallows its prey, it blinks, which pushes its eyeballs down on top of the mouth to help push the food down its throat?",
      "Did you know that a group of birds is called a flock, a group of cattle is called a herd, but a group of frogs is called an army?",
      "Did you know that there is a frog in Indonesia that has no lungs – it breathes entirely through its skin?",
      "Did you know that there’s a type of poison dart frog called the blue-jeans frog; it has a red body with blue legs. It is also sometimes called the strawberry dart frog?",
      "Did you know that the red-eyed tree frog lays it eggs on the underside of leaves that hang over water. When the eggs hatch, the tadpoles fall into the water below?",
      "Did you know that the biggest frog in the world is the Goliath frog? It lives in West Africa and can measure more than a foot in length and weigh more than 7 pounds – as much as a newborn baby.",
      "Did you know that most frogs have teeth, although usually only on their upper jaw? The teeth are used to hold prey in place until the frog can swallow it.",
      "Did you know that the waxy monkey frog secretes a wax from its neck and uses its legs to rub that wax all over its body? The wax prevents the skin of the frog from drying out in sunlight.",
      "Did you know that when a frog swallows its prey, it blinks, which pushes its eyeballs down on top of the mouth to help push the food down its throat?",
      "Did you know that frogs are amphibians?",
    ]
    await ctx.reply(random.choice(frogfacts))

bot.run("REDACTED")
