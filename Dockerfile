# Define base image
FROM python:3.14-slim

# Install dependencies
pip install streamlit

# Set working directory
WORKDIR /app

# Copy file
COPY app.py .

#  Run streamlit
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
