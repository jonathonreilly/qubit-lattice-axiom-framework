"""F1 part 1b (replaces the open-box count for wide stencils, where boundary rows drop out):
infinite-lattice Killing fields of a local linearized gauge map D, exactly.

Translation-invariant D: solutions of D xi = 0 are exponential polynomials whose frequencies are
the points where the symbol D(k) (10x4) drops rank.
 (i)  polynomial solutions (frequency 0): exact sympy solve with a degree<=3 polynomial ansatz on
      the infinite lattice; expected exactly the 10 (4D) / 6 (3D) affine Killing fields.
 (ii) other frequencies: rank of D(k) at k != 0 (real random, and the complex zero set of the
      1D stencil s(k)).  For the K7a/IMP/AVG structure s_m xi_n + s_n xi_m the rank drops only
      where every s_m(k_m)=0, i.e. a finite set mod 2 pi.
"""
import sympy as sp, itertools, numpy as np

def stencil_terms(st):
    if st == 'K7a': return [(1, 1), (0, -1)]
    if st == 'IMP': return [(1, sp.Rational(27, 24)), (0, -sp.Rational(27, 24)), (2, -sp.Rational(1, 24)), (-1, sp.Rational(1, 24))]
    if st == 'BAD': return None

def solve_poly(dim, st, deg=3):
    X = sp.symbols('x0:%d' % dim)
    monos = [m for m in itertools.product(range(deg+1), repeat=dim) if sum(m) <= deg]
    coef = {}
    xi = []
    for nu in range(dim):
        expr = 0
        for m in monos:
            c = sp.Symbol(f'c_{nu}_' + '_'.join(map(str, m))); coef[c] = 1
            expr += c * sp.prod([X[i]**m[i] for i in range(dim)])
        xi.append(expr)
    def shift(f, mu, a):
        return f.subs(X[mu], X[mu] + a)
    def nab(m, f, n_comp):
        if st == 'BAD':
            c = 2 if m == 0 else 1
            return c*(shift(f, m, 1) - f)
        if st == 'AVG':
            rs = [r for r in range(dim) if r not in (m, n_comp)]
            if not rs: return shift(f, m, 1) - f
            tot = 0
            for r in rs:
                for sg in (1, -1):
                    g = shift(f, r, sg)
                    tot += shift(g, m, 1) - g
            return tot / (2*len(rs))
        return sum(c * shift(f, m, a) for a, c in stencil_terms(st))
    eqs = []
    for m in range(dim):
        for n in range(m, dim):
            e = sp.expand(nab(m, xi[n], n) + nab(n, xi[m], m))
            P = sp.Poly(e, *X)
            eqs += list(P.coeffs())
    sol = sp.linsolve(eqs, list(coef))
    sol = list(sol)[0]
    free = set()
    for s in sol: free |= s.free_symbols
    return len(free), [sp.expand(x.subs(dict(zip(coef, sol)))) for x in xi]

for dim in (3, 4):
    for st in ('K7a', 'IMP', 'AVG', 'BAD'):
        nfree, gen = solve_poly(dim, st, deg=3 if dim == 3 else 2)
        print(f"d={dim} stencil {st}: polynomial Killing fields (degree<= {3 if dim==3 else 2}) dimension = {nfree}")
    print()

# (ii) symbol rank away from k = 0
k = sp.symbols('k')
for st in ('K7a', 'IMP'):
    s = sum(c * sp.exp(sp.I*a*k) for a, c in stencil_terms(st))
    zs = sp.solve(sp.Eq(sp.simplify(s*sp.exp(sp.I*k/2)), 0), k) if st == 'K7a' else None
    # IMP: s = e^{ik/2}(27*2i sin(k/2) - 2i sin(3k/2))/24 -> zeros: sin(x)=0 or sin^2 x = -6 (x=k/2)
    print(f"stencil {st}: 1D symbol s(k) =", sp.simplify(sp.expand(s)))
print("IMP zeros: 27 sin x = sin 3x  <=>  sin x (24 + 4 sin^2 x) = 0 : real zeros only x in pi Z (k in 2 pi Z);")
print("           complex zeros sin^2 x = -6 (finite set mod 2 pi) -> finitely many extra exponential (non-tempered) kernel modes.")
rng = np.random.default_rng(0)
def Dk(kv, st, dim):
    if st == 'K7a': s = np.exp(1j*kv) - 1
    else: s = (27*(np.exp(1j*kv)-1) - (np.exp(2j*kv) - np.exp(-1j*kv)))/24
    rows = []
    for m in range(dim):
        for n in range(m, dim):
            r = np.zeros(dim, complex); r[n] += s[m]; r[m] += s[n]; rows.append(r)
    return np.array(rows)
for st in ('K7a', 'IMP'):
    mins = min(np.linalg.svd(Dk(rng.uniform(-np.pi, np.pi, 4), st, 4), compute_uv=False)[-1] for _ in range(2000))
    print(f"{st}: min over 2000 random real k of the 4th singular value of D(k) = {mins:.3e} (>0: rank 4 off k=0)")
