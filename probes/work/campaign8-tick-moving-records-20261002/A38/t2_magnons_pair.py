"""A38 t2: single flips (magnons) over H8 under its unique calm pair law J(s.s + s^a s^a), J=1.
8x8 Bloch Hamiltonian (cost relative to the background), plaquette Wilson loops on all 24 faces per cell,
band touchings (where, at what cost, point or line), slope anisotropy, and the 1->2 flip leakage."""
import os, sys, signal, itertools, time
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(55)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lib38 import *
t0 = time.time()
H8 = {r: np.array([(-1) ** r[0], (-1) ** r[1], (-1) ** r[2]], float) / np.sqrt(3) for r in CELL}
law = pair_law(1, 1, 0)
terms = onefl_terms(H8, law)
hop = realspace_hop(terms)
# background energy per site and the calm residual
amps = flip_amplitudes(H8, law)
print("calm check: largest flip amplitude", max(abs(v) for v in amps.values()))
E0 = 0
for x in CELL:
    for key, C in law.items():
        S = [tuple(np.array(x) + np.array(s)) for s in key]
        T = C
        for y in S:
            T = np.tensordot(np.array([tex_m(H8, y)[a] for a in range(3)]), T, axes=([0], [0]))
        E0 += T
print(f"background energy per site {E0 / 8:.3e}")
# on-site cost of a flip, hop magnitudes
diag = sorted(set(round(H1(hop, x, x).real, 9) for x in CELL))
print("one-flip on-site cost (all 8 sites):", diag)
mags = sorted(set(round(abs(H1(hop, x, tuple(np.array(x) + s * np.eye(3, dtype=int)[a]))), 9)
                  for x in CELL for a in range(3) for s in (1, -1)))
print("NN hop magnitudes:", mags)
# Wilson loops
fl = plaquette_fluxes(hop)
print("plaquette Wilson loops (corner, face, |W|, phase/pi):")
for x, f, aw, ph in fl:
    print(f"   {x} {f} |W|={aw:.4f} phase/pi={ph:+.6f}")
# Bloch spectrum: band touchings at cost 0 and elsewhere
def ev(k):
    return np.linalg.eigvalsh(bloch(terms, np.asarray(k)))
g = np.linspace(-np.pi / 2, np.pi / 2, 25)
herm = max(np.max(np.abs(bloch(terms, np.array(k)) - bloch(terms, np.array(k)).conj().T)) for k in itertools.product(g[::6], repeat=3))
print(f"Hermiticity of H(k): {herm:.1e}")
specsym = max(np.max(np.abs(np.sort(ev(k)) + np.sort(ev(k))[::-1])) for k in itertools.product(g[::4], repeat=3))
print(f"spectrum symmetric about zero cost (max |e_i + e_(9-i)|): {specsym:.1e}")
zero = []
for k in itertools.product(g, repeat=3):
    e = ev(k)
    zero.append((np.min(np.abs(e)), k))
nz = [k for v, k in zero if v < 1e-9]
print(f"grid points (25^3 on the reduced zone) with a zero-cost mode: {len(nz)} of {len(zero)}")
# test the dual-frame prediction: zero cost iff |cos kx|=|cos ky|=|cos kz| (folded); check on the body-diagonal line
for s in np.linspace(0, np.pi / 2, 7):
    for d in [(1, 1, 1), (1, 1, -1), (1, 0, 0), (1, 1, 0)]:
        k = s * np.array(d, float)
        e = ev(k)
        if d == (1, 1, 1) or s in (0, np.pi / 2):
            pass
    print(f"  s={s:.3f}: min|E| along (1,1,1): {np.min(np.abs(ev(s*np.array([1,1,1.])))):.2e}; along (1,1,-1): {np.min(np.abs(ev(s*np.array([1,1,-1.])))):.2e};"
          f" along (1,0,0): {np.min(np.abs(ev(s*np.array([1,0,0.])))):.2e}; along (1,1,0): {np.min(np.abs(ev(s*np.array([1,1,0.])))):.2e}")
# dispersion transverse to the nodal line at k0 = s(1,1,1)
k0 = 0.3 * np.array([1, 1, 1.])
for d in [(1, -1, 0), (1, 1, -2), (1, 1, 1)]:
    dv = np.array(d, float) / np.linalg.norm(d)
    vals = [np.sort(np.abs(ev(k0 + h * dv)))[0] for h in (1e-3, 2e-3)]
    print(f"  at k0=0.3(1,1,1), smallest |E| grows along {d}: {vals[0]:.3e} at h=1e-3, {vals[1]:.3e} at h=2e-3")
# leakage: one flip -> two flips (cubic magnon couplings), per localised flip
lk = []
for x in CELL:
    tot = 0
    for key, C in law.items():
        pass
print(f"time {time.time() - t0:.1f} s")
