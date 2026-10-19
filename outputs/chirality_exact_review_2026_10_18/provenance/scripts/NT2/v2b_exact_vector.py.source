"""V2b: explicit rational negative vector for the V2 pool (first-order lemma: v = (1, beta, 1), 0 < sum v < 2 s^2/w^2),
and the scaling statement (box4 is homogeneous of degree 3, so the same pool scaled by delta/0.6 is negative for
every 0 < delta < pi/4)."""
from fractions import Fraction as Fr
import itertools
def box4_exact(sig, a):
    tot = Fr(0)
    for eps in itertools.product((1, -1), repeat=4):
        s = sig + sum(Fr(e) * ai for e, ai in zip(eps, a)) / 2
        if s > 0:
            tot += (eps[0] * eps[1] * eps[2] * eps[3]) * s ** 3 / 6
    return tot
for d in (Fr(3, 10), Fr(3, 5), Fr(3, 4)):
    w = 2 * d; e = d / 12; S = [-d * 11 / 12, Fr(0), d * 11 / 12]
    cfg = [(x, s) for x in (Fr(0), e) for s in S]
    K = [[box4_exact(c1[1] - c2[1], [w - abs(c1[0] - c2[0])] * 2 + [w, w]) for c2 in cfg] for c1 in cfg]
    for beta in (Fr(-179, 100), Fr(-9, 5), Fr(-17, 10)):
        v = [Fr(1), beta, Fr(1)]; vec = v + [-z for z in v]
        q = sum(vec[i] * K[i][j] * vec[j] for i in range(6) for j in range(6))
        nrm = sum(z * z for z in vec) * K[0][0]
        print(f"delta={d}: beta={beta}: v^T K v = {q}  ({float(q):+.4e}; relative to |v|^2 K_aa: {float(q/nrm):+.3e})")
