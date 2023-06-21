import streamlit as st

st.set_page_config(layout='wide',
                   page_title='Art Guessing / Behind the scenes',
                   page_icon='🎨',
                   initial_sidebar_state="auto")

# Logo:
st.image('./images/LogoFinal.png', width=250, use_column_width=False)
st.markdown(' ')

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
st.image('./images/modelworkflow.png', width=800, use_column_width=False)
