# Zero-shot Classifier REST API
This repository contains a RESTful API built using FastAPI for performing zero-shot text classification using Hugging Face Transformers library. The API utilizes a pre-trained model to classify input text against given candidate labels.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/socode-marcelo/zero-shot-classifier-rest-api.git
   cd your-repository
   ```

2. Install the required dependencies:

   It's recommended to create a virtual environment before installing dependencies.

   ```bash
   pip install --no-cache-dir transformers fastapi uvicorn sentencepiece python-multipart torch
   ```

3. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

## Usage

### Health Check Endpoint

The API provides a health check endpoint to verify the server's status:

- **GET /:** Check if the server is running.

### Classification Endpoint

The main endpoint of the API is for zero-shot text classification:

- **POST /classify:** Perform text classification by sending a POST request with JSON data containing the text to classify and candidate labels.

  Example Request Body:
  ```json
  {
    "sequence_to_classify": "Input text to classify.",
    "candidate_labels": ["Label 1", "Label 2", "Label 3"]
  }
  ```

  Example Response Body:
  ```json
  {
    "labels": ["Label 1", "Label 3"],
    "scores": [0.85, 0.75]
  }
  ```

## Configuration

- By default, the API tries to utilize GPU (if available) for text classification. You can configure the device in `main.py` by changing the `device` variable to `'cuda'` or `'cpu'`.

## Contributing

Contributions are welcome! If you'd like to enhance this API or fix issues, please fork the repository and create a pull request. Any contributions you make are greatly appreciated.

## License

This project is licensed under the MIT License.
