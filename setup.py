#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()


setuptools.setup(
    name="syz",
    version="0.0.1",
    author="Sun Yuanzhen",
    author_email="sunyuanzhen@gmail.com",
    description="common tools",
    long_description="common tools",
    long_description_content_type="text/markdown",
    url="https://sunyuanzhen.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "psutil",
    ],
)
