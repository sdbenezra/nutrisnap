import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import json
import prompt, health_scale
import base64


def setup_page():
    st.set_page_config(page_title="NutriSnap", page_icon="🍎", layout="wide")
    st.header("🍎 NutriSnap", anchor=False, divider="green")
    st.write("Take a photo or upload a photo of the nutrition facts label or food item. The app will summarize the health value of your food.")
    st.write("**Bon Appetit!**")
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

model_version = "gemini-1.5-flash"
model = genai.GenerativeModel(model_version)

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

def analyze_image(image):
    promptText = prompt.prompt
    print(promptText)
    responses = model.generate_content([image, promptText], generation_config=genai.GenerationConfig(temperature=0, max_output_tokens=1500))
    responses.resolve()
    print("+++++++++++++++++++++++++++++++")
    print(responses)
    if ("**Overall Rating**: HEALTHY" in responses.text):
        render_svg(health_scale.get_health_scale_svg(rating='healthy'))
    elif ("**Overall Rating**: MODERATE" in responses.text):
        render_svg(health_scale.get_health_scale_svg(rating='moderate'))
    elif ("**Overall Rating**: LOW" in responses.text):
        render_svg(health_scale.get_health_scale_svg(rating='low'))
    st.markdown("  ")
    st.markdown(responses.text)

def main():
    """
    1. set up page
    2. ask user to take a picture
    3. submit to MLLM with a prompt
    4. display response

    Returns
    -------
    None.

    """

    setup_page()

    # Option selection
    option = st.radio(
        "Choose an option:",
        ("Take a picture", "Upload a picture")
    )

    col1, col2 = st.columns([1, 2])

    if option == "Take a picture":
        with col1:
            picture = st.camera_input("Take a picture")  
        with col2:
            if picture:
                with st.spinner():
                    image = Image.open(picture)
                    analyze_image(image)

    if option == "Upload a picture":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
        if (uploaded_file is not None):
            image = Image.open(uploaded_file)
            with col1:
                st.image(image, caption='Uploaded Image', use_column_width="auto")
            with col2:
                with st.spinner():
                    analyze_image(image)

    st.divider()
    st.markdown("""HEALTH INFORMATION DISCLAIMER  
 - This app provides educational information only, not medical advice.  
 - Nutritional needs vary by individual.  
 - Always consult your healthcare provider before making dietary changes.  
 - Do not rely on this app in place of professional medical guidance.""")
    st.write("")
    st.markdown(f"""PRIVACY NOTICE

- This app is powered by Google's {model_version} model
- Data submitted may be used by Google to improve their services
- Free API quota usage does not guarantee data privacy
- DO NOT SUBMIT:
  - Sensitive information
  - Confidential data
  - Personal information""")


if __name__ == '__main__':
    GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
    genai.configure(api_key=GOOGLE_API_KEY)
    main()
