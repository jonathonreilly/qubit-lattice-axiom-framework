"""R18-10 s4: planar (subsystem) conservation laws of the registered LOCAL dipole-conserving move set.
Claim (by inspection of the patterns, proved): every balanced flip conserves N_aa(plane x_a = c) for each diagonal type aa:
 - cube flips touch no diagonal slot;
 - each mu8 orientation contains two diagonal pairs; each pair lies in one plane perpendicular to its own index
   (xz-mu8: zz pair at equal z, xx pair at equal x), and a balanced flip is one-up-one-down on each pair.
So the 3L planar counts (equivalently the a-charge sum_{plane} gamma_a in every a-plane: sum_{x,y} (Gn)_z(x,y,z) = N_zz(z+1) - N_zz(z))
are conserved: the chain is NOT ergodic on the N-sector (Krylov sectors labelled by the diagonal planar profiles).
Checks: (i) the pattern geometry; (ii) the per-plane charge identity on random states; (iii) a run of the local chain:
diagonal planar profiles unchanged, face planar profiles N_xz(z) do change."""
import numpy as np
from common import PATTERNS, TYPES
from mc import *
from mc10 import sweeps_c, counts
from mcpair import sweeps_bias
for p in PATTERNS:
    diag = [(d, t) for d, t in p if t < 3]
    s = []
    for t in range(3):
        cs = sorted(set(int(d[t]) for d, tt in diag if tt == t))
        if any(tt == t for d, tt in diag): s.append("%s-slots: %d, plane coords along own axis %s" % (TYPES[t], sum(1 for d, tt in diag if tt == t), cs))
    print("pattern (types %s): %s" % (sorted(t for d, t in p), "; ".join(s) if s else "no diagonal slots"))
rng = np.random.default_rng(3); L = 6; V = L**3
for it in range(5):
    n = rng.integers(0, 2, (6, L, L, L)).astype(np.int64); g = charges(n, L)   # unconstrained integer Gn (mod-2 law not needed for the identity)
    lhs = g[2].sum(axis=(0, 1)); Nzz = n[2].sum(axis=(0, 1)); rhs = np.roll(Nzz, -1) - Nzz
    assert np.array_equal(lhs, rhs)
print("(ii) sum_{x,y} (Gn)_z(x,y,z) = N_zz(z+1) - N_zz(z): checked on 5 random label fields, L = 6")
S, GE, GN = move_tables(L); half = V//2
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); sweeps(n, g, L, 0.0, S, GE, GN, 50, 9, 1)
Nc = counts(n); fl = np.zeros_like(n); d = 0
while np.abs(Nc - half).sum() > 0 and d < 2000: sweeps_c(n, g, Nc, L, 0.0, S, GE, GN, 1, 20 + d, d % 2, 1, half, fl); d += 1
prof = lambda n: (n[0].sum(axis=(1, 2)), n[1].sum(axis=(0, 2)), n[2].sum(axis=(0, 1)), n[5].sum(axis=(0, 1)), n[5].sum(axis=(1, 2)))
P0 = prof(n)
for bU in [0.0, 1.0, 2.0]:
    sweeps_c(n, g, Nc, L, bU, S, GE, GN, 3000, 77, 1, 0, half, fl)
P1 = prof(n)
print("(iii) local chain, L = 6, 9000 sweeps (bU 0,1,2): N_xx(x) unchanged %s, N_yy(y) unchanged %s, N_zz(z) unchanged %s; N_xz(z) unchanged %s, N_xz(x) unchanged %s"
      % tuple(bool(np.array_equal(a, b)) for a, b in zip(P0, P1)))
print("      N_zz(z) profile:", P1[2], " N_xz(z) before/after:", P0[3], P1[3])
