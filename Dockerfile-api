# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for FastAPI
EXPOSE 8089

# Copy wait-for-it.sh
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Run the FastAPI server after ensuring the index file exists
CMD ["/wait-for-it.sh", "/shared-data/car_metadata.pkl", "--", "uvicorn", "search_engine_api:app", "--host", "0.0.0.0", "--port", "8089"]