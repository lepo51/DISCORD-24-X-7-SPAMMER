from webserver import keep_alive
import requests

channelID = 7188954516
headers = {
    "authorization":
    "A1458415axs45xswTYszws15"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
