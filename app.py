import streamlit as st
import os
import re
from dotenv import load_dotenv
from google import genai
from prompt import create_prompt

# ----------------------------
# Load Gemini API Key
# ----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("🌍 AI Travel Planner")
st.write("Plan your dream vacation with the power of Gemini AI!")

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:

    st.header("🧳 Trip Details")

    destination = st.text_input(
        "📍 Destination",
        placeholder="Example: Goa"
    )

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=3
    )

    budget = st.number_input(
        "💰 Budget (₹)",
        min_value=1000,
        max_value=500000,
        value=10000,
        step=1000
    )

    travel_style = st.selectbox(
        "✈ Travel Style",
        [
            "Budget",
            "Luxury",
            "Family",
            "Solo",
            "Adventure"
        ]
    )

    interests = st.multiselect(
        "❤️ Interests",
        [
            "Food",
            "Shopping",
            "Adventure",
            "Nature",
            "History",
            "Beaches",
            "Wildlife",
            "Photography"
        ]
    )
col1,col2,col3=st.columns(3)

col1.metric("💰 Budget",f"₹{budget}")

col2.metric("📅 Days",days)

col3.metric("✈ Style",travel_style)
# ----------------------------
# Show Selected Budget
# ----------------------------

# ----------------------------
# Generate Button
# ----------------------------
if st.button("🚀 Generate Trip"):

    if destination.strip() == "":
        st.warning("Please enter a destination.")

    elif len(interests) == 0:
        st.warning("Please select at least one interest.")

    else:

        prompt = create_prompt(
            destination,
            days,
            budget,
            travel_style,
            interests
        )

        try:

            with st.spinner("🤖 Gemini AI is planning your trip..."):

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

            st.success("✅ Trip Generated Successfully!")


            # ----------------------------
            # Display Itinerary
            # ----------------------------
            st.markdown("---")
            formatted_text = response.text

# Bold main headings
            formatted_text = re.sub(
    r"^# (.*)$",
    r"<h1 style='color:#1565C0;'>\1</h1>",
    formatted_text,
    flags=re.MULTILINE,
)

            formatted_text = re.sub(
    r"^## (.*)$",
    r"<h2 style='color:#00897B;'>\1</h2>",
    formatted_text,
    flags=re.MULTILINE,
)

            formatted_text = formatted_text.replace("---", "<hr>")

            #st.markdown(formatted_text, unsafe_allow_html=True)
            st.markdown(response.text)
            # ----------------------------
            # Download Button
            # ----------------------------
            st.download_button(
                label="📄 Download Travel Plan",
                data=response.text,
                file_name=f"{destination}_travel_plan.txt",
                mime="text/plain"
            )

        except Exception as e:

            st.error(f"❌ Error: {e}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")

st.markdown(
    """
    <center>
    Made with ❤️ using <b>Streamlit</b> + <b>Google Gemini AI</b>
    </center>
    """,
    unsafe_allow_html=True
)