AUDIT_INPUT_PATHS = ('docs/QUBIT_CELL_COMPLEX_EMERGENT_GAUGE_FIELDS_SELECT_NO_MATTER_MULTIPLET_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Emergent gauge fields and matter from qubit sites: a composite-route scouting runner.

A. The rung-2 cell complex of Z^3: sites with 0,1,2,3 odd coordinates are the
   vertices, edges, faces and cubes of the coarse lattice 2Z^3. A toric-code rule
   built from nearest-neighbour stars of fine sites gives an emergent Z2 gauge
   theory with bosonic point charges and flux loops.
B. Bravyi-Kitaev superfast (BKSF) twist on the same edge sites: fermionic charges,
   but the rule needs an ordering of directions (lopsided) and range > 1.
C. Spin-1/2 ice on the edge sites (Gauss law at vertex sites, ring flips at face
   sites): exact Gauss invariance; RK-point (equal-weight) ice sampling shows
   Coulomb-type dipolar correlations; the Gaussian reading has 2 gapless modes.
D. Emergent fermions hop locally on Z^3: Weyl charges sum to zero (doubling).
E. Which protected, anomaly-free multiplets can emergent fermions form (fermion
   parity is gauged because fermions are string ends)? Table + exact checks.
Supplied/cited items are listed at the end. Seeded; dense matrices <= 32x32.
"""
import time
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = 0
NF = 0


def check(tag, ok, msg, detail=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}" + (f" | {detail}" if detail else ""))


# ---------------------------------------------------------------- GF(2) Paulis
def comm(p, q):
    """Pauli (x,z) bitmask pairs commute? returns True if commute."""
    return bin((p[0] & q[1]) ^ (p[1] & q[0])).count("1") % 2 == 0


def gf2_rank(vecs):
    basis = {}
    r = 0
    for v in vecs:
        while v:
            h = v.bit_length() - 1
            if h in basis:
                v ^= basis[h]
            else:
                basis[h] = v
                r += 1
                break
    return r


def pack(p, n):
    return p[0] | (p[1] << n)


# ------------------------------------------------------------ A. cell complex
print("== A. rung-2 cell complex of Z^3 and the nearest-neighbour toric-code rule")
blk = list(itertools.product((0, 1), repeat=3))
cls = [sum(c) for c in blk]
counts = [cls.count(k) for k in range(4)]
check("A1 [T]", counts == [1, 3, 3, 1],
      "a 2^3 block of qubit sites splits by number of odd coordinates into 1 vertex, "
      "3 edge, 3 face, 1 cube site: one qubit per site hosts a full cell complex at rung 2",
      f"counts {counts}")


def edges_index(L):
    idx = {}
    for v in itertools.product(range(L), repeat=3):
        for a in range(3):
            idx[(v, a)] = len(idx)
    return idx


def add(v, a, s, L):
    w = list(v)
    w[a] = (w[a] + s) % L
    return tuple(w)


def fine_pos(v, a):
    p = [2 * c for c in v]
    p[a] += 1
    return tuple(p)


def toric(L):
    idx = edges_index(L)
    n = len(idx)
    stars, plaqs, star_fine, plaq_fine = [], [], [], []
    for v in itertools.product(range(L), repeat=3):
        x = 0
        sup = []
        for a in range(3):
            for e in ((v, a), (add(v, a, -1, L), a)):
                x |= 1 << idx[e]
                sup.append(fine_pos(*e))
        stars.append((x, 0))
        star_fine.append((tuple(2 * c for c in v), sup))
        for a, b in ((0, 1), (1, 2), (0, 2)):
            z = 0
            sup = []
            for e in ((v, a), (add(v, a, 1, L), b), (add(v, b, 1, L), a), (v, b)):
                z |= 1 << idx[e]
                sup.append(fine_pos(*e))
            plaqs.append((0, z))
            c = [2 * q for q in v]
            c[a] += 1
            c[b] += 1
            plaq_fine.append((tuple(c), sup))
    return idx, n, stars, plaqs, star_fine, plaq_fine


def fdist(p, q, M):
    return sum(min(abs(a - b) % M, M - abs(a - b) % M) for a, b in zip(p, q))


ks = {}
nn_ok = True
comm_ok = True
for L in (3, 4):
    idx, n, stars, plaqs, sf, pf = toric(L)
    M = 2 * L
    for c, sup in sf + pf:
        nn_ok &= all(fdist(c, s, M) == 1 for s in sup) and len(set(sup)) == len(sup)
    if L == 3:
        for s in stars:
            comm_ok &= all(comm(s, p) for p in plaqs)
    ks[L] = n - gf2_rank([pack(g, n) for g in stars + plaqs])
check("A2 [T]", nn_ok and comm_ok,
      "star = X on the 6 nearest neighbours of a vertex site, plaquette = Z on the 4 edge-site "
      "nearest neighbours of a face site; all terms commute (no gauge group written in)",
      f"supports all at fine distance 1: {nn_ok}; commute: {comm_ok}")
check("A3 [T]", ks == {3: 3, 4: 3},
      "torus code dimension log2 = 3 = b1(T^3) at coarse L = 3, 4: topological (deconfined Z2) order",
      f"log2 dim {ks}")
idx, n, stars, plaqs, sf, pf = toric(3)
e0 = idx[((0, 0, 0), 0)]
zst = (0, 1 << e0)
xst = (1 << e0, 0)
nflipS = sum(not comm(zst, s) for s in stars)
nflipP = sum(not comm(xst, p) for p in plaqs)
zops = [(0, 1 << idx[((0, 0, 0), a)]) for a in range(3)]
tj = 1
for i, j in ((0, 1), (0, 2), (1, 2)):
    tj *= 1 if comm(zops[i], zops[j]) else -1
check("A4 [T]", nflipS == 2 and nflipP == 4 and tj == 1,
      "Z on an edge site makes a pair of point charges, X makes a flux loop through 4 face sites; "
      "the charge hops commute, Levin-Wen T-junction +1: the emergent charge is a BOSON",
      f"stars flipped {nflipS}, plaquettes flipped {nflipP}, T-junction {tj:+d}")

# ------------------------------------------------------------- B. BKSF twist
print("== B. BKSF twist on the same edge sites: fermionic charges, at a price")
DIRS = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]


def bksf(L, order):
    idx = edges_index(L)
    n = len(idx)
    rank = {d: order.index(d) for d in DIRS}

    def inc(j):  # incident edges at j by direction
        out = {}
        for a in range(3):
            out[(a, 1)] = (j, a)
            out[(a, -1)] = (add(j, a, -1, L), a)
        return out
    A = {}
    for (v, a), i in idx.items():
        k = add(v, a, 1, L)
        x = 1 << i
        z = 0
        for j, dj in ((v, (a, 1)), (k, (a, -1))):
            for d, e in inc(j).items():
                if rank[d] < rank[dj]:
                    z ^= 1 << idx[e]
        A[(v, a)] = (x, z)
    B = {}
    for j in itertools.product(range(L), repeat=3):
        z = 0
        for e in inc(j).values():
            z |= 1 << idx[e]
        B[j] = (0, z)
    S = []
    for v in itertools.product(range(L), repeat=3):
        for a, b in ((0, 1), (1, 2), (0, 2)):
            x = z = 0
            for e in ((v, a), (add(v, a, 1, L), b), (add(v, b, 1, L), a), (v, b)):
                x ^= A[e][0]
                z ^= A[e][1]
            S.append((x, z))
    return idx, n, A, B, S


order = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]
L = 4
idx, n, A, B, S = bksf(L, order)
keys = list(A)
alg_ok = True
for i in range(len(keys)):
    vi = {keys[i][0], add(keys[i][0], keys[i][1], 1, L)}
    for j in range(i + 1, len(keys)):
        vj = {keys[j][0], add(keys[j][0], keys[j][1], 1, L)}
        share = len(vi & vj) > 0
        if comm(A[keys[i]], A[keys[j]]) == share:
            alg_ok = False
bv_ok = all((not comm(B[j], A[e])) == (j in (e[0], add(e[0], e[1], 1, L))) for j in B for e in keys[:40])
s_ok = all(comm(s, A[e]) for s in S for e in keys) and all(comm(s, b) for s in S for b in B.values())
kb = n - gf2_rank([pack(g, n) for g in list(B.values()) + S])
check("B1 [T]", alg_ok and bv_ok and s_ok,
      "edge operators A_e anticommute iff they share a vertex (the fermion-hopping algebra), B_v "
      "flips only at endpoints, loop products S_p commute with every A_e and B_v",
      f"L={L}, edges {n}, log2 dim of <B,S> (GF(2)) {kb}")
e3 = [((0, 0, 0), a) for a in range(3)]
tjB = 1
for i, j in ((0, 1), (0, 2), (1, 2)):
    tjB *= 1 if comm(A[e3[i]], A[e3[j]]) else -1


def supp_fine(p, idx):
    inv = {i: e for e, i in idx.items()}
    m = p[0] | p[1]
    return [fine_pos(*inv[i]) for i in range(len(inv)) if m >> i & 1]


M = 2 * L
dA = max(max(fdist(p, q, M) for p in sp for q in sp) for sp in (supp_fine(A[e], idx) for e in keys[:12]))
dS = max(max(fdist(p, q, M) for p in sp for q in sp) for sp in (supp_fine(s, idx) for s in S[:12]))
check("B2 [T]", tjB == -1 and dA > 2,
      "T-junction -1: the point charge is a FERMION (cf. main BKSF note); but the fermion rule's terms "
      "are not nearest-neighbour stars (fine-lattice diameter > 2) and need a direction ordering",
      f"T-junction {tjB:+d}; support diameters A_e {dA}, S_p {dS} (toric stars: 2)")


def rotations():
    R = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            Mx = np.zeros((3, 3), int)
            for i in range(3):
                Mx[perm[i], i] = sg[i]
            if round(np.linalg.det(Mx)) == 1:
                R.append(Mx)
    return R


def rot_edge(e, Rm, L):
    v, a = e
    vv = tuple(int(c) % L for c in Rm @ np.array(v))
    d = Rm[:, a]
    b = int(np.nonzero(d)[0][0])
    if d[b] == 1:
        return (vv, b)
    return (add(vv, b, -1, L), b)


def rot_pauli(p, Rm, idx, L):
    inv = {i: e for e, i in idx.items()}
    x = z = 0
    for i in range(len(inv)):
        ne = idx[rot_edge(inv[i], Rm, L)]
        if p[0] >> i & 1:
            x |= 1 << ne
        if p[1] >> i & 1:
            z |= 1 << ne
    return (x, z)


def n_invariant(gens, idx, L, n):
    base = [pack(g, n) for g in gens]
    r0 = gf2_rank(base)
    cnt = 0
    for Rm in rotations():
        rot = [pack(rot_pauli(g, Rm, idx, L), n) for g in gens]
        cnt += gf2_rank(base + rot) == r0
    return cnt


Lr = 3
idx3, n3, st3, pl3, _, _ = toric(Lr)
ninvT = n_invariant(st3 + pl3, idx3, Lr, n3)
idxb, nb, Ab, Bb, Sb = bksf(Lr, order)
ninvB = n_invariant(list(Bb.values()) + Sb, idxb, Lr, nb)
check("B3 [T]", ninvT == 24 and ninvB < 24,
      "the toric rule is invariant under all 24 cube rotations; the BKSF fermion rule is not "
      "(a lopsided choice; main: no BKSF code is O-invariant, a covariant fermion code needs 3 qubits per site)",
      f"rotations preserving the code: toric {ninvT}/24, BKSF {ninvB}/24 (coarse L={Lr})")

# --------------------------------------------------------------- C. U(1) ice
print("== C. spin-1/2 ice on edge sites: emergent U(1) (Gauss at vertex sites, ring at face sites)")
L = 6
E = np.empty((3, L, L, L), int)
X, Y, Z = np.meshgrid(range(L), range(L), range(L), indexing="ij")
E[0] = (-1) ** (Y + Z)
E[1] = (-1) ** (X + Z)
E[2] = (-1) ** (X + Y)


def div(E):
    return sum(E[a] - np.roll(E[a], 1, axis=a) for a in range(3))


d0 = np.abs(div(E)).max()
planes = [(0, 1), (1, 2), (0, 2)]
qs = {"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1), "xy": (1, 1, 0)}
ph = {k: np.exp(-2j * np.pi * (q[0] * X + q[1] * Y + q[2] * Z) / L) for k, q in qs.items()}
acc = {k: 0.0 for k in qs}
nsamp = 0
nflip = 0
burn, total, every = 60000, 360000, 1500
r = RNG.integers(0, L, size=(total, 3))
pp = RNG.integers(0, 3, size=total)
for t in range(total):
    a, b = planes[pp[t]]
    v = tuple(r[t])
    va = list(v); va[a] = (va[a] + 1) % L; va = tuple(va)
    vb = list(v); vb[b] = (vb[b] + 1) % L; vb = tuple(vb)
    s = E[a][v]
    if E[b][va] == s and E[a][vb] == -s and E[b][v] == -s:
        E[a][v] = -s; E[b][va] = -s; E[a][vb] = s; E[b][v] = s
        nflip += 1
    if t >= burn and t % every == 0:
        for k in qs:
            acc[k] += abs((E[0] * ph[k]).sum()) ** 2 / L ** 3
        nsamp += 1
d1 = np.abs(div(E)).max()
S = {k: acc[k] / nsamp for k in qs}
check("C1 [T]", d0 == 0 and d1 == 0 and nflip > 1000,
      "ring flips at face sites keep every vertex-site divergence (Gauss law) exactly; the ice "
      "manifold is a U(1) constraint built from one qubit per edge site",
      f"max |div| before {d0}, after {nflip} flips {d1}")
ratio = S["xy"] / S["y"]
check("C2 [D]", S["x"] < 1e-9 and S["y"] > 0.2 and abs(S["y"] / S["z"] - 1) < 0.3 and abs(ratio - 0.5) < 0.15,
      "RK-point (equal-weight ice) correlations of E_x: zero for q along x (exact, divergence-free), finite "
      "transverse, and S(1,1,0)/S(0,1,0) near the transverse projector value 1/2: Coulomb (dipolar) form",
      f"S_xx(q) x:{S['x']:.1e} y:{S['y']:.3f} z:{S['z']:.3f} xy:{S['xy']:.3f}; ratio {ratio:.3f}; samples {nsamp}")
ok = True
lam = []
for k in [(0.3, 0.1, 0.0), (1.0, 0.5, 0.2), (np.pi, 0.4, 2.0), (0.05, 0.05, 0.05)]:
    dlt = np.array([1 - np.exp(1j * c) for c in k])
    C = np.array([[0, -dlt[2], dlt[1]], [dlt[2], 0, -dlt[0]], [-dlt[1], dlt[0], 0]])
    w = np.sort(np.linalg.eigvalsh(C.conj().T @ C))
    lt = sum(4 * np.sin(c / 2) ** 2 for c in k)
    ok &= abs(w[0]) < 1e-12 and abs(w[1] - lt) < 1e-12 and abs(w[2] - lt) < 1e-12
    lam.append(np.sqrt(lt) / np.linalg.norm(k))
check("C3 [T]", ok and abs(lam[-1] - 1) < 1e-3,
      "Gaussian (Coulomb-phase) reading H = U/2 E^2 + K/2 (curl A)^2: per k one pure-gauge zero and TWO "
      "transverse modes, omega^2 = UK sum 4 sin^2(k/2) -> linear: 2 photon polarisations",
      f"omega/(sqrt(UK)|k|) at small k {lam[-1]:.5f}")

# --------------------------------------------------------------- D. doubling
print("== D. emergent fermions hop locally on Z^3: Weyl charges cancel (Nielsen-Ninomiya)")
cf = RNG.normal(0, 0.15, size=(3, 7))


def dvec(kx, ky, kz):
    b = [np.ones_like(kx), np.cos(kx), np.cos(ky), np.cos(kz), np.sin(kx), np.sin(ky), np.sin(kz)]
    pert = [sum(cf[i, j] * b[j] for j in range(7)) for i in range(3)]
    return (np.sin(kx) + pert[0], np.sin(ky) + pert[1], 2 - np.cos(kx) - np.cos(ky) - np.cos(kz) + pert[2])


def chern(kz, N=24):
    g = np.linspace(-np.pi, np.pi, N, endpoint=False)
    KX, KY = np.meshgrid(g, g, indexing="ij")
    d1, d2, d3 = dvec(KX, KY, np.full_like(KX, kz))
    H = np.zeros((N, N, 2, 2), complex)
    H[..., 0, 0] = d3; H[..., 1, 1] = -d3
    H[..., 0, 1] = d1 - 1j * d2; H[..., 1, 0] = d1 + 1j * d2
    _, V = np.linalg.eigh(H)
    u = V[..., :, 0]
    def lk(a, b):
        z = (a.conj() * b).sum(-1)
        return z / abs(z)
    u1 = np.roll(u, -1, 0); u2 = np.roll(u, -1, 1); u12 = np.roll(u1, -1, 1)
    F = np.angle(lk(u, u1) * lk(u1, u12) * lk(u12, u2) * lk(u2, u))
    return int(round(F.sum() / (2 * np.pi)))


kzs = -np.pi + (np.arange(40) + 0.5) * 2 * np.pi / 40
Cs = [chern(k) for k in kzs]
jumps = [Cs[(i + 1) % 40] - Cs[i] for i in range(40)]
check("D1 [T]", any(c != 0 for c in Cs) and sum(jumps) == 0 and sum(abs(j) for j in jumps) >= 2,
      "a seeded random local two-band hop on Z^3 has Weyl nodes (slice Chern number jumps) whose "
      "charges sum to zero: emergent lattice fermions with a local hop come in L/R pairs",
      f"C(kz) values {sorted(set(Cs))}, node charges {[j for j in jumps if j]}")

# ------------------------------------------------------ E. multiplet selection
print("== E. which protected anomaly-free multiplets can emergent fermions form?")
zn = [m for m in range(2, 13, 2) if (2 * 1) % m != 0]
check("E1 [T]", zn[0] == 4,
      "emergent fermions are string ends, so fermion parity is an element of the emergent gauge group; "
      "the smallest cyclic group forbidding every Majorana mass of odd-charge Weyl fermions is Z4",
      f"Z_n (n even, charge 1) forbidding psi psi: {zn[:3]}...")


def spinj(j):
    m = np.arange(j, -j - 1, -1)
    d = len(m)
    Jp = np.zeros((d, d))
    for i in range(1, d):
        Jp[i - 1, i] = np.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
    return [(Jp + Jp.T) / 2, (Jp - Jp.T) / 2j, np.diag(m)]


def inv_forms(gens):
    d = gens[0].shape[0]
    I = np.eye(d)
    Mx = np.vstack([np.kron(T.T, I) + np.kron(I, T.T) for T in gens])
    w, V = np.linalg.eigh(Mx.conj().T @ Mx)
    null = V[:, w < 1e-9].T
    out = []
    for v in null:
        Bm = v.reshape(d, d)
        out.append("S" if np.allclose(Bm, Bm.T, atol=1e-8) else ("A" if np.allclose(Bm, -Bm.T, atol=1e-8) else "?"))
    return out


rows = []
okE2 = True
for twoj in range(1, 16, 2):
    j = twoj / 2
    forms = inv_forms(spinj(j))
    prot = "S" not in forms
    witten = round(2 * j * (j + 1) * (2 * j + 1) / 3) % 2 == 1
    new = (twoj - 3) % 8 == 0
    okE2 &= prot
    rows.append((twoj, int(2 * j + 1), witten, new))
surv = [r for r in rows if not r[2] and not r[3]]
check("E2 [T+C]", okE2 and surv[0][0] == 7,
      "SU(2) spin j (half-integer): no symmetric invariant, so G alone forbids masses; Witten (j=2r+1/2) "
      "and the new SU(2) anomaly (j=4r+3/2, cited WWW, applies since fermion parity is the centre) remove "
      "j=1/2,3/2,5/2: the SMALLEST consistent protected irreducible multiplet is j=7/2, 8 Weyl, not 16",
      "2j:dim " + " ".join(f"{a}:{b}{'W' if w else ''}{'N' if nw else ''}" for a, b, w, nw in rows))

# Spin(10) 16 from 5 fermion modes (composite: 5 modes = 5 sites)
sz = np.diag([1.0, -1.0]); sm = np.array([[0, 1.0], [0, 0]]); I2 = np.eye(2)


def kronl(ms):
    out = np.ones((1, 1))
    for m in ms:
        out = np.kron(out, m)
    return out


a = [kronl([sz] * k + [sm] + [I2] * (4 - k)) for k in range(5)]
gam = []
for k in range(5):
    gam += [a[k] + a[k].T, 1j * (a[k] - a[k].T)]
Nop = sum(ak.T @ ak for ak in a)
ev = np.where(np.isclose(np.diag(Nop) % 2, 0))[0]
gens = [(-1j / 4 * (gam[p] @ gam[q] - gam[q] @ gam[p]))[np.ix_(ev, ev)] for p, q in itertools.combinations(range(10), 2)]
forms16 = inv_forms(gens)
dmax = 0.0
for _ in range(300):
    ta, tb, tc = (gens[i] for i in RNG.integers(0, 45, 3))
    dmax = max(dmax, abs(np.trace(ta @ (tb @ tc + tc @ tb))))
Q = (Nop - 2.5 * np.eye(32))[np.ix_(ev, ev)]
zc = np.diag(np.exp(1j * np.pi * np.diag(Q)))
cen = np.allclose(zc, zc[0, 0] * np.eye(16)) and abs(zc[0, 0] ** 2 + 1) < 1e-12
T16 = np.diag([1.0] * 15 + [-15.0])
check("E3 [T]", len(forms16) == 0 and dmax < 1e-10 and cen and abs(np.trace(T16 ** 3)) > 1,
      "Spin(10) 16 built from 5 modes (a 5-site cluster, composite): no invariant bilinear (masses forbidden), "
      "cubic anomaly 0, central element exp(i pi Q) acts as i on the 16 (the Z4); SU(16) fundamental is anomalous",
      f"invariant forms {len(forms16)}, max|d_abc| {dmax:.1e}, centre^2 = {zc[0,0]**2:.0f}, Tr T^3 SU(16) {np.trace(T16**3):.0f}")
check("E4 [C]", True,
      "cited classification: simple groups with a 16-dim irrep are SU(2) j=15/2 (pseudoreal), Sp(4) (pseudoreal), "
      "Spin(9) (real), SO(16) (real), Sp(16) (pseudoreal), SU(16) (complex, anomalous), Spin(10) (complex, "
      "anomaly-free): Spin(10) is the only complex anomaly-free one, but 'complex' and 'dim 16' are selector choices")
F = {"Q": (6, 1 / 3, 1 / 6), "u^c": (3, -1 / 3, -2 / 3), "d^c": (3, -1 / 3, 1 / 3), "L": (2, -1, -1 / 2),
     "e^c": (1, 1, 1), "nu^c": (1, 1, 0)}
Xc = {k: 5 * bl - 4 * y for k, (m, bl, y) in F.items()}
odd1 = all(abs(x - round(x)) < 1e-9 and round(x) % 4 == 1 for x in Xc.values())
nu16 = sum(m for k, (m, _, _) in F.items())
nu15 = nu16 - 1
y3 = sum(m * y ** 3 for k, (m, _, y) in F.items())
y1 = sum(m * y for k, (m, _, y) in F.items())
check("E5 [E+C]", odd1 and nu16 % 16 == 0 and nu15 % 16 != 0 and abs(y3) < 1e-12 and abs(y1) < 1e-12,
      "measured content: X = 5(B-L) - 4Y is 1 mod 4 on all 16 Weyl of a family incl. nu^c, so the measured "
      "family is a Z4-protected multiplet with nu = 16 = 0 mod 16 (Spin-Z4 bordism Z16, cited); without nu^c "
      "nu = 15 is anomalous: Z4 protection REQUIRES nu^c",
      f"X charges {dict((k, round(v)) for k, v in Xc.items())}; sum Y^3 {y3:.0e}, sum Y {y1:.0e}")

print(f"elapsed_seconds {time.time() - T0:.1f}")
print("supplied: the cell-complex role assignment, the star/plaquette/ice energy functions, the BKSF ordering, "
      "the RK equal-weight ensemble, the Gaussian reading, the random two-band hop; [E] uses measured charges.")
print("cited: Kitaev toric code; Bravyi-Kitaev 2002; Levin-Wen PRB 67 245316 (2003); Wen PRD 68 065003 (2003); "
      "Hermele-Balents-Fisher PRB 69 064404; Chandrasekharan-Wiese 1997; Nielsen-Ninomiya; Witten 1982; "
      "Wang-Wen-Witten 1810.00844; Garcia-Etxebarria-Montero 1808.00009; Wang-Wen 1809.11171; main BKSF and "
      "Majorana-per-direction notes (2026-10-17), spin-half cubic ice RK note (2026-09-03), SU(N) link 2N-state note.")
print(f"TOTAL: PASS={NP} FAIL={NF}")
