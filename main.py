# main.py
import streamlit as st
from streamlit_option_menu import option_menu

# Sahifa sozlamalari
st.set_page_config(
    page_title="Brayl Tarjimon",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

from src.menus import tekshirgich, generatsiya, tarjima, statistika, account, brayl

class Multiapp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        # Agar authenticated bo'lmasa, faqat "Hisob qaydnomasi" ko'rsatiladi
        if not st.session_state.get('is_authenticated', False):
            options = ["Hisob qaydnomasi"]
            icons = ['person-bounding-box']
        else:
            options = ["Hisob qaydnomasi", "Braylcha yozish", "Brayl tarjimon", "Matn tekshiruvi", "Nutqqa generatsiya", "Statistika"]
            icons = ['person-bounding-box', 'pencil-square', 'translate', 'check2-square', 'earbuds', 'graph-up-arrow']

        with st.sidebar:
            app = option_menu(
                menu_title="Brayl",
                options=options,
                icons=icons,
                menu_icon='gem',
                default_index=0,
                styles={
                    "container": {
                        "padding": "2px !important",
                        "background-color": '#003135',
                        "border-radius": "8px",
                        "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.15)",
                        "margin": "3px 0px",
                        "backdrop-filter": "blur(10px)",
                        "border": "1px solid rgba(255, 255, 255, 0.1)"
                    },
                    "icon": {
                        "color": "white", 
                        "font-size": "17px",
                        "margin-right": "4px",
                        "transition": "all 0.3s ease",
                        "opacity": "0.9",
                        "&:hover": {
                            "transform": "scale(1.1) rotate(5deg)",
                            "opacity": "1"
                        }
                    },
                    "nav-link": {
                        "color": "rgba(255, 255, 255, 0.85)",
                        "font-size": "16px", 
                        "text-align": "left", 
                        "margin": "1px 0px",
                        "padding": "7px 10px",
                        "border-radius": "6px",
                        "transition": "all 0.2s ease-in-out",
                        "--hover-color": "#0a21c0",
                        "letter-spacing": "0.3px",
                        "backdrop-filter": "blur(5px)",
                        "&:hover": {
                            "background-color": "rgba(255, 255, 255, 0.08)",
                            "transform": "translateX(3px)",
                            "color": "white",
                            "letter-spacing": "0.5px",
                            "box-shadow": "0 2px 8px rgba(0, 0, 0, 0.12)"
                        }
                    },
                    "nav-link-selected": {
                        "background-color": "#0fa4af",
                        "border-radius": "6px",
                        "box-shadow": "0 2px 8px rgba(15, 164, 175, 0.3)",
                        "border-left": "2px solid rgba(255, 255, 255, 0.8)",
                        "color": "white",
                        "font-weight": "500",
                        "backdrop-filter": "blur(8px)",
                        "transform": "translateX(2px)"
                    }
                }
            )

        # Ilovalarni ishga tushirish
        if app == "Hisob qaydnomasi":
            account.app()
        elif st.session_state.get('is_authenticated', False):
            if app == "Braylcha yozish":
                brayl.app()
            elif app == "Brayl tarjimon":
                tarjima.app()    
            elif app == "Matn tekshiruvi":
                tekshirgich.app()        
            elif app == "Nutqqa generatsiya":
                generatsiya.app() 
            elif app == "Statistika":
                statistika.app()
        else:
            st.warning("Iltimos, avval tizimga kiring!")

app = Multiapp()
app.run()
