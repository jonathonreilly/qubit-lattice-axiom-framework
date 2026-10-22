AUDIT_INPUT_PATHS = ('docs/UNTUNED_ALL_DIRECTION_MASSLESS_CROSSINGS_SELECT_SPACE_DIMENSION_EQUAL_TO_THE_BLOCH_BALL_DIMENSION_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""why-three-dims: which structural principles select d = 3 space dimensions?

Sections
  A  codimension of a two-fold level crossing = Bloch-ball dimension (R, C, H)
  B  generic nearest-neighbour two-level bands on Z^d: gapped (d<3), isolated
     cones (d=3), nodal manifolds with flat directions (d>3); real class -> d=2,
     quaternionic class -> d=5
  C  at a d=3 cone: chirality = sign det J = solid-angle degree, total zero
     (Nielsen-Ninomiya), and space rotations act as qubit (SU(2)) rotations
  D  clause checks for candidate (a): chirality needs odd d, propagating
     photon/graviton counts, 1+1D 3-4-5-0 anomaly freedom
  E  candidate (c): lattice Green function at the origin (Polya), radial
     Coulomb binding in d = 3, 4, 5 with a short-distance cutoff
  F  candidate (d): Clifford algebra of the 2^d cell, Weyl species per
     chirality for one mode per site; staggered Z^3 zero-mode count
Self-contained: numpy + scipy.  Seeded.  Stdout < 6000 chars.
"""
AUDIT_TIMEOUT_SEC = 120

import itertools
import time

import numpy as np
from scipy import integrate, optimize, special
from scipy.linalg import eigh_tridiagonal

T0 = time.time()
PASS = 0
FAIL = 0
RNG = np.random.default_rng(20261022)


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS" if ok else "FAIL") + ": " + name + (" | " + detail if detail else ""))


SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)


def kron_all(ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


def clifford_gens(n_pairs):
    """2*n_pairs mutually anticommuting Hermitian matrices on (C^2)^{n_pairs} (Jordan-Wigner)."""
    g = []
    for j in range(n_pairs):
        left = [SZ] * j
        right = [I2] * (n_pairs - j - 1)
        g.append(kron_all(left + [SX] + right))
        g.append(kron_all(left + [SY] + right))
    return g


# ------------------------------------------------------------------ A
print("== A: crossing codimension = Bloch-ball dimension ==")
# traceless Hermitian 2x2 over F = R, C, H as real vector spaces:
# diagonal (t, -t): 1 real; off-diagonal one element of F: beta reals.
def traceless_herm_dim(beta):
    # realise H-valued 2x2 as 4x4 complex with quaternion structure J; count real
    # dimension of {X : X^dag = X, tr X = 0, X commutes with the F-structure}.
    if beta == 1:
        basis_space = [np.real(SX), np.real(SZ)]
        return np.linalg.matrix_rank(np.array([b.ravel() for b in basis_space]))
    if beta == 2:
        return np.linalg.matrix_rank(np.array([np.concatenate([m.real.ravel(), m.imag.ravel()]) for m in (SX, SY, SZ)]))
    # beta = 4: quaternion-Hermitian 2x2 == 4x4 Hermitian commuting with antiunitary J = (I (x) i sy) K
    J = np.kron(I2, 1j * SY)
    herm = []
    for a in range(4):
        for b in range(a, 4):
            for ph in ([1] if a == b else [1, 1j]):
                M = np.zeros((4, 4), complex)
                M[a, b] = ph
                M[b, a] = np.conj(ph)
                herm.append(M)
    # constraint: J conj(M) J^-1 = M  and tr M = 0 ; solve linear real system
    rows = []
    for M in herm:
        C = J @ np.conj(M) @ np.linalg.inv(J) - M
        rows.append(np.concatenate([C.real.ravel(), C.imag.ravel(), [np.trace(M).real]]))
    A = np.array(rows).T  # columns = basis elements
    null = A.shape[1] - np.linalg.matrix_rank(A, tol=1e-10)
    return null


dims = {b: int(traceless_herm_dim(b)) for b in (1, 2, 4)}
check("A1 codim of a 2-fold crossing = beta+1 = Bloch-ball dim (R,C,H -> 2,3,5)",
      dims == {1: 2, 2: 3, 4: 5}, str(dims))

# ------------------------------------------------------------------ B
print("== B: generic nearest-neighbour two-level bands on Z^d ==")


def make_model(d, m, rng, cscale=0.3):
    a = rng.normal(size=(d, m))
    b = rng.normal(size=(d, m))
    c = cscale * rng.normal(size=m)
    return a, b, c


def hvec(k, mdl):
    a, b, c = mdl
    return c + np.cos(k) @ a + np.sin(k) @ b


def jac(k, mdl):
    a, b, c = mdl
    return (-np.sin(k)[:, None] * a + np.cos(k)[:, None] * b).T  # m x d


def grid(d, n):
    ax = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return np.array(list(itertools.product(ax, repeat=d)))


def min_gap(d, mdl, n):
    K = grid(d, n)
    H = mdl[2] + np.cos(K) @ mdl[0] + np.sin(K) @ mdl[1]
    nrm = np.linalg.norm(H, axis=1)
    i0 = np.argsort(nrm)[:8]
    best = nrm[i0[0]]
    for i in i0:
        r = optimize.minimize(lambda k: np.linalg.norm(hvec(k, mdl)), K[i], method="Nelder-Mead",
                              options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 4000})
        best = min(best, r.fun)
    return best


# B1: d = 1, 2 complex: generically gapped
gaps = {}
for d in (1, 2):
    gaps[d] = [min_gap(d, make_model(d, 3, RNG), 64 if d == 2 else 512) for _ in range(12)]
check("B1 d=1,2 complex two-level bands: all 12+12 random NN models gapped (min 2|h| > 1e-2)",
      min(min(gaps[1]), min(gaps[2])) > 5e-3,
      "min|h| d=1 %.3f, d=2 %.3f" % (min(gaps[1]), min(gaps[2])))


def find_nodes(d, mdl, n, nseed=200):
    K = grid(d, n)
    H = mdl[2] + np.cos(K) @ mdl[0] + np.sin(K) @ mdl[1]
    nrm = np.linalg.norm(H, axis=1)
    idx = np.argsort(nrm)[:nseed]
    nodes = []
    for i in idx:
        sol = optimize.root(lambda k: hvec(k, mdl), K[i], jac=lambda k: jac(k, mdl), method="hybr")
        if sol.success and np.linalg.norm(hvec(sol.x, mdl)) < 1e-10:
            x = np.mod(sol.x, 2 * np.pi)
            if all(np.linalg.norm(np.angle(np.exp(1j * (x - y)))) > 1e-6 for y in nodes):
                nodes.append(x)
    return nodes


def solid_angle_degree(mdl, k0, r=1e-3, nt=24, npp=48):
    """degree of n = h/|h| on a small sphere around k0 (signed solid angle / 4 pi)."""
    th = np.linspace(0, np.pi, nt + 1)
    ph = np.linspace(0, 2 * np.pi, npp + 1)
    P = np.zeros((nt + 1, npp + 1, 3))
    for i, t in enumerate(th):
        for j, p in enumerate(ph):
            k = k0 + r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
            v = hvec(k, mdl)
            P[i, j] = v / np.linalg.norm(v)

    def tri(a, b, c):
        num = np.dot(a, np.cross(b, c))
        den = 1 + np.dot(a, b) + np.dot(b, c) + np.dot(c, a)
        return 2 * np.arctan2(num, den)

    tot = 0.0
    for i in range(nt):
        for j in range(npp):
            a, b, c, e = P[i, j], P[i + 1, j], P[i + 1, j + 1], P[i, j + 1]
            tot += tri(a, b, c) + tri(a, c, e)
    return tot / (4 * np.pi)


# B2/C: d = 3 complex: isolated cones
d3 = []
for s in range(40):
    mdl = make_model(3, 3, RNG)
    nodes = find_nodes(3, mdl, 22)
    if len(nodes) >= 2:
        d3.append((mdl, nodes))
    if len(d3) >= 4:
        break
ok_iso, chir_ok, nn_ok, robust = True, True, True, True
summary = []
for mdl, nodes in d3:
    signs = []
    for k0 in nodes:
        J = jac(k0, mdl)
        sv = np.linalg.svd(J, compute_uv=False)
        ok_iso &= sv[-1] > 1e-3
        sgn = int(np.sign(np.linalg.det(J)))
        deg = solid_angle_degree(mdl, k0)
        chir_ok &= abs(deg - sgn) < 1e-6
        signs.append(sgn)
    nn_ok &= sum(signs) == 0
    pert = tuple(x + 1e-2 * RNG.normal(size=x.shape) for x in mdl)
    robust &= len(find_nodes(3, pert, 22)) == len(nodes)
    summary.append("%d nodes, charges %s" % (len(nodes), "".join("+" if q > 0 else "-" for q in signs)))
check("B2 d=3 complex: nodes are isolated cones (det J != 0) in 4 random models", ok_iso and len(d3) == 4,
      "; ".join(summary))
check("B3 d=3 nodes survive a random 1e-2 change of every hop (no symmetry used)", robust)

# B4: d = 4 complex: nodal lines, flat direction at every node
mdl4 = make_model(4, 3, RNG)
slices, kerflat, ntrack = 0, [], 0
for k4 in np.linspace(0, 2 * np.pi, 12, endpoint=False):
    sub = (mdl4[0][:3], mdl4[1][:3], mdl4[2] + np.cos(k4) * mdl4[0][3] + np.sin(k4) * mdl4[1][3])
    nd = find_nodes(3, sub, 16, nseed=60)
    if nd:
        slices += 1
        k0 = np.concatenate([nd[0], [k4]])
        J = jac(k0, mdl4)
        _, s, vt = np.linalg.svd(J)
        v = vt[-1]
        t = 1e-4
        flat = np.linalg.norm(hvec(k0 + t * v, mdl4)) / t
        side = min(np.linalg.norm(hvec(k0 + t * w, mdl4)) / t for w in vt[:3])
        kerflat.append((flat, side))
        # track the node 0.01 along k4: Newton at fixed k4' from the old node
        sub2 = (mdl4[0][:3], mdl4[1][:3], mdl4[2] + np.cos(k4 + 1e-3) * mdl4[0][3] + np.sin(k4 + 1e-3) * mdl4[1][3])
        sol = optimize.root(lambda k: hvec(k, sub2), nd[0], jac=lambda k: jac(k, sub2), method="hybr")
        ntrack += int(sol.success and np.linalg.norm(hvec(sol.x, sub2)) < 1e-10)
check("B4 d=4 complex: zero set is a line (node continues as k4 moves, dk4=1e-3), with a flat direction",
      slices >= 2 and ntrack == slices and max(f / sd for f, sd in kerflat) < 0.02,
      "%d/12 k4-slices hold nodes, %d tracked over dk4=1e-3; max (kernel/transverse) splitting slope %.1e at t=1e-4"
      % (slices, ntrack, max(f / sd for f, sd in kerflat)))

# B5: real class in d = 2 has generic point nodes; a small complex hop gaps them (linear in eps)
real_nodes = None
for s in range(60):
    a = RNG.normal(size=(2, 2)); b = RNG.normal(size=(2, 2)); c = 0.3 * RNG.normal(size=2)
    mr = (a, b, c)
    nd = find_nodes(2, mr, 48, nseed=80)
    if nd:
        real_nodes = (mr, nd)
        break
mr, nd = real_nodes
ay = RNG.normal(size=2); by = RNG.normal(size=2); cy = RNG.normal()
gl = []
for eps in (1e-2, 1e-3):
    mc = (np.column_stack([mr[0], eps * ay]), np.column_stack([mr[1], eps * by]), np.append(mr[2], eps * cy))
    gl.append(min_gap(2, mc, 96))
check("B5 d=2 real (rebit) class: point nodes exist; a complex hop eps opens a gap ~ eps",
      len(nd) >= 1 and gl[0] > 1e-5 and 5 < gl[0] / gl[1] < 20,
      "%d real nodes; gap(1e-2)/gap(1e-3) = %.2f" % (len(nd), gl[0] / gl[1]))

# B6: quaternionic class (5 anticommuting 4x4 Gammas): isolated nodes need d = 5
G5 = clifford_gens(2) + [kron_all([SZ, SZ])]
anti = all(np.allclose(G5[i] @ G5[j] + G5[j] @ G5[i], 2 * (i == j) * np.eye(4)) for i in range(5) for j in range(5))
mdl5 = make_model(5, 5, RNG, cscale=0.2)
n5 = find_nodes(5, mdl5, 7, nseed=120)
iso5 = all(np.linalg.svd(jac(k, mdl5), compute_uv=False)[-1] > 1e-3 for k in n5)
Hn = sum(hvec(n5[0], mdl5)[a] * G5[a] for a in range(5)) if n5 else None
k1 = n5[0] + 1e-3 * RNG.normal(size=5) if n5 else None
ev = np.linalg.eigvalsh(sum(hvec(k1, mdl5)[a] * G5[a] for a in range(5))) if n5 else None
check("B6 d=5 quaternionic class: Kramers-pair bands, nodes isolated with det J != 0",
      anti and len(n5) >= 1 and iso5 and np.allclose(ev[0], ev[1]) and np.allclose(ev[2], ev[3]),
      "%d nodes found" % len(n5))

# ------------------------------------------------------------------ C
print("== C: at a d=3 cone, space rotations act as qubit rotations ==")
check("C1 chirality of each cone = sign det J = solid-angle degree (exactly +-1)", chir_ok)
check("C2 charges sum to zero in every model (Nielsen-Ninomiya mirrors are forced)", nn_ok)
mdl, nodes = d3[0]
J = jac(nodes[0], mdl)  # h ~ J q,  q = k - k0
Q, _ = np.linalg.qr(RNG.normal(size=(3, 3)))
Q *= np.sign(np.linalg.det(Q))  # random SO(3) of the Bloch vector
R = np.linalg.solve(J, Q @ J)   # induced linear map of momentum q -> R q
g = np.linalg.inv(J.T @ J)      # emergent metric on momentum (inverse)
# SU(2) lift of Q
w, V = np.linalg.eig(Q)
iax = np.argmin(abs(w - 1)); ax = np.real(V[:, iax]); ax /= np.linalg.norm(ax)
ang = np.angle(w[(iax + 1) % 3])
cand = []
for sgn in (1, -1):
    th = sgn * abs(ang)
    U = np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * (ax[0] * SX + ax[1] * SY + ax[2] * SZ)
    cand.append(U)
errs = []
for U in cand:
    e = 0
    for _ in range(5):
        q = RNG.normal(size=3)
        hq = J @ q; hr = J @ (R @ q)
        Hq = hq[0] * SX + hq[1] * SY + hq[2] * SZ
        Hr = hr[0] * SX + hr[1] * SY + hr[2] * SZ
        e = max(e, np.abs(U @ Hq @ U.conj().T - Hr).max())
    errs.append(e)
iso = np.abs(R.T @ J.T @ J @ R - J.T @ J).max()
check("C3 every Bloch rotation is a momentum rotation for metric J^T J, realised by an SU(2) lift",
      min(errs) < 1e-10 and iso < 1e-10, "lift err %.1e, metric err %.1e" % (min(errs), iso))

# ------------------------------------------------------------------ D
print("== D: clause checks for candidate (a) ==")
res = []
for D in range(2, 8):
    n = D // 2
    gens = clifford_gens(n)
    if D % 2 == 1:
        gens = gens + [kron_all([SZ] * n)]  # odd D: product adjoined
    gens = gens[:D]
    w = np.eye(gens[0].shape[0], dtype=complex)
    for G in gens:
        w = w @ G
    anti_all = all(np.allclose(w @ G + G @ w, 0) for G in gens)
    comm_all = all(np.allclose(w @ G - G @ w, 0) for G in gens)
    res.append((D, anti_all, comm_all))
ok = all((a and not c) if D % 2 == 0 else (c and not a) for D, a, c in res)
check("D1 Clifford volume element grades (chirality exists) iff D = d+1 even, i.e. d odd (D=2..7)", ok)
tab = [(d, d - 1, (d + 1) * (d - 2) // 2) for d in range(1, 6)]
check("D2 propagating photon (d-1) / graviton ((d+1)(d-2)/2) polarisations: both > 0 first at d = 3",
      [t for t in tab if t[1] > 0 and t[2] > 0][0][0] == 3, " ".join("d%d:%d/%d" % t for t in tab))
check("D3 d=1 is NOT excluded by gauge anomaly: 3-4-5-0 has 3^2+4^2-5^2-0^2 = 0",
      3 ** 2 + 4 ** 2 - 5 ** 2 - 0 == 0)

# ------------------------------------------------------------------ E
print("== E: candidate (c) recurrence and binding ==")
u3 = integrate.quad(lambda t: special.i0e(t / 3.0) ** 3, 0, np.inf, limit=400)[0]
P3 = 1 - 1 / u3
part = {d: [integrate.quad(lambda t: special.i0e(t / d) ** d, 0, T, limit=400)[0] for T in (1e3, 1e5)] for d in (1, 2)}
check("E1 Polya: u(3) = 1.516386, return prob 0.3405 (transient); d = 1, 2 Green integral diverges",
      abs(u3 - 1.516386) < 1e-5 and abs(P3 - 0.340537) < 1e-5 and part[1][1] > 5 * part[1][0] and part[2][1] - part[2][0] > 1.3,
      "u3=%.6f P=%.4f; d1 %.0f->%.0f, d2 %.2f->%.2f" % (u3, P3, part[1][0], part[1][1], part[2][0], part[2][1]))


def radial_E0(d, alpha, a, Rmax=40.0, N=4000):
    h = Rmax / N
    r = h * np.arange(1, N)
    V = (d - 1) * (d - 3) / 4.0 / r ** 2 - alpha / np.maximum(r, a) ** (d - 2)
    diag = 2 / h ** 2 + V
    off = -np.ones(N - 2) / h ** 2
    return eigh_tridiagonal(diag, off, select="i", select_range=(0, 0))[0][0]


cuts = (0.4, 0.2, 0.1, 0.05)
E3 = [radial_E0(3, 1.0, a) for a in cuts]
E5 = [radial_E0(5, 1.0, a) for a in cuts]
E4w = [radial_E0(4, 0.5, a) for a in cuts]
E4s = [radial_E0(4, 2.0, a) for a in cuts]
check("E2 d=3 Coulomb: E0 -> -alpha^2/4 as cutoff -> 0 (stable for any alpha)", abs(E3[-1] + 0.25) < 0.01,
      " ".join("%.3f" % e for e in E3))
check("E3 d=5: E0 runs away as cutoff -> 0 (no stable atom)", E5[-1] < 4 * E5[-2] < 0,
      " ".join("%.1f" % e for e in E5))
check("E4 d=4 scale-free: alpha=0.5 no bound state (E0>=0); alpha=2 collapses ~ -1/a^2",
      min(E4w) >= 0 and 3 < E4s[-1] / E4s[-2] < 5, "alpha=0.5: min E0 %.4f; alpha=2, a=.4..05: %s" % (min(E4w), " ".join("%.0f" % e for e in E4s)))

# ------------------------------------------------------------------ F
print("== F: candidate (d) 2^d cell Clifford counting ==")
irr = True
for d in (1, 3, 5):
    gens = clifford_gens(d)  # 2d anticommuting on C^(2^d)
    prods = []
    for mask in itertools.product((0, 1), repeat=2 * d):
        M = np.eye(2 ** d, dtype=complex)
        for bit, G in zip(mask, gens):
            if bit:
                M = M @ G
        prods.append(M.ravel())
    irr &= np.linalg.matrix_rank(np.array(prods)) == 4 ** d
check("F1 the 2^d corner space carries Cl(2d) irreducibly (d = 1, 3, 5)", irr)
wcount = {}
for d in (1, 3, 5, 7, 9):
    gens = clifford_gens(d)[:d]
    w = np.eye(2 ** d, dtype=complex)
    for G in gens:
        w = w @ G
    w = w * (1j ** (-(d * (d - 1) // 2) % 4))  # make w Hermitian with w^2 = 1
    ev = np.linalg.eigvalsh((w + w.conj().T) / 2)
    nplus = int(np.sum(ev > 0.5))
    wcount[d] = nplus // 2 ** ((d - 1) // 2)
check("F2 one mode per site: Weyl species per chirality = 2^((d-1)/2); reaches 16 only at d = 9",
      wcount == {1: 1, 3: 2, 5: 4, 7: 8, 9: 16}, str(wcount))
L = 8
n = L ** 3
idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
H = np.zeros((n, n), complex)
for x, y, z in itertools.product(range(L), repeat=3):
    i = idx(x, y, z)
    for mu, (dx, dy, dz), eta in ((0, (1, 0, 0), 1), (1, (0, 1, 0), (-1) ** x), (2, (0, 0, 1), (-1) ** (x + y))):
        j = idx(x + dx, y + dy, z + dz)
        H[i, j] += 0.5j * eta
        H[j, i] += -0.5j * eta
ev = np.linalg.eigvalsh(H)
p = 2 * np.pi * np.arange(L) / L
target = np.sort(np.array([np.sin(a) ** 2 + np.sin(b) ** 2 + np.sin(c) ** 2 for a in p for b in p for c in p]))
nzero = int(np.sum(abs(ev) < 1e-9))
check("F3 staggered Z^3 (one mode/site): H^2 spectrum = sum sin^2 p, 8 zero modes = 2 Weyl per chirality",
      np.allclose(np.sort(ev ** 2), target, atol=1e-9) and nzero == 8, "zero modes %d" % nzero)

print("elapsed %.1f s" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
