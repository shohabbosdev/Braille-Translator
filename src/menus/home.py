import streamlit as st
from braille_symbols import BrailleConverter 
from annotated_text import annotated_text

st.logo(
    "src/logo.jpg",
    link="https://t.me/shohabbosdev"
)
def app():
    # Braille converter obyekti
    convertor = BrailleConverter()
    st.caption("O'zbekcha Brayl alifbosidan foydalanib matnlar bilan ishlash ko'nikmangizni oshiring")

    # Tarjima funksiyalari
    def convert_to_text(braille_text):
        """Braille'dan oddiy matnga o'tkazuvchi funksiya"""
        try:
            text = convertor.convert_braille_to_chars(braille_text)
            return text
        except Exception as e:
            st.error(f"Tarjima vaqtida xatolik yuz berdi: {e}")

    def hisoblash():
        with st.sidebar:
            st.image('src/image.png', width=150)
            st.markdown("<p>👁 O'zbekcha Brayl tarjimon</p>", unsafe_allow_html=True)
            st.divider()
            tanlov = st.radio("Tarjima turini tanlang", options=("Matndan Braylga", "Brayldan matnga"))
            st.link_button("Men bilan bog'lanish", 'https://t.me/shohabbosdev', type='secondary', icon="💻", use_container_width=True)

        with st.expander("Brayl alifbosini ko'rish ⬇️"):
            st.image('src/alifbo.png', caption="Brayl alifbosi")
        
        if tanlov == "Matndan Braylga":
            st.write("Matndan Brayl yozuviga o'tkazish")
            with st.popover("Matn kiritish uchun ushbu tugmani bosing"):
                st.markdown("Brayl yozuviga o'tkazadigan matnni kiriting 👋")
                text = st.text_input("Ma'lumot yozishni boshlang?")

            if text is None:
                st.info("Maydon bo'sh bo'lmasligiga e'tibor bering", icon='🥺')
            else:
                braille_text = convertor.convert_chars_to_braille(text)
                wrapped_braille = '<div>'
                for i in range(0, len(braille_text), 80): 
                    line = braille_text[i:i+80]
                    colored_line = ''.join([f'<span style="color: red; font-size: 40pt">{char}</span>' if char != ' ' else char for char in line])
                    wrapped_braille += colored_line + '<br>'
                wrapped_braille += '</div>'
                st.write(f"<h4>Siz yozgan dastlabki matn:</h4><code>{text.capitalize()}</code>", unsafe_allow_html=True)
                st.write(f"<h4>Tarjima matn: 👇</h4> {wrapped_braille}", unsafe_allow_html=True)

        else:
            st.write("Brayl matndan oddiy matnga o'tkazish")
            with st.popover("Matn kiritish uchun ushbu tugmani bosing"):
                st.markdown("⠨⠃⠗⠁⠯⠇⠀⠍⠁⠞⠝⠊⠝⠊⠀⠅⠊⠗⠊⠞⠊⠝⠛⠲⠲⠲👋")
                text = st.text_input("Ma'lumot yozishni boshlang?")
            if text is None:
                st.info("Maydon bo'sh bo'lmasligiga e'tibor bering", icon='🥺')
            else:
                sample_text  = convertor.convert_braille_to_chars(text)
                wrapped_braille = '<div style="width: 100%; word-wrap: break-word;">'
                for i in range(0, len(sample_text), 80):  
                    line = sample_text [i:i+80]
                    colored_line = ''.join([f'<span style="color: #0fad47; font-size: 20pt">{char}</span>' if char != ' ' else char for char in line])
                    wrapped_braille += colored_line + '<br>'
                wrapped_braille += '</div>'
                st.write(f"<h4>Siz yozgan Brayl matn:</h4><code>{text.capitalize()}</code>", unsafe_allow_html=True)
                
                st.write(f"<code>{annotated_text(
                        "Bu ",
                        ("bo‘ladi", "fe'l"),
                        " bir oz ",
                        ("belgilangan", "sifat"),
                        ("matn", "ot"),
                        " sizlardan ",
                        ("kim", "olmosh"),
                        " bu kabi narsalarni ",
                        ("yoqtiradi", "fe'l"),
                        "."
                    )
                }</code>", unsafe_allow_html=True)
                        
                st.write(f"<h4>Tarjima matn: 👇</h4> {wrapped_braille}", unsafe_allow_html=True)

    # if __name__ == '__main__':
    hisoblash()
