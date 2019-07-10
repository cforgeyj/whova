import xlrd
from db_table import db_table

agenda = db_table("agenda", {"id": "integer PRIMARY KEY", "date": "text", "start_time": "text", "end_time": "text",
                             "session_title": "'text'", "location": "'text'"})

# XLS_FILE = os.getcwd() + "\\agenda.xls"
workbook = xlrd.open_workbook('agenda.xls')
ws = workbook.sheet_by_name('Agenda')
key = 0
count = 0
for row in range(ws.nrows):
    if count > 15:
        key += 1
        tempStr = ws.cell(row, 3).value
        tempStr.replace("'", "\'")
        tempStr2 = ws.cell(row, 4).value
        tempStr2.replace("'", "\'")
        tempStr3 = ws.cell(row, 5).value
        tempStr3.replace("'", "\'")

        agenda.insert({"date": ws.cell(row, 0).value, "start_time": ws.cell(row, 1).value,
                       "end_time": ws.cell(row, 2).value, "session_title": tempStr, "location": tempStr2})
    count += 1
