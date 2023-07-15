# Shoes-Brand-Classification

## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:
vHJmHPAtCx//70uHEyXro6w4QofCIQavmLMIoFGnjk+ACRCac6T7


## Run from terminal:

docker build -t shoesapp.azurecr.io/shoesclassification:latest .

docker login shoesapp.azurecr.io

docker push shoesapp.azurecr.io/shoesclassification:latest