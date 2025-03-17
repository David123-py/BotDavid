import discord
def etiqueta_ambiente():
    embed= discord.Embed(
        title= 'Como evitar el plastico contaminante',
        description= 'Se trata de como ser mas ecologico con los plasticos que puedan llegar a contaminar',
        color= 0xAEEA94
        
    )
    embed.add_field(
        name= 'como reusarlo?',
        value= """- No usar platos desechables /n
            - Usar recipientes de vidrio /n
            - Lavar las botellas de plastico /n"""
    )
    
    embed.set_thumbnail(
        url = "https://i.postimg.cc/hPyVSm8P/IMG-COCA-COLA.webp"
    )

    
    return embed