import streamlit as st
from braille_symbols import BrailleConverter 
import requests
import time

def app():
    # Braille converter obyekti
    convertor = BrailleConverter()
    
    st.markdown("# :link: :rainbow[Brayl alifbosidan o'zbek alifbosiga yoki aksincha o'tkazish]")
    st.markdown('''
    > :rainbow[Brayl shrifti]- boʻrtma nuqtalardan iborat shrift. Koʻzi ojizlar oʻqish va yozishi uchun moʻljallangan. 
    [Luis Brayl](https://www.labarandilla.org/wp-content/uploads/2018/01/luis-braille.jpg) tomonidan yaratilgan. 
    Brayl shrifti asosida :red[6] nuqtani turli vaziyatda uygʻunlashtirish yotadi.
    ''')
    @st.dialog("Ro'yxatdan o'tish")
    def email_form(lastname,firstname,email):
        lastname=st.text_input("Familiyangizni kiriting", placeholder="Ulug'murodov")
        firstname=st.text_input("Ismingizni kiriting", placeholder="Shoh Abbos")
        email=st.text_input("Elektron pochtangizni kiriting", placeholder='shohabbosdev@gmail.com')
        if st.button("Saqlash", type='primary', icon='👌', use_container_width=True):
            st.session_state.email_form = {"lastname":lastname, "firstname":firstname, "email":email}
            st.rerun()
    if "email_form" not in st.session_state:
        st.write("Keling siz bilan tanishamiz")
        if st.button("Tanishish", type='primary', icon="✅",use_container_width=True):
            email_form("Alisherov","Dilmurod","alisher@gmail.com")
    else:
        st.markdown(f":mag_right: Sizning FISH: :rainbow[{st.session_state.email_form['lastname']} {st.session_state.email_form['firstname']}], :mailbox_closed: Elektron pochtangiz {st.session_state.email_form['email']}")
    st.caption("O'zbekcha Brayl alifbosidan foydalanib matnlar bilan ishlash ko'nikmangizni oshiring")

    def query(audio_bytes):
        headers = {"Authorization": f"Bearer {st.secrets['API_TOKEN']}"}
        response = requests.post(st.secrets['STTAPI_URL'], headers=headers, data=audio_bytes)
        return response.json()

    def hisoblash():
        # Audio yuklash
        audio_file = st.sidebar.file_uploader('Audio yuklang (wav yoki ogg formatda)', type=['ogg', 'wav', 'mp3'], help="Audio faylni shu yerga olib keling")
        output_text = ""  # Natijani saqlash uchun

        if audio_file is not None:
            audio_bytes = audio_file.read()
            st.audio(audio_file)

            with st.spinner("Audiodan matnlar aniqlanayabdi..."):
                output = query(audio_bytes)
                time.sleep(2)
                st.toast('Muvaffaqiyatli bajarildi!', icon='🎉')
                output_text = output.get('text', '')

        # Tarjima turini tanlash
        with st.sidebar:
            st.image('src/image.png', width=150)
            st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")
            st.divider()
            tanlov = st.radio("Tarjima turini tanlang", options=("Matndan Braylga", "Brayldan matnga"))
            st.markdown('[shohabbosdev](https://github.com/shohabbosdev)')    

        with st.expander("Brayl alifbosini ko'rish ⬇️"):
            st.image('src/alifbo.png', caption="Brayl alifbosi")

        # Tarjima bo'limi
        with st.container(border=True, key="container1"):
            if tanlov == "Matndan Braylga":
                st.markdown(":rainbow[Matndan Brayl yozuviga o'tkazish]")
                st.markdown("### 👋 :green[Brayl yozuviga o'tkazadigan matnni kiriting ]")
                
                text = st.text_area("Ma'lumot yozishni boshlang?", key="matn_to_braille", 
                                    value=output_text if audio_file is not None else " ")
                if text:  # Faqat text mavjud bo'lganda bajariladi
                    braille_text = convertor.convert_chars_to_braille(text)
                    wrapped_braille = ''.join([f'<span style="color: red; font-size: 24pt">{char}</span>' if char != ' ' else char 
                                            for char in braille_text])
                    
                    resultRow1, resultRow2 = st.columns([1, 4])
                    resultRow1.markdown(f"👇:rainbow[Siz yozgan dastlabki matn:]\n :blue-background[{text}]")
                    resultRow2.markdown(f"👇:rainbow[Tarjima matn]\n {wrapped_braille}", unsafe_allow_html=True)

            else:
                st.markdown(":rainbow[Brayl matndan oddiy matnga o'tkazish]")
                st.markdown("### 👋 :blue[⠨⠃⠗⠁⠯⠇⠀⠍⠁⠞⠝⠊⠝⠊⠀⠅⠊⠗⠊⠞⠊⠝⠛⠲⠲⠲]")
                
                text = st.text_area("Ma'lumot yozishni boshlang?", key="braille_to_text", value=convertor.convert_chars_to_braille(output_text) if audio_file is not None else "⠨⠁⠎⠎⠁⠇⠕⠍⠥⠀⠁⠇⠁⠯⠅⠥⠍")

                if text:
                    sample_text = convertor.convert_braille_to_chars(text)
                    wrapped_text = ''.join([f'<span style="color: #0fad47; font-size: 24pt">{char}</span>' if char != ' ' else char 
                                            for char in text])
                    
                    result1Row1, result1Row2 = st.columns(2)
                    result1Row1.markdown(f"👇:rainbow[Siz yozgan Brayl matn:] \n :blue[{wrapped_text}]", unsafe_allow_html=True)
                    result1Row2.markdown(f"👇:rainbow[Tarjima matn] \n\n :green[{sample_text}]")

    hisoblash()
