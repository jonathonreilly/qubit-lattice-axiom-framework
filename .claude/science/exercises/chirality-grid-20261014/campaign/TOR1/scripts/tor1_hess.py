"""TOR-1 (b2, descriptive add-on F3): locality of the FULL measure current j_l = d log rho / d theta_l (complex): the response
d j_l' / d theta_l0 = d^2 log rho / d theta_l0 d theta_l' (mixed central differences, eps = 2e-3) for fixed source links l0,
vs torus taxicab distance of link midpoints.  usage: python3 tor1_hess.py Lx Lt model nfield seed"""
import sys, time
import numpy as np
from tor1_lib import *
Lx, Lt, model, nf, seed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
S = Torus(Lx, Lt); rng = np.random.default_rng(seed); eps = 2e-3; t0 = time.time()
M = TorusMeasure(S, model, Ns=8, sk=-1, ntor=96, nloop=1024); M.ntor1 = 24; M.use_spline()
mid = np.array([(l[4] + 0.5, l[5]) if l[2] == 'x' else (l[4], l[5] + 0.5) for l in S.L])
def td(a, b):
    dx = abs(a[0] - b[0]); dt = abs(a[1] - b[1]); return min(dx, Lx - dx) + min(dt, Lt - dt)
print(f"# TOR-1 full-current response Lx={Lx} Lt={Lt} model={model} eps={eps}", flush=True)
for f in range(nf):
    while True:
        th = rng.normal(0, 0.12, S.nl) + rng.uniform(0, 2*np.pi) * S.Ux + rng.uniform(0, 2*np.pi) * S.Ut
        Fr = (th @ S.Pm.T + np.pi) % (2*np.pi) - np.pi
        if np.abs(Fr).max() < 0.5 and abs(round(Fr.sum()/(2*np.pi))) == 0: break
    for l0 in (S.key[('x', 1, 2)], S.key[('t', 2, 1)]):
        E = np.eye(S.nl) * eps
        pts = np.concatenate([th + E[l0] + E, th + E[l0] - E, th - E[l0] + E, th - E[l0] - E], 0)
        W = np.concatenate([M.logrho(pts[c:c+32]) for c in range(0, len(pts), 32)])
        def un(x): return x.real + 1j * np.unwrap(x.imag)
        n = S.nl; a, b, c, d = W[:n], W[n:2*n], W[2*n:3*n], W[3*n:]
        dd = lambda u, v: u.real - v.real + 1j * np.angle(np.exp(1j * (u.imag - v.imag)))
        H = (dd(a, b) - dd(c, d)) / (4 * eps * eps)
        ds = np.array([td(mid[l0], mid[l]) for l in range(n)])
        prof = {dv: (np.abs(H.real[ds == dv]).max(), np.abs(H.imag[ds == dv]).max()) for dv in np.unique(ds)}
        print(f"field {f} source {S.L[l0][2]}{S.L[l0][4:6]}: |d2 Re| / |d2 Im| vs d: " + " ".join(f"{dv:.1f}:{p[0]:.1e}/{p[1]:.1e}" for dv, p in prof.items()) + f" [{time.time()-t0:.0f}s]", flush=True)
