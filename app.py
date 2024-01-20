import streamlit as st


st.header("Recruitment Covenant Form Hiring - 2024-25")

st.subheader("To")
st.subheader("The Talent Acquisition Team,")
st.subheader("We request you to kindly help us with filling this covenant form to enable us to shortlist most relevant candidates for the selection process. Thank you so much for your support and we look forward to build an effective and prolific association")
st.subheader("Thanking you,")
st.subheader("Corporate Relations Team  Anudip Foundation")


x=st.text_input("Name of the Employer","type here")

if st.button('Submit Name'):
    r=x.title()
    st.success(r)


y=st.text_input("Name of the Representative","type here")

if st.button('Submit Representative'):
    a=y.title()
    st.success(a)


d=st.text_input("Designation","type here")

if st.button('Submit Designation'):
    c=d.title()
    st.success(c)

st.text("Please put a check mark against the hiring role and number of vacancies")

level=st.slider("Customer Support / Remote Technology / System / Software Support (Chat, Email and Web)  NON VOICE",10,100)

level1=st.slider("Customer Care/Process Associate Domestic or International  VOICE Support Technology",10,100)

level2=st.slider("Software - Engineer, Jr. Developer, Developer, UI-UX engineer",10,100)

level3=st.slider("Cloud Engineer or Cloud Support /AWS",10,100)

level4=st.slider("Dev-Ops Engineer / Support",10,100)

level5=st.slider("Data Analyst & Data Support",10,100)

level6=st.slider("Data Visualizer",10,100)

level7=st.slider("Website Developer",10,100)

level8=st.slider("Web Designer / Graphic Designer",10,100)

level9=st.slider("Hardware Associate (Or related)",10,100)

level10=st.slider("Networking Engineer (Or related)",10,100)






