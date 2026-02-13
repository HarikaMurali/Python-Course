import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('stud.txt',delim_whitespace=True)
data['Marks'] = pd.to_numeric(data['Marks'], errors='coerce').astype(int)
print(data)

'''print(data["Marks"].sum())
print(data["Marks"].min())
print(data["Marks"].max())
print("retrieve with condition")
greater_than_90=data[data["Marks"]0]
print(f"students with marks greater than 90: {greater_than_90}")'''

print("----------graph-------")
plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()