"""Attack on (4)/(6): is the pair-test sign an invariant of the charge anyon?
Pair-test sign lambda for several representatives of the SAME anyon pair
(charge at x and at Rx), and for purely local (trivial-sector) objects."""
AUDIT_TIMEOUT_SEC = 1800
import numpy as np
from mj import *
from rot import *

L = 6; lat = Lat(L); N = lat.N
g = generators(lat); gens = g['D'] + g['Pu'] + g['Pd'] + g['W']
G = StabGroup(gens)
groups = consistent_link_groups(); ML = matter_lifts()
C2s = [(i, R) for i, R in enumerate(ROTS) if round(np.trace(R)) == -1]
def cls(R): return 'axis' if any(R[a, a] == 1 for a in range(3)) else 'edge'
x0 = (1, 2, 0)
out = {}
for Gp in groups[:4]:
    for ri, R in C2s:
        x = x0; Rx = tuple(int(v) for v in R @ np.array(x))
        if lat.idx(Rx) == lat.idx(x): x = (2, 1, 1); Rx = tuple(int(v) for v in R @ np.array(x))
        sx, sRx = lat.idx(x), lat.idx(Rx)
        p = tuple(dir_perm(R))
        for ls in [y for y in Gp if y[0] == p]:
            for (q, D, M4) in ML[ri]:
                act = Action(lat, R, ls, M4)
                w, V = np.linalg.eig(D); e = V[:, 0]
                Sf = path_string(lat, x, Rx)
                cc = poly_mul(c_dag(N, sx, e), c_dag(N, sRx, e))
                bb = to_poly(mul(mono(N, [(sx, 0)]), mono(N, [(sRx, ls[0][0])])))
                cb = poly_mul(poly_mul(c_dag(N, sx, e), to_poly(mono(N, [(sx, 0)]))),
                              poly_mul(c_dag(N, sRx, e), to_poly(mono(N, [(sRx, ls[0][0])]))))
                reps = {
                    'charge pair: bare S_f                 [D flips]': Sf,
                    'charge pair: doublet c c S_f           [P flips]': poly_mul(cc, Sf),
                    'charge pair: flux-loop b b S_f         [4W loops]': poly_mul(bb, Sf),
                    'charge pair: doublet+flux c c b b S_f  [P + 4W]': poly_mul(poly_mul(cc, bb), Sf),
                    'LOCAL: c_e^dag(x) c_e^dag(Rx)          [D+P, trivial sector]': cc,
                    'LOCAL: b b                              [D+4W, trivial sector]': bb,
                    'LOCAL: (c^dag b)(c^dag b)               [P+4W, D=+1, trivial sector]': cb,
                }
                for k, A in reps.items():
                    lam, ab = pair_eig(G, act, A)
                    assert abs(ab - 1) < 1e-8, (k, ab)
                    out.setdefault(k, {}).setdefault(cls(R), set()).add(complex(np.round(lam, 8)))
for k, v in out.items():
    print(f'{k}: axis {sorted(v["axis"], key=abs)}  edge {sorted(v["edge"], key=abs)}')

# V(-1): identity rotation with matter lift -1 = global matter parity
iid = [i for i, R in enumerate(ROTS) if (R == np.eye(3)).all()][0]
for (q, D, M4) in ML[iid]:
    if q[0] < 0:
        act = Action(lat, ROTS[iid], (tuple(range(6)), (1,) * 6), M4)
        s = lat.idx((1, 1, 1))
        for name, A in [('c_up^dag(x)|vac>  (local; D+P flipped)', c_dag(N, s, np.array([1, 0]))),
                        ('c_up^dag(x) b_{x,+x}|vac> (local; D=+1 everywhere, P_up + 4W)',
                         poly_mul(c_dag(N, s, np.array([1, 0])), to_poly(mono(N, [(s, 0)])))),
                        ('doublet pair c c S_f |vac>', poly_mul(poly_mul(c_dag(N, s, np.array([1, 0])), c_dag(N, lat.idx((1, 1, 3)), np.array([0, 1]))), path_string(lat, (1, 1, 1), (1, 1, 3))))]:
            print('V(-1) eigenvalue on', name, ':', np.round(pair_eig(G, act, A)[0], 8))
