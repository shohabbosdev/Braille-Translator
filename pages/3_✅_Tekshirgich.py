import streamlit as st  
from transformers import pipeline  

# Modelni yuklash  
unmasker = pipeline('fill-mask', model='tahrirchi/tahrirchi-bert-small')  

# CSS faylini o'qish va Streamlit ilovasida qo'llash  
with open('src//style.css') as f:  
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  

# Kirish matni  
input_text = "Egiluvchan boʻgʻinlari va <mask>, yarim bukilgan tirnoqlari tik qiyaliklar hamda daraxtlarga oson chiqish imkonini beradi."
st.text_input("Matn kiriting", value=input_text)  

with st.sidebar:
    st.image('src/image.png', width=150)
    st.markdown("<p>👁 O'zbekcha Brayl tarjimon</p>",unsafe_allow_html=True)
    st.divider()
    st.link_button(" Men bilan bog'lanish",'https://t.me/shohabbosdev',type='secondary', icon="💻",use_container_width=True)

# Matnni to'ldirish  
results = unmasker(input_text)  

# Natijalarni chiqarish  
st.markdown("<h1>Maskni To'ldirish Dasturi</h1>",unsafe_allow_html=True)  
# st.write("Quyidagi matndagi <mask> ni to'ldirish natijalari:")  
for result in results:
    st.markdown(f"💬 {input_text.replace('<mask>', result['token_str'])} <br>(Aniqligi: {result['score']*100:.2f}%, 👉 {result['token_str']})",unsafe_allow_html=True)