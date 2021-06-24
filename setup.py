from setuptools import setup, find_packages

setup(
    name="bard",
    version="3.9.11",
    description="Packaging bardapi ",
    author="Mathias Darr",
    author_email="dakobedbard@gmail.com",
    url="https://github.com/MathiasDarr/bardapi",
    packages=find_packages(),
    entry_points={
        "bard.init": [],
        "console_scripts": ["bard = bard.manage:cli"],
    }
)

