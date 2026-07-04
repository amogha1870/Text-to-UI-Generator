# app.py
import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Text to UI Generator",
    page_icon="✨",
    layout="wide"
)

# Configure the Gemini API key from Streamlit secrets
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}. Make sure you have set your GOOGLE_API_KEY in Streamlit's secrets.")
    st.stop()

def get_gemini_response(user_description, prompt):
    """
    Sends the user's description and a system prompt to Gemini
    """
  
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    full_prompt = f"{prompt}\n\nHere is the user's description of the UI:\n\n{user_description}"
    response = model.generate_content(full_prompt)
    
  
    cleaned_code = response.text.replace("```html", "").replace("```", "").strip()
    return cleaned_code

st.title("📝 Text-to-UI Generator")
st.write("Describe the web page you want to create, and the AI will generate the HTML and CSS code for it.")

# Define the detailed "system prompt" for the model. 
system_prompt = """
You are an expert web developer specializing in Tailwind CSS.
Your task is to take a natural language description of a UI and generate a single, complete HTML file that accurately represents it.
Follow these rules strictly:
1.  **Single HTML File:** Generate only a single HTML file.
2.  **Tailwind CSS:** Use Tailwind CSS for all styling. You MUST include the official Tailwind CDN script in the `<head>` section: `<script src="https://cdn.tailwindcss.com"></script>`. Do not use any custom CSS in a `<style>` tag or inline `style="..."` attributes.
3.  **Accuracy:** Faithfully translate the user's description into a visual layout. Pay attention to colors, layout, text, and components mentioned.
4.  **Placeholders:** For any images, use placeholder images from `https://placehold.co/`. For example: `https://placehold.co/600x400`. For user avatars, use `https://i.pravatar.cc/150`.
5.  **Code Only:** Your entire output must be ONLY the HTML code. Start with `<!DOCTYPE html>` and end with `</html>`. Do not include any explanations, comments, or markdown formatting.
"""
col1, col2 = st.columns([1, 1.2]) 

with col1:
    st.subheader("Describe Your UI")
    user_input = st.text_area(
        "Enter a detailed description of your desired UI:",
        height=300,
        placeholder="e.g., A clean login page with a centered card. The card should have a logo, an email field, a password field, and a 'Sign In' button. The background should be a light gray."
    )

    if st.button("✨ Generate Code"):
        if user_input:
            with st.spinner(" AI is crafting your UI..."):
                try:
                    
                    generated_code = get_gemini_response(user_input, system_prompt)
                    
                 
                    st.session_state.generated_code = generated_code

                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.session_state.generated_code = None
        else:
            st.warning("Please enter a description for your UI.")

with col2:
    st.subheader("Generated Code & Preview")
    
   
    if "generated_code" in st.session_state and st.session_state.generated_code:
        st.code(st.session_state.generated_code, language='html')
        with st.expander("Show Preview", expanded=True):
           
            st.components.v1.html(st.session_state.generated_code, height=600, scrolling=True)
