#!/usr/bin/env python3
"""C6 part C: illustration (not a proof; the proof is in the report) that an iid-priority formation
rule cannot register a block superlattice.

Rule (in the B3 class, range 4 in l_inf, from an empty start): at its iid activation time a site
becomes a block centre iff no earlier-formed site within l_inf distance 4 is a centre (so centres are at least 5 apart).  This is the
most block-favouring local rule one can write: it produces a maximal packing of disjoint 5x5x5 blocks.  We
measure the registration amplitudes |S(Q)| = |mean_centres exp(i Q.x)| for the 5Z^3 superlattice
momenta Q = 2pi(a,b,c)/5 != 0.  Registration (a perfect or long-range ordered block lattice) would
give |S(Q)| = O(1); a mixing field gives |S(Q)| ~ N_c^(-1/2).

Exact arithmetic (dimension bound in the report): a corner site's even mode algebra needs >= 12
qubits, so rung-1 site density <= 1/12; the smallest cubic block is 3^3 = 27 (12 modes) / 4^3 = 64
(48 BKSF qubits); the repo's equivariant placement uses 5^3 = 125.
"""
import itertools, sys
import numpy as np

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


check("smallest integer cubic block holding 12 logical modes is 3 (27 >= 12 > 8)", min(a for a in range(1, 9) if a ** 3 >= 12) == 3)
check("smallest integer cubic block holding the 48 BKSF qubits is 4 (64 >= 48 > 27)", min(a for a in range(1, 9) if a ** 3 >= 48) == 4)

L = 40
rng = np.random.default_rng(0)
amps = []
dens = []
for trial in range(4):
    order = rng.permutation(L ** 3)
    centre = np.zeros((L, L, L), bool)
    offs = np.array([o for o in itertools.product(range(-4, 5), repeat=3)])
    for s in order:
        x, y, z = s // (L * L), (s // L) % L, s % L
        nb = (np.array([x, y, z]) + offs) % L
        if not centre[nb[:, 0], nb[:, 1], nb[:, 2]].any():
            centre[x, y, z] = True
    pts = np.argwhere(centre)
    dens.append(len(pts) / L ** 3)
    Qs = [2 * np.pi * np.array(q) / 5 for q in itertools.product(range(5), repeat=3) if any(q)]
    amps.append(max(abs(np.exp(1j * pts @ Q).mean()) for Q in Qs))
    print(f"  trial {trial}: centres {len(pts)} (density {len(pts)/L**3:.5f} vs perfect block lattice 1/125 = 0.008),"
          f" max_Q |S(Q)| over the 124 superlattice momenta = {amps[-1]:.4f}; 1/sqrt(N_c) = {1/np.sqrt(len(pts)):.4f}")
# L = 40 is a multiple of 5, so a perfect block lattice would give |S| = 1 at every superlattice Q
print(f"FINDING: max registration amplitude {max(amps):.4f} (perfect registration = 1)")
check("the formed packing has no block registration: max |S(Q)| < 10/sqrt(N_c) in every trial (perfect lattice gives 1)",
      all(a < 10 / np.sqrt(d * L ** 3) for a, d in zip(amps, dens)))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
