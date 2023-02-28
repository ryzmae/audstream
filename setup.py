from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = ''
LONG_DESCRIPTION = ''

# Setting up
setup(
    name="audstream",
    version=VERSION,
    author="ryzmae (Ceeq9717)",
    author_email="<juwennagpal6@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['wave', 'pyaudio'],
    keywords=['python', 'audio', 'stream', 'audio stream'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ],
    options={
        'bdist_wheel': {
            'universal': True
        }
    }
)