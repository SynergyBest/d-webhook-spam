while True:
  import requests
  import time

  url = # discord webhook url

  embed = {
    "description": "get spammed", 
    "title": "LMAOOO"
    }

  data = {
      "username": "botname",
      "discriminator": "bot tag",
      "content": "<@!userid>",
      "embeds": [embed]
  }
# All params: https://discord.com/developers/docs/resources/webhook#webhook-object-webhook-structure
  result = requests.post(url, json=data)
  if 200 <= result.status_code < 300:
      print(f"Webhook sent {result.status_code}")
  else:
      print(f"Not sent with {result.status_code}, response:\n{result.json()}")
  time.sleep(1)
