import streamlit as st  
from transformers import pipeline  

st.logo(
    "src/logo.jpg",
    link="https://t.me/shohabbosdev"
)

def app():
    # Modelni yuklash  
    unmasker = pipeline('fill-mask', model='tahrirchi/tahrirchi-bert-small')  

    # # CSS faylini o'qish va Streamlit ilovasida qo'llash  
    # with open('src/style.css') as f:  
    #     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  
    st.markdown("<h1 style='text-align: center;'>✅ Matnlar tekshirgichi</h1>", unsafe_allow_html=True)
    with st.form("my_form"):
        input_text = "Egiluvchan boʻgʻinlari va <mask>, yarim bukilgan tirnoqlari tik qiyaliklar hamda daraxtlarga oson chiqish imkonini beradi."
        matn = st.text_area("Matn kiriting", value=input_text)  
        tugma = st.form_submit_button("Bajarish", type="primary", use_container_width=True, icon="👌")
        tozalash = st.form_submit_button("Tozalash", type="secondary", use_container_width=True, icon='🧹')
        # tozalash = st.form

        with st.sidebar:
            st.image('src/image.png', width=150)
            st.markdown("<p>👁 O'zbekcha Brayl tarjimon</p>",unsafe_allow_html=True)
            st.divider()
            st.markdown("<p style='font-weight: bold; color: rgba(25,25,225, 0.8);'>👁 O'zbekcha Brayl tarjimon</p>",unsafe_allow_html=True)
            
            st.link_button(" Men bilan bog'lanish",'https://t.me/shohabbosdev',type='secondary', icon="💻",use_container_width=True)

        if tugma:
            # Matnni to'ldirish  
            results = unmasker(matn)  

            # Natijalarni chiqarish  
            st.markdown("<h3 style='text-align: center; text-decoration: underline;'>Maskni To'ldirish Dasturi</h3>",unsafe_allow_html=True)  
            # st.write("Quyidagi matndagi <mask> ni to'ldirish natijalari:")  
            for result in results:
                st.markdown(f"💬 {matn.replace('<mask>', result['token_str'])} <br />(Aniqligi: <span style='color: blue;'>{result['score']*100:.2f}%</span>, 👉 <code>{result['token_str']})</code>",unsafe_allow_html=True)
        else:          
            st.write("## 2. Matematik model")
            st.write("Brayl belgisini tanib olish masalasini quyidagicha modellashtirish mumkin:")
            st.latex("B = \{b_1, b_2, ..., b_6\}")
            st.write("- har bir Brayl belgisidagi 6 ta nuqtaning holati (0 yoki 1)")
            st.latex("C = \{c_1, c_2, ..., c_n\}")
            st.write("- mumkin bo'lgan Brayl belgilari to'plami")
            st.latex(r"f : B\rightarrow  C")
            st.write("- klassifikatsiya funksiyasi")
            st.write("Maqsadimiz $f$ funksiyani shunday topishki, u xatolarni minimallashtirsin:")
            st.latex("\min E = \sum_{i=1}^m d(f(B_i), C_i")
            st.write("bunda $m$ - o'quv to'plamidagi namunalar soni, $d$ - xatolikni o'lchovchi metrika.")
            
            