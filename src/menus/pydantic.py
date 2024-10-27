import streamlit as st

def get_button_style(color="red", hover_color="red", active_color="aqua"):
    return f"""
    <style>
        .braille-button {{
            color: {color};
            border-radius: 10px;
            font-size: 40px;
            border: 1px solid green;
            background-color: transparent;
            transition: background-color 0.3s, color 0.3s;
            padding: 5px 15px;
            cursor: pointer;
            margin: 5px;
        }}
        .braille-button:hover {{
            background-color: {hover_color};
            color: white;
        }}
        .braille-button:active {{
            background-color: {active_color};
            color: white;
        }}
    </style>
    """

def init_session_state():
    if 'result' not in st.session_state:
        st.session_state.result = ""

def create_braille_alphabet():
    alphabet = {
        'a': '⠁', 'b': '⠃', 'd': '⠙', 'e': '⠑',
        'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊',
        'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍',
        'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠽',
        'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥',
        'v': '⠺', 'x': '⠹', 'y': '⠯', 'z': '⠵',
        'ch': '⠟', 'sh': '⠱', "o'": '⠧', "g'": '⠻'
    }
    return alphabet

def create_braille_numbers():
    numbers = {
        '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙',
        '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊'
    }
    return numbers

def app():
    init_session_state()
    
    st.title("Brayl alifbosi")
    
    # Add custom styles for buttons
    st.markdown(get_button_style(), unsafe_allow_html=True)
    
    # Alphabet Section
    st.markdown("<h2 style='text-align:center; color:red;'>Brayl alifbosi</h2>", unsafe_allow_html=True)
    
    alphabet = create_braille_alphabet()
    cols = st.columns(7)
    
    for i, (letter, symbol) in enumerate(alphabet.items()):
        with cols[i % 7]:
            if st.button(symbol, key=f"btn_{letter}", help=f"{letter}"):
                st.session_state.result += letter
    
    # Numbers Section
    st.markdown("<h2 style='text-align:center; color:#116466;'>Brayl raqamlari</h2>", unsafe_allow_html=True)
    
    numbers = create_braille_numbers()
    num_cols = st.columns(5)
    
    for i, (number, symbol) in enumerate(numbers.items()):
        with num_cols[i % 5]:
            if st.button(symbol, key=f"num_btn_{number}", help=f"{number} raqami"):
                st.session_state.result += number
    
    # Space button and Result Section
    if st.button("Bo'sh joy", type='primary', use_container_width=True, icon="🪐"):
        st.session_state.result += " "
    
    # Clear button to reset the text area
    if st.button("Tozalash", type='secondary', use_container_width=True, icon="🆑"):
        st.session_state.result = ""
    
    st.text_input(
        "Natija qismi",
        value=st.session_state.result,
        key="result"
    )

if __name__ == "__main__":
    app()
