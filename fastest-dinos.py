# You will be supplied with two data files in CSV format. The first file
# contains statistics about various dinosaurs. The second file contains
# additional data.
#
# Given the formula:
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#     where g = 9.8 m/s^2 (gravitational constant)
#
# write a program to read in the data files from disk, it must then print the
# names of only the bipedal (i.e. two-legged) dinosaurs from fastest to slowest. Do not print any
# other information.
#
# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore
#
#
# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal

import csv
import math

ds1 = None
ds2 = None
dinos = {}
g = 9.8  # m/s^2 (gravitational constant)

with open('dataset1.csv') as dataset1:
    ds1 = list(csv.DictReader(dataset1))

with open('dataset2.csv') as dataset2:
    ds2 = list(csv.DictReader(dataset2))

for dino in ds1:
    dinos[dino['NAME']] = {
        'leg-length': float(dino['LEG_LENGTH']), 'diet': dino['DIET'], 'speed': 0}

for dino in ds2:
    name = dino['NAME']
    if name not in dinos.keys():
        dinos[name] = {}
    dinos[name]['stride-length'] = float(dino['STRIDE_LENGTH'])
    dinos[name]['stance'] = dino['STANCE']
    if 'leg-length' not in dinos[name].keys():
        dinos[name]['speed'] = 0
    else:
        dinos[name]['speed'] = ((dinos[name]['stride-length'] / dinos[name]
                                 ['leg-length']) - 1) * math.sqrt(dinos[name]['leg-length'] * g)

for dino, chars in sorted(dinos.items(), key=lambda kv: (kv[1]['speed'], kv[0]), reverse=True):
    if 'stance' in chars.keys() and chars['stance'] == 'bipedal' and chars['speed'] != 0:
        print(dino + ' has speed ' + str(chars['speed']))
