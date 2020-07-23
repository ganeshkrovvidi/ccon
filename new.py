
import xlrd
import json
import csv
import os


mypath = os.path.abspath(os.path.dirname(__file__))
temp = '{"links": [],"nodes": []}'
template = json.loads(temp)
tempset = set()
xlpath1 = os.path.join(mypath, "APPID_VS_USERCOUNTRY.xlsx")
wb = xlrd.open_workbook(xlpath1)
sheet = wb.sheet_by_name('APPID_VS_USERCOUNTRY')
sheet.cell_value(0, 0)


countries = {}
for i in range(0, sheet.nrows):
    countries[sheet.row_values(i)[2]] = json.loads(temp)

print(list(countries.keys()))

for i in range(0, sheet.nrows):
    if(sheet.row_values(i)[2] in list(countries.keys())):
        tempobj = {}
        tempobj["source"] = sheet.row_values(i)[2]
        tempobj["value"] = 1
        tempobj["target"] = sheet.row_values(i)[0]
        if tempobj not in countries[sheet.row_values(i)[2]]["links"]:
            countries[sheet.row_values(i)[2]]["links"].append(tempobj)
        tempset = {}
        tempset["name"] = (sheet.row_values(i)[0])
        if tempset not in countries[sheet.row_values(i)[2]]["nodes"]:
            countries[sheet.row_values(i)[2]]["nodes"].append(tempset)
        tempset = {}
        tempset["name"] = (sheet.row_values(i)[2])
        if tempset not in countries[sheet.row_values(i)[2]]["nodes"]:
            countries[sheet.row_values(i)[2]]["nodes"].append(tempset)

xlpath2 = os.path.join(mypath, "APPID_VS_PUBLISHEDCOUNTRY.xlsx")
wb = xlrd.open_workbook(xlpath1)
sheet = wb.sheet_by_name('APPID_VS_PUBLISHEDCOUNTRY.xlbs')
sheet.cell_value(0, 0)


for i in range(0, sheet.nrows):
    if(sheet.row_values(i)[3] in list(countries.keys())):
        tempobj = {}
        tempobj["source"] = sheet.row_values(i)[0]
        tempobj["value"] = 1
        tempobj["target"] = sheet.row_values(i)[3]
        if tempobj not in countries[sheet.row_values(i)[3]]["links"]:
            countries[sheet.row_values(i)[3]]["links"].append(tempobj)
        tempset = {}
        tempset["name"] = (sheet.row_values(i)[0])
        if tempset not in countries[sheet.row_values(i)[3]]["nodes"]:
            countries[sheet.row_values(i)[3]]["nodes"].append(tempset)
        tempset = {}
        tempset["name"] = (sheet.row_values(i)[3])
        if tempset not in countries[sheet.row_values(i)[3]]["nodes"]:
            countries[sheet.row_values(i)[3]]["nodes"].append(tempset)

for i in countries:
    mypath = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(mypath, i+"-input.json")
    s = json.dumps(countries[i], indent=4, sort_keys=True)
    with open(path, "w") as outfile:
        outfile.write(s)
