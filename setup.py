from setuptools import setup

setup(
    name='finnhub',
    version='0.1.0',
    author='s0h3ck',
    author_email='s0h3ck@gmail.com',
    description='Finnhub API Python client',
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
