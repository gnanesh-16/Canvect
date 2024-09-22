# setup.py

from setuptools import setup, find_packages

setup(
    name='Canvect',
    version='0.1.1',
    description='CAN Communication Package for Controlling with Ring Buffer such that many of ',
    author='Gnanesh B',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'python-can',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
