from setuptools import setup, find_packages

reqs=[]
ver="0.0.0"

with open("./requirements.txt", 'r+') as f:
    for line in f.readlines():
        reqs.append(line.replace("\n", ""))

with open("./.version", "r+") as f:
    ver = f.read()

setup(
    name='openpy-pkg',
    version='{}'.format(ver),
    packages=find_packages(),
    install_requires=reqs,
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
