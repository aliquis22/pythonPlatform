# PythonSiteProject

The site is a portal with educational information and materials on the Python programming language.

## Getting started

### Cloning

Clone the repository

```bash
git clone https://codelab.tpu.ru/vaz30/pythonsiteproject.git
```

### Database

Create a new PostgreSQL database if you don't have one. See [Use PostgreSql with Django](https://tpu.atlassian.net/wiki/spaces/DS/pages/6127618/Use+PostgreSQL+with+Django+Application)

### Environment variables

Copy the `.env.example` file and rename it to `.env`. Fill the `.env` file with the required environment variables.

### Installation and Creating a Virtual Environment

**Step 1.** Create a virtual environment.

```bash
py -m venv .venv
```

**Step 2.** Activate the virtual environment and verify it

```bash
.\.venv\Scripts\activate
```

**Step 3.** Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django.

```bash
pip install django
```

**Step 4.** Run the Django server by running the below command.

```bash
python manage.py runserver
```

## License

[MIT](https://choosealicense.com/licenses/mit/)