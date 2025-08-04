FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy and run the model download script
COPY download.py .
RUN python download.py

# Copy rest of the app
COPY . .

# Set Streamlit to run on 0.0.0.0 for Render
ENV PORT 8080
EXPOSE 8080

CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
