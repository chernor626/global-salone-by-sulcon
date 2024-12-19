# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install system dependencies, including PostgreSQL client tools
RUN apt-get update \
    && apt-get install -y libpq-dev postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "global_salone.wsgi:application", "--bind", "0.0.0.0:8000"]