#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="mplcatppuccin",
    url="https://githubcom/brambozz/matplotlib-catppuccin",
    license="MIT",
    author="Bram de Wilde",
    author_email="contact@bramdewilde.com",
    description="Soothing pastel theme for matplotlib",
    long_description="Soothing pastel theme for matplotlib. See https://github.com/brambozz/matplotlib-catppuccin",
    packages=["mplcatppuccin"],
    package_data={
        "mplcatppuccin": ["data/*.mplstyle"],
    },
    install_requires=["matplotlib"],
    # Derive version from git. If HEAD is at the tag, the version will be the tag itself.
    version_config={"version_format": "{tag}.dev{sha}", "starting_version": "v0.0.1"},
    setup_requires=["better-setuptools-git-version"],
    classifiers=[
        "Framework :: Matplotlib",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
