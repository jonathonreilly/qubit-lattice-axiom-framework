AUDIT_INPUT_PATHS = ('docs/RULESET_A_HYPERCUBE_DOES_NOT_SELECT_PATI_SALAM_OR_THE_STANDARD_MODEL_IN_SPIN10_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Ruleset A, decisive calculation 2: does the 4D hypercube select the unbroken subgroup of Spin(10)?

Exact finite linear algebra on Cl(10) (5 modes, 32 dims, 16 = even half) and on the vector 10.
  A. involutions of so(10) and their commutants (Pati-Salam = flip of exactly 4 generators)
  B. the hypercubic group W(B4) (order 384) acting on the 10 generators: commutants for the natural actions;
     the content each leaves (anomaly, spin)
  C. one-body selectors cannot leave exactly SU(3)xSU(2)xU(1)_Y (double commutant = 13 = SM x U(1)_chi);
     the hypercube supplies no complex structure on its 4 directions
  D. vacuum orientation, Casimir-exchange mean field: singlet (16 x 16bar), 10 (16 x 16) and the 45 directions
     aX + bY, J_12, X, Y; Lorentz-scalar 45 bilinears of one 16 do not exist
Supplied model; finite diagnostic; no physical identification.
"""
import itertools, signal, sys, time
import numpy as np

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (print('TIMEOUT'), sys.exit(1)))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
np.random.seed(20261022)
T0 = time.time()
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))


# ---------------- Clifford algebra Cl(10) on 5 modes (Jordan-Wigner) ----------------
I2 = np.eye(2); X2 = np.array([[0, 1], [1, 0]], complex); Y2 = np.array([[0, -1j], [1j, 0]]); Z2 = np.diag([1., -1.])


def kron(*m):
    out = np.eye(1)
    for a in m:
        out = np.kron(out, a)
    return out


G = []
for j in range(5):
    pre = [Z2] * j; post = [I2] * (4 - j)
    G.append(kron(*pre, X2, *post)); G.append(kron(*pre, Y2, *post))
G = [g.astype(complex) for g in G]
c = [(G[2 * j] + 1j * G[2 * j + 1]) / 2 for j in range(5)]          # annihilators: mode j <-> generators (2j, 2j+1)
Nops = [ci.conj().T @ ci for ci in c]
Ntot = sum(Nops)
par = np.diag(np.round(np.real(np.diag(Ntot))) % 2)
P16 = np.eye(32)[:, np.where(np.diag(par) == 0)[0]]                  # even half = the 16
PAIRS = list(itertools.combinations(range(10), 2))
SIG = [0.5j * G[a] @ G[b] for a, b in PAIRS]                         # Hermitian so(10) generators, eig +-1/2


def r16(M):
    return P16.T @ M @ P16


S16 = [r16(s) for s in SIG]
cas16 = sum(s @ s for s in S16)

# vector-rep so(10) basis
def Lvec(a, b):
    L = np.zeros((10, 10)); L[a, b] = 1; L[b, a] = -1
    return L
LV = [Lvec(a, b) for a, b in PAIRS]


def _unused(mats, basis):
    """dim of span{basis} commuting with every matrix in mats (adjoint action)."""
    if not mats:
        return len(basis)
    rows = []
    for m in mats:
        rows.append(np.array([(m @ B - B @ m).ravel() for B in basis]).T)
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < 1e-9 * max(1, s.max()))) + max(0, len(basis) - A.shape[1] if False else 0)


def nullity(A):
    s = np.linalg.svd(A, compute_uv=False)
    return A.shape[1] - int(np.sum(s > 1e-9 * max(1.0, s.max())))


def comm_dim(mats, basis):
    rows = [np.array([(m @ B - B @ m).ravel() for B in basis]).T for m in mats]
    return nullity(np.vstack(rows)) if rows else len(basis)


print("== A. involutions of so(10): conjugation by a product of k Clifford generators")
dims = {}
for k in range(1, 11):
    T = np.diag([-1.] * k + [1.] * (10 - k))
    dims[k] = comm_dim([T], LV)
exp = {k: k * (k - 1) // 2 + (10 - k) * (9 - k) // 2 for k in range(1, 11)}
check("A1 THEOREM flipping k generators leaves so(k)+so(10-k): Pati-Salam (21) is k = 4, Spin(9) (36) is k = 1",
      all(dims[k] == exp[k] for k in dims) and dims[4] == 21 and dims[1] == 36,
      "dims k=1..9: " + str([dims[k] for k in range(1, 10)]))
Th = G[0] @ G[1] @ G[2] @ G[3]
signs = [np.allclose(Th @ g @ np.linalg.inv(Th), -g) for g in G[:4]] + [np.allclose(Th @ g @ np.linalg.inv(Th), g) for g in G[4:]]
ev = np.round(np.linalg.eigvalsh(r16(Th).real if np.allclose(r16(Th).imag, 0) else (r16(Th) + r16(Th).conj().T) / 2), 6)
check("A2 THEOREM Theta = G1G2G3G4 (square +1) flips the 4, splits 16 = 8 + 8 = (4,2,1) + (4b,1,2)", all(signs) and np.allclose(Th @ Th, np.eye(32)) and sorted(set(ev)) == [-1, 1]
      and list(ev).count(1) == 8, f"Theta^2 = +1, 16 eigenvalues +1 x{list(ev).count(1)}, -1 x{list(ev).count(-1)}")

print("== B. the 4D hypercubic group W(B4) acting on the 10 generators")
def signed_perm(p, s):
    M = np.zeros((4, 4))
    for i in range(4):
        M[p[i], i] = s[i]
    return M
WB4 = [signed_perm(p, s) for p in itertools.permutations(range(4)) for s in itertools.product([1, -1], repeat=4)]
rot = [g for g in WB4 if np.linalg.det(g) > 0]
pl = list(itertools.combinations(range(4), 2))
def wedge2(g):
    M = np.zeros((6, 6))
    for J, (a, b) in enumerate(pl):
        for I, (c_, d) in enumerate(pl):
            M[I, J] = g[c_, a] * g[d, b] - g[d, a] * g[c_, b]
    return M
def blk(*ms):
    n = sum(m.shape[0] for m in ms); out = np.zeros((n, n)); i = 0
    for m in ms:
        k = m.shape[0]; out[i:i + k, i:i + k] = m; i += k
    return out
one = lambda n: np.eye(n)
reps = {
    "4v+6.1 (Gamma_mu on each lattice direction)": lambda g: blk(g, one(6)),
    "4v+Lambda2 (6 = hypercube planes)": lambda g: blk(g, wedge2(g)),
    "4v+4v+2.1 (spin and taste vectors)": lambda g: blk(g, g, one(2)),
    "4v+|4|+2.1 (link modes, reversal = particle-hole)": lambda g: blk(g, np.abs(g), one(2)),
    "4.det+6.1 (lattice seen only through Theta)": lambda g: blk(np.linalg.det(g) * one(4), one(6)),
    "10.1 (lattice blind)": lambda g: one(10),
}
res = {}
for name, f in reps.items():
    mats = [f(g) for g in WB4]
    assert all(np.allclose(m @ m.T, np.eye(10)) for m in mats[:20])
    res[name] = (comm_dim(mats, LV), comm_dim([f(g) for g in rot], LV))
want = [15, 0, 2, 3, 21, 45]
check("B1 THEOREM commutants in so(10) of W(B4) (rotations): PS (21) only if the lattice acts through a sign on 4 generators",
      [r[0] for r in res.values()] == want, "; ".join(f"{k.split(' (')[0]}: {v[0]} ({v[1]})" for k, v in res.items()))
# Theta as image: W(B4) central inversion -1 maps to Theta under the 4v+6.1 lift (product of the 4 reflections)
refl = [np.diag([(-1.) if i == m else 1. for i in range(10)]) for m in range(4)]
cG, cT = comm_dim(refl, LV), comm_dim([np.diag([-1.] * 4 + [1.] * 6)], LV)
check("B2 THEOREM Gamma_mu realisation: inversion -> Theta, but each axis reflection -> Gamma_mu, so C = so(6), not 21", cG == 15 and cT == 21, f"C(G1..G4) = {cG}, C(Theta) = {cT}")
# content when so(4) = span(G_mu G_nu) is the Lorentz group (untwisted): 16 -> (2,1,4) + (1,2,4b)
so4 = [SIG[PAIRS.index(p)] for p in pl]
# self-dual / anti-self-dual combinations
A = [(so4[pl.index((0, 1))] + so4[pl.index((2, 3))]) / 2, (so4[pl.index((0, 2))] - so4[pl.index((1, 3))]) / 2,
     (so4[pl.index((0, 3))] + so4[pl.index((1, 2))]) / 2]
B = [(so4[pl.index((0, 1))] - so4[pl.index((2, 3))]) / 2, (so4[pl.index((0, 2))] + so4[pl.index((1, 3))]) / 2,
     (so4[pl.index((0, 3))] - so4[pl.index((1, 2))]) / 2]
A16 = [r16(a) for a in A]; B16 = [r16(b) for b in B]


def orient(T):
    sg = 1 if np.allclose(T[0] @ T[1] - T[1] @ T[0], 1j * T[2]) else -1
    return [sg * t for t in T]
A16, B16 = orient(A16), orient(B16)
su2ok = lambda T: all(np.allclose(T[i] @ T[j] - T[j] @ T[i], 1j * T[k]) for i, j, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)])
cA = sum(a @ a for a in A16); cB = sum(b @ b for b in B16)
ok_su2 = su2ok(A16) and su2ok(B16) and all(np.allclose(a @ b, b @ a) for a in A16 for b in B16)
PL = np.linalg.eigh(cA)[1][:, np.isclose(np.linalg.eigvalsh(cA), 0.75)]     # (2,1,4): left-handed Weyl
PR = np.linalg.eigh(cB)[1][:, np.isclose(np.linalg.eigvalsh(cB), 0.75)]
H = SIG[PAIRS.index((4, 5))] + SIG[PAIRS.index((6, 7))] + SIG[PAIRS.index((8, 9))]   # Cartan element of so(6) = su(4)
HL = PL.conj().T @ r16(H) @ PL; HR = PR.conj().T @ r16(H) @ PR
anom = np.trace(HL @ HL @ HL).real - np.trace(HR @ HR @ HR).real
check("B3 THEOREM so(4) as Lorentz: 16 = (2,1,4)+(1,2,4b), 8 Weyl, no internal SU(2), SU(4)^3 anomalous",
      ok_su2 and PL.shape[1] == 8 and PR.shape[1] == 8 and abs(anom) > 1,
      f"dims L {PL.shape[1]}, R {PR.shape[1]}; tr_L H^3 - tr_R H^3 = {anom:.2f}")
# twisted: extra Lorentz Weyl index, Lorentz' = Lorentz x diag(so(4) internal)
sl = [kron(s / 2, np.eye(16)) for s in (X2, Y2, Z2)]
Ap = [sl[i] + np.kron(np.eye(2), A16[i]) for i in range(3)]; Bp = [np.kron(np.eye(2), B16[i]) for i in range(3)]
cAp = sum(a @ a for a in Ap); cBp = sum(b @ b for b in Bp)
wA, VA = np.linalg.eigh(cAp)
pairs = set()
jof = lambda c2: round((-1 + np.sqrt(1 + 4 * c2)) / 2, 6)
for v in sorted(set(np.round(wA, 6))):
    sub = VA[:, np.isclose(wA, v)]
    for wb in np.linalg.eigvalsh(sub.conj().T @ cBp @ sub):
        pairs.add((float(jof(v)), float(jof(wb))))
pairs = sorted(pairs)
check("B4 THEOREM twisted (gamma_mu x Gamma_mu): all j_a + j_b integer, against measured spin 1/2",
      all(abs((a + b) - round(a + b)) < 1e-6 for a, b in pairs), f"(j_a, j_b) present: {pairs}")

print("== C. the last step SU(2)_R x U(1)_B-L -> U(1)_Y is not a one-body commutant")
Np = [r16(n) for n in Nops]
Y = (Np[0] + Np[1]) / 2 - (Np[2] + Np[3] + Np[4]) / 3
Xc = r16(2 * Ntot - 5 * np.eye(32))
yv = sorted(float(v) for v in np.round(np.linalg.eigvalsh(Y), 6)); xv = sorted(set(float(v) for v in np.round(np.linalg.eigvalsh(Xc), 6)))
def bil(i, j):
    return r16(c[i].conj().T @ c[j])
su2 = [bil(0, 1) + bil(1, 0), 1j * (bil(0, 1) - bil(1, 0)), bil(0, 0) - bil(1, 1)]
su3 = []
for i, j in itertools.combinations(range(2, 5), 2):
    su3 += [bil(i, j) + bil(j, i), 1j * (bil(i, j) - bil(j, i))]
su3 += [bil(2, 2) - bil(3, 3), bil(2, 2) + bil(3, 3) - 2 * bil(4, 4)]
SM = su3 + su2 + [Y]
in16 = lambda M: np.array([np.trace(s.conj().T @ M).real for s in S16])
basis45 = S16
csm = comm_dim(SM, basis45)
# commutant of SM inside gl(16)
E16 = [np.eye(16)[:, [i]] @ np.eye(16)[[j], :] for i in range(16) for j in range(16)]
gl_c = comm_dim(SM, E16)
yset = sorted(set(yv)); ycount = [yv.count(v) for v in yset]
check("C1 Y = (N1+N2)/2 - (N3+N4+N5)/3, X = 2N - 5: SM hypercharges and chi charges", [round(v, 4) for v in yset] == [-0.6667, -0.5, 0.0, 0.1667, 0.3333, 1.0]
      and ycount == [3, 2, 1, 6, 3, 1] and xv == [-5.0, -1.0, 3.0], f"Y values {[round(v, 4) for v in yset]} x {ycount}; X {xv}")
# double commutant: commutant (in so(10)) of the commutant of SM
ns = np.array([in16(s) for s in S16])
Cbasis = []
Amat = np.vstack([np.array([(m @ B - B @ m).ravel() for B in S16]).T for m in SM])
s, vh = np.linalg.svd(Amat, full_matrices=False)[1:]; null = vh[np.sum(s > 1e-9):].conj()
Cbasis = [sum(v[k] * S16[k] for k in range(45)) for v in null]
dcc = comm_dim(Cbasis, S16)
check("C2 THEOREM C(SM) = span(X,Y), abelian in gl(16) (dim 6): any one-body C(F) >= SM contains C(C(SM)) = 13", csm == 2 and gl_c == 6 and dcc == 13, f"C(SM) {csm}, gl(16) commutant {gl_c}, double commutant {dcc}")
TH = np.diag([-1.] * 4 + [1.] * 6)
Jv = np.zeros((10, 10))
for j in range(5):
    Jv[2 * j + 1, 2 * j] = 1; Jv[2 * j, 2 * j + 1] = -1
check("C3 THEOREM C(Theta, J) = u(2)+u(3) = 13, C(J) = u(5) = 25", comm_dim([TH, Jv], LV) == 13 and comm_dim([Jv], LV) == 25,
      f"C(Theta,J) {comm_dim([TH, Jv], LV)}, C(J) {comm_dim([Jv], LV)}")
E4 = [np.eye(4)[:, [i]] @ np.eye(4)[[j], :] for i in range(4) for j in range(4)]
check("C4 THEOREM W(B4) (and rotations) commutant on R^4 = scalars: no hypercube J, u(2) in so(4) not selected",
      comm_dim(WB4, E4) == 1 and comm_dim(rot, E4) == 1, f"gl(4) commutants {comm_dim(WB4, E4)}, {comm_dim(rot, E4)}")
nucs = np.where(np.isclose(np.linalg.eigvalsh(Y), 0))[0]
Z4 = r16(np.diag(np.exp(1j * np.pi * np.diag(2 * Ntot - 5 * np.eye(32)).real / 2)))
check("C5 nu^c unique Y = 0 state: U(1)_chi breaking needs nu^c nu^c, odd under the protecting Z4 = exp(i pi X/2)",
      np.allclose(Z4, -1j * np.eye(16)) and len(nucs) == 1, "Z4 on 16 = -i; Y = 0 states: 1")

print("== D. vacuum orientation (Casimir exchange, mean field)")
CR = {}
cas = lambda Ms: sum(m @ m for m in Ms)
C2 = np.zeros((256, 256), complex); C2b = np.zeros((256, 256), complex)
for s_ in S16:
    t = np.kron(s_, np.eye(16)) + np.kron(np.eye(16), s_); C2 += t @ t
    t = np.kron(s_, np.eye(16)) - np.kron(np.eye(16), s_.conj()); C2b += t @ t
del t
ev2 = np.round(np.linalg.eigvalsh(C2), 6); ev2b = np.round(np.linalg.eigvalsh(C2b), 6)
mult = lambda e: {float(v): list(e).count(v) for v in sorted(set(e))}
m1, m2 = mult(ev2), mult(ev2b)
c16 = np.trace(cas(S16)).real / 16
check("D1 THEOREM C16 = 45/4; Casimir multiplicities below: one chiral 16 has no 45 bilinear (needs mirror/composite)",
      abs(c16 - 11.25) < 1e-9 and m1 == {9.0: 10, 21.0: 120, 25.0: 126} and m2 == {0.0: 1, 16.0: 45, 24.0: 210},
      f"16x16 {m1}; 16x16b {m2}")
dC = {k: (2 * c16 - v) / 2 for k, v in [("1", 0), ("45", 16), ("210", 24), ("10", 9), ("120", 21), ("126", 25)]}
print(f"   binding Delta C = (2 C16 - C_R)/2: " + ", ".join(f"{k} {v:+.2f}" for k, v in dC.items()))
Cm = G[1] @ G[3] @ G[5] @ G[7] @ G[9]
Ma = [r16(Cm @ g) for g in G]
phi = np.random.randn(10); Mphi = sum(p * m for p, m in zip(phi, Ma))
sv10 = np.linalg.svd(Mphi, compute_uv=False) / np.linalg.norm(phi)
check("D2 THEOREM the 10 pairing has uniform gaps in every direction", np.allclose(sv10, sv10[0]) and np.allclose(sv10, 1), f"sv spread {np.ptp(sv10):.1e}")


def phi_bcs(x):
    x = np.abs(x) + 1e-300
    return 0.5 * np.sqrt(1 + x * x) + 0.5 * x * x * np.arcsinh(1 / x) - 0.5


def Fmin(spec, g):
    spec = np.asarray(spec, float); spec = spec * np.sqrt(len(spec) / np.sum(spec ** 2))
    D = np.linspace(1e-4, 3, 1500)
    F = len(spec) * D ** 2 / g - np.array([np.sum(phi_bcs(d * spec)) for d in D])
    i = int(np.argmin(F)); return F[i]


def spec45(h):
    return np.abs(np.linalg.eigvalsh(h))
J12 = S16[PAIRS.index((0, 1))]
spX, spY, spJ = spec45(Xc), spec45(Y), spec45(J12)
best_ab = None
for t in np.linspace(0, np.pi, 181):
    sp = spec45(np.cos(t) * Xc / np.linalg.norm(Xc) + np.sin(t) * Y / np.linalg.norm(Y))
    f = Fmin(sp, 0.25 * dC["45"])
    if best_ab is None or f < best_ab[0]:
        best_ab = (f, t)
# best 45 orientation over Cartan directions
best45 = (0, None)
cart = [S16[PAIRS.index((2 * j, 2 * j + 1))] for j in range(5)]
for th in [np.eye(5)[0], np.ones(5)] + [np.random.randn(5) for _ in range(80)]:
    f = Fmin(spec45(sum(t * h for t, h in zip(th, cart))), 0.25 * dC["45"])
    if f < best45[0]:
        best45 = (f, th / np.linalg.norm(th))
nzero = int(np.sum(np.isclose(spY, 0)))
for g0 in (0.25, 0.4):
    Fs = {"singlet": Fmin(np.ones(16), g0 * dC["1"]), "10 (Spin9)": Fmin(sv10, g0 * dC["10"]),
          "45 J12": Fmin(spJ, g0 * dC["45"]), "45 X": Fmin(spX, g0 * dC["45"]), "45 Y": Fmin(spY, g0 * dC["45"]),
          "45 best aX+bY": min(Fmin(spec45(np.cos(t) * Xc / np.linalg.norm(Xc) + np.sin(t) * Y / np.linalg.norm(Y)), g0 * dC["45"])
                               for t in np.linspace(0, np.pi, 91))}
    order = sorted(Fs, key=Fs.get)
    check(f"D3 DIAGNOSTIC g0 = {g0}: F order singlet < 10 < 45 J12 < aX+bY", order[0] == "singlet" and order[1] == "10 (Spin9)" and Fs["45 J12"] < Fs["45 best aX+bY"] - 1e-12,
          ", ".join(f"{k} {Fs[k]:.3e}" for k in order))
check("D4 DIAGNOSTIC J_12 (C = 29) beats every aX+bY; best of 82 Cartan directions is one plane", nzero == 1 and
      Fmin(spJ, 0.25 * dC["45"]) < best_ab[0] and np.max(np.abs(best45[1])) > 0.99,
      f"Y zeros {nzero}, best aX+bY angle {best_ab[1]:.3f}, best Cartan |theta| max {np.max(np.abs(best45[1])):.3f}, "
      f"C(J12) {comm_dim([Lvec(0, 1)], LV)}")
check("D5 a Theta selector does not help: singlet, J_12, X, Y all commute with Theta", all(np.allclose(r16(Th) @ M, M @ r16(Th)) for M in (J12, Xc, Y,
      np.eye(16))), "all four commute with Theta")
print("== E. owner principle: the 5 (10 = 4 + 6) from covariant clusters of one-mode sites, not one site")
Wst = np.array(WB4)                                                   # (384, 4, 4)
pts = np.array(list(itertools.product(range(-4, 5), repeat=4))).T    # site-centred window
orb = {}
for n in range(pts.shape[1]):
    key = tuple(sorted(np.abs(pts[:, n])))
    if key not in orb:
        orb[key] = n
sizes = {k: len({tuple(v) for v in Wst @ pts[:, n]}) for k, n in orb.items()}
# body-centred orbits (doubled coordinates, odd entries)
bpts = np.array(list(itertools.product([-7, -5, -3, -1, 1, 3, 5, 7], repeat=4))).T
bs = set()
for n in range(bpts.shape[1]):
    if list(np.abs(bpts[:, n])) == sorted(np.abs(bpts[:, n])) and all(bpts[:, n] > 0):
        bs.add(len({tuple(v) for v in Wst @ bpts[:, n]}))
nontriv = sorted(set(v for k, v in sizes.items() if any(k)))
Oh = [np.array([[sg[i] if p[i] == j else 0 for i in range(3)] for j in range(3)])
      for p in itertools.permutations(range(3)) for sg in itertools.product([1, -1], repeat=3)]
o3 = min(len({tuple(g @ np.array(v)) for g in Oh}) for v in itertools.product(range(-2, 3), repeat=3) if any(v))
check("E1 THEOREM no covariant 5-site cluster: site-centred orbits even >= 8 (O_h: >= 6), body-centred even >= 16 (other "
      "centres: inversion pairs sites, argued)", o3 == 6 and len(Oh) == 48 and min(nontriv) == 8 and
      all(v % 2 == 0 for v in nontriv) and min(bs) == 16 and all(v % 2 == 0 for v in bs),
      f"site orbits {nontriv[:6]}..., body {sorted(bs)[:3]}...")
check("E2 THEOREM (Frobenius, cited) group orders 384, 768, 12288, 48, 96 are 2^a 3^b: no protected 5 or 10 multiplet",
      all(n % 5 for n in (384, 768, 12288, 48, 96)) and 384 % 16 == 0 and len(WB4) == 384)
chars = {"perm sign": lambda g: round(np.linalg.det(np.abs(g))), "flip sign": lambda g: round(np.linalg.det(g) * np.linalg.det(np.abs(g))),
         "det": lambda g: round(np.linalg.det(g))}
minorb = {}
for name, ch in chars.items():
    best = None
    for k, n in orb.items():
        v = pts[:, n]
        H = [g for g in WB4 if np.array_equal(g @ v, v)]
        if all(ch(h) == 1 for h in H) and (best is None or (sizes[k], sum(k)) < (best[0], sum(best[1]))):
            best = (sizes[k], k)
    minorb[name] = best
check("E3 THEOREM smallest orbit carrying each 1-dim character (trivial on stabiliser)",
      minorb["flip sign"][0] == 16 and minorb["perm sign"][0] == 192 and minorb["det"][0] == 384,
      "; ".join(f"{k}: {v[0]} at {tuple(int(x) for x in v[1])}" for k, v in minorb.items()))
# the 33-site cluster: centre + corners at 1 and at 2
cl = [np.zeros(4, int)] + [np.array(s) for s in itertools.product([1, -1], repeat=4)] + [2 * np.array(s) for s in itertools.product([1, -1], repeat=4)]
cidx = {tuple(v): i for i, v in enumerate(cl)}
def permrep(g):
    P = np.zeros((33, 33))
    for i, v in enumerate(cl):
        P[cidx[tuple(g @ v)], i] = 1
    return P
RG = [permrep(g) for g in WB4]
fl = chars["flip sign"]
Ptr = sum(RG) / 384; Pfl = sum(fl(g) * R for g, R in zip(WB4, RG)) / 384
rt, rf = int(round(np.trace(Ptr))), int(round(np.trace(Pfl)))
gens = [permrep(signed_perm((1, 0, 2, 3), (1, 1, 1, 1))), permrep(signed_perm((1, 2, 3, 0), (1, 1, 1, 1))),
        permrep(signed_perm((0, 1, 2, 3), (-1, 1, 1, 1)))]
E33 = [np.eye(33)[:, [i]] @ np.eye(33)[[j], :] for i in range(33) for j in range(33)]
cG = comm_dim(gens, E33)
Rr = np.random.randn(33, 33); Rr = Rr + Rr.T
Hinv = sum(R @ Rr @ R.T for R in RG) / 384
cGH = comm_dim(gens + [Hinv], E33)
# light 5 = trivial(3) + flip(2) made degenerate by hand; lattice action on the 10 Majoranas of those 5 modes
Bt = np.linalg.eigh(Ptr)[1][:, -rt:]; Bf = np.linalg.eigh(Pfl)[1][:, -rf:]
B5 = np.hstack([Bt, Bf])
rho5 = [B5.T @ R @ B5 for R in [gens[0], gens[1], gens[2]]]
rho10 = [np.kron(r, np.eye(2)) for r in rho5]
J10 = np.kron(np.eye(5), np.array([[0., -1.], [1., 0.]]))
check("E4 THEOREM 33-site cluster (centre, corners at 1, 2): trivial x3 + flip x2 -> C = PS (21); with mode number J: 13",
      rt == 3 and rf == 2 and comm_dim(rho10, LV) == 21 and comm_dim(rho10 + [J10], LV) == 13,
      f"multiplicities {rt}, {rf}; C = {comm_dim(rho10, LV)}, with J {comm_dim(rho10 + [J10], LV)}")
check("E5 THEOREM (Schur) a generic invariant update leaves an abelian commutant: the 3+2 degeneracy costs 3 tuned equalities",
      cGH < cG and cGH == len(set(np.round(np.linalg.eigvalsh(Hinv), 8))), f"distinct levels {len(set(np.round(np.linalg.eigvalsh(Hinv), 8)))}; commutant of the lattice {cG} (sum m^2), with a generic invariant update {cGH} (sum m)")
print("supplied: Cl(10) on 5 modes (an abstract algebra; one site holding 5 modes is a smuggling risk, see E), the W(B4) actions listed in B1, the Casimir-exchange (one-gauge-boson) channel strengths, "
      "flat-band BCS with unit cutoff, couplings g0; cited: involution classification of so(n) (Cartan), MAC heuristic")
print(f"elapsed {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
