from webserver import keep_alive
import requests

channelID = a71201503498878
headers = {
    "authorization":
    "ODEzOTAwMDQ0NDU3NjA3MTc5.GxfTd6.JbMEh7_QuuQW4lfKbonvHlMXooW9DZ0iAzTF9Y"
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
