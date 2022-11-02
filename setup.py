# setup.py sdist bdist_wheel
from setuptools import setup
import setuptools

setup(
    name="miskibin",
    package_dir={"": "src"},
    version="1.0.5",
    author="Michał Skibiński",
    description="This is package with useful tools",
    long_description="This is a package  with useful tools",
    url="https://github.com/michalskibinski109/miskibin",
    python_requires=">=3.7, <4",
    packages=["miskibin"],
    license="MIT",
)
