# Image Classification with CNN

Build a Convolutional Neural Network (CNN) model to classify images for the CIFAR-10 dataset into predefined classes.

[Project in GitHub](https://github.com/biancaene/ironhack_2026_cnn_group1)

## Project Motivation
The aim of the project is to train, test, evaluate, save and reuse CNN classifiers using the CIFAR-10 dataset. This project is using the support offered by the Keras library.

## Project Steps

The steps we covered:

- We started with a basic CNN model, that showed an accuracy of aprox. 70%, measured on the testing dataset.

- We continously improved the model, reaching an accuracy of aprox. 85% on the testing dataset.

## Project Deployment

- The model with the high accuracy was deployed with Gradio, and tested with random pictures taken from Internet. The model was able to correctly classify the random pictures that we have tested.

![gradio_demo](deployment/screenshots/Capture_prediction_automobile.PNG)

## Repository Folders and Files

The repository is splitted in several folders, as follows:

### code
The Notebooks for all trained models are stored in the code folder.
- **main**: The basic CNN used as the first stone of the project.

### trained_models
The trained models with a high accuracy are stored for a later usage.

### deployment
Python code to deploy the model using Gradio.
**pics**
Random pictures to test the trained models.
**screenshots**
Screen captures with the predicted categories for the random pictures given as inputs. 

### spreadsheet
The spreadsheet storing the most important metrics used for comparing the trained models.

### presentation
The presentation containing details about the project.

### requirements
The **requirements.txt** file can be used to install the needed environment to run the notebooks. It is advised to use a virtual environment.
```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```
