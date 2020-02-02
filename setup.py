import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="mdgreet",
    version="0.0.1",
    author="AfoninZ",
    author_email="zakharafonin@icloud.com",
    description="Modular, extensible MOTD script with theme support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
