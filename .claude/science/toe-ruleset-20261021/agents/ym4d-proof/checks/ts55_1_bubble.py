# ts55_1 -- exact constants of the free bubble coefficient c_bub = 12(N^2-1)/pi^4 (TSE55 section 2.4).
# Criteria: checks/ts55_1_criteria.md (written before this script). Exact arithmetic only.
from fractions import Fraction as Fr
import itertools, sys

POINTS4 = [(1, 2, 3, 4), (Fr(1, 2), -1, 2, 5), (3, -2, 1, Fr(7, 2)), (-1, -1, 4, 2),
           (2, 0, Fr(-3, 2), 1), (5, 1, -2, Fr(1, 2)), (Fr(3, 2), Fr(5, 2), -1, -3), (7, -3, 2, 1)]
POINTS3 = [(1, 2, 3), (Fr(1, 2), -1, 2), (3, -2, Fr(7, 2)), (-1, 4, 2), (2, Fr(-3, 2), 1), (5, 1, -2)]

def poly_P(d):
    # P(z) = sum z_a^2 as a dict {exponent tuple: coeff}
    P = {}
    for a in range(d):
        e = [0] * d; e[a] = 2; P[tuple(e)] = Fr(1)
    return P

def poly_eval(p, z):
    tot = Fr(0)
    for e, c in p.items():
        t = c
        for zi, ei in zip(z, e):
            t *= Fr(zi) ** ei
        tot += t
    return tot

def poly_diff(p, a):
    q = {}
    for e, c in p.items():
        if e[a] > 0:
            f = list(e); f[a] -= 1
            q[tuple(f)] = q.get(tuple(f), Fr(0)) + c * e[a]
    return q

def T_matrix(z):
    d = len(z)
    P = poly_P(d)
    Pz = poly_eval(P, z)
    dP = [poly_eval(poly_diff(P, a), z) for a in range(d)]
    ddP = [[poly_eval(poly_diff(poly_diff(P, a), b), z) for b in range(d)] for a in range(d)]
    # generic quotient rule for d_r d_m (1/P)
    return [[-ddP[m][r] / Pz**2 + 2 * dP[m] * dP[r] / Pz**3 for r in range(d)] for m in range(d)], Pz

def X_tensor(T, d):
    dl = lambda i, j: 1 if i == j else 0
    X = {}
    for m, n, r, s in itertools.product(range(d), repeat=4):
        X[(m, n, r, s)] = dl(n, s) * T[m][r] - dl(n, r) * T[m][s] - dl(m, s) * T[n][r] + dl(m, r) * T[n][s]
    return X

def trace_T2(T, d):
    return sum(T[i][j] * T[j][i] for i in range(d) for j in range(d))

def trace_T(T, d):
    return sum(T[i][i] for i in range(d))

res = {}
# A1 and A1-F, A3
A1 = True; A1F_differs = 0; A3 = True; vals = []
for z in POINTS4:
    T, Pz = T_matrix(z)
    X = X_tensor(T, 4)
    S = sum(v * v for v in X.values())
    closed = (4 * 4 - 8) * trace_T2(T, 4) + 4 * trace_T(T, 4) ** 2
    wrong = (4 * 4 - 4) * trace_T2(T, 4) + 4 * trace_T(T, 4) ** 2
    if S != closed or S * Pz**4 != 384:
        A1 = False
    if wrong != S:
        A1F_differs += 1
    S_unord = sum(X[(m, n, r, s)] ** 2 for m in range(4) for n in range(m + 1, 4) for r in range(4) for s in range(r + 1, 4))
    if S_unord != S / 4:
        A3 = False
    vals.append((z, S * Pz**4, S_unord * Pz**4))
res['A1'] = A1; res['A1-F differs at #points'] = A1F_differs; res['A3'] = A3
# A2 (d = 3)
A2_identity = True; A2_not384 = 0
for z in POINTS3:
    T, Pz = T_matrix(z)
    X = X_tensor(T, 3)
    S = sum(v * v for v in X.values())
    closed = (4 * 3 - 8) * trace_T2(T, 3) + 4 * trace_T(T, 3) ** 2
    if S != closed:
        A2_identity = False
    if S * Pz**4 != 384:
        A2_not384 += 1
res['A2 identity'] = A2_identity; res['A2 #points with S*P^4 != 384'] = A2_not384
# A4
S4 = Fr(384)  # S * P^4 in d = 4, certified by A1
plaq = 2 * (S4 / 4) / 16
clover = Fr(1, 32) * 16 * (S4 / 16)
clover_wrong = Fr(1, 32) * 4 * (S4 / 16)
res['A4 plaquette route'] = plaq; res['A4 clover route'] = clover; res['A4-F clover with 4 pairs'] = clover_wrong
# A5 generator normalisation and Taylor coefficient (sympy, exact)
import sympy as sp
def gens(N):
    if N == 2:
        s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
        return [m / 2 for m in (s1, s2, s3)]
    if N == 3:
        L = []
        L.append(sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
        L.append(sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]]))
        L.append(sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))
        L.append(sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]))
        L.append(sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]]))
        L.append(sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]))
        L.append(sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]]))
        L.append(sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3))
        return [m / 2 for m in L]
A5 = True; A5F_differs = 0
Fvecs = {2: [(1, 2, -1), (Fr(1, 2), 3, 2), (-2, 1, 1)],
         3: [(1, 0, 2, -1, 1, 0, 3, 1), (Fr(1, 2), 1, -1, 2, 0, 1, 1, -2), (2, 2, 1, 0, -1, 3, 0, 1)]}
for N in (2, 3):
    t = gens(N)
    for a in range(len(t)):
        for b in range(len(t)):
            v = sp.simplify((t[a] * t[b]).trace())
            if sp.simplify(v - (sp.Rational(1, 2) if a == b else 0)) != 0:
                A5 = False
    tt = sp.symbols('tt')
    for F in Fvecs[N]:
        Fs = [sp.Rational(Fr(x).numerator, Fr(x).denominator) for x in F]
        for wrongnorm in (False, True):
            gg = [g * (sp.sqrt(2) if wrongnorm else 1) for g in t]   # tr(gg_a gg_b) = delta if wrongnorm
            X = sp.sqrt(2 * N) * sum((Fs[a] * gg[a] for a in range(len(gg))), sp.zeros(N, N))
            # 1 - N^{-1} Re tr exp(i tt X) = (tt^2/(2N)) tr X^2 + O(tt^4): coefficient of tt^2 from tr(X^2)
            coeff2 = sp.nsimplify(sp.simplify((X * X).trace() / (2 * N)))
            target = sp.Rational(1, 2) * sum(f * f for f in Fs)
            if not wrongnorm and sp.simplify(coeff2 - target) != 0:
                A5 = False
            if wrongnorm and sp.simplify(coeff2 - target) != 0:
                A5F_differs += 1
    # independent check of the Taylor coefficient itself on one diagonal element: 1 - cos(th) series
    th = sp.symbols('th')
    ser = sp.series(1 - sp.cos(th), th, 0, 5).removeO()
    if sp.simplify(ser - (th**2 / 2 - th**4 / 24)) != 0:
        A5 = False
res['A5'] = A5; res['A5-F #differs (of 6)'] = A5F_differs

ok = (res['A1'] and res['A1-F differs at #points'] >= 1 and res['A2 identity'] and res['A2 #points with S*P^4 != 384'] >= 1
      and res['A3'] and plaq == 12 and clover == 12 and clover_wrong != 12 and res['A5'] and res['A5-F #differs (of 6)'] >= 1)
for k, v in res.items():
    print(k, ':', v)
print('per-point (z, S*P^4, Sunordered*P^4):')
for v in vals:
    print('  ', v)
print('VERDICT ts55_1:', 'PASS' if ok else 'FAIL')
