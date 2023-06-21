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
                Imagine, **you are with other people on a party or receptio**, where several **paintings of different artists are exhibited**. 
                You sure know the feeling "Wait, I know that art style. Or do I? Hmmm... I am not really sure".
                Others seem to be very sure about the art style although some of their guesses appear quite bold. 
                Some even fight over who is right or wrong, families are devided, couples split - this is when art is hard.
                
                Well, **our application **ARTEND** comes in handy now**.
                You can load pictures into it by either uploading them from the web or by photographing them with your mobile phone and **ARTEND predicts the style for you**.
                Isn't that marvelous? Now **you can be more confident on your hunch**. Of course you can guess yourself the style before **ARTEND** predicts it so you can see if you were right. 
                Or, why don't you **use it as a party game** and be the good samaritan who keeps families and couples together? 
                **Socialising with art, but doing it smart**. What **a jolly time**!


                We have already many ideas how to improve and modify **ARTEND** and its neural network model that does all the work in the background in the future, **please see for perspectives the "about us" page**. 
                ''')

# Textblock1 - Picture1:
st.image('./images/cartoon.png', width=800, use_column_width=False)