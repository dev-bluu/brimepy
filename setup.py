import setuptools
import os
import codecs

cwd = os.path.abspath(os.path.dirname(__file__))


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='brimepy',
    version=get_version('brime/__init__.py'),
    author='雲華',
    description='An asynchronous API wrapper for the Brime API.',
    url='https://github.com/yunwah/brimepy',
    packages=setuptools.find_packages()
)
