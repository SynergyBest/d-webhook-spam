import requests
import time

while True:
  webhook = # discord webhook url
    }

  data = {
      "username": "botname", # bot username
      "avatar_url": "" # link to image of the webhook
      "content": "<@!userid>", # id of the user to spam
      "embeds": [
      {
        "title": "", # embed title
        "url": "", # link in the embed title
        "color": "", # color of embed
        "description": "", # webhook description
        "image": {
          "url": "" # image url
        }
      }]
    }
# All params: https://discord.com/developers/docs/resources/webhook#webhook-object-webhook-structure
  result = requests.post(webhook, json=data)
  if 200 <= result.status_code < 300:
      print(f"Webhook sent with status {result.status_code}")
  else:
      print(f"Webhook errored with status {result.status_code}, response:\n{result.json()}")
  time.sleep(1)
