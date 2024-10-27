import streamlit.components.v1 as components
import streamlit as st
# def app():
#     # components.iframe("https://xarajat.netlify.app/",scrolling=True)
#     st.html("<h2 style='text-align:center; color:red;'>Brayl alifbosi</h2>")
#     col1,col2,col3, col4, col5, col6, col7 = st.columns(7)
#     with col1:
#         a=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠁</button>  
#                     # onclick="document.getElementById('result').value += 'a'
#                 """)
#         b=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠃</button>  
#                 """)
#         d=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠙</button>  
#                 """)
#         e=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠑</button>  
#                 """)
        
#     with col2:
#         f=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠋</button>  
#                 """)
#         g=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠛</button>  
#                 """)
#         h=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠓</button>  
#                 """)
#         i=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠊</button>  
#                 """)
#     with col3:
#         j=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠚</button>  
#                 """)
#         k=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠅</button>  
#                 """)
#         l=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠇</button>  
#                 """)
#         m=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠍</button>  
#                 """)
#     with col4:
#         n=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠝</button>  
#                 """)
#         o=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠕</button>  
#                 """)
#         p=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠏</button>  
#                 """)
#         q=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠽</button>  
#                 """)
#     with col5:
#         r=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠗</button>  
#                 """)
#         s=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠎</button>  
#                 """)
#         t=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠞</button>  
#                 """)
#         u=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠥</button>  
#                 """)
#     with col6:
#         v=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠺</button>  
#                 """)
#         x=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠹</button>  
#                 """)
#         y=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠯</button>  
#                 """)
#         z=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠵</button>  
#                 """)
#     with col7:
#         ch=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠟</button>  
#                 """)
#         sh=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠱</button>  
#                 """)
#         o_=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠧</button>  
#                 """)
#         g_=st.html("""  
#                     <style>  
#                         .my-button {  
#                             color: red;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button">⠻</button>  
#                 """)
    
#     st.html("<h2 style='text-align:center; color:#116466;'>Brayl raqamlari</h2>")
#     qator1, qator2, qator3, qator4, qator5= st.columns(5)
    
#     with qator1:
#         N0=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠚</button>  
#                 """)
#         N1=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠁</button>  
#                 """)
#     with qator2:
#         N2=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠃</button>  
#                 """)
#         N3=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠉</button>  
#                 """)
#     with qator3:
#         N4=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠙</button>  
#                 """)
#         N5=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠑</button>  
#                 """)
#     with qator4:
#         N6=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠋</button>  
#                 """)
#         N7=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠛</button>  
#                 """)
#     with qator5:
#         N8=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠓</button>  
#                 """)
#         N9=st.html("""  
#                     <style>  
#                         .my-button1 {  
#                             color: #116466;   
#                             border-radius: 10px;   
#                             font-size: 40px;   
#                             border-color: blue;   
#                             border: 1px solid green;  
#                             background-color: transparent;  
#                             transition: background-color 0.3s, color 0.3s;  
#                         }  
#                         .my-button1:hover {  
#                             background-color: red;   
#                             color: white;  
#                         }  
#                         .my-button1:active {  
#                             background-color: aqua;   
#                             color: white;  
#                         }  
#                     </style>  
                    
#                     <button class="my-button1">⠊</button>  
#                 """)
#     space=st.button("Space", type='primary', use_container_width=True)
#     # result = st.text_input("Natija qismi", placeholder="Text output...")
#     result = st.text_input("Natija qismi", placeholder="Text output...", key="result")


import streamlit as st

def app():
    if 'result' not in st.session_state:
        st.session_state.result = ""

    st.html("<h2 style='text-align:center; color:red;'>Brayl alifbosi</h2>")
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    with col1:
        if st.button("⠁", key="a", help="A harfi"):
            st.session_state.result += "a"
        if st.button("⠃", key="b", help="B harfi"):
            st.session_state.result += "b"
        if st.button("⠙", key="d", help="D harfi"):
            st.session_state.result += "d"
        if st.button("⠑", key="e", help="E harfi"):
            st.session_state.result += "e"

    with col2:
        if st.button("⠋", key="f", help="F harfi"):
            st.session_state.result += "f"
        if st.button("⠛", key="g", help="G harfi"):
            st.session_state.result += "g"
        if st.button("⠓", key="h", help="H harfi"):
            st.session_state.result += "h"
        if st.button("⠊", key="i", help="I harfi"):
            st.session_state.result += "i"

    with col3:
        if st.button("⠚", key="j", help="J harfi"):
            st.session_state.result += "j"
        if st.button("⠅", key="k", help="K harfi"):
            st.session_state.result += "k"
        if st.button("⠇", key="l", help="L harfi"):
            st.session_state.result += "l"
        if st.button("⠍", key="m", help="M harfi"):
            st.session_state.result += "m"

    with col4:
        if st.button("⠝", key="n", help="N harfi"):
            st.session_state.result += "n"
        if st.button("⠕", key="o", help="O harfi"):
            st.session_state.result += "o"
        if st.button("⠏", key="p", help="P harfi"):
            st.session_state.result += "p"
        if st.button("⠽", key="q", help="Q harfi"):
            st.session_state.result += "q"

    with col5:
        if st.button("⠗", key="r", help="R harfi"):
            st.session_state.result += "r"
        if st.button("⠎", key="s", help="S harfi"):
            st.session_state.result += "s"
        if st.button("⠞", key="t", help="T harfi"):
            st.session_state.result += "t"
        if st.button("⠥", key="u", help="U harfi"):
            st.session_state.result += "u"

    with col6:
        if st.button("⠺", key="v", help="V harfi"):
            st.session_state.result += "v"
        if st.button("⠹", key="x", help="X harfi"):
            st.session_state.result += "x"
        if st.button("⠯", key="y", help="Y harfi"):
            st.session_state.result += "y"
        if st.button("⠵", key="z", help="Z harfi"):
            st.session_state.result += "z"

    with col7:
        if st.button("⠟", key="ch", help="Ch harfi"):
            st.session_state.result += "ch"
        if st.button("⠱", key="sh", help="Sh harfi"):
            st.session_state.result += "sh"
        if st.button("⠧", key="o'", help="O' harfi"):
            st.session_state.result += "o'"
        if st.button("⠻", key="g'", help="G' harfi"):
            st.session_state.result += "g'"

    st.html("<h2 style='text-align:center; color:#116466;'>Brayl raqamlari</h2>")
    
    qator1, qator2, qator3, qator4, qator5 = st.columns(5)
    
    with qator1:
        if st.button("⠚", key="0", help="0 raqami"):
            st.session_state.result += "0"
        if st.button("⠁", key="1", help="1 raqami"):
            st.session_state.result += "1"

    with qator2:
        if st.button("⠃", key="2", help="2 raqami"):
            st.session_state.result += "2"
        if st.button("⠉", key="3", help="3 raqami"):
            st.session_state.result += "3"

    with qator3:
        if st.button("⠙", key="4", help="4 raqami"):
            st.session_state.result += "4"
        if st.button("⠑", key="5", help="5 raqami"):
            st.session_state.result += "5"

    with qator4:
        if st.button("⠋", key="6", help="6 raqami"):
            st.session_state.result += "6"
        if st.button("⠛", key="7", help="7 raqami"):
            st.session_state.result += "7"

    with qator5:
        if st.button("⠓", key="8", help="8 raqami"):
            st.session_state.result += "8"
        if st.button("⠊", key="9", help="9 raqami"):
            st.session_state.result += "9"

    if st.button("Space", type='primary', use_container_width=True):
        st.session_state.result += " "

    result = st.text_input("Natija qismi", 
                          value=st.session_state.result,
                          key="result_input",
                          placeholder="Text output...")
    
    if st.button("Tozalash", type="secondary", use_container_width=True):
        st.session_state.result = ""
        st.experimental_rerun()

if __name__ == "__main__":
    app()