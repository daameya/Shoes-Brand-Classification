# Shoes-Brand-Image-Classification

## Workflows
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml

<div id="header">
  <h1>
    <img src="screenshots\shoe_classification_webpage.jpg" alt="Image classification" width="1000" align="center"/>
  </h1>
</div>

Project Overview:

Objective: To build a machine learning model that can classify shoe images into different brands.

Dataset: Gathered a diverse dataset of shoe images from 3 brands and used a ingestion pipeline to import the images from the web.

Model: Utilized a deep learning approach, specifically VGG16 model, for image classification.

Accuracy: Achieved an impressive accuracy rate of 78% on the test set.


Key Features:

🌟 Accurate classification of shoe brands (Nike, Adidas and Converse.).

📸 Robust to variations in lighting, angles, and backgrounds.

🚀 Fast and efficient predictions for real-world applications.

🌟 Used MLops tools like DVC to track pipelines.

🚀 Used docker file and github actions to deploy the model in Azure cloud.


# AZURE-CICD-Deployment-with-Github-Actions

<div id="header">
  <h1>
    <img src="screenshots\Deployment.jpg" alt="Web deployment using github actions" width="1000" align="center"/>
  </h1>
</div>

## Run from terminal:

docker build -t shoesapp.azurecr.io/shoesclassification:latest .

docker login shoesapp.azurecr.io

docker push shoesapp.azurecr.io/shoesclassification:latest

## To use the shoe classification application

1. Clone the repository using the command: `git clone <repo_url>`
2. Navigate to the project directory: `cd <repo>`
3. Run the script using the command: `python app.py`
4. Once the application is running.

    Use port - 127.0.0.1:8080
