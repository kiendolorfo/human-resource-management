# Base image
FROM ubuntu:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Manila
ENV DEBIAN_FRONTEND=noninteractive 


# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql \
        postgresql-client \
        libpq-dev \
        python3 \
        python3-dev \
        python3-pip \
        gcc \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./humanresource/requirements.txt /app/requirements.txt 
RUN pip3 install -r /app/requirements.txt --no-cache-dir

# Copy project files into container
COPY ./humanresource /app/

# Expose port for the Django development server
EXPOSE 8000

# Run Django development server
CMD ["python3", "/app/manage.py", "runserver", "0.0.0.0:8000"]