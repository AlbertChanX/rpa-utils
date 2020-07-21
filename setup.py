from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requires = f.readlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='rpa-utils',
    version='1.0.1',
    py_modules=['rpa_utils'],
    install_requires=requires,
    python_requires='>=3.6',
    packages=find_packages(),
    author='Albert Chan',
    description='a Python package for RPA (robotic process automation)',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
