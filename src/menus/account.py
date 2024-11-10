# account.py
import streamlit as st
import pyrebase

# Firebase konfiguratsiyasi
firebase_config = {
  'apiKey': st.secrets['apiKey'],
  'authDomain': st.secrets['authDomain'],
  'databaseURL': st.secrets['databaseURL'],
  'projectId': st.secrets['projectId'],
  'storageBucket': st.secrets['storageBucket'],
  'messagingSenderId': st.secrets['messagingSenderId'],
  'appId': st.secrets['appId'],
  'measurementId': st.secrets['measurementId']
}

# Pyrebase orqali autentifikatsiya qilish
firebase = pyrebase.initialize_app(firebase_config)
auth_client = firebase.auth()

def app():
    if 'is_authenticated' not in st.session_state:
        st.session_state.is_authenticated = False
        
    st.title("📚 Salom siz :violet[BTarjimon]dasiz")
    
    choice = st.selectbox("Kirish/Ro'yxatdan o'tish", ['Kirish', "Ro'yxatdan o'tish"])
    
    def sign_in(email, password):
        try:
            # Haqiqiy parolni tekshirish uchun Pyrebase client SDK dan foydalanamiz
            user = auth_client.sign_in_with_email_and_password(email, password)
            st.session_state.is_authenticated = True
            st.session_state.user_email = email
            st.session_state.user_id = user['localId']
            st.markdown(f"Salom :rainbow[{user['localId']}], :rainbow[{user['email']}]")
            st.success("Tizimga muvaffaqiyatli kirdingiz!")
        except:
            st.session_state.is_authenticated = False
            st.error("Email yoki parol noto'g'ri!")
    
    if choice == 'Kirish':
        email = st.text_input('Email manzilingiz')
        password = st.text_input('Parolingiz', type='password')
        
        if st.button(':blue[Kirish]', icon='💡'):
            sign_in(email, password)
            
    elif choice == 'Ro\'yxatdan o\'tish':
        email = st.text_input("Email manzilingiz")
        password = st.text_input('Parolingiz', type='password')
        reEnterpassword = st.text_input('Parolingizni qayta tering', type='password')
        
        if password == reEnterpassword:
            username = st.text_input("O'zingiz uchun takrorlanmas username kiriting")
            if st.button("Hisob qaydnomasini yaratish"):
                try:
                    # Pyrebase orqali yangi foydalanuvchi yaratish
                    user = auth_client.create_user_with_email_and_password(email, password)
                    st.success("Hisob qaydnomasi muvaffaqiyatli yaratildi!")
                    st.markdown("Iltimos Login menyusi orqali hisobingizga kirishingiz mumkin")
                    st.snow()
                except:
                    st.error("Ro'yxatdan o'tishda xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.")
        else:
            st.error("Parollar mos emas, iltimos qayta kiriting!")

    with st.sidebar:
        st.image('src/image.png', width=150)
        st.markdown("👁 :rainbow[O'zbekcha Brayl tarjimon]")

    # Chiqish tugmasi
    if st.session_state.get('is_authenticated', False):
        if st.sidebar.button("Chiqish"):
            # Autentifikatsiya holatini yangilash
            st.session_state.is_authenticated = False
            st.session_state.user_email = None
            st.session_state.user_id = None
            # Sahifani qayta yuklash
            st.session_state.clear()
