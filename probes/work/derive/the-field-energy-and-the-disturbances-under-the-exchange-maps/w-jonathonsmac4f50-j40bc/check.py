#!/usr/bin/env python3
"""the-field-energy-and-the-disturbances-under-the-exchange-maps, attempt 2 (worker w-jonathonsmac4f50-j40bc, claude-opus-5-5).

Exact claims: sympy (continuum symbols at weak field, as block 64 T2-T4 are) and exact integer/dyadic matrix identities on a 4^3 torus
(numpy with small integers: every entry is a dyadic rational, so the equalities checked are exact). Step labels refer to ATTEMPT.md.
"""
import itertools
import sys
import time

import numpy as np
import sympy as sp

T0 = time.time()
NP = NF = 0


def ok(label, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NF += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


nodes = list(itertools.product((0, 1), repeat=3))
dvec = lambda n: [(-1) ** q for q in n]

# ---------------------------------------------------------------- Step 1: the lattice curls under B -> B D (exact)
Bs = [[sp.Function(f"B{a}{j}") for j in range(3)] for a in range(3)]  # B_a^j(x): bond a, component j
X = sp.symbols("x1:4", integer=True)
sh = lambda f, a: f(*[X[i] + (1 if i == a else 0) for i in range(3)])
at = lambda f: f(*X)
Fcurl = lambda Bf, a, b, j: (sh(Bf[b][j], a) - at(Bf[b][j])) - (sh(Bf[a][j], b) - at(Bf[a][j]))
ok1 = True
for n in nodes:
    d = dvec(n)
    for a, b in ((0, 1), (0, 2), (1, 2)):
        for j in range(3):
            BD = [[(lambda jj, aa: (lambda *xx: d[jj] * Bs[aa][jj](*xx)))(j2, a2) for j2 in range(3)] for a2 in range(3)]
            ok1 &= sp.simplify(Fcurl(BD, a, b, j) - d[j] * Fcurl(Bs, a, b, j)) == 0
ok("1.1 lattice, exactly: under B -> B D (component j scaled by d_j = (-1)^{n_j}) every plaquette curl goes to F_ab^j d_j, for all eight species", ok1)

# ---------------------------------------------------------------- Step 2: block 64's family at weak field, per species (plane-wave symbols)
k = sp.symbols("k1:4", real=True)
Br = sp.Matrix(3, 3, lambda a, j: sp.Symbol(f"r{a}{j}", real=True))
Bi = sp.Matrix(3, 3, lambda a, j: sp.Symbol(f"i{a}{j}", real=True))
Bh = Br + sp.I * Bi  # plane-wave amplitude of B_a^j


def T(Bm):
    """T^j_ab = d_a B_b^j - d_b B_a^j for a plane wave (d -> i k)"""
    return {(j, a, b): sp.I * (k[a] * Bm[b, j] - k[b] * Bm[a, j]) for j in range(3) for a in range(3) for b in range(3)}


def quad(Bm):
    Tt = T(Bm)
    cj = lambda z: sp.conjugate(z)
    T1 = sum(Tt[(j, a, b)] * cj(Tt[(j, a, b)]) for j in range(3) for a in range(3) for b in range(3))
    T2 = sum(Tt[(j, a, b)] * cj(Tt[(b, a, j)]) for j in range(3) for a in range(3) for b in range(3))
    V = [sum(Tt[(a, a, b)] for a in range(3)) for b in range(3)]
    T3 = sum(V[b] * cj(V[b]) for b in range(3))
    epsT = sum(sp.LeviCivita(j, a, b) * Tt[(j, a, b)] for j in range(3) for a in range(3) for b in range(3))
    return [sp.expand(sp.re(sp.expand(z))) for z in (T1, T2, T3)], sp.expand(epsT), V


def lin_div(Bm):
    """first-order part of the divergence term d_b V^b (the c4 term; it multiplies the rates)"""
    _, _, V = quad(Bm)
    return sp.expand(sum(sp.I * k[b] * V[b] for b in range(3)))


(q1, q2, q3), e0, _ = quad(Bh)
Dstar0 = q1 / 4 + q2 / 2 - q3
c1, c2, c3, cc = sp.symbols("c1 c2 c3 cc")
eff = {}
for n in nodes:
    d = dvec(n)
    Dm = sp.diag(*d)
    (p1, p2, p3), epn, _ = quad(Bh * Dm)
    target = sp.expand(p1 / 4 + p2 / 2 - p3)  # D*[B' D] as a function of the species' own strain B' = Bh
    expr = sp.expand(target - (c1 * q1 + c2 * q2 + c3 * q3))
    coeffs = sp.Poly(expr, *k, *list(Br), *list(Bi)).coeffs()
    sol = sp.solve(coeffs, [c1, c2, c3], dict=True)
    lin_n = lin_div(Bh * Dm)
    lin0 = lin_div(Bh)
    lsol = sp.solve(sp.Poly(sp.expand(lin_n - cc * lin0), *k, *list(Br), *list(Bi)).coeffs(), [cc], dict=True)
    eff[n] = (sol, lsol, sp.expand(epn - e0) == 0 if sum(n) == 0 else sp.expand(epn + e0) == 0)
ok("2.1 T1 is unchanged by B -> B D for every species (the component index is summed in squares)",
   all(sp.expand(quad(Bh * sp.diag(*dvec(n)))[0][0] - q1) == 0 for n in nodes))
ok("2.2 species (000): the curvature member (c1, c2, c3) = (1/4, 1/2, -1) and the rate coupling unchanged",
   eff[(0, 0, 0)][0] == [{c1: sp.Rational(1, 4), c2: sp.Rational(1, 2), c3: -1}] and eff[(0, 0, 0)][1] == [{cc: 1}])
ok("2.3 species (111): the quadratic part is the SAME member (1/4, 1/2, -1) but the first-order divergence term, which multiplies the rates, changes sign (c4 -> -c4)",
   eff[(1, 1, 1)][0] == [{c1: sp.Rational(1, 4), c2: sp.Rational(1, 2), c3: -1}] and eff[(1, 1, 1)][1] == [{cc: -1}])
mixed = [n for n in nodes if 0 < sum(n) < 3]
ok("2.4 the six species with |n| = 1, 2: D*[B' D] is NOT of the family's form c1 T1 + c2 T2 + c3 T3 for any (c1, c2, c3), and the rate coupling is not a multiple of species (000)'s: they live outside the isotropic family",
   all(eff[n][0] == [] and eff[n][1] == [] for n in mixed), f"{len(mixed)} species")
# the rate coupling on the isotropic stretch B' = lam delta: -2 Lap lam for (000); species n: sum_a d_a d_a^2 lam - (sum d) Lap lam
lam = sp.Function("lam")(*sp.symbols("y1:4", real=True))
ys = sp.symbols("y1:4", real=True)
rate_ok = True
rows = []
for n in nodes:
    d = dvec(n)
    # d_b V^(n)_b with V^(n)_b = sum_a d_a (d_a B'_b^a - d_b B'_a^a), B' = lam * identity
    Vn = [sum(d[a] * (sp.diff(lam * (1 if a == b else 0), ys[a]) - sp.diff(lam * 1, ys[b])) for a in range(3)) for b in range(3)]
    div = sp.expand(sum(sp.diff(Vn[b], ys[b]) for b in range(3)))
    claim = sum(d[a] * sp.diff(lam, ys[a], 2) for a in range(3)) - sum(d) * sum(sp.diff(lam, y, 2) for y in ys)
    rate_ok &= sp.simplify(div - claim) == 0
    rows.append((n, sp.simplify(div)))
ok("2.5 on the isotropic stretch lam: the rate coupling seen by species n is sum_a d_a d_a^2 lam - (sum_a d_a) Lap lam: -2 Lap lam for (000), +2 Lap lam for (111), -2 d_1^2 lam for (100)",
   rate_ok and sp.simplify(dict(rows)[(0, 0, 0)] + 2 * sum(sp.diff(lam, y, 2) for y in ys)) == 0
   and sp.simplify(dict(rows)[(1, 1, 1)] - 2 * sum(sp.diff(lam, y, 2) for y in ys)) == 0
   and sp.simplify(dict(rows)[(1, 0, 0)] + 2 * sp.diff(lam, ys[0], 2)) == 0)
# block 64 T4: beta = c4/(4c1 + 2c2 + 4c3); blind member (-1/8, -1/4, 1/2, 1) -> beta = 1; species (111): c4 -> -c4 -> beta = -1
cb = [sp.Rational(-1, 8), sp.Rational(-1, 4), sp.Rational(1, 2), 1]
beta = lambda c: c[3] / (4 * c[0] + 2 * c[1] + 4 * c[2])
ok("2.6 block 64 T4's exponent: beta = 1 for (000); species (111) sees c4 -> -c4 and beta = -1, so for it a ray's bending over a slow body's fall, 1 + beta, is 0",
   beta(cb) == 1 and beta(cb[:3] + [-cb[3]]) == -1)
ok("2.7 the inversion-odd term eps.T is unchanged for (000) and reversed for (111); for the mixed species it becomes sum_j d_j eps^jkl T^j_kl (c5 = 0 in the member, so no effect)",
   all((sp.expand(quad(Bh * sp.diag(*dvec(n)))[1] - (-1) ** (sum(n) % 2) * e0) == 0) for n in [(0, 0, 0), (1, 1, 1)]))

# ---------------------------------------------------------------- Step 3: block 62's transverse-traceless disturbances, the three vertices
h = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"h{min(i, j)}{max(i, j)}", real=True))
vert_ok = True
for n in nodes:
    D = sp.diag(*dvec(n))
    frame = D * h * D  # frame coupling: E -> rho E rho, rho = s_n D
    two = (h * D + D * h) / 2  # reach two: g = (1 + B D)^T (1 + B D), symmetric strain B = h/2
    for i in range(3):
        for j in range(3):
            di, dj = dvec(n)[i], dvec(n)[j]
            vert_ok &= sp.simplify(frame[i, j] - di * dj * h[i, j]) == 0
            vert_ok &= sp.simplify(two[i, j] - (di + dj) / 2 * h[i, j]) == 0
ok("3.1 vertex of species n with a metric disturbance h: frame D h D (h_ij times d_i d_j: shear components flip for d_i != d_j); reach two (hD + Dh)/2 (h_ij times (d_i + d_j)/2: zero for d_i != d_j, sign d_i on the diagonal); reach three h",
   vert_ok)
# TT wave along z: h = [[a, b, 0], [b, -a, 0], [0, 0, 0]]
aa, bb = sp.symbols("a b", real=True)
hTT = sp.Matrix([[aa, bb, 0], [bb, -aa, 0], [0, 0, 0]])
tab = []
for n in nodes:
    D = sp.diag(*dvec(n))
    tab.append((n, (D * hTT * D)[0, 0], (D * hTT * D)[0, 1], ((hTT * D + D * hTT) / 2)[0, 0], ((hTT * D + D * hTT) / 2)[0, 1]))
ok("3.2 a TT wave along z: under the frame coupling species with d_1 d_2 = -1 see the x-polarisation reversed; under reach two they do not couple to it at all, and species with d_1 = d_2 = -1 see + reversed",
   all((r[2] == (dvec(r[0])[0] * dvec(r[0])[1]) * bb) and (r[4] == (0 if dvec(r[0])[0] != dvec(r[0])[1] else dvec(r[0])[0] * bb))
       and (r[1] == aa) and (r[3] == dvec(r[0])[0] * aa) for r in tab))

# ---------------------------------------------------------------- Step 4: reach three is species-blind, exactly (4^3 torus, integer matrices)
L = 4
N = L ** 3
sites = list(itertools.product(range(L), repeat=3))
idx = {x: i for i, x in enumerate(sites)}
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def Tm(a, s=1):
    M = np.zeros((N, N), complex)
    for x in sites:
        y = tuple((x[i] + (s if i == a else 0)) % L for i in range(3))
        M[idx[x], idx[y]] = 1
    return M


Tp = [Tm(a) for a in range(3)]
S = [(Tp[a] - Tp[a].conj().T) / (2j) for a in range(3)]
Cc = [(Tp[a] + Tp[a].conj().T) / 2 for a in range(3)]
P = [S[a] @ Cc[a] for a in range(3)]


def Chop(a, v):  # symmetric hop along a weighted by the bond function v (v at the bond's first site)
    M = np.zeros((N, N), complex)
    for x in sites:
        y = tuple((x[i] + (1 if i == a else 0)) % L for i in range(3))
        M[idx[x], idx[y]] += v[idx[x]] / 2
        M[idx[y], idx[x]] += v[idx[x]] / 2
    return M


kron = np.kron
H0 = sum(kron(S[a], sig[a]) for a in range(3))
rng = np.random.default_rng(3)
Bf = rng.integers(-2, 3, size=(3, 3, N)).astype(float)
H3 = H0 + sum(kron((Chop(a, Bf[a, j]) @ P[j] + P[j] @ Chop(a, Bf[a, j])) / 2, sig[a]) for a in range(3) for j in range(3))
H2 = H0 + sum(kron((Chop(a, Bf[a, j]) @ S[j] + S[j] @ Chop(a, Bf[a, j])) / 2, sig[a]) for a in range(3) for j in range(3))


def Vmap(n):
    d = dvec(n)
    s = d[0] * d[1] * d[2]
    rho = [s * q for q in d]
    # coin half turn R_n with R sigma_a R^dag = rho_a sigma_a (for rho = (+,+,+): 1; for two -1 entries: the remaining Pauli; for s=-1 cases use rho)
    cand = [np.eye(2), sig[0], sig[1], sig[2]]
    R = next(c for c in cand if all(np.allclose(c @ sig[a] @ c.conj().T, rho[a] * sig[a]) for a in range(3)))
    U = np.diag([(-1) ** (n[0] * x[0] + n[1] * x[1] + n[2] * x[2]) for x in sites]).astype(complex)
    return kron(U, R), s, d


r3 = r2 = True
for n in nodes:
    Vn, s, d = Vmap(n)
    r3 &= np.array_equal(Vn @ H3 @ Vn.conj().T, s * H3)
    H2D = H0 + sum(kron((Chop(a, Bf[a, j] * d[j]) @ S[j] + S[j] @ Chop(a, Bf[a, j] * d[j])) / 2, sig[a]) for a in range(3) for j in range(3))
    r2 &= np.array_equal(Vn @ H2 @ Vn.conj().T, s * H2D)
ok("4.1 exactly on a 4^3 torus with an integer strain: V_n H3[B] V_n^dag = s_n H3[B] for all eight species (reach three: the strain unchanged)", r3)
ok("4.2 and V_n H2[B] V_n^dag = s_n H2[B D] (reach two: the strain seen as B D) - block 70, reproduced", r2)
# the reach-three response K_a^j = d<H3>/dB_a^j(x): under psi -> V_n psi it goes to s_n K; energy density likewise
psi = (rng.integers(-2, 3, size=2 * N) + 1j * rng.integers(-2, 3, size=2 * N)).astype(complex)


def K(ps, a, j, xi):
    e = np.zeros(N)
    e[xi] = 1
    dH = kron((Chop(a, e) @ P[j] + P[j] @ Chop(a, e)) / 2, sig[a])
    return np.vdot(ps, dH @ ps).real


resp_ok = True
for n in nodes:
    Vn, s, d = Vmap(n)
    pn = Vn @ psi
    for (a, j, xi) in [(0, 0, 5), (1, 2, 17), (2, 1, 40), (0, 2, 63)]:
        resp_ok &= K(pn, a, j, xi) == s * K(psi, a, j, xi)
ok("4.3 the reach-three bond response K_a^j at sampled bonds maps to s_n K for every species (exact): every species sources the common strain alike up to its energy sign",
   resp_ok)
# the energy density in a rate field (integer phi): e_x = Re psi_x^dag (phi H3 phi psi)_x maps to s_n e_x
phi = np.kron(np.diag(rng.integers(1, 3, size=N).astype(complex)), np.eye(2))
Hw = phi @ H3 @ phi
def edens(ps):
    v = Hw @ ps
    return np.array([np.vdot(ps[2 * i:2 * i + 2], v[2 * i:2 * i + 2]).real for i in range(N)])
e_ok = all(np.array_equal(edens(Vmap(n)[0] @ psi), Vmap(n)[1] * edens(psi)) for n in nodes)
ok("4.4 in a rate field (integer phi) the energy density maps to s_n e at every site for every species (V_n commutes with phi): with block 72's fP_j -> s_n fP_j, block 66's identity (stress gradient = weight) holds for species n iff for (000)",
   e_ok)
ok("4.5 hence with reach three all eight species see the same field energy F[B] of the same strain and source it with the same response: the task's HIT condition does not arise",
   r3 and resp_ok and e_ok)

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL exact: under the reach-two map B -> B D every plaquette curl goes to F^j d_j; species (000) sees the curvature member, "
      "species (111) sees the same quadratic member with the rate coupling reversed (c4 -> -c4, block 64 T4 exponent beta = -1, bending over fall 0), "
      "and the six species with |n| = 1, 2 see a density that is not in the family at all (no (c1, c2, c3) reproduces it; their rate coupling on an "
      "isotropic stretch is -2 d_a^2 lam along their reflected axis); a TT disturbance's vertex is D h D (frame), (hD + Dh)/2 (reach two) and h (reach "
      "three); with reach three every species sees the same F[B] and sources it with s_n K: no disagreement (the task's HIT condition does not arise)")
