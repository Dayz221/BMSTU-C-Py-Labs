TOO_MANY_ITERATIONS = -1
OUT_OF_BOUNDS = -2

def findDerivative(func, x, eps):
    dx = 1
    dy = func(x + dx) - func(x)
    answ_last = dy/dx
    iters = 0
    while True:
        dx /= 2
        dy = func(x + dx) - func(x)
        answ_cur = dy/dx
        
        if abs(answ_cur-answ_last) < eps:
            return iters, answ_cur
        
        answ_last = answ_cur
        
        iters += 1

def findRoot(func, start, a, b, eps, n_max):
    x = start
    summ_iters = 0
    while True:
        iters, derivative = findDerivative(func, x, eps)
        summ_iters += iters + 1
        if summ_iters > n_max:
            return TOO_MANY_ITERATIONS, x

        delta = func(x)/derivative
        x -= delta

        if not(a <= x <= b):
            return OUT_OF_BOUNDS, 0

        if abs(delta) < eps:
            return summ_iters, x

if __name__ == "__main__":
    f = lambda x: x**2
    print(findRoot(f, 10, 0, 100, 0.0000001, 100))
