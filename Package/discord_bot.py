import discord
client = discord.Client(intents=discord.Intents.default())
client.run("MTIyOTQzNjQ1MjY2NDc3NDY1OA.GMKPR2.RKJQQ8H6kIXvwk4KQeDC6OAr91dK4oOMqgE8R4")
@client.event
async def on_ready():
    print(f'{client.user} est connecté au serveur suivant :\n')
    for server in client.guilds:
        print(f'{server.name}(id: {server.id})')
