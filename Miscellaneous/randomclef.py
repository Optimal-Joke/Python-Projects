import random as rd

clef_dict = {1: {"name": "Aaron", "part": "Bass"},
             2: {"name": "Chad", "part": "Tenor"},
             3: {"name": "David", "part": "Tenor"},
             4: {"name": "", "part": ""},
             5: {"name": "Emma", "part": "Alto"},
             6: {"name": "Hunter", "part": "Tenor"},
             7: {"name": "Ian", "part": "Tenor"},
             8: {"name": "Jungsoo", "part": "Tenor"},
             9: {"name": "Julia", "part": "Mezzo"},
             10: {"name": "Katie", "part": "Alto"},
             11: {"name": "Mira", "part": "Alto"},
             12: {"name": "Nick", "part": "Baritone"},
             13: {"name": "Secunda", "part": "Soprano"},
             14: {"name": "Stan", "part": "Baritone"},
             15: {"name": "Tas", "part": "Mezzo"},
             16: {"name": "Izzy", "part": "Alto"},
             17: {"name": "Joya", "part": "Soprano"}}


part_dict = {}
for i in range(1, len(clef_dict)+1):
    if clef_dict[i]["part"] not in part_dict.keys():
        part_dict[clef_dict[i]["part"]] = []
    part_dict[clef_dict[i]["part"]].append(clef_dict[i]["name"])

try:
    rand_sop = rd.choice(part_dict["Soprano"])
except KeyError:
    rand_sop = None

try:
    rand_mezzo = rd.choice(part_dict["Mezzo"])
except KeyError:
    rand_mezzo = None

try:
    rand_alto = rd.choice(part_dict["Alto"])
except KeyError:
    rand_alto = None

try:
    rand_tenor = rd.choice(part_dict["Tenor"])
except KeyError:
    rand_tenor = None

try:
    rand_bari = rd.choice(part_dict["Baritone"])
except KeyError:
    rand_bari = None

try:
    rand_bass = rd.choice(part_dict["Bass"])
except KeyError:
    rand_bass = None

results = f"""
Soprano: {rand_sop}
Mezzo: {rand_mezzo}
Alto: {rand_alto}
Tenor: {rand_tenor}
Bari: {rand_bari}
Bass: {rand_bass}
"""

print(results)
