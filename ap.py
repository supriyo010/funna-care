import os.path

import tensorflow as tf
from flask import Flask, render_template, request

from classifier import classify

app = Flask(__name__)

STATIC_FOLDER = "static"
UPLOAD_FOLDER = "static/images/"

cnn_model = tf.keras.models.load_model(STATIC_FOLDER + "/models/" + "animals.keras")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return make_prediction()

    return render_template("index.html")


@app.route("/classify", methods=["POST"])
def make_prediction():
    file = request.files["image"]
    if file:
        if file.filename.endswith((".jpg", ".jpeg", ".png")):
            upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(upload_image_path)

            label, prediction = classify(cnn_model, upload_image_path)

            prediction = round(prediction * 100, 2)

            return render_template(
                "classify.html",
                label=label,
                prediction=prediction,
                upload_image_path=upload_image_path
            )

        return "Invalid image file format. Only JPG, JPEG and PNG are supported."

    return "You have not selected an image."


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
