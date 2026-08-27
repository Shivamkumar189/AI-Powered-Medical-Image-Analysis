import sys
import os
import numpy as np

# Fix import path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_PATH)

from preprocessing import load_data
from model import build_model
from evaluate import evaluate_model
from utils import plot_history

def main():
    print("🩺 Medical Image Analysis Started")

    train_data, test_data = load_data("data")

    model = build_model()

    history = model.fit(train_data, epochs=3, validation_data=test_data)

    evaluate_model(model, test_data)

    plot_history(history)

    print("✅ Training Completed")

if __name__ == "__main__":
    main()