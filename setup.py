from setuptools import setup, find_packages

setup(
    name = 'Improved_Bad-Boids',
    version = '1.0',
    packages = find_packages(exclude = ['*test']),
    scripts = ['scripts/bad_boids.py'],
    install_requires = ['numpy','matplotlib','random','yaml','os']
)
