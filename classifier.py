import tensorflow as tf


IMAGE_SIZE = (180, 180)
THRESHOLD = 0.5


def preprocess_image(image):
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    return img_array


def load_and_preprocess_image(path: str):
    image = tf.keras.preprocessing.image.load_img(
        path, target_size=IMAGE_SIZE
    )

    return preprocess_image(image)


def classify(model, image_path):
    preprocessed_image = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    max_index = predictions.argmax()

    labels = ["Bird", "Cat", "Dog"]
    label = labels[max_index]
    prediction = predictions[0][max_index]

    if prediction < THRESHOLD:
        label = "Unknown"
        prediction = 0.0

    return label, prediction
