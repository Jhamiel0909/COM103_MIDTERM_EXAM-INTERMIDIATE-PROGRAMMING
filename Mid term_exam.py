tasks = {
    1: ("Program Logic / Coding", 6),
    2: ("UI / Output Formatting", 3),
    3: ("Testing & Debugging", 2),
    4: ("Documentation / README", 2),
    5: ("Presentation Slides", 2)
}
project_title = input("Enter your project Title: ")
group_name = input("Enter your group name: ")

print("== Task Types ==")
for num, (task_name, hours) in tasks.items():
    print(f"{num}. {task_name} ({hours}h)")

assignment =[]
total_points = 0

for i in range(1, 5):
    print(f"Assignment Slot {i}")
    try:
        task_num = int(input("Enter task number (1–5) or 0 to skip: "))
    except ValueError:
        print("Invalid input. Skipping this slot.")
        continue

    if task_num == 0:
        continue

    if task_num in tasks:
        member = input("Enter member name: ")
        status = input("Enter task status (done/pending): ").strip().lower()
        
        if status == "done":
            points = 2
        else:
            points = 1

        total_point += points
        assignment.append({
            "task_num": task_num,
            "task_name": tasks[task_num][0],
            "hours": tasks[task_num][1],
            "member": member,
            "status": status,
            "points": points
        })
    else:
        print("Invalid task number. Skipping this slot.")
num_assigned = len(assignment)
max_possible = num_assigned * 2

if max_possible > 0:
    progress = int((total_points / max_possible) * 100)
else:
    progress = 0  

if progress >= 75:
    project_status = "PROJECT READY!"
elif progress >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"

print("===== PROJECT BOARD =====")
print(f"Project Title : {project_title}")
print(f"Group Name    : {group_name}")
print("Assigned Tasks: ")

if assignment:
    print(f"{'No.':<5}{'Task':<30}{'Hours':<8}{'Member':<15}{'Status':<10}{'Pts'}")
    print("-" * 75)

    for idx, task in enumerate(assignment, start=1):
        print(f"{idx:<5}{task['task_name']:<30}{task['hours']:<8}{task['member']:<15}{task['status']:<10}{task['points']}")
else:
    print("No tasks assigned.")

print("--------------------------")
print(f"Total Points     : {total_points}")
print(f"Max Possible     : {max_possible}")
print(f"Progress         : {progress}%")
print(f"Project Status   : {project_status}")
print("==========================")