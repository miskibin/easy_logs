import setuptools


LONG_DESCRIPTION = """
![example workflow](https://github.com/michalskibinski109/easy_logs/actions/workflows/python-app.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/easy_logs.svg)](https://badge.fury.io/py/miskibin)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
# easy_logs
[Documentation](https://github.com/michalskibinski109/easy_logs/tree/main#readme)
"""

setuptools.setup(
    name="easy_logs",
    version="1.1.2",
    author="Michał Skibiński",
    author_email="mskibinski109@gmail.com",
    description="package for easy colored logs with predefined configurations.",
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    files_to_include=["easy_logs"],
    package_data={"readme": ["readme.md"]},
    url="https://github.com/michalskibinski109/easy_logging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
