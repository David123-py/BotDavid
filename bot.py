import discord,os, eco
from dotenv import load_dotenv
import comandos as c
from discord.ext import commands
load_dotenv()
token = os.getenv("dt")

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'💥 BOOM! 💥')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

@bot.command(name="passw")
async def passw(ctx, lenght = 25):
    contrsenia = c.psw(lenght)
    await ctx.send(f"La contraseña generada es: {contrsenia}")

@bot.command(name= "memep")
async def memep(ctx):
    pictures = c.memep()
    await ctx.send(file = pictures)

@bot.command(name= "memepp")
async def memepp(ctx):
    pictures = c.memepp()
    await ctx.send(file = pictures)

@bot.command(name="Eco")
async def Ecologia(ctx, opc:int):
    if opc == 1:
        await ctx.send(embed= eco.etiqueta_ambiente())
    elif opc == 2:
        await ctx.send(embed= eco.etiqueta_ambiente2())
    else:
        await ctx.send("no existe esa opción")



bot.run(token)