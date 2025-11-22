file_path_student = "E:\PycharmProjects\COP3502C-LAB11\data\students.txt"

with open(file_path_student, 'r') as file:
    for line in file:
        student_id = line[0:3]
        name = line[3:].strip()
        print(student_id, name)