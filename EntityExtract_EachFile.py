import csv
import os
import re
from bs4 import BeautifulSoup
need_tag1=["AwardTitle","AwardEffectiveDate","AwardExpirationDate",'AwardAmount',"MinAmdLetterDate","MaxAmdLetterDate","AwardID"]

need_tag2=["AwardInstrument_Value","ProgramOfficer_SignBlockName","Investigator_FirstName","Investigator_LastName",
          "Investigator_EmailAddress","Investigator_StartDate","Investigator_RoleCode","Institution_Name","Institution_CityName","Institution_ZipCode",
          "Institution_PhoneNumber","Institution_StreetAddress","Institution_CountryName","Institution_StateName","Institution_StateCode",
          "ProgramElement_Text"]

need_tag3=["LongName","Abbreviation"]
need_tag4=["Code"]

# db = pymysql.connect("localhost", "root", "924815Tv", "KG_db",charset="utf8",port=3306,cursorclass=pymysql.cursors.Cursor)
# cursor = db.cursor()
# cursor.execute("use KG_db;")

wrong=0
cnt=1
max=0

wrong+=1
wfile=open("data_EachFile.txt","w")

award={'Title': '','EffectiveDate': '','ExpirationDate': '','Amount': '','MinAmdLetterDate': '','MaxAmdLetterDate': '','ID': ''}
AwardInstrument={'Value': ''}
Organization={'Code': ''}
ProgramOfficer={'SignBlockName': ''}
Investigator={'FirstName': '','LastName': '','EmailAddress': '','StartDate': '','RoleCode': ''}
Institution={'Name': '','CityName': '','ZipCode': '','PhoneNumber': '','StreetAddress': '','CountryName': '','StateName': '','StateCode': ''}
ProgramElement={"Text":"",	"Code":""}
Directorate={"LongName":"",	"Abbreviation":""}
Division = {"LongName":"",	"Abbreviation":""}

award1=[]
AwardInstrument1=[]
Organization1=[]
ProgramOfficer1=[]
Investigator1=[]
Institution1=[]
ProgramElement1=[]
Directorate1=[]
Division1 = []

EachMessage=["award","AwardInstrument","Organization","ProgramOfficer","Investigator","Institution","ProgramOfficer","Investigator","Institution","ProgramElement","Directorate","Division"]

Text=""
keys=""
values=""

for fileset in os.listdir("/home/jytang/prp_f/"):
    print(fileset)
    for file in os.listdir("/home/jytang/prp_f/"+fileset):
        try:
            soup = BeautifulSoup(open("/home/jytang/prp_f/"+fileset+"/"+file, encoding='utf8'),"xml")
            for tag1 in need_tag1:
                result=soup.find_all(tag1)
                for i in result:
                    i = re.sub(" +", " ", i.get_text().strip())
                    award[tag1.replace("Award","")]=i
            for tag2 in need_tag2:
                tag=tag2.split("_")
                result=soup.find_all(tag[1])
                for i in result:
                    i = re.sub(" +", " ", i.get_text().strip())
                    exec("{}[tag[-1]]=i".format(tag[0]))
            for tag3 in need_tag3:
                result=soup.find_all(tag3)
                if len(result)==2:
                    result[0] = re.sub(" +", " ", result[0].get_text().strip())
                    Directorate[tag3]=result[0]
                    result[1] = re.sub(" +", " ", result[1].get_text().strip())
                    Division[tag3]=result[1]
            for tag4 in need_tag4:
                result=soup.find_all(tag4)
                if len(result)==2:
                    result[0] = re.sub(" +", " ", result[0].get_text().strip())
                    Organization[tag4]=result[0]
                    result[1] = re.sub(" +", " ", result[1].get_text().strip())
                    ProgramElement[tag4] = result[1]

            cnt+=1
            flag=0
            result=''
            for name in EachMessage:
                if (name=="award" ):
                    wfile.write(str(eval(name)["ID"])+"\n")
                elif  name=="Organization":
                    if len(eval(name)["Code"])==0:
                        wfile.write("0\n")
                    else:
                        wfile.write(str(eval(name)["Code"])+"\n")
                else:
                    value=eval(name)
                    result=("SELECT ID from "+name +" WHERE ")
                    for i in value:
                        result+=(str(i)+" = \""+str(value[i]).replace("\"","\'").lower()+ "\" AND ")        
                    wfile.write(result[:-4]+";\n")
            wfile.write("\n")
            if (cnt%100)==0:
                print(str(cnt)+" done.")

            award={'Title': '','EffectiveDate': '','ExpirationDate': '','Amount': '','MinAmdLetterDate': '','MaxAmdLetterDate': '','ID': ''}
            AwardInstrument={'Value': ''}
            Organization={'Code': ''}
            ProgramOfficer={'SignBlockName': ''}
            Investigator={'FirstName': '','LastName': '','EmailAddress': '','StartDate': '','RoleCode': ''}
            Institution={'Name': '','CityName': '','ZipCode': '','PhoneNumber': '','StreetAddress': '','CountryName': '','StateName': '','StateCode': ''}
            ProgramElement={"Text":"",	"Code":""}
            Directorate={"LongName":"",	"Abbreviation":""}
            Division = {"LongName":"",	"Abbreviation":""}
        except:
            print(fileset+"/"+file)

# for i in EachMessage:
#     wfile.write(str(eval("{}1".format(i)))+"\n")
# wfile.close()
# for i in EachMessage:
#     id=1
#     for message in eval(i+"1"):
#         id+=1
#         if i == "award":
#             keys=tuple(message.keys())
#             values=tuple(message.values())
#         else:
#             keys=list(message.keys())
#             keys.append("id")
#             keys=tuple(keys)
#             values=list(message.values())
#             values.append(id)
#             values=tuple(values)
#         wfile.write(i+"\t"+str(keys).replace("'", "")+"\t"+values+"\n")
        # sql = """INSERT INTO {} {} VALUES {}""".format(i, str(keys).replace("'", ""),
        #                                                    values)
        # cursor.execute(sql)
        # db.commit()
# print(wrong)
# db.close()