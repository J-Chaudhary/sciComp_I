# Hands-on Topic 5
#Student: Jignesh Chaudhary, Student id:197320
# 5.3 Determine the real root of f (x) = -25 + 82x - 90x^2 + 44x^3 - 8x^4 + 0.7x^5:
# (a) Graphically.
# (b) Using bisection to determine the root to es = 10%. Employ initial guesses of xl = 0.5 and xu = 1.0.
# (c) Perform the same computation as in (b) but use the false position method and es = 0.2%.

import _plot

def f(x): return -25 + 82*x - 90*(x**2) + 44*(x**3) - 8*(x**4) + 0.7*(x**5)

_plot.graph(f, xl = 0.5, xu = 1.0)

def bisect(f, xl, xu, es100=.5, imax=1000, debug=False, tab=10):
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

def falsepos(f, xl, xu, es100=.5, imax=1000, debug=False, tab=10):
    xl,xu = float(xl),float(xu)
    ea = 1.0  #assume 100% relative error to begin
    iter = 0
    x0 = xl
    if debug and tab:
        print('{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}'
              .format('iter','xl','xu','xr','ea', t=tab))
    while True:
        xr = (xl * f(xu)-xu*f(xl)) / (f(xu) - f(xl))
        iter += 1
        if xr:  ea = abs(1 - x0/xr)
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

print("bisect:")
bisect(f, xl = 0.5, xu = 1.0, es100=.10, debug=True)#es = 10% hence, es100=.10
print("\n")
print("falsepos:")
falsepos(f, xl = 0.5, xu = 1.0, es100=.0002, debug=True)#es = .02% hence, es100=.0002
