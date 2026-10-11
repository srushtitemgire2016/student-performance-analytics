
import pandas as pd
import numpy as np

print("=" * 50)
print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 50)

# Load student data from CSV
df = pd.read_csv("student.csv")

# Display the dataset
print("\nStudent Records:")
print(df.to_string(index=False))

# Display basic dataset information
print("\nDataset Information")
print("Total Students:", len(df))
print("Departments:", df["Department"].nunique())
print("Columns:", list(df.columns))


# Calculate total and average marks
subjects = ["Maths", "Science", "English"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = np.round(df[subjects].mean(axis=1), 2)

print("\nStudent Marks Analysis:")
print(df[["StudentID", "Name", "Total", "Average"]].to_string(index=False))


# Function to assign grades
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Apply the grading function
df["Grade"] = df["Average"].apply(calculate_grade)

print("\nStudent Grades:")
print(
    df[["StudentID", "Name", "Average", "Grade"]]
    .to_string(index=False)
)


# Determine pass or fail
df["Result"] = np.where(
    df["Average"] >= 40, "Pass", "Fail"
)

print("\nStudent Pass/Fail Results:")
print(
    df[["StudentID", "Name", "Average", "Grade", "Result"]]
    .to_string(index=False)
)

# Count students who passed and failed
passed = (df["Result"] == "Pass").sum()
failed = (df["Result"] == "Fail").sum()

print("\nPass/Fail Summary:")
print("Students Passed:", passed)
print("Students Failed:", failed)


# Overall class performance analysis
class_average = round(df["Average"].mean(), 2)

highest_index = df["Average"].idxmax()
lowest_index = df["Average"].idxmin()

highest_student = df.loc[highest_index]
lowest_student = df.loc[lowest_index]

print("\nClass Performance Summary:")
print("Class Average:", class_average)

print(
    "Highest Performer:",
    highest_student["Name"],
    "- Average:",
    highest_student["Average"]
)

print(
    "Lowest Performer:",
    lowest_student["Name"],
    "- Average:",
    lowest_student["Average"]
)


# Subject-wise performance analysis
subject_averages = df[subjects].mean().round(2)

print("\nSubject-wise Average Marks:")
print(subject_averages)

best_subject = subject_averages.idxmax()
lowest_subject = subject_averages.idxmin()

print("\nBest Performing Subject:", best_subject)
print("Lowest Performing Subject:", lowest_subject)


# Display the top 3 performing students
top_students = df.sort_values(
    by="Average", ascending=False
).head(3)

print("\nTop 3 Performing Students:")
print(
    top_students[
        ["StudentID", "Name", "Department", "Average", "Grade"]
    ].to_string(index=False)
)


# Display each student's performance using a loop
print("\nIndividual Student Performance:")

for index, row in df.iterrows():
    print(
        f"{row['Name']}: Average = {row['Average']}, "
        f"Grade = {row['Grade']}, Result = {row['Result']}"
    )


# Save the analyzed student data to a CSV file
df.to_csv("student_performance_report.csv", index=False)

print("\nStudent performance report saved successfully!")
print("File: student_performance_report.csv")



# Visualize student performance
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.bar(df["Name"], df["Average"])

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
