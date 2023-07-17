import discord
from discord.ext import commands
intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("O Bot está pronto para uso!")
    print("---------------------------")


@client.command()
async def metamembro(ctx):
    mensagem_metamembro0 = '''https://media.discordapp.net/attachments/1130536072691077221/1130537073531699270/Semanal_1024_40_px.gif'''
    mensagem_metamembro1 = '''**Métodos de Farmar** **_DINHEIRO SUJO_**:

    ```
    • AÇÕES (Lojinha, ammunation, bebidas, joalheria e fleeca)
    • VENDA DE DROGA
    • REGISTRADORA
    • ATM
    • CORRIDA
    • DESMANCHE.```

    **_Lavagem para pessoas da família_**:
    ```
    Lavagem antes de bater a META: 35%
    Lavagem após bater a META: 20%```'''

    mensagem_metamembro2 = '''
    **_Modalidades Permitidas:_**
    ```
    Drogas (50% p família 50% p quem vendeu depois de bater a meta).
    Ações (50% p família 50% p dividir por igual entre os participantes, Exceto B.C e Paleto)```
    '''

    mensagem_metamembro3 = '''https://media.discordapp.net/attachments/1124560895020908564/1127776631990255767/Semanal.gif?width=960&height=201'''
    mensagem_metamembro4 = '''**Meta referente ao dia 17/07 ao dia 23/07**
    
    **300.000** em Dinheiro Sujo
    **150** de cada Componentes por dia'''
    mensagem_metamembro5 = '''

    ```
    Exemplo: 
    Valor: 300.000
    Entregue para: Rosa```
    Imagem:'''

    mensagem_metamembro6 = '''https://media.discordapp.net/attachments/1129940071726985386/1129942126952714320/image.png'''
    mensagem_metamembro7 = '''**Obs**: Qualquer descumprimento da meta será acarretado em puniçõesda Famiília. Então caso haja algum motivo. Informar aqui no chat-privado de cada membro.'''
    mensagem_metamembro8 = '''https://media.discordapp.net/attachments/1130536072691077221/1130537073531699270/Semanal_1024_40_px.gif'''

    await ctx.send(mensagem_metamembro0)
    await ctx.send(mensagem_metamembro1)
    await ctx.send(mensagem_metamembro2)
    await ctx.send(mensagem_metamembro3)
    await ctx.send(mensagem_metamembro4)
    await ctx.send(mensagem_metamembro5)
    await ctx.send(mensagem_metamembro6)
    await ctx.send(mensagem_metamembro7)
    await ctx.send(mensagem_metamembro8)


@client.command()
async def metaassociado(ctx):
    mensagem_metazero = '''https://media.discordapp.net/attachments/1130536072691077221/1130537073531699270/Semanal_1024_40_px.gif'''
    mensagem_meta1 = '''**Métodos de Farmar** **_DINHEIRO SUJO_**:

    ```
    • AÇÕES (Lojinha, ammunation, bebidas, joalheria e fleeca)
    • VENDA DE DROGA
    • REGISTRADORA
    • ATM
    • CORRIDA
    • DESMANCHE.```

    **_Lavagem para pessoas da família_**:
    ```
    Lavagem antes de bater a META: 35%
    Lavagem após bater a META: 20%```'''

    mensagem_meta2 = '''
    **_Modalidades Permitidas:_**
    ```
    Drogas (50% p família 50% p quem vendeu depois de bater a meta).
    Ações (50% p família 50% p dividir por igual entre os participantes, Exceto B.C e Paleto)```
    '''

    mensagem_meta3 = '''https://media.discordapp.net/attachments/1124560895020908564/1127776631990255767/Semanal.gif?width=960&height=201'''
    mensagem_meta4 = '''**Meta referente ao dia 17/07 ao dia 23/07**
    
    **400.000** em Dinheiro Sujo'''
    mensagem_meta5 = '''

    ```
    Exemplo: 
    Valor: 400.000
    Entregue para: Rosa```
    Imagem:'''

    mensagem_meta6 = '''https://media.discordapp.net/attachments/1129940071726985386/1129942126952714320/image.png'''
    mensagem_meta7 = '''**Obs**: Qualquer descumprimento da meta será acarretado em puniçõesda Famiília. Então caso haja algum motivo. Informar aqui no chat-privado de cada membro.'''
    mensagem_meta8 = '''https://media.discordapp.net/attachments/1130536072691077221/1130537073531699270/Semanal_1024_40_px.gif'''

    await ctx.send(mensagem_metazero)
    await ctx.send(mensagem_meta1)
    await ctx.send(mensagem_meta2)
    await ctx.send(mensagem_meta3)
    await ctx.send(mensagem_meta4)
    await ctx.send(mensagem_meta5)
    await ctx.send(mensagem_meta6)
    await ctx.send(mensagem_meta7)
    await ctx.send(mensagem_meta8)

client.run(
    'MTEzMDUxMzMzNDk4MzIwODk3MA.GRBqvu.rJnvrZGpiV6SjxihN18CaGa-7wdsehaPhOtTpg')
