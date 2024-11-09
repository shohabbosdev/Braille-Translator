import streamlit as st
import pandas as pd
from collections import defaultdict
from organization import organizations

def app():
    grouped_organizations = defaultdict(list)
    for org in organizations:
        province = org['provincial']
        grouped_organizations[province].append(org)
    
    st.markdown("## ✅ :rainbow[Statistika ma'lumotlari]")
    st.write(f"Umumiy tashkilotlar soni: <code>{len(organizations)}</code> ta",unsafe_allow_html=True)

    selected_province = st.selectbox("Ko'zi ojizlar jamiyati korxonalari", options=list(grouped_organizations.keys()))
    
    tab1, tab2 = st.tabs(['📗 :green[Jadval]','📊 :blue[Diagramma]'])
    with tab1:
        selected_orgs = grouped_organizations[selected_province]
        data = {
            "Manzil": [org['address'] for org in selected_orgs],
            "Bog'lanish raqami": [", ".join(org['phone']) for org in selected_orgs]
        }
        df = pd.DataFrame(data, index=[i for i in range(1,len(selected_orgs)+1)])
        st.markdown(f"<h6 style='text-align: center; color: #2f2;'>{selected_province} jadvali</h6>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.write(len(selected_orgs))
    with tab2:
        st.markdown("<h6 style='text-align: center; color: aqua;'>Jamiyatning soha diagrammasi</h6>", unsafe_allow_html=True)
        province_data = {
            "province_names": list(grouped_organizations.keys()),
            "counts": [len(orgs) for orgs in grouped_organizations.values()]
        }
        province_df = pd.DataFrame(province_data)
        
        st.area_chart(province_df.set_index('province_names'), x_label="Viloyatlar", y_label="Soni", color='#4685e3', stack=True)
        st.markdown("<h6 style='text-align: center; color: red;'>Jamiyatning scatter diagrammasi</h6>", unsafe_allow_html=True)
        st.scatter_chart(province_df.set_index('province_names'), x_label="Viloyatlar", y_label="Soni", color='#ff85e3')
        
        st.write(f"Jamiyat joylashuvi: {selected_province}: {len(selected_orgs)}")
    
    with st.sidebar:
        st.image('src/image.png', width=150)
        st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")

if __name__ == "__main__":
    app()
