from setuptools import setup
from Cython.Build import cythonize

setup(
    name='AS1F555',
    version='0.0.0',
    py_modules=['AS1F555'],
    ext_modules=cythonize('AS1F555.py'),
)
