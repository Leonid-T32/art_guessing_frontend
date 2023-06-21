import streamlit as st

st.set_page_config(layout='wide',
                   page_title='Art Guessing / About project',
                   page_icon='🎨',
                   initial_sidebar_state="auto")

# Textblock1
st.markdown('''
                ## I think I know this art style...  or do I?
                Imagine the situation that you are in a location with other people, for example a party or reception, where several paintings of different artists are exhibited. 
                You sure know the feeling "Wait, I know that art style or maybe the artist but not the style. Or do I? Hmmm... I am not really sure".
                
                Other people seem to be very sure although some of their guesses you know already are actually quite wrong.
                Or, even worth, they fight over who is right or wrong, families are devided, couples split...
                
                Well, our application ARTEND comes in handy now.
                You can load pictures into it by either uploading them from the web or by photographing them with your mobile phone and ARTEND predicts the style for you.
                Isn't that marvelous? Now you can be more confident on your hunch. Of course you can also guess yourself the stlye before ARTEND predicts the style so you can see if you were right. 
                Or, why don't you use it as a party game and be the good samaritian who keeps families and couples together? 
                Socialising with art, but doing it smart. What a great time.


                We have already many ideas how to improve and modify ARTEND and its neural network model that does all the work in the background in the future, please see for perspectives on the "about us" page. 
                ''')

# Textblock1 - Picture1:
st.image('./images/cartoon.png', width=800, use_column_width=False)