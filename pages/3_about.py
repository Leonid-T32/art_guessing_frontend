import streamlit as st

page_icon = './images/title-img.png'
pic_width = 100

st.set_page_config(layout='wide',
                   page_title='Art Guessing / about',
                   page_icon=page_icon,
                   initial_sidebar_state="auto")

col1, col2 = st.columns([0.4, 0.6])

with col1:
    st.markdown('''
                ## About Art Guessing
                This web app is brought to you by a group of students of Data Science and Machine Learning at Le Wagon.
                We came up with this idea to categorise artwork ourselves, and were excited to spend two weeks working on a neural network that would be able to predict with confidence the art style of any artwork it was given,
                and an intuitive, fun front-end for our project so users could interact with it.
                Having graduated from the bootcamp, we now look forward to applying the knowledge we've acquired in our next professional opportunities.
                We welcome questions and feedback, please feel free to reach out to any of us using the e-mail addresses below.
                ''')
with col2:
    st.write(' ')

with st.container():
    st.markdown('## Developer')

    with st.container():
        st.image('./images/Eliza.jpg', width=pic_width)
        st.markdown('**Eliza Belman:** elisa.belmain@gmail.com')

    with st.container():
        st.image('./images/Laila.jpg', width=pic_width)
        st.markdown('**Laila Scur Dib:** lailadib@gmail.com')

    with st.container():
        st.image('./images/Leonid.jpg', width=pic_width)
        st.markdown('**Leonid Tafler:** leonid.tafler@gmail.com')

    with st.container():
        st.image('./images/Onur.jpg', width=pic_width)
        st.markdown('**Onur Özcan:** ozcan-onur@hotmail.com')

    with st.container():
        st.image('./images/Bjoern.jpg', width=pic_width)
        st.markdown('**Böjrn von Reumont:** bmvr@reumont.net')

st.markdown('''
            ## GitHub
            * https://github.com/lailadib/art_guessing
            * https://github.com/Leonid-T32/art_guessing_frontend
            ''')
