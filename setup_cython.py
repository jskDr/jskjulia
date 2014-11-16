# To compile cython files, type below on shell
# $ python setup_cython.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("f_cython.pyx")
)