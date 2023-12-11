# ITCS-6166-8166-CCN
This is a repository for the final project of **Group 12** for the course **ITCS 6166/8166 (Computer Communication and Networks)** under the guidance of **Dr. Pu Wang**. It has detailed instructions on how to run the project using Google Colab.
We recreated the results of the project **HumanNeRF: Free-viewpoint Rendering of Moving People from Monocular Video (Weng et al., 2022)**
The link for the original project is [here.](https://grail.cs.washington.edu/projects/humannerf/)

# Instructions on how to run the Jupyter Notebook:
**1. Access ```Google Colab``` and sign in with your Google account.**

**2. Upload the Notebook:**
  - Click on the ```Upload``` tab on the Colab homepage.
  - Select ```Choose File``` and upload ```HumanNeRF.ipynb``` from your device.

**3. Open the Notebook:**
  - After the upload, the notebook will appear in the Colab interface. Click to open it.
  - Adjust Runtime Settings (If Necessary): For GPU/TPU or specific Python version, go to the menu, select ```Runtime > Change runtime type```, choose ```settings```, and ```save```.

**4. Run the Notebook:**
  - Execute cells individually using the ```Run``` button or ```Shift + Enter```.
  - For running all cells at once, go to ```Runtime``` in the menu and choose ```Run all```.

**5. Auto-Installation of Dependencies:**
  - The notebook has code that will install any required libraries when you run the cells containing installation commands.


# Results:


https://github.com/nchandel1/ITCS-6166-8166-CCN/assets/153453695/85e1c801-f864-4a6f-a0de-bfe01d9ff64c



https://github.com/nchandel1/ITCS-6166-8166-CCN/assets/153453695/b6dd2743-35b1-4e04-abf7-d25b1786ffa3



https://github.com/nchandel1/ITCS-6166-8166-CCN/assets/153453695/77566cc6-bb73-4a99-9846-bc523539b42e



# Webpage to stream results (using Streamlit)

Please check the file ```StreamCast.mp4``` for a video demonstration of the webpage. And the folder ```webpage``` for the source files.
### App Features | Webpage Content

The webpage provides an overview of our project, its purpose, and the technologies used. It connects to a ```Streamlit``` server that hosts a video showcasing our project results. The video is served using ```Flask``` to ensure a smooth streaming experience.

**How It Works**
- **Streamlit Server**: The ```Streamlit``` server is responsible for displaying the video using the ```Streamlit``` library. It acts as the backend for the application.
- **Flask Server**: A ```Flask``` server is employed to serve the video content as a stream. This ensures efficient and seamless streaming to the client-side.
- **HTML Client**: This ```HTML``` page uses the ```video``` tag to embed the video player. The video is sourced from the Flask server, and users can easily play and control the video using the provided controls.

**Look at the screenshots below:**

![alt text](https://github.com/nchandel1/ITCS-6166-8166-CCN/blob/main/Screenshot%201.png)



![alt text](https://github.com/nchandel1/ITCS-6166-8166-CCN/blob/main/Screenshot%202.png)


