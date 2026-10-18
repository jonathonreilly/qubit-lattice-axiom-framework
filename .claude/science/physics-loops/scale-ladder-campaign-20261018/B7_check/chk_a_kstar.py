#!/usr/bin/env python3
"""(a)+(b): anticommutation of commuting-C2 lifts, where it lives, and why k* matters."""
import itertools, sys
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__file__))
from chk_core import *

print("flux pattern reproduced on all cycles (incl. all 24 face orientations):", FLUX_OK)
nshift = [g for g in PROPER if (OH[g] @ LAM[g] % 2).any()]
print("proper rotations with nonzero affine shift:", len(nshift), "/ 24")
print("unshifted proper:", [OH[g].tolist() for g in PROPER if g not in nshift])

# fixed momenta of the affine action on a rational grid (multiples of 2pi/24)
N = 24; grid = [np.array(t) * 2*np.pi/N for t in itertools.product(range(N), repeat=3)]
def fixed_by(idx):
    return [k for k in grid if all(same_k(fibre_image(g, k), k) for g in idx)]
FO = fixed_by(PROPER)
print("momenta fixed by all 24 proper (units of pi):", [tuple(np.round(wrap(k)/np.pi, 3)) for k in FO])
kst = wrap(FO[0])
gam = np.zeros(3)
print("rotations fixing Gamma:", [OH[g].tolist() for g in PROPER if same_k(fibre_image(g, gam), gam)])

# commuting C2 pairs: global (matrix) commutator of fibre matrices, sign-independent
c2 = [g for g in PROPER if np.trace(OH[g]) == -1]
pairs = [(a, b) for a, b in itertools.combinations(c2, 2) if (OH[a] @ OH[b] == OH[b] @ OH[a]).all()]
res = []
for a, b in pairs:
    X = UF[a] @ UF[b]; Y = UF[b] @ UF[a]
    res.append(1 if np.allclose(X, Y) else (-1 if np.allclose(X, -Y) else 0))
print(f"commuting C2 pairs: {len(pairs)}, fibre-matrix commutator signs: {sorted(set(res))}")

# full real-space check on L = 4 torus: G_a G_b = -G_b G_a on the WHOLE one-particle space
T4 = torus_ops(4)
a, b = find(np.diag([1, -1, -1])), find(np.diag([-1, 1, -1]))
Ga, Gb = T4['G'](a), T4['G'](b)
print("L=4 real space: G(C2x)G(C2y) = -G(C2y)G(C2x):", np.allclose(Ga @ Gb, -Gb @ Ga))
# translations vs dressed rotations: G T_e G^-1 = (-1)^{lam.e} T_{Re}
Tx = T4['T']((1, 0, 0))
for g in (a, b):
    lhs = T4['G'](g) @ Tx @ T4['G'](g).T; Re = tuple(int(x) for x in OH[g] @ np.array([1, 0, 0]))
    sgn = [s for s in (1, -1) if np.allclose(lhs, s * T4['T'](Re))]
    print(f"   G T_x G^-1 = {sgn} T_(Rx) for g={OH[g].tolist()}  lam={LAM[g]}")

# where do the two C2 fibre maps both fix k?  even degeneracy is forced exactly there
fx = fixed_by([a, b])
print(f"momenta (N={N} grid) fixed by both C2x and C2y: {len(fx)}:", [tuple(np.round(wrap(k)/np.pi, 2)) for k in fx])
print("   Gamma fixed by C2x?", same_k(fibre_image(a, gam), gam), " image of Gamma under C2x (units pi):", np.round(wrap(fibre_image(a, gam))/np.pi, 3))

# random symmetric Hamiltonian (real-space symmetrisation on L=4) -> degeneracies at k*, at D2-fixed points, and generic
rng = np.random.default_rng(99)
def random_sym(idx, r=1, L=4, ops=T4, seed=None):
    rr = np.random.default_rng(seed)
    h = {d: rr.normal(size=(12, 12)) + 1j*rr.normal(size=(12, 12)) for d in itertools.product(range(-r, r+1), repeat=3)}
    A = ops['from_blocks'](h); A = (A + A.conj().T)/2
    Gs = [ops['G'](g) for g in idx]
    S = sum(G @ A @ G.T for G in Gs) / len(Gs)
    return S
Gall = [T4['G'](g) for g in PROPER]
for trial in range(3):
    S = random_sym(PROPER, seed=trial)
    assert all(np.allclose(G @ S @ G.T, S) for G in Gall)
    h = T4['to_blocks'](S)
    assert np.allclose(T4['from_blocks'](h), S)
    ev = np.linalg.eigvalsh(Hk(h, kst)[0])
    evx = [mults(np.linalg.eigvalsh(Hk(h, k)[0]), 1e-8) for k in fx]
    evg = mults(np.linalg.eigvalsh(Hk(h, rng.uniform(-3, 3, 3))[0]), 1e-8)
    print(f"  trial {trial}: k* mults {mults(ev, 1e-8)}; all D2-fixed points even: {all(x % 2 == 0 for m in evx for x in m)}; generic k mults {evg}")
    # band-count logic: at k*, number of levels below any gap is even
    cums = np.cumsum(mults(ev, 1e-8))
    print(f"     cumulative level counts at k* (possible n(k*) for a gap at k*): {cums.tolist()}")
