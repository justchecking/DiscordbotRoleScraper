# bot.py
import os

import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        # print all channels
        for member in guild.members:
        # load roles.txt and add roles to each member
            if member.id == client.user.id:
                continue
            else:
                with open('roles.txt', 'r') as f:
                    for line in f:
                        role = line.strip()
                        # split string by first ':'
                        role = role.split(':')
                        # get role id from list
                        memberid = role[0]
                        # for all roles in list
                        for r in role:
                            if(len(r) > 3):
                                if r  !=  memberid:
                                    if float(member.id) ==  float(memberid):
                                       # convert r to number
                                        r = int(r)
                                        
                                        roleid = guild.get_role(r) 
                                        # if roleid is equal to @everyone skip
                                        if roleid.name == "@everyone":
                                            continue
                                        try:
                                            await member.add_roles(roleid)
                                        except:
                                            print("Error adding role")
                                            continue

                    
                  
      

client.run('Token')


