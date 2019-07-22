#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='vasp_tools',
    version='0.1.0',
    description="A suite of scripts that perform menial, tedious and repetitive tasks and operations on VASP files that were hurriedly and haphazardly put together by some intern.",
    long_description=readme + '\n\n' + history,
    author="Zaid Hassan aka RexGalilae",
    author_email='mdzaidgr8@gmail.com',
    url='https://github.com/RexGalilae/vasp_tools',
    packages=[
        'vasp_tools',
    ],
    scripts = [
        'scripts/cart-direct.py',
        'scripts/e-gap.py',
        'scripts/e-plot.py',
        'scripts/fix-upto.py',
        'scripts/place-at.py',
        'scripts/rotate.py',
        'scripts/split-by.py',
    ],
    package_dir={'vasp_tools':
                 'vasp_tools'},
    entry_points={
        'console_scripts': [
            'vasp_tools=vasp_tools.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='vasp python computation dft',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
