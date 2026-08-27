def evaluate_model(model, test_data):
    print("\n📊 Evaluating...")

    loss, acc = model.evaluate(test_data)

    print("Accuracy:", acc)