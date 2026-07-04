# Text to UI Generator using Generative AI

A tool that converts natural language text prompts into functional HTML/CSS UI components using Google's Gemini API and Streamlit.

## 🚀 Live Demo

https://text-to-ui-generator-rfavk2g9zp2dtmanpq7ruj.streamlit.app/

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    `git clone https://github.com/amogha1870/Text-to-UI-Generator.git`

2.  **Install dependencies:**
    `pip install -r requirements.txt`

3.  **Add Your API Key (Crucial Step):**
    *   Create a folder named `.streamlit` in the project's root directory: `mkdir .streamlit`
    *   Inside that folder, create a file named `secrets.toml`.
    *   Add your Google API key to the `secrets.toml` file like this:
        ```toml
        GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
        ```

4.  **Run the Streamlit application:**
    `streamlit run app.py`
