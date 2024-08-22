import streamlit as st
import numpy as np

def display_home():
    st.markdown (
        """
        <style>
            [data-testid="stExpander"] summary {
                background: #09241f;
                border-radius: 10px;
                align-items: center;
                outline: none !important;
            }
            [data-testid="stExpander"] summary:hover {
                color: #fff;
            }
            [data-testid="stExpander"] summary:hover svg {
                fill: #fff;
            }
            [data-testid="stExpander"] summary p {
                font-size: 18px;
            }
            [data-testid="stExpanderDetails"] {
                padding-top: 20px;
                margin-top: -10px;
                background: #09241f;
                border-radius: 0px 0 10px 10px;
            }
            .flex-center {
                display: flex;
                gap: 15px;
                align-items: center;
            }
            p:last-child {
                margin-bottom:0;
            }
            .m-n10 {
                margin-inline: -10px;
            }
            .col-33 {
                padding-inline: 10px;
                width: 33.33%;
            }
            .flex-wrap {
                display: flex;
                flex-wrap: wrap;
            }
            hr {
                background-color: #ffffff40;
            }
            .card-border {
                padding: 15px;
                text-align: center;
                border: 1px solid #ffffff40;
                border-radius: 10px;
                margin-bottom: 20px !important;
            }
            .ai-default-text {
                margin-bottom: 25px;
            }
            .user-command {
                justify-content: end;
                flex-direction: row-reverse;
                padding: 10px;
                margin-bottom: 30px;
                background: #09241f;
                border-radius: 10px;
            }
            .ai-generated {
                padding-bottom: 30px;
            }
        </style>
        """, unsafe_allow_html=True
    )
    # st.title("Welcome to the Home Page")
    st.markdown (
        """
        <h1>Welcome to Stramlit</h1>
        """,unsafe_allow_html=True)
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    st.markdown("""<br><br>""", unsafe_allow_html=True)
    # Add an expander (accordion) with HTML content
    with st.expander("Click to expand"):
        html_content = """
        <h3>This is a Heading</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <br>
        <h3>This is a Heading</h3>
        <ul>
            <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
            <li>Nullam vehicula justo eu lacinia mollis.</li>
            <li>Vestibulum placerat lorem quis leo accumsan laoreet.</li>
            <li>Proin sed nulla venenatis, finibus elit non, cursus elit.</li>
            <li>Mauris euismod tellus a mi pharetra rhoncus.</li>
            <li>Fusce rutrum lacus nec mauris aliquet, vitae volutpat risus lacinia.</li>
            <li>Fusce eget diam aliquam, tempor augue vel, placerat lacus.</li>
        </ul>
        <br>
        <h3>This is a Heading</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <br>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        
    st.markdown("""<hr>""", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="flex-center ai-default-text">
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="60" height="60" x="0" y="0" viewBox="0 0 32 32" style="enable-background:new 0 0 512 512" xml:space="preserve" class=""><rect width="32" height="32" rx="6.4" ry="6.4" fill="#09241f" shape="rounded" transform="matrix(0.99,0,0,0.99,0.16000000000000014,0.16000000000000014)"></rect><g transform="matrix(0.7,0,0,0.7,4.800000000000001,4.800000000000001)"><path d="M19 6a3 3 0 0 1-2 2.82c-.31.12-.65.18-1 .18s-.69-.06-1-.18A3 3 0 0 1 13 6c0-1.65 1.35-3 3-3s3 1.35 3 3zm7 9v11c0 1.65-1.35 3-3 3H9c-1.65 0-3-1.35-3-3V15c0-1.65 1.35-3 3-3h6v-1.1c.32.07.66.1 1 .1s.68-.03 1-.1V12h6c1.65 0 3 1.35 3 3zm-14 4.5c.83 0 1.5-.67 1.5-1.5s-.67-1.5-1.5-1.5-1.5.67-1.5 1.5.67 1.5 1.5 1.5zm7.8 2.9c-.33-.44-.96-.53-1.4-.2-.93.7-1.9.8-2.4.8-1.16 0-2-.5-2.4-.8-.44-.33-1.07-.24-1.4.2s-.24 1.07.2 1.4c.6.45 1.86 1.2 3.6 1.2.75 0 2.21-.16 3.6-1.2.44-.33.53-.96.2-1.4zm1.7-4.4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5.67 1.5 1.5 1.5 1.5-.67 1.5-1.5zM4 16c-1.103 0-2 .897-2 2v5c0 1.103.897 2 2 2zm24 0v9c1.103 0 2-.897 2-2v-5c0-1.103-.897-2-2-2z" fill="#307f71" opacity="1" data-original="#000000" class=""></path></g></svg>
            </div>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
        """, unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown ("""<p class="card-border">You gain life and enemy loses life</p>""",unsafe_allow_html=True)

        with col2:
            st.markdown ("""<p class="card-border">Vampires cards with flying ability</p>""",unsafe_allow_html=True)

        with col3:
            st.markdown ("""<p class="card-border">Blue and green colored sorcery cards</p>""",unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown ("""<p class="card-border">White card with protection from black</p>""",unsafe_allow_html=True)

        with col2:
            st.markdown ("""<p class="card-border">The famous 'Black Lotus' card</p>""",unsafe_allow_html=True)

        with col3:
            st.markdown ("""<p class="card-border">Wizard card with Vigiliance ability</p>""",unsafe_allow_html=True)

    st.markdown(
        """
        <div class="flex-center user-command">
            <div>
                <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="50" height="50" x="0" y="0" viewBox="0 0 20 21" style="enable-background:new 0 0 512 512" xml:space="preserve" class=""><rect width="20" height="21" rx="4" ry="4" fill="#307f71" shape="rounded" transform="matrix(0.99,0,0,0.99,0.09999999999999964,0.10500000000000043)"></rect><g transform="matrix(0.7,0,0,0.7,3,3.261900007724763)"><g fill="#000"><path d="M2 18a5.127 5.127 0 0 1 5.127-5.127h5.746A5.127 5.127 0 0 1 18 18c0 1.168-.79 2.182-1.943 2.373-1.442.24-3.582.5-6.057.5-2.475 0-4.615-.26-6.057-.5C2.791 20.183 2 19.168 2 18zM5 5.873a5 5 0 1 1 10 0 5 5 0 0 1-10 0z" fill="#09241f" opacity="1" data-original="#000000" class=""></path></g></g></svg>
            </div>
            <p>I need Image with text</p>
        </div>
        """, unsafe_allow_html=True)
    with st.container():
        st.markdown(
            """
            <div class="flex-center ai-generated">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="50" height="50" x="0" y="0" viewBox="0 0 32 32" style="enable-background:new 0 0 512 512" xml:space="preserve" class=""><rect width="32" height="32" rx="6.4" ry="6.4" fill="#09241f" shape="rounded" transform="matrix(0.99,0,0,0.99,0.16000000000000014,0.16000000000000014)"></rect><g transform="matrix(0.7,0,0,0.7,4.800000000000001,4.800000000000001)"><path d="M19 6a3 3 0 0 1-2 2.82c-.31.12-.65.18-1 .18s-.69-.06-1-.18A3 3 0 0 1 13 6c0-1.65 1.35-3 3-3s3 1.35 3 3zm7 9v11c0 1.65-1.35 3-3 3H9c-1.65 0-3-1.35-3-3V15c0-1.65 1.35-3 3-3h6v-1.1c.32.07.66.1 1 .1s.68-.03 1-.1V12h6c1.65 0 3 1.35 3 3zm-14 4.5c.83 0 1.5-.67 1.5-1.5s-.67-1.5-1.5-1.5-1.5.67-1.5 1.5.67 1.5 1.5 1.5zm7.8 2.9c-.33-.44-.96-.53-1.4-.2-.93.7-1.9.8-2.4.8-1.16 0-2-.5-2.4-.8-.44-.33-1.07-.24-1.4.2s-.24 1.07.2 1.4c.6.45 1.86 1.2 3.6 1.2.75 0 2.21-.16 3.6-1.2.44-.33.53-.96.2-1.4zm1.7-4.4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5.67 1.5 1.5 1.5 1.5-.67 1.5-1.5zM4 16c-1.103 0-2 .897-2 2v5c0 1.103.897 2 2 2zm24 0v9c1.103 0 2-.897 2-2v-5c0-1.103-.897-2-2-2z" fill="#307f71" opacity="1" data-original="#000000" class=""></path></g></svg>
                </div>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            </div>
            """, unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("img/image-1.jpg", caption="Sunrise by the mountains")

        with col2:
            st.image("img/image-1.jpg", caption="Sunrise by the mountains")

        with col3:
            st.image("img/image-1.jpg", caption="Sunrise by the mountains")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("img/image-1.jpg", caption="Sunrise by the mountains")

        with col2:
            st.image("img/image-1.jpg", caption="Sunrise by the mountains")

        with col3:
            st.image("img/image-1.jpg", caption="Sunrise by the mountains")

    st.markdown("""<hr>""", unsafe_allow_html=True)
    with st.chat_message("user"):
        st.write("Hello 👋")
        st.line_chart(np.random.randn(30, 3))
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        
