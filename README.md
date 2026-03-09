# WriteShot - A Django Blog Application

A full-featured blog application built with Django that allows users to create, read, update, and delete blog posts with image uploads and user authentication.

## ✨ Features

- **User Authentication** - Register, login, and logout functionality
- **Profile Management** - User profiles with profile picture upload
- **Post Management** - Create, read, update, and delete blog posts
- **Image Upload** - Upload images with posts
- **Privacy Settings** - Make posts public or private
- **Responsive Design** - Mobile-friendly interface with Bootstrap 5
- **Pagination** - Browse posts with pagination
- **User-specific Posts** - View your own posts separately

## Workflow Diagrams

- we'll post it soon

## 🚀 Tech Stack

- **Backend:** Django 4.x
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (development) / PostgreSQL (production)
- **Image Processing:** Pillow
- **Version Control:** Git

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- virtualenv (recommended)

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/writeshoot.git
cd writeshoot
```

### 2. Create and activate virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create superuser (admin)

```bash
python manage.py createsuperuser
```

### 6. Run development server

```bash
python manage.py runserver
```

### 7. Visit the application

- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
writeshoot/
├── blog_app/                 # Main blog application
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   │   └── blog_app/
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       ├── my_posts.html
│   │       └── post_confirm_delete.html
│   ├── __init__.py
│   ├── admin.py              # Admin configuration
│   ├── forms.py              # Post forms
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing
│   └── views.py              # View logic
│
├── accounts/                  # User authentication app
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── register.html
│   │       └── login.html
│   ├── __init__.py
│   ├── forms.py              # Registration forms
│   ├── models.py             # Profile model
│   ├── urls.py
│   └── views.py
│
├── media/                     # User uploaded files
│   └── profiles/              # Profile pictures
│   └── post_images/           # Post images
│
├── static/                     # Static files (CSS, JS)
├── templates/                  # Base templates
│   └── base.html
│
├── writeshoot/                 # Project configuration
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL config
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## 📦 Dependencies

Create a `requirements.txt` file:

```
Django>=4.0.0
Pillow>=9.0.0
```

## 🚦 Usage

### Creating a Post

1. Login to your account
2. Click "Create Post" button
3. Fill in title, content, and optional image
4. Choose privacy setting (public/private)
5. Submit

### Viewing Posts

- **All Posts** - Shows all public posts
- **My Posts** - Shows your posts (both public and private)

### Managing Posts

- **Edit** - Click Edit button on your post
- **Delete** - Click Delete button on your post
- **View** - Click Read button on any post

## 👥 User Roles

- **Guest Users** - Can view public posts only
- **Registered Users** - Can create posts and manage their own posts
- **Admin Users** - Full access to admin panel

## 🔒 Environment Variables

Create a `.env` file for sensitive data:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## 🚀 Deployment

### Deploy to PythonAnywhere

1. Create account on PythonAnywhere
2. Upload your code
3. Set up virtual environment
4. Configure WSGI file
5. Set up static/media files

### Deploy to Heroku

```bash
heroku create your-app-name
heroku config:set SECRET_KEY=your_secret_key
git push heroku main
heroku run python manage.py migrate
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 📧 Contact

Your Name - your.email@example.com
Project Link: [https://github.com/yourusername/writeshot](https://github.com/yourusername/writeshot)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap 5
- All contributors

## 🐛 Known Issues

- Profile pictures not showing on first upload (refresh fixes)
- Mobile menu needs improvement
- Add comment feature coming soon

## 🗓️ Roadmap

- [ ] Add comments functionality
- [ ] Add post categories/tags
- [ ] Add search feature
- [ ] Improve mobile responsiveness
- [ ] Add social sharing
- [ ] Add rich text editor
- [ ] Email notifications
