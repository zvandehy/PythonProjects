import urllib.request, urllib.parse, urllib.error
import re
url = "https://en.wikipedia.org/wiki/Emu_War"
# url = "https://en.wikipedia.org/"
# url = "https://en.wikipedia.org/wiki/The_Beatles"
webpage = urllib.request.urlopen(url)
anchors = re.findall("<a.*?</a>", webpage.read().decode())

ret = []
for anchor in anchors:
    startIndex = anchor.find("href=\"http")
    endIndex = anchor.find("\"",startIndex+7)
    tag = anchor[startIndex:endIndex+1]
    if tag != "":
        ret.append(anchor[startIndex:endIndex+1])
output = open("/Users/zeke/Programming/Python/output.txt", "w", encoding="utf-8")
output.write(str(len(ret)) + "\n")
for tag in ret:
    output.write(tag + "\n")