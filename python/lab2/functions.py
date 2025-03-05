TOO_MANY_ITERATIONS = -1
OUT_OF_BOUNDS = -2
DIVISION_BY_ZERO = -3

def firstDerivative(func, x, eps, dx_first=1e-3):
    iters = 0
    dx = dx_first
    dy = func(x + dx) - func(x)
    deriv_prev = dy / dx
    while True:
        iters += 1
        dx = dx * 0.5
        dy = func(x + dx) - func(x)
        try:
            deriv_cur = dy / dx
        except:
            return iters, deriv_prev
        
        if abs(deriv_cur - deriv_prev) < eps:
            return iters, deriv_cur
        
        deriv_prev = deriv_cur
        

# def secondDerivative(func, x, h=1e-6):
#     return (func(x+h) + func(x-h) - 2*func(x))/(h**2)

def findRoot(func, x, a, b, eps, n_max):
    iters = 0
    while True:
        iters += 1
        if iters > n_max:
            return TOO_MANY_ITERATIONS, x

        try:
            cur_iters, derivative = firstDerivative(func, x, eps)
            delta = func(x)/derivative
            x -= delta
            iters += cur_iters
        except ZeroDivisionError:
            return DIVISION_BY_ZERO, 0

        if not(a-1e-4 <= x <= b+1e-4):
            return OUT_OF_BOUNDS, 0

        if abs(delta) < eps:
            return iters, x
        
def findVertexPoints(func, x, a, b, eps, n_max):
    return findRoot(lambda x: firstDerivative(func, x, eps), x, a, b, eps, n_max)

# def findInflectionPoints(func, start, a, b, eps, n_max):
#     return findRoot(lambda x: secondDerivative(func, x), start, a, b, eps, n_max)

if __name__ == "__main__":
    f = lambda x: x**2
    print(findRoot(f, 10, 0, 100, 0.0000001, 100))
