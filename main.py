import streamlit as st
import hydralit_components as hc
import streamlit.components.v1 as com
import pandas as pd
import wordcloud
import streamlit_pandas as sp
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from IPython.display import display
from wordcloud import WordCloud

import warnings
warnings.filterwarnings("ignore")


#make it look nice from the start
st.set_page_config(layout='wide',initial_sidebar_state='collapsed')
# Cambia el color de fondo a un gris claro (puedes usar cualquier otro color)
st.markdown(
    """
    <style>
        body {
            background-color: #000000;  /* Cambia este valor al color que desees */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# specify the primary menu definition
menu_data = [
    {'id':'weare','icon': "bi bi-people", 'label':"We Are"},
    {'id':'wedo','icon':"bi bi-laptop",'label':"We Do"},
    {'id':'recommendation','icon': "bi bi-heart", 'label':"Recommendation"},#no tooltip message
    {'id':'dashboard','icon': "fas fa-tachometer-alt", 'label':"Dashboard"},
    {'id':'contact','icon':"bi bi-envelope",'label':"Contact Us"} #can add a tooltip message
]   

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=False, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)

#get the id of the menu item clicked


def home():
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Crear un espacio vacío horizontal
        
    col1,col2 = st.columns([1,1])

    with col2:
        

        # Agrega HTML personalizado con estilos CSS al encabezado
        st.markdown(
            """
            <style>
                .custom-header {
                    color: #ecf0f1;  /* Cambia este valor al color que desees */
                    font-size: 3em;  /* Tamaño de fuente */
                    text-align: center;  /* Alineación del texto */
                    padding: 20px;  /* Espaciado interno */
                    border-radius: 10px;  /* Bordes redondeados */
                }
            </style>
            """,
            unsafe_allow_html=True
        )



        # Agrega HTML personalizado con estilos CSS al contenido informativo
        st.markdown(
            """
            <style>
                .custom-info {
                    color: #2c3e50;  /* Cambia este valor al color que desees */
                    font-size: 1.2em;  /* Tamaño de fuente */
                    line-height: 1.6;  /* Altura de línea */
                    text-align: justify;  /* Alineación del texto */
                    background-color: #ecf0f1;  /* Color de fondo */
                    padding: 20px;  /* Espaciado interno */
                    border-radius: 10px;  /* Bordes redondeados */
                    margin-top: 20px;  /* Margen superior */
                    margin-bottom: 20px;  /* Margen inferior */
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.info('# Empresa binacional con un serio enfoque en los negocios')
        # Contenido informativo con estilos personalizados
        st.markdown(
            '''
            ### Concentrandonos en las oportunidades y potencial de tu emprendimiento. En cortos periodos de tiempo y con una calidad excepcional impulsamos tu negocio hacia las nubes. 
            ''',
            unsafe_allow_html=True
        )


        
    with col1:
        #st.image(img_path,use_column_width=None)
        st.markdown("<br>", unsafe_allow_html=True)
        # Crear un espacio vacío horizontal
        st.markdown("<div style='margin: 0;'></div>", unsafe_allow_html=True)
        video_path = 'pexels-tima-miroshnichenko-5717001 (2160p).mp4'
        st.video(video_path)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100px;'></div>", unsafe_allow_html=True)

    # Encabezado con estilos personalizados
    st.markdown(
            "<h1 class='custom-header'>Productos</h1>",
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)

    col1,col2,col3= st.columns([1,2,1])
    with col1:
            st.markdown(
                '''
                #
                # ''',
                unsafe_allow_html=True
            )

    with col3:
         st.markdown(
             '''
             #
             # ''',
            unsafe_allow_html=True
        )
    with col2:
        com.iframe('https://lottie.host/embed/61eaa909-466b-4f9a-a31d-956e8311da89/vK6VUUGwJ2.json')
        st.markdown(
             '''
             ## Data Base Structure
             ### En Arcol, fusionamos la artesanía tecnológica con la innovación para ofrecer soluciones de base de datos a medida que potencian su capacidad operativa y optimizan el flujo de datos en su organización.
             ''',unsafe_allow_html=True
        )

    
    st.markdown("<div style='margin: 35px;'></div>", unsafe_allow_html=True)


    col1,col2,col3= st.columns([2,1,2])

    with col1:
        com.iframe('https://lottie.host/embed/a5a0ebad-3aa3-4905-9dd2-7f4fc7e99db6/F4Kq9eI3x8.json')        
        st.markdown(
             '''
             ## Machine Learning Models
             ### Potenciamos los modelos de  inteligencia artificial con la experiencia técnica para proporcionar soluciones de machine learning automático personalizados que impulsan la innovación y el rendimiento en su organización''',
            unsafe_allow_html=True
        )
    
    with col2:
         st.markdown(
             '''
             #
             # ''',
            unsafe_allow_html=True
        )

    with col3:
        com.iframe('https://lottie.host/embed/319c99c3-ea04-4a2d-a35d-b2e947a2f9dd/OP7zE59PEX.json')
        st.markdown(
             '''
             ## Data Visualization
             ### Concentramos nuestros esfuerzos en la estética visual con la claridad analítica para ofrecer soluciones de visualización de datos que transforman datos complejos en insights comprensibles''',
            unsafe_allow_html=True
        ) 

       # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100px;'></div>", unsafe_allow_html=True)


    # Agrega HTML personalizado con estilos CSS al encabezado
    st.markdown(
            """
            <style>
                .custom-header {
                    color: #3498db;  /* Cambia este valor al color que desees */
                    font-size: 3em;  /* Tamaño de fuente */
                    text-align: center;  /* Alineación del texto */
                    padding: 20px;  /* Espaciado interno */
                    background-color: #ecf0f1;  /* Color de fondo */
                    border-radius: 10px;  /* Bordes redondeados */
                }
            </style>
            """,
        unsafe_allow_html=True
        )

        # Encabezado con estilos personalizados
    st.markdown(
            "<h1 class='custom-header'>StakeHolders: Mejores Decisiones y Recomendaciones Estrategicas</h1>",
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)

    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 15px;'></div>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns([2,1,2])

    

    with col1:
        gif_path = 'https://lottie.host/embed/ed974d44-8678-4c3d-adf5-4d57e4f6578a/hCl3BJyYQW.json'
        com.iframe(gif_path)                
        st.markdown(
            """
            <style>
                .custom-info {
                    color: #2c3e50;  /* Cambia este valor al color que desees */
                    font-size: 1.2em;  /* Tamaño de fuente */
                    line-height: 1.6;  /* Altura de línea */
                    text-align: justify;  /* Alineación del texto */
                    background-color: #ecf0f1;  /* Color de fondo */
                    padding: 20px;  /* Espaciado interno */
                    border-radius: 10px;  /* Bordes redondeados */
                    margin-top: 20px;  /* Margen superior */
                    margin-bottom: 20px;  /* Margen inferior */
                }
            </style>
            """,
        unsafe_allow_html=True
        )
        st.markdown(
            '''
            ## Tiempo Corto, Exito Alto
            ### Solidos sistemas de recomendacion basados en indicadores actualizados de manera constante. ''',
            unsafe_allow_html=True
        )
        gif_path = 'https://lottie.host/embed/2d6166a2-2e1f-48e5-8b81-a4461e348188/DyOkYv5i6U.json'
        com.iframe(gif_path)  
        
        st.markdown(
            '''
            ## Precision Y Confiabilidad
            ### Base de datos solidas e informacion precisa en relacion a aquellos negocios potencialmente atractivos.
            ''',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown('''#
                    ''',unsafe_allow_html=True)
    with col3:

        gif_path = 'https://lottie.host/embed/3e5bea85-498e-4780-a6be-18ec18745874/nueZiA09v1.json'
        com.iframe(gif_path)
        st.markdown(
            """
            <style>
                .custom-info {
                    color: #2c3e50;  /* Cambia este valor al color que desees */
                    font-size: 1.2em;  /* Tamaño de fuente */
                    line-height: 1.6;  /* Altura de línea */
                    text-align: justify;  /* Alineación del texto */
                    background-color: #ecf0f1;  /* Color de fondo */
                    padding: 20px;  /* Espaciado interno */
                    border-radius: 10px;  /* Bordes redondeados */
                    margin-top: 20px;  /* Margen superior */
                    margin-bottom: 20px;  /* Margen inferior */
                }
            </style>
            """,
        unsafe_allow_html=True
        )
        
        st.markdown(
            '''
            ## Guia Informada
            ### Identificacion de oportunidades segun las necesidades de cada cliente.
            ''',
            unsafe_allow_html=True
        )

        gif_path = 'https://lottie.host/embed/9a793a3a-64ae-4a6e-9c12-3251b5c7e27c/xcJD21hHN1.json'
        com.iframe(gif_path)
        st.markdown(
            '''
            ## Medicion de Exito
            ### Crecimiento porcentual de la satisfaccion de cada cliente. Aumento de rentabilidad y consolidacion en el mercado.''',
            unsafe_allow_html=True
        )
        # Agrega HTML personalizado para el footer
        st.markdown(
            """
            <style>
                .footer {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px;
                    background-color: #f1f1f1; /* Color de fondo del footer */
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                }
                .column {
                    display: flex;
                    align-items: center;
                }
                .column img {
                    width: 30px; /* Ajusta el tamaño de las imágenes según sea necesario */
                    margin-right: 10px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Contenido del footer en formato HTML y CSS
        footer = """
            <style>
                .footer {
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    background-color: #f1f1f1;
                    text-align: center;
                    padding: 10px;
                }
            </style>
            <div class="footer">
                <p>© 2024 ARCOL. Todos los derechos reservados.</p>
            </div>
        """

        # Mostrar el contenido del footer en la aplicación
        st.markdown(footer, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100px;'></div>", unsafe_allow_html=True)
 
def weare():
    st.markdown("<br>", unsafe_allow_html=True)

    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100;'></div>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])

    with col2:
        st.markdown(
            """
            <style>
                .custom-header {
                    color: #000000;  /* Cambia este valor al color que desees */
                    font-size: 3em;  /* Tamaño de fuente */
                    text-align: center;  /* Alineación del texto */
                    padding: 20px;  /* Espaciado interno */
                    border-radius: 10px;  /* Bordes redondeados */
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        # Encabezado con estilos personalizados

        gif_path = 'https://lottie.host/embed/03a89405-e0c5-4b9e-8046-58004a237bfe/kmV6qAkUMs.json'

        # Agrega HTML personalizado con estilos CSS al contenido informativo
        st.markdown(
            """
            <style>
                .custom-info {
                    color: #2c3e50;  /* Cambia este valor al color que desees */
                    font-size: 1.2em;  /* Tamaño de fuente */
                    line-height: 1.6;  /* Altura de línea */
                    text-align: justify;  /* Alineación del texto */
                    background-color: #ecf0f1;  /* Color de fondo */
                    padding: 20px;  /* Espaciado interno */
                    border-radius: 10px;  /* Bordes redondeados */
                    margin-top: 20px;  /* Margen superior */
                    margin-bottom: 20px;  /* Margen inferior */
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<div style='margin: 100;'></div>", unsafe_allow_html=True)


        # Contenido informativo con estilos 
        st.info('# Asesores expertos que llevaran tu negocio al exito')
        st.markdown(
            '''
            ### Somos apasionados del mundo tecnologico y empresarial. Llevando nuestro talento y disciplina a nuevas alturas a nuevas alturas. No solo creamos soluciones, sino que también forjamos caminos hacia la excelencia. 
            ### Con cada línea de código, construimos el puente entre la innovación y la realidad empresarial, impulsando el progreso y  asegurándonos de que cada desafío tecnológico sea una oportunidad para el crecimiento.''',
            unsafe_allow_html=True
        )

        st.markdown("<div style='margin: 100;'></div>", unsafe_allow_html=True)

    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        # Crear un espacio vacío horizontal
        st.markdown("<div style='margin: 150;'></div>", unsafe_allow_html=True)
        st.image('4470582.png', use_column_width=None)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 100;'></div>", unsafe_allow_html=True)

    # Encabezado con estilos personalizados
    st.markdown(
            "<h1 class='custom-header'>Nuestros Expertos</h1>",
        unsafe_allow_html=True
        )
    team_path = 'Presentacion.png'
    st.image(team_path, use_column_width=None)
    st.info('''Lideres y especialista en cada una de sus actividades. 
              Los mejores en su campo y quienes aseguraran el mayor de los exitos para tu negocio ''')
    
        # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100;'></div>", unsafe_allow_html=True)


        # Agrega HTML personalizado con estilos CSS al encabezado
    st.markdown(
            """
            <style>
                .custom-header {
                    color: #3498db;  /* Cambia este valor al color que desees */
                    font-size: 3em;  /* Tamaño de fuente */
                    text-align: center;  /* Alineación del texto */
                    padding: 20px;  /* Espaciado interno */
                    background-color: #ecf0f1;  /* Color de fondo */
                    border-radius: 10px;  /* Bordes redondeados */
                }
            </style>
            """,
        unsafe_allow_html=True
        )
    
    

        # Encabezado con estilos personalizados
    st.markdown(
            "<h1 class='custom-header'>Rocks Stars</h1>",
        unsafe_allow_html=True
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
        # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 15;'></div>", unsafe_allow_html=True)


    col1,col2 = st.columns([1,1])

    with col1:
        st.image('leonardo.png', width=550)
    with col2:
        st.subheader('Leonardo Cortes')
        com.iframe('https://lottie.host/embed/1b985ded-a835-4fde-8d74-bafaffb88f18/iB81P7TLjB.json')

        # Aplicar estilos CSS al texto
        styled_text = '''
            <div style="font-family: 'Arial', sans-serif; color: #333; background-color: #f8f8f8; padding: 15px; border-radius: 10px;">
                <p>Mathematician, musician, Jazz performer, Composer and producer.</p>
                <p><strong>Strong Skills:</strong></p>
                <ul>
                    <li>Financial Advisory</li>
                    <li>Mathematician</li>
                    <li>Data Analyst & Scientist</li>
                </ul>
                <p><strong>Soft Skills</strong></p>
                <ul>
                    <li>Leadership</li>
                    <li>Strategic Thinking</li>
                    <li>Problem Solving</li>
                </ul>
                <p><strong>Hobbies:</strong> Reading, Cars racing, Bartending, Write and produce music, DJing.</p>
            </div>
        '''

        # Mostrar el texto con estilos
        st.markdown(styled_text, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 15;'></div>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])

    with col1:
        st.image('Marcelo.png', width=550)
    with col2:
        st.subheader('Marcelo Atencio')
        com.iframe('https://lottie.host/embed/61732b10-4336-4661-83ed-f67136954c2b/Y45xknE8QG.json')

        # Aplicar estilos CSS al texto
        styled_text = '''
            <div style="font-family: 'Arial', sans-serif; color: #333; background-color: #f8f8f8; padding: 15px; border-radius: 10px;">
                <p>Engineer, Data Scientist, Data Analyst.</p>
                <p><strong>Strong Skills:</strong></p>
                <ul>
                    <li>Project Management</li>
                    <li>Machine Learning</li>
                    <li>Data Visualization</li>
                </ul>
                <p><strong>Soft Skills</strong></p>
                <ul>
                    <li>Time Management</li>
                    <li>Problem Solving</li>
                </ul>
                <p><strong>Hobbies:</strong>Cycling, Gym, Cinephile, Cook.</p>
            </div>
        '''

        # Mostrar el texto con estilos
        st.markdown(styled_text, unsafe_allow_html=True)    

    st.markdown("<br>", unsafe_allow_html=True)
    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 15;'></div>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])

    with col1:
        st.image('fede.png', width=550)
    with col2:
        st.subheader('Federico Lopez')
        com.iframe('https://lottie.host/embed/565fe640-a151-447d-9e00-d4a274f2ac5d/fCgjPL7V2P.json')

        # Aplicar estilos CSS al texto
        styled_text = '''
            <div style="font-family: 'Arial', sans-serif; color: #333; background-color: #f8f8f8; padding: 15px; border-radius: 10px;">
                <p>Computer Scientist, Data Scientist, Data Analyst.</p>
                <p><strong>Strong Skills:</strong></p>
                <ul>
                    <li>Python</li>
                    <li>Data Analysis</li>
                    <li>Data Handling</li>
                </ul>
                <p><strong>Soft Skills</strong></p>
                <ul>
                    <li>Public Speaking</li>
                    <li>Communication Skills</li>
                </ul>
                <p><strong>Hobbies:</strong> Swimming, Guitar and Piano, Programming, Voice-over.</p>
            </div>
        '''

        # Mostrar el texto con estilos
        st.markdown(styled_text, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 15;'></div>", unsafe_allow_html=True)

    col1,col2 = st.columns([1,1])

    with col1:
        st.image('Andres.png', width=550)
    with col2:
        st.subheader('Andres Ruiz')
        com.iframe('https://lottie.host/embed/9916f98f-0b71-4929-a6ea-2a61cf35a163/nGwNhGkeyN.json')

        # Aplicar estilos CSS al texto
        styled_text = '''
            <div style="font-family: 'Arial', sans-serif; color: #333; background-color: #f8f8f8; padding: 15px; border-radius: 10px;">
                <p>Mathematician, Data Scientist, Database Manager, Data Analyst.</p>
                <p><strong>Strong Skills:</strong></p>
                <ul>
                    <li>Mathematician</li>
                    <li>Data Scientist</li>
                    <li>Database Manager</li>
                </ul>
                <p><strong>Soft Skills</strong></p>
                <ul>
                    <li>Time Managment</li>
                    <li>Public Speaking</li>
                </ul>
                <p><strong>Hobbies:</strong> Reading, Video Games, Music listening & Violin, Gym & Box.</p>
            </div>
        '''

        # Mostrar el texto con estilos
        st.markdown(styled_text, unsafe_allow_html=True)

        # Contenido del footer en formato HTML y CSS
    footer = """
            <style>
                .footer {
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    background-color: #f1f1f1;
                    text-align: center;
                    padding: 10px;
                }
            </style>
            <div class="footer">
                <p>© 2024 ARCOL. Todos los derechos reservados.</p>
            </div>
        """

        # Mostrar el contenido del footer en la aplicación
    st.markdown(footer, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
        
def contact():
    
    col1, col2,col3 = st.columns([2,1,2])

    with col1:
        # Estilos CSS
        st.markdown(
            """
            <style>
            .contact-container {
                max-width: 600px;
                margin: auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .contact-header {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .contact-input {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .contact-button {
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
            }
            .contact-button:hover {
                background-color: #0056b3;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.title("Aplicación de Contacto")

        # Sección de Información de Contacto
        #st.markdown('<div class="contact-container">', unsafe_allow_html=True)
        st.write("¡Contáctanos para cualquier consulta o comentario!")

        # Campos de Entrada
        name = st.text_input("Nombre", max_chars=50, key="name")
        email = st.text_input("Correo Electrónico", max_chars=100, key="email")
        message = st.text_area("Mensaje", max_chars=500, key="message")

        # Botón de Envío
        if st.button("Enviar", key="submit"):
            # Procesa los datos (por ejemplo, envía un correo electrónico)
            # Aquí puedes agregar la lógica para manejar el formulario de contacto
            st.success("¡Mensaje enviado con éxito!")
        com.iframe('https://lottie.host/embed/cce610b2-733e-4a7a-874d-5307cdd32093/B4xd9CRsCX.json')

    with col2:
        st.markdown('''
                #''',unsafe_allow_html=True)
    with col3:
        st.markdown('''
                #
                #
                #
                ''',unsafe_allow_html=True)
        st.image('PNGArcol1.png', width= 450)

    st.markdown('</div>', unsafe_allow_html=True)

      # Contenido del footer en formato HTML y CSS
    footer = """
            <style>
                .footer {
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    background-color: #f1f1f1;
                    text-align: center;
                    padding: 10px;
                }
            </style>
            <div class="footer">
                <p>© 2024 ARCOL. Todos los derechos reservados.</p>
            </div>
        """

        # Mostrar el contenido del footer en la aplicación
    st.markdown(footer, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

def wedo():

     # Agrega HTML personalizado con estilos CSS al encabezado
    st.markdown(
            """
            <style>
                .custom-header {
                    color: #3498db;  /* Cambia este valor al color que desees */
                    font-size: 3em;  /* Tamaño de fuente */
                    text-align: center;  /* Alineación del texto */
                    padding: 20px;  /* Espaciado interno */
                    background-color: #ecf0f1;  /* Color de fondo */
                    border-radius: 10px;  /* Bordes redondeados */
                }
            </style>
            """,
        unsafe_allow_html=True
        )

        # Encabezado con estilos personalizados
    st.markdown(
            "<h1 class='custom-header'>Manejo de Datos</h1>",
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)

    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 15px;'></div>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns([2,1,2])

    with col1:
        gif_path = 'https://lottie.host/embed/1ecb74e2-8e7e-4c47-83ac-6cb51cf96f34/ORUK7uEUsp.json'
        com.iframe(gif_path)                
        st.markdown(
            """
            <style>
                .custom-info {
                    color: #2c3e50;  /* Cambia este valor al color que desees */
                    font-size: 1.2em;  /* Tamaño de fuente */
                    line-height: 1.6;  /* Altura de línea */
                    text-align: justify;  /* Alineación del texto */
                    background-color: #ecf0f1;  /* Color de fondo */
                    padding: 20px;  /* Espaciado interno */
                    border-radius: 10px;  /* Bordes redondeados */
                    margin-top: 20px;  /* Margen superior */
                    margin-bottom: 20px;  /* Margen inferior */
                }
            </style>
            """,
        unsafe_allow_html=True
        )
        st.markdown(
            '''
            ## Descarga Automatizada
            ### Sistema integrado de recopilacion de datos. Uso de la nube, APIs y otras fuentes de digitales. ''',
            unsafe_allow_html=True
        )
        gif_path = 'https://lottie.host/embed/727b21fa-7684-48e7-8e43-fc55d9f0bab5/HIMzljYryc.json'
        com.iframe(gif_path)  
        
        st.markdown(
            '''
            ## Data Cleaning
            ### Dedicacion exhaustiva de la informacion proporcionada. Limpieza, seleccion y precision garantizada.
            ''',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)

        # Crear un espacio vacío horizontal
        st.markdown("<div style='margin: 100px;'></div>", unsafe_allow_html=True)


    with col3:

        gif_path = 'https://lottie.host/embed/f189b503-e868-4591-8e48-5621d491d822/ZikmUwWLDG.json'
        com.iframe(gif_path)
        st.markdown(
            """
            <style>
                .custom-info {
                    color: #2c3e50;  /* Cambia este valor al color que desees */
                    font-size: 1.2em;  /* Tamaño de fuente */
                    line-height: 1.6;  /* Altura de línea */
                    text-align: justify;  /* Alineación del texto */
                    background-color: #ecf0f1;  /* Color de fondo */
                    padding: 20px;  /* Espaciado interno */
                    border-radius: 10px;  /* Bordes redondeados */
                    margin-top: 20px;  /* Margen superior */
                    margin-bottom: 20px;  /* Margen inferior */
                }
            </style>
            """,
        unsafe_allow_html=True
        )
        
        st.markdown(
            '''
            ## ETL & ELT
            ### Transformacion y carga efectiva. Validacion durante el proceso para garantizar los mejores estandares.
            ''',
            unsafe_allow_html=True
        )

        gif_path = 'https://lottie.host/embed/841be7ec-23e5-4e71-a914-8d97304fbeed/IGRpEmYX4F.json'
        com.iframe(gif_path)
        st.markdown(
            '''
            ## Secuencias Automatizadas
            ### Sistema de Pipelines integrados. Flujo de trabajo que permite un mejor orden y sincronizacion de todos los parametros establecidos''',
            unsafe_allow_html=True
        )
        # Agrega HTML personalizado para el footer
        st.markdown(
            """
            <style>
                .footer {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px;
                    background-color: #f1f1f1; /* Color de fondo del footer */
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                }
                .column {
                    display: flex;
                    align-items: center;
                }
                .column img {
                    width: 30px; /* Ajusta el tamaño de las imágenes según sea necesario */
                    margin-right: 10px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Contenido del footer en formato HTML y CSS
        footer = """
            <style>
                .footer {
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    background-color: #f1f1f1;
                    text-align: center;
                    padding: 10px;
                }
            </style>
            <div class="footer">
                <p>© 2024 ARCOL. Todos los derechos reservados.</p>
            </div>
        """

        # Mostrar el contenido del footer en la aplicación
        st.markdown(footer, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100px;'></div>", unsafe_allow_html=True)



            # Encabezado con estilos personalizados
    st.markdown(
            "<h1 class='custom-header'>Grupo Tecnologico</h1>",
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)
    img_path = 'Presentacion1.png'
    st.image(img_path)

    st.info('''Simpre estamos a la vanguardia con el uso de tecnologias que 
            permitan la expresion mas sincera de la informacion y la facilidad para leerla''')
    
    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100px;'></div>", unsafe_allow_html=True)

    # Encabezado con estilos personalizados
    st.markdown(
            "<h1 class='custom-header'>Modelo Relacional</h1>",
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)

    col1,col2= st.columns([1,1])

    with col1:
        img_path1 = 'histo.png'
        img_path2 = 'md_relacional.png'
        st.image(img_path1, width=600)
        
        st.markdown("<div style='margin: 30px;'></div>", unsafe_allow_html=True)

        st.image(img_path2, width=600)
    
    with col2:
         st.markdown(
             '''
             # 
             # 
             #  
             ### El orden en que estructuramos nuestros modelos relacionales define la posición de nuestra empresa en el competitivo panorama actual. 
             ### Nos esforzamos por presentar de manera clara y accesible los pasos que configuran nuestro sistema, facilitando así la comprensión para todo tipo de audiencia. Además, cada pequeño proceso, al integrarse, contribuye a la formación de una estructura robusta, lo que resulta en una notable reducción de posibles errores.
             ### En Arcol, aseguramos la implementación de las mejores prácticas para obtener nuestros modelos más destacados.
                ''',
            unsafe_allow_html=True
        )

# Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100px;'></div>", unsafe_allow_html=True)

    # Encabezado con estilos personalizados
    st.markdown(
            "<h1 class='custom-header'>Valores</h1>",
        unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)

    col1,col2,col3= st.columns([2,1,2])

    with col1:
        com.iframe('https://lottie.host/embed/b821657e-1888-41e0-b640-fc08ec7d24d0/lECSkS8Jpd.json')        
        st.markdown(
             '''
             ## Efectividad y Veracidad: Arcol Optimiza el Tiempo con Tecnología
             ### En Arcol, nos regimos por los principios de efectividad, cordialidad y veracidad. Aprovechamos las tecnologías más avanzadas para gestionar el tiempo de manera eficiente, lo que se traduce en periodos de entrega más cortos.               ''',
            unsafe_allow_html=True
        )
    
    with col2:
         st.markdown(
             '''
             #
             # ''',
            unsafe_allow_html=True
        )

    with col3:
        com.iframe('https://lottie.host/embed/f3ae84de-8e24-4f67-bab4-222be4f6bbee/q9XfmWzqnf.json')
        st.markdown(
             '''
             ## Cordialidad y Respeto: Arcol estimula un excelente ambiente laboral
             ### Buscamos siempre que nuestra comunicacion sea veraz y respetuosa. En Arcol, nuestro mayor interes es mantener un entorno que permita la comunicacion acertiva.''',
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin: 15px;'></div>", unsafe_allow_html=True)

    col1,col2,col3= st.columns([1,2,1])
    with col1:
            st.markdown(
                '''
                #
                # ''',
                unsafe_allow_html=True
            )

    with col3:
         st.markdown(
             '''
             #
             # ''',
            unsafe_allow_html=True
        )
    with col2:
        com.iframe('https://lottie.host/embed/dd3f4d18-4447-452e-b3a1-87e37492ffd2/jHrm6PRFnf.json')
        st.markdown(
             '''
             ## Colaboracion, Gestion y Organizacion: Arcol organiza su trabajo
             ### En la misión de Arcol, la colaboración, gestión y organización son los pilares fundamentales que definen nuestra manera de trabajar. A través de la plataforma GitHub, hemos implementado una sólida estructura que fomenta la colaboración eficiente entre nuestros equipos de desarrollo. 
             ### Los repositorios dedicados a cada proyecto permiten una gestión centralizada del código fuente, brindando a nuestros desarrolladores la capacidad de trabajar en paralelo, crear ramas para nuevas características y proponer cambios de manera estructurada mediante solicitudes de extracción''',unsafe_allow_html=True
        )
         
def recommendation():
    st.markdown("<br>", unsafe_allow_html=True)

    # Crear un espacio vacío horizontal
    st.markdown("<div style='margin: 100;'></div>", unsafe_allow_html=True)

    st.info('# Sistema de Recomendacion')

    st.markdown("<div style='margin: 100;'></div>", unsafe_allow_html=True)

    df_model = pd.read_parquet('model.parquet')
    df_info = pd.read_parquet('df_info.parquet')

    # Combinar las columnas relevantes en una única columna de texto
    df_model['combined_features'] = df_model['Business_Name'] + ' ' + df_model['State'] + ' ' + df_model['Category']+' '+ df_model['Tourism_Cat']

# Inicializar el vectorizador TF-IDF
    tfidf_vectorizer = TfidfVectorizer()

# Ajustar y transformar el texto combinado en una matriz TF-IDF
    tfidf_matrix = tfidf_vectorizer.fit_transform(df_model['combined_features'])

# Calcular la similitud coseno entre todas las filas de la matriz TF-IDF
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def get_recommendations(business_name, cosine_sim=cosine_sim, df=df_model):
    # Obtener el índice del negocio con el nombre dado
        idx = df[df['Business_Name'] == business_name].index[0]
    
    # Obtener pares de similitud coseno para el negocio dado
        sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Ordenar los negocios según su similitud
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Obtener los índices de los 5 negocios más similares (excluyendo el propio negocio)
        similar_indices = [i[0] for i in sim_scores[1:6]]
    
    # Obtener los nombres y categorías de los 5 negocios más similares
        similar_businesses = df[['Business_Name', 'State', 'Category']].iloc[similar_indices]
    
        return similar_businesses

    def find_businesses(state, category=None):
        if category:
            # Filtrar el DataFrame principal por estado y categoría
            filtered_df = df_model[(df_model['State'] == state) & (df_model['Category'] == category)]
        else:
            # Filtrar el DataFrame principal solo por estado
            filtered_df = df_model[df_model['State'] == state]
            
        if filtered_df.empty:
            return None
        
        if category:
            # Filtrar para asegurar que haya diferentes valores de Tourism_Cat para cada negocio
            filtered_df = filtered_df.drop_duplicates(subset='Tourism_Cat')
            # Ordenar por distancia y tomar los 3 primeros negocios
            recommended_businesses = filtered_df.sort_values(by='Distance').head(3)
        else:
            # Para cada categoría, seleccionar el negocio con el ranking más alto
            top_ranked_businesses = filtered_df.groupby('Category').apply(lambda x: x.nlargest(1, 'Ranking'))
            recommended_businesses = top_ranked_businesses.reset_index(drop=True)
        
        # Devolver solo las columnas deseadas
        return recommended_businesses[['Business_Name', 'State', 'Category']]
    
    
    def get_business_info(business_name):
    # Buscar el negocio en el DataFrame df_info
        business_info = df_info[df_info['Business_Name'] == business_name]

        if business_info.empty:
            return None

        # Obtener los comentarios de clientes del negocio
        comments = business_info['Text'].values.tolist()

        # Concatenar todos los comentarios en un solo texto
        text = ' '.join(comments)

        # Generar el wordcloud de los comentarios
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        # Excluir la columna 'Text' de la información del negocio
        business_info = business_info.drop(columns=['Text'])

        # Eliminar duplicados del DataFrame business_info
        business_info = business_info.drop_duplicates()

        st.write('### Como me defino en una palabra:  ')

        # Mostrar el wordcloud en Streamlit
        st.image(wordcloud.to_array(),width=961)

        # Convertir business_info y recommendations en DataFrames
        business_info_df = pd.DataFrame(business_info)
        recommendations_df = pd.DataFrame(get_recommendations(business_name))

        st.markdown("<div style='margin: 100;'></div>", unsafe_allow_html=True)

        # Mostrar los DataFrames como tablas con títulos en Streamlit
        st.info('### Informacion del negocio seleccionado: ')
        st.table(business_info_df)
        
        st.info('### Otras Recomendaciones: ')
        st.table(recommendations_df.style)

        return recommendations_df

    state_list = list(df_model['State'].unique())
    state_list.insert(0,None)
    
    with st.sidebar:

        st.info('# Barra de Acciones')

        option_state = st.selectbox('Seleccione un Estado: ',state_list)
        cat_aux_df = df_model[df_model['State'] == option_state]
        
        category_list = list(cat_aux_df['Category'].unique())
        category_list.insert(0,None)
        option_category = st.selectbox('Seleccione una Categoria: ',category_list)

          
          

    if option_state == None:
        st.markdown('### Seleccione un ESTADO para continuar ')
    
    else:
        df_aux = find_businesses(option_state, option_category)

        buss_list = list(df_aux['Business_Name'].unique())
        buss_list.insert(0,None)

        with st.sidebar:
            option_buss = st.selectbox('Selecione un negocio: ', buss_list)
    
        if not option_buss:
            st.markdown('## Seleccione un NEGOCIO para continuar: ')
            st.dataframe(df_aux, width=1000)
        else:
            df = get_business_info(option_buss)
            buss_list = list(df['Business_Name'].unique())
            with st.sidebar:
                option_buss = st.selectbox('Seleccione un negocio: ', buss_list)

def dashboard():

    # Crear un enlace embebido usando HTML
    enlace_embebido = '<iframe width="1366" height="768" src="https://app.powerbi.com/view?r=eyJrIjoiZmVjY2JiNGItYjM4OC00MTM4LWI2YjYtYjA5YzdiY2RhYjgwIiwidCI6Ijk2M2JjMjIzLTBjMDktNDk3MC05NTlmLTIyZjdjODFkZWYzNyIsImMiOjR9" frameborder="0" allowfullscreen></iframe>'

    # Mostrar el enlace embebido en Streamlit
    st.markdown(enlace_embebido, unsafe_allow_html=True)


if menu_id == 'weare':
    # Lógica para la página "We Are"
    weare()

elif menu_id == 'wedo':
   # Lógica para la página "We Are"
    wedo()

elif menu_id == 'recommendation':
   # Lógica para la página "We Are"
    recommendation()

elif menu_id == 'dashboard':
   # Lógica para la página "We Are"
    dashboard()

elif menu_id == 'contact':
   # Lógica para la página "We Are"
    contact()

elif menu_id == 'Home':
   # Lógica para la página "We Are"
    home()

