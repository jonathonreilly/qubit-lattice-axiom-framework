import sympy as sp
t = sp.Symbol('t'); C,S = sp.symbols('C S')
def tcoeffs(e):
    e = sp.expand(sp.expand_trig(sp.expand(e)))
    e = sp.expand(e.subs({sp.cos(t): C, sp.sin(t): S}))
    assert not e.has(t), e
    P = sp.Poly(e, S); out = 0
    for (k,), co in P.terms(): out += co * S**(k%2) * (1-C**2)**(k//2)
    P = sp.Poly(sp.expand(out), C, S)
    return [sp.expand(co) for co in P.coeffs()]
