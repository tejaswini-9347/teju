import streamlit as st
from googletrans import Translator, LANGUAGES

# Streamlit Page Config
st.set_page_config(page_title="Multi-Language Translator", page_icon="\U0001F310", layout="centered")

# Title and Description
st.title("🌍 Multi-Language Translator")
st.write("Powered by Google Translate")

# Language Selection
language_dict = LANGUAGES  # Get all languages
language_names = list(language_dict.values())  # Extract language names

col1, col2 = st.columns(2)

with col1:
    src_lang = st.selectbox("Select Input Language", language_names, index=language_names.index("english"))

with col2:
    dest_lang = st.selectbox("Select Output Language", language_names, index=language_names.index("french"))

# Text Input
text_to_translate = st.text_area("Enter Text to Translate", "")

# Translate Button
if st.button("Translate"):
    if text_to_translate.strip():
        try:
            translator = Translator()
            
            # Convert language names to language codes
            src_code = [code for code, name in language_dict.items() if name == src_lang][0]
            dest_code = [code for code, name in language_dict.items() if name == dest_lang][0]
            
            translated_text = translator.translate(text=text_to_translate, src=src_code, dest=dest_code).text
            
            # Display Translated Text
            st.subheader("Translated Text")
            st.success(translated_text)
        except Exception as e:
            st.error("Translation Error! Please check input or language selection.")
    else:
        st.warning("Please enter text to translate!")
