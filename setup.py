from setuptools import setup, find_packages

with open("app/README.md", "r") as f:
    description = f.read()

setup(
    name="flask-app",
    version="1.0",
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArjanCodes/2023-package",
)