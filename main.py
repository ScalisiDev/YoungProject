import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/help'):
        await message.channel.send("/history /daily")
    if message.content.startswith('/history'):
        await message.channel.send("Young project open surce è un nato nel 2024 grazie agli studenti di Kodland. Il progetto ha l'obbiettivo di educare i giovani al riciclo")
    if message.content.startswith("/daily"):
        await message.channel.send("Compiti giornalieri: C.1 Butta la spazzatura; C.2 Dopo il caffé mattutino stacca tutte le prese; C.3 A scuola, butta la carta del panino nella spazzatura (Suggerimento: Alluminio = plastica); C.4 Tornato a casa, dopo aver pranzato, ricordati di staccare il Televisore, che anche in stanby consuma; C.5 Se usi il pc ricorda di abbassare la luminosità, cha anche quella inquina; C.6 La sera, fai la lavatrice a pieno carico")
        
    #il bot è ancora in via di sviluppo
client.run("Token")
