import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.image(r"C:\Users\Brent\Pictures\Screenshots\Streamlit.png", width=200)


st.title("My Autobiography and Portfolio")

st.header("About Me")


st.write("""
Hello! I'm Brent Joseph A. Reyes, I love creating and designing websites.
I started my coding journey in 1st year college and have since developed numerous projects using various technologies.
My interest in technology led me to pursue a degree in BSIT major in programmming. where I honed my skills in software development, 
data science, and user experience design.
""")


st.header("My Portfolio")


st.subheader("Projects")

projects = [
    {
        "title": "Wildcats Innovation Laboratory Management System",
        "description":"This project is a cutting-edge web application developed using React and Django."
         "is an advanced platform developed to enhance the management of innovation laboratories at educational institutions. "
         "The system provides a comprehensive suite of tools designed to streamline lab operations, improve equipment utilization"
         "facilitate resource allocation, and enhance collaboration among students and faculty. "
        
    }

]

for project in projects:
    st.title(project["title"])
    st.write(project["description"])
    st.markdown("---")

skills = {
    "Programming Languages": 60,
    "Web Development": 70,
    "Data Science": 60
}
skills_df = pd.DataFrame(list(skills.items()), columns=["Skill", "Proficiency"])

st.subheader("Skills Proficiency")
st.bar_chart(skills_df.set_index("Skill"))

fig, ax = plt.subplots()
ax.bar(skills_df["Skill"], skills_df["Proficiency"], color=['#1f77b4', '#ff7f0e', '#2ca02c'])
ax.set_xlabel("Skill")
ax.set_ylabel("Proficiency (%)")
ax.set_title("Skill Proficiency Levels")
st.pyplot(fig)


st.header("Contact Me")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    submit_button = st.form_submit_button(label="Send")

if submit_button:
    st.success(f"Thank you for reaching out, {name}! I will get back to you soon.")

st.write("Made by JOSEPH")











