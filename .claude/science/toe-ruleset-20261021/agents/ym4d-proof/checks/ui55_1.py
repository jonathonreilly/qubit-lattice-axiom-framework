# ui55_1 -- exact checks for UIR55.md (Lemma P-natural, Finding 2.1, Lemma SPLIT algebra).
# Criteria: checks/ui55_1_criteria.md (written before this script). Exact Fractions only; no floats in verdicts.
import random
from fractions import Fraction as F

# ---------------- exact linear algebra ----------------
def zeros(r, c): return [[F(0)] * c for _ in range(r)]
def eye(n):
    M = zeros(n, n)
    for i in range(n): M[i][i] = F(1)
    return M
def T(A): return [list(r) for r in zip(*A)]
def mm(A, B):
    Bt = T(B)
    return [[sum((a * b for a, b in zip(row, col) if a != 0 and b != 0), F(0)) for col in Bt] for row in A]
def add(A, B): return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
def sub(A, B): return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
def smul(s, A): return [[s * a for a in r] for r in A]
def is_zero(A): return all(a == 0 for r in A for a in r)
def eq(A, B): return is_zero(sub(A, B))
def det(A):
    A = [list(r) for r in A]; n = len(A); d = F(1)
    for i in range(n):
        p = next((k for k in range(i, n) if A[k][i] != 0), None)
        if p is None: return F(0)
        if p != i: A[i], A[p] = A[p], A[i]; d = -d
        d *= A[i][i]
        inv = 1 / A[i][i]
        for k in range(i + 1, n):
            if A[k][i] != 0:
                f = A[k][i] * inv
                A[k] = [a - f * b for a, b in zip(A[k], A[i])]
    return d
def inv(A):
    n = len(A); M = [list(r) + [F(int(i == j)) for j in range(n)] for i, r in enumerate(A)]
    for i in range(n):
        p = next((k for k in range(i, n) if M[k][i] != 0), None)
        if p is None: raise ZeroDivisionError("singular")
        M[i], M[p] = M[p], M[i]
        iv = 1 / M[i][i]; M[i] = [a * iv for a in M[i]]
        for k in range(n):
            if k != i and M[k][i] != 0:
                f = M[k][i]; M[k] = [a - f * b for a, b in zip(M[k], M[i])]
    return [r[n:] for r in M]
def rank(A):
    A = [list(r) for r in A]; rk = 0; rows = len(A); cols = len(A[0]) if A else 0
    for c in range(cols):
        p = next((k for k in range(rk, rows) if A[k][c] != 0), None)
        if p is None: continue
        A[rk], A[p] = A[p], A[rk]
        for k in range(rows):
            if k != rk and A[k][c] != 0:
                f = A[k][c] / A[rk][c]; A[k] = [a - f * b for a, b in zip(A[k], A[rk])]
        rk += 1
    return rk
def nullspace(A):
    # basis (as columns) of {x : A x = 0}
    rows = len(A); cols = len(A[0]); M = [list(r) for r in A]; piv = []; r = 0
    for c in range(cols):
        p = next((k for k in range(r, rows) if M[k][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]; iv = 1 / M[r][c]; M[r] = [a * iv for a in M[r]]
        for k in range(rows):
            if k != r and M[k][c] != 0:
                f = M[k][c]; M[k] = [a - f * b for a, b in zip(M[k], M[r])]
        piv.append(c); r += 1
        if r == rows: break
    free = [c for c in range(cols) if c not in piv]; basis = []
    for fcol in free:
        v = [F(0)] * cols; v[fcol] = F(1)
        for i, pc in enumerate(piv): v[pc] = -M[i][fcol]
        basis.append(v)
    return T(basis)  # cols x k
def detU(X, U): return det(mm(mm(T(U), X), U)) / det(mm(T(U), U))
def col(v): return [[x] for x in v]

results = {}
def rep(name, ok, extra=""):
    results[name] = ok
    print(f"{name}: {'PASS' if ok else 'FAIL'} {extra}")

# ---------------- Part A ----------------
print("=== Part A: abstract fine/level split ===")
rng = random.Random(5501)
def rint(r, c, lo=-3, hi=3): return [[F(rng.randint(lo, hi)) for _ in range(c)] for _ in range(r)]
m, g0, cdim, g1 = 9, 3, 5, 2
while True:
    D0 = rint(m, g0)
    if rank(D0) == g0: break
while True:
    D = rint(cdim, g1)
    if rank(D) == g1: break
ev = rint(g1, g0)
D0p = mm(inv(mm(T(D0), D0)), T(D0))
N = rint(cdim, m)
P0 = sub(eye(m), mm(D0, D0p))
M = add(mm(mm(D, ev), D0p), mm(N, P0))
R = rint(cdim, cdim); C = add(mm(R, T(R)), eye(cdim)); Ci = inv(C)
Pi = sub(Ci, mm(mm(mm(Ci, D), inv(mm(mm(T(D), Ci), D))), mm(T(D), Ci)))
R2 = rint(m, m); RA = add(mm(R2, T(R2)), eye(m)); A = mm(mm(P0, RA), P0)
B = mm(mm(T(M), Pi), M); H = add(A, B)
U0 = nullspace(T(D0)); Un = nullspace(T(D))
print(f"dims: E_0 = {len(U0[0])}, E_n = {len(Un[0])}")
rep("A0 (M D_0 = D ev)", eq(mm(M, D0), mm(D, ev)))
rep("A1 (Pi D = 0 and B D_0 = 0)", is_zero(mm(Pi, D)) and is_zero(mm(B, D0)))
rep("A2 (H D_0 = 0 and A D_0 = 0)", is_zero(mm(H, D0)) and is_zero(mm(A, D0)))
A0p = mm(mm(U0, inv(mm(mm(T(U0), A), U0))), T(U0))
X = add(C, mm(mm(M, A0p), T(M)))
lhs = detU(H, U0) * detU(C, Un); rhs = detU(A, U0) * detU(X, Un)
rep("A3 (SPLIT determinant identity)", lhs == rhs, f"[lhs = {lhs}]")
Hp = mm(mm(U0, inv(mm(mm(T(U0), H), U0))), T(U0))
Bf = sub(Pi, mm(mm(mm(mm(Pi, M), Hp), T(M)), Pi))
def matU(Y, U): return mm(inv(mm(T(U), U)), mm(mm(T(U), Y), U))
ok4 = is_zero(mm(Bf, D)) and eq(mm(matU(Bf, Un), matU(X, Un)), eye(len(Un[0])))
def q(x, v):
    r_ = sub(v, mm(M, x))
    return (mm(mm(T(x), A), x)[0][0] + mm(mm(T(r_), Pi), r_)[0][0]) / 2
for _ in range(3):
    v = col([F(rng.randint(-4, 4)) for _ in range(cdim)])
    xs = mm(mm(mm(Hp, T(M)), Pi), v)
    ok4 = ok4 and q(xs, v) == mm(mm(T(v), Bf), v)[0][0] / 2
    for _ in range(3):
        dl = col([F(rng.randint(-4, 4), rng.randint(1, 3)) for _ in range(m)])
        ok4 = ok4 and (q(add(xs, dl), v) - q(xs, v)) >= 0
rep("A4 (envelope = Woodbury: Bf D = 0, Bf|E_n = X|E_n^-1, min value)", ok4)
rep("A5 (fine Feynman form)", det(add(A, mm(D0, T(D0)))) == detU(A, U0) * det(mm(T(D0), D0)))
rep("A6 (level Feynman form)", det(add(Bf, mm(D, T(D)))) == detU(Bf, Un) * det(mm(T(D), D))
    and detU(Bf, Un) * detU(X, Un) == 1)
Bbad = mm(mm(T(M), Ci), M)
rep("Ac1 control (C^-1 IR term transverse?) must FIRE", not is_zero(mm(Bbad, D0)))
rep("Ac2 control (SPLIT without level group) must FIRE", detU(H, U0) != detU(A, U0) * detU(X, Un))
E = zeros(m, m); E[0][1] = F(1); E[1][0] = F(1); Ap = add(A, E)
rep("Ac3 control (Feynman form for non-transverse A') must FIRE",
    (not is_zero(mm(E, D0))) and det(add(Ap, mm(D0, T(D0)))) != detU(Ap, U0) * det(mm(T(D0), D0)))
passA = all(results[k] for k in results if k.startswith("A"))
print(f"PASS(A) = {passA}")

# ---------------- Part B ----------------
print("=== Part B: Lemma P-natural on a 2D lattice (S2' root map, L = 3, one step) ===")
Lf, L, Lc = 6, 3, 2
def s(x): return (x[0] % Lf) + Lf * (x[1] % Lf)
def lnk(x, mu): return 2 * s(x) + mu
def S(X): return (X[0] % Lc) + Lc * (X[1] % Lc)
def LNK(X, mu): return 2 * S(X) + mu
nf0, nf1, nc0, nc1 = Lf * Lf, 2 * Lf * Lf, Lc * Lc, 2 * Lc * Lc
e = [(1, 0), (0, 1)]
def addv(a, b): return (a[0] + b[0], a[1] + b[1])
d0 = zeros(nf1, nf0)
for x1 in range(Lf):
    for x2 in range(Lf):
        x = (x1, x2)
        for mu in range(2):
            d0[lnk(x, mu)][s(addv(x, e[mu]))] += 1; d0[lnk(x, mu)][s(x)] -= 1
d1 = zeros(nf0, nf1)  # plaquettes (x;0,1)
for x1 in range(Lf):
    for x2 in range(Lf):
        x = (x1, x2); p = s(x)
        d1[p][lnk(x, 0)] += 1; d1[p][lnk(addv(x, e[0]), 1)] += 1
        d1[p][lnk(addv(x, e[1]), 0)] -= 1; d1[p][lnk(x, 1)] -= 1
dc = zeros(nc1, nc0)
for X1 in range(Lc):
    for X2 in range(Lc):
        X_ = (X1, X2)
        for mu in range(2):
            dc[LNK(X_, mu)][S(addv(X_, e[mu]))] += 1; dc[LNK(X_, mu)][S(X_)] -= 1
def root(X_): return (3 * X_[0] + 1, 3 * X_[1] + 1)
evm = zeros(nc0, nf0)
for X1 in range(Lc):
    for X2 in range(Lc):
        evm[S((X1, X2))][s(root((X1, X2)))] = F(1)
def step_vec(x, mu, sign):
    w = [F(0)] * nf1
    if sign > 0: w[lnk(x, mu)] += 1
    else: w[lnk(addv(x, (-e[mu][0], -e[mu][1])), mu)] -= 1
    return w
def path_vec(start, moves):
    w = [F(0)] * nf1; x = start
    for (mu, sign) in moves:
        sv = step_vec(x, mu, sign); w = [a + b for a, b in zip(w, sv)]
        x = addv(x, (sign * e[mu][0], sign * e[mu][1]))
    return w, x
def axial(c, y, order):
    moves = []
    for mu in order:
        dlt = y[mu] - c[mu]
        moves += [(mu, 1 if dlt > 0 else -1)] * abs(dlt)
    return path_vec(c, moves)
orders = [(0, 1), (1, 0)]
Q = zeros(nc1, nf1); Qs = zeros(nc1, nf1); h = zeros(nc0, nf1)
for X1 in range(Lc):
    for X2 in range(Lc):
        X_ = (X1, X2); cX = root(X_)
        block = [(3 * X1 + a, 3 * X2 + b) for a in range(3) for b in range(3)]
        for sig in orders:
            for y in block:
                wP, end = axial(cX, y, sig); assert end == y
                h[S(X_)] = [a + b / 18 for a, b in zip(h[S(X_)], wP)]
        for mu in range(2):
            Y_ = addv(X_, e[mu]); cY = (cX[0] + 3 * e[mu][0], cX[1] + 3 * e[mu][1])
            for sig in orders:
                for y in block:
                    wP, _ = axial(cX, y, sig)
                    wS, yend = path_vec(y, [(mu, 1)] * 3)
                    wP2, end2 = axial(cY, yend, sig); assert end2 == yend
                    wT = [a + b - c_ for a, b, c_ in zip(wP, wS, wP2)]
                    Q[LNK(X_, mu)] = [a + b / 18 for a, b in zip(Q[LNK(X_, mu)], wT)]
                    if sig == orders[0]:
                        Qs[LNK(X_, mu)] = [a + b / 9 for a, b in zip(Qs[LNK(X_, mu)], wS)]
rep("B1 (Q d = d_c ev)", eq(mm(Q, d0), mm(dc, evm)))
rep("B2 (Q = Q_str - d_c h)", eq(Q, sub(Qs, mm(dc, h))))
Cc = smul(F(1, 2), eye(nc1)); Cci = inv(Cc)
Delc = mm(mm(T(dc), Cci), dc); Jc = [[F(1, nc0)] * nc0 for _ in range(nc0)]
Delcp = sub(inv(add(Delc, Jc)), Jc)
PiB = sub(Cci, mm(mm(mm(Cci, dc), Delcp), mm(T(dc), Cci)))
Del0 = mm(T(d0), d0); J0 = [[F(1, nf0)] * nf0 for _ in range(nf0)]
Del0p = sub(inv(add(Del0, J0)), J0)
PL = mm(mm(d0, Del0p), T(d0)); PT = sub(eye(nf1), PL)
IR = mm(mm(T(Q), PiB), Q)
O = add(add(mm(T(d1), d1), mm(d0, T(d0))), IR)
rep("B3 (Q^T Pi Q d = 0)", is_zero(mm(IR, d0)))
rep("B4 (no cross block P_L O P_T = 0)", is_zero(mm(mm(PL, O), PT)))
IRs = mm(mm(T(Qs), PiB), Qs)
rep("B5 (on ker d*: Q^T Pi Q = Q_str^T Pi Q_str)", is_zero(mm(mm(PT, sub(IR, IRs)), PT)))
GT = mm(inv(add(mm(mm(PT, O), PT), PL)), PT); GL = mm(mm(mm(d0, Del0p), Del0p), T(d0))
rep("B6 (O^-1 = C_perp + d Delta^-2 d*)", eq(mm(O, add(GT, GL)), eye(nf1)))
Obad = add(add(mm(T(d1), d1), mm(d0, T(d0))), mm(mm(T(Q), Cci), Q))
rep("Bc control (C^-1 IR term: cross block) must FIRE", not is_zero(mm(mm(PL, Obad), PT)))
passB = all(results[k] for k in results if k.startswith("B"))
print(f"PASS(B) = {passB}")

# ---------------- Part C ----------------
print("=== Part C: composite straight-average kernel ===")
def pmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, F(0)) + x * y
    return {k: v for k, v in out.items() if v != 0}
def Ks(sz, scale=1):
    box = {scale * y: F(1) for y in range(sz)}
    return {k: v / sz for k, v in pmul(box, box).items()}
lhsC = pmul(Ks(3, 1), Ks(3, 3)); rhsC = Ks(9, 1)
rep("C1 (K_3(z) K_3(z^3) = K_9(z))", lhsC == rhsC)
X_ = (0, 0); row = Q_s_row = Qs[LNK(X_, 0)]
wts = {}
for x1 in range(Lf):
    for x2 in range(Lf):
        for mu in range(2):
            w = row[lnk((x1, x2), mu)]
            if w != 0: wts[(x1, x2, mu)] = w
tri = [F(1), F(2), F(3), F(2), F(1)]; box = [F(1), F(1), F(1)]
expected = {(a, b, 0): tri[a] / 3 * box[b] / 3 for a in range(5) for b in range(3)}
rep("C2 (Q_str weights = (tri/3) x (box/3), leg along mu)", wts == expected)
marg = [sum(w for (a, b, mu), w in wts.items() if a == k) for k in range(5)]
rep("Cc control (single box in leg direction) must FIRE", marg != [F(1), F(1), F(1), F(0), F(0)] and marg[:3] != box)
print(f"leg-direction marginal of Q_str weights: {[str(x) for x in marg]}")
passC = all(results[k] for k in results if k.startswith("C"))
print(f"PASS(C) = {passC}")
print(f"OVERALL: {'PASS' if (passA and passB and passC) else 'FAIL'}  ({sum(results.values())}/{len(results)} items true; controls counted as true when they fire)")
