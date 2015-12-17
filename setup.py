from setuptools import setup, find_packages

setup(
    name = 'Improved_Boids',
    version = '1.0',
    packages = find_packages(exclude = ['*test']),
    scripts = ['scripts/runBoids.py'],
    install_requires = ['numpy','matplotlib','pyyaml']
)
