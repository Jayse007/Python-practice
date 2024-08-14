import request_tutorial

res = request_tutorial.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
playFile = open("RomeoAndJuliet.txt", 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()