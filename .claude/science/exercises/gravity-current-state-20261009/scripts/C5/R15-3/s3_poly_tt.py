"""R15-3 s3: dimension of the space of homogeneous polynomial Sym^2-valued fields T(k) of degree d that are
TT at every k (k_a T_ab(k) = 0 and T_aa(k) = 0 identically). Exact (sympy rational linear algebra).
Also: 'transverse only' (k_a T_ab = 0) and 'TT up to a helicity-0 admixture' are reported for comparison.
Used in Lemma N (gyro-free soft class): degree 1 and degree 2 TT fields must vanish."""
import itertools, sympy as sp
k = sp.symbols('k1 k2 k3')
def monos(d):
    return [sp.Mul(*[k[i]**e[i] for i in range(3)]) for e in itertools.product(range(d + 1), repeat=3) if sum(e) == d]
pairs = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
for d in range(0, 5):
    M = monos(d)
    coeffs = sp.symbols(f'c0:{6*len(M)}')
    T = [[0] * 3 for _ in range(3)]
    for p, (i, j) in enumerate(pairs):
        poly = sum(coeffs[p * len(M) + m] * M[m] for m in range(len(M)))
        T[i][j] = poly; T[j][i] = poly
    def nullity(eqs_polys):
        eqs = []
        for P in eqs_polys:
            P = sp.Poly(sp.expand(P), *k)
            eqs += [c for c in P.coeffs()]
        if not eqs: return len(coeffs)
        A = sp.Matrix([[sp.diff(e, c) for c in coeffs] for e in eqs])
        return len(coeffs) - A.rank()
    trans = [sum(k[a] * T[a][b] for a in range(3)) for b in range(3)]
    trace = [T[0][0] + T[1][1] + T[2][2]]
    n_T = nullity(trans)
    n_TT = nullity(trans + trace)
    print(f"degree {d}: unknowns {len(coeffs)}; transverse fields: {n_T}; TT fields: {n_TT}")
