#! /usr/bin/env python
# -*- coding: utf-8 -*-
from discord_webhook import DiscordWebhook
import requests
import json
r = requests.get('https://api.battlemetrics.com/servers/10871556')
reponse_data = json.loads(r.content)
# print(reponse_data["data"]["attributes"])
content = ""
name = reponse_data["data"]["attributes"]["name"]
status = reponse_data["data"]["attributes"]["status"]
online = reponse_data["data"]["attributes"]["players"]
ip = reponse_data["data"]["attributes"]["ip"]
port = reponse_data["data"]["attributes"]["port"]
mplayers = reponse_data["data"]["attributes"]["maxPlayers"]

content += '--------------------------------------------------' + '\r\n'
content += '🏳️  Инфо: ' + str(name) + '\r\n'
content += '🚹 Игроков онлайн: ' + str(online) + '/' + str(mplayers) + '\r\n'
content += '🟢 татус:  ' + str(status) + '\r\n'
content += '💾 IP сервера:  ' + str(ip) + ':' + str(port) + '\r\n'
content += '--------------------------------------------------'
print(content)
allowed_mentions = {
    "users": ["123", "124"]
}

webhook = DiscordWebhook(url='YOUR-WEBHOOK-URL', content=content, allowed_mentions=allowed_mentions)
response = webhook.execute()
