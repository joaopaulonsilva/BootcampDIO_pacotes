from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="BootcampDIO_pacotes",
    version="0.0.1",
    author="Joao",
    author_email="joaopaulonsilva@gmail.com",
    description="Pacote criado para aprendizado do bootcamp DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joaopaulonsilva/BootcampDIO_pacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)