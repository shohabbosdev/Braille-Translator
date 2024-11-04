import streamlit as st
from streamlit_elements import nivo, mui, elements
from transformers import pipeline

# Logotip joylashtirish
st.sidebar.image("src/logo.jpg", caption="shohabbosdev", width=150)

# Modelni yuklash va kechlashtirish
@st.cache_resource
def load_model():
    return pipeline('fill-mask', model='tahrirchi/tahrirchi-bert-small')

unmasker = load_model()

def display_header():
    st.markdown("<h1 style='text-align: center;'>✅ Matnlar tekshirgichi</h1>", unsafe_allow_html=True)

def process_text(matn, masklangan_soz):
    return matn.replace(masklangan_soz, "<mask>")

def truncate_text(text, length=10):
    # Matnni belgilangan uzunlikka qisqartirish
    return text if len(text) <= length else text[:length] + "..."

def display_results(masklangan_matn):
    results = unmasker(masklangan_matn)
    st.markdown("<h3 style='text-align: center;'>Natijalar</h3>", unsafe_allow_html=True)
    
    data = []  # Aniqlangan so'z va foiz qiymatlarni saqlash uchun ro'yxat
    
    for result in results:
        token_str = result['token_str']
        aniqlik = result['score'] * 100
        data.append({
            "id": truncate_text(token_str),  # Legendda qisqartirilgan matn
            "value": round(aniqlik, 2),
            "label": f"{truncate_text(token_str)}: {aniqlik:.2f}%"  # Legendda foiz formati bilan ko'rsatish
        })
    
        # Rangli natijalarni ko'rsatish
        rangli_natija = masklangan_matn.replace(
            "<mask>", f"<span style='color: #ff5733; font-weight: bold;'>{token_str}</span>"
        )
        
        # Natija va aniqlikni ko'rsatish
        st.markdown(f"💬 {rangli_natija}", unsafe_allow_html=True)
        st.metric("Aniqlik", f"{aniqlik:.2f}%")

    # Nivo grafikni ko'rsatish
    show_nivo_chart(data)
    
def show_nivo_chart(data):
    with elements("nivo_charts"):  
        with mui.Box(sx={"height": 500, "width": 700}):  
            nivo.Pie(  
                data=data,  
                width=800,  
                height=500,  
                margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                innerRadius=0.5,
                pixelRatio=4,
                padAngle=0.7,
                cornerRadius=3,
                activeOuterRadiusOffset=8,
                borderWidth=1,
                arcLinkLabelsSkipAngle=10,
                arcLinkLabelsTextColor="#f33333",
                arcLinkLabelsThickness=2,
                arcLabelsSkipAngle=10,
                motionConfig="wobbly",
                arcLabelsTextColor=[{
                    "from": 'color',
                    "modifiers": [["darker", 2]]
                }],
                borderColor=[{
                    "from": 'color',
                    "modifiers": [["darker", 0.2]]
                }],
                defs=[  
                    {  
                        "id": 'dots',  
                        "type": 'patternDots',  
                        "background": 'inherit',  
                        "color": 'rgba(255, 255, 255, 0.4)',  
                        "size": 4,  
                        "padding": 1,  
                        "stagger": True  
                    }  
                ],
                legends=[
                    {
                        "anchor": 'right',  
                        "direction": 'column',  
                        "justify": False,
                        "translateX": 120,
                        "translateY": 0,
                        "itemsSpacing": 0,
                        "itemWidth": 150,
                        "itemHeight": 45,
                        "itemTextColor": '#999',
                        "itemDirection": 'left-to-right',
                        "itemOpacity": 1,
                        "symbolSize": 18,
                        "symbolShape": 'circle',
                        "effects": [
                            {
                                "on": 'hover',
                                "style": {
                                    "itemTextColor": '#000'
                                }
                            }
                        ]
                    }
                ],
                fill=[{ "match": { "id": 'react' }, "id": 'dots' }],
                enableArcLinkLabels=False
            )

def app():
    display_header()

    # Foydalanuvchi kiritgan matn
    default_text = "Egiluvchan bo‘g‘inlari va yarim bukilgan tirnoqlari tik qiyaliklar hamda daraxtlarga oson chiqish imkonini beradi."
    matn = st.text_area("Matn kiriting", value=default_text, placeholder="Matnni kiriting...")

    # Matnni so'zlar bo'yicha ajratish
    sozlar = matn.split()
    
    # So'zlar orasidan tanlash uchun selectbox
    masklangan_soz = st.selectbox("Mask qilmoqchi bo'lgan so'zni tanlang", sozlar)

    # Natijalarni chiqarish formasi
    with st.form("text_form"):
        bajarish = st.form_submit_button("Bajarish")
        if bajarish:
            masklangan_matn = process_text(matn, masklangan_soz)
            if "<mask>" in masklangan_matn:
                display_results(masklangan_matn)
            else:
                st.warning("Iltimos, matndan biror so'zni tanlang.")
    
    # Sidebarda qo'shimcha ma'lumotlar
    st.sidebar.markdown("### 👁 O'zbekcha Brayl tarjimon")
    st.sidebar.markdown("[ Men bilan bog'lanish ](https://t.me/shohabbosdev) 💻", unsafe_allow_html=True)

if __name__ == "__main__":
    app()
