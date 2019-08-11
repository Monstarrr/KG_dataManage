import pandas as pd
EachMessage=["award","AwardInstrument","Organization","ProgramOfficer","Investigator","Institution","ProgramOfficer","Investigator","Institution","ProgramElement","Directorate","Division"]
rfile=open("data.txt","r")
award1=[]
AwardInstrument1=[]
Organization1=[]
ProgramOfficer1=[]
Investigator1=[]
Institution1=[]
ProgramElement1=[]
Directorate1=[]
Division1 = []

# exec("{}1=pd.DataFrame(eval(rflie.readline))")
for i in EachMessage:
    exec("{}1=pd.DataFrame(eval(rfile.readline().lower()))".format(i))
    exec("{}1.drop_duplicates(subset=None,keep='first',inplace=True)".format(i))
    exec("{}1.to_csv(\"/home/jytang/KG/graph/data/{}.txt\",sep=\"\t\",index=False)".format(i,i))
    print("{}done".format(i))
    # for di in eval(rfile.readline()):
    #     exec("({}1).append(str(di))".format(i))
    #     # print(di)
    # exec("({}1).sort()".format(i))
    # print(eval("{}1".format(i)))
    # print("done.")
    
    # exec("({}1)=rfile.readline()".format(i))
    # for e in eval("{}1".format(i)):
    #     e=str(e)

    