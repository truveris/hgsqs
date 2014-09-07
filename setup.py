# Copyright 2014, Truveris Inc.

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="hgsqs",
    version="0.9.0",
    description="Mercurial to SQS hook",
    long_description=open(os.path.join(here, 'README.md')).read(),
    license="LICENSE.txt",
    author="Truveris Inc.",
    author_email="dev@truveris.com",
    url="https://github.com/truveris/hgsqs",
    install_requires=[
        "boto",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Version Control",
    ],
    packages=find_packages(),
)
