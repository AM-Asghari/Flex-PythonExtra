import discord

client = discord.Client()

@client.event
async def on_ready():
    # De bot kan op veel verschillende servers draaien. Met deze regel code pak je de eerste server die deze bot heeft. Als jouw bot maar 1 server heeft is het makkelijk.
    guild = client.guilds[0]
    
    # De naam van de server printen we gelijk uit.
    print(guild.name, "is the name of the server")

    # We printen de naam van de bot user uit.
    print(client.user, "has connected to the client")
    
    channel = guild.text_channels[0]
    print(channel.name, "is the name of the channel")
    await channel.send("I'm online!")



client.run("ODk2MDE1NzE4OTgwNjUzMDg3.YWA9qg.KHMhcwZ85nBPEROqJ7pTA1WH7ic")