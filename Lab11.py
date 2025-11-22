file_path_student = r"data\students.txt"
file_path_assignment = r"data\assignments.txt"

student_data_dict = {}

with open(file_path_student, 'r') as file:
    for line in file:
        student_id = line[0:3]
        name = line[3:].strip()
        student_data_dict[name] = student_id

print(student_data_dict)

assign_id_to_total_points = {}
assign_name_to_assign_id = {}

with open(file_path_assignment, 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):

        assign_id_to_total_points[lines[i+1].strip()] = lines[i+2].strip()
        assign_name_to_assign_id[lines[i].strip()] = lines[i+1].strip()

print(assign_id_to_total_points)
print(assign_name_to_assign_id)