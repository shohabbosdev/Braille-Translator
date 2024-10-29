import streamlit as st
import requests
import asyncio
import aiohttp
from latin_cyrillic_symbols import to_cyrillic


# API tokeni va URL’ni himoyalangan holatda olish
api_key = st.secrets["API_TOKEN"]
API_URL = st.secrets["API_URL"]

# Braille klaviatura tugmalari uchun CSS uslublar
def get_button_style(color="red", hover_color="red", active_color="aqua"):
    return f"""
    <style>
        .braille-button {{
            color: {color};
            border-radius: 10px;
            font-size: 1em;  /* Keeps font size consistent */
            border: 1px solid green;
            background-color: transparent;
            padding: 10px 15px;
            cursor: pointer;
            margin: 5px;
            transition: background-color 0.3s ease, color 0.3s ease;
            flex: 0 1 calc(25% - 10px); /* Allowing 4 buttons per row */
            box-sizing: border-box; /* Ensures padding is included in width */
        }}
        .braille-button:hover {{
            background-color: {hover_color};
            color: white;
        }}
        .braille-button:active {{
            background-color: {active_color};
            color: white;
        }}

        /* Responsive and mobile styles */
        .braille-buttons-container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-start; /* Align buttons to the left */
            gap: 5px;
            max-width: 640px; /* Set a max width for the container */
            margin: 0 auto; /* Center the container */
        }}
        @media (max-width: 600px) {{
            .braille-button {{
                font-size: 0.9em;
                padding: 8px 12px;
                flex: 0 1 calc(50% - 10px); /* Allowing 2 buttons per row on small screens */
            }}
        }}
    </style>
    """


# Braille harf va raqamlarni yaratish
def create_braille_alphabet():
    return {
        'a': '⠁', 'b': '⠃', 'd': '⠙', 'e': '⠑',
        'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊',
        'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍',
        'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠽',
        'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥',
        'v': '⠺', 'x': '⠹', 'y': '⠯', 'z': '⠵',
        'ch': '⠟', 'sh': '⠱', "o'": '⠧', "g'": '⠻'
    }

def create_braille_numbers():
    return {
        '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
        '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊'
    }

def app():
    # Braille matnini kiritish uchun sessiya holatini o'rnatish
    if 'result' not in st.session_state:
        st.session_state.result = ""

    # Matnni tovushga aylantirish funksiyasi
    async def text_to_speech(text, language="uz"):
        try:
            # Matnni Kirill alifbosiga o‘tkazish
            text = text if any('\u0400' <= char <= '\u04FF' for char in text) else to_cyrillic(text)
            
            # API so‘rovi
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {"inputs": text}
            async with aiohttp.ClientSession() as session:
                async with session.post(API_URL, headers=headers, json=payload) as response:
                    if response.status == 200:
                        return response.status, text, await response.read()
                    return response.status, text, None
        except Exception as e:
            st.error(f"❌ Matnni tovushga aylantirishda xatolik yuz berdi: {e}")
            return None, None, None

    # CSS uslublarni qo'shish
    st.markdown(get_button_style(), unsafe_allow_html=True)

    # Braille klaviaturasini yaratish
    st.markdown("<h2 style='text-align:center; color:red;'>Brayl harflari</h2>", unsafe_allow_html=True)
    alphabet = create_braille_alphabet()
    cols = st.columns(6)
    for i, (letter, symbol) in enumerate(alphabet.items()):
        with cols[i % 6]:
            if st.button(symbol, key=f"btn_{letter}", help=letter):
                st.session_state.result += letter

    st.markdown("<h2 style='text-align:center; color:#116466;'>Brayl raqamlari</h2>", unsafe_allow_html=True)
    numbers = create_braille_numbers()
    num_cols = st.columns(5)
    for i, (number, symbol) in enumerate(numbers.items()):
        with num_cols[i % 5]:
            if st.button(symbol, key=f"num_btn_{number}", help=number):
                st.session_state.result += number

    # "Bo'sh joy" va "Tozalash" tugmalari
    if st.button("Bo'sh joy", key="space_button", use_container_width=True, type='primary', icon='👉'):
        st.session_state.result += " "
    if st.button("Tozalash", key="clear_button", use_container_width=True, type='secondary', icon='🆑'):
        st.session_state.result = ""

    # Natijani ko'rsatish
    st.text_area("💬 Matn kiriting yoki yuqoridagi Brayl klaviaturasidan foydalaning", value=st.session_state.result, key="result", height=100)

    # Tovushga aylantirish tugmasi
    if st.button("🎧 Tovushga aylantirish", disabled=not st.session_state.result.strip()):
        with st.spinner("Jarayon boshlandi. Iltimos, kuting..."):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            status_code, processed_text, audio_content = loop.run_until_complete(text_to_speech(st.session_state.result, "uz"))
            loop.close()
            
            if status_code == 200 and audio_content:
                st.success("✅ Matn muvaffaqiyatli tovushga aylandi!")
                st.audio(audio_content, format='audio/wav', autoplay=True)
            else:
                st.warning("⚠️ Server bilan muammo yuz berdi. Qayta urinib ko'ring.")

if __name__ == '__main__':
    app()