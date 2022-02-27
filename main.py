# bot.py
import os
import discord
import random
import datetime
from replit import db
#from dotenv import load_dotenv
from datetime import timedelta
from datetime import time
from discord.ext import commands


client = discord.Client()
# 1

def update_database(Event, Day, Time, Remind):
    if "EventName" in db.keys():
      EventN = db["EventName"]
      EventN.append(Event)
      db["EventName"] = EventN
    else:
      db["EventName"] = [Event]
      
    if "EventDay" in db.keys():
      EventD = db["EventDay"]
      EventD.append(Day)
      db["EventDay"] = EventD
    else:
      db["EventDay"] = [Day]

    if "EventTime" in db.keys():
      EventT = db["EventTime"]
      EventT.append(Time)
      db["EventTime"] = EventT
    else:
      db["EventTime"] = [Day]

    if "EventRemind" in db.keys():
      EventR = db["EventRemind"]
      EventR.append(Remind)
      db["EventRemind"] = EventR
    else:
      db["EventRemind"] = [Remind]

    print("Name: ")
    print(db["EventName"])
    print("Day: ")
    print(db["EventDay"])
    print("Time: ")
    print(db["EventTime"])
    print("Reminder: ")
    print(db["EventRemind"])


def delete_Event(index):
  EventNames = db["EventName"]
  EventDays = db["EventDay"]
  EventTimes = db["EventTime"]
  EventReminders = db["EventRemind"]
  if len(EventNames) > index:
    del EventNames[index]
    del EventDays[index]
    del EventTimes[index]
    del EventRemind[index]
    db["EventName"] = EventNames
    db["EventDay"] = EventDays
    db["EventTime"] = EventTimes
    db["EventRemind"] = EventReminders
      

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  #user enters !remind 'Event Name'
  #then prompted to enter date of event
  #then prompted to enter time of event
  if msg.startswith('!remind'):

    Event = msg.split("!remind",1)[1]
    await message.channel.send("Enter date of event: (dd/mm/yyyy)")
    msg2 = await client.wait_for('message', timeout=60);

    
    msg2=msg2.content
    msg2 = str(msg2)
    day = int(msg2[0])*10+int(msg2[1]);
    month = int(msg2[3])*10+int(msg2[4]);
    year = int(msg2[6])*1000+int(msg2[7])*100+int(msg2[8])*10+int(msg2[9])
    EventDay = datetime.date(year,month,day)

    
    await message.channel.send("Please enter the time of the event: (hh:mm)")
    msg3 = await client.wait_for('message', timeout=60);
    msg3 = str(msg3.content)
    
    hour = int(msg3[0])*10+int(msg3[1])
    min = int(msg3[3])*10+int(msg3[1])
    EventTime = datetime.time(hour,min)
    
    await message.channel.send("How long before the event do you want get notified by me? (hh:mm)")
    msg4  = await client.wait_for('message', timeout=60);
    msg4 = str(msg4.content)
    hour = int(msg4[0]*10)+int(msg4[1])
    min = int(msg4[3]*10)+int(msg4[4])

    update_database(Event, msg2, msg3, msg4)
  
  
  # Register an event
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
  
client.run(os.getenv('TOKEN'));