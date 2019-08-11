import pymysql
import os

db = pymysql.connect("localhost", "root", "******", "KG_db",charset="utf8",port=3306,cursorclass=pymysql.cursors.Cursor)
cursor = db.cursor()
cursor.execute("use KG_db;")
count=0
wfile=open("wrong.txt","w",encoding="utf8")
for file in os.listdir("C:\\Users\\99402\\PycharmProjects\\KG\\data"):
    print(file)
    id=1
    if file !="award.txt":
            rfile = (open("C:\\Users\\99402\\PycharmProjects\\KG\\data\\{}".format(file), "r", encoding="utf8"))
            table = rfile.readline().strip().split("\t")
            table.append('ID')
            table = tuple(table)
            for line in rfile:
                count+=1
                if count % 100==0:
                    print(str(count)+" done.")
                line = line.replace("\n","").split("\t")
                if len(line)==0:
                    continue
                while (len(line)+1)!=len(table):
                    line.append("")
                line.append(str(id))
                try:
                    sql = """INSERT INTO {} {} VALUES {}""".format(file[:-4], str(table).replace("'", ""), tuple(line))
                    cursor.execute(sql)
                    db.commit()
                    id += 1
                except:
                    wfile.write(file+"\t"+str(tuple(table)).replace("'", "")+"\t"+ str(tuple(line))+"\n")

                # print(line)

