from setuptools import setup, find_packages

setup(
    name = 'Improved_Boids',
    version = '1.0.0',
    author = 'Oscar Bennett',
    licence = 'The MIT License',
    description = 'An improved refactored version of the BadBoids code',
    packages = find_packages(exclude = ['*test']),
    scripts = ['scripts/runBoids'],
    install_requires = ['numpy','matplotlib','pyyaml']
)
