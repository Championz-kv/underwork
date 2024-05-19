import openpyxl 
  
try:
    wb = openpyxl.load_workbook("gojo.xlsx") 
except:
    wb = openpyxl.Workbook()
wb.active = 1
sheet = wb.active 
objects = sheet['A1':'B7']
x = []
for i in objects:
    for j in i:
        x.append(j.value)
print(x)

data = [x]
for i in data:
    sheet.append(i)
  
# save the file 
wb.save("gojo.xlsx") 