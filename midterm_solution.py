tasks = {
    1: ("Program Logic / Coding", 6),
    2: ("UI / Output Formatting", 3),
    3: ("Testing & Debugging", 2),
    4: ("Documentation / README", 2),
    5: ("Presentation Slides", 2)
}


project_title = input("Project title: ")
group_name = input("Group name: ")


print("==========================================")
print("   COM 103 PROJECT -- TASK TYPES")
print("==========================================")
for num, (task_name, hours) in tasks.items():
    print(f" {num}. {task_name:<25} [{hours}h]")
print("==========================================")


assignment = []
total_points = 0

for i in range(1, 5):
    print(f"--- TASK {i} ---")
    task_input = input("Task number (0 to skip): ")

    
    if task_input not in ["0", "1", "2", "3", "4", "5"]:
        print("Invalid input. Skipping this slot.")
        continue

    task_num = int(task_input)

    if task_num == 0:
        print("Slot skipped.")
        continue

    member = input("Member name: ")
    status = input("Status (done/pending): ").strip()

    if status == "done":
        points = 2
    else:
        points = 1

    total_points += points

    assignment.append({
        "task_num": task_num,
        "task_name": tasks[task_num][0],
        "hours": tasks[task_num][1],
        "member": member,
        "status": status,
        "points": points
    })
    print()  


num_assigned = len(assignment)
max_possible = num_assigned * 2

progress = int((total_points / max_possible) * 100) if max_possible > 0 else 0

if progress >= 75:
    project_status = "PROJECT READY!"
elif progress >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"


print("================================================")
print(f"     {project_title} -- TASK BOARD")
print("================================================")
print(f"Project : {project_title}")
print(f"Group   : {group_name}")
print("------------------------------------------------")

for idx, task in enumerate(assignment, start=1):
    print(f"[{idx}] {task['task_name']:<25} [{task['hours']}h]")
    print(f"    Assigned to : {task['member']}")
    print(f"    Status      : {task['status']}")
    print(f"    Points      : {task['points']} / 2\n")

print("------------------------------------------------")
print(f"Points Earned   : {total_points} / {max_possible}")
print(f"Progress        : {progress}%")
print(f"Project Status  : {project_status}")
print("================================================")
