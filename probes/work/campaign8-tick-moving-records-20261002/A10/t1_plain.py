"""t1: plain (sign-free) cycle.  Factorization, nodes, speeds."""
import numpy as np, itertools
from cyc import cycle, W1, phases

rng = np.random.default_rng(1)
pi = np.pi

# (a) factorization U = W(Kz) x W(Ky) x W(Kx), all 6 axis orders, general angles
err = 0.0
for trial in range(200):
    K = rng.uniform(-pi, pi, 3)
    te, to = rng.uniform(0, pi, 2)
    target = np.kron(W1(K[2], te, to), np.kron(W1(K[1], te, to), W1(K[0], te, to)))
    for order in itertools.permutations((0, 1, 2)):
        U = cycle(K, te, to, signed=False, order=order)
        err = max(err, np.abs(U - target).max())
        err = max(err, np.abs(U.conj().T @ U - np.eye(8)).max())
print("(a) max |U_order - WxWxW| and unitarity defect over 200 K x 6 orders:", f"{err:.2e}")

# (b) 1D dispersion check: cos w = c_e c_o - s_e s_o cos K (relative to exp(i(te+to)))
e1 = 0.0
for trial in range(200):
    K = rng.uniform(-pi, pi); te, to = rng.uniform(0, pi, 2)
    ev = np.linalg.eigvals(W1(K, te, to)) * np.exp(-1j * (te + to))
    cw = np.cos(te) * np.cos(to) - np.sin(te) * np.sin(to) * np.cos(K)
    e1 = max(e1, np.abs(np.sort(ev.real) - np.sort([cw, cw])).max())
print("(b) 1D dispersion law error:", f"{e1:.2e}")

# (c) gap at K=pi equals 2|te-to| (mass = angle difference)
for te, to in [(0.7, 0.7), (0.7, 0.5), (pi / 2, pi / 2 - 0.3)]:
    ph = np.angle(np.linalg.eigvals(W1(pi, te, to)) * np.exp(-1j * (te + to)))
    print(f"(c) te={te:.3f} to={to:.3f}: W(pi) relative eigenphases {np.round(np.sort(ph), 12)}  (expect +-|te-to|)")

# (d) 3D: uniform angle th; degeneracy at K*=(pi,pi,pi); planar sheets; speeds
for th in [pi / 8, pi / 4, 3 * pi / 8, pi / 2]:
    Ks = np.array([pi, pi, pi])
    U0 = cycle(Ks, th)
    deg = np.abs(U0 - np.exp(6j * th) * np.eye(8)).max()
    # slopes along unit directions n: eigenphases at K*+d n relative to exp(6i th)
    d = 1e-5
    out = []
    for n in [np.array([1, 0, 0]), np.array([1, 1, 0]) / np.sqrt(2), np.array([1, 1, 1]) / np.sqrt(3),
              rng.normal(size=3)]:
        n = n / np.linalg.norm(n)
        ph = np.sort(np.angle(np.linalg.eigvals(cycle(Ks + d * n, th)) * np.exp(-6j * th))) / d
        pred = np.sort([np.sin(th) * np.dot(sg, n) for sg in itertools.product((1, -1), repeat=3)])
        out.append(np.abs(ph - pred).max())
    print(f"(d) th={th:.4f}: |U(K*)-e^(6i th) 1|={deg:.1e}; slopes = sin(th)*(sx,sy,sz).n  max dev {max(out):.1e}")

# (e) minimal gap over the BZ: where do bands meet?  uniform th, grid
th = pi / 4
g = np.linspace(-pi, pi, 41)[:-1]
best = []
for Kx in g:
    for Ky in g:
        for Kz in g:
            ph = np.sort(np.angle(np.linalg.eigvals(cycle(np.array([Kx, Ky, Kz]), th)) * np.exp(-6j * th)))
            gaps = np.diff(np.concatenate([ph, [ph[0] + 2 * pi]]))
            best.append((gaps.min(), Kx, Ky, Kz))
best.sort()
print("(e) th=pi/4 smallest band gaps on a 40^3 grid (gap,K):", [tuple(np.round(b, 3)) for b in best[:4]])
cnt = sum(1 for b in best if b[0] < 1e-9)
print(f"    grid points with an exact touching: {cnt} of {len(best)} (nodal surfaces of the separable step)")

# (f) 1D max group velocity = sin(th) at K=pi (cells per W-step)
for th in [pi / 8, pi / 4, 3 * pi / 8]:
    Kg = np.linspace(-pi, pi, 20001)
    w = np.arccos(np.clip(np.cos(th) ** 2 - np.sin(th) ** 2 * np.cos(Kg), -1, 1))
    v = np.gradient(w, Kg)
    print(f"(f) th={th:.4f}: max|v_1D| = {np.abs(v).max():.6f}  sin th = {np.sin(th):.6f}")
