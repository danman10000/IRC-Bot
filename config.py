import os
import os.path
import time
import logging

# some commands can be executed only if the user's nick is found in this list
owner = list(set([
    'foobarfoo',
    'dan',
    'anson',
    'bh',
]))

owner_email = {
    'foobarfoo': 'foobar@gmail.com',
}

# server to connect to
server = '192.168.168.201'
#server = '10.4.0.174'
#server = raw_input("What is the IP of the IRC server? ")
# server's port
port = 6667

# bot's nicknames
#nicks = list(set(['PPyBot']))
nicks = raw_input("Enter your bot's nicknames(letters only and no spaces): ")
nicks = list(set([nicks]))
# bot's real name
#real_name = 'Paul Python Bot'
real_name = raw_input("What is your real name or user id (spaces and numbers allowed): ")

# channels to join on startup
channels = list(set([
    '#ppybbot',
    '#test-chan',
]))

cmds = {
    # core commands list, these commands will be run in the same thread as the bot
    # and will have acces to the socket that the bot uses
    'core': list(set([
        'quit',
        'join',
        'channels',
    ])),

    # normal commands list, the ones that are accessible to any user
    'user': list(set([
        'task',
        'wiki',
        'answer',
        'about',
        'help',
        'weather',
        'google',
        'mball',
        'uptime',
        'so',
        'twitter',
        'dos',
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action
    'auto': list(set([
        'email_alert',
    ])),
}

# smtp server for email_alert
smtp_server = 'smtp.gmail.com'
smtp_port = 25
from_email_address = 'changeme@gmail.com'
from_email_password = 'p@s$w0rd'

# users should NOT modify below!
log = os.path.join(os.getcwd(), '..', 'logs', '')
logging_level = logging.DEBUG
start_time = time.time()
current_nick = ''
