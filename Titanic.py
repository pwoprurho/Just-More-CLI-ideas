import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
df = pd.read_csv("tested.csv")
ndf = df.copy()
ndf.drop(["Name", "Ticket", "Fare","SibSp", "Parch", "Age"], axis=1, inplace=True)
"""
ndf["Sex"] = ndf["Sex"].map({"male":0, "female":1})
ndf["Survived"] = ndf["Survived"].map({0: 0, 1: 1})
survived_by_sex = ndf.groupby(["Sex", "Survived"], observed=True).size()
print(survived_by_sex)
plt.figure(figsize=(8, 5))
survived_by_sex.plot(kind="bar")
plt.xlabel("Sex")
plt.ylabel("Percentage")
plt.show()
"""
ndf["Embarked"] = ndf["Embarked"].map({"C":0, "S":1, "Q":2})
ndf["Survived"] = ndf["Survived"].map({0: 4, 1:5})
survived_by_embarked = ndf.groupby(["Embarked", "Survived"], observed=True).size()
plt.figure(figsize=(8, 6))
survived_by_embarked.plot(kind="bar")
plt.title("Relationship between Port and survived")
plt.xlabel("Grouped by survival to Embarked")
plt.ylabel("Number tha survived")
plt.show()
