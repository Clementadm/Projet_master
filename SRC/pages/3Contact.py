import streamlit as st
from ihm.set_page_config import page_config, footer
page_config(initial_sidebar_state="collapsed", layout="centered")
st.markdown(
    """
    <div style='text-align: center;'>
        <h2 style='color: #ffde00;'>📤 Contact Us</h2>
        <p style='color: #ccc; font-size: 17px; max-width: 700px; margin: 0 auto;'>
            Do you have a question, suggestion, or want to integrate <b>TradeHelper</b> into your platform?<br>
            Use the form below to contact our team. We’ll get back to you as soon as possible!
        </p>
    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# Layout
# col1, col2, col3, col4 = st.columns([3, 0.25, 1, 0.25])
col1, col2, col3 = st.columns([0.25, 3, 0.25])

with col2:
    email = st.text_input("📧 Your Email *", value=st.session_state.get('email', ''), key='email')
    topic = st.selectbox("📌 Topic *", ["General Inquiry", "Feedback", "Integration Request", "Technical Issue"], key="topic")
    message = st.text_area("💬 Your Message *", height=200, value=st.session_state.get('message', ''), key='message')

    st.markdown('<p style="font-size: 13px; color: #999;">* Required fields</p>', unsafe_allow_html=True)

    if st.button("📨 Send", type="primary"):
        if not email or not message:
            st.error("🚫 Please fill in all required fields.")
        else:
            # 👇 Logique d'envoi ici (SMTP, SendGrid, stockage...)
            st.success("✅ Message sent successfully! Our team will reach out to you shortly.")

footer()