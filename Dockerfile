# Base Python image
FROM python:3.12-slim

# Install Tkinter and X11 dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application
COPY src ./src

COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run GUI application
CMD ["python", "src/main.py"]