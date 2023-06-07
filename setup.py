import setuptools


with open("readme.md", "r", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name="easy_logging",
    version="1.2.0",
    author="Michał Skibiński",
    author_email="mskibinski109@gmail.com",
    description="My personal package for colored logs. Highly customizable.",
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    files_to_include=["easy_logging"],
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
