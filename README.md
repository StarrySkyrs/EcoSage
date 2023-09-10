
<p align="center">
  <img src="https://altaml.com/media/ul4ibm45/logo-for-dark.png?#gh-dark-mode-only">
  <h1 align="center"> 
    AltaML Hackathon 2023 - Sustainability
    <br>
    :recycle: :earth_americas: Eco Sage :earth_americas: :recycle:
    <br>
    <img src="https://github.com/StarrySkyrs-AltaML/EcoSage/assets/82040820/e983a1e5-4b46-4990-98e3-9bb75270e1fa" width="150" height="300">

  <h1> 
<p>

## At a glance ... 
Welcome to the :recycle::earth_americas: Eco Sage :earth_americas::recycle: hackathon project repository! Our goal is to create an innovative recycling app that simplifies the recycling process by providing clear instructions on how to recycle various objects. The app takes an input image of an object, uses advanced image processing and language models, and outputs detailed recycling instructions based on a comprehensive knowledge database.

## Table of Contents :clipboard:
- [Project Overview](#project-overview-rocket)
- [How to Use the RecycleSage App](#how-to-run-ecosage-computer)
- [Contributions Welcome!](#contributions-welcome-raised_hands)
- [Contact Us](#contact-us-dove)

## Project Overview :rocket:

In this hackathon project, we are building a recycling app that consists of three main components: image segmentation, image captioning, and recycling instructions generation. The web app is launched using Streamlit. 
![Copy of DisposeCam drawio](https://github.com/StarrySkyrs-AltaML/EcoSage/assets/82040820/1edfb9b4-50b0-463c-a938-fbb25e857bb7)


### 1️⃣ Image Segmentation

The first step of our pipeline involves image segmentation. We utilize **Fast Segment Anything Model (FastSAM)** CNN model to analyze the input image and identify objects within it. The model will then crop these objects to provide a clear view of each item. 
<br>
[For more information about FastSAM, visit the documentation.](https://github.com/CASIA-IVA-Lab/FastSAM)

### 2️⃣ Image Captioning

Once the objects are segmented, we proceed to generate descriptions for each of them using the **BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation** model. It takes the segmented image and provides a caption describing the contents of an image. 
<br>
[For more information about BLIP, visit the documentation.](https://huggingface.co/Salesforce/blip-image-captioning-large)

### 3️⃣ Recycling Instructions Generation

The final step of our pipeline involves generating recycling instructions based on the object descriptions and our comprehensive knowledge database. We utilize OpenAI's Language Model to create detailed and specific instructions on how to recycle each identified object. The knowledge database contains links to the City of Calgary's recycling guidelines _What goes where?_.
<br>
[For more information about OpenAI, visit the documentation.](https://platform.openai.com/docs/introduction)
<br>
[For more information about City of Calgary guidelined, visit the _What goes where?_](https://www.calgary.ca/waste/what-goes-where/default.html)

## How to Run EcoSage :computer:

1. Clone this repository using `git clone https://github.com/altaml-hackathon/hackathon-aug-2023-happy.git`
2. Go to the root folder and create your conda environment using `make setup-environment`
3. Copy the secrets file using `cp secrets.env.template .env` if working in bash, or `copy secrets.env.template .env` if working in CMD or PowerShell and replace the contents of the file with your credentials. 
4. Open another terminal. Then, launch the web app using `cd deployment_components\backend\knowledge_base` from the root folder and run `uvicorn main:app --reload`.
5. Upload an image of `.png`, `.jpeg` or `.jpg` format in the app and enjoy the recycling instructions! :blush:

## Contributions Welcome! :raised_hands:

Since this is a proof of concept project during a hackathon, it has several areas of improvement and scalability! As such, we encourage contributions to improve the :recycle::earth_americas: Eco Sage :earth_americas::recycle: app! To make you contribution, follow these steps:
1. Fork this repository to your GitHub account.
2. Create a new branch for your feature using `git checkout -b <feature>/<your-feature-name>`.
3. Commit your changes using `git commit -m 'Add some feature'`.
4. Push to the branch using `git push origin <feature>/<your-feature-name>`.
5. Open a pull request, and our team will review your contribution. 🌱🌍

## Contact Us :dove:

Our beautiful team: @fatemehyb, @ameeny, @timurkz, @hannayurchyk, @ACCHarles and @StarrySkyrs! ❤️
<br>
Thank you for joining us in this important endeavor to promote recycling and sustainability! 
<br>
🌿🌟








