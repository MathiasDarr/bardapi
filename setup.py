from setuptools import setup, find_packages

setup(
    name="bard",
    version="3.9.11",
    description="Packaging a Flask application",
    author="Mathias Darr",
    author_email="dakobedbard@gmail.com",
    url="https://github.com/MathiasDarr/dakobed_flask",
    packages=find_packages(),
    install_requires=["pyyaml"],
    tests_require=["pytest"]
)

