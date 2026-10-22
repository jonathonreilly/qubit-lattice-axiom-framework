AUDIT_INPUT_PATHS = ('docs/THE_CUBE_TICK_HAS_NO_LOCAL_CONSTANTS_OF_MOTION_SO_RUNG_TWO_GAUSS_LAWS_ARE_SUPPLIED_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Do the rung-2 star/plaquette (Gauss-law) functions follow from the update rule?

A. CL-1 flat cube tick (one fermion mode per site, two 2x2x2 tilings, face phase -1,
   mass angle mu, copy mass M): a Gaussian (free-fermion) unitary. Lemma: a
   Gaussian unitary has a local constant of motion on a region A (any degree)
   iff its one-mode map has an invariant subspace inside A. Brute-force check of
   the lemma on 5 modes, then the largest invariant subspace inside vertex stars,
   face plaquettes, cubes and boxes up to 6^3 on an 8^3 torus.
B. Symmetry: affine maps of Z^3 (mod 2) preserving the two tilings versus those
   preserving the rung-2 roles (number of odd coordinates).
C. Qubit Margolus rules (Ruleset A2 shape: one cube gate, two tilings): a rule
   that keeps every star and plaquette at every half-tick must act on the edge
   sites of each 2x2x2 cube by a fixed Pauli (GF(2) span of restrictions); the
   covariant image set freezes the whole cube; 4^3 blocks (zoom) free sites;
   random Clifford cube gates keep no star over a full tick (finite diagnostic).
D. What the tick does select: global on-site commutant = one U(1) (number).
Seeded; dense matrices <= 512 x 512; no Fock space above 2^5.
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


# ------------------------------------------------------------ A. CL-1 tick
L = 8
N = L ** 3


def idx(x, y, z):
    return (x % L) + L * (y % L) + L * L * (z % L)


def eta(i, x, y, z):
    # staggered phases: W_i anticommute <=> -1 around every unit face
    return [1, (-1) ** (x % 2), (-1) ** ((x + y) % 2)][i]


def cube_ops(c):
    """Sites of the cube with least corner c and its unit involutions R_1..R_3."""
    corners = list(itertools.product((0, 1), repeat=3))
    sites = [idx(c[0] + u[0], c[1] + u[1], c[2] + u[2]) for u in corners]
    Rs = []
    for i in range(3):
        W = np.zeros((8, 8))
        for a, u in enumerate(corners):
            if u[i] == 0:
                v = list(u); v[i] = 1
                b = corners.index(tuple(v))
                e = eta(i, c[0] + u[0], c[1] + u[1], c[2] + u[2])
                W[a, b] = W[b, a] = e
        Rs.append(W)
    return sites, Rs


def tick(eps, mu, MN):
    """One-mode map of a full CL-1 tick (copy gate, even, copy gate, odd)."""
    Ue = np.eye(N, dtype=complex); Uo = np.eye(N, dtype=complex); Cg = np.eye(N, dtype=complex)
    r2err = 0.0
    for par, (Ublk, sgn) in ((0, (Ue, -1)), (1, (Uo, +1))):
        for c in itertools.product(range(par, L, 2), repeat=3):
            s, Rs = cube_ops(c)
            R = sum(Rs) / np.sqrt(3)
            r2err = max(r2err, np.abs(R @ R - np.eye(8)).max())
            th = (eps - mu / 2) if par == 0 else (eps + mu / 2)
            blk = np.cos(th) * np.eye(8) + sgn * 1j * np.sin(th) * R
            ix = np.ix_(s, s)
            Ublk[ix] = blk
            if par == 0:
                sc = 1j * Rs[0] @ Rs[1] @ Rs[2] @ R
                G = (MN / 4) * (np.eye(8) - sc) @ R
                w, V = np.linalg.eigh((G + G.conj().T) / 2)
                Cg[ix] = V @ np.diag(np.exp(1j * w)) @ V.conj().T
    return Uo @ Cg @ Ue @ Cg, r2err


def inv_dim(U, A):
    """Dimension of the largest U-invariant subspace of C^A (A = site list)."""
    B = np.zeros((U.shape[0], len(A)), dtype=complex)
    B[A, np.arange(len(A))] = 1.0
    for _ in range(4 * len(A) + 4):
        k = B.shape[1]
        if k == 0:
            return 0
        X = U @ B
        Res = X - B @ (B.conj().T @ X)
        _, sv, Vh = np.linalg.svd(Res, full_matrices=True)
        sv = np.concatenate([sv, np.zeros(k - len(sv))]) if len(sv) < k else sv
        null = Vh[sv < 1e-9].conj().T
        if null.shape[1] == k:
            return k
        B = B @ null
    return B.shape[1]


# --- A0 lemma check by brute force on 5 modes (Jordan-Wigner, 32 x 32)
def jw(n):
    I2 = np.eye(2); Zp = np.diag([1.0, -1.0]); a = np.array([[0, 1], [0, 0.0]])
    cs = []
    for j in range(n):
        ops = [Zp] * j + [a] + [I2] * (n - j - 1)
        m = ops[0]
        for o in ops[1:]:
            m = np.kron(m, o)
        cs.append(m)
    return cs


def gaussian_U(h, cs):
    H = sum(h[i, j] * cs[i].conj().T @ cs[j] for i in range(len(cs)) for j in range(len(cs)))
    w, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(-1j * w)) @ V.conj().T


def local_commutant_dim(U, cs, A):
    maj = []
    for j in A:
        maj += [cs[j] + cs[j].conj().T, 1j * (cs[j] - cs[j].conj().T)]
    mons = []
    for r in range(len(maj) + 1):
        for comb in itertools.combinations(range(len(maj)), r):
            m = np.eye(cs[0].shape[0], dtype=complex)
            for q in comb:
                m = m @ maj[q]
            mons.append(m)
    K = np.array([(U @ m @ U.conj().T - m).ravel() for m in mons]).T
    sv = np.linalg.svd(K, compute_uv=False)
    return int(np.sum(sv < 1e-9 * max(1.0, sv.max())))


def planted_h(n, k):
    """Hermitian h with k eigenvectors spanning modes {0..k-1} exactly (k=0: generic)."""
    Q1 = np.linalg.qr(RNG.normal(size=(k, k)) + 1j * RNG.normal(size=(k, k)))[0] if k else None
    Q2 = np.linalg.qr(RNG.normal(size=(n - k, n - k)) + 1j * RNG.normal(size=(n - k, n - k)))[0]
    Q = np.zeros((n, n), dtype=complex)
    if k:
        Q[:k, :k] = Q1
    Q[k:, k:] = Q2
    # mix the complement with mode block {0..k-1} untouched? no: generic case k=0
    if k == 0:
        Q = np.linalg.qr(RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n)))[0]
    lam = RNG.uniform(0.3, 2.9, size=n)
    return Q @ np.diag(lam) @ Q.conj().T


cs5 = jw(5)
A2 = [0, 1]
pred = {0: 1, 1: 2, 2: 4}
got = {}
for k in (0, 1, 2):
    if k == 1:
        # one eigenvector on modes {0,1}, others generic
        v = np.array([0.6, 0.8j, 0, 0, 0])
        M = RNG.normal(size=(5, 5)) + 1j * RNG.normal(size=(5, 5))
        M[:, 0] = v
        Q = np.linalg.qr(M)[0]
        h = Q @ np.diag(RNG.uniform(0.3, 2.9, size=5)) @ Q.conj().T
    else:
        h = planted_h(5, k)
    got[k] = local_commutant_dim(gaussian_U(h, cs5), cs5, A2)
    u1 = np.linalg.eigh(h)
    U1 = u1[1] @ np.diag(np.exp(-1j * u1[0])) @ u1[1].conj().T
    got[(k, 'inv')] = inv_dim(U1, A2)
check("A0", all(got[k] == pred[k] for k in pred) and [got[(k, 'inv')] for k in pred] == [0, 1, 2],
      "lemma: local commutant on 2 of 5 modes = Lambda-fixed count of the invariant mode space",
      f"many-body dims {[got[k] for k in pred]} (pred 1,2,4); invariant one-mode dims {[got[(k,'inv')] for k in pred]}")

# --- A1 tick and its local constants of motion
regions = {}
o = 2  # a vertex site (all coordinates even)
regions["star"] = [idx(o, o, o)] + [idx(o + d[0], o + d[1], o + d[2]) for d in
                                    [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
f = (o + 1, o + 1, o)  # a face site
regions["plaq"] = [idx(*f)] + [idx(f[0] + d[0], f[1] + d[1], f[2]) for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
regions["star+4plaq"] = sorted(set(regions["star"]) | {idx(o + a, o + b, o + c) for a in (-1, 0, 1)
                                                       for b in (-1, 0, 1) for c in (-1, 0, 1)})
regions["box4"] = [idx(o + a, o + b, o + c) for a in range(4) for b in range(4) for c in range(4)]
regions["box6"] = [idx(a, b, c) for a in range(6) for b in range(6) for c in range(6)]

params = [("involution eps=pi/2", np.pi / 2, 0.0, 0.0), ("eps=0.3", 0.3, 0.0, 0.0),
          ("eps=0.3 mu=0.1", 0.3, 0.1, 0.0), ("eps=0.3 mu=0.1 MN=0.2", 0.3, 0.1, 0.2)]
e_r, m_r = RNG.uniform(0.1, 1.4), RNG.uniform(0.0, 0.5)
params.append((f"seeded eps={e_r:.3f} mu={m_r:.3f} MN=0.15", e_r, m_r, 0.15))
r2max = 0.0
for name, eps, mu, MN in params:
    U1, r2 = tick(eps, mu, MN)
    r2max = max(r2max, r2)
    un = np.abs(U1.conj().T @ U1 - np.eye(N)).max()
    dims = {k: inv_dim(U1, v) for k, v in regions.items()}
    nph = len(np.unique(np.round(np.angle(np.linalg.eigvals(U1)), 6)))
    check("A1", un < 1e-10 and all(d == 0 for d in dims.values()) and nph > 2,
          f"{name}: no local constant of motion on star, plaquette or boxes",
          f"inv dims {list(dims.values())}; distinct quasienergies {nph}")
check("A2", r2max < 1e-12, "every cube hop R is an involution (R^2 = 1, face phase -1)", f"max err {r2max:.1e}")

# --- A3 control: mu = 2 eps (even half-tick is the identity: flat bands)
U1, _ = tick(0.3, 0.6, 0.0)
dims = {k: inv_dim(U1, v) for k, v in regions.items()}
nph = len(np.unique(np.round(np.angle(np.linalg.eigvals(U1)), 6)))
check("A3", dims["box4"] == 8 and dims["box6"] == 64 and nph == 2,
      "control mu = 2 eps: even half-tick trivial, constants of motion live in single odd cubes",
      f"inv dims {list(dims.values())} (box4 holds 1 odd cube = 8, box6 holds 8 = 64); distinct quasienergies {nph}")

# --- A4 band formula (cited register band): cos w = A S - (cos 2b - cos mu)/2, S in [-1, 1]
eps, mu = 0.37, 0.11
U1, _ = tick(eps, mu, 0.0)
cw = np.cos(np.angle(np.linalg.eigvals(U1)))
b = np.pi / 2 - eps
A = (np.cos(2 * b) + np.cos(mu)) / 2
c0 = (np.cos(2 * b) - np.cos(mu)) / 2
check("A4", abs(cw.max() - (abs(A) - c0)) < 1e-9 and abs(cw.min() - (-abs(A) - c0)) < 1e-9,
      "quasienergy range matches |A| -/+ (cos2b-cos mu)/2: flat iff A = 0 iff cos mu = cos 2eps",
      f"max {cw.max():.6f} vs {abs(A)-c0:.6f}, min {cw.min():.6f} vs {-abs(A)-c0:.6f}")

# --- D. global on-site commutant: diagonal phases commuting with U1
U1, _ = tick(0.3, 0.1, 0.2)
rows = []
nz = np.argwhere(np.abs(U1) > 1e-12)
adj = {}
for i, j in nz:
    adj.setdefault(i, set()).add(j)
seen = {0}; stack = [0]
while stack:
    a = stack.pop()
    for bb in adj.get(a, ()):
        if bb not in seen:
            seen.add(bb); stack.append(bb)
Q = np.eye(N)  # number operator one-mode form
check("D1", len(seen) == N and np.abs(U1 @ Q - Q @ U1).max() < 1e-12,
      "on-site phase symmetries of the tick: one U(1) (support graph connected), number conserved",
      f"component size {len(seen)}/{N}")

# ------------------------------------------------------------ B. symmetry clash
corners = list(itertools.product((0, 1), repeat=3))


def role(x):
    return sum(v % 2 for v in x)


tiling_ok = 0; role_ok = 0; both = 0; both_strict = 0; proper_strict = 0
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        P = np.zeros((3, 3), int)
        for i in range(3):
            P[i, perm[i]] = sg[i]
        for t in corners:
            def g(x):
                return tuple(P @ np.array(x) + np.array(t))
            imgs = [g(u) for u in corners]
            lc = tuple(min(v[i] for v in imgs) for i in range(3))
            par = [v % 2 for v in lc]
            t_ok = par in ([0, 0, 0], [1, 1, 1])
            pts = list(itertools.product(range(2), repeat=3))
            r_strict = all(role(g(x)) == role(x) for x in pts)
            r_dual = all(role(g(x)) == 3 - role(x) for x in pts)
            tiling_ok += t_ok
            role_ok += (r_strict or r_dual)
            both += t_ok and (r_strict or r_dual)
            both_strict += t_ok and r_strict
            proper_strict += t_ok and r_strict and round(np.linalg.det(P)) == 1
check("B1", tiling_ok == 96 and role_ok == 96 and both == 24 and both_strict == 12 and proper_strict == 6,
      "tick symmetries (mod 2Z^3) and rung-2 role symmetries share 24 of 96 maps",
      f"tiling {tiling_ok}, roles(+dual) {role_ok}, both {both}, role-strict {both_strict}, proper role-strict {proper_strict}")

# ------------------------------------------------------------ C. qubit Margolus rules (GF(2))
LQ = 4
NQ = LQ ** 3


def q(x, y, z):
    return (x % LQ) + LQ * (y % LQ) + LQ * LQ * (z % LQ)


DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
PL = {0: [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], 1: [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)],
      2: [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]}


def stars_plaqs(images):
    ops = []
    for x in itertools.product(range(LQ), repeat=3):
        r = role(x)
        if r == 0 or images:
            ops.append((frozenset(q(x[0] + d[0], x[1] + d[1], x[2] + d[2]) for d in DIRS), frozenset()))
        if r == 2 or images:
            normals = [i for i in range(3) if x[i] % 2 == 0] if not images else [0, 1, 2]
            for nrm in normals:
                ops.append((frozenset(), frozenset(q(x[0] + d[0], x[1] + d[1], x[2] + d[2]) for d in PL[nrm])))
    return ops


def gf2_basis(vecs):
    basis = {}
    for v in vecs:
        while v:
            h = v.bit_length() - 1
            if h in basis:
                v ^= basis[h]
            else:
                basis[h] = v
                break
    return basis


def in_span(basis, v):
    while v:
        h = v.bit_length() - 1
        if h not in basis:
            return False
        v ^= basis[h]
    return True


def frozen_sites(ops, block):
    pos = {s: i for i, s in enumerate(block)}
    n = len(block)
    vecs = []
    for xs, zs in ops:
        xv = sum(1 << pos[s] for s in xs if s in pos)
        zv = sum(1 << pos[s] for s in zs if s in pos)
        if xv or zv:
            vecs.append(xv | (zv << n))
    bas = gf2_basis(vecs)
    fz = [s for s in block if in_span(bas, 1 << pos[s]) and in_span(bas, 1 << (pos[s] + n))]
    return len(bas), fz


def blocks(side, off):
    out = []
    for c in itertools.product(range(off, LQ + off, side), repeat=3):
        out.append([q(c[0] + a, c[1] + b, c[2] + cc) for a in range(side) for b in range(side) for cc in range(side)])
    return out


def coords(s):
    return (s % LQ, (s // LQ) % LQ, s // (LQ * LQ))


ops = stars_plaqs(False)
res = []
for off in (0, 1):
    for blk in blocks(2, off):
        rk, fz = frozen_sites(ops, blk)
        edges = [s for s in blk if role(coords(s)) == 1]
        res.append((rk, sorted(fz) == sorted(edges)))
check("C1", all(r == 6 and ok for r, ok in res),
      "2x2x2 Margolus: restrictions of stars+plaquettes span the full Pauli group of each cube's 3 edge sites",
      f"{len(res)} cubes, both tilings: rank 6, frozen = edge sites")
opsI = stars_plaqs(True)
resI = [frozen_sites(opsI, blk) for off in (0, 1) for blk in blocks(2, off)]
check("C2", all(r == 16 and len(fz) == 8 for r, fz in resI),
      "covariant image set (stars and plaquettes at every site): every cube site frozen",
      f"rank {resI[0][0]} of 16 on all {len(resI)} cubes")
# zoom: 4^3 blocks, two tilings offset (2,2,2) need LQ = 8; use an 8^3 torus here
LQ = 8; NQ = LQ ** 3
ops8 = stars_plaqs(False)
dyn = set(); allE = set(); nfr = []
for off in (0, 2):
    fr = set()
    for blk in blocks(4, off):
        _, fz = frozen_sites(ops8, blk)
        fr |= set(fz)
    E = {s for s in range(NQ) if role(coords(s)) == 1}
    allE = E
    nfr.append(len(fr & E))
    dyn |= (E - fr)
check("C3", len(dyn) == len(allE) and min(nfr) > 0,
      "zoom: 4^3 blocks leave edge sites unfrozen in at least one tiling (theorem evaded at a coarser rung)",
      f"frozen per tiling {nfr} of {len(allE)}; free in some tiling {len(dyn)}/{len(allE)}")
LQ = 4; NQ = LQ ** 3


# random Clifford cube gate, same on every cube of both tilings, full tick
def rand_symp(n, steps):
    M = np.eye(2 * n, dtype=np.uint8)
    J = np.zeros((2 * n, 2 * n), dtype=np.uint8)
    J[:n, n:] = np.eye(n, dtype=np.uint8); J[n:, :n] = np.eye(n, dtype=np.uint8)
    for _ in range(steps):
        h = RNG.integers(0, 2, size=2 * n).astype(np.uint8)
        if not h.any():
            continue
        # transvection v -> v + <v,h> h
        T = (np.eye(2 * n, dtype=np.uint8) + np.outer((J @ h) % 2, h).T) % 2
        M = (T @ M) % 2
    return M


def full_tick_map(Mc):
    big = np.eye(2 * NQ, dtype=np.uint8)
    for off in (0, 1):
        H = np.zeros((2 * NQ, 2 * NQ), dtype=np.uint8)
        for blk in blocks(2, off):
            ix = blk + [s + NQ for s in blk]
            H[np.ix_(ix, ix)] = Mc
        big = (H @ big) % 2
    return big


def opvec(xs, zs):
    v = np.zeros(2 * NQ, dtype=np.uint8)
    for s in xs:
        v[s] = 1
    for s in zs:
        v[s + NQ] = 1
    return v


sv = np.array([opvec(*o) for o in ops]).T
Jn = np.zeros((16, 16), dtype=np.uint8); Jn[:8, 8:] = np.eye(8, dtype=np.uint8); Jn[8:, :8] = np.eye(8, dtype=np.uint8)
kept = 0; nsamp = 200; symp_ok = True
for _ in range(nsamp):
    Mc = rand_symp(8, 40)
    symp_ok &= bool(np.array_equal((Mc.T @ Jn @ Mc) % 2, Jn))
    Mb = full_tick_map(Mc)
    img = (Mb @ sv) % 2
    kept += int(np.array_equal(img, sv))
check("C4", symp_ok and kept == 0,
      "random Clifford cube gates (same on all cubes, two tilings): none keeps the stars over a full tick",
      f"{kept}/{nsamp} keep all {sv.shape[1]} stars+plaquettes (finite diagnostic)")
Mid = np.eye(16, dtype=np.uint8)
check("C5", np.array_equal((full_tick_map(Mid) @ sv) % 2, sv),
      "control: the identity (least information, moves nothing) keeps every star", "")

el = time.time() - T0
print(f"elapsed {el:.1f} s (AUDIT_TIMEOUT_SEC = {AUDIT_TIMEOUT_SEC})")
print("SUPPLIED: CL-1 flat-edge tick (no links, no edge registers, no split); the star/plaquette sets;")
print("  Clifford-only gates in C4. CITED: register band formula (A4 checks it numerically).")
print(f"TOTAL: PASS={NP} FAIL={NF}")
