import setuptools
import os

path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(path, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="miskibin",
    version="1.0.6",
    author="Michał Skibiński",
    author_email="mskibinski109@gmail.com",
    description="My personal package for colored logs. Highly customizable.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michalskibinski109/miskibin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
