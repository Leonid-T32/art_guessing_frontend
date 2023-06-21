import streamlit as st

st.set_page_config(layout='wide',
                   page_title='Art Guessing / Dataset',
                   page_icon='🎨',
                   initial_sidebar_state="auto")

# Logo:
st.image('./images/LogoFinal.png', width=250, use_column_width=False)
st.markdown(' ')

# Textblock1
st.markdown('''
                ## Our dataset - art spotlight on
                **ArtBench-10** is a dataset of **60,000 image** from **10 art styles** that are extracted from the Wikiart database.
                These 10 styles are selected based on the balanced number of pictures available (5,000 for training and 1,000 for testing) which is an advantage over the highly imbalanced Wikiart data.
                
                In general, it is actually **difficult to create large, balanced datasets** because many styles are not well represented.
                We thus chose ArtBench-10 to train our neural network model to avoid model mistraining because of long-tail class distribution.
                The ten art styles with example paintings are shown below.
                
                If you like to know more about the WikiArt and the ArtBench-10 datasets, please follow these links that provide more detailed information:
                ("- [https://www.kaggle.com/datasets/steubk/wikiart](https://www.kaggle.com/datasets/steubk/wikiart)") and
                ("- [https://www.kaggle.com/datasets/alexanderliao/artbench10](https://www.kaggle.com/datasets/alexanderliao/artbench10)")
                ''')

st.markdown(' ')
st.markdown(' ')

# Textblock1 - Picture1:
st.image('./images/artstyles.png', width=1000, use_column_width=False)

