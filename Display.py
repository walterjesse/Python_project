import sqlite3
conn=sqlite3.connect("MITMidmorning.db")
print("OPen dtb succesfully")
data=conn.execute("select * from Wanafunzi")
for row in data:
    print("ID",row[0])
    print("NAME",row[1])
    print("AGE",row[2])
    print("SCHOOL",row[3])
    print("GENDER",row[4])
conn.close()