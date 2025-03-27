import streamlit as st
import subprocess
import base64

# Function to encode the image to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Error: '{image_path}' not found.")
        return None

# Set the page title and favicon
st.set_page_config(
    page_title="Harry Potter Invisibility Cloak",
    page_icon="🧙‍♂️",
    layout="wide",
)

# Get base64 string of the background image
bg_image = get_base64_image("background1.jpg")

# Apply the background using custom CSS
if bg_image:
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{bg_image}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Create a container with centered content
container = st.container()

# Add header and description
with container:
    st.markdown("<h1 style='font-family: Harry Potter; color: #ffcc00; text-align: center;'>🧙‍♂️ Harry Potter Invisibility Cloak</h1>", unsafe_allow_html=True)

# Add a dropdown to choose cloak color
with container:
    st.markdown("<h2 style='font-family: Harry Potter; font-size: 20px; color: #fff; text-align: center;'>Choose Your Cloak Color</h2>", unsafe_allow_html=True)
    cloak_color = st.selectbox("", ["Red", "Green", "Blue", "Yellow"])

# Display the chosen cloak color
with container:
    st.markdown(f"<div style='background-color: {cloak_color.lower()}; width: 100%; height: 120px; border-radius: 10px; display: flex; justify-content: center; align-items: center; font-weight: bold; font-size: 18px; color: #ffffff;'>{cloak_color}</div>", unsafe_allow_html=True)

# Add a button to launch the corresponding color module
if cloak_color == "Red":
    if st.button("Launch Red Cloak"):
        try:
            subprocess.run(["python", "red.py"])
        except Exception as e:
            st.error(f"Error: {e}")
elif cloak_color == "Green":
    if st.button("Launch Green Cloak"):
        try:
            subprocess.run(["python", "green.py"])
        except Exception as e:
            st.error(f"Error: {e}")
elif cloak_color == "Blue":
    if st.button("Launch Blue Cloak"):
        try:
            subprocess.run(["python", "blue.py"])
        except Exception as e:
            st.error(f"Error: {e}")
elif cloak_color == "Yellow":
    if st.button("Launch Yellow Cloak"):
        try:
            subprocess.run(["python", "yellow.py"])
        except Exception as e:
            st.error(f"Error: {e}")
