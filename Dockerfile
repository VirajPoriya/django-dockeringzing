# Use the official Python image as a base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

# Start the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["uvicorn", "myproject.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
