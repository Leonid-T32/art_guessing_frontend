import streamlit as st

page_icon = './images/title-img.png'
pic_width = 100

st.set_page_config(layout='wide',
                   page_title='Art Guessing / Behind the scenes',
                   page_icon='🎨',
                   initial_sidebar_state="auto")

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

# Markdown textblock separator - return and thin line
st.markdown('---')


# Textblock2
st.markdown('''
                ## Approach & model - next CNN topmodel?
                To solve the challenging task of predicting art styles, we used the **deep learning (DL)** method in which **convolutional neural networks (CNNs)** are built to analyze large datasets.
                First, we tested our **own neural models**, setting up new neural layers from scratch.
                However, computationally and accuracy-wise, they did not perform well.
                As a consequence, we switched our strategy to **transfer learning**, which means that we applied neural models that were already tested on general image identification problems.
                To the core layers of these models, we then added our own final dense layers adapted to our dataset.
                Overall, we tested different models: VGG-16, ResNet50, EfficientNet-B1, EfficientNet-B2, and EfficientNet-B7.
                In general, it seems that EfficientNet models show high performance related to image identification, as shown in this link: [https://pypi.org/project/efficientnet/](https://pypi.org/project/efficientnet/).
                **For our dataset the best performing model was EfficientNetB2**, which we finally implemented in our application.
                For more details, please see the figure below.
                ''')

st.markdown(' ')
st.markdown(' ')

# Textblock2 - Picture2:
st.image('./images/modelworkflow.png', width=1000, use_column_width=False)
