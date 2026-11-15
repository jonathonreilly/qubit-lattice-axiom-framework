#!/usr/bin/env python3
"""fl55_3 -- gauge-covariance step of the h-tadpole lemma (FLOW55 §K), exact rational arithmetic.
Criteria: checks/fl55_3_criteria.md (written first).  fractions.Fraction only; no numpy, no floats in verdicts."""
import random
from fractions import Fraction as Fr

L = 3                     # (Z/3)^2
NS = L * L                # sites
NL = 2 * NS               # links (x, x+e_mu), mu = 0, 1

def site(x1, x2): return (x1 % L) * L + (x2 % L)
def coords(s): return divmod(s, L)
def link_ends(c):
    s, mu = divmod(c, 2)
    x1, x2 = coords(s)
    y = site(x1 + (1 if mu == 0 else 0), x2 + (1 if mu == 1 else 0))
    return s, y

# ---------------- small exact linear algebra
def zeros(n, m): return [[Fr(0)] * m for _ in range(n)]
def eye(n):
    M = zeros(n, n)
    for i in range(n): M[i][i] = Fr(1)
    return M
def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = zeros(n, m)
    for i in range(n):
        Ai = A[i]; Ci = C[i]
        for t in range(k):
            a = Ai[t]
            if a == 0: continue
            Bt = B[t]
            for j in range(m):
                b = Bt[j]
                if b != 0: Ci[j] += a * b
    return C
def transpose(A): return [list(r) for r in zip(*A)]
def add(A, B, sa=1, sb=1): return [[sa * a + sb * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
def scal(A, s): return [[s * a for a in r] for r in A]
def inverse(A):
    n = len(A)
    M = [list(r) + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        p = M[col][col]
        M[col] = [v / p for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [row[n:] for row in M]
def det3(R):
    return (R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1]) - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
            + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0]))

def crossmat(k):  # [k]_x
    return [[Fr(0), -k[2], k[1]], [k[2], Fr(0), -k[0]], [-k[1], k[0], Fr(0)]]
def cross(a, b): return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
def mv(M, v): return [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]
E3 = eye(3)
def cayley(k):
    K = crossmat(k)
    return matmul(add(E3, K), inverse(add(E3, K, 1, -1)))

def rand_vec(rng, nlo, nhi, dhi):
    return [Fr(rng.randint(nlo, nhi), rng.randint(1, dhi)) for _ in range(3)]

w = [Fr(1) + Fr(c % 5, 7) for c in range(NL)]
m2 = Fr(1, 3)

def D_matrix(Rc):
    """(D nu)_c = Rc^T nu(x) - nu(y); rows 3c+a, cols 3s+b."""
    D = zeros(3 * NL, 3 * NS)
    for c in range(NL):
        x, y = link_ends(c)
        RT = transpose(Rc[c])
        for a in range(3):
            for b in range(3):
                D[3 * c + a][3 * x + b] += RT[a][b]
            D[3 * c + a][3 * y + a] -= Fr(1)
    return D
def Wmat():
    M = zeros(3 * NL, 3 * NL)
    for c in range(NL):
        for a in range(3): M[3 * c + a][3 * c + a] = w[c]
    return M
WM = Wmat()
def G_of(D):
    G = matmul(matmul(transpose(D), WM), D)
    for i in range(3 * NS): G[i][i] += m2
    return G

def tadpole(Cov, Rc):
    """T_c = -1/2 sum_{a,b} Cov[(x,a),(y,b)] (Rc^T e_a) x e_b."""
    out = []
    for c in range(NL):
        x, y = link_ends(c)
        RT = transpose(Rc[c])
        T = [Fr(0)] * 3
        for a in range(3):
            Rea = [RT[i][a] for i in range(3)]
            for b in range(3):
                cv = Cov[3 * x + a][3 * y + b]
                if cv == 0: continue
                cr = cross(Rea, E3[b])
                T = [t - Fr(1, 2) * cv * z for t, z in zip(T, cr)]
        out.append(T)
    return out
def is_zero(vs): return all(all(z == 0 for z in v) for v in vs)

results = []; controls = []
def verdict(name, ok, detail=""):
    results.append(ok); print(f"{name}: {'PASS' if ok else 'FAIL'}  {detail}")
def control(name, fired, detail=""):
    controls.append(fired); print(f"{name}: {'control fires' if fired else 'CONTROL DOES NOT FIRE'}  {detail}")

# ---------------- trivial background
R1 = [E3 for _ in range(NL)]
D1 = D_matrix(R1)
Cov1 = inverse(G_of(D1))

# ---------------- Part 1: pure gauge
rng = random.Random(5503)
g = [cayley(rand_vec(rng, -3, 3, 4)) for _ in range(NS)]
rot_ok = all(matmul(transpose(gx), gx) == E3 and det3(gx) == 1 for gx in g)
print(f"(sanity) site rotations exact SO(3): {rot_ok}")
Rpg = []
for c in range(NL):
    x, y = link_ends(c)
    Rpg.append(matmul(g[x], transpose(g[y])))
Dpg = D_matrix(Rpg)
Covpg = inverse(G_of(Dpg))
Tpg = tadpole(Covpg, Rpg)
verdict("P1 pure-gauge tadpole T_c = 0 on all 18 links", is_zero(Tpg),
        f"max-numerator-size={max(max(abs(z.numerator) for z in v) for v in Tpg)}")
Tnaive = tadpole(Cov1, Rpg)
nz = sum(1 for v in Tnaive if any(z != 0 for z in v))
control("P1-c naive (untransported) tadpole nonzero on >= 1 link", nz >= 1, f"nonzero links: {nz}/18; e.g. T_0={[str(z) for z in Tnaive[0]]}")

# ---------------- Part 2: first order
def first_order(v, keep_dcov=True):
    # delta D: (dD nu)_c = - v_c x nu(x)  -> rows 3c+a, cols 3x+b : -[v_c]_x
    dD = zeros(3 * NL, 3 * NS)
    for c in range(NL):
        x, y = link_ends(c)
        Vx = crossmat(v[c])
        for a in range(3):
            for b in range(3):
                dD[3 * c + a][3 * x + b] -= Vx[a][b]
    dG = add(matmul(matmul(transpose(dD), WM), D1), matmul(matmul(transpose(D1), WM), dD))
    dCov = scal(matmul(matmul(Cov1, dG), Cov1), Fr(-1))
    out = []
    for c in range(NL):
        x, y = link_ends(c)
        T = [Fr(0)] * 3
        for a in range(3):
            for b in range(3):
                if keep_dcov:
                    cv = dCov[3 * x + a][3 * y + b]
                    if cv != 0:
                        cr = cross(E3[a], E3[b])
                        T = [t - Fr(1, 2) * cv * z for t, z in zip(T, cr)]
                c1 = Cov1[3 * x + a][3 * y + b]
                if c1 != 0:
                    va = cross(v[c], E3[a]); va = [-z for z in va]      # -v_c x e_a
                    cr = cross(va, E3[b])
                    T = [t - Fr(1, 2) * c1 * z for t, z in zip(T, cr)]
        out.append(T)
    return out

def gradient_field(lam):
    v = []
    for c in range(NL):
        x, y = link_ends(c)
        v.append([lam[x][i] - lam[y][i] for i in range(3)])
    return v

rngl = random.Random(5504)
p2_ok = True; p2c_fired = False
for trial in range(3):
    lam = [rand_vec(rngl, -4, 4, 3) for _ in range(NS)]
    vg = gradient_field(lam)
    T1 = first_order(vg, True)
    T1n = first_order(vg, False)
    z = is_zero(T1); p2_ok &= z
    nzc = sum(1 for vv in T1n if any(q != 0 for q in vv))
    if nzc >= 1: p2c_fired = True
    print(f"  gradient trial {trial}: full T^(1) zero: {z};  without dCov: nonzero on {nzc}/18 links")
verdict("P2 first-order T^(1)[gradient] = 0 (3 independent lambda)", p2_ok)
rngv = random.Random(5505)
vgen = [rand_vec(rngv, -4, 4, 3) for _ in range(NL)]
Tgen = first_order(vgen, True)
nzg = sum(1 for vv in Tgen if any(q != 0 for q in vv))
verdict("P2-n non-vacuity: T^(1)[generic v] nonzero on >= 1 link", nzg >= 1, f"nonzero links: {nzg}/18; e.g. T_0={[str(q) for q in Tgen[0]]}")
control("P2-c dropping dCov gives nonzero on a gradient", p2c_fired)
lam = [rand_vec(random.Random(5506), -4, 4, 3) for _ in range(NS)]
vg = gradient_field(lam)
vsum = [[a + b for a, b in zip(p, q)] for p, q in zip(vgen, vg)]
Ts = first_order(vsum, True); Tg = first_order(vg, True)
lin = all(all(Ts[c][i] == Tgen[c][i] + Tg[c][i] for i in range(3)) for c in range(NL))
verdict("P3 linearity T^(1)[v1+v2] = T^(1)[v1] + T^(1)[v2]", lin)

print("=== fl55_3 SUMMARY ===")
print(f"verdict lines: {sum(results)}/{len(results)} PASS; controls fired: {sum(controls)}/{len(controls)}")
print("OVERALL:", "PASS" if all(results) and all(controls) else ("INVALID (a control did not fire)" if all(results) else "FAIL"))
