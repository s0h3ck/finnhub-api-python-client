from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='finnhub',
    version='0.1.1',
    author='s0h3ck',
    author_email='s0h3ck@gmail.com',
    description='Finnhub API Python client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['finnhub'],
    url='https://github.com/s0h3ck/finnhub-api-python-client/',
    license='MIT',
    install_requires=['requests'],
    keywords='finnhub api stocks cryptocurrency',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
