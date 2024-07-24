# setup.py
from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='easy_yt',
    version='0.1',
    packages=find_packages(),
    install_requires=required_packages,
    description='A simple wrapper for yt-dlp to make downloading videos easier.',
    author='Manish Kumar',
    url='https://github.com/mnsdojo/easy_yt',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
