import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📚",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #f7f7f5;
}

.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #222222;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 25px;
}

.section-title {
    font-size: 24px;
    font-weight: bold;
    color: #222222;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    "<div class='main-title'>📚 AI Study Planner</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Plan smarter, study better and stay consistent ✨</div>",
    unsafe_allow_html=True
)

# ---------------- SESSION STATE ----------------

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------------- MOTIVATIONAL QUOTES ----------------

quotes = [
    "Small progress is still progress 📈",
    "Study now, stress less later 😎",
    "Every chapter completed is a win 🏆",
    "Consistency beats intensity 💪",
    "One task at a time leads to big results 🎯"
]

st.info(random.choice(quotes))

# ---------------- PRIORITY FUNCTION ----------------

def priority_score(hours, difficulty):

    if difficulty == "Easy":
        return hours * 1

    elif difficulty == "Medium":
        return hours * 1.5

    else:
        return hours * 2

# ---------------- ADD TASK ----------------

st.markdown(
    "<div class='section-title'>➕ Add Study Task</div>",
    unsafe_allow_html=True
)

with st.form("task_form"):

    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input("Subject")

    with col2:
        topic = st.text_input("Topic")

    col3, col4 = st.columns(2)

    with col3:
        hours = st.slider("Hours Required", 1, 8, 2)

    with col4:
        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"]
        )

    submit = st.form_submit_button("Add Task")

if submit:

    if subject.strip() and topic.strip():

        score = priority_score(hours, difficulty)

        st.session_state.tasks.append({
            "Subject": subject,
            "Topic": topic,
            "Hours": hours,
            "Difficulty": difficulty,
            "Priority": score
        })

        st.success("Task Added Successfully ✅")

    else:
        st.warning("Please enter Subject and Topic")

# ---------------- TASK TRACKER ----------------

st.markdown(
    "<div class='section-title'>📌 Task Tracker</div>",
    unsafe_allow_html=True
)

completed_tasks = 0

if st.session_state.tasks:

    for i, task in enumerate(st.session_state.tasks):

        checked = st.checkbox(
            f"{task['Subject']} - {task['Topic']}",
            key=f"task_{i}"
        )

        if checked:
            completed_tasks += 1

else:
    st.info("No tasks added yet.")

# ---------------- DASHBOARD ----------------

total_tasks = len(st.session_state.tasks)

total_hours = sum(
    task["Hours"]
    for task in st.session_state.tasks
)

st.markdown(
    "<div class='section-title'>📊 Dashboard</div>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tasks", total_tasks)

with col2:
    st.metric("Completed", completed_tasks)

with col3:
    st.metric("Hours Planned", total_hours)

# ---------------- PROGRESS BAR ----------------

if total_tasks > 0:

    progress = completed_tasks / total_tasks

    st.progress(progress)

    st.write(
        f"Progress: {completed_tasks}/{total_tasks} Tasks Completed"
    )

# ---------------- TASK TABLE ----------------

if st.session_state.tasks:

    table_data = []

    for i, task in enumerate(st.session_state.tasks):

        table_data.append({
            "Subject": task["Subject"],
            "Topic": task["Topic"],
            "Hours": task["Hours"],
            "Difficulty": task["Difficulty"],
            "Priority": task["Priority"],
            "Completed": st.session_state.get(
                f"task_{i}",
                False
            )
        })

    st.dataframe(
        pd.DataFrame(table_data),
        use_container_width=True,
        hide_index=True
    )

# ---------------- AI RECOMMENDATION ----------------

st.markdown(
    "<div class='section-title'>🤖 AI Recommendation</div>",
    unsafe_allow_html=True
)

hard_tasks = [
    task
    for task in st.session_state.tasks
    if task["Difficulty"] == "Hard"
]

if len(hard_tasks) >= 3:

    st.warning(
        "You have several difficult tasks. Take short breaks between study sessions."
    )

elif len(hard_tasks) == 0 and total_tasks > 0:

    st.success(
        "Your workload looks manageable today!"
    )

# ---------------- SMART TIMETABLE ----------------

st.markdown(
    "<div class='section-title'>🧠 Smart Study Timetable</div>",
    unsafe_allow_html=True
)

if st.button("Generate Timetable"):

    if st.session_state.tasks:

        sorted_tasks = sorted(
            st.session_state.tasks,
            key=lambda x: x["Priority"],
            reverse=True
        )

        current = datetime.now().replace(
            minute=0,
            second=0,
            microsecond=0
        )

        plan = []

        for task in sorted_tasks:

            end = current + timedelta(
                hours=task["Hours"]
            )

            plan.append({
                "Time Slot":
                f"{current.strftime('%I:%M %p')} - {end.strftime('%I:%M %p')}",
                "Subject": task["Subject"],
                "Topic": task["Topic"]
            })

            current = end

        st.success("Timetable Generated 🎯")

        st.table(
            pd.DataFrame(plan)
        )

    else:
        st.warning(
            "Please add tasks first."
        )

# ---------------- ATTENDANCE CALCULATOR ----------------


st.markdown(
    "<div class='section-title'>📅 Attendance Calculator</div>",
    unsafe_allow_html=True
)

subjects = [
    "Mathematics",
    "Python",
    "Civil",
    "BEE",
    "CAD",
    "English"
]

attendance_data = []

for subject in subjects:

    st.subheader(subject)

    col1, col2 = st.columns(2)

    with col1:
        attended = st.number_input(
            f"{subject} - Classes Attended",
            min_value=0,
            value=0,
            key=f"{subject}_attended"
        )

    with col2:
        total = st.number_input(
            f"{subject} - Total Classes",
            min_value=1,
            value=1,
            key=f"{subject}_total"
        )

    percentage = (attended / total) * 100

    attendance_data.append({
        "Subject": subject,
        "Attendance %": round(percentage, 2)
    })

    if percentage >= 75:

        st.success(
            f"Attendance: {percentage:.2f}% ✅ Safe"
        )

    else:

        required_classes = 0

        future_attended = attended
        future_total = total

        while (future_attended / future_total) * 100 < 75:
            future_attended += 1
            future_total += 1
            required_classes += 1

        st.error(
            f"Attendance: {percentage:.2f}% ⚠️"
        )

        st.warning(
            f"You must attend {required_classes} consecutive classes to reach 75% attendance."
        )

st.markdown("### Attendance Summary")

st.dataframe(
    pd.DataFrame(attendance_data),
    use_container_width=True,
    hide_index=True
)

# ---------------- RESET BUTTON ----------------

if st.button("Reset All Tasks"):

    st.session_state.tasks = []

    keys_to_delete = [
        key for key in st.session_state.keys()
        if key.startswith("task_")
    ]

    for key in keys_to_delete:
        del st.session_state[key]

    #st.rerun()

# ---------------- FOOTER ----------------

st.markdown("---")
st.caption("Python Mini Project | AI Study Planner 📚")
