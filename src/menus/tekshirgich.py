import streamlit as st
from streamlit_elements import nivo, mui, elements
from transformers import pipeline
@st.cache_resource
def load_model():
    return pipeline('fill-mask', model='tahrirchi/tahrirchi-bert-small')

unmasker = load_model()

def display_header():
    st.markdown("# ✅ :rainbow[Matnlar tekshirgichi]")

def process_text(matn, masklangan_soz):
    return matn.replace(masklangan_soz, "<mask>")

def truncate_text(text, length=10):
    return text if len(text) <= length else text[:length] + "..."

def display_results(masklangan_matn):
    with st.spinner("Natijalar yuklanmoqda..."):
        tab1, tab2 = st.tabs(["1\.✏️ :orange[Matnli natijalar]", "2\. 📊 Diagrammali natijalar"])
        with tab1:
            results = unmasker(masklangan_matn)
            
            st.markdown("<h6 style='text-align: center;'>Natijalar</h6>", unsafe_allow_html=True)
            data = []
            for result in results:
                token_str = result['token_str']
                aniqlik = result['score'] * 100
                data.append({
                    "id": truncate_text(token_str),
                    "value": round(aniqlik, 2),
                    "label": f"{truncate_text(token_str)}: {aniqlik:.2f}%"
                })

                rangli_natija = masklangan_matn.replace(
                    "<mask>", f"<span style='color: #ba5733;'>{token_str}</span>"
                )
                
                # Natijani individual kartochka sifatida ko'rsatish
                st.markdown(f"""
                <div style="border-radius: 5px; padding: 5px; background-color: #aaf0f0; margin-bottom: 5px;">
                    <h4 style="color: #333;">💬 {rangli_natija}</h4>
                    <h6 style='color: red;'><strong>Aniqlik:</strong> {aniqlik:.2f}%</h6>
                </div>
                """, unsafe_allow_html=True)
        with tab2:
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
                colors={"scheme":'paired'},
                sortByValue=True,
                cornerRadius=3,
                activeOuterRadiusOffset=8,
                borderWidth=1,
                arcLinkLabelsSkipAngle=10,
                arcLinkLabelsTextColor="#f33333",
                arcLinkLabelsThickness=2,
                arcLabelsSkipAngle=10,
                motionConfig="wobbly",
                arcLabelsTextColor=[{"from": 'color',"modifiers": [["darker", 2]]}],
                borderColor=[{"from": 'color',"modifiers": [["darker", 0.2]]}],
                defs=[{ "id": 'dots', "type": 'patternDots', "background": 'inherit',"color": 'rgba(255, 255, 255, 0.4)', "size": 4, "padding": 1,"stagger": True }],
                legends=[ {
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
                        "effects": [ { "on": 'hover', "style": {"itemTextColor": '#000'}}]
                    }
                ],
                fill=[{ "match": { "id": 'react' }, "id": 'dots' }],
                enableArcLinkLabels=False
            )

def app():
    display_header()
    default_text = "Egiluvchan bo‘g‘inlari va yarim bukilgan tirnoqlari tik qiyaliklar hamda daraxtlarga oson chiqish imkonini beradi."
    matn = st.text_area("Matn kiriting", value=default_text, placeholder="Matnni kiriting...")
    masklangan_soz = st.selectbox("Mask qilmoqchi bo'lgan so'zni tanlang", matn.split())

    with st.form("text_form"):
        bajarish = st.form_submit_button(":green[Bajarish]", icon="♻️")
        if bajarish:
            masklangan_matn = process_text(matn, masklangan_soz)
            if "<mask>" in masklangan_matn:
                display_results(masklangan_matn)
            else:
                st.warning("Iltimos, matndan biror so'zni tanlang.")
    with st.sidebar:
        st.image('src/image.png', width=150)
        st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")

if __name__ == "__main__":
    app()
