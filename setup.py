#!/usr/bin/env python
import os
import codecs

try:
    from setuptools import (
        setup,
        find_packages
    )

except ImportError:
    from distutils.core import (
        setup,
        find_packages
    )

from keras_datasets import (
    __version__,
    __contact_names__,
    __contact_emails__,
    __repository_url__,
    __download_url__,
    __description__,
    __package_name__,
    __homepage__,
    __keywords__
)

here = os.path.abspath(os.path.dirname(__file__))

if os.path.exists('README.rst'):
    # codec is used for consistent encoding
    long_description = codecs.open(os.path.join(here, 'README.rst'), 'r', 'utf-8').read()
else:
    long_description = 'See ' + __homepage__
# ======================= Reading Requirements files as TXT files =======================


def req_file(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters
    # Example: `\n` at the end of each line
    return [x.strip() for x in content]

# =================================== Setup Operations ===================================


setup(
    name=__package_name__,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description=__description__,
    long_description=long_description,

    # The project's main homepage.
    url=__repository_url__,
    download_url=__download_url__,

    # Author details
    author=__contact_names__,
    author_email=__contact_emails__,

    # maintainer Details
    maintainer=__contact_names__,
    maintainer_email=__contact_emails__,

    # The licence under which the project is released
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #  1 - Planning
        #  2 - Pre-Alpha
        #  3 - Alpha
        #  4 - Beta
        #  5 - Production/Stable
        #  6 - Mature
        #  7 - Inactive
        'Development Status :: 1 - Planning',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',

        # Indicate what your project relates to
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        # Additionnal Settings
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    keywords=__keywords__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=req_file("requirements_lib.txt"),

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,travis]
    extras_require={
        'dev': req_file("requirements_dev.txt"),
        'travis': req_file("requirements_travis.txt")
    },
    zip_safe=True,
)
