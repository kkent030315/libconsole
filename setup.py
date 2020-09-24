from setuptools import setup
from codecs import open
from os import path

current_dir = path.abspath(path.dirname(__file__))

with open(path.join(current_dir, 'README.md'), encoding='utf-8') as file:
    description = file.read()

setup(
    name='libconsole',
    packages=['libconsole'],
    version='1.0.0',
    license='MIT',
    install_requires=['pyparsing'],
    author='kkent030315',
    author_email='hrn832@protonmail.com',
    url='https://github.com/kkent030315/libconsole',
    description='Beautiful printouts in console',
    long_description=description,
    long_description_content_type='text/markdown',
    keywords='console libconsole beautiful color',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6.5',
    ],
)