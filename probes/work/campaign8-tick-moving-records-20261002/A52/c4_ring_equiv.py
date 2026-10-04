"""A52 c4: (a) records are invisible: a CZ circuit on a corner's star maps tournament T to T' exactly
(symbolic on the torus; dense on the star).  (b) light in the charge-free sector: is the decorated ring
term (loop product of the record-conditioned hops) equivalent to the bare ring term by a diagonal sign
change?  BFS over ice configurations reachable by ring flips on small coarse tori, U(1) spin-1/2 links."""
import signal, sys, itertools
signal.alarm(115)
import numpy as np
from collections import deque
from a52lib import *

rng = np.random.default_rng(404)
# ---------- (a) CZ equivalence ----------
tor = Torus(4)
def q_of(T, T2):
    return [(j, k) for j in range(6) for k in range(j + 1, 6) if T[j][k] != T2[j][k]]
def apply_cz(A, pairs_links):
    x, z, p = A
    for (a, b) in pairs_links:
        if (x >> a) & 1: z ^= 1 << b
        if (x >> b) & 1: z ^= 1 << a
    return (x, z, p)
bad = 0; tot = 0; ncz = []
for trial in range(6):
    Tof1, _ = family(ALL_C3_T[rng.integers(32)]); Tof2, _ = family(ALL_C3_T[rng.integers(32)])
    r1 = {v: BD[rng.integers(8)] for v in tor.corners}; r2 = {v: BD[rng.integers(8)] for v in tor.corners}
    H1 = [hop_string(tor, l, r1, Tof1) for l in range(tor.n)]
    H2 = [hop_string(tor, l, r2, Tof2) for l in range(tor.n)]
    cz = []
    for v in tor.corners:
        cz += [(tor.link(v, j), tor.link(v, k)) for (j, k) in q_of(Tof1[r1[v]], Tof2[r2[v]])]
    ncz.append(len(cz))
    for l in range(tor.n):
        tot += 1; bad += int(apply_cz(H1[l], cz)[:2] != H2[l][:2])
print("(a) CZ circuit V (pairs of star links where the two tournaments disagree) maps every hop of one random")
print("    record background / tournament choice to the other's: mismatches %d of %d (CZ gates used: %s)" % (bad, tot, ncz))
# dense on the star: V t_i[f] V^dag = t_i[f']  (true U(1) operators)
SITES = [tuple(d) for d in DIRS]
def kron6(op):
    out = np.array([[1.0 + 0j]])
    for s in SITES:
        out = np.kron(out, op.get(s, I2))
    return out
def star_hop(T, i):
    op = {SITES[i]: raise_out(i)}
    for j in range(6):
        if j != i and T[i][j]:
            op[SITES[j]] = PAUL[AXIS[j] + 1]
    return kron6(op)
def CZ(j, k):
    Ej = kron6({SITES[j]: PAUL[AXIS[j] + 1]}); Ek = kron6({SITES[k]: PAUL[AXIS[k] + 1]})
    return (np.eye(64) + Ej + Ek - Ej @ Ek) / 2
Tof, _ = family(ALL_C3_T[0]); worst = 0.0
for f2 in BD:
    V = np.eye(64)
    for (j, k) in q_of(Tof[F0], Tof[f2]):
        V = V @ CZ(j, k)
    for i in range(6):
        worst = max(worst, np.linalg.norm(V @ star_hop(Tof[F0], i) @ V.conj().T - star_hop(Tof[f2], i)))
print("    dense star check (U(1) raise operators, CZ in the field basis), f0 -> each of 8 records: max residual %.1e" % worst)

# ---------- (b) ring term in the charge-free sector ----------
def run_torus(Ls, Tof, recs_kind, cap=250000):
    t = Torus(Ls)
    recs = {v: F0 for v in t.corners} if recs_kind == 'uniform' else {v: BD[rng.integers(8)] for v in t.corners}
    # field basis: bit 1 <=> field along +axis is -1.  start: e(a-link at v) = (-1)^{sum_{b != a} v_b / 2}
    st0 = 0
    for l in range(t.n):
        v, i, w, ip = t.ends(l); a = i // 2
        e = (-1) ** (sum(v[b] // 2 for b in range(3) if b != a))
        if e == -1: st0 |= 1 << l
    # Gauss check of the start: outward field sum zero at every corner
    def div(st, v):
        s = 0
        for j in range(6):
            l = t.link(v, j); e = -1 if (st >> l) & 1 else 1
            s += e * SIGN[j]
        return s
    assert all(div(st0, v) == 0 for v in t.corners)
    # hops: decoration sets per link (field factors at both ends), and loop data
    dec = []
    for l in range(t.n):
        x, z, _ = hop_string(t, l, recs, Tof)
        dec.append(z)
    loops = []
    for p in t.plaqs:
        lp = t.plaq_loop(p)   # (link, from, leg_from, to, leg_to); hop raises outward field from 'from'
        loops.append([(l, SIGN[i]) for (l, v, i, w, ip) in lp])
    def apply_loop(st, loop, dagger):
        """L_p = t4 t3 t2 t1 (t1 acts first); returns (new_state, sign) or None.  Raise of outward field
        s*e on link l: requires s*e = -1 before; the raise matrix element is 1 in this basis."""
        seq = loop if not dagger else loop[::-1]
        sign = 1
        for (l, s) in seq:
            e = -1 if (st >> l) & 1 else 1
            want = -1 if not dagger else 1
            if s * e != want:
                return None
            # field factors of this hop act first (they commute with its own raise)
            sign *= -1 if bin(st & dec[l]).count('1') % 2 else 1
            st ^= 1 << l
        return st, sign
    def apply_bare(st, loop, dagger):
        seq = loop if not dagger else loop[::-1]
        for (l, s) in seq:
            e = -1 if (st >> l) & 1 else 1
            if s * e != (-1 if not dagger else 1):
                return None
            st ^= 1 << l
        return st, 1
    chi = {st0: 1}; q = deque([st0]); edges = 0; incons = 0; neg = 0
    while q and len(chi) < cap:
        st = q.popleft()
        for loop in loops:
            for dg in (False, True):
                r = apply_loop(st, loop, dg)
                rb = apply_bare(st, loop, dg)
                assert (r is None) == (rb is None)
                if r is None:
                    continue
                st2, sg = r; edges += 1; neg += sg < 0
                if st2 in chi:
                    if chi[st2] != chi[st] * sg:
                        incons += 1
                else:
                    chi[st2] = chi[st] * sg; q.append(st2)
    full = not q
    return len(chi), edges, neg, incons, full, t

for Ls in [(2, 2, 2), (2, 2, 3), (2, 2, 4)]:
    for k in (0, 31):
        Tof, _ = family(ALL_C3_T[k])
        for rk in ('uniform', 'random'):
            n, e, neg, inc, full, t = run_torus(Ls, Tof, rk)
            print("(b) torus %s T%-2d %-7s: states %7d%s, flip edges %8d, negative-sign edges %7d, sign inconsistencies %d" % (
                Ls, k, rk, n, '' if full else ' (capped)', e, neg, inc))
print("done")
