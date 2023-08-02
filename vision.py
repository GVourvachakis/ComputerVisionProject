import os
from imageai.Classification import ImageClassification

def classify_image(image_path, model_path, model_type='MobileNetV2', result_count=5):
    
    """
    Classify an image using the specified pre-trained model.

    Parameters:
        image_path (str): The path to the input image.
        model_path (str): The path to the pre-trained model file.
        model_type (str): The type of pre-trained model to use (default is 'MobileNetV2').
        result_count (int): Number of predictions to display (default is 5).

    Returns:
        List of tuples: Each tuple contains the predicted label and its corresponding probability.
    """

    if not os.path.isfile(model_path):
        raise FileNotFoundError("Model file not found. Please provide a valid model_path.")

    prediction = ImageClassification()
    
    if model_type == 'MobileNetV2':
        prediction.setModelTypeAsMobileNetV2()
    else:
        raise ValueError("Invalid model_type. Supported model_type is 'MobileNetV2'.")

    prediction.setModelPath(model_path)
    prediction.loadModel()

    predictions, probabilities = prediction.classifyImage(image_path, result_count=result_count)

    results = list(zip(predictions, probabilities))
    return results

if __name__ == "__main__":
    image_path = os.path.join(os.getcwd(), 'giraffe.jpg')
    model_path = os.path.join(os.getcwd(), 'mobilenet_v2-b0353104.pth')

    try:
        results = classify_image(image_path, model_path, model_type='MobileNetV2', result_count=5)
        for label, probability in results:
            print(f'{label} : {probability}')
    except Exception as e:
        print(f"Error: {str(e)}")





