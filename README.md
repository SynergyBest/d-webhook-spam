# This is a webhook spam for [Discord](https://discord.com)
[![Run it on Repl.it](https://repl.it/badge/github/SynergyDev/d-webhook-spam)](https://repl.it/github/synergybest/d-webhook-spam) [![Discord](https://img.shields.io/discord/759108372447887450?color=7289DA&label=Discord&logo=discord)](https://discord.gg/dCcBFwQStT) [![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/synergybest/d-webhook-spam?include_prereleases&label=Version&logo=Python&logoColor=white)](https://github.com/synergybest/d-webhook-spam/releases)
## Json Parameters
```json
{
  "username": "botname",
  "avatar_url": "url to avatar",
  "discriminator": "bot tag",
  "content": "<@!userid>",
  "embeds": [embed]
}
```
Fill the content parameter with the user who you want to spam's ID and whatever unembedded text you want.
FIll the botname parameter with the name of the bot/webhook
Fill the avatar_url parameter with a link to an avatar eg. https://cdn.discordapp.com/avatars/543599597210304542/a_0615405a6d668013cee4399316f6916b.gif?size=256&f=.gif
```json
{
"title": "fill-in",
"description": "fill-in" 
}
```
Fill the title parameter with the text you want for the embed title 
Fill the description parameter with the text you want embedded
## Python options
### time.sleep
```py
time.sleep()
```
Add a number inbetween the parentheses for the amount of seconds you want it to wait until it runs again
### Webhook URL
```py
url = ""
```
Add the webhook url inbetween the double quotes
### while True
```py
While True:
```
To have it not run infinitely please remove ```while True:``` and ``time.sleep()`` then highlight it all and press shift + tab and save
