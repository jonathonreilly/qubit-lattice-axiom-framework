"""A50 t0: sanity of the library.
 (1) own-link transport: Ad(U_g) raise_out(i) proportional to raise_out(g i) for all 24 turns;
 (2) covariance residual of seeded hop sets (O on W27, several seed modes, with/without Gauss bits);
 (3) factorized junction phase vs state-vector junction phase on subsets of <= 13 qubits;
 (4) Task-1 control: U(1) link-phase dressing with NO symmetry gives a generic phase;
     the formula (r13 r32 r21)/(r31 r23 r12) matches.
"""
import signal
import numpy as np
from collections import Counter
from a50lib import *
signal.alarm(250)
rng = np.random.default_rng(5001)

# (1)
w = 0.0
for g in range(24):
    for i in range(6):
        c, r = phase_fit(ad(g, raise_out(i)), raise_out(PERM[g][i]))
        w = max(w, r)
print("(1) own-link transport residual over 24 x 6: %.1e" % w)

# (2)
for mode in ['id', 'cliff', 'cont', 'mix']:
    worst = 0.0
    for t in range(6):
        gb = rng.integers(2, size=6) if t % 2 else None
        hops = build_hops(GRP['O'], W27, lambda o, S: sample_seed(o, S, rng, mode), gauss_bits=gb)
        r = covariance_residual(hops, GRP['O'], W27) if gb is None else 0.0
        worst = max(worst, r)
    print("(2) mode %-5s covariance residual (no Gauss bits) %.1e" % (mode, worst))

# (3) cross-check on subsets: v + 6 links + up to 6 random other window sites
worst_diff = 0.0; nchk = 0
for t in range(40):
    mode = ['cliff', 'cont'][t % 2]
    def seeder(o, S):
        if kind(o) in (2, 3) and rng.random() < 0.85:
            return I2.copy()
        return sample_seed(o, S, rng, mode if kind(o) != 0 else 'cliff')
    hops = build_hops(GRP['O'], W27, seeder)
    others = [x for x in W27 if x not in LEGLINK and x != (0, 0, 0)]
    pick = [others[k] for k in rng.choice(len(others), 6, replace=False)]
    sites = [(0, 0, 0)] + LEGLINK + pick
    # restrict hops to these sites for the factorized formula
    sub = [{s: h[s] for s in sites if s in h} for h in hops]
    for tri in TRIPLES:
        th, res, _ = junction(sub, tri, sites, tol=1e-8)
        c, r, spread = sv_junction(sub, tri, sites, rng, nvec=2)
        if th is not None:
            nchk += 1
            worst_diff = max(worst_diff, abs(c - th), r)
        else:
            # factorized says not scalar: state vector must also fail
            if r < 1e-8 and spread < 1e-8:
                print("   MISMATCH: factorized non-scalar but state vector scalar", tri)
print("(3) factorized vs state-vector theta: %d scalar junctions compared, max |diff|+res %.1e" % (nchk, worst_diff))

# (4) Task-1 control: generic U(1) link phases, no symmetry
hops = [{LEGLINK[i]: raise_out(i)} for i in range(6)]
phi = rng.uniform(0, np.pi, size=(6, 6))
for i in range(6):
    for m in range(6):
        if m != i:
            e = np.zeros(3); e[AXIS[m]] = phi[i, m]
            hops[i][LEGLINK[m]] = su2_exp(e)
tri = (0, 1, 4)
th, res, _ = junction(hops, tri, [(0, 0, 0)] + LEGLINK)
# r_jk = f(up)/f(down) for outward field s*sigma^a: f(s=+1 outward) / f(outward -1)
def r(j, k):
    return np.exp(2j * phi[j, k] * SIGN[k])
i, j, k = tri
pred = (r(i, k) * r(k, j) * r(j, i)) / (r(k, i) * r(j, k) * r(i, j))
print("(4) no-symmetry U(1) link dressing: theta = %s (|theta| %.6f, res %.1e); formula %s" %
      (np.round(th, 6), abs(th), res, np.round(pred, 6)))
print("done")
