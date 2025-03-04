TOO_MANY_ITERATIONS = -1
OUT_OF_BOUNDS = -2
DEVISIO_BY_ZERO = -3

def firstDerivative(func, x, h=1e-6):
    return (func(x+h)-func(x-h))/(2*h)

# def secondDerivative(func, x, h=1e-6):
#     return (func(x+h) + func(x-h) - 2*func(x))/(h**2)

def findRoot(func, start, a, b, eps, n_max):
    x = start
    iters = 0
    while True:
        iters += 1
        if iters > n_max:
            return TOO_MANY_ITERATIONS, x

        try:
            delta = func(x)/firstDerivative(func, x, eps)
            x -= delta
        except:
            return DEVISIO_BY_ZERO, 0

        if not(a <= x <= b):
            return OUT_OF_BOUNDS, 0

        if abs(delta) < eps:
            return iters, x
        
def findVertexPoints(func, start, a, b, eps, n_max):
    return findRoot(lambda x: firstDerivative(func, x), start, a, b, eps, n_max)

# def findInflectionPoints(func, start, a, b, eps, n_max):
#     return findRoot(lambda x: secondDerivative(func, x), start, a, b, eps, n_max)

if __name__ == "__main__":
    f = lambda x: x**2
    print(findRoot(f, 10, 0, 100, 0.0000001, 100))
