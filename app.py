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
    "image_format": (
            'image/jpg',
            'image/jpeg',
            'image/webp'
    ),
    "styles": {
            'Art nouveau': 'art_nouveau',
            'Baroque': 'baroque',
            'Expressionism': 'expressionism',
            'Impressionism': 'impressionism',
            'Post-impressionism': 'post_impressionism',
            'Realism': 'realism',
            'Renaissance': 'renaissance',
            'Romanticism': 'romanticism',
            'Surrealism': 'surrealism',
            'Ukiyo-e': 'ukiyo_e'
    }
}

WIKI_PARAMS = {
        "action": "opensearch",
        "namespace": "0",
        "search": 'some_style', # to exchange before query
        "limit": "5",
        "format": "json"}

st.set_page_config(layout='wide',
                   page_title='Art guessing',
                   page_icon='🎨',
                   initial_sidebar_state= "collapsed",
                )

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

def local_css(css_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css(params["css_file"])

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows, gap="large")
    return grid

def input_art():
    with grid[0][0]:
        option = st.radio('Your options:', ('File', 'Link', 'Camera'))

        if option == 'File':
            uploaded_file = st.file_uploader(' ', accept_multiple_files=False, label_visibility='hidden')
            if uploaded_file:
                if uploaded_file.type == 'image/jpeg' or uploaded_file.type == 'image/jpg':
                    img = Image.open(uploaded_file)
                    return img
                else:
                    st.error('Error: File uploaded is not an image of extension JPG or JPEG.', icon='🚫')
        elif option == 'Link':
            url_with_pic = st.text_input('Artwork URL:')
            if url_with_pic:
                response = requests.get(url_with_pic)
                if response.headers['Content-Type'] in params['image_format']:
                    img = Image.open(BytesIO(response.content))
                    return img
                else:
                    st.error('Error: Link inputted does not result in an image in format JPG or JPEG.', icon='🚫')
        elif option == 'Camera':
            img_file_buffer = st.camera_input('Take a picture')
            if img_file_buffer is not None:
                img = Image.open(img_file_buffer)
                return img
    return None

def crop_max(img, padding=50):
    width, height = img.size
    diff = np.abs(width - height)
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
    else:
        return img
    cropped_img = img.crop((l,t,r,b))
    return cropped_img

def process_image(img):
    if params['img_mod_size'] < img.size[0] and params['img_mod_size'] < img.size[1]:
        img = img.resize((params['img_mod_size'], params['img_mod_size']))
        grid[0][2].image(img, width=256)
    return img

def guess_it(img):
    grid[0][2].markdown( f'<h4>Guess the style!</h4>',
        unsafe_allow_html=True
        )
    guessed_style = grid[0][2].radio('options', params['styles'].keys(), label_visibility='collapsed')
    if grid[0][2].button('Click me❕'):
        if img != None:
            classified_style, other_styles = classify_art_style(img)
            if params['styles'][guessed_style] == classified_style:
                grid[0][2].success(f"We agree that it should be {classified_style}, so it probably is! Yay us!", icon='🖌️')
                grid[0][2].balloons()
                result_table(other_styles)
            elif classified_style == None or classified_style == 'None':
                grid[0][2].warning("We tried our best but weren't able to classify your image. Are you sure it's an artwork?", icon='🛸')
            else:
                grid[0][2].error("Hmmmmm, doesn't look like it to us! Guess we can agree to disagree!", icon='🤷🏻‍♀️')
                WIKI_PARAMS['search'] = guessed_style
                res = requests.get(url=params["wiki_url"], params=WIKI_PARAMS).json()
                grid[0][2].write(res[3][0])
                result_table(other_styles)

def result_table(results):
    print("results before:", results)
    for key in results.keys():
        results[key] = f"{str(round((results[key]*100))).rstrip('0').rstrip('.')}%"
    results = dict(zip(params['styles'].keys(), results.values()))
    print("results after:", results)

    with grid[0][2]:
        with st.expander("See results in detail"):
            st.dataframe(results, column_config={'': 'Style', 'value': 'Probability'})

def classify_art_style(img):
    with grid[0][2]:
        st.spinner('Hold on while we ask ChatGPT... Just kidding!')
        # transfer image to bytes
        output = BytesIO()
        img.save(output, format='JPEG')
        img_bytes = output.getvalue()
        files = {'file': BytesIO(img_bytes)}
        # make request to the API
        api_response = requests.post(params['api_url'] + params['api_img_endpoint'], files=files) #img_bytes})
        classified_style = api_response.json()[0]['style']
        if api_response.json()[1]:
            other_styles = api_response.json()[1]
        else:
            other_styles = 'None'
        return classified_style, other_styles

#Grid n1 - top of the page
grid = make_grid(3,(2,3,2))

grid[0][0].markdown(
    f"<h2 style='text-align: left; color: #7B2E20; font-family: Rufina;'>Make your educated guess on art</h2>",
    unsafe_allow_html=True
)
grid[0][0].markdown(
    f"<p style='text-align: justify; color: #183247;'>We know how hard it can be to keep different art styles in mind and categorise the works you're looking at, so we've built a predictive model to help you out when you're not so sure.</p>",
    unsafe_allow_html=True

)
#top[0][1].image(image='./images/banner.jpg', use_column_width='always')

grid[0][0].markdown( f'<h4>Select and upload artwork</h4>',
        unsafe_allow_html=True
    )
grid[0][0].info("Upload art as a JPG or JPEG file, paste the URL, or use your camera to snap a picture of it.", icon="🖼️")

img = input_art()
cropped_image = None

with grid[0][0]:
    enable_crop = st.radio('Crop image:', ('Automatically', 'Manually'))

if img is not None:
    if enable_crop == 'Manually':
        with grid[0][1]:
            cropped_image = st_cropper(img, aspect_ratio=(1, 1))
    elif enable_crop == 'Automatically':
        with grid[0][1]:
            cropped_image = crop_max(img)
            grid[0][1].image(img)

if cropped_image:
    processed = process_image(cropped_image)
    guess_it(processed)
