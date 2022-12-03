import re
x="Mortal.Engines.2018.1080p.BluRay.x265-RARBG"

out = re.sub('[^\w+]', ' ', x)
print(out)



