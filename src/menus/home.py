import streamlit as st
from braille_symbols import BrailleConverter
import requests
import time

# BrailleConverter obyekti
converter = BrailleConverter()

def display_welcome_message():
    """Braille haqida umumiy tushuncha berish va qiziqtiruvchi kirish qismi"""
    st.markdown("# :link: :rainbow[Brayl alifbosidan o'zbek alifbosiga yoki aksincha o'tkazish]")
    st.markdown('''
    > :rainbow[Brayl shrifti]- koʻzi ojizlar oʻqish va yozishi uchun moʻljallangan boʻrtma nuqtalardan iborat shrift. 
    [Luis Brayl](https://www.labarandilla.org/wp-content/uploads/2018/01/luis-braille.jpg) tomonidan yaratilgan. 
    Brayl shrifti asosida :red[6] nuqtani turli vaziyatda uygʻunlashtirish yotadi.
    ''')
    st.caption("O'zbekcha Brayl alifbosidan foydalanib matnlar bilan ishlash ko'nikmangizni oshiring")


def user_registration():
    """Foydalanuvchining ism, familiya va elektron pochtasini olish va saqlash"""
    @st.dialog("Ro'yxatdan o'tish")
    def email_form(lastname, firstname, email):
        lastname = st.text_input("Familiyangizni kiriting", placeholder="Ulug'murodov")
        firstname = st.text_input("Ismingizni kiriting", placeholder="Shoh Abbos")
        email = st.text_input("Elektron pochtangizni kiriting", placeholder='shohabbosdev@gmail.com')
        
        if st.button("Saqlash", type='primary', icon='👌', use_container_width=True):
            st.session_state.email_form = {"lastname": lastname, "firstname": firstname, "email": email}
            st.rerun()
    
    if "email_form" not in st.session_state:
        st.write("Keling siz bilan tanishamiz")
        if st.button("Tanishish", type='primary', icon="✅", use_container_width=True):
            email_form("Alisherov", "Dilmurod", "alisher@gmail.com")
    else:
        st.markdown(f":mag_right: Sizning FISH: :rainbow[{st.session_state.email_form['lastname']} {st.session_state.email_form['firstname']}], :mailbox_closed: Elektron pochtangiz {st.session_state.email_form['email']}")


def audio_to_text_query(audio_bytes):
    """Audio fayldan matnni olish uchun so'rov yuborish funksiyasi"""
    headers = {"Authorization": f"Bearer {st.secrets['API_TOKEN']}"}
    try:
        response = requests.post(st.secrets['STTAPI_URL'], headers=headers, data=audio_bytes)
        return response.json()
    except Exception:
        st.error("Internetga ulanishda xatolik bor. Qurilmangiz internetga ulanganligini tekshiring.")
        return None


def upload_audio_and_convert(audio_file):
    """Audio faylni yuklab, uning ichidagi matnni ajratib olish"""
    output_text = ""

    if audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_file)

        with st.spinner("Audiodan matnlar aniqlanayabdi..."):
            output = audio_to_text_query(audio_bytes)
            time.sleep(2)
            if output:
                output_text = output.get('text', '')
                st.toast('Muvaffaqiyatli bajarildi!', icon='🎉')
            else:
                st.toast("Internet ulanish xatolik bo'ldi", icon='🔎')
    return output_text


def translation_options():
    """Tarjima turini tanlash va Brayl alifbosi bilan ishlash qismi"""
    with st.sidebar:
        st.image('src/image.png', width=150)
        st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")
        st.markdown('[shohabbosdev](https://github.com/shohabbosdev)')

    with st.expander("Brayl alifbosini ko'rish ⬇️"):
        st.image('src/alifbo.png', caption="Brayl alifbosi")


def text_to_braille_section(input_text):
    """Oddiy matndan Brayl yozuviga o'tkazish qismi"""
    st.markdown(":rainbow[Matndan Brayl yozuviga o'tkazish]")
    text = st.text_area("Ma'lumot yozishni boshlang?", key="matn_to_braille", value=input_text)
    
    if st.button("Braylga o'tkazish", icon='🧿'):
        if text:
            braille_text = converter.convert_chars_to_braille(text)
            wrapped_braille = ''.join(
                [f'<span style="color: red; font-size: 24pt">{char}</span>' if char != ' ' else char for char in braille_text]
            )
            
            resultRow1, resultRow2 = st.columns([1, 4])
            resultRow1.markdown(f"👇:rainbow[Siz yozgan dastlabki matn:]\n :blue-background[{text}]")
            resultRow2.markdown(f"👇:rainbow[Tarjima matn]\n\n {wrapped_braille}", unsafe_allow_html=True)


def braille_to_text_section(input_text):
    """Brayl yozuvini oddiy matnga o'tkazish qismi"""
    st.markdown(":rainbow[⠨⠃⠗⠁⠯⠇⠀⠍⠁⠞⠝⠙⠁⠝⠀⠕⠙⠙⠊⠯⠀⠍⠁⠞⠝⠛⠁⠀⠧⠞⠅⠁⠵⠊⠱]")
    text = st.text_area("⠨⠃⠗⠁⠯⠇⠀⠍⠁⠞⠝⠝⠊⠀⠅⠊⠗⠊⠞⠊⠝⠛", key="braille_to_text", value=input_text)
    
    if st.button("⠨⠍⠁⠞⠝⠛⠁⠀⠧⠞⠅⠁⠵⠊⠱", icon='🧭'):
        if text:
            sample_text = converter.convert_braille_to_chars(text)
            wrapped_text = ''.join(
                [f'<span style="color: red; font-size: 24pt">{char}</span>' if char != ' ' else char for char in text]
            )
            
            result1Row1, result1Row2 = st.columns(2)
            result1Row1.markdown(f"👇:rainbow[⠨⠎⠊⠵⠀⠯⠕⠵⠛⠁⠝⠀⠨⠃⠗⠁⠯⠇⠀⠍⠁⠞⠝⠒] \n :red[{wrapped_text}]", unsafe_allow_html=True)
            result1Row2.markdown(f"👇:rainbow[⠨⠞⠁⠗⠚⠊⠍⠁⠀⠍⠁⠞⠝] \n\n :green[{sample_text}]")


def app():
    display_welcome_message()
    user_registration()
    audio_file = st.sidebar.file_uploader('Audio yuklang (wav yoki ogg formatda)', type=['ogg', 'wav', 'mp3'], help="Audio faylni shu yerga olib keling")
    output_text = upload_audio_and_convert(audio_file)
    translation_options()

    # Tab shaklida tarjima bo'limlari
    tab1, tab2 = st.tabs(["Matndan Braylga", "⠨⠃⠗⠁⠯⠇⠙⠁⠝⠀⠍⠁⠞⠝⠛⠁"])
    with tab1:
        text_to_braille_section(output_text)
    with tab2:
        braille_to_text_section(converter.convert_chars_to_braille(output_text) if output_text else "")


if __name__ == "__main__":
    app()
