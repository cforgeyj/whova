import sqlite3
import sys
from import_agenda import agenda

#connect file to the interview test db

conn = sqlite3.connect("interview_test.db")
cursor = conn.cursor()

#parse command line args where first is column name and second is value
col=sys.argv[1] if len(sys.argv) > 1 else "somevalue"
val = sys.argv[2]
print("column: " + col)
print("value: " + val)
#call select and get all rows with val in column col
result = agenda.select([col], where = {col: val})
#print these rows
print(result)
