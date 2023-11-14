# Use the base image from Hugging Face
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory
WORKDIR /app

# Install the required dependencies
RUN pip install --no-cache-dir transformers fastapi uvicorn sentencepiece python-multipart torch
#-r requirements.txt

# Copy the main.py file
COPY main.py .

# Expose the port on which the API will run
EXPOSE 8000

# Check if the server is responding
HEALTHCHECK --interval=60s --timeout=4s CMD curl --fail http://localhost:8000/ || exit 1

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]