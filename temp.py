# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import CubicSpline
# import math

# #1. Asl funksiyani yasaymi
# def original_functions(x):
#     return x**2+2*x+5

# #2. Ma'lumotlarni tanlaymiz
# x_points = np.array([i for i in range(0,10)])
# y_points = np.array([original_functions(i) for i in range(0,10)])

# #3.Kubik splaynni yaratamiz
# spline_function = CubicSpline(x_points, y_points)

# # 4. Grafik uchun kengaytirilgan x qiymatlari
# x_fine = np.linspace(0, 5, 100)
# # 5. Grafik chizish
# plt.figure(figsize=(14, 8))

# # Asl funksiyani chizish
# plt.plot(x_fine, original_functions(x_fine), 'r-', label='Asl funksiyamiz: $y = x^2 + 2x + 5$')

# # Splayn funksiyasini chizish
# plt.plot(x_fine, spline_function(x_fine), 'b--', label='Kubik splayn interpolyatsiyasi')

# # Splayn uzluksizligini tekshirish uchun birinchi va ikkinchi hosilalarni chizish
# # Birinchi hosila
# plt.plot(x_fine, spline_function(x_fine, 1), 'g-', label="Splayn funksiyadan 1-tartibli hosila")
# # Ikkinchi hosila
# plt.plot(x_fine, spline_function(x_fine, 2), 'm-', label="Splayn funksiya+dan 2-tartibli hosila")

# # Belgilar va jadval
# plt.scatter(x_points, y_points, color='black', label="Ma'lumotlar nuqtalari")
# plt.legend(loc='upper left')
# plt.title("$y = x^2 + 2x + 5$ funksiya uchun Kubik splayn funksiya")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid(True)

# # Grafiklarni ko'rsatish
# plt.show()

# import numpy as np
# from scipy.interpolate import lagrange
# import matplotlib.pyplot as plt

# X = np.array([5, 7, 13, 15, 10, 3])
# Y = np.array([0, 5, 10, 15, 20, 24])

# x=12
# def langranj(item, array1,array2):
#     poly = lagrange(array1,array2)
#     sum=0
#     for i in range(len(array1)-1,-1,-1):
#         sum+=poly[i]*item**i
#     return {
#         "summa":sum,
#         "kuphad":poly
#     }

# plt.xlabel("X data")
# plt.ylabel("Y data")
# plt.title(f"Lagrang ko'phadi: \n\n{langranj(x,X,Y)['kuphad']}\nX={x} bo'lganda yechim: {langranj(x,X,Y)['summa']}")
# plt.plot(X,Y,color='red')
# plt.show() 

# import requests
# import time
# import streamlit as st

# # Hugging Face token

# st.markdown("# :link: :rainbow[STT (Speech to Text)]")
# def query(audio_bytes):
#     headers = {"Authorization": f"Bearer {st.secrets['API_TOKEN']}"}
#     response = requests.post(st.secrets['STTAPI_URL'], headers=headers, data=audio_bytes)
#     return response.json()

# audio_file = st.file_uploader('Audio yuklang (wav yoki ogg formatda)', type=['ogg', 'wav'])
# if audio_file is not None:
#     audio_bytes = audio_file.read()
#     with st.status("Audiodan matnlar aniqlanayabdi..."):
#         output = query(audio_bytes)
#         time.sleep(2)
#         st.write("Aniqlangan matn:")
#         st.markdown(f"## :link: :rainbow[{output['text']}]")

# import requests
# import time
# import streamlit as st

# st.markdown("# :link: :rainbow[STT (Speech to Text)]")
# @st.cache_data()
# def query(file_data):
#     try:
#         headers = {"Authorization": f"Bearer {st.secrets['API_TOKEN']}"}
#         response = requests.post(st.secrets['API_URL_HAND'], headers=headers, data=file_data)
#         if response.status_code == 200:
#             return response.json()
#     except Exception as e:
#         st.warning(f"Xatolik bo'ldi: {e}")
#         return None

# photo_file = st.file_uploader('Rasm yuklang', type=['png','jpg'])
# if photo_file is not None:
#     photo_file_bytes = photo_file.read()
#     st.image(photo_file,caption="Yuklagan rasmingiz")
#     with st.status("Rasmdan matnlar aniqlanayabdi..."):
#         output = query(photo_file_bytes)
#         time.sleep(2)
#         st.write("Aniqlangan matn:")
#         st.markdown(f"## :link: :rainbow[{output[0]['generated_text']}]")


# import streamlit as st
# import requests
# from random import randrange
# import time

# # Kategoriya ro'yxati
# category_lists = [
#     'happiness', 'age', 'alone', 'amazing', 'anger', 'architecture', 'art', 
#     'attitude', 'beauty', 'best', 'birthday', 'business', 'car', 'change', 
#     'communication', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 
#     'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 
#     'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 
#     'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 
#     'government', 'graduation', 'great', 'health', 'history', 'home', 'hope', 
#     'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 
#     'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 
#     'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success'
# ]

# # Tasodifiy kategoriya tanlash
# category = category_lists[randrange(len(category_lists))]

# st.markdown("## :rainbow[Oraliqni hisoblash]")
# st.markdown("### :rainbow[{} qator oraliqini olish uchun API ga xabar berish]".format(category))

# # Tanlangan kategoriyaga oid iqtibos olish funksiyasi
# def select_category(category):
#     api_url = f'{st.secrets['QUOTE_URL']}{category}'
#     response = requests.get(api_url, headers={'X-Api-Key': f"{st.secrets['OCR_QUOTE_API']}"})
#     if response.status_code == 200:
#         quote = response.json()[0]["quote"]
#         author = response.json()[0]["author"]
#         return [quote, author]
#     else:
#         st.error(f"Xatolik: {response.status_code}, {response.text}")

# # Rasmni matnga aylantirish funksiyasi
# def image_to_text(image):
#     files = {'image': image}
#     headers = {'X-Api-Key': f"{st.secrets['OCR_QUOTE_API']}"}
#     try:
#         response = requests.post(st.secrets['OCR_URL'], headers=headers, files=files)
#         if response.status_code == 200:
#             text_results = response.json()
#             if text_results:
#                 extracted_text = " ".join([item["text"] for item in text_results])
#                 return extracted_text
#             else:
#                 return "Hech qanday matn topilmadi."
#         else:
#             return f"Xatolik: {response.status_code}, {response.text}"
#     except Exception as e:
#         return f"Xatolik: {e}"

# # Kategoriya bo'yicha iqtibos olish

# st.markdown(f"> {select_category(category)[0]}\n\n*{select_category(category)[1]}*")

# # Fayl yuklash
# uploaded_image = st.file_uploader("Rasmni yuklang...", type=['jpg', 'png'])

# # Rasm yuklangan yoki yuklanmaganligini tekshirish va vaqtni hisoblash
# if uploaded_image:
#     row1, row2 = st.columns([2, 4])
#     row1.image(uploaded_image, caption="Dastlabki rasm")

#     # Matn ajratish vaqti
#     with st.spinner("Siz yuborgan tasvirdan matnlar ajratib olinayabdi. Iltimos, kuting..."):
#         start_time = time.time()
#         extracted_text = image_to_text(uploaded_image)
#         end_time = time.time()
#         elapsed_time = end_time - start_time

#     # Natijani ko'rsatish
#     row2.text_area("Natija...", value=extracted_text, height=200)
#     st.write(f"Aniqlashga sarflangan vaqt: {elapsed_time:.2f} sekund")
# else:
#     st.write("Fayl yuklash tugmasini bosing")

# import streamlit as st
# import requests

# def facts():
#     api_url = f'{st.secrets['FACTS_URL']}'
#     response = requests.get(api_url, headers={'X-Api-Key': f"{st.secrets['OCR_QUOTE_API']}"})
#     if response.status_code == requests.codes.ok:
#         print(response.json()[0]['fact'])
#     else:
#         print("Error:", response.status_code, response.text)

# # 389eebc7-4e87-4c59-b0c0-d1a1f1c0aacc
# def tahrirchi(text):
#     api_url = "https://websocket.tahrirchi.uz/translate"
#     headers = {
#         "api-key": "389eebc7-4e87-4c59-b0c0-d1a1f1c0aacc", # "Authorization" o'rniga "api-key" ishlatib ko'ring
#         "Content-Type": "application/json"
#     }
#     data = {
#         "text": {"texts": [text]},
#         "source_lang": "eng_Latn",
#         "target_lang": "uzn_Latn",
#     }
#     response = requests.post(api_url, json=data, headers=headers)
#     if response.status_code == 200:
#         print(response.json()['sentences'][-1]['translated'])
#     else:
#         print("Error:", response.status_code, response.text)

# # tahrirchi(facts())
# tahrirchi("Hi my name is Alijon")