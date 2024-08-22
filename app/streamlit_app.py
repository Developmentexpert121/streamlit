import streamlit as st

# Set the sidebar background color to dark
st.markdown(
    """
    <style>
    p, h1, h2, h3, h4, h5, h6, div, body {
            color: #fff !important;
        }
        h1, h2, h3, h4, h5, h6 {
            padding-top: 0;
        }
    [data-testid="stSidebar"], .stApp[data-testid="stApp"] {
    background: #09241f;
    color: #fff;
}
[data-testid="stSidebarUserContent"] label[data-baseweb="radio"] > div:last-child p,
[data-testid="stSidebarUserContent"] h1, [data-testid="stSidebar"] + section.main h1 {
    color: #fff;
}
[data-testid="stSidebarUserContent"] label[data-baseweb="radio"] > div:first-child {
    display: none;
}
[data-testid="stSidebarUserContent"] label[data-baseweb="radio"] > div:last-child {
    padding: 10px;
    width: 100%;
    border-radius: 10px;
}
[data-testid="stAppViewBlockContainer"] {
    max-width: 1000px;
    padding-inline: 40px;
}
 [data-testid="stSidebar"] + section.main h1 {
    padding-top: 0;
 }
[data-testid="stSidebarUserContent"] label[data-baseweb="radio"] {
    width: 100%;
    margin-right: 0;
}
[data-testid="stSidebarUserContent"] [data-testid="stWidgetLabel"] {
    display: none;
}
[data-testid="stSidebar"] + section.main {
    background: #0f352e;
}
header[data-testid="stHeader"] {
    background: #09241f;
}
[data-testid="baseButton-headerNoPadding"] {
    background-color: rgb(255 255 255 / 85%) !important;
    color: #000 !important
}
[data-testid="baseButton-headerNoPadding"]:hover {
    background-color: rgb(255 255 255 / 100%) !important;
}
[data-testid="stSidebarUserContent"] label[data-baseweb="radio"] [tabindex="0"] + div:last-child, 
[data-testid="stSidebarUserContent"] label[data-baseweb="radio"] [tabindex="-1"] + div:last-child:hover {
    background: #307f71;
}
[data-testid="stSidebarUserContent"] [role="radiogroup"] {
    gap: 5px;
}
hr {
            background-color: #ffffff40;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the sidebar menu with icons
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📄 FAQ",
        "📑 Page 2",
        "📊 Page 3",
        "📊 Signin"
    ]
)

# Map menu items to functions
pages = {
    "🏠 Home": "home",
    "📄 FAQ": "faq",
    "📑 Page 2": "page2",
    "📊 Page 3": "page3",
    "📊 Signin": "signin"
}

def main():
    # Load the selected page module and call the display function
    module_name = pages.get(menu)
    if module_name:
        module = __import__(module_name)
        display_func = getattr(module, f"display_{module_name}")
        display_func()

if __name__ == "__main__":
    main()
