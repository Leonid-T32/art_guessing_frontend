import streamlit as st

st.set_page_config(layout='wide',
                   page_title='Art Guessing / About project',
                   page_icon='🎨',
                   initial_sidebar_state="auto")

# Logo:
st.image('./images/LogoFinal.png', width=250, use_column_width=False)
st.markdown(' ')

# Textblock1
st.markdown('''
                ## I think I know this art style...  or do I?
                Imagine, **you are mingling with others at a party or reception**, where several **paintings by different artists are exhibited**.
                You have the familiar feeling of "Wait, I know that art style. Or do I? Hmmm... I am not really sure".
                Others seem overly confident about the art style, but some of their guesses appear quite bold.
                Some even fight over who's right and who's wrong, families are divided, couples split - this is when art is hard.

                Well, **our application **ARTEND** comes in handy now!**.
                You can input artworks into it, either by uploading them from the web or by photographing them with your mobile phone, and **ARTEND recognises the style for you**.
                Isn't that marvellous? Now **you can be more confident on your hunch**. Of course, you can submit your own guess before **ARTEND** predicts the style so you can see if you were right.
                Or why not **use it as a party game**, become the good Samaritan who keeps families and couples together?
                **Socialising with art, but doing it smart**. What **a jolly time**!

                While we love the app we've been able to build in two weeks, we already have a list of ideas on how to improve and further **ARTEND**. For more on the future of our app and its neural network model, **please see the "about us" page**.
                ''')

# Textblock1 - Picture1:
st.image('./images/cartoon.png', width=800, use_column_width=False)
