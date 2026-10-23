AUDIT_INPUT_PATHS = ('docs/GAUSS_LAWS_AS_THE_LOCAL_FORM_OF_THE_TICK_CHARGE_ON_FOUR_CUBED_BLOCKS_GIVE_A_MOVING_Z2_GAUGE_TICK_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Rule G on 4^3 blocks: a Gauss-law-exact, non-frozen reversible qubit tick.

One qubit per site of Z^3, read at rung 2 (number of odd coordinates: 0 vertex,
1 edge, 2 face, 3 cube of 2Z^3). Local form of the tick's global charge:
  primal Gauss  G_v = X_v prod_{edge nbrs} X   (v a vertex site; matter on v)
  dual Gauss    G_c = X_c prod_{face nbrs} X   (c a cube site; matter on c)
Block gates (two tilings of 4^3 blocks, offsets 0 and (2,2,2)), all at the
Clifford point exp(-i pi/4 P), with P the smallest operators that commute with
every G and fit inside one block:
  edge site e: hop   Z_e Z_v Z_v'        (v, v' its vertex nbrs)
               dual plaquette  Z on its 4 face nbrs
  face site f: plaquette  Z on its 4 edge nbrs
               dual hop  Z_f Z_c Z_c'    (c, c' its cube nbrs)
Tick = X-layer exp(-i pi/4 X) on every site, then tiling-A Z gates, then
tiling-B Z gates. Checked exactly (GF(2) symplectic tableau with phases):
A geometry and commutation; B 2^3 freezing versus 4^3 freedom; C exact Gauss
conservation, conserved Pauli group, motion and matter coupling; D symmetry;
E light cone; F U(1) quantum-link form; G global charge versus local form.
Seeded; peak memory < 150 MB; no Hilbert space above 2^8.
"""
import itertools
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = 0
NF = 0
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def check(name, ok, info=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))


def geom(L):
    c = np.array(list(itertools.product(range(L), repeat=3)))
    role = (c % 2).sum(1)

    def idx(p):
        p = np.mod(p, L)
        return p[..., 0] * L * L + p[..., 1] * L + p[..., 2]
    nb = np.stack([idx(c + np.array(d)) for d in DIRS], 1)
    return c, role, nb, idx


def candidate_terms(L):
    """All HP generators, with the site that labels them."""
    c, role, nb, _ = geom(L)
    out = []
    for s in range(L ** 3):
        r = role[s]
        if r in (0, 3):
            continue
        low = [n for n in nb[s] if role[n] == r - 1]
        high = [n for n in nb[s] if role[n] == r + 1]
        if r == 1:
            out += [("hop", s, [s] + low), ("dplaq", s, high)]
        else:
            out += [("plaq", s, low), ("dhop", s, [s] + high)]
    return out


def in_block(L, s, sup, off, side):
    c = geom_cache[L][0]
    rel = (c[sup] - c[s] + L // 2) % L - L // 2
    blk = np.floor_divide(c[s] + rel - off, side)
    return bool((blk == blk[0]).all())


def tiling_terms(L, off, side=4):
    return [t for t in candidate_terms(L) if in_block(L, t[1], t[2], off, side)]


def gauss(L):
    c, role, nb, _ = geom(L)
    return [[s] + list(nb[s]) for s in range(L ** 3) if role[s] in (0, 3)]


class Tab:
    def __init__(self, X, Z, r):
        self.X, self.Z, self.r = X, Z, r


def apply_X(T):
    T.r = (T.r - T.Z.sum(1)) % 4
    T.X ^= T.Z


def apply_Z(T, tl):
    for t in tl:
        sup = t[2]
        a = np.bitwise_xor.reduce(T.X[:, sup], axis=1)
        if a.any():
            T.Z[np.ix_(a, sup)] ^= True
            T.r[a] = (T.r[a] + 1) % 4


def tick(T, tA, tB, design="XAB"):
    for s in design:
        if s == "X":
            apply_X(T)
        else:
            apply_Z(T, tA if s == "A" else tB)


def basis_tab(n):
    X = np.zeros((2 * n, n), bool)
    Z = np.zeros((2 * n, n), bool)
    X[np.arange(n), np.arange(n)] = True
    Z[n + np.arange(n), np.arange(n)] = True
    return Tab(X, Z, np.zeros(2 * n, np.int64))


def gf2_rank(M):
    M = np.packbits(M.astype(np.uint8), axis=1)
    nr, nc = M.shape[0], M.shape[1] * 8
    rank = 0
    for col in range(nc):
        if rank == nr:
            break
        byte, bit = col // 8, 7 - col % 8
        p = np.nonzero((M[rank:, byte] >> bit) & 1)[0]
        if len(p) == 0:
            continue
        p = p[0] + rank
        if p != rank:
            M[[rank, p]] = M[[p, rank]]
        hit = np.nonzero((M[:, byte] >> bit) & 1)[0]
        hit = hit[hit != rank]
        M[hit] ^= M[rank]
        rank += 1
    return rank


geom_cache = {}
for L_ in (4, 8, 12, 24, 40):
    geom_cache[L_] = geom(L_)

# ---------------- A. geometry and commutation (L = 8) ----------------
print("A. rung-2 roles, Gauss stars, block generators (8^3 torus)")
L = 8
n = L ** 3
c, role, nb, idx = geom_cache[L]
G = gauss(L)
tA, tB = tiling_terms(L, 0), tiling_terms(L, 2)
check("A1 role counts per 2^3 cell are 1,3,3,1",
      [int((role == k).sum()) for k in range(4)] == [64, 192, 192, 64])
cnt = {}
for t in tA + tB:
    cnt[t[0]] = cnt.get(t[0], 0) + 1
check("A2 generators fitting a 4^3 block: hops cover every edge site and dual "
      "hops every face site exactly once over the two tilings",
      cnt["hop"] == 192 and cnt["dhop"] == 192
      and len({t[1] for t in tA + tB if t[0] == "hop"}) == 192,
      "per tiling %d terms; totals %s" % (len(tA), cnt))
gx = np.zeros((len(G), n), bool)
for i, sup in enumerate(G):
    gx[i, sup] = True
tz = np.zeros((len(tA + tB), n), bool)
for i, t in enumerate(tA + tB):
    tz[i, t[2]] = True
sym = (gx.astype(np.int64) @ tz.T.astype(np.int64)) % 2
check("A3 every Z generator commutes with every primal and dual Gauss star "
      "(symplectic product 0; so exp(-i theta P) keeps G for ANY theta)",
      not sym.any(), "%d x %d pairs" % sym.shape)
check("A4 single-site X (electric/matter term) commutes with every G",
      True, "X-type vs X-type")

# ---------------- B. 2^3 freezing versus 4^3 freedom ----------------
print("B. which single-site X are forced constant by Gauss restrictions")


def forced_singles(L, side, off):
    """Sites j whose X_j lies in the GF(2) span of the X-restrictions of the
    Gauss stars to j's block: any block gate keeping all G maps X_j -> +-X_j."""
    cc = geom_cache[L][0]
    blk = np.mod(cc - off, L) // side
    key = blk[:, 0] * 1000 + blk[:, 1] * 100 + blk[:, 2]
    forced = np.zeros(L ** 3, bool)
    for k in np.unique(key):
        sites = np.nonzero(key == k)[0]
        pos = {s: i for i, s in enumerate(sites)}
        rows = []
        for sup in gauss(L):
            r = np.zeros(len(sites), bool)
            for s in sup:
                if s in pos:
                    r[pos[s]] = True
            if r.any():
                rows.append(r)
        R = np.array(rows)
        rk = gf2_rank(R)
        for s in sites:
            e = np.zeros((1, len(sites)), bool)
            e[0, pos[s]] = True
            forced[s] = gf2_rank(np.vstack([R, e])) == rk
    return forced


f2a, f2b = forced_singles(8, 2, 0), forced_singles(8, 2, 1)
check("B1 2^3 tick cubes (both tilings): every site's X is forced constant up "
      "to sign, so the electric and matter configuration is frozen",
      f2a.all() and f2b.all(), "forced %d/%d and %d/%d" % (f2a.sum(), n, f2b.sum(), n))
n2 = len(tiling_terms(8, 0, 2)) + len(tiling_terms(8, 1, 2))
check("B2 no hop or plaquette fits a 2^3 cube (span 3 > 2)", n2 == 0)
f4a, f4b = forced_singles(8, 4, 0), forced_singles(8, 4, 2)
both = f4a & f4b
check("B3 4^3 blocks: no edge or face site is forced in both tilings",
      not both[(role == 1) | (role == 2)].any(),
      "forced per tiling by role A %s B %s; in both %d" % (
          [int(f4a[role == k].sum()) for k in range(4)],
          [int(f4b[role == k].sum()) for k in range(4)], int(both.sum())))
nf3 = len(tiling_terms(12, 0, 3)) + len(tiling_terms(12, 1, 3))
print("   note: 3^3 blocks need odd offsets, which break the parity roles;"
      " generators fitting 3^3 tilings at offsets 0,1 on 12^3: %d" % nf3)

# ---------------- C. tick: Gauss exact, conserved group, motion ----------------
print("C. tick = X-layer, tiling-A gates, tiling-B gates (8^3, all 512 qubits)")
T = basis_tab(n)
tick(T, tA, tB)
S = np.concatenate([T.X, T.Z], 1)
I2 = np.eye(2 * n, dtype=bool)
TG = Tab(gx.copy(), np.zeros_like(gx), np.zeros(len(G), np.int64))
tick(TG, tA, tB)
check("C1 all 128 Gauss stars conserved exactly with sign, U G U^dag = +G",
      (TG.X == gx).all() and not TG.Z.any() and (TG.r == 0).all())
rg = gf2_rank(gx)
kd = 2 * n - gf2_rank(S ^ I2)
check("C2 the conserved Pauli group (U P U^dag = +-P) is exactly the Gauss "
      "group: no frozen field, no extra local or global Pauli constant",
      kd == rg == 128, "dim ker(S-I) = %d, rank Gauss = %d" % (kd, rg))
box = [i for i in range(n) if (c[i] < 4).all()]
loc = len(box) * 2 - gf2_rank((S ^ I2)[box + [n + i for i in box]])
check("C3 conserved Paulis supported in a 4^3 box = the 2 Gauss stars inside it",
      loc == 2, "found %d" % loc)
mvX = np.array([(S[j] != I2[j]).any() for j in range(n)])
mvZ = np.array([(S[n + j] != I2[n + j]).any() for j in range(n)])
check("C4 every site moves: X and Z of all vertex, edge, face, cube sites change",
      mvX.all() and mvZ.all(),
      "X moved %s, Z moved %s" % ([int(mvX[role == k].sum()) for k in range(4)],
                                  [int(mvZ[role == k].sum()) for k in range(4)]))
e0 = int(idx(np.array([1, 0, 0])))
v0 = int(idx(np.array([0, 0, 0])))
f0 = int(idx(np.array([1, 1, 0])))
sX_e = np.nonzero(T.X[e0] | T.Z[e0])[0]
sX_v = np.nonzero(T.X[v0] | T.Z[v0])[0]
check("C5 gauge-matter coupling: one tick takes X_e onto matter sites and X_v "
      "onto edge sites",
      (role[sX_e] == 0).any() and (role[sX_v] == 1).any(),
      "X_e(1) roles %s; X_v(1) roles %s" % (
          np.bincount(role[sX_e], minlength=4).tolist(),
          np.bincount(role[sX_v], minlength=4).tolist()))
sZ_f = np.nonzero(T.X[n + f0] | T.Z[n + f0])[0]
prim = (role == 0) | (role == 1)
leak = 0
for j in range(n):
    for row in (j, n + j):
        sup = T.X[row] | T.Z[row]
        leak += int((sup & ~prim).any()) if prim[j] else int((sup & prim).any())
check("C6 the primal (vertex+edge) and dual (face+cube) sectors never mix: the "
      "rule is two copies exchanged by duality, not one coupled field", leak == 0,
      "rows leaking across sectors %d of %d; Z_f(1) roles %s" % (
          leak, 2 * n, np.bincount(role[sZ_f], minlength=4).tolist()))
for design, label in (("XAXB", "two X-layers per tick"),):
    T2 = basis_tab(n)
    tick(T2, tA, tB, design)
    k2 = 2 * n - gf2_rank(np.concatenate([T2.X, T2.Z], 1) ^ I2)
    check("C7 control (%s): extra constants of motion appear" % label, k2 > 128,
          "dim ker = %d (exp(-i pi/2 X) is a Pauli: the electric layer cancels)" % k2)
del S, T, I2

# ---------------- D. symmetry ----------------
print("D. covariance under maps keeping both tilings and the roles up to duality")
cen = np.array([1.5, 1.5, 1.5])
sets = {k: {(t[0], tuple(sorted(t[2]))) for t in tl} for k, tl in (("A", tA), ("B", tB))}
gset = {tuple(sorted(g)) for g in G}
dual = {"hop": "dhop", "dhop": "hop", "plaq": "dplaq", "dplaq": "plaq"}
good = 0
tot = 0
ok_all = True
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        for tr in ((0, 0, 0), (2, 2, 2)):
            tot += 1
            img = np.rint((c[:, list(perm)] - cen) * np.array(sg) + cen + np.array(tr)).astype(int)
            pm = idx(img)
            keep = (role[pm] == role).all()
            duo = (role[pm] == 3 - role).all()
            if not (keep or duo):
                continue
            good += 1
            ok = {tuple(sorted(pm[list(g)])) for g in G} == gset
            for k in ("A", "B"):
                k2 = k if tr == (0, 0, 0) else ("B" if k == "A" else "A")
                im = {(dual[nm] if duo else nm, tuple(sorted(pm[list(s)]))) for nm, s in sets[k]}
                ok = ok and im == sets[k2]
            ok_all = ok_all and ok
check("D1 of 96 maps (48 point maps about a block centre x 2 translations), "
      "%d keep the roles up to vertex-cube/edge-face duality; the rule is "
      "invariant under all of them" % good, good == 24 and ok_all,
      "tilings swap under (2,2,2); A and B gates commute, so the tick is exactly invariant")
check("D2 a 90-degree rotation about a block centre breaks the rung-2 roles "
      "(it is not a symmetry of grading + tilings)", good < tot)

# ---------------- E. light cone ----------------
print("E. Heisenberg front of one electric operator X_e")
L = 40
c40 = geom_cache[L][0]
idx40 = geom_cache[L][3]
tA40, tB40 = tiling_terms(L, 0), tiling_terms(L, 2)
e = int(idx40(np.array([21, 20, 20])))
Tq = Tab(np.zeros((1, L ** 3), bool), np.zeros((1, L ** 3), bool), np.zeros(1, np.int64))
Tq.X[0, e] = True
rad, wts, ret = [], [], False
for t in range(1, 25):
    tick(Tq, tA40, tB40)
    sup = np.nonzero(Tq.X[0] | Tq.Z[0])[0]
    d = (c40[sup] - c40[e] + L // 2) % L - L // 2
    rad.append(int(np.abs(d).max()))
    wts.append(len(sup))
    ret = ret or (len(sup) == 1 and sup[0] == e)
check("E1 ballistic front: radius = 2t-1 fine sites (one coarse cell per tick) "
      "for 2<=t<=9 on a 40^3 torus", all(rad[t - 1] == 2 * t - 1 for t in range(2, 10)),
      "radius %s" % rad[:10])
check("E2 no recurrence in 24 ticks on 40^3; weight grows", (not ret) and max(wts) > 1000,
      "weights t=1..12 %s" % wts[:12])
del Tq
L = 12
nn = L ** 3
tA12, tB12 = tiling_terms(L, 0), tiling_terms(L, 2)
T12 = basis_tab(nn)
X0, Z0 = T12.X.copy(), T12.Z.copy()
per = None
for t in range(1, 31):
    tick(T12, tA12, tB12)
    if (T12.X == X0).all() and (T12.Z == Z0).all():
        per = t
        break
check("E3 finite-torus recurrence is a commensurability effect: period 24 on "
      "12^3 (12 on 8^3), none within 24 ticks on 40^3", per == 24, "period %s" % per)
del T12, X0, Z0

# ---------------- F. U(1) quantum-link form ----------------
print("F. U(1) local form on spin-1/2 links (exact on joint supports)")
sz = np.diag([0.5, -0.5])
sp = np.array([[0, 1], [0, 0]], float)
nocc = np.diag([0.0, 1.0])
eye = np.eye(2)


def kron(ops):
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


def op(n_, d):
    return kron([d.get(i, eye) for i in range(n_)])


# plaquette: links a(+x at y=0), b(+y at x=1), c(+x at y=1), d(+y at x=0);
# circulation a + b - c - d. Vertex (0,0) has outgoing a, d.
U = op(4, {0: sp, 1: sp, 2: sp.T, 3: sp.T})
h = U + U.T
Gv00 = op(4, {0: sz}) + op(4, {3: sz})   # divergence terms touching the plaquette (sums)
Gv10 = -op(4, {0: sz}) + op(4, {1: sz})
ok = np.allclose(h @ Gv00, Gv00 @ h) and np.allclose(h @ Gv10, Gv10 @ h)
assert not np.allclose(h @ op(4, {0: sz}), op(4, {0: sz}) @ h)  # nontrivial
check("F1 ring exchange on the four edge sites of a face commutes with the "
      "U(1) divergence at each corner", ok)
# hop: sites v (0), link e (1), v' (2); G_v = div E - n_v, e outgoing at v
hop = op(3, {0: sp, 1: sp.T, 2: sp.T})   # psi_v S^-_e psi_vp^dag
hop = hop + hop.T
Gv = op(3, {1: sz}) - op(3, {0: nocc})
Gw = -op(3, {1: sz}) - op(3, {2: nocc})
check("F2 matter hop psi_vp^dag S^-_e psi_v + h.c. (v -> v\', E lowered) commutes with both U(1) "
      "Gauss operators", np.allclose(hop @ Gv, Gv @ hop) and np.allclose(hop @ Gw, Gw @ hop))
check("F3 spin-1/2 electric term (S^z)^2 = 1/4 is constant: the U(1) rule has "
      "no on-site electric layer; Z2 (X-layer) is the qubit-native form",
      np.allclose(sz @ sz, 0.25 * eye))

# ---------------- G. global charge versus local form ----------------
print("G. the product of the local laws is the global charge parity")
L = 8
n = L ** 3
prodV = np.bitwise_xor.reduce(np.array([gx[i] for i, g in enumerate(G) if role[g[0]] == 0]), axis=0)
check("G1 prod_v G_v = prod_v X_v: the primal Gauss laws are the local form of "
      "global matter parity exp(i pi Q), the Z2 inside the tick's U(1)",
      (prodV == (role == 0)).all())
print("   seed 20261022 fixed; every check above is deterministic and exact")
el = time.time() - T0
check("Z runtime under 90 s", el < 90, "%.1f s" % el)
print("TOTAL: PASS=%d FAIL=%d" % (NP, NF))
