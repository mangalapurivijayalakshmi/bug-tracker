# 🐛 Bug Tracker App

A full-stack web application built with Python Django to report, track, and manage software bugs — with role-based ownership and secure access control.

## Features
- User Authentication (Login / Logout) using Django's built-in auth system
- Report New Bugs with title, description, and priority
- Track Status (Open / In Progress / Resolved)
- Assign bugs to team members
- Edit and Delete Bugs
- Secure, ownership-based access — users can only edit/delete bugs they created
- Color-coded priority and status badges for quick visual tracking

## Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite
- **Testing:** Manual test cases (see `test_cases/` folder)
## How to Run
1. Clone the repository

git clone https://github.com/mangalapurivijayalakshmi/bug-tracker.git
cd bug-tracker

2. Install dependencies

pip install -r requirements.txt

3. Run migrations

python manage.py migrate

4. Start the server

python manage.py runserver

5. Open http://127.0.0.1:8000/login/

## Manual Testing
This project was manually tested for core flows including bug creation, editing, status updates, and access control. Test cases covering functional and negative scenarios are documented in the [`test_cases/`](./test_cases) folder.

## Screenshots

### All Bugs Page
![All Bugs](bugtracker/screenshots/All%20Bugs%20Page.png)

### Login Page
![Login](bugtracker/screenshots/Login%20Page.png)

### Report New Bug Page
![Report Bug](bugtracker/screenshots/Report%20New%20Bug%20Page.png)
## Future Improvements
- Pagination for large bug lists
- Email notifications on bug assignment
- Search and filter by status/priority

## Author
Mangalapuri Vijaya Lakshmi