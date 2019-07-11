import xlrd
from db_table import db_table

#constructor for creating a table in a database with the given schema
agenda = db_table("agenda", {"id": "integer PRIMARY KEY", "date": "text", "start_time": "text", "end_time": "text",
                             "session_title": "'text'", "location": "'text'"})

#open up the the excel file that we need to import and make sure we are using the correct sheet in the excel file
workbook = xlrd.open_workbook('agenda.xls')
ws = workbook.sheet_by_name('Agenda')

#key will increment by 1 with each iteration of the for loop to make sure that each row in the table
#is given a unique id
key = 0

#count makes sure that we are only inserting columns 13-77
count = 0

#iterate through all rows in the agenda
for row in range(ws.nrows):

    if count > 15:
        key += 1

        #get temp strings that format correctly in case the input text from the excel file has an apostrophe
        tempStr = ws.cell(row, 3).value
        tempStr.replace("'", "\'")
        tempStr2 = ws.cell(row, 4).value
        tempStr2.replace("'", "\'")

        #insert the row into the db table
        agenda.insert({"date": ws.cell(row, 0).value, "start_time": ws.cell(row, 1).value,
                       "end_time": ws.cell(row, 2).value, "session_title": tempStr, "location": tempStr2})
    count += 1
