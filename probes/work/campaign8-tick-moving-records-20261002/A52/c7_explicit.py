"""A52 c7: the explicit covariant rule for T_f, and the decorated ring term on the uniform background."""
import signal
signal.alarm(60)
import numpy as np
from a52lib import *

def R120(f):
    """right-handed 120-degree turn about the body diagonal f (as an index into ROT)."""
    fn = np.array(f) / np.sqrt(3)
    for g in range(24):
        R = ROT[g].astype(float)
        if np.allclose(R @ fn, fn) and not np.allclose(R, np.eye(3)):
            # right-handed by 120 deg: R e x e' has positive overlap with f for e perpendicular to f
            e = np.cross(fn, [1, 0, 0]); e /= np.linalg.norm(e)
            if np.dot(np.cross(e, R @ e), fn) > 0:
                return g
def rule(f):
    g = R120(f); T = [[0] * 6 for _ in range(6)]
    for i in range(6):
        si = np.dot(f, DIRS[i])
        for j in range(6):
            if j == i: continue
            sj = np.dot(f, DIRS[j])
            if (si > 0 > sj) or (np.sign(si) == np.sign(sj) and PERM[g][i] == j):
                T[i][j] = 1
    return T
Tof, _ = family(ALL_C3_T[0])
print("explicit rule == transported T0 for all 8 body diagonals:", all(rule(f) == Tof[f] for f in BD))
print("rule is a tournament for all f:", all(is_tournament(rule(f)) for f in BD))
cov = all(transport_T(g, rule(f)) == rule(act_vec(g, f)) for g in range(24) for f in BD)
print("rule covariant under the 24 turns:", cov)
tor = Torus(3)
recs = {v: F0 for v in tor.corners}
H = [hop_string(tor, l, recs, Tof) for l in range(tor.n)]
v0 = (0, 0, 0)
for p in [(v0, 0, 1), (v0, 0, 2), (v0, 1, 2)]:
    P = (0, 0, 0)
    for (l, *_r) in tor.plaq_loop(p):
        P = pmul(P, H[l])
    loop = {l for (l, *_r) in tor.plaq_loop(p)}
    offs = []
    for q in range(tor.n):
        if (P[1] >> q) & 1 and q not in loop:
            # name it by (corner of the plaquette, leg)
            for (l, a, i, b, ip) in tor.plaq_loop(p):
                for c in (a,):
                    for j in range(6):
                        if tor.link(c, j) == q:
                            offs.append("%s%s" % (str(tuple(int(t) for t in c)), NAMES[j]))
    print("plaquette at %s in plane %s: off-loop field factors of the decorated ring: %s" % (v0, "xyz"[p[1]] + "xyz"[p[2]], sorted(set(offs))))
print("done")
