# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyserverses",
    version="0.1.0",
    author="kote",
    author_email="arturzavalov64@gmail.com",
    description="Простая библиотека для создания серверов и клиентов",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/koteey/pyserverses",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
)