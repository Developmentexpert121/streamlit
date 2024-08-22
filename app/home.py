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
                background: #09241f;
                border-radius: 10px;
                margin-bottom: 20px !important;
            }
            [data-testid="stChatInputSubmitButton"] {
                color: #307f71 !important;
            }
            [data-testid="stChatInput"] {
                background: none;
            }
            [data-testid="stChatInput"] [data-baseweb="textarea"] {
                border-color: #307f71;
            }
            [data-testid="stChatInput"] [data-baseweb="textarea"] textarea {
                color: #fff !important;
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
            [data-testid="stChatMessage"] {
                background: #09241f;
                border-radius: 10px;
            }
            [data-testid="stBottom"] > div {
                background: #0f352e;
            }
            [data-testid="stBottom"] [data-testid="stBottomBlockContainer"] {
                max-width: 1000px;
                padding-inline: 40px;
            }
            .ai-default-text > div {
                display: flex;
                width: 3rem;
                height: 3rem;
                flex-shrink: 0;
                border-radius: 0.5rem;
                -webkit-box-align: center;
                align-items: center;
                -webkit-box-pack: center;
                justify-content: center;
                background-color: rgb(255, 189, 69);
            }
            .ai-default-text > div > svg {
                width: 2rem;
                height: 2rem;
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
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" class="eyeqlp53 st-emotion-cache-1pbsqtx ex0cdmw0"><rect width="24" height="24" fill="none"></rect><path d="M20 9V7c0-1.1-.9-2-2-2h-3c0-1.66-1.34-3-3-3S9 3.34 9 5H6c-1.1 0-2 .9-2 2v2c-1.66 0-3 1.34-3 3s1.34 3 3 3v4c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-4c1.66 0 3-1.34 3-3s-1.34-3-3-3zm-2 10H6V7h12v12zm-9-6c-.83 0-1.5-.67-1.5-1.5S8.17 10 9 10s1.5.67 1.5 1.5S9.83 13 9 13zm7.5-1.5c0 .83-.67 1.5-1.5 1.5s-1.5-.67-1.5-1.5.67-1.5 1.5-1.5 1.5.67 1.5 1.5zM8 15h8v2H8v-2z"></path></svg>
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

    # st.markdown("""<hr>""", unsafe_allow_html=True)
    # with st.chat_message("user"):
    #     st.write("Hello 👋")
    #     st.line_chart(np.random.randn(30, 3))
    # prompt = st.chat_input("Say something")
    # if prompt:
    #     st.write(f"User has sent the following prompt: {prompt}")
    # prompt = st.chat_input("Say something")
    # if prompt:
    #     st.write(f"User has sent the following prompt: {prompt}")

    prompt = st.chat_input("Say something")
    messages = st.container()
    if prompt:
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
    # with st.container():
    #     messages = st.container()
    #     if prompt := st.chat_input("Say something"):
    #         messages.chat_message("user").write(prompt)
    #         messages.chat_message("assistant").write(f"Echo: {prompt}")
            
