#!/bin/env python

import xlrd

##### ADVERTISING DATA ######

wb = xlrd.open_workbook("./data/HealthConnectorAprilReport.xlsx")
sheets = wb.sheet_names()

cm = sheets[0]
dm = sheets[1]
pm = sheets[2]
CE = wb.sheet_by_name(cm)
DM = wb.sheet_by_name(dm)
PM = wb.sheet_by_name(pm)

total_reached = dict()
for i in range(21,265):
    if CE.cell(i, 1).value == "":
        continue
    total_reached[CE.cell(i, 1).value] = CE.cell(i,13).value

impressions = dict()

Barnstable_County = 213444
Middlesex_County = 1603000
Norfolk_County = 700322
Plymouth_County = 515142
Suffolk_County = 767719
Essex_County = 769362
Worcester_County = 813589
Nantucket_County = 10694
Dukes_County = 17325
Franklin_County = 70916
Hampshire_County = 161834
Hampton_County = 469818

impressions["Telemundo Boston"] = 8110000
impressions["Univision Boston"] = 5607000
impressions["Univision WUTF UniMass"] = 306000

print("The following are cities reached by window and physical advertisements")
print(total_reached, "\n")

print("The following are broadcast impressions by counties")
print(impressions, "\n")

printMedia = dict()

def addToCirculation(start_cell, end_cell):
    for i in range(start_cell, end_cell):
        city = PM.cell(i, 2).value.split()[0].replace(":", "")
        if city == "":
            continue
        if city in printMedia:
            printMedia[city] += PM.cell(start_cell, 6).value
        else:
            printMedia[city] = PM.cell(start_cell, 6).value

addToCirculation(2, 25)
addToCirculation(25, 46)
addToCirculation(46, 52)
addToCirculation(52, 53)
addToCirculation(63, 66)
addToCirculation(66, 69)
addToCirculation(69, 74)
addToCirculation(74, 92)
addToCirculation(92, 93)
addToCirculation(94, 97)
addToCirculation(97, 105)
addToCirculation(105, 110)
addToCirculation(110, 115)
addToCirculation(115, 136)
addToCirculation(136, 151)
addToCirculation(151, 187)
addToCirculation(187, 223)
addToCirculation(259, 275)


print("The following are cities by print media in circulation")
print(printMedia, "\n")
