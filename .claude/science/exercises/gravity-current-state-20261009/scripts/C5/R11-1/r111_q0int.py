"""R11-1 helper: closed-form Euclidean frequency integrals, derived with sympy by residues, as rational functions of p0.
K[j][n](p0, a, b) = int dr/(2pi) r^n / ((r^2 + b^2) ((p0 - r)^2 + a^2)^j),   j = 1 (n = 0..2), j = 2 (n = 0..4).
Derived for real p0 (upper-half-plane poles r = i b and r = p0 + i a), then simplified to one rational function, whose
analytic continuation to p0 = i E (E < a + b, below threshold) is the Wick-rotated on-shell value.
Self-test: numerical quadrature at real p0; and I_0 continuation against the old-fashioned-PT form
(1/(2ab)) * (1/2) [1/(a+b-E) + 1/(a+b+E)].
"""
import sympy as sp, numpy as np, pickle, os
from scipy.integrate import quad

r, p0 = sp.symbols('r p0')
a, b = sp.symbols('a b', positive=True)

def derive(n, j):
    f = r ** n / ((r ** 2 + b ** 2) * ((p0 - r) ** 2 + a ** 2) ** j)
    res = sp.residue(f, r, sp.I * b) + sp.residue(f, r, p0 + sp.I * a)
    val = sp.I * res          # (1/2pi) * 2 pi i * sum Res
    return sp.factor(sp.cancel(sp.together(val)))

HERE = os.path.dirname(os.path.abspath(__file__))
PK = os.path.join(HERE, 'r111_q0int.pkl')

def get_funcs():
    if os.path.exists(PK):
        exprs = pickle.load(open(PK, 'rb'))
    else:
        exprs = {(j, n): derive(n, j) for j, ns in [(1, range(3)), (2, range(5))] for n in ns}
        pickle.dump(exprs, open(PK, 'wb'))
    return {key: sp.lambdify((p0, a, b), e, 'numpy') for key, e in exprs.items()}, exprs

if __name__ == '__main__':
    F, ex = get_funcs()
    for key, e in ex.items():
        print(key, ' denominator:', sp.factor(sp.denom(e)))
    rng = np.random.default_rng(1)
    worst = 0.0
    for _ in range(20):
        P0, A, Bv = rng.uniform(-2, 2), rng.uniform(0.05, 2), rng.uniform(0.3, 3)
        for (j, n), f in F.items():
            num = quad(lambda x: x ** n / ((x * x + Bv * Bv) * ((P0 - x) ** 2 + A * A) ** j), -np.inf, np.inf, limit=400)[0] / (2 * np.pi)
            v = complex(f(P0, A, Bv))
            worst = max(worst, abs(v - num) / max(abs(num), 1e-12), abs(v.imag))
    print('max rel. deviation, closed form vs quadrature (real p0), and max |imag|: %.2e' % worst)
    E, A, Bv = 0.9, 0.3, 1.0
    ofpt = (1 / (2 * A * Bv)) * 0.5 * (1 / (A + Bv - E) + 1 / (A + Bv + E))
    print('I_0 continued to p0 = iE: %.12f  old-fashioned PT: %.12f' % (complex(F[(1, 0)](1j * E, A, Bv)).real, ofpt))
