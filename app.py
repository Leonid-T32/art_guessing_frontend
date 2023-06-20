import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
from io import BytesIO
import requests
import matplotlib.pyplot as plt
import numpy as np

params = {
    "css_file": './app.css',
    "wiki_url": 'https://en.wikipedia.org/w/api.php',
    "api_url": 'https://service-art-guessing-l6hzosl6eq-ew.a.run.app/', # 'http://0.0.0.0:8000'
    "api_img_endpoint": '/upload_image',
    "title_img_path": './images/title-img.jpg',
    "padding": 0,
    "img_mod_size": 256,
    "img": None,
    "uploaded_file": None,
    "url_with_pic": None,
    "show": False,
    "bytes_data": None,
    "img_file_buffer": None,
    "api_response": None,
    "styles": ('art_nouveau',
            'baroque',
            'expressionism',
            'impressionism',
            'post-impressionism',
            'realism',
            'renaissance',
            'romanticism',
            'surrealism',
            'ukiyo_e')
}

WIKI_PARAMS = {
        "action": "opensearch",
        "namespace": "0",
        "search": 'some_style', # to exchange before query
        "limit": "5",
        "format": "json"}

st.set_page_config(layout='wide',
                   page_title='Art guessing',
                   page_icon='./images/banner.jpg',
                   initial_sidebar_state= "collapsed",
                )

def local_css(css_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css(params["css_file"])

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


def input_art():
    with grid[0][0]:
        option = st.radio('Your options:', ('File', 'Link', 'Camera'))

        if option == 'File':
            uploaded_file = st.file_uploader(' ', accept_multiple_files=False, label_visibility='hidden')
            if uploaded_file:
                img = Image.open(uploaded_file)
                return img
        elif option == 'Link':
            url_with_pic = st.text_input('Artwork URL:')
            if url_with_pic :
                response = requests.get(url_with_pic)
                img = Image.open(BytesIO(response.content))
                return img
        elif option == 'Camera':
            img_file_buffer = st.camera_input('Take a picture')
            if img_file_buffer is not None:
                img = Image.open(img_file_buffer)
                return img
    return None

def process_image(img):
    if params['img_mod_size'] < img.size[0] and params['img_mod_size'] < img.size[1]:
        img = img.resize((params['img_mod_size'], params['img_mod_size']))
        grid[0][1].image(img, width=256)
    return img


def guess_it(img):
    grid[0][2].markdown( f'<h4>Guess the style!</h4>',
        unsafe_allow_html=True
        )
    guessed_style = grid[0][2].radio('options', params['styles'], label_visibility='collapsed')
    if grid[0][2].button('Click me!'):
        if img != None:
            classified_style = classify_art_style(img)
            if guessed_style == classified_style:
                grid[1][2].subheader(f'Well done! It is {classified_style}! You are the king of the arts!')
                grid[1][2].balloons()
            else:
                grid[1][2].subheader(f'Are you kidding me? Go home and study arts!')
                grid[1][2].snow()
                WIKI_PARAMS['search'] = guessed_style
                res = requests.get(url=params["wiki_url"], params=WIKI_PARAMS).json()
                grid[1][2].write(res[3][0])

def classify_art_style(img):
    with st.spinner('Hold on while we ask ChatGPT... Just kidding!'):
        # transfer image to bytes
        output = BytesIO()
        img.save(output, format='JPEG')
        img_bytes = output.getvalue()
        files = {'file': BytesIO(img_bytes)}
        # make request to the API
        api_response = requests.post(params['api_url'] + params['api_img_endpoint'], files=files) #img_bytes})
<<<<<<< HEAD
        print(api_response)
=======
>>>>>>> e311e05c230b13b00a0416ddbba12aa941bf2763
        classified_style = api_response.json()[0]['style']
        return classified_style

#Grid n1 - top of the page
top = make_grid(2,2)

top[0][0].markdown(
    f"<h2 style='text-align: justify; color: #DCBF9Cff; bottom-padding: 1em;'>Make your educated guess on art</h2>",
    unsafe_allow_html=True
)
top[0][0].markdown(
    f"<h4 style='text-align: justify; color: #738881ff; bottom-padding: 0.5em;'>We know how hard it can be to keep different art styles in mind and categorise the artworks you're looking at, so we've built a predictive model that can help you out when you're not so sure.</h4>",
    unsafe_allow_html=True

)
top[0][0].markdown(
    f"<h5 style='text-align: justify; color: #738881ff; bottom-padding: 0.5em;'>Feel free to upload the artwork as a file, paste the URL to it, or use your camera to snap a picture of it. We'll tell you our best guess at the art style of the artwork you've submitted. Happy guessing!</h5>",
    unsafe_allow_html=True

)
top[0][1].image(image='./images/banner.jpg', use_column_width='always')

#Grid n2 - rest of the page
grid = make_grid(3,(1,3,1))

grid[0][0].markdown( f'<h4>Select and upload artwork</h4>',
        unsafe_allow_html=True
    )

img = input_art()
cropped_image = None
if img is not None:
    with grid[0][1]:
        cropped_image = st_cropper(img, aspect_ratio=(1, 1))
if cropped_image:
    processed = process_image(cropped_image)
    with grid[1][1]:
        st.image(processed)
    print(processed.size)
    guess_it(processed)
