students = {
    101 : {"Name": "Aditi", "Scores": [78, 85, 90]},
    102 : {"Name": "Rahul", "Scores": [45, 60, 50]},
    103 : {"Name": "Sneha", "Scores": [90, 88, 95]},
    104 : {"Name": "Karan", "Scores": [55, 72, 68]},
    105 : {"Name": "Priya", "Scores": [49, 51, 47]},
}

# Calculate average score and flag pass/fail
for sid, details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 50 #Boolean Flag

#Print names of students who passed
print("Students who passsed: ")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])