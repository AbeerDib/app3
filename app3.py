import streamlit as st

import requests
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# local_css("style/style.css")

# # ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sven :wave:")
    st.title("A Data Analyst From Germany")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")



# from streamlit_lottie import st_lottie

# st.set_page_config(page_title="My Webpage", page_icon="🥼", layout="wide")
# st.subheader("Welcome to the faculty of medecine :wave:")
# st.write("[Learn More >](https://www.aub.edu.lb/FM/Pages/default.aspx)")

# def chatbot_response(user_input):
#     if "course" in user_input.lower():
#         return "You can find the course details on our website."
#     elif "contact" in user_input.lower():
#         return "You can contact the administration at contact@university.edu."
#     else:
#         return "I'm sorry, I didn't understand that. Can you please rephrase?"

# st.title("Faculty of Medicine Chatbot")
# st.write("Ask me anything about the faculty!")

# user_input = st.text_input("You:", "")
# if user_input:
#     response = chatbot_response(user_input)
#     st.write(f"Chatbot: {response}")

