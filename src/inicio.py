# PRESENTATION TIER

# No standard imports
# 3rd party library imports
import streamlit as st
# local imports from CONTROL tier
import funciones

# Version de la aplicación
version = "0.20231127"

# Configuración de la página
st.set_page_config(
    page_title="Appetito",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded")

# Establecer login como falso
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


def sidebar():
    """
    Esta función define y despliega la barra lateral de la
    aplicación "Appetito". Crea botones según las diferentes
    vistas de la página web. Si se presiona algún botón, la sesión
    cambia y luego se llama a la función funciones.vistas() para
    mostrar la página correspondiente.

    Detalles de la función:

    - Si el usuario está loggeado, muestra un saludo personalizado
      en la barra lateral.

    - Crea botones en la barra lateral para navegar entre las
      diferentes secciones de la aplicación, como la página principal
      ("Home"), recetas saludables ("Healthy recipes"), recetas sencillas
      ("Simple Recipes"), recetas especiales ("Special Recipes"),
      recetas horneadas ("Baked Recipes"), favoritos ("Favorites"),
      y cerrar sesión ("Logout").

    - Si el usuario no está loggeado, muestra opciones para registrarse
      ("Sign up") o iniciar sesión ("Log In").

    - La función utiliza el estado de la sesión de Streamlit para
      gestionar la página actual y redirigir a la función
      funciones.vistas() para mostrar el contenido correspondiente
      a la página seleccionada.

    Ejemplo de uso:
    >>> sidebar()
    """

    if st.session_state['logged_in']:
        st.sidebar.title("Welcome " + st.session_state.nombre + "!")

        if st.sidebar.button("Home", key="home"):
            st.session_state.page = 'home'
        
        if st.sidebar.button("contact us", key="contact_us"):
            st.session_state.page = 'contact_us'

        st.sidebar.title("Recipes")
        # Para desplegar las recetas fit
        if st.sidebar.button("Healthy recipes", key="recetas_fit"):
            st.session_state.page = 'saludable'

        # Para desplegar las recetas sencillas
        if st.sidebar.button("Simple Recipes", key="recetas_sencillas"):
            st.session_state.page = 'presupuesto'

        # Para desplegar las recetas especiales
        if st.sidebar.button("Special Recipes", key="recetas_especiales"):
            st.session_state.page = 'especiales'

        # Para desplegar las recetas horneadas
        if st.sidebar.button("Baked Recipes", key="recetas_horneadas"):
            st.session_state.page = 'horneado'
        
        st.sidebar.title("Account")

        if st.sidebar.button("Account", key="account"):
            st.session_state.page = 'account'

        if st.sidebar.button('Favorites', key="favorites"):
            st.session_state.page = 'favorites'

        if st.sidebar.button("Account", key="account"):
            st.session_state.page = 'account'

        if st.sidebar.button("Logout", key="logout"):
            st.session_state['logged_in'] = False
            st.session_state.nombre = None
            st.session_state.page = 'home'
            st.rerun()

    else:
        if st.sidebar.button("Home", key="home"):
            st.session_state.page = 'home'
        
        if st.sidebar.button("contact us", key="contact_us"):
            st.session_state.page = 'contact_us'

        # Aquí es la parte de cuenta de la aplicación
        st.sidebar.title("Account")
        # Para registrarse - crear cuenta
        if st.sidebar.button("Sign up", key="signup"):
            st.session_state.page = 'signup'

        # Para iniciar sesión - acceder a una cuenta existente
        if st.sidebar.button("Log In", key="login"):
            st.session_state.page = 'login'

    # Llamar a la función para mostrar la página correspondiente
    page = st.session_state.get('page', 'home')
    return funciones.vistas(page)


def footer():
    """
    This function creates the footer to display developer information.

    Detalles de la función:

    - Crea un pie de página para mostrar información sobre los desarrolladores
      y la forma de contacto.

    - Utiliza el módulo `streamlit` para mostrar HTML con estilos CSS.

    Ejemplo de uso:
    >>> footer()
    """
    st.markdown("""
        <style>
            .ezrtsby2, .ea3mdgi1 { visibility: hidden; }
            .footer: {
                position: fixed;
                bottom: 0;
                width: 100%;
                height: 50px;
                background-color: #00000;
                color: #ffffff;
                text-align: left;
                padding-top: 15px;
                padding-left: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <footer class='footer'>
            Developed by: Daniel Garzon and Luis Moreno |
            Contact: dgarzonac@unal.edu.co</a> and lumorenoc@unal.edu.co</a>
            \n Version {version} Alpha snapshot
        </footer>
    """, unsafe_allow_html=True)


# sidebar y footer de llaman para que sean siempre visibles
sidebar()
footer()
