import setuptools

with open("./README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name = "gitigno",
    version = "0.0.3",
    author = "Minenhle Ngubane",
    author_email = "mino@minenhlengubane.com",
    description = "A Python CLI tool that generates a .gitignore template file using the gitignore.io API",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Minenhle-Ngubane/gitigno",
    packages = setuptools.find_packages(),
    license="MIT",
    classifiers = [
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["click>=8.1.3", "requests>=2.31.0"],
    extras_require = {
        "dev": ["pytest>=7.4.0", "twine>=4.0.2"],
    },
    python_requires = ">=3.10"
)