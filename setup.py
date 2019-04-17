from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='log_parser',
    version='1.0',
    description='Parser',
    long_description=long_description,
    author='Gukov Aleksey',
    author_email='gukov.mail@yandex.ru',
    packages=['log_parser'],
    install_requires=['pytest'],
)
