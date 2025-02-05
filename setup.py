from setuptools import find_packages, setup

setup(
    name="opstack-py",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "eth-ape>=0.8.25",
        "ape-optimism",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
