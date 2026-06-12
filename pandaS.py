import pandas as pd
data=[100,200,345]
series=pd.Series(data,index=["a","b","c"])
print(series)

series.loc["a"]=200 #update the value

print(series.loc["a"]) #loc lock the property

marks={"OS":97,"NetWork":88,"ML":78}
mark=pd.Series(marks)

print(mark.loc["OS"])