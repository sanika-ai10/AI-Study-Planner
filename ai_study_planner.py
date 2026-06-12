# ==========================================
# AI STUDY PLANNER
# Python Mini Project
# ==========================================

tasks = []

# ------------------------------------------
# Function to add task
# ------------------------------------------

def add_task():

    subject = input("Enter Subject: ")
    topic = input("Enter Topic: ")
    hours = int(input("Enter Hours Required: "))

    print("Difficulty Levels:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = int(input("Choose Difficulty: "))

    if choice == 1:
        difficulty = "Easy"
        priority = hours * 1

    elif choice == 2:
        difficulty = "Medium"
        priority = hours * 2

    else:
        difficulty = "Hard"
        priority = hours * 3

    task = [subject, topic, hours, difficulty, priority, False]

    tasks.append(task)

    print("Task Added Successfully")


# ------------------------------------------
# Function to view tasks
# ------------------------------------------

def view_tasks():

    if len(tasks) == 0:
        print("No Tasks Added")
        return

    print("\n------ TASK LIST ------")

    for i in range(len(tasks)):

        if tasks[i][5] == True:
            status = "Completed"
        else:
            status = "Pending"

        print(
            i + 1,
            "| Subject:", tasks[i][0],
            "| Topic:", tasks[i][1],
            "| Hours:", tasks[i][2],
            "| Difficulty:", tasks[i][3],
            "|", status
        )


# ------------------------------------------
# Mark task complete
# ------------------------------------------

def complete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    task_no = int(input("Enter Task Number: "))

    if task_no >= 1 and task_no <= len(tasks):

        tasks[task_no - 1][5] = True

        print("Task Marked Completed")

    else:
        print("Invalid Task Number")


# ------------------------------------------
# Dashboard
# ------------------------------------------

def dashboard():

    total_tasks = len(tasks)

    completed = 0
    total_hours = 0

    for task in tasks:

        total_hours = total_hours + task[2]

        if task[5] == True:
            completed = completed + 1

    print("\n------ DASHBOARD ------")
    print("Total Tasks:", total_tasks)
    print("Completed Tasks:", completed)
    print("Hours Planned:", total_hours)

    if total_tasks > 0:

        progress = (completed / total_tasks) * 100

        print("Progress:", round(progress, 2), "%")


# ------------------------------------------
# AI Recommendation
# ------------------------------------------

def recommendation():

    hard_tasks = 0

    for task in tasks:

        if task[3] == "Hard":
            hard_tasks = hard_tasks + 1

    print("\n------ AI RECOMMENDATION ------")

    if hard_tasks >= 3:

        print("You have many difficult tasks.")
        print("Take short breaks while studying.")

    elif hard_tasks == 0 and len(tasks) > 0:

        print("Your workload looks manageable today.")

    else:

        print("Stay consistent and complete tasks one by one.")


# ------------------------------------------
# Timetable Generator
# ------------------------------------------

def timetable():

    if len(tasks) == 0:

        print("No Tasks Available")
        return

    print("\n------ STUDY TIMETABLE ------")

    sorted_tasks = sorted(
        tasks,
        key=lambda x: x[4],
        reverse=True
    )

    slot = 1

    for task in sorted_tasks:

        print(
            "Slot", slot,
            "->",
            task[0],
            "-",
            task[1],
            "(",
            task[2],
            "Hours )"
        )

        slot = slot + 1


# ------------------------------------------
# Attendance Calculator
# ------------------------------------------

def attendance():

    print("\n------ ATTENDANCE CALCULATOR ------")

    attended = int(input("Classes Attended: "))
    total = int(input("Total Classes: "))

    percentage = (attended / total) * 100

    print("Attendance =", round(percentage, 2), "%")

    if percentage >= 75:

        print("Attendance Safe")

    else:

        future_attended = attended
        future_total = total

        required = 0

        while (future_attended / future_total) * 100 < 75:

            future_attended = future_attended + 1
            future_total = future_total + 1

            required = required + 1

        print("Attendance Low")
        print(
            "Attend",
            required,
            "consecutive classes to reach 75%"
        )


# ------------------------------------------
# Motivational Quote
# ------------------------------------------

def quote():

    print("\nQuote Of The Day")
    print("Small Progress Is Still Progress")


# ------------------------------------------
# Main Program
# ------------------------------------------

while True:

    print("\n================================")
    print("        AI STUDY PLANNER")
    print("================================")

    print("1. Add Study Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Dashboard")
    print("5. AI Recommendation")
    print("6. Generate Timetable")
    print("7. Attendance Calculator")
    print("8. Motivational Quote")
    print("9. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_task()

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        complete_task()

    elif choice == 4:
        dashboard()

    elif choice == 5:
        recommendation()

    elif choice == 6:
        timetable()

    elif choice == 7:
        attendance()

    elif choice == 8:
        quote()

    elif choice == 9:

        print("Thank You For Using AI Study Planner")
        break

    else:

        print("Invalid Choice")
