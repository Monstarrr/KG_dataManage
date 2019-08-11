import pymysql
import os

db = pymysql.connect("localhost", "root", "924815Tv", "KG_db",charset="utf8",port=3306,cursorclass=pymysql.cursors.Cursor)
cursor = db.cursor()
cursor.execute("use KG_db;")
count=0
wfile=open("wrong2.txt","w",encoding="utf8")

rfile = (open("C:\\Users\\99402\\PycharmProjects\\KG\\data\\Organization.txt", "r", encoding="utf8"))
table = rfile.readline().strip().split("\t")
table.append("ID")
table = tuple(table)

for line in rfile:
    count+=1
    if count % 100==0:
        print(str(count)+" done.")
    line = line.replace("\n","").split("\t")

    line.append(line[0])
    if len(line)==0:
        continue
    while (len(line))!=len(table):
        line.append("")

    try:
        print(table,line)
        sql = """INSERT INTO {} {} VALUES {}""".format("organization", str(table).replace("'", ""), tuple(line))
        cursor.execute(sql)
        db.commit()
    except:
        wfile.write("award.txt"+"\t"+str(tuple(table)).replace("'", "")+"\t"+ str(tuple(line))+"\n")

        # print(line)

