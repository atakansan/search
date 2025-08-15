#!/usr/bin/env python3
"""
Setup script for instant-search package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="instant-search",
    version="1.0.0",
    author="Atakan San",
    author_email="",
    description="Instant multi-platform search tool that opens 9 search sites simultaneously",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atakansan/search",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "linux": [],  # xclip or xsel recommended for Linux clipboard support
    },
    entry_points={
        "console_scripts": [
            "instant-search=instant_search.main:main",
            "isearch=instant_search.main:main",
            "s=instant_search.main:main",
        ],
    },
    keywords="search, browser, automation, productivity, multi-search",
    project_urls={
        "Bug Reports": "https://github.com/atakansan/search/issues",
        "Source": "https://github.com/atakansan/search",
    },
)