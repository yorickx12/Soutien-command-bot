import discord
from discord.ext import commands
from discord.ext.commands import check
from discord.utils import get
from asyncio import sleep




entrée = "ticket.json"
sorti = "ticket.json"

intents = discord.Intents().all()
client = commands.Bot(command_prefix="+", intents=intents)
client.remove_command("help")



serverid = 959079750473768990




@client.command()
async def configrole(ctx, roles):
    global role
    role = discord.utils.find(lambda r: r.name == roles, ctx.message.guild.roles)
    await ctx.send(role)


@client.command()
async def configactivity(ctx, act):
    global required_activity
    required_activity = act
    await ctx.send(f"__**{required_activity}**__ a étais choisis comme message de soutient")







@client.event
async def on_ready():
    print("OKKKKKKKKKKK")















@client.event
async def on_member_update(before, after):
    guild = client.get_guild(959079750473768990)
    role = guild.get_role(966003065243185153)

    if after.bot == True:
        return

    if before.activities == after.activities:
        return


    userHasActivity = False
    for activity in after.activities:
        if isinstance(activity, discord.CustomActivity):
            if required_activity in str(activity):
                userHasActivity = True

    if userHasActivity == True:
        await after.add_roles(role)
    else:
        await after.remove_roles(role)






client.run("")
