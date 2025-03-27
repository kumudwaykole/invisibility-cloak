import streamlit as st
import base64  # Missing import

# Function to load an image and convert it to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Error: '{image_path}' not found.")
        return None

# Set page title, favicon, and layout
st.set_page_config(
    page_title="Harry Potter Invisibility Cloak",
    page_icon="🧙‍♂️",  # Wizard emoji as favicon
    layout="wide",
)

# Get base64 string of the background image
bg_image = get_base64_image("background.jpg")

# Apply the background using custom CSS (only if image is found)
if bg_image:
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{bg_image}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: white;
                text-align: center;
            }}
            .cloak-container {{
                padding: 20px;
                background: rgba(0, 0, 0, 0.7);
                border-radius: 10px;
            }}
            .cloak-button:hover {{
                background-color: #ffcc00 !important;
                transform: scale(1.1);
                transition: 0.3s;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# st.title("🧙‍♂️ Harry Potter's Invisibility Cloak")
# st.write("Step into the magical world and choose your cloak color to disappear like Harry Potter!")

# Title with magical font
st.markdown("""
    <h1 style='font-family: fantasy; color: gold; text-shadow: 2px 2px 5px #000;'>
        🔮 Harry Potter's Invisibility Cloak
    </h1>
""", unsafe_allow_html=True)

st.write("Step into the magical world and choose your cloak color to disappear like Harry Potter!")

# Cloak color selection with emojis for fun
cloak_color = st.selectbox(
    "Choose Your Cloak Color",
    ["\U0001F534 Red", "\U0001F7E2 Green", "\U0001F535 Blue", "\U0001F7E1 Yellow"],
    index=1,
)

# Extract the color name
color_name = cloak_color.split(" ")[1].lower()

# Display a preview box for the selected color
st.markdown(f"""
    <div style='background-color: {color_name}; width: 100%; height: 80px;
                border-radius: 10px; display: flex; justify-content: center;
                align-items: center; font-size: 24px; color: white;'>
        {cloak_color}
    </div>
""", unsafe_allow_html=True)

# Button to activate the selected cloak
if st.button(f"Activate {cloak_color} Cloak", key=color_name, help="Click to vanish!"):
    try:
        subprocess.run(["python", f"{color_name}.py"])
        st.success(f"{cloak_color} Cloak Activated! 🌟")
    except Exception as e:
        st.error(f"Error: {e}")

# Add some animation text for effect
st.markdown("""
    <h3 style='color: lightblue;'>
        "The cloak shimmers... You slowly fade away!" 🌟
    </h3>
""", unsafe_allow_html=True)
