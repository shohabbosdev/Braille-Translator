import streamlit as st
import asyncio
import aiohttp
from latin_cyrillic_symbols import to_cyrillic

# API tokeni va URL'ni himoyalangan holda olish
api_key = st.secrets["API_TOKEN"]
API_URL = st.secrets["API_URL"]

# CSS uslublarni qaytaruvchi funksiyalar
def get_button_style(color="black", hover_color="#ff6f61", active_color="#4CAF50"):
    return f"""
    <style>
        .braille-button {{
            color: {color};
            border-radius: 15px;
            font-size: 1.1em;
            border: 1px solid #4CAF50;
            background-color: transparent;
            padding: 12px 16px;
            cursor: pointer;
            margin: 4px;
            transition: background-color 0.3s ease, color 0.3s ease;
            text-align: center;
        }}
        .braille-button:hover {{
            background-color: {hover_color};
            color: white;
        }}
        .braille-button:active {{
            background-color: {active_color};
            color: white;
        }}

        /* "Bo'sh joy" va "Tozalash" tugmalari uchun dizayn */
        .control-buttons {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }}
        .control-button {{
            color: white;
            background-color: #007BFF;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1em;
            transition: background-color 0.3s ease;
        }}
        .control-button:hover {{
            background-color: #0056b3;
        }}
    </style>
    """

# Braille belgilarini yaratish
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

# Matnni tovushga aylantirish funksiyasi
async def text_to_speech(text, language="uz"):
    try:
        text = text if any('\u0400' <= char <= '\u04FF' for char in text) else to_cyrillic(text)
        
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"inputs": text}
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, headers=headers, json=payload) as response:
                if response.status == 200:
                    return await response.read()
    except Exception as e:
        st.error(f"❌ Xatolik: {e}")
        return None

# Braille interfeysining asosiy qismi
def app():
    st.markdown(get_button_style(), unsafe_allow_html=True)
    st.markdown("# ✅ :rainbow[Brayl klaviaturasi]")

    # Braille harflarini ko'rsatish
    st.markdown("## 🔑 :red[Brayl Harflari]")
    alphabet = create_braille_symbols("alphabet")
    ustunlar_soni = [5,6]
    # Harflarni 5 ustunli qatorlarda ko'rsatish va `help` orqali ko'rsatish
    cols = st.columns(ustunlar_soni[1])
    for i, (letter, symbol) in enumerate(alphabet.items()):
        col = cols[i % ustunlar_soni[1]]  # Har bir qator uchun 5 ta ustun
        with col:
            st.button(symbol, key=f"btn_{letter}", help=f"{letter}", on_click=lambda l=letter: st.session_state.update(result=st.session_state.result + l))

    # Braille raqamlarini ko'rsatish
    st.markdown("## 📌 :green[Brayl Raqamlari]")
    numbers = create_braille_symbols("numbers")
    
    with st.sidebar:
        st.divider()
        st.image('src/image.png', width=150)
        st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")
    # Raqamlarni 5 ustunli qatorlarda ko'rsatish va `help` orqali ko'rsatish
    num_cols = st.columns(ustunlar_soni[0])
    for i, (number, symbol) in enumerate(numbers.items()):
        col = num_cols[i % ustunlar_soni[0]]
        with col:
            st.button(symbol, key=f"num_btn_{number}", help=f"{number}", on_click=lambda n=number: st.session_state.update(result=st.session_state.result + n))

    # "Bo'sh joy" va "Tozalash" tugmalari uchun maxsus qator
    st.markdown("<div class='control-buttons'>", unsafe_allow_html=True)
    row1,row2=st.columns(2)
    with row1:
        if st.button("Bo'sh joy", key="space_button", use_container_width=True, type='primary', icon='🗳'):
            st.session_state.result += " "
    with row2:
        if st.button("Tozalash", key="clear_button", use_container_width=True, type='primary', icon='🖇'):
            st.session_state.result = ""
    st.markdown("</div>", unsafe_allow_html=True)

    # Matn maydoni va tovushga aylantirish tugmasi
    st.text_area("💬 Matn kiriting yoki yuqoridagi Brayl klaviaturasidan foydalaning", value=st.session_state.result, key="result", height=100)

    if st.button("🎧 Tovushga aylantirish", disabled=not st.session_state.result.strip()):
        with st.spinner("Jarayon boshlandi. Iltimos, kuting..."):
            audio_content = asyncio.run(text_to_speech(st.session_state.result, "uz"))
            
            if audio_content:
                st.success("✅ Matn muvaffaqiyatli tovushga aylandi!")
                st.audio(audio_content, format='audio/wav', autoplay=True)
            else:
                st.warning("⚠️ Server bilan muammo yuz berdi. Qayta urinib ko'ring.")

# Session state uchun boshlang‘ich qiymatni o‘rnatish
if 'result' not in st.session_state:
    st.session_state.result = ""

# Dastur funksiyasini chaqirish
if __name__ == '__main__':
    app()
