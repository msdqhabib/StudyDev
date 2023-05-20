# StudyDev Web Application
This web application is a discussion room platform that allows users to create and join discussions in various rooms.
It is built using Django, a high-level Python web framework, and provides user authentication and CRUD operations for discussions and rooms.

<!-- Add table of contents -->
## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<!-- Add features list -->
## Features
- User Registration and Authentication
- Discussion Rooms
- Discussions
- Room Management

<!-- Add installation instructions -->
## Installation

To get started with Django Study Dev App, you need to have Python and pip installed on your system. Then, follow these steps:

1. Clone this repository:
```python
git clone https://github.com/msdqhabib/StudyDev
```
2. Navigate to the project directory:
```python
cd studydev
```
3. Install the required packages:
```python
pip install -r requirements.txt
```
4. Apply the database migrations:
```python
python manage.py makemigrations
python manage.py migrate
```
5. Run the development server:
```python
python manage.py runserver
```

The application will now be available at `http://localhost:8000`.


## Contributing

If you would like to contribute to the Django Study Dev Web App, you can follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and add tests if possible.
4. Submit a pull request.

## License

The Django Study Dev Web App is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
