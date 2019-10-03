import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("titanic.csv")
print(data.head(10))

print(data.isnull())

sns.heatmap(data.isnull(),yticklabels=False , cbar=False  ,cmap = "viridis" )  #all the null values is shown as yellow color. most of the nan values is presented in age and cabin column
plt.title("Null values is shown as Yellow color")
plt.show()


sns.set_style('whitegrid')
sns.countplot(x='survived',data=data) #0 - not survived and {1 -  survived }
plt.title("survived or not")
plt.show()

#how many male people  are survived and how many female  people  are survived
sns.set_style("whitegrid")
sns.countplot(x = "survived" , hue = 'sex' , data = data)
plt.title("survived based on sex")
plt.show()


#based on passenger class
sns.set_style("whitegrid")
sns.countplot(x ="survived" , hue = "pclass"  , data = data)
plt.title("survived based on passenger class")
plt.show()

#age plot

plt.hist(data["age"].dropna() , bins = 40)
plt.title("Age")
plt.xlabel("Age")
plt.ylabel("People")
plt.show()


