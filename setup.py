from setuptools import setup

if __name__ == "__main__":
    setup(
        name="miskibin",
        package_dir={"": "src"},
        packages=["miskibin", "miskibin._internal_modules"],
    )
