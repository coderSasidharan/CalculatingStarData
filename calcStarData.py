import csv

mass = []
radius = []
with open("dwarf_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in f:
        radius.append(i)
with open("bright_stars.csv", "r") as f2:
    csv_reader = csv.reader(f2)
    for i in f2:
        mass.append(i)

radius1 = radius[2]
mass1 = mass[3]
for i in radius1:
    final_radius = float(i)*6.957+8

for i in mass1:
    final_mass = float(i)* 1.989+30

gravity = []
g = 6.67*10**-11
gravity = g*final_mass/final_radius
for i in gravity:
    gravity.append(i)
print(gravity)