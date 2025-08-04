FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app code (includes download.py, main.py, etc.)
COPY . .

# Run the model download script once, during image build
RUN python download.py

# Streamlit config for Render
ENV PORT 8080
EXPOSE 8080

# Avoid file watcher issues in production
ENV STREAMLIT_WATCHDOG=false

# Launch Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
