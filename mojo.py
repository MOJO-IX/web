from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain 

# Directories and file paths
This_Dir = Path(__file__).parent
CSS_FILE = This_Dir / "style" / "style.css"
assets = This_Dir / "assets"
LOTTIE_ANIMATION = assets / "LottieFiles Platform_3.json"


# Function to load and display
#def load_lottie_animation(file_path):
    #with open(file_path, "r") as f:
        #return json.load(f)
    


# Function to snowfall
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")



# Function to get name
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["friend"])[0]


# PAGE CONFIGURATION
st.set_page_config(page_title="We are Here To help you", page_icon="❤️")

# Run snowfall
run_snow_animation()

# Apply custom css
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display header with name of person
person_name = get_person_name()
st.header(f"We are Here To help you, {person_name}! ❤️", anchor=False)

# Display the lottie animation 
#LOTTIE_ANIMATION = load_lottie_animation(LOTTIE_ANIMATION)
#st_lottie(LOTTIE_ANIMATION, key="Animation55", height=300)

# Personalized message
st.markdown(
    f"Dear {person_name}, we wish you the best! 👌😊"
)
