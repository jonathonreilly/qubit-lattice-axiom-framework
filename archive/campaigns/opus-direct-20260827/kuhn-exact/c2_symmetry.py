"""C2 -- the two reductions the production run relies on, both tested, not assumed:
   (a) Bloch spectrum symmetry  q -> -q, q_i -> -q_i, and (conformal only) q permutations
       => momentum_orbits() reproduces the full L^3 momentum sum;
   (b) eps -> -eps parity of the whole heat trace
       (conformal: eps -> -eps is the translation x0 -> x0 + L/(2n);
        TT:        same translation combined with the 1<->2 coordinate swap, and the
        Kuhn complex is invariant under coordinate permutations)
       => the 5-point eps derivative needs only eps = 0, h, 2h.
Non-axis (body-diagonal) stencil entries are nonzero at eps != 0 (C1b), so neither
symmetry is obvious a priori.
"""
import math, itertools
import numpy as np
from kx_base import (build, _bands, bloch_eigs, CH_P, N_MODE, momentum_orbits,
                     lat_trace, fmte)

L, n = 12, N_MODE
kk = 2 * math.pi * n / L
rng = np.random.default_rng(0)

print("=== C2a  Bloch spectrum symmetries  (L=%d, eps=0.1) ===" % L)
for name, P in CH_P.items():
    r = build(L, 0.1, P, kk)
    bd = _bands(L, r['stencil'])
    base = np.array([(2 * np.pi / L) * np.array([3.0, 5.0, 8.0])])
    ev0, herm = bloch_eigs(L, bd, r['mass'], base, C=r['C'], improve=True)
    ev0 = np.sort(ev0[0])
    tests = {
        "q -> -q          ": -base,
        "q1 -> -q1        ": base * np.array([[-1, 1, 1]]),
        "q2 -> -q2        ": base * np.array([[1, -1, 1]]),
        "q3 -> -q3        ": base * np.array([[1, 1, -1]]),
        "perm (q2,q3,q1)  ": base[:, [1, 2, 0]],
        "perm (q2,q1,q3)  ": base[:, [1, 0, 2]],
    }
    print(f"  -- {name}   hermiticity residual {herm:.3e}")
    for tag, q in tests.items():
        ev, _ = bloch_eigs(L, bd, r['mass'], q, C=r['C'], improve=True)
        d = float(np.max(np.abs(np.sort(ev[0]) - ev0)))
        print(f"     {tag}: max |dlambda| = {d:.3e}   {'OK' if d < 1e-12 else 'FAIL'}")

print("\n=== C2b  orbit-reduced momentum sum vs full L^3 sum (heat trace) ===")
sv = np.array([5.0, 20.0, 60.0])
for name, P in CH_P.items():
    for eps in (0.0, 0.1):
        a, _ = lat_trace(L, P, eps, n, sv, True, use_sym=True)
        b, ib = lat_trace(L, P, eps, n, sv, True, use_sym=False)
        print(f"  {name:13s} eps={eps:.2f}  rel diff : {fmte(a/b-1)}   "
              f"(nq {len(momentum_orbits(L, np.allclose(P[1:],P[1]))[0])} vs {ib['nq']})")

print("\n=== C2c  eps -> -eps parity of the lattice heat trace ===")
for LL in (12, 16):
    for name, P in CH_P.items():
        for eps in (0.05, 0.10):
            a, _ = lat_trace(LL, P, +eps, n, sv, True, use_sym=False)
            b, _ = lat_trace(LL, P, -eps, n, sv, True, use_sym=False)
            print(f"  L={LL} {name:13s} eps={eps:.2f}  |K(+e)/K(-e)-1| : {fmte(a/b-1)}")

print("\n=== C2d  eps -> -eps parity of the CONTINUUM heat trace (opus_t206) ===")
from opus_t206 import cont_heat
from kx_base import CH_T206
Lc = 32
kap = 2 * math.pi * n / Lc
svc = np.array([0.4, 1.0, 2.0]) / kap ** 2
for name, ch in CH_T206.items():
    for eps in (0.05, 0.10):
        a = cont_heat(Lc, ch, +eps, n, svc, 14)
        b = cont_heat(Lc, ch, -eps, n, svc, 14)
        print(f"  {name:13s} eps={eps:.2f}  |K(+e)/K(-e)-1| : {fmte(a/b-1)}")
