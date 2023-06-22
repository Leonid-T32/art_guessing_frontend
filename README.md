# art-guessing frontend

This repository contains the frontend code for Artend, a (web) application built for educational or socialising purposes. The main functionality of the app is taking artworks provided by the users and returning the likely art style of that work. You can check our app out by following [this link](https://art-guessing.streamlit.app/).

The frontend was built as a Streamlit application, hosted and run on [Streamlit](https://streamlit.io/).

The backend is hosted on Google Cloud Run (GCR) at https://service-art-guessing-l6hzosl6eq-ew.a.run.app/. The connection between the front and backend takes place via a post request.

Artend - step by step

1. Input image
There are three input methods available:
- Upload file from disk
- Provide URL
- Use device camera to snap a picture (webcam or mobile)

2. Crop image
Our model expects images in the 256x256 format. Once the user inputs a valid image, they can either crop it themselves, so they're able to decide which section of the image to select, or allow the application to crop it automatically.

3. Guess the style
Users are prompted to guess which of the 10 art styles the model was trained on they think this artwork belongs to.

4. Submit image and guess
Once the user clicks on the 'Click me!' button, if needed, the image they inputted will be cropped and downsized to 256x256px. Once the image has been preprocessed, it's sent to the backend via a post request, where our model will evaluate it across the 10 art styles it was trained to recognise.

5. Results
The model will provide a probability across each of the art styles. Based on these probabilities, we've built two possible outcomes.
If none of the probabilities is at 20% or more, the user is told that unfortunately, no prediction could be made. If at least one of the categories has a probability of 20% or more, the user will be given a success message in case they guessed the top category correctly, or an error message in case their guess does not match the model's result.

Mobile usage

The frontend of the application is responsive, so it can be used on a mobile device without issues. We do, however, recommend switching the 'Wide mode' off when on mobile devices. To achieve that:

1. Click on the small icon with three horizontal bars in the upper-right corner of the window;
2. Click on 'Settings';
3. Remove the checkmark on 'Wide mode'.

Happy guessing!
