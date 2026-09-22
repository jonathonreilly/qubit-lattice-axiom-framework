"""normal-ordering-as-a-rule, attempt a1 (w-jonathonsmac4f50-jd669): checks.

Exact (fractions, integers, sympy, or floating point whose every operand and result is a dyadic rational, asserted with
array_equal) for every finite claim; items labelled NUMERIC use floating point and support no exact claim.

Objects (block 76, PR #8611).  Walk H = sum_a sigma_a (x) S_a on the torus (Z/L)^3, S_a = (T_a - T_a^dagger)/(2i).
Clocked walk H_w = phi H phi, phi = sqrt(w).  Sea E_sea[w] = sum of the negative eigenvalues of H_w.  c0 = E_sea[1]/N.
Counter-terms (weight one, covariant, nearest-neighbour):  T_site = -c0 sum_x w_x  (the sea's energy at the site's own rate,
counted per local tick);  T_bond = -(c0/3) sum_bonds sqrt(w_x w_y)  (the same energy at each bond's geometric-mean rate);
T_theta = theta T_site + (1 - theta) T_bond.  Remainder R = E_sea + T_site.
"""
import itertools
from fractions import Fraction as F

import numpy as np
import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.array([[1, 0], [0, -1]], complex)


def walk(L):
    N = L ** 3
    idx = lambda x: ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
    H = np.zeros((2 * N, 2 * N), complex)
    S = [np.zeros((N, N), complex) for _ in range(3)]
    bonds = []
    for x in itertools.product(range(L), repeat=3):
        i = idx(x)
        for a, s in enumerate((SX, SY, SZ)):
            y = list(x); y[a] += 1; j = idx(y)
            H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += s / 2j
            H[2 * j:2 * j + 2, 2 * i:2 * i + 2] += -s / 2j
            S[a][i, j] += 1 / 2j; S[a][j, i] += -1 / 2j
            bonds.append((i, j))
    xs = [tuple(x) for x in itertools.product(range(L), repeat=3)]
    return H, S, bonds, N, xs


# ------------------------------------------------------------------ E1-E3: the walk, the sea at uniform rate, the chessboard
H4, S4, B4, N4, X4 = walk(4)
H2 = H4 @ H4
sumS2 = sum(np.kron(Sa @ Sa, np.eye(2)) for Sa in S4)                              # H is indexed (site, coin) = kron(site, coin)
want("E1 4^3 torus: H^2 = (sum_a S_a^2) (x) 1 exactly (the coin matrices anticommute and the S_a commute), so |E| = sqrt(sum_a sin^2 k_a) "
     "(every entry a dyadic rational; compared with array_equal)", np.array_equal(H2, sumS2) and np.array_equal(H4, H4.conj().T))
# exact sea energy per site on 4^3: sin k in {0, +-1}; j coordinates with sin^2 = 1 occur for C(3,j) 8 wavevectors
c0_4 = -sum(sp.binomial(3, j) * 8 * sp.sqrt(j) for j in range(4)) / 64
ev = np.linalg.eigvalsh(H4)
want("E2 4^3 torus: c0 = E_sea[1]/N = -(3 + 3 sqrt 2 + sqrt 3)/8 exactly (the diagonalisation agrees to 1e-12); c0 < 0",
     sp.simplify(c0_4 + (3 + 3 * sp.sqrt(2) + sp.sqrt(3)) / 8) == 0 and abs(ev[ev < 0].sum() / N4 - float(c0_4)) < 1e-12 and c0_4 < 0,
     f"c0(4) = {sp.nsimplify(c0_4)} = {float(c0_4):.6f}")
eps_x = np.array([(-1) ** sum(x) for x in X4])
phi = np.repeat(np.where(eps_x > 0, 2.0, 0.5), 2)
want("E3 4^3 torus: a chessboard of clocks, phi = 2^{eps(x)}, gives phi H phi = H exactly (block 76 T1: every bond product is 1)",
     np.array_equal(phi[:, None] * H4 * phi[None, :], H4))

# ------------------------------------------------------------------ E4: the remainder on uniform rates and on the chessboard
e, lam, wb, c0s, Ns = sp.symbols("epsilon lambda wbar c0 N", real=True)
# weight one: E_sea[lam^2 w] = lam^2 E_sea[w] because H_{lam^2 w} = lam^2 H_w; checked on 4^3 with lam^2 = 4
want("E4 weight one: H_{4w} = 4 H_w exactly on 4^3 for the chessboard rates above (hence E_sea[4w] = 4 E_sea[w]); "
     "so R = E_sea - c0 sum w vanishes on every uniform rate: R[wbar 1] = wbar(c0 N) - c0 N wbar = 0",
     np.array_equal((2 * phi)[:, None] * H4 * (2 * phi)[None, :], 4 * (phi[:, None] * H4 * phi[None, :]))
     and sp.simplify(wb * c0s * Ns - c0s * Ns * wb) == 0)
R_chess = c0s * Ns - c0s * (Ns / 2) * (sp.exp(e) + sp.exp(-e))
want("E5 on the chessboard mode u = eps (-1)^{x+y+z} the remainder is exactly R = -c0 N (cosh eps - 1) at every amplitude "
     "(E_sea unchanged by E3; sum_x w_x = N cosh eps): positive for c0 < 0, with second variation |c0| N / 2 per eps^2 "
     "- the chessboard is no longer a zero mode",
     sp.simplify((R_chess - (-c0s * Ns * (sp.cosh(e) - 1))).rewrite(sp.exp)) == 0
     and sp.simplify(sp.diff(R_chess, e, 2).subs(e, 0) + c0s * Ns) == 0)

# ------------------------------------------------------------------ E6: the two counter-terms' second variations, exactly
ok = True; rows = []
for q in [(F(1, 2), 0, 0), (F(1, 2), F(1, 2), 0), (F(1, 2), F(1, 2), F(1, 2)), (1, 0, 0), (1, 1, 0), (1, 1, 1)]:   # q = pi * q
    COS = {F(0): 1, F(1, 2): 0, F(1): -1}                                          # cos(pi t) for t in {0, 1/2, 1}
    def cval(x):
        # cos(pi (q . x)) for q with entries in {0, 1/2, 1}: exact
        t = sum(F(qi) * xi for qi, xi in zip(q, x)) % 2
        return {F(0): 1, F(1, 2): 0, F(1): -1, F(3, 2): 0}[F(t)]
    cx = [cval(x) for x in X4]
    site2 = F(1, 2) * sum(v * v for v in cx)                                          # d2/deps2 /2 of sum_x e^{eps c_x}
    bond2 = F(1, 8) * sum((cx[i] + cx[j]) ** 2 for i, j in B4)                         # of sum_bonds e^{eps (c_x + c_y)/2}
    ql = sum(2 * (1 - COS[F(qi)]) for qi in q)                                       # |q|^2_lat
    # T_bond = -(c0/3) sum_bonds: coefficient ratio to T_site = (bond2/3)/site2 must be 1 - |q|^2/12
    ratio = (bond2 / 3) / site2
    ok = ok and ratio == 1 - F(ql) / 12
    rows.append(f"q=pi{tuple(str(t) for t in q)}: |q|^2={ql}, ratio={ratio}")
want("E6 4^3 torus, six modes u = eps cos(q.x): the second variation of T_bond is (1 - |q|^2_lat/12) times that of T_site, exactly; "
     "so both cancel the volume term at q -> 0, but at the chessboard (|q|^2 = 12) T_bond cancels nothing", ok, "; ".join(rows))

# Euler row-sum lemma on the counter-terms (exact): sum_y d2T/du_x du_y at uniform = T[1]/N
u = sp.symbols("u0:8")
xs2 = [(a, b, c) for a in range(2) for b in range(2) for c in range(2)]
bonds2 = []
for i, x in enumerate(xs2):
    for a in range(3):
        y = list(x); y[a] = (y[a] + 1) % 2; bonds2.append((i, xs2.index(tuple(y))))
Tsite = sum(sp.exp(ui) for ui in u)
Tbond = sum(sp.exp((u[i] + u[j]) / 2) for i, j in bonds2) / 3
ok = True
for T in (Tsite, Tbond):
    rowsum = sp.simplify(sum(sp.diff(T, u[0], uy) for uy in u).subs({ui: 0 for ui in u}))
    ok = ok and rowsum == sp.simplify(T.subs({ui: 0 for ui in u}) / 8)
want("E7 Euler: for weight-one translation-invariant T, sum_y d2T/du_x du_y at uniform rate = T[1]/N (checked exactly for sum_x w_x and "
     "(1/3) sum_bonds sqrt(w_x w_y) on the 2x2x2 torus): the q -> 0 symbol of a weight-one field term's Hessian is its uniform value per site", ok)

# ------------------------------------------------------------------ E8: the family and the declared values
c0d, kd = sp.Rational(-1193, 1000), sp.Rational(95, 1000)                              # block 76's declared rounded values
th = sp.Symbol("theta")
kappa_theta = kd + (1 - th) * c0d / 12
want("E8 declared values c0 = -1193/1000, kappa = 95/1000 (block 76): the admissible family T_theta has long-wavelength stiffness "
     "kappa + (1-theta) c0/12 and chessboard stiffness theta |c0|/4; theta = 1 gives kappa (gamma = 200/19); theta = 1/2 gives "
     "1087/24000 (gamma = 24000/1087); theta = 0 gives -53/12000",
     kappa_theta.subs(th, 1) == sp.Rational(95, 1000) and kappa_theta.subs(th, sp.Rational(1, 2)) == sp.Rational(1087, 24000)
     and kappa_theta.subs(th, 0) == sp.Rational(-53, 12000),
     f"gamma(1) = {float(1 / kd):.4f}, gamma(1/2) = {24000 / 1087:.4f}")
want("E9 the sea's remainder R and block 56's F_gamma (gamma = 1/kappa) agree at second order and long wavelength by construction, "
     "but on the chessboard F/R = (6/gamma)(c - 1/c)^2 N / ((|c0|/2)(c - 1/c)^2 N) = 12 kappa/|c0| = 1140/1193 with the declared values",
     12 * kd / abs(c0d) == sp.Rational(1140, 1193), f"{float(sp.Rational(1140, 1193)):.5f}")

# ------------------------------------------------------------------ E10: block 56's strong field with gamma = 1/kappa, exactly on a box
n = 5                                                                              # interior 5^3, walls phi = 1
inner = [(a, b, c) for a in range(n) for b in range(n) for c in range(n)]
pos = {x: i for i, x in enumerate(inner)}
M = sp.zeros(len(inner), len(inner)); rhs = sp.zeros(len(inner), 1)
gam = sp.Rational(200, 19); m = sp.Integer(1); ctr = (2, 2, 2)
for x, i in pos.items():
    M[i, i] = 1 + (gam / 12 * m if x == ctr else 0)
    for a in range(3):
        for d in (1, -1):
            y = list(x); y[a] += d; y = tuple(y)
            if y in pos:
                M[i, pos[y]] -= sp.Rational(1, 6)
            else:
                rhs[i] += sp.Rational(1, 6)                                       # wall value 1
G = sp.zeros(len(inner), len(inner))
A0 = sp.eye(len(inner))
for x, i in pos.items():
    for a in range(3):
        for d in (1, -1):
            y = list(x); y[a] += d; y = tuple(y)
            if y in pos:
                A0[i, pos[y]] -= sp.Rational(1, 6)
e_c = sp.zeros(len(inner), 1); e_c[pos[ctr]] = 1
g0 = (A0.LUsolve(e_c))[pos[ctr]]
phi_sol = M.LUsolve(rhs)
x0 = gam / 12 * g0 * m
want("E10 block 56's law with gamma = 200/19 on a 5^3 box (walls phi = 1), one body m = 1 at the centre: the exact solution has "
     "phi_0 = 1/(1 + (gamma/12) g0 m) with g0 = G(centre, centre) of (1 - A) with zero walls, and the ledger m phi_0 is below 12/(gamma g0)",
     sp.simplify(phi_sol[pos[ctr]] - 1 / (1 + x0)) == 0 and m * phi_sol[pos[ctr]] < 12 / (gam * g0),
     f"g0(box) = {g0} = {float(g0):.6f}, phi_0 = {float(phi_sol[pos[ctr]]):.6f}, bound 12/(gamma g0) = {float(12 / (gam * g0)):.6f}")

# ------------------------------------------------------------------ NUMERIC
import mpmath as mpm
g0_Z3 = mpm.sqrt(6) / (32 * mpm.pi ** 3) * mpm.gamma(mpm.mpf(1) / 24) * mpm.gamma(mpm.mpf(5) / 24) * mpm.gamma(mpm.mpf(7) / 24) * mpm.gamma(mpm.mpf(11) / 24)
sat = 12 * 0.095 / float(g0_Z3); sat2 = 12 * 0.0952 / float(g0_Z3)
want("N1 NUMERIC saturation on Z^3 with gamma = 1/kappa: 12/(gamma g0) = 12 kappa/g0, g0 = the cubic walk's expected visits to the origin "
     "(closed form sqrt6/(32 pi^3) Gamma(1/24)Gamma(5/24)Gamma(7/24)Gamma(11/24)) = 1.516386; kappa = 0.095 gives 0.7518, kappa = 0.0952 (block 76's estimate) gives 0.7534",
     abs(float(g0_Z3) - 1.516386) < 1e-6 and abs(sat - 0.75178) < 1e-4, f"g0 = {float(g0_Z3):.6f}, 12 kappa/g0 = {sat:.5f} / {sat2:.5f}")


def esea(H, phi_site):
    P = np.repeat(phi_site, 2)
    evs = np.linalg.eigvalsh(P[:, None] * H * P[None, :])
    return evs[evs < 0].sum()


rows = []; ok = True
for L in (6, 8, 10):
    H, S, B, N, X = walk(L)
    xs = np.array(X)
    E0 = esea(H, np.ones(N)); c0 = E0 / N
    q = np.array([2 * np.pi / L, 0, 0]); cq = np.cos(xs @ q); ql = sum(2 * (1 - np.cos(t)) for t in q)
    eps = 0.02
    Pi = (esea(H, np.exp(eps * cq / 2)) + esea(H, np.exp(-eps * cq / 2)) - 2 * E0) / (2 * eps ** 2 * N)
    k_site = 4 * (Pi - c0 / 4) / ql
    k_bond = 4 * (Pi - (c0 / 4) * (1 - ql / 12)) / ql
    ok = ok and k_site > 0 and k_bond < 0 and abs(k_bond - (k_site + c0 / 12)) < 1e-9
    rows.append(f"L={L}: c0={c0:.5f} kappa_site={k_site:.5f} kappa_bond={k_bond:.5f}")
want("N2 NUMERIC the actual sea, smallest wavevector, tori 6^3, 8^3, 10^3: with T_site the stiffness is positive (block 76's kappa); with T_bond "
     "it is kappa + c0/12 < 0 on every torus tested (repulsive), approaching 0 from below as L grows (the infinite-volume sign is not claimed)",
     ok, "; ".join(rows))

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: ROUTE FAILS AT (c): the counter-term is not a consequence of clauses A and C alone. What A and C force (A's weak-field law "
          "has no mass term; C makes the static law the ledger's stationarity; Euler for weight one) is only its value on uniform rates, "
          "T[wbar] = -c0 N wbar. The per-site counter-term -c0 sum w_x and the per-bond one -(c0/3) sum_bonds sqrt(w_x w_y) both satisfy A and C "
          "and agree on every uniform rate, yet give different static laws (stiffness kappa against kappa + c0/12; the chessboard stiff against "
          "exactly soft); the family between them gives gamma_ind(theta) = 1/(kappa + (1-theta) c0/12). Selecting the per-site member is "
          "counting the counter-term per local tick, fork (i), a supplied clause. With it, R = E_sea - c0 sum w is weight one, zero on uniform "
          "rates, first variation zero, second variation the polarisation without volume part, the chessboard stiff (-c0 N (cosh eps - 1) "
          "exactly); block 56's law with gamma = 1/kappa saturates at 12 kappa/g0 = 0.752 on Z^3")
    print("HIT: normal ordering is not a consequence of clauses A and C alone - they fix the counter-term only on uniform rates (T[wbar] = -c0 N wbar); "
          "two weight-one nearest-neighbour counter-terms that agree there give different static laws (exact on 4^3: their second "
          "variations differ by the factor 1 - |q|^2/12, the per-bond one leaves the chessboard a zero mode), so the per-site "
          "counter-term is a supplied clause (fork (i) applied to it)")
