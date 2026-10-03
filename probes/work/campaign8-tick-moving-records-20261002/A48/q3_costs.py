"""A48 Q3: decision 28's first two costs under the looser reading.

(A) KS / pi-flux signs on one internal state per place (one-particle sector, 4^3 torus):
    each turn about a site and each unit translation is a symmetry up to a Z relabeling;
    group law of the relabeled turns: projective class of the 24 turns (invariant W_a^4,
    a = C4z), translation commutator, period-2 translations.
(B) Hop-only form under relabelings of exact turns: linear conserved charges of an XY bond
    (null space), and the largest turn group fixing an axis.  Glued form: spectra of +-sigma.sigma.
(C) One-part charged hop through a spin-1/2 link: phase of the link's outward raising operator
    under the quarter turn about its own axis, exact (Q3), random frame changes of Q3 (non-
    Clifford), and the looser link action that does not turn a link about its own axis;
    Gauss-law check; ring terms at a vertex under the looser link action.
"""
import itertools, signal
import numpy as np
from a48lib import *

signal.alarm(280)
rng = np.random.default_rng(4803)

# ---------- (A) KS one-particle ----------
print("(A) KS signs, one internal state per place, 4^3 torus (one-particle sector)")
L = 4
sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
sidx = {s: k for k, s in enumerate(sites)}
N = len(sites)
def eta(a, s):
    x1, x2, x3 = s
    return [1, (-1) ** x1, (-1) ** (x1 + x2)][a]
h = np.zeros((N, N))
bonds = []
for s in sites:
    for a in range(3):
        t = list(s); t[a] = (t[a] + 1) % L; t = tuple(t)
        h[sidx[s], sidx[t]] = h[sidx[t], sidx[s]] = eta(a, s)
        bonds.append((sidx[s], sidx[t]))
def perm_of(g):
    tr, k = g
    P = np.zeros((N, N))
    for s in sites:
        y = tuple(int(c) % L for c in ROT[k] @ np.array(s) + np.array(tr))
        P[sidx[y], sidx[s]] = 1
    return P
def relabel(g):
    """W_g = D_g P_g with D_g diagonal +-1 and W_g h W_g^T = h, or None."""
    P = perm_of(g); hp = P @ h @ P.T
    rows = []
    for (i, j) in bonds:
        rhs = int(round(hp[i, j])) != int(round(h[i, j]))
        if abs(hp[i, j]) < 0.5:
            return None
        rows.append(((1 << i) | (1 << j), int(rhs)))
    sol = gf2_solve(rows, N)
    if sol is None:
        return None
    D = np.diag([(-1) ** b for b in sol])
    W = D @ P
    assert np.allclose(W @ h @ W.T, h)
    return W
turns = [((0, 0, 0), k) for k in range(24)]
trans = [((1, 0, 0), ID), ((0, 1, 0), ID), ((0, 0, 1), ID)]
W = {g: relabel(g) for g in turns + trans + [((2, 0, 0), ID), ((0, 2, 0), ID), ((0, 0, 2), ID)]}
print("   each of the 24 turns about a site is a symmetry up to a Z relabeling: %s" % all(W[g] is not None for g in turns))
print("   each unit translation is a symmetry up to a Z relabeling: %s" % all(W[g] is not None for g in trans))
print("   without relabeling, turns that keep the signs exactly: %d of 24" % sum(np.allclose(perm_of(g) @ h @ perm_of(g).T, h) for g in turns))
def scal(M):
    """M must be +-identity (diagonal gauge symmetry of a connected pi-flux pattern)."""
    d = np.diag(M)
    assert np.allclose(M, np.diag(d)) and np.allclose(np.abs(d), 1)
    return int(round(d[0])) if np.allclose(d, d[0]) else None
Wa = W[((0, 0, 0), C4[2])]; Wb = W[((0, 0, 0), C3d)]
lam1 = scal(np.linalg.matrix_power(Wa, 4)); lam2 = scal(np.linalg.matrix_power(Wb, 3))
lam3 = scal(np.linalg.matrix_power(Wa @ Wb, 2))
print("   24 turns about a site: W_a^4 = %s, W_b^3 = %s, (W_a W_b)^2 = %s  (a = C4z, b = C3(111));" % (lam1, lam2, lam3))
print("      projective invariant lam1^3 lam2^4 lam3^-6 = %s  (-1: the relabeled turns compose only up to the global charge parity)"
      % (lam1 ** 3 * lam2 ** 4 * lam3 ** -6))
# also check: is every relation defect a global sign (not a pattern)?
defects = set()
for g in turns:
    for hh in turns:
        gh = ((0, 0, 0), MUL[g[1]][hh[1]])
        defects.add(scal(W[g] @ W[hh] @ W[gh].T))
print("   defects W_g W_h W_gh^-1 over all 24x24 pairs of turns: %s (all global)" % sorted(defects))
Tx, Ty, Tz = (W[g] for g in trans)
print("   unit translations: Tx Ty Tx^-1 Ty^-1 = %s, Ty Tz.. = %s, Tz Tx.. = %s"
      % (scal(Tx @ Ty @ Tx.T @ Ty.T), scal(Ty @ Tz @ Ty.T @ Tz.T), scal(Tz @ Tx @ Tz.T @ Tx.T)))
T2 = [W[((2, 0, 0), ID)], W[((0, 2, 0), ID)], W[((0, 0, 2), ID)]]
print("   period-2 translations: commutators %s" % [scal(T2[i] @ T2[j] @ T2[i].T @ T2[j].T) for i, j in [(0, 1), (1, 2), (2, 0)]])
# turns vs unit translations: W_g T W_g^-1 vs T_{g e}
mix = set()
for g in turns:
    for a, tg in enumerate(trans):
        e = np.zeros(3, dtype=int); e[a] = 1
        ge = tuple(int(c) for c in ROT[g[1]] @ e)
        # T_{ge} as product of unit relabeled translations (with inverses)
        M = np.eye(N)
        for b in range(3):
            Tb = W[trans[b]]
            M = M @ (Tb if ge[b] == 1 else (Tb.T if ge[b] == -1 else np.eye(N)))
        mix.add(scal(W[g] @ W[tg] @ W[g].T @ M.T))
print("   turn-translation relations W_g T_e W_g^-1 T_ge^-1: %s" % sorted(mix, key=lambda v: (v is None, v)))
ev = np.linalg.eigvalsh(h)
print("   KS one-particle spectrum: min %.4f max %.4f, symmetric: %s, distinct |E| levels %d"
      % (ev.min(), ev.max(), np.allclose(np.sort(ev), np.sort(-ev)), len(set(np.round(np.abs(ev), 8)))))

# ---------- (B) hop-only form under relabelings of exact turns ----------
print("(B) hop-only (XY) form under relabelings of exact turns; glued form")
def bond_op(B):
    return sum(B[a, b] * np.kron(PAUL[a + 1], PAUL[b + 1]) for a in range(3) for b in range(3))
vecs = []
hxy = bond_op(np.diag([1.0, 1.0, 0.0]))
cols = []
for a in range(3):
    cols.append((hxy @ np.kron(PAUL[a + 1], I2) - np.kron(PAUL[a + 1], I2) @ hxy).ravel())
for a in range(3):
    cols.append((hxy @ np.kron(I2, PAUL[a + 1]) - np.kron(I2, PAUL[a + 1]) @ hxy).ravel())
Mc = np.array(cols).T
sv = np.linalg.svd(Mc, compute_uv=False)
null = np.linalg.svd(Mc)[2][-int(np.sum(sv < 1e-10)):] if np.sum(sv < 1e-10) else []
print("   XY bond: linear conserved charges m_x.s_x + m_y.s_y: null-space dim %d, vector %s"
      % (int(np.sum(sv < 1e-10)), np.round(null[0], 6).tolist() if len(null) else None))
best = 0
for n in [np.array(v, float) for v in itertools.product(range(-2, 3), repeat=3) if any(v)]:
    cnt = sum(1 for k in range(24) if np.allclose(ROT[k] @ n, n) or np.allclose(ROT[k] @ n, -n))
    best = max(best, cnt)
print("   largest number of turns about a place keeping an axis (up to sign): %d of 24" % best)
ss = bond_op(np.eye(3))
print("   glued form: spectra of s.s %s and -s.s %s (no on-site relabeling maps one to the other)"
      % (np.round(np.linalg.eigvalsh(ss), 6).tolist(), np.round(np.linalg.eigvalsh(-ss), 6).tolist()))

# ---------- (C) one-part charged hop ----------
print("(C) one-part charged hop through a spin-1/2 link")
def frame(d):
    a = AXIS[d]; b = (a + 1) % 3; c = (a + 2) % 3; s = SIGN[d]
    F = np.zeros((3, 3)); F[a, 0] = s; F[b, 1] = 1; F[c, 2] = s
    assert abs(np.linalg.det(F) - 1) < 1e-12
    return F
def phase(A, B):
    c = np.vdot(B, A) / np.vdot(B, B)
    return c, np.linalg.norm(A - c * B) / np.linalg.norm(A)
O = {d: raise_out(d) for d in range(6)}
# exact Q3: quarter turn about the link's own axis (fixes the link, the corner v and v + delta)
for d in (0, 2, 4):
    U = su2_of_rot(ROT[C4[AXIS[d]]])
    c, r = phase(U @ O[d] @ U.conj().T, O[d])
    print("   Q3: quarter turn about the %s link maps its outward raising operator to (%.3f%+.3fi) x itself (residual %.0e)"
          % (NAMES[d], c.real, c.imag, r))
# random frame changes of Q3 (non-Clifford): the link's frame V, operator V O V^dag, action V U V^dag
worst = 0.0; phs = set()
for _ in range(200):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    Vf = q[0] * I2 - 1j * (q[1] * SX + q[2] * SY + q[3] * SZ)
    d = int(rng.choice([0, 2, 4]))
    U = su2_of_rot(ROT[C4[AXIS[d]]])
    Ub = Vf @ U @ Vf.conj().T                      # frame-changed action on the link
    Ob = Vf @ O[d] @ Vf.conj().T                   # frame-changed raising operator
    c, r = phase(Ub @ Ob @ Ub.conj().T, Ob)
    phs.add((round(c.real, 9), round(c.imag, 9))); worst = max(worst, r)
print("   200 random (non-Clifford) frame changes of Q3: phases seen %s, residual %.0e" % (sorted(phs), worst))
print("   corner with one qubit under a soldered-class action: an invariant charge axis would need R_g n = +-n for all 24 turns: none (max stabilizer of an axis = %d)" % best)
# looser link action: frame maps, S_g(g d) = F_{gd} F_d^-1 (links do not turn about their own axis)
Og = GROUPS['O (24 turns)']
cyc = 0.0; hop_ph = set(); exact_twist = set()
for g in Og:
    for hh in Og:
        for d in range(6):
            Sg = lambda gg, dd: frame(PERM[gg][dd]) @ frame(dd).T
            lhs = Sg(MUL[g][hh], d); rhs = Sg(g, PERM[hh][d]) @ Sg(hh, d)
            cyc = max(cyc, np.linalg.norm(lhs - rhs))
for g in Og:
    for d in range(6):
        S = frame(PERM[g][d]) @ frame(d).T
        U = su2_of_rot(S)
        c, r = phase(U @ O[d] @ U.conj().T, O[PERM[g][d]])
        hop_ph.add((round(c.real, 9), round(c.imag, 9)))
        if PERM[g][d] == d:
            exact_twist.add(key(np.round(S @ ROT[g].T).astype(int)))
print("   looser link action: group-law residual %.0e; outward raising maps to outward raising with phases %s" % (cyc, sorted(hop_ph)))
print("      the twist relative to Q3 on a link's own stabilizer undoes the turn about its axis: %d distinct twists" % len(exact_twist))
# Gauss law on (corner v, link, corner v+delta): G_v = n_v - E_out, G_w = n_w + E_out (w = v+delta), E_out = s*sigma^a/2
d = 0
nv = np.kron(np.kron((I2 + SZ) / 2, I2), I2); nw = np.kron(np.kron(I2, I2), (I2 + SZ) / 2)
Eout = np.kron(np.kron(I2, SIGN[d] * PAUL[AXIS[d] + 1] / 2), I2)
sp = np.array([[0, 1], [0, 0]], dtype=complex); sm = sp.T.copy()
t = np.kron(np.kron(sp, O[d]), sm)              # charge moves from v+delta to v, outward field up
Gv = nv - Eout; Gw = nw + Eout
print("   Gauss law: ||[G_v, t]|| = %.1e, ||[G_(v+d), t]|| = %.1e (t nonzero: %s)"
      % (np.linalg.norm(Gv @ t - t @ Gv), np.linalg.norm(Gw @ t - t @ Gw), np.linalg.norm(t) > 0))
# ring terms at a vertex: product of four outward/inward raising operators around a plaquette
# phases under the looser action are identically 1 by construction; under exact Q3 compute them.
ring_ph = set()
for a, b in [(0, 1), (1, 2), (2, 0)]:
    for g in Og:
        # plaquette spanned by +e_a, +e_b at v: links (v,+a) out, (v+a,+b) out-of-(v+a), (v+b,+a) reversed, (v,+b) reversed
        # under a turn about v the plaquette's four links rotate; the soldered action rotates each link qubit by R_g.
        U = su2_of_rot(ROT[g])
        da, db = 2 * a, 2 * b                    # +e_a, +e_b direction indices
        ops_src = [O[da], O[db], O[da].conj().T, O[db].conj().T]   # raise along +a, +b; lower along +a, +b (circulation)
        ga, gb = PERM[g][da], PERM[g][db]
        ops_tgt = [O[ga], O[gb], O[ga].conj().T, O[gb].conj().T]
        tot = 1.0 + 0j; ok = True
        for os_, ot in zip(ops_src, ops_tgt):
            c, r = phase(U @ os_ @ U.conj().T, ot)
            if r > 1e-9:
                ok = False
            tot *= c
        if ok:
            ring_ph.add((round(tot.real, 9), round(tot.imag, 9)))
print("   exact Q3, ring (two raising, two lowering, parallel pairs) phases under the 24 turns: %s" % sorted(ring_ph))
print("done")
