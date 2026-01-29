import gradio as gr 
import numpy as np 
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing.image import img_to_array 
from PIL import Image 

# load the trained model (PyTorch) 
model = load_model("../trained_models/cifar10.model14.keras") 

# the classes of the CIFAR-10 dataset 
labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"] 

# function: prediction
def predict(image): 

    # preprocessing the image: resize and normalization
    # resize using the dimensions of the trained model 
    img = image.resize((32, 32)) 
    img = img_to_array(img)
    # normalization
    img = img / 255.0 
    img = np.expand_dims(img, axis=0) 
    
    # predict
    #preds = model.predict(img) 
    #idx = np.argmax(preds[0]) 
    #return labels[idx] 

    # predict 
    preds = model.predict(img)[0] 
    # the index of the class with the highest probability 
    idx = np.argmax(preds) 
    max_label = labels[idx] 
    max_prob = float(preds[idx]) 

    # dictionary with the probabilities of all available classes
    probs = {labels[i]: float(preds[i]) for i in range(len(labels))} 
    
    summary = ( 
        f"<b>Predicted class:</b> {max_label} &nbsp;&nbsp;" 
        f"<b>Probability:</b> {max_prob:.4f}<br><br>" 
        f"<b>All probabilities:</b>" 
    ) 
    
    return summary, probs


# interface Gradio 
demo = gr.Interface( 
    fn=predict, 
    inputs=gr.Image(type="pil"), 
    #outputs=gr.Label(), 
    outputs=[gr.HTML(), gr.JSON()],
    title="Classification using the trained model" 
) 

demo.launch()