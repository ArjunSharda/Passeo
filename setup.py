import pathlib
from setuptools import setup, find_packages

project_dir = pathlib.Path(__file__).parent.resolve()
long_description = (project_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="passeo",
    version="1.0.1",
    description="🔓 Generate a Password with multiple options",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArjunSharda/Searchor",
    author="Arjun Sharda",
    author_email="sharda.aj17@gmail.com",
    classifiers=[  # Optional
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    package_dir={"": "src"},
    packages=find_packages(where="src"),

    python_requires=">=3.7, <4",

    install_requires=["random", "string", "hashlib", "requests"],


    project_urls={
        "Homepage": "https://github.com/ArjunSharda/Passeo",
        "Bug Tracker": "https://github.com/ArjunSharda/Passeo/issues"
    },
)
