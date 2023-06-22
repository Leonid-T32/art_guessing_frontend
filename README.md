# art-guessing frontend
This application (the app) is built to be used as a social game or in terms of self-education.  
It is supposed to automatically assign an art style to an image uploaded by the user.  
The frontend is built as a streamlit application hosted and runs on [streamlit](https://streamlit.io/). 
Be free to check out the amazing art-guessing app [here](https://art-guessing.streamlit.app/).  
It reaches out to the backend application run on Google Cloud Run (GCR) at https://service-art-guessing-l6hzosl6eq-ew.a.run.app/  
via post request every time you click the button 'Click me!' as long as an image is uploaded by the user.  

The are three options to upload an image:  
- file upload from disk
- providing url
- taking image via camera (webcam or mobile)
  
After clicking the 'Click me!'-button the uploaded image is being cropped and downsized to 256x256px as it is required by the backend model then posted to it and processed. The model's best guess is returned to the frontend along with a table of all styles known by the model with their appropriate probabilities. Those are then presented to the user.   

No extra effort is needed to run the application on your desktop or mobile. However, to run on mobile we recommend switching off the 'Wide mode'.
For that,  
1. click on three tiny horizontal bars in the right upper corner of the window,
2. click on settings,
3. remove the checkmark on 'Wide mode'.

Have fun!
