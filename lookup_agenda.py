import sys
from import_agenda import agenda

#parse command line args where first is column name and second is value
col=sys.argv[1] if len(sys.argv) > 1 else "somevalue"
val = sys.argv[2]
#initialize array of different columns that can be queried
columns = ["id", "date", "start_time", "end_time", "session_title", "location"]

#call select to get all rows where the text in column col is val.
#store these rows in result
result = agenda.select(columns, where = {col: val})

#print result
print(result)



