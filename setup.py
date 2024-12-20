from setuptools import setup

setup(
    name="safe-pfl-distance",
    version="0.1.2",
    description="safe-pfl distance calculator",
    url="https://github.com/safe-pfl/distances",
    author="MohammadMojtaba Roshani",
    author_email="mohammadmojtabaroshani@outlook.com",
    license="Apache Software License",
    packages=["safe-pfl-distance"],
    install_requires=[
        "torch>=2.5",
        "matplotlib==3.6.3",
        "matplotlib-inline==0.1.7",
        "matplotlib2tikz==0.7.6",
        "scipy>=1.14",
        "scikit-learn>=1.5",
        "numpy>=2.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
)
