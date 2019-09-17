#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup the package {{ cookiecutter.project_name }}"""

from runpy import run_path

from setuptools import find_packages, setup

_INFO = run_path('src/{{ cookiecutter.project_slug }}/_meta.py')
_TEST_REQUIRES = [
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-flake8',
    'pytest-isort',
    'pytest-mock',
    'pytest-mock',
    'pytest-pep8',
    'pytest-pylint',
    'pytest-yapf',
]

setup(
    # Metadata
    author=_INFO['__author__'],
    author_email=_INFO['__email__'],
    url=_INFO['__home__'],
    use_scm_version=True,
    zip_safe=False,
    # Package modules and data
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # Entries
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.__main__:main',
        ],
    },
    # Requires
    python_requires='>=3.4',
    install_requires=[],
    setup_requires=[
        'pytest-runner',
        'setuptools-scm',
    ],
    tests_require=_TEST_REQUIRES,
    extras_require={
        'dev': _TEST_REQUIRES + [
            'flake8',
            'isort',
            'pylint',
            'yapf',
        ],
    },
    # PyPI Metadata
    keywords=['CLI'],
    platforms=['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
