import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import matplotlib.pyplot as plt
import numpy as np

wiki_url = 'https://en.wikipedia.org/w/api.php'
api_url = 'https://service-art-guessing-l6hzosl6eq-ew.a.run.app' # 'http://0.0.0.0:8000'
api_img_endpoint = '/upload_image'
title_img_path = './images/title-img.jpg'
padding = 0
img_mod_size = 256
img = None
uploaded_file = None

# these are params for the wiki request
PARAMS = {
        "action": "opensearch",
        "namespace": "0",
        "search": 'some_style', # to exchange before query
        "limit": "5",
        "format": "json"}

api_response = None

styles = ('art nouveau',
            'baroque',
            'expressionism',
            'impressionism',
            'post-impressionism',
            'realism',
            'renaissance',
            'romanticism',
            'surrealism',
            'ukiyo-e')

st.title('Guess the arts')
title_img = Image.open(title_img_path)
st.image(title_img, width=100)

pred_col1, pred_col2 = st.columns(2)
st.divider()

with pred_col1:
    st.subheader('Choose your pic!')
    uploaded_file = st.file_uploader(' ', accept_multiple_files=False, label_visibility='collapsed')
    st.divider()
    st.subheader('Make your guess!')
    guessed_style = st.radio('options', styles, label_visibility='collapsed')
    st.divider()
    padding = st.slider('Set padding!', min_value=0, max_value=100, value=50, step=10, format=None, disabled=False, label_visibility="visible")
    if uploaded_file != None:
        img = Image.open(uploaded_file)
        #crop and downsize the image
        width, height = img.size
        diff = np.abs(width - height)
        if width != height: #crop if image is not square
            if width > height:
                if padding >= height/2: padding = 0 #set padding 0 to prevent cut of whole image
                l = diff/2 + padding
                r = l + height - 2*padding
                t = 0 + padding
                b = height - padding
            elif width < height:
                if padding >= width/2: padding = 0 #set padding 0 to prevent cut of whole image
                l = 0 + padding
                r = width - padding
                t = diff/2 + padding
                b = t + width - 2*padding
            img = img.crop((l,t,r,b))
        if img_mod_size < img.size[0] and img_mod_size < img.size[1]:
            img = img.resize((img_mod_size, img_mod_size))
        st.image(img, width=100)
        st.subheader('Test your knowlede!')
        if st.button('Click me!'):
            if img != None:
                with st.spinner('Be patient ... we are asking ChatGPT'):
                    st.divider()
                    # transfer image to bytes
                    output = BytesIO()
                    img.save(output, format='JPEG')
                    img_bytes = output.getvalue()
                    files = {'file': BytesIO(img_bytes)}
                    # make request to the API
                    api_response = requests.post(api_url + api_img_endpoint, files=files) #img_bytes})

                    classified_style = api_response.json()['style']

                    if api_response!= None and api_response.status_code == 200:
                        if guessed_style == classified_style:
                            st.subheader(f'Well done! It is {classified_style}! You are the king of the arts!')
                            st.balloons()
                        else:
                            st.subheader(f'Are you kidding me? Go home and study arts!')
                            st.snow()
                            PARAMS['search'] = guessed_style
                            res = requests.get(url=wiki_url, params=PARAMS).json()
                            st.write(res[3][0])
                    else:
                        st.write(f'api responded with: {api_response}')
            else:
                st.subheader('Please choose your pic first!')

with pred_col2:
    if uploaded_file != None:
        st.image(uploaded_file, width=300)


# this is optional (nice to have)
# with st.expander('Look into the kitchen!'): # show plots or other usefull info behind the wall
