from setuptools import setup, find_packages

setup(
    name='openpy-pkg',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        "colorama"
    ],
    author='Corbin Chandler',
    author_email='corbinchandler777@icloud.com',
    description='OpenPython is a python package that allows users to collaborate to make the best python package available!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/thatcodingdonut/openpython',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
