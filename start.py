import feedparser
import socket
import time

#Do not change the values
var = ""  
count = 0

#Change the values 
server = ""
channel = ""
nick = ""
feed_url = ""

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
irc.send(bytes(f"USER {nick} 0 * :{nick}\r\n", "UTF-8"))
irc.send(bytes(f"NICK {nick}\r\n", "UTF-8"))
irc.send(bytes(f"JOIN {channel}\r\n", "UTF-8"))

def Feed(irc):
    global var
    global feed_url
    feed = feedparser.parse(feed_url)

    if feed.entries:
        latest_article = feed.entries[0]
        title = latest_article.title
        url = latest_article.link
        
        if title != var:
            message = f"Latest Article: {title} - {url}"
            irc.send(bytes(f"PRIVMSG {channel} :{message}\r\n", "UTF-8"))
            var = title

Feed(irc)
            
while True:
    data = irc.recv(2048).decode("UTF-8")
    if "PING" in data:
        irc.send(bytes("PONG " + data.split()[1] + "\r\n", "UTF-8"))
        count = count + 1 #On libera.chat it seems like PING are sent in intervals of 260 seconds
    if count > 2:
        Feed(irc)
        count = 0
