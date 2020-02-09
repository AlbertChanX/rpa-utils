from setuptools import setup, find_packages

requires = []
with open('requirements.txt', 'r') as f:
    requires = f.readlines()

setup(
    name='rpa-utils',
    version='1.0.0',
    py_modules=['rpa_utils'],
    install_requires=requires,
    python_requires='>=3.6',
    packages=find_packages(),
    author='Albert Chan',
    description='a Python package for RPA (robotic process automation)'
)
