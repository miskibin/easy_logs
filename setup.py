from setuptools import setup

if __name__ == "__main__":
    setup(
        name="miskibin",
        version="1.0.1",
        description="this is an library with utils for my studies",
        long_description="this is an library with utils for my studies.",
        author="Michal Skibinski",
        author_email="mskibinski109@gmail.com",
        package_dir={"": "src"},
        license="MIT",
        packages=["miskibin", "miskibin._internal_modules"],
    )
