import streamlit as st
from streamlit_option_menu import option_menu

# Sahifa sozlamalari
st.set_page_config(
    page_title="Brayl Tarjimon",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
from src.menus import tekshirgich, generatsiya, home, tarjima, statistika
class Multiapp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Brayl",
                options=["Bosh sahifa","Brayl tarjimon","Matn tekshiruvi","Nutqqa generatsiya", "Statistika"],
                icons=['house-up-fill','translate','check2-square','earbuds', 'graph-up-arrow'],
                menu_icon='gem',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'#003135'},
                    "icon": {"color": "white", "font-size": "18px"}, 
                    "nav-link": {"color":"white","font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#0a21c0"},
                    "nav-link-selected": {"background-color": "#0fa4af"},}
            )
        if app == "Bosh sahifa":
            home.app()
        if app == "Brayl tarjimon":
            tarjima.app()    
        if app == "Matn tekshiruvi":
            tekshirgich.app()        
        if app == 'Nutqqa generatsiya':
            generatsiya.app() 
        if app == "Statistika":
            statistika.app() 

    run()