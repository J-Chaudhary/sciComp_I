#Student: Jignesh Chaudhary
#Student Id : 197320
#Research Paper : Computing of chemical engineering process finding a value of x to satisfy given mole function
# of H2O using Bisection and Newton-Raphson method
import _plot

def f(x): return 0.0025*(x**3) - 6*(x**2) - 0.0075 * x + 0.005
_plot.graph(f, xl = 0, xu = 0.05)
def bisect(f, xl, xu, es100=.5, imax=10000, debug=False, tab=10):
    xl,xu = float(xl),float(xu)
    ea = 1.0  #assume 100% relative error to begin
    iter = 0
    x0 = xl
    if debug and tab:
        print('{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}'
              .format('iter','xl','xu','xr','ea', t=tab))
    while True:
        xr = (xl + xu) / 2.
        iter += 1
        if xr: ea = abs(1 - x0/xr)
        if debug:
            print(('{:<{t}}{:<{t}.4}{:<{t}.4}{:<{t}.4}{:<{t}.4%}' if tab
                   else'iter={}, xl={}, xu={}, xr={}, ea={:%}')
                  .format(iter, xl, xu, xr, ea, t=tab))
        test = f(xl)*f(xr)
        if test < 0: xu = xr
        elif test > 0: xl = xr
        else: ea = 0.
        if ea*100 < es100 or iter >= imax:
            break
        x0 = xr
    return xr


def df(x): return 0.0075*x**2 - 12*x - 0.0075

def newton(f, df, x0, es100=1.00, imax=1000, debug=False):
    x0 = float(x0)
    iter = 0
    while True:
        xr = (x0) - f(x0) / df(x0)
        if xr:  ea = abs(1 - x0/xr)
        if ea*100 < es100 or iter > imax:
            break
        iter += 1
        x0 = xr
        if debug: print('iter={}, xr={:.5f}, ea={:%}'.format(iter, xr, ea))
    return xr

print("Result of Bisection Method:")
bisect(f, xl = 0, xu = 0.05, es100=.10, debug=True)
print("\n")
print("Result of Newton-Raphson Method:")
newton(f, df, x0=0.05, debug=True)
