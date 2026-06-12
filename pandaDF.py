import pandas as pd
data={"Name":["Zayn","Nanthini","Flynn"],
       "Age":[21,19,20]}
df=pd.DataFrame(data)
print(df)
df1=pd.DataFrame(data,index=["stu1","stu2","stu3"])
print(df1)
#add column

df1["job"]=["Account","Cloud Architect","cashier"]
print(df1)

#add row

new_row=pd.DataFrame([{"Name":"Zara","Age":34,"job":"Developer"}],index=["stu4"])

df1=pd.concat([df1,new_row])

print(df1)