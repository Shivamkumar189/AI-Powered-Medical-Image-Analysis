import tensorflow as tf

def load_data(path):
    print("📂 Loading images...")

    train = tf.keras.preprocessing.image_dataset_from_directory(
        path + "/train",
        image_size=(224, 224),
        batch_size=32
    )

    test = tf.keras.preprocessing.image_dataset_from_directory(
        path + "/test",
        image_size=(224, 224),
        batch_size=32
    )

    return train, test