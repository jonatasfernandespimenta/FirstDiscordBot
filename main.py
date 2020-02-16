import discord
import random
from discord.voice_client import VoiceClient

startup_extensions = ["Music"]

client = discord.Client()
prefix = '.'

@client.event
async def on_ready():
    print("To pronto mlk")

@client.event
async def on_message(msg):
    if msg.author.bot is False:
        arg =  msg.content.lower().split()

        if arg[0] == prefix + 'blyat':
        	await client.send_message(msg.channel, 'https://i.ytimg.com/vi/xvXXgkknO7c/maxresdefault.jpg')

        elif arg[0] == prefix + 'cc':
            main = await client.send_message(msg.channel, 'Caro ou coroa?' '\n A = Caro, B = Coroa')
            await client.add_reaction(main, '🇦')
            await client.add_reaction(main, '🇧')

            cc = random.choice(['caro', 'coroa'])

            def check(reaction, user):
                react = str(reaction.emoji)
                return react.startswith(('🇦', '🇧'))
            wfr = await client.wait_for_reaction(message = main, user = msg.author, check = check)
            if wfr.reaction.emoji == '🇦':
                if cc == 'caro':
                    await client.send_message(msg.channel, 'Resultado: Cara, vitoria')
                elif cc == 'coroa':
                    await client.send_message(msg.channel, 'Resultado: Coroa, derrota')
            elif wfr.reaction.emoji == '🇧':
                if cc == 'caro':
                    await client.send_message(msg.channel, 'Resultado: Cara, derrota')
                elif cc == 'coroa':
                    await client.send_message(msg.channel, 'Resultado: Coroa, vitoria')

        elif arg[0] == prefix + 'ppt':
            main = await client.send_message(msg.channel, 'Vamos brincar de **Pedra, Papel ou Tesoura**?')

            await client.add_reaction(main, '✂')
            await client.add_reaction(main, '📰')
            await client.add_reaction(main, '🗿')

            ppt = random.choice(['pedra', 'papel', 'tesoura'])

            def check(reaction, user):
                react = str(reaction.emoji)
                return react.startswith(('✂', '📰', '🗿'))

            wfr = await client.wait_for_reaction(message=main, user=msg.author, check=check)
            if wfr.reaction.emoji == '✂':
                if ppt == 'tesoura':
                    await client.send_message(msg.channel, 'Empate!')
                elif ppt == 'papel':
                    await client.send_message(msg.channel, 'Perdi!')
                elif ppt == 'pedra':
                    await client.send_message(msg.channel, 'Você perdeu noobzinho!')
            elif wfr.reaction.emoji == '📰':
                if ppt == 'tesoura':
                    await client.send_message(msg.channel, 'Você perdeu noobzinho!')
                elif ppt == 'papel':
                    await client.send_message(msg.channel, 'Empate!')
                elif ppt == 'pedra':
                    await client.send_message(msg.channel, 'Perdi!')
            elif wfr.reaction.emoji == '🗿':
                if ppt == 'tesoura':
                    await client.send_message(msg.channel, 'Perdi!')
                elif ppt == 'papel':
                    await client.send_message(msg.channel, 'Você perdeu noobzinho!')
                elif ppt == 'pedra':
                    await client.send_message(msg.channel, 'Empate!')
        elif arg[0] == prefix + 'oi':
            await client.send_message(msg.channel, 'Oi, {}!'.format(msg.author.mention))
        elif arg[0] == prefix + 'asay':
            args = msg.content.lstrip(prefix + 'asay')
            await client.send_message(msg.channel, args)
            await client.delete_message(msg)

        elif arg[0] == prefix + 'rpg':
            main = await client.send_message(msg.channel, 'Olá, esse é apenas um RPG de texto criado por um noob em python, divirta-se (ou tenta sla)')
            main = await client.send_message(msg.channel, 'Você acorda caido no meio de uma floresta e avista 4 rotas...Qual seguir')
            main = await client.send_message(msg.channel, 'A = reto, B = Esquerda, C = Direita, D = Para trás')

            await client.add_reaction(main, '🇦')
            await client.add_reaction(main, '🇧')
            await client.add_reaction(main, '🇨')
            await client.add_reaction(main, '🇩')

            def check(reaction, user):
                react = str(reaction.emoji)
                return react.startswith(('🇦', '🇧', '🇨', '🇩'))

            wfr = await client.wait_for_reaction(message=main, user=msg.author, check=check)
            if wfr.reaction.emoji == '🇦':
            	main = await client.send_message(msg.channel, 'Você segue reto e se depara com um alce impedindo Você de continuar. O que fazer??')
            	main = await client.send_message(msg.channel, 'A = Atacar o alce, B = Voltar, C = Conversar com o Alce')

            	await client.add_reaction(main, '🇦')
            	await client.add_reaction(main, '🇧')
            	await client.add_reaction(main, '🇨')

            if wfr.reaction.emoji == '🇦':
            	main = await client.add_reaction(msg.channel, 'Alce -Olá viajante, estou te dando esta poçao magica, pegue e seja feliz')
            	main = await client.send_message(msg.channel, 'A = Aumento de QI, B = Invisibilidade, C = Aumento de força')

            	await client.add_reaction(main, '🇦')
            	await client.add_reaction(main, '🇧')
            	await client.add_reaction(main, '🇨')

            elif wfr.reaction.emoji == '🇧':
            	main = await client.send_message(msg.channel, 'Você encontra um tronco, um pequeno frasco jogado emcima e um machado fincado. O que fazer??')
            	main = await client.send_message(msg.channel, 'A = Pegar o machado e o frasco, B = Seguir em frente')

            	await client.add_reaction(main, '🇦')
            	await client.add_reaction(main, '🇧')

            elif wfr.reaction.emoji == '🇨':
            	main = await client.send_message(msg.channel, 'Você encontra um velho homem com grandes barbas e um manto com uma touca cobrindo sua face. O que fazer??')
            	main = await client.send_message(msg.channel, 'A = Dizer oi, B = Perguntar quem é, C = Ataca-lo, D = passar reto de fininho')

            	await client.add_reaction(main, '🇦')
            	await client.add_reaction(main, '🇧')
            	await client.add_reaction(main, '🇨')
            	await client.add_reaction(main, '🇩')

            elif wfr.reaction.emoji == '🇩':
            	main = await client.send_message(msg.channel, 'Você encontra um coelho...falante??? O que fazer??')
            	main = await client.send_message(msg.channel, 'A = Dizer oi ao coelho, B = SEQUESTRA-LO, C = ataca-lo')

            	await client.add_reaction(main, '🇦')
            	await client.add_reaction(main, '🇧')
            	await client.add_reaction(main, '🇨')

@client.event
async def on_member_remove(member):
    await client.send_message(discord.utils.get(member.server.channels, id="473931745721319465"), "{} saiu do server, bye bye".format(member.name))

@client.event
async def on_member_join(member):
    await client.send_message(discord.utils.get(member.server.channels, id="473931745721319465"), "{} entrou no server, bem vindo".format(member.name))


client.run() # Discord token here
