from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example pyton packages',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/iyinoluwa60/mypackage',
    author='Oluwawapelumi Joseph',
    author_email='pelzy60@gmail.com'
)