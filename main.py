import os
import random

from irc_class import IRCbot

# Constants for the server, channel and botnick
# SERVER = "irc.libera"
# PORT = 6667
# CHANNEL = "#Inter.Net"
# BOTNICK = "bot"

## IRC Config
server = str(os.getenv("SERVER"))  # server to connect to
port = 6697
channel = str(os.getenv("CHANNEL"))  # channel to join
botnick = str(os.getenv("BOTNICK"))  # bot's nickname
botusrn = str(os.getenv("BOTNICK"))
bothost = str(os.getenv("BOTNICK"))
botnickpass = "guido"
botpass = "<%= @guido_password %>"

irc = IRCbot(server=server,
             channel=channel,
             botnick=botnick,
             botusrn=botusrn,
             bothost=bothost)

irc.send("JOIN #Inter.Net")

# irc.connect(server, port, channel, botnick, botpass, botnickpass)

# while True:
#   text = irc.get_response()
#   print(text)

#   if "PRIVMSG" in text and channel in text and "hello" in text:
#     irc.send(channel, "Hello!")
