import sqlite3
db=sqlite3.connect("college.db")
cr=db.cursor()
# cr.execute("create table collegedata(stdname text,stdnumber text,stdfather text)")
# db.commit()
# db.close()
# print("data base created")
# name=input("enter name:")
number=input("enter number")
father=input("enter father name:")
# cr.execute(f"insert into collegedata(stdname,stdnumber,stdfather) values('{name}','{number}','{father}')")
# db.commit()
# db.close()
r=cr.execute(f"select * from collegedata where stdnumber='{number}' and stdfather='{father}'")
# r=cr.execute("select * from collegedata")

db.commit()
num=(len(r.fetchall()))
print(num)
# for data in r:
#     print(data)
if(num==1):
    print("data found")
else:
    print("not found")
db.close()