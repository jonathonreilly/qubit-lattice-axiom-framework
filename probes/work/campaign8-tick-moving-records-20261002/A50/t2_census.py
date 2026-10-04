"""A50 t2_census: covariant product dressings on the 27-place window (corner, 6 edges,
12 faces, 8 cubes), exact soldered action of a group G (argv[1] in O, T, D2, C2z).
Seeds: one 2x2 unitary per orbit of the seed leg's stabilizer, invariant up to phase under the
place's stabilizer (links: field-diagonal), transported by the exact action; half the samples
also carry random Gauss factors B_v^{c_i}.  For each sample all 20 Levin-Wen junctions:
scalar or not, theta.  Prediction (lemma F''): under O every scalar T-junction has theta = +1.
"""
import signal, sys
import numpy as np
from collections import Counter
from a50lib import *
signal.alarm(285)
gname = sys.argv[1]
G = GRP[gname]
rng = np.random.default_rng({'O': 11, 'T': 12, 'D2': 13, 'C2z': 14}[gname])
NPER = int(sys.argv[2]) if len(sys.argv) > 2 else 1200
NONLEG = [x for x in W27 if x not in LEGLINK]

def dag(A):
    return np.conj(np.swapaxes(A, -1, -2))

def junctions_fast(hops, sites, tol=1e-9):
    A = [np.array([h.get(x, I2) for x in sites]) for h in hops]
    K = [kron6([h.get(LEGLINK[m], I2) for m in range(6)]) for h in hops]
    out = {}
    for tri in TRIPLES:
        i, j, k = tri
        W = dag(A[i]) @ A[j] @ dag(A[k]) @ A[i] @ dag(A[j]) @ A[k]
        lam = (W[:, 0, 0] + W[:, 1, 1]) / 2
        res = np.abs(W - lam[:, None, None] * I2).max()
        T1 = K[i] @ K[j].conj().T @ K[k]; T2 = K[k] @ K[j].conj().T @ K[i]
        c, rL = phase_fit(T1, T2)
        worst = max(res, rL)
        out[tri] = (c * np.prod(lam) if worst < tol else None, worst)
    return out

MODES = {
    'cliff-sparse': ('cliff', 0.7), 'cont-sparse': ('cont', 0.7),
    'cliff-dense': ('cliff', 0.0), 'cont-dense': ('cont', 0.0), 'axis-only': ('mix', 1.0)}

def r6(z):
    return complex(np.round(z.real, 6), np.round(z.imag, 6))

print("group %s (%d turns), window 27 places, %d samples per mode" % (gname, len(G), NPER))
cov_worst = 0.0
for mname, (base, p_id) in MODES.items():
    stats = Counter(); thT = Counter(); thC = Counter(); examples = {}
    for s in range(NPER):
        def seeder(o, S):
            if kind(o) in (2, 3) and rng.random() < p_id:
                return I2.copy()
            return sample_seed(o, S, rng, base)
        gb = rng.integers(2, size=6) if s % 2 else None
        hops = build_hops(G, W27, seeder, gauss_bits=gb)
        if s < 3 and gb is None:
            cov_worst = max(cov_worst, covariance_residual(hops, G, W27))
        J = junctions_fast(hops, NONLEG)
        tsc = all(J[t][0] is not None for t in T_TRI)
        asc = tsc and all(J[t][0] is not None for t in C_TRI)
        stats['n'] += 1
        if tsc:
            stats['T scalar'] += 1
            vals = Counter(r6(J[t][0]) for t in T_TRI)
            key_ = 'all +1' if set(vals) == {1 + 0j} else ('all -1' if set(vals) == {-1 + 0j} else 'mixed %s' % sorted(vals.items(), key=lambda z: z[0].real))
            thT[key_] += 1
            if key_ != 'all +1' and key_ not in examples:
                examples[key_] = s
        if asc:
            stats['all 20 scalar'] += 1
            cv = Counter(r6(J[t][0]) for t in C_TRI)
            thC['corner ' + ('all +1' if set(cv) == {1 + 0j} else ('all -1' if set(cv) == {-1 + 0j} else 'mixed'))] += 1
            if all(r6(J[t][0]) == -1 for t in TRIPLES):
                stats['all 20 = -1'] += 1
    print(" %-12s %s" % (mname, dict(stats)))
    print("              T-junction patterns: %s" % dict(thT))
    if thC:
        print("              corner patterns (all-20-scalar samples): %s" % dict(thC))
print("covariance residual (spot checks): %.1e" % cov_worst)
print("done")
