import os
import json

import parkClass as park

with open("parkings.json", "r") as file:
    place = json.load(file)

park1 = park.Park(place)

for i, k in enumerate (park1.locations):
    hit = "http://172.21.27.142:5000/data/add?"
    qstring1 = "coords="
    qstring2 = "&type="
    qstring3 = "&num_spots="
    qstring4 = "&restriction="
    qstring5 = "&time_restriction="
    qstring6 = "&id="
    construct = [qstring1, qstring2, qstring3, qstring4, qstring5, qstring6]
    for i, value in enumerate (k.values()):
        if(i != 0):
            construct[i] += str(value).replace(" ", "%20")
        else:
            v = list(value)
            for x in v:
                for z in x.values():
                    construct[0] += str (z) + ","
    construct[0] = construct[0][:-1]
    for i in construct:
        hit += i
    print(hit)

        