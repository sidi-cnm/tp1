"""
Setup script pour l'installation de VizStyle
"""

from setuptools import setup, find_packages

# Lire le contenu du README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Lire les dépendances
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="vizstyle",
    version="1.0.0",
    author="Emin",
    author_email="emin@example.com",
    description="Une bibliothèque de visualisation Python élégante avec un style cohérent et moderne",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emin/vizstyle",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="visualization plotting matplotlib graphs charts data-science",
    project_urls={
        "Documentation": "https://github.com/emin/vizstyle",
        "Source": "https://github.com/emin/vizstyle",
        "Bug Reports": "https://github.com/emin/vizstyle/issues",
    },
)
