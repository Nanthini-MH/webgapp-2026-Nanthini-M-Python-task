import pandas as pd


# 1. CREATE DATAFRAME

students = {
    "Name": ["Santhosh", "Arun", "Kavin", "Meena", "Priya"],
    "Age": [22, 21, 23, 22, 24],
    "Department": ["CSE", "IT", "ECE", "CSE", "IT"],
    "Mark": [90, 25, 75, 88, 35]
}

df = pd.DataFrame(students)

print("========== DATAFRAME ==========")
print(df)



# 2. COLUMN SELECTION


print("\n========== COLUMN SELECTION ==========")

print("\nName Column")
print(df["Name"])

print("\nMark Column")
print(df["Mark"])

print("\nMultiple Columns")
print(df[["Name", "Mark"]])



# 3. ROW SELECTION


print("\n========== ROW SELECTION ==========")

print("\nFirst Row")
print(df.iloc[0])

print("\nFirst Three Rows")
print(df.iloc[:3])

print("\nRows 1 to 3")
print(df.iloc[1:4])


# 4. FILTERING


print("\n========== FILTERING ==========")

print("\nStudents Passed")
print(df[df["Mark"] >= 35])

print("\nStudents Failed")
print(df[df["Mark"] < 35])

print("\nCSE Students")
print(df[df["Department"] == "CSE"])

print("\nMark > 80")
print(df[df["Mark"] > 80])



# 5. AGGREGATE FUNCTIONS


print("\n========== AGGREGATE FUNCTIONS ==========")

print("Total Marks:", df["Mark"].sum())

print("Average Mark:", df["Mark"].mean())

print("Highest Mark:", df["Mark"].max())

print("Lowest Mark:", df["Mark"].min())

print("Student Count:", df["Name"].count())



# 6. SORTING


print("\n========== SORTING ==========")

print("\nSort by Mark Ascending")
print(df.sort_values("Mark"))

print("\nSort by Mark Descending")
print(df.sort_values("Mark", ascending=False))



# 7. ADD NEW COLUMN


print("\n========== ADD COLUMN ==========")

df["Bonus"] = 5

print(df)

df["Total"] = df["Mark"] + df["Bonus"]

print("\nAfter Total Column")
print(df)


# 8. UPDATE VALUES


print("\n========== UPDATE VALUES ==========")

df.loc[df["Name"] == "Arun", "Mark"] = 40

print(df)



# 9. MISSING VALUES


print("\n========== MISSING VALUES ==========")

df.loc[2, "Age"] = None

print(df)

print("\nMissing Value Count")
print(df.isnull().sum())

print("\nFill Missing Age with 0")
print(df.fillna(0))



# 10. GROUP BY


print("\n========== GROUP BY ==========")

print(
    df.groupby("Department")["Mark"].mean()
)

print(
    df.groupby("Department")["Mark"].max()
)