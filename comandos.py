import random as r, string as s, discord, os

def psw(lend):
    
    elements = s.ascii_letters + s.ascii_uppercase + s.digits + s.punctuation
    
    password = ""

    for i in range (lend):
        password += r.choice(elements)
        return password

def flip_coin():
    coin = ['CARA', 'SELLO']
    return r.choice(coin)
    
def memep():
    with open("IMG/Juan.jpeg", "rb") as mm:
        picture = discord.File(mm)
    return picture
   
def memepp():
    memesdir = r.choice(os.listdir('IMG'))
    with open (f"IMG/{memesdir}", "rb") as f:
        picture = discord.File(f)
    return picture
    
    
