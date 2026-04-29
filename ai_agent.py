import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="OPENAI_API_KEY")

st.title("AI Meeting Prep Agent")

company = st.text_input("Company Name")
meeting = st.selectbox("Meeting Type", ["Discovery","Renewal","Executive","Follow-Up"])
notes = st.text_area("Notes")

if st.button("Generate Prep"):

    prompt = f"""
You are an enterprise sales meeting prep assistant.

Prepare a seller for a meeting.

Company: {company}
Meeting Type: {meeting}
Notes: {notes}

Return:

1. Company Summary
2. Relationship Summary
3. Risks
4. 5 Smart Questions
5. Recommended Positioning
6. Follow-up Email
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    st.write(response.choices[0].message.content)
