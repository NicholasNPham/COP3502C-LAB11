import os

file_path_student = r"data\students.txt"
file_path_assignment = r"data\assignments.txt"

def main():
    student_data_dict = {}

    with open(file_path_student, 'r') as file:
        for line in file:
            student_id = int(line[0:3])
            name = line[3:].strip()
            student_data_dict[name] = student_id

    # print(student_data_dict)

    assign_id_to_total_points = {}
    assign_name_to_assign_id = {}

    with open(file_path_assignment, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            assign_id_to_total_points[int(lines[i + 1].strip())] = int(lines[i + 2].strip())
            assign_name_to_assign_id[lines[i].strip()] = int(lines[i + 1].strip())

    # print(assign_id_to_total_points)
    # print(assign_name_to_assign_id)

    submissions_dict = {}

    files = os.listdir("data/submissions")
    for filename in files:
        with open(f"data/submissions/{filename}", 'r') as file:
            split_info = file.readline().split("|")

            student_id = int(split_info[0])
            assignment_id = int(split_info[1])
            grade = float(split_info[2])

            if student_id not in submissions_dict:
                submissions_dict[student_id] = {}

            submissions_dict[student_id][assignment_id] = grade

    # print(submissions_dict)

    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Submission statistics\n")
    selection = input("Enter your selection: ")

    if selection == "1":

        student_name = input("What is the student's name: ") # Michael Potter


        if student_name not in student_data_dict:
            print("Student name not found")
        else:

            total_points_overall = 0
            total_points_earn = 0

            student_id = student_data_dict[student_name] #174

            for assignment_id, grade_percentage in submissions_dict[student_id].items():
                total_points_earn += assign_id_to_total_points[assignment_id] * (submissions_dict[student_id][assignment_id] / 100 )
                total_points_overall += assign_id_to_total_points[assignment_id]

            print(total_points_overall)
            print(total_points_earn)
            average = (total_points_earn / total_points_overall) * 100

            print(f"{round(average)}%")

    elif selection == "2":
        pass

    elif selection == "3":
        pass

if __name__ == "__main__":
    main()