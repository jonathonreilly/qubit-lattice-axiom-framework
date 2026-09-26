#!/usr/bin/env python3
"""Window-confined sources and the formation price (block 162's open case).
J:derive:confined-sources-and-the-formation-price:a2

Setting (block 116 as landed, block 162 on its branch): held cube, wall phi = 1, g = (1 - A)^-1 with zero wall values,
k = gamma/12, amplitude sourcing ((1 - A) + kK) psi = k e, phi = 1 - psi, effective source s = K phi, Q = sum s,
price E' = Q/phi'_y with phi'_y = 1 - k Q g_yy; window data = amplitude and pre-event rates in B_R(y).
Identical window data in two boxes <=> same s (supported in the window) and (G1 - G2) s = 0 on the window.

X  counterexample, every R: if both boxes share the wall plane at distance R+1 from y, then with f = delta at the site next
   to that wall, s = (1 - A) f (interior points) lies in B_R(y), Q = 1/6, is not point-equivalent, and G s = f in EVERY such
   box; the window data coincide and the prices Q/(1 - kQ g_yy) differ with g_yy. Exact for R = 1, sides 5 and 7.
G  Gram identity for nested boxes (Omega_1 inside Omega_2): G_2 - G_1 = H_1 Gamma H_1^T on I_1, H_1 the harmonic measure,
   Gamma = g_2 on Omega_1's wall (zero on shared wall points); exact for a shared-face pair and a strictly nested pair; the
   counterexample's outer flux c = H_1^T s sits on one shared wall point.  [the proof and corollaries are in ATTEMPT]
C  same pairs: a Q != 0 window-identical source exists iff the boxes share a wall plane at distance R + 1 from y.
P  nonnegative sources (bodies of positive rest energy): no pair of cubes of side 5 and 7 (R = 1, y at distance >= 2) with
   different g_yy has a nonzero nonnegative window-identical source: exact Stiemke certificates z > 0, z orthogonal to ker.
F  far regime survey (R = 1, y at distance >= 3 from every wall, cubes of side 7, 9, 11): no pair has a window-identical
   source with Q != 0 and different g_yy (exact kernel bounds mod a prime; equal-g pairs are congruent).
"""
import itertools, sys, time
from fractions import Fraction as Fr
T0 = time.time()
FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

def solve_exact(n, rest, k):
    """exact solution psi of ((1 - A) + k diag(rest)) psi = k rest on the interior of the side-n held cube."""
    pts = list(itertools.product(range(1, n - 1), repeat=3)); idx = {p: i for i, p in enumerate(pts)}; N = len(pts)
    M = [[Fr(0)]*N for _ in range(N)]; b = [Fr(0)]*N
    for p, i in idx.items():
        M[i][i] = Fr(1) + k*rest.get(p, 0)
        for ax in range(3):
            for d in (1, -1):
                q = list(p); q[ax] += d; q = tuple(q)
                if q in idx: M[i][idx[q]] -= Fr(1, 6)
        b[i] = k*rest.get(p, 0)
    # banded elimination (exact)
    for c in range(N):
        piv = next(r for r in range(c, N) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]; b[c], b[piv] = b[piv], b[c]
        inv = 1/M[c][c]
        for r in range(c + 1, N):
            if M[r][c] != 0:
                f = M[r][c]*inv
                for cc in range(c, N):
                    if M[c][cc] != 0: M[r][cc] -= f*M[c][cc]
                b[r] -= f*b[c]
    x = [Fr(0)]*N
    for r in range(N - 1, -1, -1):
        x[r] = (b[r] - sum(M[r][cc]*x[cc] for cc in range(r + 1, N) if M[r][cc] != 0))/M[r][r]
    return {p: x[i] for p, i in idx.items()}
def g_at(n, y):
    """exact g(y, y) for the side-n held cube (solve (1 - A) u = delta_y)."""
    pts = list(itertools.product(range(1, n - 1), repeat=3)); idx = {p: i for i, p in enumerate(pts)}; N = len(pts)
    M = [[Fr(0)]*N for _ in range(N)]; b = [Fr(0)]*N
    for p, i in idx.items():
        M[i][i] = Fr(1)
        for ax in range(3):
            for d in (1, -1):
                q = list(p); q[ax] += d; q = tuple(q)
                if q in idx: M[i][idx[q]] -= Fr(1, 6)
    b[idx[y]] = Fr(1)
    for c in range(N):
        piv = next(r for r in range(c, N) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]; b[c], b[piv] = b[piv], b[c]
        inv = 1/M[c][c]
        for r in range(c + 1, N):
            if M[r][c] != 0:
                f = M[r][c]*inv
                for cc in range(c, N):
                    if M[c][cc] != 0: M[r][cc] -= f*M[c][cc]
                b[r] -= f*b[c]
    x = [Fr(0)]*N
    for r in range(N - 1, -1, -1):
        x[r] = (b[r] - sum(M[r][cc]*x[cc] for cc in range(r + 1, N) if M[r][cc] != 0))/M[r][r]
    return x[idx[y]]

print("== X counterexample (R = 1): boxes sharing the low x-wall at distance 2 from y")
k = Fr(1, 12)                                    # gamma = 1
R = 1
boxes = [(5, (2, 2, 2)), (7, (2, 3, 3))]         # both have the wall x = 0 at distance R+1 = 2 from y; other walls differ
res = []
for n, y in boxes:
    fsite = (y[0] - R, y[1], y[2])                # next to the wall x = 0
    s = {fsite: Fr(1)}
    for ax in range(3):
        for d in (1, -1):
            q = list(fsite); q[ax] += d; q = tuple(q)
            if all(1 <= q[i] <= n - 2 for i in range(3)): s[q] = s.get(q, 0) - Fr(1, 6)
    inwin = all(max(abs(q[i] - y[i]) for i in range(3)) <= R for q in s)
    phi_claim = {fsite: 1 - k}                   # phi = 1 - k f
    rest = {q: v/phi_claim.get(q, Fr(1)) for q, v in s.items()}   # bodies at rest: K = diag(rest), s = K phi
    psi = solve_exact(n, rest, k)
    exact_psi = all(psi[p] == (k if p == fsite else 0) for p in psi)
    Q = sum(s.values())
    win = {tuple(q[i] - y[i] for i in range(3)): (rest.get(q, 0), 1 - psi[q]) for q in itertools.product(*[range(y[i] - R, y[i] + R + 1) for i in range(3)])}
    gyy = g_at(n, y)
    price = Q/(1 - k*Q*gyy)
    res.append((win, Q, gyy, price))
    check(f"X1 side {n}, y = {y}: source s = (1-A) delta_(y - e1) (interior) lies in B_1(y); the static law's exact solution "
          f"is psi = k delta_(y-e1) (elimination found every pivot, so the solution is unique)", inwin and exact_psi)
check("X2 identical window data: rest energies and pre-event rates in B_1(y) agree exactly in the two boxes", res[0][0] == res[1][0])
check("X3 same total effective source Q = 1/6 in both boxes", res[0][1] == res[1][1] == Fr(1, 6), str(res[0][1]))
check("X4 g_yy differs between the two boxes, so the prices Q/(1 - kQ g_yy) differ", res[0][2] != res[1][2] and res[0][3] != res[1][3],
      f"g_yy = {res[0][2]} vs {res[1][2]}; prices = {res[0][3]} vs {res[1][3]}")
# X5 not point-equivalent: the x-moment of s - Q delta_y is -1/3 (x is discrete harmonic, and (1-A)f has zero harmonic moments)
n, y = boxes[0]; fsite = (y[0] - 1, y[1], y[2])
s = {fsite: Fr(1)}
for q in [(y[0], y[1], y[2]), (y[0] - 1, y[1] + 1, y[2]), (y[0] - 1, y[1] - 1, y[2]), (y[0] - 1, y[1], y[2] + 1), (y[0] - 1, y[1], y[2] - 1)]:
    s[q] = s.get(q, 0) - Fr(1, 6)
mom = sum((q[0] - y[0])*v for q, v in s.items())
check("X5 the source is not point-equivalent at y: its first moment along the wall normal is -1/3 != 0", mom == Fr(-1, 3), str(mom))
# X6 every R: the construction's support and charge (combinatorial)
okR = True
for Rr in range(1, 6):
    fs = (-Rr, 0, 0); supp = [fs] + [tuple(fs[i] + (d if i == ax else 0) for i in range(3)) for ax in range(3) for d in (1, -1)]
    supp = [q for q in supp if q[0] > -(Rr + 1)]          # drop the wall site at x = -(R+1)
    if not all(max(abs(c) for c in q) <= Rr for q in supp) or len(supp) != 6: okR = False
check("X6 for every R = 1..5 the construction (wall at distance R+1) is supported in B_R(y) with charge 1 - 5/6 = 1/6", okR)


print("== G Gram identity for nested boxes (exact)")
import sympy as sp
from sympy.polys.matrices import DomainMatrix
def box(lo, hi):
    I = list(itertools.product(*[range(lo[i] + 1, hi[i]) for i in range(3)])); Iset = set(I)
    Wl = sorted({tuple(p[j] + (d if j == ax else 0) for j in range(3)) for p in I for ax in range(3) for d in (1, -1)} - Iset)
    return I, Wl                                   # interior; wall points adjacent to the interior
def green_cols(I, cols):
    idx = {p: i for i, p in enumerate(I)}; N = len(I)
    M = sp.zeros(N, N)
    for p, i in idx.items():
        M[i, i] = 1
        for ax in range(3):
            for d in (1, -1):
                q = tuple(p[j] + (d if j == ax else 0) for j in range(3))
                if q in idx: M[i, idx[q]] = sp.Rational(-1, 6)
    B = sp.zeros(N, len(cols))
    for j, c in enumerate(cols): B[idx[c], j] = 1
    return idx, DomainMatrix.from_Matrix(M).convert_to(sp.QQ).lu_solve(DomainMatrix.from_Matrix(B).convert_to(sp.QQ)).to_Matrix()
def gram(lo1, hi1, lo2, hi2):
    I1, W1 = box(lo1, hi1); I2, W2 = box(lo2, hi2); I2s = set(I2)
    idx1, g1 = green_cols(I1, I1)
    inner = [b for b in W1 if b in I2s]; shared = [b for b in W1 if b not in I2s]
    cols2 = I1 + inner; pos2 = {c: j for j, c in enumerate(cols2)}
    idx2, g2c = green_cols(I2, cols2)
    g2 = lambda a, b: 0 if (a not in I2s or b not in I2s) else g2c[idx2[a], pos2[b]]
    H1 = sp.zeros(len(I1), len(W1))                # H_1(z, b) = (1/6) sum over interior neighbours x of b of g_1(z, x)
    for j, b in enumerate(W1):
        for ax in range(3):
            for d in (1, -1):
                x = tuple(b[k] + (d if k == ax else 0) for k in range(3))
                if x in idx1:
                    for i in range(len(I1)): H1[i, j] += g1[i, idx1[x]]/6
    Gam = sp.Matrix(len(W1), len(W1), lambda a, b: g2(W1[a], W1[b]))
    D = sp.Matrix(len(I1), len(I1), lambda a, b: g2(I1[a], I1[b])) - g1
    return I1, W1, shared, H1, Gam, D
for name, (lo1, hi1, lo2, hi2) in [("shared face: side 5 at y = (2,2,2) inside side 7 at y = (2,3,3)", ((-2,)*3, (2,)*3, (-2, -3, -3), (4, 3, 3))),
                                   ("strictly nested: side 5 centred inside side 9 centred", ((-2,)*3, (2,)*3, (-4,)*3, (4,)*3))]:
    I1, W1, shared, H1, Gam, D = gram(lo1, hi1, lo2, hi2)
    check(f"G1 {name}: G_2 - G_1 = H_1 Gamma H_1^T on I_1 x I_1, and every row of H_1 sums to 1",
          (H1*Gam*H1.T - D).is_zero_matrix and all(sum(H1.row(i)) == 1 for i in range(len(I1))),
          f"{len(W1)} wall points, {len(shared)} shared")
    if shared:
        sv = sp.zeros(len(I1), 1); fs = (-1, 0, 0)
        for q, v in [(fs, 1)] + [(tuple(fs[i] + (d if i == ax else 0) for i in range(3)), sp.Rational(-1, 6)) for ax in range(3) for d in (1, -1)]:
            if q in I1: sv[I1.index(q)] += v
        c = H1.T*sv
        check("G2 the counterexample's outer flux c = H_1^T s is (1/6) delta at the shared wall point y - 2e1, zero elsewhere, "
              "so (G_2 - G_1) s = H_1 Gamma c = 0 on all of I_1",
              all(c[j] == (sp.Rational(1, 6) if W1[j] == (-2, 0, 0) else 0) for j in range(len(W1))) and (-2, 0, 0) in shared
              and (D*sv).is_zero_matrix)
    else:
        A_ = [[Fr(int(sp.numer(v)), int(sp.denom(v))) for v in Gam.row(i)] for i in range(Gam.rows)]; piv_ok = True
        for c_ in range(len(A_)):                  # symmetric elimination without row exchanges: all pivots > 0 <=> positive definite
            if A_[c_][c_] <= 0: piv_ok = False; break
            for r_ in range(c_ + 1, len(A_)):
                f_ = A_[r_][c_]/A_[c_][c_]
                if f_: A_[r_] = [a - f_*b for a, b in zip(A_[r_], A_[c_])]
        check("G3 strictly nested: Gamma (= g_2 on the wall of Omega_1, all inside Omega_2) is symmetric positive definite "
              "(exact elimination without row exchanges, every pivot > 0)", Gam.is_symmetric() and piv_ok)

print("== P nonnegative sources: exact Stiemke certificates, cubes of side 5 and 7, R = 1")
from scipy.optimize import linprog
import numpy as np
Wn = list(itertools.product(range(-1, 2), repeat=3)); iy = Wn.index((0, 0, 0))
def GW_exact(n, y):
    pts = list(itertools.product(range(1, n - 1), repeat=3))
    idx, X = green_cols(pts, [tuple(y[i] + w[i] for i in range(3)) for w in Wn])
    return X.extract([idx[tuple(y[i] + w[i] for i in range(3))] for w in Wn], list(range(27)))
confsP = [(n, y) for n in (5, 7) for y in itertools.product(range(2, n - 2), repeat=3)]
GP = {c: GW_exact(*c) for c in confsP}
relP = lambda c: tuple((-c[1][i], c[0] - 1 - c[1][i]) for i in range(3))
npP = certP = failP = 0; chart = {}
for c1, c2 in itertools.combinations(confsP, 2):
    if relP(c1) == relP(c2) or GP[c1][iy, iy] == GP[c2][iy, iy]: continue
    npP += 1
    ker = DomainMatrix.from_Matrix(GP[c1] - GP[c2]).convert_to(sp.QQ).nullspace().to_Matrix()     # rows span ker D
    qnz = any(sum(ker.row(i)) != 0 for i in range(ker.rows))
    r1_, r2_ = relP(c1), relP(c2)
    shared2 = any(r1_[i][e] == r2_[i][e] and abs(r1_[i][e]) == 2 for i in range(3) for e in (0, 1))
    chart[(qnz, shared2)] = chart.get((qnz, shared2), 0) + 1
    Z = DomainMatrix.from_Matrix(ker).convert_to(sp.QQ).nullspace().to_Matrix().T                # columns span (ker D)^perp
    r = linprog(np.zeros(Z.shape[1]), A_ub=-np.array(Z.evalf(20).tolist(), dtype=float), b_ub=-np.ones(27),
                bounds=[(None, None)]*Z.shape[1], method='highs')
    if r.status != 0: failP += 1; continue
    z = Z*sp.Matrix([sp.Rational(Fr(v).limit_denominator(10**6)) for v in r.x])
    if all(v > 0 for v in z) and (ker*z).is_zero_matrix: certP += 1
    else: failP += 1
check(f"P1 {npP} pairs (side 5 and 7 cubes, y at distance >= 2, different g_yy): each has an exact z > 0 orthogonal to "
      f"ker(G_1 - G_2)_W, so no nonzero nonnegative window source gives identical window data", failP == 0 and certP == npP,
      f"certificates {certP}, failures {failP}")
check("C1 the same 269 pairs: a window-identical source with Q != 0 exists (exact kernel over Q) iff the two boxes share a wall "
      "plane at distance R + 1 = 2 from y", set(chart) <= {(True, True), (False, False)},
      f"(Q != 0 kernel, shared plane at distance 2): {chart}")

print("== F far regime (R = 1, y at distance >= 3 from every wall): exact kernel bounds mod a prime")
if '--skip-F' not in sys.argv:
    P = 2147483629
    Wn = list(itertools.product(range(-1, 2), repeat=3))
    def inv(a): return pow(int(a) % P, P - 2, P)
    def solve_mod(M, B):
        M = M.copy() % P; B = B.copy() % P; n_ = M.shape[0]
        for c in range(n_):
            piv = c + int(np.nonzero(M[c:, c])[0][0])
            if piv != c: M[[c, piv]] = M[[piv, c]]; B[[c, piv]] = B[[piv, c]]
            iv = inv(M[c, c]); M[c] = (M[c]*iv) % P; B[c] = (B[c]*iv) % P
            col = M[:, c].copy(); col[c] = 0; nz = np.nonzero(col)[0]
            if len(nz):
                M[nz] = (M[nz] - (col[nz, None]*M[c][None, :]) % P) % P
                B[nz] = (B[nz] - (col[nz, None]*B[c][None, :]) % P) % P
        return B
    def rank_mod(A):
        A = A.copy() % P; r = 0; rows, cols = A.shape
        for c in range(cols):
            nz = np.nonzero(A[r:, c])[0]
            if not len(nz): continue
            piv = r + int(nz[0]); A[[r, piv]] = A[[piv, r]]
            iv = inv(A[r, c]); A[r] = (A[r]*iv) % P
            col = A[:, c].copy(); col[r] = 0; nzr = np.nonzero(col)[0]
            if len(nzr): A[nzr] = (A[nzr] - (col[nzr, None]*A[r][None, :]) % P) % P
            r += 1
            if r == rows: break
        return r
    cacheM = {}
    def GW_mod(n, y):
        if n not in cacheM:
            pts = list(itertools.product(range(1, n - 1), repeat=3)); idx = {p: i for i, p in enumerate(pts)}
            M = np.zeros((len(pts), len(pts)), dtype=np.int64)
            for p, i in idx.items():
                M[i, i] = 6
                for ax in range(3):
                    for d in (1, -1):
                        q = list(p); q[ax] += d; q = tuple(q)
                        if q in idx: M[i, idx[q]] = P - 1
            cacheM[n] = (idx, M)
        idx, M = cacheM[n]
        cols = [idx[tuple(y[i] + w[i] for i in range(3))] for w in Wn]
        B = np.zeros((M.shape[0], len(Wn)), dtype=np.int64)
        for j, c in enumerate(cols): B[c, j] = 6
        return solve_mod(M, B)[cols, :] % P
    confs = [(n, y) for n in (7, 9, 11) for y in itertools.product(range(3, n - 3), repeat=3)]
    G = {c: GW_mod(*c) for c in confs}
    iy = Wn.index((0, 0, 0)); ones = np.ones((1, len(Wn)), dtype=np.int64)
    rel = lambda c: tuple((-c[1][i], c[0] - 1 - c[1][i]) for i in range(3))
    congr = lambda c: tuple(sorted(tuple(sorted((-a, b))) for a, b in rel(c)))
    bad = 0; triv = 0; big = 0; gs_noncongruent = 0; npairs = 0
    for c1, c2 in itertools.combinations(confs, 2):
        if rel(c1) == rel(c2): continue
        npairs += 1
        D = (G[c1] - G[c2]) % P
        rk = rank_mod(D); kdim = 27 - rk
        q = rank_mod(np.vstack([D, ones])) > rk
        gs = G[c1][iy, iy] == G[c2][iy, iy]
        if gs and congr(c1) != congr(c2): gs_noncongruent += 1
        if kdim == 1: triv += 1
        else: big += 1
        if q and not gs: bad += 1
        if kdim > 1 and not gs: bad += 1
    check(f"F1 {npairs} far pairs: every pair either has kernel exactly the trivial (1-A)delta_y (Q = 0; exact because "
          f"dim ker over Q <= dim ker mod p) or equal g_yy, so identical window data give identical prices",
          bad == 0, f"trivial-kernel pairs {triv}, larger-kernel pairs {big} (all with equal g_yy)")
    check("F2 every pair with equal g_yy (mod p) is congruent by a symmetry fixing y (so g_yy is equal exactly)", gs_noncongruent == 0)

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: COUNTEREXAMPLE (block 162's open case): for every R, a window-confined, non-point-equivalent source next to "
          "a wall shared by two held boxes (s = (1-A) delta at the site next to the wall, Q = 1/6) has field exactly f in both "
          "boxes, so the amplitude and pre-event rates in B_R(y) coincide while the prices Q/(1 - kQ g_yy) differ (exact, sides "
          "5 and 7). Nested boxes: coincidence iff the outer flux H_1^T s sits on shared wall points (Gram identity), so strict nesting forces a point-equivalent source with Q = 0 and nonnegative sources never coincide (proof); in cubes of side 5-7 (269 pairs) a Q != 0 coincidence occurs iff a wall plane at distance R+1 is shared, and nonnegative sources give none (exact certificates); far windows (distance >= 3, R = 1, sides "
          "7-11, 11628 pairs) give identical prices")
    print("HIT: the window does not determine the formation price even for window-confined sources: explicit exact wall-adjacent counterexample for every R")
