import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data/students.csv")

# Display the data
print("Student Data:")
print(df)

# Calculate average score for each student
df["Average"] = df[["Math", "Physics", "English", "Computer"]].mean(axis=1)

print("\nStudent Averages:")
print(df[["Name", "Average"]])

# Calculate average score for each subject
subject_averages = df[["Math", "Physics", "English", "Computer"]].mean()

print("\nSubject Averages:")
print(subject_averages)

# Find the highest-performing student
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Student:")
print(top_student["Name"], "-", round(top_student["Average"], 2))

# Create a bar chart
subject_averages.plot(kind="bar")

plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
