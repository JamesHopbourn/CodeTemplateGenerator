# setup.py

from setuptools import setup, find_packages

setup(
    name='Simple Code Template Generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'jinja2', 'argparse'
    ],
    entry_points={
        'console_scripts': [
            'cgen = CodeTemplateGenerator.generator:main',
        ],
    },
)
