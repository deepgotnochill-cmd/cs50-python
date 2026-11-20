students = {1001: {"Roll Number": "26HEL2121", "Name":"Deep Datta Chaudhury" , "Marks":92},
            1002: { "Roll Number" :"26HEL2122","Name": "Amit Sharma", "Marks": 85}}
adm_no = int(input("Enter Admission Number to search : "))
if adm_no in students:
    info = students[adm_no]
    print(f"\nRecord Found:")
    print(f"Name: {info['Name']}\nRoll No: {info['Roll Number']}\nMarks {info['Marks']}")
else:
    print("Record not found!")    