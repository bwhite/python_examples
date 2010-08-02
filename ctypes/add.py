import numpy as np
import ctypes


_libadd = np.ctypeslib.load_library('libadd', '.')
_libadd.add_with_c.restype = ctypes.c_double
_libadd.add_with_c.argtypes = [ctypes.c_double, ctypes.c_double]


def add_with_c(a, b):
    """Takes two numbers, returns their sum computed using a C library.

    Args:
        a: float
        b: float
    Returns:
        The sum of a and b
    """
    return _libadd.add_with_c(a, b)


if __name__ == '__main__':
    # Here is a simple test
    a, b = np.random.random(), np.random.random()
    c = add_with_c(a, b)
    print('%f + %f = %f' % (a, b, c))
