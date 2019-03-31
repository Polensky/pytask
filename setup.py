from setuptools import setup, find_packages

setup(
    name='pytask',
    version='0.1',
    packages=find_packages(exclude=('test', )),
    long_description=open('README.md').read(),
    scripts=('bin/pytask',)
)
