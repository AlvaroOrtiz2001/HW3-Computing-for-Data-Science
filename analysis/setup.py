try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import my_library


def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='my_library',
    version=my_library.__version__,
    description='Assignment 3 library',
    author='Pere, Alvaro, Sebastien',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='https://github.com/AlvaroOrtiz2001/HW3-Computing-for-Data-Science/tree/main',
    classifiers=[
        'Programming Language :: Python :: 3.10.7'
    ]
)