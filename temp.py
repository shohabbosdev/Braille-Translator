# import pandas as pd

# tabel = pd.DataFrame({"Columns1":[1, 2, 3, 4, 5, 6, 7], "Columns2": [11, 12, 13, 14, 15, 16, 17]})

# st.title("Bu streamlit yordamida ishlanadigan 1-darsimiz")
# st.subheader("Subheader qismi mavjud")
# st.header("Header qismimiz shu yerda yozilgan")
# st.text("Oddiy matnlarni ushbu maydonga yozishingiz mumkin bo'ladi. Bunda siz yozgan matn oddiy holatga keladi.")

# st.markdown("""
# <style>
# .css stApp stAppEmbeddingId-sdm71h8amnqk st-emotion-cache-1r4qj8v erw9t6i1
#             {
#             visibility: hidden
#             }
# </style>
# """, unsafe_allow_html=True)
# st.markdown("**Bu qalin** holatda yozilgan matn")
# st.markdown('*Bu kursiv* tarzda yozilgan matn')
# st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
# st.latex(r"\int_a^b f(x) dx")
# st.json({"raqamlar":"0,1,2,3,4,5,6,7,8,9", "sonlar":"1,2,3,4,5,6,7,8 n", "juft sonlar":"2, 4, 6, 8, 10,  ,2n"})
# st.markdown("---")
# dastur_kodi="""
# #Factorialni hisoblash dasturi
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))
# # Natija 120 chiqadi
# """
# st.code(dastur_kodi, language="python")
# st.metric(label='Shamol tezligi', value='120ms⁻¹', delta='-1.4ms⁻¹')
# st.table(tabel)
# st.image('src/image1.png', caption='Bu lacore uchun tayyorlangan setifikat')
# st.audio("src/Ulug'bek Rahmatullayev - Men Seni Sevaman (Parvona.com).mp3", format='audio/mp3')
# st.video("src/Custom Braille Lables Instructional Video.mp4", format='video/mp4')

# rozilik=st.checkbox("Siz shartnomaning barcha shartlariga rozimisiz?")
# radio_btn = st.radio("Jinsingizni tanlang", options=("Erkak", "Ayol", "Aniqlanmagan"))

# def clicked():
#     st.write("Hisoblash tugmasi bosildi")
# btn = st.button("Hisoblash", type='secondary', on_click=clicked)
# select = st.selectbox("Tilni tanlang", options=("O'zbekcha", "English", "Ўзбекча"), placeholder="Tilni tanlamasangiz bo'lmaydi", help="Yordam kerakmi")
# kup_tanlov = st.multiselect("Yoqtirgan mashina rusumini tanlang", options=("BMW", "Audi", "BYD","TESLA"), placeholder='Aniq tanlang', help="Ko'p tanlov qilish imkoniyati")
# st.write(kup_tanlov)

# st.title("Fayl yuklash")
# st.markdown("---")
# rasm = st.file_uploader("Iltimos biror fayl tanlang", type=["png","jpg"])
# if rasm is not None:
#     st.image(rasm, caption='Dastlabki yuklangan rasm', width=500)
# else:
#     st.write("> Hozircha rasm yuklangani yo'q")

# age = st.slider("Bu slider", 1.0, 100.0, 4.0, 1.0)
# st.write(f"Yoshingiz {int(age)} da va siz {int(2024-age)}-yil tug'ilgansiz")

# course_name = st.text_input("Kurs nomini kiriting", max_chars=60, placeholder='Algoritmlar va berilganlar strukturasi', help="Iltimos o'zingiz o'qiyotgan kurs nomini kiriting")
# st.write(f"Siz o'qiyotgan kurs nomi: **{course_name}**")

# date_entry = st.date_input("Kursni qachondan boshlamoqchisiz?", help='Bu qismda kurslar Sentabr oyidan boshlanadi kuzgi semestr, bahorgi semestr martdan boshlanadi', format="DD-MM-YYYY")
# st.write(f"Kursni shu paytda boshlaysizmi?: **{date_entry}**")

# st.write(f"O'zingizga maqbul vaqt: **{time_entry}**")
# import time as ts
# from datetime import time

# def converter(value):
#     m,s,mm=value.split(":")
#     t_s = int(m)*60+int(s)+int(mm)/1000
#     return t_s

# val = st.time_input("Vaqtni o'rnating", value=time(0,0,0))
# if str(val) == "00:00:00":
#     st.write("Vaqtni o'rnating")
# else:
#     sec=converter(str(val))
#     bar=st.progress(0, text='Yuklanish boshlandi')
#     pre = sec/100
#     progres_status = st.empty()
#     for i in range(100):
#         bar.progress(i+1)
#         progres_status.text(f"{i+1}%")
#         ts.sleep(pre)
# st.image('src/logo.png', width=150, use_column_width='never')
# st.markdown("""<h5 align='center'>OʻZBEKISTON RESPUBLIKASI OLIY TA’LIM, FAN VA INNOVATSIYALAR VAZIRLIGI</h5>""",unsafe_allow_html=True)
# st.markdown("""<h5 align='center'>Mirzo Ulugʻbek nomidagi O‘zbekiston Milliy universitetining Jizzax filialida <code>2024-yil 17-18-may</code> kunlari onlayn va oflayn rejimida o‘tkaziladigan Respublika miqyosidagi ilmiy-texnik anjumanida qatnashgan qatnashuvchilarni</h5>""",unsafe_allow_html=True)
# st.markdown("<h3 align='center'><i>Ro'yxatga olish formasi</i></h3>""", unsafe_allow_html=True)
# st.markdown("---")

# with st.form("Birinchi formamiz"):
#     fish = st.text_input("F.I.SH", placeholder="Misol: Egamqulov Bekzod Alibekovich", help='Bu maydonda FISH kiritiladi')
#     maqola = st.text_input("Maqola mavzuingiz", placeholder="Misol: Ma'lumotlar xavfsizligini oshirishda blockchayn texnologiyalarning o'rni",max_chars=20, help="Bu qismda maqola mavzusi lo'nda kiritilishi kerak")
#     shuba = st.selectbox(
#         "Sho'bani tanlang", 
#         options=(
#             "1-sho‘ba. Ta’lim tizimini takomillashtirish: dolzarb tendensiyalar va strategik yo‘nalishlar", 
#             "2-sho‘ba. Biomuhandislik va biotexnologiyalar sohasida innovatsiyalar", 
#             "3-sho‘ba. Raqamli iqtisod va innovatsion axborot-kommunikatsiya texnologiyalarini joriy etishning dolzarb masalalari",
#             "4-sho‘ba. Psixologiya, tabiiy va aniq fanlar sohasida dolzarb tadqiqotla",
#             "5-sho‘ba. Zamonaviy jamiyatda filologiya, tilshunoslik va didaktika",
#             "6-sho‘ba. Zamonaviy gumanitar ta’limning dolzarb muammolar"
#             ), 
#             placeholder="O'z sho'bangizni tanlang", help="O'z sho'bangizni tanlashda qiynalsangiz konferensiya ma'muriyatiga telefon qilishingizi mumkin: https://t.me/UzMU_JF_conf_1_2_3_shuba, https://t.me/UzMU_JF_conf_4_5_6_shuba")
#     col1,col2=st.columns(2)
#     email = col1.text_input("Email manzilingizni kiriting", placeholder="Misol: sayyod33@inbox.ru", help="Elektron manzil barchangizda bo'ladi degan umiddaman")
#     phone = col2.text_input("Phone", placeholder="+998912345678", help="Telefon raqamni kiriting")
#     rozilik=st.checkbox("Yuqoridagi barcha ma'lumotlar to'g'ri va aniq ekanligini tasdiqlaysizmi?")
#     taqsdiqlash = st.form_submit_button("Tasdiqlash", type='primary')
#     if rozilik and taqsdiqlash:
#         if fish =="" or email == "" or maqola == "":
#             st.warning("Iltimos maydonlar bo'sh bo'lmasligiga e'tibor bering!!")
#         else:
#             st.success("Ma'lumotlar muvaffaqiyatli saqlandi")
#     elif taqsdiqlash and not rozilik:
#         st.error("Siz ma'lumotlaringiz to'g'ri ekanlgini tasdqilashingiz kerak!!")