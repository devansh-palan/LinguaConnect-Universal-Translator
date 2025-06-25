LinguaConnect: Universal Translator
Overview
LinguaConnect is a Streamlit-based web application that provides seamless translation of text across multiple languages using the facebook/mbart-large-50-many-to-many-mmt model from Hugging Face. It supports 50+ languages, leveraging the power of AI to deliver accurate translations in a user-friendly interface.
Features

Multi-language Support: Translate text between 50+ languages, including Arabic, Chinese, English, French, Hindi, and more.
AI-Powered: Utilizes the MBART-50 model for high-quality translations.
Interactive UI: Built with Streamlit for an intuitive and responsive user experience.
GPU/CPU Support: Automatically detects and uses GPU (CUDA) if available, with fallback to CPU.
Efficient Caching: Uses Streamlit's caching to minimize model loading time.

Installation
Prerequisites

Python 3.8+
pip
(Optional) CUDA-compatible GPU for faster translations

Steps

Clone the Repository
git clone https://github.com/your-username/linguaconnect.git
cd linguaconnect


Set Up a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies
pip install -r requirements.txt


Run the Application
streamlit run app.py



Requirements
Create a requirements.txt file with the following:
streamlit
transformers
torch

Usage

Launch the app using the command above.
Open your browser to the provided local URL (e.g., http://localhost:8501).
Enter the text you want to translate in the text area.
Select the source and target languages from the dropdown menus.
Click the Translate button to see the translated text.

Example
Translate "Hello, how are you?" from English to French:

Input: Hello, how are you?
Source Language: en_XX
Target Language: fr_XX
Output: Bonjour, comment vas-tu ?
