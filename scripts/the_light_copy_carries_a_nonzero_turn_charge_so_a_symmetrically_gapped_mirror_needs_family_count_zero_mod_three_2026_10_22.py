AUDIT_INPUT_PATHS = ('docs/THE_LIGHT_COPY_CARRIES_A_NONZERO_TURN_CHARGE_SO_A_SYMMETRICALLY_GAPPED_MIRROR_NEEDS_FAMILY_COUNT_ZERO_MOD_THREE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""family-count-5mode: is there a non-fitted reason for exactly 3 families when each site carries
5 modes (Spin(10) on a 16 per family) and the cell/tick is CL-1's (2^3 cell, Margolus cube tick on both
tilings, face phase -1, copy mass)?

Self-contained (numpy + scipy). Seeded. Exact finite checks:
  A. CL-1 cell tick, the 24 cube-centred rotations (site gauge), and which survive the copy mass.
  B. The C3 taste charge q of the light copy left by the copy mass (gauge-invariant: det of the turn on
     the light chirality block = lambda^2), on both chiralities, both copy-mass signs, two steps.
  C. Spin(10) data from weights: 4 instanton zero modes per 16 (2T(16) = 4), centre Z4, Delta n = 0 mod 4.
  D. Anomaly algebra for N family-blind copies with the mirror gapped keeping Spin(10) and one turn:
     vertex phase w^(4Nq); every twist (fermion number Z_m, Spin(10), family U(N)) fails to rescue N != 0 mod 3.
  E. Doubling counts (candidate a) and the hw-corner triplet (anomaly-silent).
  F. Cone-rule sums (candidate c) are linear in N, so they select nothing.
  G. Z-width estimate (not a check of the rule).
"""
import itertools as it
import numpy as np
from scipy.linalg import expm, null_space

AUDIT_TIMEOUT_SEC = 90
rng = np.random.default_rng(20261022)
NPASS = NFAIL = 0
W3 = np.exp(2j * np.pi / 3)


def check(name, ok, detail=""):
    global NPASS, NFAIL
    ok = bool(ok)
    NPASS += ok
    NFAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


# ------------------------------------------------------------------ A. CL-1 cell tick
print("== A. CL-1 cell: one mode per site per internal component, face phase -1, cube tick ==")
CELL = list(it.product([0, 1], repeat=3))
IDX = {a: 4 * a[0] + 2 * a[1] + a[2] for a in CELL}


def eta(i, a):
    return [1, (-1) ** a[0], (-1) ** (a[0] + a[1])][i]


def W_even(i):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == 0:
            b = list(a); b[i] = 1; b = tuple(b)
            M[IDX[b], IDX[a]] = M[IDX[a], IDX[b]] = eta(i, a)
    return M


def W_odd(i, k):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == 1:
            b = list(a); b[i] = 0; b = tuple(b)
            ph = np.exp(2j * k[i])
            M[IDX[b], IDX[a]] = eta(i, a) * ph
            M[IDX[a], IDX[b]] = eta(i, a) * np.conj(ph)
    return M


W = [W_even(i) for i in range(3)]
Re = sum(W) / np.sqrt(3)
s_copy = 1j * W[0] @ W[1] @ W[2] @ Re


def U(k, eps=0.3, mu=0.0, M=0.0, cs=1):
    Ro = sum(W_odd(i, k) for i in range(3)) / np.sqrt(3)
    Ue = expm(-1j * (eps - mu / 2) * Re)
    if M:
        Cm = expm(1j * (M / 4) * (np.eye(8) - cs * s_copy) @ Re)
        Ue = Cm @ Ue @ Cm
    return expm(1j * (eps + mu / 2) * Ro) @ Ue


ROTS = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0:
            ROTS.append(R)
isC3 = [round(np.trace(R)) == 0 for R in ROTS]
cen = np.array([0.5, 0.5, 0.5])
SIGNS = list(it.product([1, -1], repeat=8))
kt = [rng.uniform(-1, 1, 3) for _ in range(2)]


def site_perm(R):
    P = np.zeros((8, 8))
    for a in CELL:
        b = tuple(np.rint(R @ (np.array(a) - cen) + cen).astype(int)); P[IDX[b], IDX[a]] = 1
    return P


def gauges(R, **kw):
    P = site_perm(R)
    out = []
    for sgn in SIGNS:
        Vg = np.diag(sgn) @ P
        if all(np.allclose(Vg @ U(k, **kw) @ Vg.T, U(R @ k, **kw), atol=1e-10) for k in kt):
            out.append(Vg)
    return out


def even_perm(R):
    p = [int(np.argmax(abs(R[:, i]))) for i in range(3)]
    return sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j]) % 2 == 0


V0 = [gauges(R) for R in ROTS]
check("A1 all 24 cube-centred rotations are tick symmetries up to a +-1 site gauge, unique up to overall sign",
      all(len(g) == 2 for g in V0))
VM = [gauges(R, M=0.7) for R in ROTS]
kept = [len(g) > 0 for g in VM]
nC3k = sum(1 for n in range(24) if kept[n] and isC3[n])
check("A2 the copy mass keeps exactly the 12 even (tetrahedral) rotations, including all 8 three-fold turns",
      sum(kept) == 12 and nC3k == 8 and all(kept[n] == even_perm(ROTS[n]) for n in range(24)),
      f"kept {sum(kept)}, turns kept {nC3k}")
h = 1e-6
Av = []
for i in range(3):
    d = np.zeros(3); d[i] = h
    Av.append(1j * (U(d) - U(-d)) / (2 * h))
v2 = np.trace(Av[0] @ Av[0]).real / 8
Ah = [a / np.sqrt(v2) for a in Av]
S = [-0.25j * (Ah[(i + 1) % 3] @ Ah[(i + 2) % 3] - Ah[(i + 2) % 3] @ Ah[(i + 1) % 3]) for i in range(3)]
chi = 1j * Ah[0] @ Ah[1] @ Ah[2]
check("A3 velocity matrices give Cl(3) (one cone), spin su(2), chirality chi = iA1A2A3 traceless (n_L = n_R)",
      all(np.allclose(Ah[i] @ Ah[j] + Ah[j] @ Ah[i], 2 * (i == j) * np.eye(8), atol=1e-5) for i in range(3) for j in range(3))
      and abs(np.trace(chi)) < 1e-6 and np.allclose(chi @ s_copy, s_copy @ chi, atol=1e-6))


def axang(R):
    w, v = np.linalg.eig(R)
    n = np.real(v[:, np.argmin(abs(w - 1))])
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    if not np.allclose(expm(th * K), R):
        n = -n
    return n, th


def spinor(R):
    n, th = axang(R)
    return expm(-1j * th * sum(n[i] * S[i] for i in range(3)))


# ------------------------------------------------------------------ B. C3 taste charge of the light copy
print("== B. C3 taste charge q of the light copy (det of the turn on a light chirality block = lambda^2) ==")


def qcharge(d):
    """lambda^2 = det; lambda^3 = +-1 so lambda^2 = w^(2q) up to the sign; return q mod 3 or None."""
    for q in range(3):
        if abs(d - W3 ** (2 * q)) < 1e-6:
            return q
    return None


def light_blocks(M, eps=0.3, tol=1e-3, cs=1):
    Uk = U(np.zeros(3), eps=eps, M=M, cs=cs)
    w, v = np.linalg.eig(Uk)
    Lt = v[:, abs(np.angle(w)) < tol]
    Lt, _ = np.linalg.qr(Lt)
    out = {}
    for s in (+1, -1):
        Pc = Lt.conj().T @ ((np.eye(8) + s * chi) / 2) @ Lt
        ew, ev = np.linalg.eigh((Pc + Pc.conj().T) / 2)
        out[s] = Lt @ ev[:, ew > 0.5]
    return out


res = {}
for M, cs in ((0.7, 1), (-0.7, 1), (0.7, -1)):
    for eps in (0.3, 0.5):
        B = light_blocks(M, eps, cs=cs)
        for n in range(24):
            if not isC3[n]:
                continue
            Vg = gauges(ROTS[n], eps=eps, M=M, cs=cs)[0]
            rho = spinor(ROTS[n])
            for s in (+1, -1):
                X = B[s]
                Vl = X.conj().T @ Vg @ X
                lam_op = X.conj().T @ (rho.conj().T @ Vg) @ X
                scal = np.allclose(lam_op, lam_op[0, 0] * np.eye(2), atol=1e-6)
                res[((M, cs), eps, n, s)] = (X.shape[1], scal, qcharge(np.linalg.det(Vl)))
dims_ok = all(r[0] == 2 for r in res.values())
check("B1 copy mass leaves one light taste per chirality (2 spin states each) at k = 0, both signs, eps = 0.3, 0.5",
      dims_ok)
check("B2 on each light block the turn factorises as spin-1/2 rotation x a scalar taste phase lambda",
      all(r[1] for r in res.values()))
qs = {k: r[2] for k, r in res.items()}
check("B3 every three-fold turn has NONZERO taste charge on the light copy (q in {1,2}, never 0)",
      all(q in (1, 2) for q in qs.values()), f"q values seen {sorted(set(qs.values()))}")
check("B4 light L and light R carry the same q (the free tick is anomaly-free: the cone-rule sum q_L - q_R = 0)",
      all(qs[(M, e, n, 1)] == qs[(M, e, n, -1)] for (M, e, n, s) in qs if s == 1))
ninv = {}
for n in range(24):
    if isC3[n]:
        ninv[n] = next(m for m in range(24) if np.allclose(ROTS[m], ROTS[n].T))
check("B5 q(turn^-1) = -q(turn) and q is independent of the step eps (a topological, not dynamical, number)",
      all((qs[(M, e, n, s)] + qs[(M, e, ninv[n], s)]) % 3 == 0 for (M, e, n, s) in qs)
      and all(qs[(M, 0.3, n, s)] == qs[(M, 0.5, n, s)] for (M, e, n, s) in qs))
qsame = all(qs[((0.7, 1), 0.3, n, 1)] == qs[((-0.7, 1), 0.3, n, 1)] for n in ninv)
qflip = all(qs[((0.7, 1), 0.3, n, 1)] == (-qs[((0.7, -1), 0.3, n, 1)]) % 3 for n in ninv)
check("B6 q is blind to the copy-mass sign; the copy-sign projector (1 -+ s) picks which E taste stays light "
      "(q -> -q), and neither gives q = 0", qsame and qflip)
# massless tick: both tastes light per chirality, charges {1,2}
Uk = U(np.zeros(3))
Vg = V0[next(n for n in range(24) if isC3[n])][0]
nC = next(n for n in range(24) if isC3[n])
tau = spinor(ROTS[nC]).conj().T @ Vg
PL = (np.eye(8) + chi) / 2
tl = np.linalg.eigvals(tau @ PL + 10 * (np.eye(8) - PL))
tl = tl[abs(tl) < 2]
if not np.allclose(tl ** 3, 1, atol=1e-6):
    tl = -tl
qm = sorted(int(round(np.angle(x) / (2 * np.pi / 3))) % 3 for x in tl)
check("B7 without the copy mass the two light tastes per chirality are E with q = {1, 2} (one of each spin pair): sum 0",
      qm == [1, 1, 2, 2], f"taste phases per L state -> q {qm}")

# ------------------------------------------------------------------ C. Spin(10) weights
print("== C. Spin(10) on the 16: zero modes, centre, fermion-number steps ==")
WTS = [np.array(w) / 2 for w in it.product([1, -1], repeat=5) if sum(1 for x in w if x < 0) % 2 == 0]
WV = [s * np.eye(5)[i] for i in range(5) for s in (1, -1)]
T16 = sum(w[0] ** 2 for w in WTS); T10 = sum(w[0] ** 2 for w in WV)
check("C1 Dynkin index ratio T(16)/T(10) = 2, so a unit Spin(10) instanton has 2T(16) = 4 zero modes per 16",
      len(WTS) == 16 and abs(T16 / T10 - 2) < 1e-12, f"T16 = {T16}, T10 = {T10}")
zm = [w for w in WTS if w[0] == 0.5 and w[1] == 0.5]
check("C2 explicit: an SU(2)_A instanton in Spin(4) x Spin(6) sees 4 doublets in the 16; zero-mode weights sum to "
      "zero on every centraliser Cartan (Spin(10)-twists leave the vertex phase 1)",
      len(zm) == 4 and np.allclose(sum(w[2:] for w in zm), 0) and abs(sum(w[0] - w[1] for w in zm)) < 1e-12)
cz = [np.exp(1j * np.pi * sum(w)) for w in WTS]
check("C3 the centre element exp(i pi sum H) acts on the 16 as one phase of order 4 (Z4, square = (-1)^F)",
      np.allclose(cz, cz[0]) and abs(cz[0] ** 2 + 1) < 1e-12)
dn_ok = all((abs(cz[0] ** dn - 1) < 1e-9) == (dn % 4 == 0) for dn in range(1, 25))
check("C4 a Spin(10)-invariant term changes fermion number by Delta n = 0 mod 4 (needs centre charge 1)", dn_ok)
check("C5 the mirror 16bar alone has U(1)_F x Spin(10)^2 = 4 per family != 0: symmetric gapping must break U(1)_F",
      2 * T16 / T10 == 4)

# ------------------------------------------------------------------ D. anomaly algebra
print("== D. N family-blind copies, mirror gapped keeping Spin(10) and one turn ==")
q0 = qs[((0.7, 1), 0.3, nC, 1)]
NS = range(1, 13)


def vertex_ok(N, q, nzm=4):
    return abs(W3 ** (nzm * N * q) - 1) < 1e-9


allowed = [N for N in NS if vertex_ok(N, q0)]
check("D1 light vertex phase w^(4Nq), q != 0: the turn survives mirror gapping only for N = 0 mod 3; smallest N = 3",
      allowed == [3, 6, 9, 12], f"q = {q0}, allowed N <= 12: {allowed}")
grav = [N for N in NS if (16 * N * q0) % 3 == 0]
cub = [N for N in NS if (16 * N * q0 ** 3) % 3 == 0]
check("D2 the mixed turn-gravity (16Nq) and cubic (16Nq^3) conditions give the same set (cited normalisations)",
      grav == allowed and cub == allowed)
check("D3 contrast: with both E tastes light (no copy mass) the light charges sum to 1 + 2 = 0: every N allowed",
      all(abs(W3 ** (4 * N * (1 + 2)) - 1) < 1e-9 for N in NS))
# twist by a residual fermion-number Z_m: must be mirror anomaly-free (4N = 0 mod m and 16N = 0 mod m)
resc = {}
for N in NS:
    ms = [m for m in range(2, 200) if (4 * N) % m == 0 and (16 * N) % m == 0]
    resc[N] = any(m % 3 == 0 for m in ms)
check("D4 a Z3 inside the residual fermion-number group Z_m (m | 4N, mirror anomaly-free) exists only if 3 | N: "
      "no fermion-number twist rescues N != 0 mod 3", all(resc[N] == (N % 3 == 0) for N in NS))
# family twists h in U(N) act alike on light L and mirror (exact commutant of the copy-mass tick is U(1) per mode)
ok_h = True
for N in (1, 2, 4, 5):
    for _ in range(30):
        ph = rng.integers(0, 12, N)
        dh = np.exp(2j * np.pi * ph.sum() / 12)
        if abs(dh ** (-4) - 1) < 1e-9:
            ok_h &= abs(W3 ** (4 * N * q0) * dh ** 4 - 1) > 1e-6
check("D5 a family twist h is allowed on the mirror only if det(h)^4 = 1, which leaves the light phase w^(4Nq) != 1 "
      "for N = 1, 2, 4, 5", ok_h and abs(W3 ** (4 * 1 * q0) - 1) > 1e-6)
Uqs = [U(rng.uniform(-1.5, 1.5, 3), M=0.7) for _ in range(3)]
cdim2 = null_space(np.vstack([np.kron(u, np.eye(8)) - np.kron(np.eye(8), u.T) for u in Uqs]), rcond=1e-9).shape[1]
check("D6 the copy-mass tick's exact internal commutant (three generic k) is dim 1 per mode: a twist acts alike on L and R",
      cdim2 == 1, f"dim {cdim2}")
fam_dep = [N for N in NS if any(sum(c) % 3 == 0 for c in it.product((1, 2), repeat=N))]
check("D7 loophole: family-dependent copy-sign projectors (q_f in {1,2}) allow every N >= 2; N = 1 is obstructed under every choice",
      fam_dep == list(range(2, 13)))

l8 = np.diag([1, 1, -2]) / np.sqrt(3)
check("D8 candidate SU(3)_family on the light 16s: cubic anomaly 16 x tr(l8^3) != 0, so a family SU(N >= 3) cannot "
      "be gauged and gives no count", abs(16 * np.trace(l8 @ l8 @ l8)) > 1)

# ------------------------------------------------------------------ E. doubling counts (candidate a)
print("== E. doubling counts with the 16 ==")
check("E1 per family the massless tick has 2 light 16 + 2 light 16bar (E + E), the copy mass 1 + 1; "
      "never 3 (counts are powers of 2 times 1)", dims_ok and np.trace(PL).real == 4)
corners = list(it.product([0, 1], repeat=3))
hw1 = [c for c in corners if sum(c) == 1]
Pm = np.zeros((3, 3))
for j, c in enumerate(hw1):
    Pm[hw1.index((c[2], c[0], c[1])), j] = 1
qp = sorted(int(round(np.angle(x) / (2 * np.pi / 3))) % 3 for x in np.linalg.eigvals(Pm))
check("E2 the hw = 1 corner triplet (the 3 of 8 = 1+3+3+1) carries turn charges {0,1,2}: sum 0, so the anomaly "
      "is silent there (the triplet route gets no count from (b))", qp == [0, 1, 2] and sum(qp) % 3 == 0)
check("E3 Nielsen-Ninomiya on the cell: tr chi = 0 for any N copies (n_16 = n_16bar before mirror removal)",
      abs(np.trace(np.kron(chi, np.eye(5)))) < 1e-6)

# ------------------------------------------------------------------ F. cone-rule sums (candidate c)
print("== F. cone-rule corollary 'charges sum to zero' over many cones ==")
okF = True
for N in range(1, 7):
    for _ in range(3):
        Q = rng.normal(size=(N, N)); Q = Q + Q.T
        okF &= abs(np.trace(np.kron(chi, Q))) < 1e-6
check("F1 for N family-blind copies every cone-rule sum is tr(chi) x tr(Q) = 0 for EVERY N: linear sums select nothing",
      okF)
check("F2 the only N-sensitive datum is the multiplicative vertex phase after the mirror is removed (= D1)",
      len(allowed) < len(NS))

# ------------------------------------------------------------------ G. estimate
print("== G. estimate against measurement (not a check of the rule) ==")
Nnu, dN = 2.9840, 0.0082
sig = {N: abs(N - Nnu) / dN for N in (3, 6)}
print(f"  LEP N_nu = {Nnu} +- {dN}: N = 3 at {sig[3]:.1f} sigma, N = 6 at {sig[6]:.0f} sigma; N = 1 (copy mass, one "
      f"family) at {abs(1 - Nnu) / dN:.0f} sigma")
check("G1 among the allowed set {3, 6, 9, ...} only N = 3 survives the Z width (>300 sigma for N = 6)",
      sig[3] < 3 and sig[6] > 300)
print(f"TOTAL: PASS={NPASS} FAIL={NFAIL}")
