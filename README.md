# art-guessing frontend
The applicaton (the app) is built to be used as a game or in terms of self education.
It is supposed to automatically assign an art style to image uploaded by user.
The frontend is built as a streamlit application hosted and run on [streamlit](https://streamlit.io/).
Check out the art-guessing app [here](https://art-guessing.streamlit.app/).
It reaches out to the backend appliation run on GCR at (https://service-art-guessing-l6hzosl6eq-ew.a.run.app/) 
via post request every time you click the button 'Click me!' as long as an image is uploaded by user.
The are three options to upload the image: file upload from disk, providing url, or taking image via camera 
(last option is suitable to use the webcam of your desktop computer or the camera of your mobile).
After clicking the 'Click me!'-button the uploaded image is being cropped and downsized to 256x256px 
(as it is required by the backend model) then posted to the backend. Models best guess is being returned 
to the frontend along with a table of all styles known by the model with their appropriate probabilities. 
Those are then presented to the user. 
No extra efort is needed to run the application on your desktop or mobile. However, to run on mobile we recommend
to switch off the 'Wide mode' (click on three tiny horizontal bar in the right upper conner of the window,
click on settings, then remove the checkmark on 'Weide mode').
Have fun!
