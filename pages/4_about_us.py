import streamlit as st

pic_width = 100


st.set_page_config(layout='wide',
                   page_title='Art Guessing / About us',
                   page_icon='🎨',
                   initial_sidebar_state="auto")

# Logo:
st.image('./images/LogoFinal.png', width=250, use_column_width=False)
st.markdown(' ')

# col1, col2 = st.columns([0.4, 0.6])

# with col1:
st.markdown('''
                ## About Art Guessing
                This web app is brought to you by a group of students of the [**Data Science and Machine Learning course** at **Le Wagon**](https://www.lewagon.com/data-science-course).
                We came up with this idea to categorise artwork ourselves, and were excited to spend two weeks working on a neural network that would be able to predict with confidence the art style of any artwork it was given,
                and an intuitive, fun front-end for our project so users could interact with it.
                Having graduated from the bootcamp, we now look forward to applying the knowledge we've acquired in our next professional opportunities.
                We welcome questions and feedback, **please feel free to reach out to any of us** using the e-mail addresses below.
                ''')

# Markdown textblock separator - return and thin line
st.markdown('---')


# First Row
col1, col2, col3 = st.columns(3)

with col1:
    st.image('./images/Eliza.jpg', width=pic_width)
    st.markdown('''
                **Eliza Belmain:**\n
                elisa.belmain@gmail.com
                ''')

with col2:
    st.image('./images/Laila.jpg', width=pic_width)
    st.markdown('''
                **Laila Dib:**\n
                lailadib@gmail.com
                ''')

with col3:
    st.image('./images/Leonid.jpg', width=pic_width)
    st.markdown('''
                **Leonid Tafler:**\n
                leonid.tafler@gmail.com
                ''')

# Second Row
col4, col5 = st.columns([0.36, 0.74])

with col4:
    st.image('./images/Onur.jpg', width=pic_width)
    st.markdown('''
                **Onur Özcan:**\n
                ozcan-onur@hotmail.com
                ''')

with col5:
    st.image('./images/Bjoern.jpg', width=pic_width)
    st.markdown('''
                **Björn von Reumont:**\n
                bmvr@reumont.net
                ''')

# Markdown textblock separator - return and thin line
st.markdown('---')

st.markdown('''
            ## GitHub
            * https://github.com/lailadib/art_guessing
            * https://github.com/Leonid-T32/art_guessing_frontend
            ''')

# Markdown textblock separator - return and thin line
st.markdown('---')

st.markdown('''
            ## Future plans
            The first technical endeavour we would embark on would be improving the prediction accuracy of our app by **training a more specific convolutional neural network model** to take over the work behind the scenes.
            Art styles are actually harder to predict than you probably imagine, so longer training and/or new training of transfer models could probably increase the precision.

            Other ideas we have include building a model that will **predict the artist** rather than the art style. That would be a nice additional feature after we've improved the original model.
            We've also discussed building a new model which would take an artwork as input and return **the artwork and/or artist it identifies as most similar**.
            ''')
