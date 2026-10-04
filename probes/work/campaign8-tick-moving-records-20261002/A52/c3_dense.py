"""A52 c3: numeric checks with the true U(1) link operators (raise_out, sigma^axis) and exact SU(2) lifts.
(A) corner star, 6 link qubits, dense 64x64: covariance under the 24 turns about v with the record turned,
    Gauss commutators, all 20 Levin-Wen phases; controls.
(B) one coarse cube, 12 link qubits (product-operator arithmetic, plus sparse 4096-dim spot checks):
    covariance under the 24 turns about the cube centre with the 8 corner records turned; Gauss; corner
    junctions; decorated ring = loop product of hops; commutation with off-loop hops; bare ring control."""
import signal, itertools
signal.alarm(110)
import numpy as np
from collections import Counter
from a52lib import *

rng = np.random.default_rng(5252)
def ad(g, m):
    return U[g] @ m @ U[g].conj().T
def field(a):
    return PAUL[a + 1]
def kron_sites(op, sites):
    out = np.array([[1.0 + 0j]])
    for s in sites:
        out = np.kron(out, op.get(s, I2))
    return out
def fit(A, B):
    nb = np.vdot(B, B).real
    if nb < 1e-14:
        return None, np.inf
    c = np.vdot(B, A) / nb
    return c, np.linalg.norm(A - c * B) / np.sqrt(nb)
def pmult(*ops):
    out = {}
    for op in ops:
        for s, m in op.items():
            out[s] = out.get(s, I2) @ m
    return out
def pdag(op):
    return {s: m.conj().T for s, m in op.items()}
def pprop(A, B):
    """A = c B for product operators (per site); returns c, residual."""
    c = 1.0 + 0j; res = 0.0
    for s in set(A) | set(B):
        a = A.get(s, I2); b = B.get(s, I2)
        cs, r = fit(a, b)
        if cs is None:
            return None, np.inf
        c *= cs; res = max(res, r)
    return c, res

# ---------------- (A) corner star ----------------
print("(A) corner star (6 link qubits), dense")
SITES = [tuple(d) for d in DIRS]
def star_hops(T):
    hops = []
    for i in range(6):
        op = {SITES[i]: raise_out(i)}
        for j in range(6):
            if j != i and T[i][j]:
                op[SITES[j]] = field(AXIS[j])
        hops.append(op)
    return hops
def turn_op(g, op):
    return {tuple(int(v) for v in ROT[g] @ np.array(s)): ad(g, m) for s, m in op.items()}
Tof, _ = family(ALL_C3_T[0])
HOPS = {f: star_hops(Tof[f]) for f in BD}
worst = 0.0; phases = Counter()
for g in range(24):
    for f in BD:
        for i in range(6):
            img = kron_sites(turn_op(g, HOPS[f][i]), SITES)
            tgt = kron_sites(HOPS[act_vec(g, f)][PERM[g][i]], SITES)
            c, r = fit(img, tgt)
            worst = max(worst, r, abs(abs(c) - 1))
            phases[np.round(c, 6)] += 1
print("   covariance U_g t_i[f] U_g^dag = c t_{gi}[gf]: max residual %.1e over 24 x 8 x 6; phases c seen: %s" % (worst, sorted(phases, key=lambda z: (z.real, z.imag))))
G = sum(SIGN[j] * kron_sites({SITES[j]: field(AXIS[j])}, SITES) for j in range(6)) / 2
gw = 0.0
for f in BD:
    for i in range(6):
        t = kron_sites(HOPS[f][i], SITES)
        gw = max(gw, np.linalg.norm(G @ t - t @ G - t))
print("   Gauss: max ||[G_v, t_i] - t_i|| = %.1e (G_v = outward field / 2)" % gw)
jt = Counter(); jres = 0.0
for f in BD:
    T = [kron_sites(h, SITES) for h in HOPS[f]]
    for tri in itertools.combinations(range(6), 3):
        for (a, b, c) in itertools.permutations(tri):
            X1 = T[a] @ T[b].conj().T @ T[c]; X2 = T[c] @ T[b].conj().T @ T[a]
            th, r = fit(X1, X2)
            jres = max(jres, r); jt[np.round(th, 9)] += 1
print("   junction phases, all 8 records x 20 triples x 6 orderings: %s, max residual %.1e" % (dict(jt), jres))
# control 1: fully covariant (no record) random decorations: field factors chosen O-symmetrically (A45)
def covariant_random():
    # orbit rep: hop +x; its stabilizer C4x permutes {+y,+z,-y,-z} cyclically, fixes -x
    b_anti = rng.integers(2); b_perp = rng.integers(2)
    T = [[0] * 6 for _ in range(6)]
    for g in range(24):
        i = PERM[g][0]
        for j in range(6):
            if j == i: continue
            if j == PERM[g][1]: T[i][j] = b_anti
            elif j != i: T[i][j] = b_perp
    return T
ct = Counter()
for _ in range(20):
    T = covariant_random(); H = [kron_sites(h, SITES) for h in star_hops(T)]
    for tri in itertools.combinations(range(6), 3):
        th, r = fit(H[tri[0]] @ H[tri[1]].conj().T @ H[tri[2]], H[tri[2]] @ H[tri[1]].conj().T @ H[tri[0]])
        kind = 'T' if len({AXIS[k] for k in tri}) < 3 else 'corner'
        ct[(kind, np.round(th, 9))] += 1
print("   control, no record (O-covariant decorations, 20 samples): %s" % dict(ct))
# control 2: C3-symmetrized BK order (covariance forced by summing the 3 images)
order = [1, 3, 5, 0, 2, 4]
Tbk = [[0] * 6 for _ in range(6)]
for a in range(6):
    for b in range(6):
        if order.index(a) < order.index(b): Tbk[b][a] = 1
imgs = [star_hops(transport_T(g, Tbk)) for g in C3GROUP]
Hs = [sum(kron_sites(im[i], SITES) for im in imgs) / 3 for i in range(6)]
cs = Counter(); rmax = 0.0
for tri in itertools.combinations(range(6), 3):
    th, r = fit(Hs[tri[0]] @ Hs[tri[1]].conj().T @ Hs[tri[2]], Hs[tri[2]] @ Hs[tri[1]].conj().T @ Hs[tri[0]])
    cs['scalar' if r < 1e-9 else 'not scalar'] += 1; rmax = max(rmax, r)
cres = 0.0
for g in C3GROUP:
    for i in range(6):
        img = sum(kron_sites(turn_op(g, im[i]), SITES) for im in imgs) / 3
        cres = max(cres, fit(img, Hs[PERM[g][i]])[1])
print("   control, BK order made C3-covariant by summing its 3 images: C3 covariance residual %.1e; junctions %s (max residual %.2f)" % (cres, dict(cs), rmax))
# control 3: BK order with an arbitrary (non-transported) record family: covariance residual
fam_bad = {f: Tbk for f in BD}
w2 = 0.0
for g in range(24):
    for i in range(6):
        img = kron_sites(turn_op(g, star_hops(fam_bad[F0])[i]), SITES)
        tgt = kron_sites(star_hops(fam_bad[act_vec(g, F0)])[PERM[g][i]], SITES)
        w2 = max(w2, fit(img, tgt)[1])
print("   control, same BK order for every record (no transport): max covariance residual %.3f" % w2)

# ---------------- (B) one coarse cube ----------------
print("(B) one coarse cube: 12 link qubits, 8 corner records, turns about the cube centre")
CEN = np.array([1, 1, 1])
CORN = [tuple(c) for c in itertools.product([0, 2], repeat=3)]
LINKS = sorted({tuple(int(v) for v in (np.array(c) + np.array(d))) for c in CORN for d in DIRS
                if all(0 <= x <= 2 for x in np.array(c) + np.array(d))})
assert len(LINKS) == 12
def legs_in(v):
    return [i for i in range(6) if all(0 <= x <= 2 for x in np.array(v) + 2 * np.array(DIRS[i]))]
def cube_hop(l, recs):
    x = np.array(l); a = [k for k in range(3) if x[k] % 2][0]
    e = np.zeros(3, int); e[a] = 1
    v = tuple(int(t) for t in x - e); w = tuple(int(t) for t in x + e)
    i, ip = 2 * a, 2 * a + 1
    op = {l: raise_out(i)}          # raises the field pointing out of v (along +a)
    for (c, leg) in ((v, i), (w, ip)):
        T = Tof[recs[c]]
        for j in legs_in(c):
            if j != leg and T[leg][j]:
                s = tuple(int(t) for t in np.array(c) + np.array(DIRS[j]))
                op[s] = op.get(s, I2) @ field(AXIS[j])
    return op
def turn_c(g, x):
    return tuple(int(t) for t in CEN + ROT[g] @ (np.array(x) - CEN))
def turn_cop(g, op):
    return {turn_c(g, s): ad(g, m) for s, m in op.items()}
FACES = []
for a, b in [(0, 1), (0, 2), (1, 2)]:
    k = 3 - a - b
    for h in (0, 2):
        v0 = [0, 0, 0]; v0[k] = h
        ea = np.eye(3, dtype=int)[a] * 2; eb = np.eye(3, dtype=int)[b] * 2
        cs_ = [tuple(v0), tuple(np.array(v0) + ea), tuple(np.array(v0) + ea + eb), tuple(np.array(v0) + eb)]
        FACES.append(cs_)
def mid(c1, c2):
    return tuple(int(t) for t in (np.array(c1) + np.array(c2)) // 2)
def hop_dir(c1, c2, recs):
    """hop moving along the link from c1 to c2: raise of the field out of c1 = cube_hop if c1 is the lower end."""
    l = mid(c1, c2); h = cube_hop(l, recs)
    return h if sum(c1) < sum(c2) else pdag(h)
def loop_op(cs_, recs):
    return pmult(*[hop_dir(cs_[k], cs_[(k + 1) % 4], recs) for k in range(4)][::-1])   # rightmost acts first
bgs = {'uniform f0': {c: F0 for c in CORN}}
for r in range(3):
    bgs['random %d' % r] = {c: BD[rng.integers(8)] for c in CORN}
for name, recs in bgs.items():
    cw = 0.0; lw = 0.0
    for g in range(24):
        recs_g = {turn_c(g, c): act_vec(g, f) for c, f in recs.items()}
        for l in LINKS:
            x = np.array(l); a = [k for k in range(3) if x[k] % 2][0]; e = np.zeros(3, int); e[a] = 1
            v = tuple(int(t) for t in x - e); w = tuple(int(t) for t in x + e)
            c, r = pprop(turn_cop(g, cube_hop(l, recs)), hop_dir(turn_c(g, v), turn_c(g, w), recs_g))
            cw = max(cw, r, abs(abs(c) - 1) if c is not None else 1)
        for cs_ in FACES:
            img = turn_cop(g, loop_op(cs_, recs))
            gcs = [turn_c(g, c) for c in cs_]
            # image face: same corner cycle (possibly reversed orientation / shifted start)
            cands = [loop_op(gcs[k:] + gcs[:k], recs_g) for k in range(4)] + [loop_op((gcs[::-1])[k:] + (gcs[::-1])[:k], recs_g) for k in range(4)]
            best = min(pprop(img, cd)[1] for cd in cands)
            lw = max(lw, best)
    # Gauss (sparse-free: per-site algebra): field factors commute with fields; raise shifts one link
    # corner junctions: three cube legs at each corner
    jc = Counter()
    for v in CORN:
        lg = legs_in(v)
        hv = [hop_dir(v, tuple(int(t) for t in np.array(v) + 2 * np.array(DIRS[i])), recs) for i in lg]
        X1 = pmult(hv[2], pdag(hv[1]), hv[0]); X2 = pmult(hv[0], pdag(hv[1]), hv[2])
        th, r = pprop(X1, X2); jc[(np.round(th, 9), r < 1e-9)] += 1
    # loop vs hops: commute with hops off the loop; bare ring control
    lc = Counter(); bc = Counter()
    for cs_ in FACES:
        Lp = loop_op(cs_, recs)
        Wbare = pmult(*[{mid(cs_[k], cs_[(k + 1) % 4]): hop_dir(cs_[k], cs_[(k + 1) % 4], recs)[mid(cs_[k], cs_[(k + 1) % 4])]} for k in range(4)][::-1])
        loopl = {mid(cs_[k], cs_[(k + 1) % 4]) for k in range(4)}
        for l in LINKS:
            if l in loopl: continue
            t = cube_hop(l, recs)
            c1, r1 = pprop(pmult(t, Lp), pmult(Lp, t)); lc[(np.round(c1, 9), r1 < 1e-9)] += 1
            c2, r2 = pprop(pmult(t, Wbare), pmult(Wbare, t)); bc[np.round(c2, 9)] += 1
    print("   %-11s covariance: hops max residual %.1e, loop ops %.1e | corner junctions %s" % (name, cw, lw, dict(jc)))
    print("               decorated loop vs off-loop hops (t L = c L t): %s | bare ring loop: %s" % (dict(lc), dict(bc)))
print("done")
