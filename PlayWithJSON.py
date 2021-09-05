import json
print("Play With JSON".center(75, "="))

x = {
    "nama": "Enny Zakiyyah Arisa",
    "nim": "M3119035",
    "prodi": "D3 Teknik Informatika"
}

y = json.dumps(x)

print(y)
