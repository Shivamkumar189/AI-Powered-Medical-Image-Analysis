import matplotlib.pyplot as plt

def plot_history(history):
    plt.plot(history.history['accuracy'], label="Train")
    plt.plot(history.history['val_accuracy'], label="Validation")
    plt.legend()
    plt.title("Training Accuracy")
    plt.show()