from prioBanChecker import __version__
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='classy-json',
    version=__version__,
    author='BGP#0419',
    description='A funtion to check if you are banned from donate.2b2t.org',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BGP0/Prio-ban-checker',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)