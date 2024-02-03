# IRC-RSS-Feeds-Bot
A bot that sends RSS feed notifications to your IRC channel

## Program Configuration
* Set values of the variables as per your case: <br>
```server```, ```channel```, ```nick``` <br><br>
* Set the value of ```feed_url``` to your feed url. <br><br>
* The interval of fetching feeds depends on the relational statement in the last loop of the program. <br>
By default the feeds are fetched after **3** PING messages are received from the IRC network. <br>
On libera.chat network, the interval between two consecutive PING are approximately 260 seconds. <br>

## Setting Up The Bot
Requirements: A computer that can boot (optional) <br>
Operating System: GNU/Linux <br><br>

(Debian)
```
sudo apt install python3 python3-pip -y 
```
```
pip install feedparser
```
```
wget https://raw.githubusercontent.com/fury999io/IRC-RSS-Feeds-Bot/main/start.py
```
```
nohup python3 start.py > /dev/null 2>&1 &
```
## Terminating The Bot
```
kill -9 $(ps aux | grep 'python3' | grep 'start.py' | awk '{print $2}')
```
