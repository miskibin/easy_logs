# setup.py sdist bdist_wheel
from setuptools import setup
import setuptools

if __name__ == "__main__":
    setup(package_dir={"": "src"}, packages=setuptools.find_packages())
