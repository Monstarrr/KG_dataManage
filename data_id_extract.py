import pymysql
import os

db = pymysql.connect("localhost", "root", "924815Tv", "KG_db",charset="utf8",port=3306,cursorclass=pymysql.cursors.Cursor)
cursor = db.cursor()
cursor.execute("use KG_db;")
# sql="SELECT ID FROM Institution WHERE Name = 'Rensselaer Polytechnic Institute'"
# cursor.execute(sql)
# rs=cursor.fetchall()
# for r in rs:
#     print(r)
rfile=open("data/data_EachFile.txt","r")
wfile=open("data/data_ID.txt","a")
wfile2=open("wrong.txt","a")
EachMessage=["award","AwardInstrument","Organization","ProgramOfficer","Investigator","Institution","ProgramOfficer","Investigator","Institution","ProgramElement","Directorate","Division"]
result=[]
cnt=0
for line in rfile.readlines():
    try:
        if line!='\n':
            if line[:6]!="SELECT":
                result.append(line.strip())
            else:
                cursor.execute(line)
                rs=cursor.fetchall()
                # print(rs)
                if (len(rs)!=1):
                    wfile2.write(line)
                    wfile2.write(str(rs))
                    wfile2.write("\n\n")
                    print(line.strip())
                    print(str(rs))
                    continue
                else:
                    for r in rs:
                        result.append(r[0])
        else:
            cnt+=1
            if cnt%100==0:
                print(cnt)
            wfile.write(str(result)+"\n")
            print(result)
            result=[]
    except:
        wfile2.write("wrong\t"+str(line))
wfile2.close()
wfile.close()
