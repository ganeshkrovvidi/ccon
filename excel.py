import xlrd
import json
import csv
import os


mypath = os.path.abspath(os.path.dirname(__file__))
temp = '{"links": [],"nodes": []}'
template = json.loads(temp)
tempset = set()
xlpath1 = os.path.join(mypath, "APPID_VS_USERCOUNTRY.xlbs")
wb = xlrd.open_workbook(xlpath1)
sheet = wb.sheet_by_name('APPID_VS_USERCOUNTRY')
sheet.cell_value(0, 0)


for i in range(0, sheet.nrows):
    if(sheet.row_values(i)[0] != ""):
        tempobj = {}
        tempobj["source"] = sheet.row_values(i)[2]
        tempobj["value"] = 1
        tempobj["target"] = sheet.row_values(i)[0]
        template["links"].append(tempobj)
        tempset.add(sheet.row_values(i)[0])
        tempset.add(sheet.row_values(i)[2])

xlpath2 = os.path.join(mypath, "APPID_VS_PUBLISHEDCOUNTRY.xlbs")
wb = xlrd.open_workbook(xlpath1)
sheet = wb.sheet_by_name('APPID_VS_PUBLISHEDCOUNTRY')
sheet.cell_value(0, 0)


for i in range(0, sheet.nrows):
    if(sheet.row_values(i)[0] != ""):
        tempobj = {}
        tempobj["source"] = sheet.row_values(i)[0]
        tempobj["value"] = 1
        tempobj["target"] = sheet.row_values(i)[3]
        template["links"].append(tempobj)
        tempset.add(sheet.row_values(i)[0])
        tempset.add(sheet.row_values(i)[3])

for i in tempset:
    tempnode = {}
    tempnode["name"] = i
    template["nodes"].append(tempnode)


mypath = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(mypath, "input.json")
s = json.dumps(template, indent=4, sort_keys=True)
with open(path, "w") as outfile:
    outfile.write(s)
