import streamlit as st
from braille_symbols import BrailleConverter 
from annotated_text import annotated_text
def app():
    # Braille converter obyekti
    st.markdown("# 🏘 :rainbow[Brayl alifbosidan o'zbek alifbosiga yoki aksincha o'tkazish]")
    st.markdown('''
    > :rainbow[Brayl shrifti]- boʻrtma nuqtalardan iborat shrift. Koʻzi ojizlar oʻqish va yozishi uchun moʻljallangan. [Luis Brayl](https://www.labarandilla.org/wp-content/uploads/2018/01/luis-braille.jpg) tomonidan yaratilgan. Brayl shrifti asosida :red[6] nuqtani turli vaziyatda uygʻunlashtirish yotadi. Ixtirochi :blue-background[lotin alifbosidagi harflar] tartibini qabul qilgan. Alifboning oldingi harflarini belgilash uchun :red[6] nuqtaning yuqori va oʻrta nuqtalaridan foydalanilgan. Keyingi harflarni belgilash uchun qoʻsh nuqtalar chapdan, soʻng chap va oʻngdan, undan keyin oʻngdan qoʻshilgan. Mazkur belgilar bilan oʻzbekkirill va oʻzbeklotin harflari ham ifodalangan. :red[6] nuqtaning turli holatdagi uygʻunlashuvidan sonlar, tinish belgilari, matematika, kimyo va nota belgilarini ham ifodalash [mumkin.](https://uz.wikipedia.org/wiki/Brayl_yozuvi)''')
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
            st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")
            st.divider()
            tanlov = st.radio("Tarjima turini tanlang", options=("Matndan Braylga", "Brayldan matnga"))
            st.markdown('[shohabbosdev](https://github.com/shohabbosdev)')    


        with st.expander("Brayl alifbosini ko'rish ⬇️"):
            st.image('src/alifbo.png', caption="Brayl alifbosi")
        
        # Har ikki bo‘limda `text` o'zgaruvchisini alohida aniqlash
        if tanlov == "Matndan Braylga":
            st.markdown(":rainbow[Matndan Brayl yozuviga o'tkazish]")
            with st.popover("Matn kiritish uchun ushbu tugmani bosing"):
                st.markdown("### 👋 :green[Brayl yozuviga o'tkazadigan matnni kiriting ]")
                text = st.text_input("Ma'lumot yozishni boshlang?", key="matn_to_braille")

            if text:  # Faqat text mavjud bo'lganda bajariladi
                braille_text = convertor.convert_chars_to_braille(text)
                wrapped_braille = '<div>'
                for i in range(0, len(braille_text), 35): 
                    line = braille_text[i:i+35]
                    colored_line = ''.join([f'<span style="color: red; font-size: 24pt">{char}</span>' if char != ' ' else char for char in line])
                    wrapped_braille += colored_line + '<br>'
                wrapped_braille += '</div>'
                resultRow1, resultRow2 = st.columns([1,4])
                resultRow1.markdown(f"👇:rainbow[Siz yozgan dastlabki matn:]\n :blue-background[{text.capitalize()}]")
                resultRow2.markdown(f"👇:rainbow[Tarjima matn]{wrapped_braille}", unsafe_allow_html=True)

        else:
            st.markdown(":rainbow[Brayl matndan oddiy matnga o'tkazish]")
            with st.popover("Matn kiritish uchun ushbu tugmani bosing"):
                st.markdown("### 👋 :blue[⠨⠃⠗⠁⠯⠇⠀⠍⠁⠞⠝⠊⠝⠊⠀⠅⠊⠗⠊⠞⠊⠝⠛⠲⠲⠲]")
                text = st.text_input("Ma'lumot yozishni boshlang?", key="braille_to_text")
            
            if text:  # Bu shart `Brayldan matnga` uchun ishlaydi
                sample_text = convertor.convert_braille_to_chars(text)
                wrapped_braille = '<div style="width: 100%; word-wrap: break-word;">'
                for i in range(0, len(sample_text), 70):  
                    line = sample_text[i:i+70]
                    colored_line = ''.join([f'<span style="color: #0fad47; font-size: 20pt">{char}</span>' if char != ' ' else char for char in line])
                    wrapped_braille += colored_line + '<br>'
                wrapped_braille += '</div>'
                result1Row1, result1Row2 = st.columns(2)
                result1Row1.markdown(f"👇:rainbow[Siz yozgan Brayl matn:]\n :blue-background[{text.capitalize()}]")
                result1Row2.markdown(f"👇:rainbow[Tarjima matn]{wrapped_braille}", unsafe_allow_html=True)

    hisoblash()
