"""A52 c2: exact symbolic (Pauli / GF(2)) checks of the record-conditioned hop set on a coarse torus.
Z2 version of the hop: X_l (transverse flip; same commutation signs as the U(1) raise) x field factors."""
import signal, sys, itertools
signal.alarm(110)
import numpy as np
from a52lib import *

L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
tor = Torus(L)
rng = np.random.default_rng(52)
print("coarse torus %s: %d corners, %d links, %d plaquettes" % (tor.L, len(tor.corners), tor.n, len(tor.plaqs)))

def build(recs, Tof):
    return [hop_string(tor, l, recs, Tof) for l in range(tor.n)]

def share_corner(l, m):
    a = tor.ends(l); b = tor.ends(m)
    return len({a[0], a[2]} & {b[0], b[2]}) > 0

PAIRS_SHARE = {}
def algebra_violations(H):
    bad = 0; nsh = 0
    for l in range(tor.n):
        for m in range(l + 1, tor.n):
            sh = share_corner(l, m)
            nsh += sh
            if anticomm(H[l], H[m]) != int(sh):
                bad += 1
    return bad, nsh

def junctions(H, recs):
    """all 20 triples at every corner, from the pair signs; returns Counter of theta."""
    from collections import Counter
    cnt = Counter()
    for v in tor.corners:
        ls = [tor.link(v, i) for i in range(6)]
        for i, j, k in itertools.combinations(range(6), 3):
            s = anticomm(H[ls[i]], H[ls[j]]) + anticomm(H[ls[i]], H[ls[k]]) + anticomm(H[ls[j]], H[ls[k]])
            cnt[-1 if s % 2 else 1] += 1
    return cnt

def gauss_check(H):
    bad = 0
    G = {v: gauss_string(tor, v) for v in tor.corners}
    for l in range(tor.n):
        v, i, w, ip = tor.ends(l)
        for u in tor.corners:
            if anticomm(H[l], G[u]) != int(u in (v, w)):
                bad += 1
    return bad

def covariance(H, recs, Tof, centres):
    bad = 0; tot = 0
    for c in centres:
        for g in range(24):
            recs_g = {tor.turn(g, v, c): act_vec(g, f) for v, f in recs.items()}
            Hg = build(recs_g, Tof)
            for l in range(tor.n):
                img = turn_string(tor, g, H[l], c)
                lg = tor.lidx[tor.turn(g, tor.links[l], c)]
                tot += 1
                if img[0] != Hg[lg][0] or img[1] != Hg[lg][1]:
                    bad += 1
    # translations by 2e_a
    for a in range(3):
        sh = [0, 0, 0]; sh[a] = 2
        recs_t = {tor.wrap(np.array(v) + sh): f for v, f in recs.items()}
        Ht = build(recs_t, Tof)
        for l in range(tor.n):
            x, z, _ = H[l]
            def tr(bits):
                out = 0
                for q in range(tor.n):
                    if (bits >> q) & 1:
                        out |= 1 << tor.lidx[tor.wrap(np.array(tor.links[q]) + sh)]
                return out
            lt = tor.lidx[tor.wrap(np.array(tor.links[l]) + sh)]
            tot += 1
            if tr(x) != Ht[lt][0] or tr(z) != Ht[lt][1]:
                bad += 1
    return bad, tot

def loop_products(H):
    """S_p = product of the four hops around p (loop order), as Pauli string with phase."""
    S = []
    for p in tor.plaqs:
        P = (0, 0, 0)
        for (l, *_r) in tor.plaq_loop(p):
            P = pmul(P, H[l])
        S.append(P)
    return S

def loop_report(H, label):
    S = loop_products(H)
    G = [gauss_string(tor, v) for v in tor.corners]
    sq = {pmul(P, P)[2] for P in S}
    bad_h = sum(anticomm(P, h) for P in S for h in H)
    bad_g = sum(anticomm(P, g) for P in S for g in G)
    bad_s = sum(anticomm(S[a], S[b]) for a in range(len(S)) for b in range(a + 1, len(S)))
    # off-loop field factors of S_p
    offs = []
    for p, P in zip(tor.plaqs, S):
        loop = {l for (l, *_r) in tor.plaq_loop(p)}
        offs.append(sum(1 for q in range(tor.n) if (P[1] >> q) & 1 and q not in loop))
    # bare ring X-loop vs off-loop hops
    nb = 0; nbp = 0
    for p in tor.plaqs:
        loop = [l for (l, *_r) in tor.plaq_loop(p)]
        W = (sum(1 << l for l in loop), 0, 0)
        k = sum(anticomm(W, H[m]) for m in range(tor.n) if m not in loop)
        nb += k; nbp += int(k > 0)
    # cube relation: product of the 6 face loops of each coarse cube (faces at c and c+2e_k)
    pidx = {p: k for k, p in enumerate(tor.plaqs)}
    cube_vals = set()
    for c in tor.corners:
        P = (0, 0, 0)
        for (a, b), k in [((0, 1), 2), ((0, 2), 1), ((1, 2), 0)]:
            sh = [0, 0, 0]; sh[k] = 2
            P = pmul(P, S[pidx[(c, a, b)]])
            P = pmul(P, S[pidx[(tor.wrap(np.array(c) + sh), a, b)]])
        assert P[0] == 0 and P[1] == 0, "cube product not scalar"
        cube_vals.add(P[2])
    # plane relations: all plaquettes of one orientation in one layer
    plane_vals = {}
    for (a, b), k in [((0, 1), 2), ((0, 2), 1), ((1, 2), 0)]:
        P = (0, 0, 0)
        for p in tor.plaqs:
            if (p[1], p[2]) == (a, b) and p[0][k] == 0:
                P = pmul(P, S[pidx[p]])
        plane_vals[(a, b)] = P[2] if (P[0] == 0 and P[1] == 0) else 'not scalar'
    print("   %s: S_p^2 phases %s; S_p anticommuting with hops %d, with Gauss %d, with other S %d" % (label, sq, bad_h, bad_g, bad_s))
    print("      off-loop field factors per S_p: min %d max %d; bare X-loops anticommuting with an off-loop hop: %d of %d plaquettes (%d pairs)" % (min(offs), max(offs), nbp, len(tor.plaqs), nb))
    print("      cube relation (product of 6 faces) phases i^k, k in %s; plane products (i^k): %s" % (sorted(cube_vals), plane_vals))

T_list = ALL_C3_T
print("(a) uniform f0 background, all 32 C3 tournaments; (b) random body-diagonal backgrounds")
summary = []
for k, T0 in enumerate(T_list):
    Tof, conf = family(T0)
    assert conf == 0
    for bg in ('uniform', 'random'):
        if bg == 'uniform':
            recs = {v: F0 for v in tor.corners}
        else:
            if k % 8 != 0:
                continue
            recs = {v: BD[rng.integers(8)] for v in tor.corners}
        H = build(recs, Tof)
        bad, nsh = algebra_violations(H)
        jc = junctions(H, recs)
        gb = gauss_check(H)
        summary.append((k, bg, bad, dict(jc), gb))
print("   pair rule (anticommute iff share a corner) violations, junction counts, Gauss violations:")
agg = {}
for (k, bg, bad, jc, gb) in summary:
    agg.setdefault(bg, []).append((bad, tuple(sorted(jc.items())), gb))
for bg, lst in agg.items():
    print("      %-8s runs %2d: max violations %d; junction tallies %s; Gauss violations %d" % (
        bg, len(lst), max(x[0] for x in lst), sorted({x[1] for x in lst}), max(x[2] for x in lst)))
print("(c) covariance of the law as a function of the records (turns about a corner and a cube centre, translations)")
for k in (0, 13, 31):
    Tof, _ = family(T_list[k])
    for bg in ('uniform', 'random'):
        recs = {v: F0 for v in tor.corners} if bg == 'uniform' else {v: BD[rng.integers(8)] for v in tor.corners}
        H = build(recs, Tof)
        bad, tot = covariance(H, recs, Tof, [(0, 0, 0), (1, 1, 1)])
        print("   tournament %2d, %-7s background: covariance mismatches %d of %d hop images" % (k, bg, bad, tot))
# control: records NOT transformed (law with a fixed background tournament)
Tof, _ = family(T_list[0])
recs = {v: F0 for v in tor.corners}
H = build(recs, Tof)
bad = 0; tot = 0
for g in range(24):
    for l in range(tor.n):
        img = turn_string(tor, g, H[l])
        lg = tor.lidx[tor.turn(g, tor.links[l])]
        tot += 1; bad += int(img[1] != H[lg][1])
print("   control (records held fixed, not turned): mismatches %d of %d" % (bad, tot))
print("(d) loop products around plaquettes (Z2 version, exact phases)")
for k in (0, 31):
    Tof, _ = family(T_list[k])
    loop_report(build({v: F0 for v in tor.corners}, Tof), "T%d uniform" % k)
    loop_report(build({v: BD[rng.integers(8)] for v in tor.corners}, Tof), "T%d random " % k)
# bosonic control: no decorations
Hb = [(1 << l, 0, 0) for l in range(tor.n)]
jb = junctions(Hb, None)
print("   control, bare hops (no decorations): junction tally %s" % dict(jb))
print("done")
