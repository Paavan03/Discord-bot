import discord
import random
from discord.ext import commands, tasks
import youtube_dl
from random import choice

TOKEN = ('NzU2ODEwNDMzMTI5NzQyMzM3.X2XQpA.JDrabfNWG3BTY3ozsUnsI9RRaTc')

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(help='This command will give you random quotes')
async def quote(ctx):
    responses = ['If you don’t share someone’s pain, you can never understand them. – Nagato',
                 'The concept of hope is nothing more than giving up. A word that holds no true meaning.  – Madara Uchiha',
                 'The longer you live… The more you realize that reality is just made of pain, suffering and emptiness.  – Madara Uchiha',
                 'When a man learns to love, he must bear the risk of hatred.  – Madara Uchiha',
                 'It is only through the eyes of others that our lives have any meaning.  – Haku',
                 'Rejection is a part of any man’s life. If you can’t accept and move past rejection, or at least use it as writing material – you’re not a real man.  – Jiraiya',
                 'If you don’t like your destiny, don’t accept it. Instead have the courage to change it the way you want it to be.  – Naruto Uzumaki',
                 'It’s not the face that makes someone a monster, it’s the choices they make with their lives.  – Naruto Uzumaki',
                 f'{ctx.author.name}, your name is already written in my Death Note 39 seconds ago',
                 'People live their lives bound by what they accept as correct and true. That’s how they define “reality”. But what does it mean to be “correct” or “true”? Merely vague concepts… Their “reality” may all be a mirage. Can we consider them to simply be living in their own world, shaped by their beliefs?  – Itachi Uchiha',
                 'Sometimes you must hurt in order to know, fall in order to grow, lose in order to gain because life’s greatest lessons are learned through pain.  – Pain',
                 'Someday, I just want to marry a regular girl who isn’t too ugly and not too pretty. Have two children, first a girl, then a boy. Retire after my daughter is married and my son becomes a successful ninja, and spend the rest of my life playing shōgi or Go. Then die of old age before my wife.  – Nara Shikamaru',
                 'Laziness is the mother of all bad habits. But ultimately she is a mother and we should respect her.  – Nara Shikamaru',
                 'Death is never an apology.  – Brook',
                 'What do you know of death? Have you ever died? You think death will preserve your cause forever? Ridiculous! Death leaves nothing behind! Once a person passes on, nothing remains but dead bones. If there is one thing I can’t stand, it is a person with no respect for life.  – Brook',
                 'A real man is someone who forgives a woman for her lies!  – Sanji',
                 'If you hurt somebody… or if somebody hurts you, the same red blood will be shed.  – Monkey D Luffy',
                 'Power isn’t determined by your size, but the size of your heart and dreams!  – Monkey D Luffy',
                 'Killer Queen has already touched your keyboard',
                 'When do you think people die? When they are shot through the heart by the bullet of a pistol? No. When they are ravaged by an incurable disease? No. When they drink a soup made from a poisonous mushroom!? No! It’s when… they are forgotten.  – Dr. Hiluluk',
                 'It doesn’t matter who your parents were. Everyone is a child of the sea.  – Whitebeard',
                 'A man who raises his hands on a woman is trash. If I have to become trash in order to survive… It’ll be just like dying.  – Renji Abarai',
                 'You wanted revenge? You’re just making other peoples miserable as you. Revenge is just the path you took to escape your suffering.  – Ichigo Kurosaki',
                 'It’s meaningless to just live, and it’s meaningless to just fight. I want to win.  – Ichigo Kurosaki',
                 'Don’t break anyone’s heart, they only have one. Break their bones, they have 206.  – Ichigo Kurosaki',
                 'Even if no one believes in you, stick out your best and scream your defiance!  – Rukia Kuchiki',
                 'It’s easier to crush a dream than realize one. Forming a bond is infinitely more difficult than breaking one.  – Gin Ichimaru']


    await ctx.send(f'{random.choice(responses)}')
        
client.run(TOKEN)
