import streamlit as st
import asyncio
import aiohttp
import time
from latin_cyrillic_symbols import to_cyrillic

# API tokeni va URL'ni himoyalangan holda olish
api_key,API_URL = st.secrets["API_TOKEN"],st.secrets["API_URL"]

def create_braille_symbols(symbol_type="alphabet"):
    symbols = {
        'alphabet': {
            'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
            'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
            'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
            'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
            'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
            'z': '⠵', 'ch': '⠟', 'sh': '⠱', "o'": '⠧', "g'": '⠻'
        },
        'numbers': {
            '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
            '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊'
        }
    }
    return symbols[symbol_type]

async def text_to_speech(text, language="uz"):
    try:
        text = text if any('\u0400' <= char <= '\u04FF' for char in text) else to_cyrillic(text)
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"inputs": text}
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, headers=headers, json=payload) as response:
                if response.status == 200:
                    return await response.read()
                else:
                    error_message = await response.text()  
                    st.error(f"⚠️ Xatolik: Server javobida xato (Status kodi: {response.status}). Tafsilotlar: {error_message}")
                    return None
    except Exception as e:
        st.error(f"❌ Xatolik: {e}")
        return None

def app():
    if 'result' not in st.session_state:
        st.session_state.result = ""
    st.markdown("# ✅ :rainbow[Brayl klaviaturasi]")

    # Braille harflarini ko'rsatish
    st.markdown("## 🔑 :red[Brayl Harflari]")
    alphabet = create_braille_symbols("alphabet")
    ustunlar_soni = [5,6]
    cols = st.columns(ustunlar_soni[1])
    for i, (letter, symbol) in enumerate(alphabet.items()):
        col = cols[i % ustunlar_soni[1]]  
        with col:
            if st.button(symbol, key=f"btn_{letter}", help=f"{letter}"):
                st.session_state.result += letter
    st.markdown("## 📌 :green[Brayl Raqamlari]")
    numbers = create_braille_symbols("numbers")
    with st.sidebar:
        st.divider()
        st.image('src/image.png', width=150)
        st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")
    num_cols = st.columns(ustunlar_soni[0])
    for i, (number, symbol) in enumerate(numbers.items()):
        col = num_cols[i % ustunlar_soni[0]]
        with col:
            if st.button(symbol, key=f"num_btn_{number}", help=f"{number}"):
                st.session_state.result += number
    st.markdown("<div class='control-buttons'>", unsafe_allow_html=True)
    row1,row2=st.columns(2)
    with row1:
        if st.button("Bo'sh joy", key="space_button"):
            st.session_state.result += " "
    with row2:
        if st.button("Tozalash", key="clear_button"):
            st.session_state.result = ""
    st.markdown("</div>", unsafe_allow_html=True)

    st.text_area("💬 Matn kiriting yoki yuqoridagi Brayl klaviaturasidan foydalaning", value=st.session_state.result, key="result", height=100)

    if st.button("🎧 Tovushga aylantirish", disabled=not st.session_state.result.strip()):
        with st.spinner("Jarayon boshlandi. Iltimos, kuting..."):
            audio_content = asyncio.run(text_to_speech(st.session_state.result, "uz"))
            
            if audio_content:
                st.success("✅ Matn muvaffaqiyatli tovushga aylandi!")
                st.toast('Ajoyib!', icon='🎉')
                time.sleep(.5)
                st.audio(audio_content, format='audio/wav', autoplay=True)
            else:
                st.warning("⚠️ Server bilan muammo yuz berdi. Qayta urinib ko'ring.")

if __name__ == '__main__':
    app()
