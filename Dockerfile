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

# Run the FastAPI server
CMD ["uvicorn", "search_engine_api:app", "--host", "0.0.0.0", "--port", "8089"]