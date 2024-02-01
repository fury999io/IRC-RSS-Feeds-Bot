import feedparser
import socket
import time

var = "" #Do not change the value 

#Enter the values
server = ""
channel = ""
bot_nick = ""

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
irc.send(bytes(f"USER {bot_nick} 0 * :{bot_nick}\r\n", "UTF-8"))
irc.send(bytes(f"NICK {bot_nick}\r\n", "UTF-8"))
irc.send(bytes(f"JOIN {channel}\r\n", "UTF-8"))

def feed(irc):
    global var
    rss_url = "" #Paste your feed url
    feed = feedparser.parse(rss_url)

    if feed.entries:
        latest_article = feed.entries[0]
        title = latest_article.title
        url = latest_article.link
        
        if title != var:
            message = f"Latest Article: {title} - {url}"
            irc.send(bytes(f"PRIVMSG {channel} :{message}\r\n", "UTF-8"))
            var = title

while True:
    data = irc.recv(2048).decode("UTF-8")
    if "PING" in data:
        irc.send(bytes("PONG " + data.split()[1] + "\r\n", "UTF-8"))
    feed(irc)
    time.sleep(120) #Deafult is set to 120 seconds
