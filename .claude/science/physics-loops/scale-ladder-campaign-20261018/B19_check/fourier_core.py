"""B19 check core (written fresh; imports nothing from B14/B16/B19).

Different path from B19's jet calculus:
  * fields are sympy Functions of (x0,x1,x2); variational derivatives use sympy's own euler_equations;
  * a local multilinear functional int E is tested for identical vanishing by its Fourier kernel:
    each field slot -> amplitude * exp(i k.x) (repeated slots are polarised), the kernel must vanish
    on the momentum-conservation surface sum k = 0.  (No Euler-operator zero test.)
"""
from __future__ import annotations
import sympy as sp
from sympy.calculus.euler import euler_equations

X = sp.symbols("x0 x1 x2", real=True)
I = sp.I


def Fn(name):
    return sp.Function(name)(*X)


def vd(dens, f):
    """variational derivative delta int dens / delta f via sympy euler_equations (f a Function application)."""
    if not dens.has(f.func):
        return sp.Integer(0)
    eq = euler_equations(dens, [f], list(X))[0]
    return sp.expand(eq.lhs)


def pb(Fd, Gd, pairs):
    out = 0
    for q, p in pairs:
        a = vd(Fd, q)
        b = vd(Gd, p)
        c = vd(Fd, p)
        d = vd(Gd, q)
        out += a * b - c * d
    return sp.expand(out)


class Slot:
    """a group of component functions sharing one momentum; mult = how many copies (polarisation)."""
    def __init__(self, name, comps, mult=1):
        self.name, self.comps, self.mult = name, comps, mult


def fourier_kernel(expr, slots):
    """polarised Fourier kernel of int expr; returns (kernel poly, list of momentum symbol triples, amplitude symbols).
    The last copy of the last slot carries momentum -(sum of the others)."""
    expr = sp.expand(expr)
    copies = []  # (slot, r)
    for s in slots:
        for r in range(s.mult):
            copies.append((s, r))
    ks = [sp.symbols(f"k_{s.name}{r}_0:3") for (s, r) in copies]
    amps = {}
    # polarise
    t = sp.symbols(f"t0:{len(copies)}")
    sub = {}
    ci = 0
    for s in slots:
        for c in s.comps:
            newsum = 0
            for r in range(s.mult):
                idx = copies.index((s, r))
                g = sp.Function(f"{c.func.__name__}__{r}")(*X)
                newsum += t[idx] * g
            sub[c] = newsum
    e = expr.subs(sub).doit()
    e = sp.expand(e)
    mono = sp.Mul(*t)
    e = sp.Poly(e, *t).coeff_monomial(mono) if e != 0 else sp.Integer(0)
    # replace by plane waves
    def amp(fname):
        if fname not in amps:
            amps[fname] = sp.Symbol("A_" + fname)
        return amps[fname]
    kof = {}
    for s in slots:
        for c in s.comps:
            for r in range(s.mult):
                idx = copies.index((s, r))
                kof[f"{c.func.__name__}__{r}"] = ks[idx]

    def rep_der(d):
        f = d.expr
        fname = f.func.__name__
        k = kof[fname]
        fac = amp(fname)
        for v, n in d.variable_count:
            j = X.index(v)
            fac *= (I * k[j]) ** n
        return fac
    e = e.replace(lambda a: isinstance(a, sp.Derivative), rep_der)
    e = e.replace(lambda a: isinstance(a, sp.core.function.AppliedUndef) and a.func.__name__ in kof,
                  lambda a: amp(a.func.__name__))
    # momentum conservation
    last = ks[-1]
    tot = [sum(k[j] for k in ks[:-1]) for j in range(3)]
    e = sp.expand(e.subs({last[j]: -tot[j] for j in range(3)}))
    return e, ks[:-1], list(amps.values())


def kernel_eqs(expr, slots):
    e, ks, amps = fourier_kernel(expr, slots)
    if e == 0:
        return []
    gens = [x for k in ks for x in k] + amps
    P = sp.Poly(e, *gens)
    return [c for c in P.coeffs() if c != 0]


def is_zero(expr, slots):
    return len(kernel_eqs(expr, slots)) == 0
