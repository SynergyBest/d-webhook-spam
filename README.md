# This is a webhook spam for [Discord](https://discord.com)
[![Run it on Repl.it](https://repl.it/badge/github/SynergyDev/d-webhook-spam)](https://repl.it/github/synergybest/d-webhook-spam) [![Discord](https://img.shields.io/discord/759108372447887450?color=7289DA&label=Discord&logo=discord)](https://discord.gg/dCcBFwQStT) [![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/synergybest/d-webhook-spam?include_prereleases&label=Version&logo=Python&logoColor=white)](https://github.com/synergybest/d-webhook-spam/releases/latest) ![GitHub top language](https://img.shields.io/github/languages/top/synergybest/d-webhook-spam?logo=python&logoColor=white)
# [![DeepSource](https://deepsource.io/gh/SynergyBest/d-webhook-spam.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/SynergyBest/d-webhook-spam/?ref=repository-badge) [![DeepSource](https://deepsource.io/gh/SynergyBest/d-webhook-spam.svg/?label=resolved+issues&show_trend=true)](https://deepsource.io/gh/SynergyBest/d-webhook-spam/?ref=repository-badge)
## Json Parameters
```py
data = {
    "username": "botname",  # bot username
    "avatar_url": "",  # link to image of the webhook
    "content": "<@!userid>",  # id of the user to spam
    "embeds": [
        {
            "title": "",  # embed title
            "url": "",  # link in the embed title
            "color": "",  # color of embed
            "description": "",  # webhook description
            "image": {"url": ""},  # image url
        }
    ],
}
```
Self explanatory.
## Python options
### time.sleep
```py
time.sleep()
```
Add a number inbetween the parentheses for the amount of seconds you want it to wait until it runs again
### Webhook URL
```py
webhook = ""
```
Add the webhook url inbetween the double quotes
### while True
```py
While True:
```
To have it not run infinitely please remove ```while True:``` and ``time.sleep()`` then highlight it all and press shift + tab and save
<!-- Lmao idk -->
