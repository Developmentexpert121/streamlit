import streamlit as st

def display_signin():
    # Inject custom CSS
    st.markdown(
        """
        <style>
        [data-testid="stVerticalBlock"] {
            max-width: 600px;
            margin: auto;
        }
        p, h1, h2, h3, h4, h5, h6, div, body {
            color: #fff;
        }
        .google-signin-btn {
            border: 0;
            padding: 10px 20px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            margin-inline: auto;
            background: #fff;
            color: #000;
            cursor: pointer;
            font-size: 16px;
        }
        .google-signin-btn svg {
            fill: #000;
            margin-right: 8px;
        }
        .signin-content {
        text-align:center;}
        [data-testid="stMarkdownContainer"] {
            margin-bottom:0;
        }
        [data-testid="stForm"] {
    background: #09241f;
    border-radius: 20px;
    padding: 25px;
}
.term-privacy-links {
    margin-top: 30px
}
        </style>
        """,
        unsafe_allow_html=True
    )

    # st.title("Sign In")

    # Create a placeholder for the button
    placeholder = st.empty()

    # Insert a form in the container
    with placeholder.form("login"):
        # Add the SVG directly to the button
        st.markdown (
            """
            <div class="signin-content">
                <h2>Welcome to Stramlit</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>

            """
        , unsafe_allow_html=True)
        st.markdown(
            """
            <button type="submit" class="google-signin-btn">
                <svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24" x="0" y="0" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512" xml:space="preserve" class="icon">
                    <g>
                        <path d="m492.668 211.489-208.84-.01c-9.222 0-16.697 7.474-16.697 16.696v66.715c0 9.22 7.475 16.696 16.696 16.696h117.606c-12.878 33.421-36.914 61.41-67.58 79.194L384 477.589c80.442-46.523 128-128.152 128-219.53 0-13.011-.959-22.312-2.877-32.785-1.458-7.957-8.366-13.785-16.455-13.785z" style="" fill="#167ee6" data-original="#167ee6" class=""></path>
                        <path d="M256 411.826c-57.554 0-107.798-31.446-134.783-77.979l-86.806 50.034C78.586 460.443 161.34 512 256 512c46.437 0 90.254-12.503 128-34.292v-.119l-50.147-86.81c-22.938 13.304-49.482 21.047-77.853 21.047z" style="" fill="#12b347" data-original="#12b347"></path>
                        <path d="M384 477.708v-.119l-50.147-86.81c-22.938 13.303-49.48 21.047-77.853 21.047V512c46.437 0 90.256-12.503 128-34.292z" style="" fill="#0f993e" data-original="#0f993e"></path>
                        <path d="M100.174 256c0-28.369 7.742-54.91 21.043-77.847l-86.806-50.034C12.502 165.746 0 209.444 0 256s12.502 90.254 34.411 127.881l86.806-50.034c-13.301-22.937-21.043-49.478-21.043-77.847z" style="" fill="#ffd500" data-original="#ffd500"></path>
                        <path d="M256 100.174c37.531 0 72.005 13.336 98.932 35.519 6.643 5.472 16.298 5.077 22.383-1.008l47.27-47.27c6.904-6.904 6.412-18.205-.963-24.603C378.507 23.673 319.807 0 256 0 161.34 0 78.586 51.557 34.411 128.119l86.806 50.034c26.985-46.533 77.229-77.979 134.783-77.979z" style="" fill="#ff4b26" data-original="#ff4b26"></path>
                        <path d="M354.932 135.693c6.643 5.472 16.299 5.077 22.383-1.008l47.27-47.27c6.903-6.904 6.411-18.205-.963-24.603C378.507 23.672 319.807 0 256 0v100.174c37.53 0 72.005 13.336 98.932 35.519z" style="" fill="#d93f21" data-original="#d93f21"></path>
                    </g>
                </svg>
                <span>Sign in with Google</span>
            </button>
            <div class="signin-content term-privacy-links">
                <p>By registration you agree to <a href="#">Term of Use</a> and <a href="#">Privacy Policy</a>.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown (
            """
            

            """
        , unsafe_allow_html=True)
        # Handle form submission
        # submit = st.form_submit_button("Sign in with Google")
        # if submit:
        #     st.warning("Google sign-in is not yet implemented.")
