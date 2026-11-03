# Initializing database with student records
student_db = {
    "ADM001": {"Roll No": 10, "Name": "Amit", "Marks": 85},
    "ADM002": {"Roll No": 12, "Name": "Sneha", "Marks": 92},
    "ADM003": {"Roll No": 15, "Name": "Rahul", "Marks": 78}
}

search_adm = input("Enter Admission Number to search: ")

if search_adm in student_db:
    record = student_db[search_adm]
    print("\n--- Student Details Found ---")
    print(f"Admission No: {search_adm}")
    print(f"Roll Number : {record['Roll No']}")
    print(f"Name        : {record['Name']}")
    print(f"Marks       : {record['Marks']}")
else:
    print("Record not found matching that Admission Number.")
