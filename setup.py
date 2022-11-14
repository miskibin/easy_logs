import setuptools
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="miskibin",
    version="1.0.8",
    author="Michał Skibiński",
    author_email="mskibinski109@gmail.com",
    description="My personal package for colored logs. Highly customizable.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/michalskibinski109/miskibin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
