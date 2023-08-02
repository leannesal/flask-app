from setuptools import setup, find_packages

with open("project/README.md", "r") as f:
    description = f.read()

setup(
    name="flask-app",
    version="1.0",
    packages=find_packages(where="project/src"),
    package_dir={"": "project/src"},
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/leannesal/flask-app",
    author="LayannSalame",
    author_email="lsalame@cisco.com",
    install_requires=[
    'blinker==1.6.2',
    'certifi==2023.7.22',
    'charset-normalizer>=3.2.0',
    'click==8.1.6',
    'exceptiongroup==1.1.2',
    'Flask==2.3.2',
    'Flask-Login==0.6.2',
    'Flask-SQLAlchemy==3.0.5',
    'greenlet==2.0.2',
    'idna==3.4',
    'importlib-metadata==6.8.0',
    'iniconfig==2.0.0',
    'itsdangerous==2.1.2',
    'Jinja2==3.1.2',
    'MarkupSafe==2.1.3',
    'packaging==23.1',
    'pluggy==1.2.0',
    'pytest==7.4.0',
    'requests==2.31.0',
    'SQLAlchemy==2.0.19',
    'tomli==2.0.1',
    'typing_extensions==4.7.1',
    'urllib3==2.0.4',
    'Werkzeug==2.3.6',
    'zipp==3.16.2'
    ],
    extras_require={
        "dev": ["pytest>=7.0"]
    },
     python_requires=">=3.9.0",
)
