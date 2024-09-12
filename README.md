
# University CRM - API with CRUD Operations using ApiView

This project is a CRM (Customer Relationship Management) system for managing university entities such as faculties, groups, kafedras (departments), subjects, teachers, and students. The system is built using Django and Django REST Framework (DRF) and provides full CRUD (Create, Read, Update, Delete) functionality through a custom API built with `ApiView`.

## Features

- **CRUD Operations**: Implemented for each model using Django's `ApiView`.
- **Models**: The system manages Faculties, Groups, Kafedras (Departments), Subjects, Teachers, and Students.
- **Detailed API Endpoints**: Separate endpoints for list and detail views for each model.

## Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mirmakhmudoff/02-University-ApiView.git
   cd 02-University-ApiView
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**

   ```bash
   python manage.py runserver
   ```

## API Endpoints

Each model has its own list and detail endpoints, providing full CRUD capabilities.

### Faculty

- **List All Faculties**: `GET /faculties/`
- **Create a Faculty**: `POST /faculties/`
  - Body: `{ "name": "Engineering" }`
- **Retrieve a Specific Faculty**: `GET /faculties/<id>/`
- **Update a Specific Faculty**: `PUT /faculties/<id>/`
  - Body: `{ "name": "Updated Faculty Name" }`
- **Delete a Specific Faculty**: `DELETE /faculties/<id>/`

### Group

- **List All Groups**: `GET /groups/`
- **Create a Group**: `POST /groups/`
  - Body: `{ "name": "Group A", "faculty": 1 }`
- **Retrieve a Specific Group**: `GET /groups/<id>/`
- **Update a Specific Group**: `PUT /groups/<id>/`
  - Body: `{ "name": "Updated Group Name", "faculty": 1 }`
- **Delete a Specific Group**: `DELETE /groups/<id>/`

### Kafedra (Department)

- **List All Kafedras**: `GET /kafedras/`
- **Create a Kafedra**: `POST /kafedras/`
  - Body: `{ "name": "Computer Science" }`
- **Retrieve a Specific Kafedra**: `GET /kafedras/<id>/`
- **Update a Specific Kafedra**: `PUT /kafedras/<id>/`
  - Body: `{ "name": "Updated Kafedra Name" }`
- **Delete a Specific Kafedra**: `DELETE /kafedras/<id>/`

### Subject

- **List All Subjects**: `GET /subjects/`
- **Create a Subject**: `POST /subjects/`
  - Body: `{ "name": "Mathematics", "kafedra": 1 }`
- **Retrieve a Specific Subject**: `GET /subjects/<id>/`
- **Update a Specific Subject**: `PUT /subjects/<id>/`
  - Body: `{ "name": "Updated Subject Name", "kafedra": 1 }`
- **Delete a Specific Subject**: `DELETE /subjects/<id>/`

### Teacher

- **List All Teachers**: `GET /teachers/`
- **Create a Teacher**: `POST /teachers/`
  - Body: `{ "first_name": "John", "last_name": "Doe", "subject": 1 }`
- **Retrieve a Specific Teacher**: `GET /teachers/<id>/`
- **Update a Specific Teacher**: `PUT /teachers/<id>/`
  - Body: `{ "first_name": "Updated Name", "last_name": "Updated Last Name", "subject": 1 }`
- **Delete a Specific Teacher**: `DELETE /teachers/<id>/`

### Student

- **List All Students**: `GET /students/`
- **Create a Student**: `POST /students/`
  - Body: `{ "first_name": "Jane", "last_name": "Doe", "kafedra": 1, "group": 1 }`
- **Retrieve a Specific Student**: `GET /students/<id>/`
- **Update a Specific Student**: `PUT /students/<id>/`
  - Body: `{ "first_name": "Updated Name", "last_name": "Updated Last Name", "kafedra": 1, "group": 1 }`
- **Delete a Specific Student**: `DELETE /students/<id>/`

## Customization

Feel free to modify the models, serializers, and views according to your specific requirements. The CRUD operations are implemented using Django's `ApiView` for full control over each request.
