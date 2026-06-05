import streamlit as st
import requests

# 1. Page Setup
st.set_page_config(
    page_title="Adlytix AI Strategist", page_icon="✨", layout="centered"
)

# 2. The UI Hack (Injecting Black & Gold Glassmorphism CSS)
custom_css = """
<style>
/* Main Dark Background */
.stApp {
    background-color: #0a0a0a;
    background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000000 70%);
    color: #D4AF37;
}

/* Glassmorphism Text Inputs */
.stTextInput>div>div>input {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(212, 175, 55, 0.3) !important;
    color: #FFFFFF !important;
    border-radius: 12px !important;
    backdrop-filter: blur(10px);
    padding: 10px 15px !important;
}

/* Input Focus Glow */
.stTextInput>div>div>input:focus {
    border: 1px solid #D4AF37 !important;
    box-shadow: 0 0 10px rgba(212, 175, 55, 0.3) !important;
}

/* Premium Gold Button */
.stButton>button {
    background: linear-gradient(135deg, #D4AF37 0%, #AA7C11 100%) !important;
    color: #000000 !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
    transition: all 0.3s ease !important;
    width: 100%;
}

/* Button Hover Effect */
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important;
}

/* Markdown Text Styling */
p, .stMarkdown {
    color: #cccccc !important;
}
h1, h2, h3, label {
    color: #D4AF37 !important;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. The Visual Content
st.markdown(
    "<h1 style='text-align: center;'>✨ Adlytix AI Strategist</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; margin-bottom: 30px;'>Generate high-converting Meta Ads strategies powered by deep learning.</p>",
    unsafe_allow_html=True,
)

# Layout Setup (Using columns to make it look structured)
col1, col2 = st.columns(2)
with col1:
    product = st.text_input("📦 Product Name", placeholder="e.g., Luxury Perfume")
with col2:
    audience = st.text_input(
        "🎯 Target Audience", placeholder="e.g., Corporate Executives"
    )

st.markdown("<br>", unsafe_allow_html=True)

# 4. The Logic Execution
if st.button("INITIALIZE STRATEGY ENGINE 🧠"):
    if product and audience:
        with st.spinner("Analyzing market dynamics..."):
            API_URL = "http://127.0.0.1:8000/generate-strategy"
            payload = {"product_name": product, "target_audience": audience}

            try:
                response = requests.post(API_URL, json=payload)
                data = response.json()

                st.success("✅ Strategy Compiled!")
                # Displaying the result inside an emphasized block
                st.info(f"**Targeting:** {data['Product']} ➔ {data['Audience']}")
                st.markdown(data["AI_Strategy"])

            except Exception as e:
                st.error("⚠️ Backend server is offline. Please start FastAPI.")
    else:
        st.warning("⚠️ Parameters incomplete. Awaiting input.")
