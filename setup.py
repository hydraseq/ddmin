import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ddmin",
    version="0.0.1",
    author="Efrain Olivares",
    author_email="efrain.olivares@gmail.com",
    description="Elementary implementation of delta debugging algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hydraseq/ddmin",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)