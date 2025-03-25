import streamlit as st
import subprocess

# Set the page title and background image
st.set_page_config(
    page_title="Harry Potter Invisibility Cloak",
    page_icon=":clover:",
    layout="wide",
)

# Create a container with centered content
st.markdown(
    """
    <style>
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-image: url('/mystical.jpg');
            background-size: cover;
            background-repeat: no-repeat;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a container div
container = st.container()

# Add header and description
with container:
    st.markdown("<h1 style='font-family: Harry Potter; color: #333;'>Harry Potter Invisibility Cloak</h1>", unsafe_allow_html=True)
  
# Add a dropdown to choose cloak color
with container:
    st.markdown("<h2 style='font-family: Harry Potter; font-size: 20px; color: #555;'>Choose Your Cloak Color</h2>", unsafe_allow_html=True)
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
