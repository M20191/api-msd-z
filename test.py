import requests


# Libreria
print("Active development for Minecraft 1.18.2")
spigot_select = int(input("[1]1.18.2\n[2]1.18.1\n[3]1.17.1\n..."))

resp = requests.get(f'http://localhost:80/spigot/{spigot_select}')
print(resp.json()["link"])
