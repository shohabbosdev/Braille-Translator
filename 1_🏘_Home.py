import os
import numpy as np
import io
import tempfile
import time
import decimal
import streamlit as st
from ultralytics import YOLO
from PIL import Image
from braille_symbols import BrailleConverter

convertor = BrailleConverter()
st.set_page_config(
     page_title="Uz Braille",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded"
     )
# with open('src\style.css') as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>✍️ Brayl alifbosidan foydalanib yozishni o'rganamiz</h1>", unsafe_allow_html=True)
st.caption("O'zbekcha Brayl alifbosidan foydalanib matnlar bilan ishlash ko'nikmangizni oshiring")

def main():
    try:
        with st.sidebar:
            st.image('src/image.png', width=150)
            st.markdown("<p>👁 O'zbekcha Brayl tarjimon</p>",unsafe_allow_html=True)
            st.divider()
            tanlov = st.radio("Tarjima turini tanlang", options=("Matndan Braylga", "Brayldan matnga"))
            st.link_button(" Men bilan bog'lanish",'https://t.me/shohabbosdev',type='secondary', icon="💻",use_container_width=True)

        with st.expander("Brayl alifbosini ko'rish ⬇️"):
            st.image('src/alifbo.png', caption="Brayl alifbosi")

        if tanlov == "Matndan Braylga":
            st.write("Matndan Brayl yozuviga o'tkazish")
            text = st.chat_input("Matn kriting", max_chars=200)
            if text is None:
                st.info("Maydon bo'sh bo'lmasligiga e'tibor bering", icon='🥺')
            else:
                braille_text = convertor.convert_chars_to_braille(text)
                wrapped_braille = '<div>'
                for i in range(0, len(braille_text), 80):
                    line = braille_text[i:i+80]
                    colored_line = ''.join([f'<span>{char}</span>' if char != ' ' else char for char in line])
                    wrapped_braille += colored_line + '<br>'
                wrapped_braille += '</div>'
                st.write(f"<h4>Siz yozgan dastlabki matn:</h4><code>{text.capitalize()}</code>",unsafe_allow_html=True)
                st.write(f"<h4>Tarjima matn: 👇</h4> {wrapped_braille}", unsafe_allow_html=True)
                

        else:
            st.write("Brayl matndan oddiy matnga o'tkazish")
            text = st.chat_input("⠨⠃⠗⠁⠯⠇⠀⠍⠁⠞⠝⠊⠝⠊⠀⠅⠊⠗⠊⠞⠊⠝⠛⠲⠲⠲", max_chars=200)
            if text is None:
                st.info("Maydon bo'sh bo'lmasligiga e'tibor bering", icon='🥺')
            else:
                sample_text = convertor.convert_braille_to_chars(text)
                wrapped_braille = '<div style="width: 100%; word-wrap: break-word;">'
                for i in range(0, len(sample_text), 80):
                    line = sample_text[i:i+80]
                    colored_line = ''.join([f'<span style="color: #ff6347; font-size: 20pt">{char}</span>' if char != ' ' else char for char in line])
                    wrapped_braille += colored_line + '<br>'
                wrapped_braille += '</div>'
                st.write(f"<h4>Siz yozgan dastlabki matn:</h4><code>{text.capitalize()}</code>",unsafe_allow_html=True)
                st.write(f"<h4>Tarjima matn: 👇</h4> {wrapped_braille}", unsafe_allow_html=True)
                

    except Exception as e:
        st.error(f"Xatolik paydo bo'ldi: {e}")
if __name__ == '__main__':
    main()