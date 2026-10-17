"""(2) Levin-Wen T-junction sign for all 20 triples of straight legs.
Legs W_d = product of edge operators A along a straight path from o in
direction d (length l).  Sign = phase in W1 W2 W3 = s W3 W2 W1 (computed
directly by exact multiplication; equals c12 c13 c23)."""
import itertools
from mpd_core import *

ok_all = True


def leg(lat, o, d, l):
    a = d % 3
    p = (0, 0, 0)
    labs = []
    for t in range(l):
        if d < 3:
            v = tuple(o[i] + t * DIRS[a][i] for i in range(3))
        else:
            v = tuple(o[i] - (t + 1) * DIRS[a][i] for i in range(3))
        labs += lat.edge_labels(v, a)
    return lat.mono(labs)


for L, l in [(5, 2), (6, 2), (7, 3), (10, 4)]:
    lat = Lattice(L)
    o = (0, 0, 0)
    sec = all_sectors()[0]
    S = [lat.to_pauli(lat.plaq_mono(v, a, b)) for v in lat.all_sites() for (a, b) in ORIENTS]
    Bs = [lat.to_pauli(lat.B_mono(v)) for v in lat.all_sites()]
    legs = {}
    good = True
    for d in range(6):
        W = leg(lat, o, d, l)
        legs[d] = W
        good &= not any(anticommute(W, s) for s in S)
        flipped = {lat.coords(i) for i, b in enumerate(Bs) if anticommute(W, b)}
        end = tuple((o[i] + l * DIRS[d][i]) % L for i in range(3))
        good &= flipped == {o, end}
    signs = []
    for tri in itertools.combinations(range(6), 3):
        W1, W2, W3 = (legs[d] for d in tri)
        lhs = mul(mul(W1, W2), W3)
        rhs = mul(mul(W3, W2), W1)
        assert lhs[0] == rhs[0] and lhs[1] == rhs[1]
        s = 1 if (lhs[2] - rhs[2]) % 4 == 0 else -1
        c = 1
        for P, Q in [(W1, W2), (W1, W3), (W2, W3)]:
            c *= -1 if anticommute(P, Q) else 1
        assert c == s
        signs.append(s)
    ok = good and len(signs) == 20 and all(s == -1 for s in signs)
    ok_all &= ok
    print("L=%d leg=%d: legs commute with all S_p & flip only {o,end}: %s; "
          "T-junction signs: %d of 20 are -1 -> %s" % (L, l, good, signs.count(-1), "PASS" if ok else "FAIL"))

# Control: the same test with bosonic legs (products of Z on qubit 1 along a
# path, a toric-code-like string) must give +1, to show the test discriminates.
lat = Lattice(6)
def zleg(d, l):
    a = d % 3
    z = 0
    for t in range(l + 1):
        v = tuple((t if d < 3 else -t) * DIRS[a][i] for i in range(3))
        if t > 0:
            z |= 1 << (3 * lat.site(v))
    return (0, z, 0)
cs = []
for tri in itertools.combinations(range(6), 3):
    W = [zleg(d, 2) for d in tri]
    c = 1
    for P, Q in itertools.combinations(W, 2):
        c *= -1 if anticommute(P, Q) else 1
    cs.append(c)
print("control (commuting bosonic strings): %d of 20 are +1" % cs.count(1))
print("OVERALL", "PASS" if ok_all else "FAIL")
