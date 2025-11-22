file_path_student = r"data\students.txt"

student_data_dict = {}

with open(file_path_student, 'r') as file:
    for line in file:
        student_id = line[0:3]
        name = line[3:].strip()
        student_data_dict[name] = student_id

print(student_data_dict)