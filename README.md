overview for python task tracker com 103

This Python program is a comprehensive yet simple project task tracker designed for group projects, particularly useful for students collaborating on assignments.
The program allows groups to organize, assign, and monitor tasks while tracking progress in a structured manner.

Features and Workflow:

Predefined Tasks with Estimated Hours:
The program comes with five common project tasks, each with an estimated number of hours to help in planning:
Program Logic / Coding (6h)
UI / Output Formatting (3h)
Testing & Debugging (2h)
Documentation / README (2h)
Presentation Slides (2h)
This helps the group quickly understand the workload associated with each task.
Interactive User Input:
Users enter the project title and group name, personalizing the task tracker for their team.
The program displays all task types with their corresponding numbers and estimated hours.
Users can assign up to four tasks, specifying:
Task number (or skip by entering 0)
Member responsible for the task
Task completion status (done or pending)
Point-Based Task Completion:
Completed tasks earn 2 points; pending tasks earn 1 point.
Points are used to calculate the overall progress of the project.
This point system provides a simple way to quantify productivity and contribution.
Automated Progress Calculation:
The program calculates progress as a percentage using the ratio of earned points to maximum possible points.
Based on the calculated percentage, a project status label is automatically assigned:
75% or higher → PROJECT READY!
50–74% → ON TRACK.
Below 50% → NEEDS MORE WORK!
This gives the team a quick visual cue of the project’s completion level.
Formatted Project Board Display:
The program prints a well-organized project board showing:
Task number, task name, estimated hours, assigned member, task status, and points earned
Total points, maximum possible points, progress percentage, and overall project status
This provides a clear and immediate overview of the group’s workload and progress, helping members stay coordinated.
Error Handling and User-Friendly Design:
The program gracefully handles invalid inputs (like non-numeric task numbers) by skipping the assignment slot, preventing crashes.
Users can skip any assignment slot by entering 0, making the program flexible for teams with fewer than four tasks.

Purpose and Benefits:

This program helps groups track task assignments and completion in a simple, organized, and visually clear way.
It encourages accountability, as each member’s assignment and status are recorded.
It provides instant feedback on progress, helping the team identify tasks that need attention before deadlines.
It can be used as a foundation for more advanced project management tools or as a learning exercise for beginners in Python programming.
