from setuptools import setup, find_packages
import os

setup(
    name="string_processor",
    version="0.1.0",
    packages=find_packages(),
    author="Duc Tri Nguyen",
    author_email="logger1606@gmail.com",
    description="A comprehensive string processing utility package",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/string_processor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'typing>=3.7.4',  # For type hints
        'pytest>=7.0.0',  # For testing
        'black>=22.0.0',  # For code formatting
        'mypy>=0.950',    # For static type checking
    ],
    extras_require={
        'dev': [
            'pytest-cov>=2.12.0',  # For test coverage
            'flake8>=4.0.0',       # For linting
        ]
    },
    test_suite="tests",
)