"""A34 c14: bands of the glued, gauge-covariant hops of vector (triplet) charged matter found in c13 (own code).
Classical light background on the coarse lattice: links U -> u_l, zero flux (u = 1) or pi flux (u = KS signs,
eta_x = 1, eta_y = (-1)^x, eta_z = (-1)^(x+y); magnetic cell 2x2x1, 12 bands). For hops M = cos(t) M0 + sin(t) M1
(the 2-parameter covariant family): on a 20^3 grid, the smallest gap between any two neighbouring bands, the
smallest |E| (zero-energy touchings), and whether the spectrum is symmetric about 0. Supplied toy; mean-field links.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import signal, io, contextlib, itertools
import numpy as np
signal.alarm(28)
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "c13_glued_link_hops.py")).read()
ns = {"__file__": "c13"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, "c13", "exec"), ns)
vec = ns["vector"]
def H_zero(k, M):
    return sum(M[a] * np.exp(-1j * k[a]) + (M[a] * np.exp(-1j * k[a])).conj().T for a in range(3))
cell = [(x, y) for x in range(2) for y in range(2)]
def H_pi(k, M):
    H = np.zeros((12, 12), complex)
    def blk(i): return slice(3 * i, 3 * i + 3)
    for i, (x, y) in enumerate(cell):
        for a, (dx, dy) in enumerate(((1, 0), (0, 1), (0, 0))):
            eta = [1, (-1) ** x, (-1) ** (x + y)][a]
            x2, y2 = x + dx, y + dy
            ph = np.exp(-1j * k[a])       # Bloch phase with the true coarse displacement (one site along a)
            j = cell.index((x2 % 2, y2 % 2))
            T = eta * M[a] * ph
            H[blk(i), blk(j)] += T; H[blk(j), blk(i)] += T.conj().T
    return H
g = np.linspace(-np.pi, np.pi, 20, endpoint=False) + np.pi / 40
for t in (0.0, np.pi / 4, np.pi / 2, 3 * np.pi / 4):
    M = [np.cos(t) * vec[0][a] + np.sin(t) * vec[1][a] for a in range(3)]
    for name, Hf, nb in (("zero flux", H_zero, 3), ("pi flux", H_pi, 12)):
        mingap, minabs, sym = np.inf, np.inf, True
        for k in itertools.product(g, repeat=3):
            e = np.linalg.eigvalsh(Hf(np.array(k), M))
            mingap = min(mingap, np.min(np.diff(e))); minabs = min(minabs, np.min(np.abs(e)))
            sym &= np.allclose(np.sort(e), np.sort(-e), atol=1e-9)
        print(f"t={t:.3f} {name:9s}: bands {nb}; smallest neighbouring-band gap on grid {mingap:.3e}; "
              f"smallest |E| {minabs:.3e}; symmetric about 0 everywhere: {sym}")
