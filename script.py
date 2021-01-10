import requests as r

tokens = open("tokens.txt", 'r').read()
url = "https://discordapp.com/api/v6/users/@me/library"

tokens = tokens.split('\n')

for token in tokens:
    header = {
        "Content-Type": "application/json",
        "authorization": token
    }

    code = r.get(url, headers=header).status_code

    if (code == 200):
        print(f"{token} - Valid")

    else:
        print(f"{token} - Invalid")