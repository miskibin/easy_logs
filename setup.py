# setup.py sdist bdist_wheel
from setuptools import setup

if __name__ == "__main__":
    setup(
        name="miskibin",
        package_dir={"": "src"},
        packages=["miskibin.utils", "miskibin.ml"],
    )
