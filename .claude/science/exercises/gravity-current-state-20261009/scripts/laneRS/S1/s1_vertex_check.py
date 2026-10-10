"""Independent real-space check of the band-basis vertex W used in s1_matrix_collision.py,
plus the free (V=0) control.  Builds Bloch states psi(x) = sum_A U[A,a] e^{i(k+pi A).x} on an
L^d torus and evaluates sum_{x,y} K(x-y) phi3*(x) phi4*(y) [psi1(x) psi2(y) - psi2(x) psi1(y)]."""
import numpy as np, itertools
from s1_matrix_collision import *
rng = np.random.default_rng(5)
for d, L, inter in ((2, 8, 'nn'), (2, 8, 'cube'), (3, 4, 'nn'), (3, 4, 'cube')):
    model = Stag(d, 0.5, inter)
    sites = np.array(list(itertools.product(range(L), repeat=d)))
    Kr = {}
    for r in itertools.product([-1, 0, 1], repeat=d):
        r = np.array(r)
        if inter == 'nn': val = 1.0 if np.sum(np.abs(r)) == 1 else 0.0
        else: val = float(np.prod(2 - np.abs(r))) if np.any(r) else 0.0
        if val: Kr[tuple(r)] = val
    def bloch(k, U):
        ph = np.exp(1j*(sites @ k))[:, None] * np.exp(1j*np.pi*(sites @ model.As.T))  # (N, n)
        return ph @ U / np.sqrt(len(sites))
    idx = {tuple(s): i for i, s in enumerate(sites)}
    worst = 0
    for trial in range(3):
        ks = [2*np.pi*rng.integers(0, L, d)/L for _ in range(3)]
        k1, k2, k3 = ks; k4 = k1 + k2 - k3
        Us = []
        for k in (k1, k2, k3, k4):
            Um, Up, w = model.U(k); Us.append(Up if rng.random() < 0.5 else Um)
        Wc = model.W((k1, k2, k3, k4), Us) / len(sites)
        ps = [bloch(k, U) for k, U in zip((k1, k2, k3, k4), Us)]
        D = model.D; Wr = np.zeros((D,)*4, complex)
        for xi, x in enumerate(sites):
            for r, val in Kr.items():
                yi = idx[tuple((x - np.array(r)) % L)]
                Wr += val*np.einsum('i,j,k,l->ijkl', ps[2][xi].conj(), ps[3][yi].conj(), ps[0][xi], ps[1][yi])
                Wr -= val*np.einsum('i,j,k,l->ijkl', ps[2][xi].conj(), ps[3][yi].conj(), ps[0][yi], ps[1][xi])
        worst = max(worst, np.max(np.abs(Wc - Wr)) / max(np.max(np.abs(Wr)), 1e-12))
    print(f"d={d} L={L} {inter}: max rel |W_code - W_realspace| = {worst:.2e}")
# free control: v = 0 -> every one-body F passes (nullity = full block-distinct dimension)
model = Stag(2, 0.5, 'zero'); r2 = np.random.default_rng(1)
procs = sample_processes(model, 200, ALLCH, r2)
sv, ncol, nsec, Wn = nullspace_run(model, 2, procs, 'odd', r2)
print(f"free control d=2 R=2 odd: block-distinct {ncol}, nullity {int(np.sum(sv < 1e-8))} (all pass), sv_max {sv[0]:.1e}")
