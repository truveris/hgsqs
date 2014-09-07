# Copyright 2014, Truveris Inc.

from setuptools import setup, find_packages


setup(
    name="hgsqs",
    version="0.9.0",
    description="Mercurial to SQS hook",
    author="Truveris Inc.",
    author_email="dev@truveris.com",
    url="http://labs.truveris.com/",
    install_requires=[
        "boto",
    ],
    packages=find_packages(),
)
