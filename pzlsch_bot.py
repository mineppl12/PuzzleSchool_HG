#!/usr/bin/python

import asyncio
import discord
import time
import re
from discord.ext import commands
import random
from discord.utils import get

client = commands.Bot(command_prefix = '!')
client.remove_command("help")

subjects = {"수학","영어"}

gld = discord.Guild

token = "NzUxODI5NjY1NjU1Njg1MjEz.X1Ox8A.ZJS7LyM1C8QCTerzgzkNh8MGH6o"
@client.event
async def on_ready():
	print("-------------------")
	print(client.user.name)
	print("-------------------")

@client.event
async def on_member_join(member):
	if member.bot == False:
		await member.add_roles(client.get_guild(751819869795909793).get_role(751841232304603136), reason="디스코드봇 자동부여")
		await client.get_guild(751819869795909793).get_channel(751846474811441192).send("{}님이 서버에 오셨습니다".format(member.name))

@client.command()
async def 수강신청(ctx,cmd):
	m = ctx.author
	fl = 0
	if m != ctx.bot:
		for i in subjects:
			if cmd == i:
				fl = 1
		if fl == 0:
			await ctx.send("{}님, {}라는 과목은 현재 존재하지 않습니다".format(m.mention,cmd))
		elif fl == 1:
			await reqsubj(ctx,cmd)

@client.command()
async def 수강취소(ctx,cmd):
        m = ctx.author
        fl = 0
        i = 0
        if m != ctx.bot:
                for i in subjects:
                        if cmd == i:
                                fl = 1
                                break
                if fl == 0:
                        await ctx.send("{}님, {}이라는 과목은 현재 존재하지 않습니다".format(m.mention,cmd))
                elif fl == 1:
                        await ctx.send("{}님, 성공적으로 {} 수강 취소가 되었습니다".format(m.mention,cmd))

async def reqsubj(ctx,subj):
	m = ctx.author
	if m in get(ctx.guild.roles, name=subj).members:
		await ctx.send("{}님은 이미 {} 수강 신청을 하셨습니다".format(m.mention,subj))
	else:
		await m.add_roles(get(ctx.guild.roles, name=subj),reason = "수강신청")
		await ctx.send("{}님,성공적으로 {} 수강 신청이 되었습니다".format(m.mention,subj))

client.run(token)
