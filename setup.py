from setuptools import setup, find_packages


setup(
    name="evoaug",
    version="1.0.6",
    packages=find_packages(),
    description = "A Python package that trains models with evolution-inspired data augmentations. ",
    python_requires=">=3.6",
    install_requires=[
        "lightning>=2.0.0",
        "torch>=1.12.0",
        "numpy>=1.21.0"
    ],
)
