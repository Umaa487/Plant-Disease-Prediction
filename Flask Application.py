from flask import Flask, render_template, request, url_for
from flask_ngrok import run_with_ngrok
import os
import base64
import cv2
import tensorflow as tf
from tensorflow import keras


app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def home():
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/Templates/main_page.html", "r") as f:
        html_content = f.read()

    # return the HTML content as a response
    return html_content
@app.route("/feed")
def page1():
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/Templates/feed.html", "r") as f:
        html_content = f.read()

    # return the HTML content as a response
    return html_content
@app.route("/about")
def page2():
    # read the HTML file into a string variable
    '''file = request.files['image']
    filename='OURTEAM.jpg'

    file_path = os.path.join('/content/',filename)
    file.save(filepath)
    # read input image and encode to base64
    image = cv2.imread(file_path)
    _, buffer = cv2.imencode('.jpg', image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')
    img_url = f"data:image/jpeg;base64,{image_base64}"'''
    with open("/content/drive/MyDrive/Templates/aboutus.html", "r") as f:
        html_content = f.read()
        filename='umaa.jpg'
        file_path = os.path.join('/content/drive/MyDrive/static', filename)
        # read input image and encode to base64
        image = cv2.imread(file_path)
        _, buffer = cv2.imencode('.jpg', image)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        img_url = f"data:image/jpeg;base64,{image_base64}"
        html_content = html_content.replace('{{img}}', img_url)

    # return the HTML content as a response
    return html_content
@app.route("/chat")
def page3():
    # read the HTML file into a string variable
    with open("/content/drive/MyDrive/static/chatbot.html", "r") as f:
        html_content = f.read()

    # add the path to the stylesheet and JavaScript file
    css_url = url_for('static', filename='style2.css')
    js_url = url_for('static', filename='script1.js')
    # replace the placeholders in the HTML content with the URLs
    html_content = html_content.replace('{{css_url}}', css_url)
    html_content = html_content.replace('{{js_url}}', js_url)

    # return the HTML content as a response
    return html_content
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # fetch input image
        file = request.files['image']
        filename = file.filename
        print("@@ Input posted = ", filename)

        # save input image
        file_path = os.path.join('/content/drive/MyDrive/static/Upload ', filename)
        file.save(file_path)
        print("File saved to:", file_path)

        # read input image and encode to base64
        image = cv2.imread(file_path)
        _, buffer = cv2.imencode('.jpg', image)
        image_base64 = base64.b64encode(buffer).decode('utf-8')
        img_url = f"data:image/jpeg;base64,{image_base64}"

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
        print("Prediction result:", pred)
        print("Output page:", output_page)

        with open(output_page, 'r') as f:
            html1 = f.read()
            html1 = html1.replace('{{pred_output}}', pred)
            html1 = html1.replace('{{img_url}}', img_url)

        return html1

if __name__ == "__main__":
    app.run()
