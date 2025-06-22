import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("titanic.csv")

os.makedirs("assets", exist_ok=True)

# 1. Line Graph: Age vs Fare
plt.figure(figsize=(10,5))
plt.plot(df['age'], df['fare'], 'o', alpha=0.8)
plt.title('Line Graph: Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.grid(True)
plt.savefig("assets/age_vs_fare.png")
plt.close()

# 2. Histogram: Age Distribution
plt.figure(figsize=(8,5))
plt.hist(df['age'].dropna(), bins=5, color='orange', edgecolor='black')
plt.title('Histogram of Passenger Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig("assets/age_histogram.png")
plt.close()

# 3. Pie Chart: Gender Proportion
gender_counts = df['sex'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart of Gender Distribution')
plt.axis('equal')
plt.savefig("assets/gender_pie_chart.png")
plt.close()

# 4. Box and Whiskers Plot: Age by Passenger Class
plt.figure(figsize=(8,5))
sns.boxplot(x='pclass', y='age', data=df)
plt.title('Box & Whiskers: Age Distribution by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.savefig("assets/boxplot_age_pclass.png")
plt.close()