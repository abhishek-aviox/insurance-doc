# Insurance Document Management System

This project is a web-based application designed to manage insurance documents efficiently. It provides functionalities to upload, view, and manage various insurance-related documents.

## Project Structure

- **ins_documation/**: Contains the main configuration files for the Django project.
  - `settings.py`: Configuration settings for the Django project.
  - `urls.py`: URL routing for the project.
  - `wsgi.py` and `asgi.py`: Entry points for WSGI/ASGI-compatible web servers.

- **documents/**: Contains the application logic for managing documents.
  - `models.py`: Defines the data models for the application.
  - `views.py`: Contains the view logic for handling requests and responses.
  - `admin.py`: Configuration for the Django admin interface.
  - `tests.py`: Basic tests for the application.
  - `apps.py`: Application configuration.

- **templates/**: Contains HTML templates for rendering the web pages.

- **db.sqlite3**: The SQLite database file used for development.

- **manage.py**: A command-line utility for interacting with the Django project.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x

### Installation


1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the database migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Access the application at `http://127.0.0.1:8000/`.

## Features

- Upload and manage insurance documents.
- User-friendly interface for document management.
- Secure and efficient handling of document data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.