import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hugowickham",
    version="1.0.0",
    author="Hugo Wickham",
    author_email="hugo.wickham@apexx.global",
    description="Package containing functions for accessing Apexx API 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sandmgw.apexxfintech.com/mgw/v2/api/doc#",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)