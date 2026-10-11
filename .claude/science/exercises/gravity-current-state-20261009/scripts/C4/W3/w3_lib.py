"""Shared helpers for C4 / RW / W3 (same conventions as scripts/C4/W2/w2_stueckelberg_scalar.py).
Fields are functions of (t,x,y,z); plane waves exp(i(k x - w t)); a real bilinear term c*D1 f_a*D2 f_b
contributes M[ib,ia] += c s1 conj(s2)/4 and M[ia,ib] += c conj(s1) s2/4  (L = v^dag M v, period average).
Mode energy (Krein) sign: E = w v^dag (dM/dw) v at a null vector (Noether energy of a single-frequency mode)."""
import sympy as sp, numpy as np
t, x, y, z = sp.symbols('t x y z', real=True)
X = (x, y, z)
w, k = sp.symbols('omega k', positive=True)
F = lambda name: sp.Function(name)(t, x, y, z)
def grad(f): return [sp.diff(f, v) for v in X]
def dot(u, v): return sum(ui*vi for ui, vi in zip(u, v))
def lap(f): return sum(sp.diff(f, v, 2) for v in X)
def dt(f, n=1): return sp.diff(f, t, n)

def vary(L, subs):
    s = sp.symbols('s_var')
    Ls = L.subs({f: f + s*d for f, d in subs.items()}, simultaneous=True)
    return sp.expand(sp.diff(Ls, s).subs(s, 0))

def euler_zero(expr, fields):
    """True iff expr is a total divergence: Euler-Lagrange derivative vanishes for every field in it."""
    funcs = [f for f in expr.atoms(sp.Function) if f.args == (t, x, y, z)]
    for f in funcs:
        res = sp.euler_equations(expr, [f], [t, x, y, z])
        el = res[0].lhs if res else 0
        if sp.simplify(sp.expand(el)) != 0:
            return False, f, sp.simplify(el)
    return True, None, None

def fourier_matrix(L, fields):
    L = sp.expand(L.doit())
    n = len(fields)
    def sym(fac):
        if isinstance(fac, sp.Derivative):
            mult = 1
            for var, cnt in fac.variable_count:
                if var == t: mult *= (-sp.I*w)**cnt
                elif var == x: mult *= (sp.I*k)**cnt
                else: mult *= 0
            return fields.index(fac.expr), mult
        return fields.index(fac), 1
    M = sp.zeros(n, n)
    for term in sp.Add.make_args(L):
        coeff, facs = sp.Integer(1), []
        for fac in sp.Mul.make_args(term):
            if isinstance(fac, sp.Derivative) or (isinstance(fac, sp.Function) and fac.args == (t, x, y, z)):
                facs.append(fac)
            elif isinstance(fac, sp.Pow) and fac.exp == 2 and (isinstance(fac.base, (sp.Derivative,)) or (isinstance(fac.base, sp.Function) and fac.base.args == (t, x, y, z))):
                facs += [fac.base, fac.base]
            else:
                coeff *= fac
        if len(facs) == 0:
            continue
        if len(facs) != 2:
            raise ValueError(f"non-quadratic term {term}")
        (ia, s1), (ib, s2) = sym(facs[0]), sym(facs[1])
        M[ib, ia] += coeff*s1*sp.conjugate(s2)/4
        M[ia, ib] += coeff*sp.conjugate(s1)*s2/4
    return sp.simplify(M)

def spectrum_tools(M, params):
    """Return (coef_fun, Mfun, dMfun): det M as polynomial in W = w^2 with coefficients lambdified in (k, *params)."""
    W = sp.symbols('W')
    det = sp.expand(sp.simplify(M.det()))
    det = sp.expand(det.subs(w, sp.sqrt(W)))
    if det.has(sp.sqrt(W)):
        raise ValueError("det not even in w")
    poly = sp.Poly(det, W)
    coeffs = poly.all_coeffs()
    cf = sp.lambdify((k, *params), coeffs, 'numpy')
    Mf = sp.lambdify((w, k, *params), M, 'numpy')
    dMf = sp.lambdify((w, k, *params), sp.diff(M, w), 'numpy')
    return cf, Mf, dMf, poly

def classify(cf, Mf, dMf, kval, pv, rtol=1e-7):
    c = np.array(cf(kval, *pv), dtype=complex)
    # strip leading (near-)zeros
    nz = np.flatnonzero(np.abs(c) > 1e-14*np.max(np.abs(c)))
    c = c[nz[0]:]
    roots = np.roots(c) if len(c) > 1 else np.array([])
    out = []
    for r in roots:
        if abs(r.imag) > rtol*max(1.0, abs(r)):
            out.append(('COMPLEX', r)); continue
        r = r.real
        if r < 0:
            out.append(('TACHYON', r)); continue
        if r == 0:
            out.append(('ZERO', r)); continue
        wv = np.sqrt(r)
        Mv = np.array(Mf(wv, kval, *pv), dtype=complex)
        u, s, vh = np.linalg.svd(Mv)
        v = vh[-1].conj()
        E = wv*np.real(v.conj() @ np.array(dMf(wv, kval, *pv), dtype=complex) @ v)
        out.append(('healthy' if E > 0 else 'GHOST', r))
    return out
