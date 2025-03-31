from setuptools import setup, find_packages

setup(
    name="maphub",
    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.25.1",  # For API calls
    ],
    author="MapHub",
    author_email="info@meteory.eu",
    description="A client wrapper for the MapHub API",
    long_description=open("DOCS.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/your-package-name",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.12",
)
