"""C5 R5-4 (5): 1+1 analogue, low-mass regime m*tau << 1 (tau = sqrt(k) = link proper length).
Same coined unitary link walk and covariant matching as r54_1p1_branches.py, with a log-spaced mass grid.
Question: do the l^2 masses become theta-independent (an emergent shell) as m -> 0? Report the l^2 masses
(zero crossings of the mismatch) in [1e-4, 5e-2] at 12 rapidities in [0, eta0)."""
import mpmath as mp, numpy as np
mp.mp.dps = 60
K = 3; g = ((2, 1), (3, 2)); eta = mp.acosh(2)
def mul(g, v): return (g[0][0]*v[0] + g[0][1]*v[1], g[1][0]*v[0] + g[1][1]*v[1])
N = 30
D = {0: (1, 0)}; w = (1, 0)
for n in range(1, N+4): w = mul(g, w); D[n] = w
w = (1, 0); gi = ((2, -1), (-3, 2))
for n in range(1, N+4): w = mul(gi, w); D[-n] = w
def mismatch(m, th, zeta):
    c, s = np.cos(zeta), np.sin(zeta)
    q0, q1 = -mp.sqrt(K)*m*mp.cosh(th), m*mp.sinh(th)
    nc = int(mp.nint(th/eta))
    ph = {n: float(mp.fmod(q0*D[n][0] + q1*D[n][1], 2*mp.pi)) for n in range(nc-N, nc+N)}
    def T(n):
        e = np.exp(-1j*ph[n]); return np.array([[e/c, -s/c], [-s/c, np.conj(e)/c]])
    rng = np.random.default_rng(1)
    wp = rng.normal(size=2) + 1j*rng.normal(size=2)
    for n in range(nc+N-1, nc-1, -1):
        wp = np.linalg.solve(T(n), wp); wp /= np.linalg.norm(wp)
    wm = rng.normal(size=2) + 1j*rng.normal(size=2)
    for n in range(nc-N, nc):
        wm = T(n) @ wm; wm /= np.linalg.norm(wm)
    return np.angle((wp[1]/wp[0])/(wm[1]/wm[0]))
for zeta in (1.2, 0.6):
    ms = np.exp(np.linspace(np.log(1e-4), np.log(5e-2), 900))
    print(f"zeta = {zeta}, k = {K}, N = {N}; l^2 masses (mismatch zero crossings) in [1e-4, 5e-2]:")
    for i in range(12):
        th = eta*i/12
        a = np.array([mismatch(mp.mpf(m), th, zeta) for m in ms])
        cr = [float(np.sqrt(ms[j]*ms[j+1])) for j in range(len(ms)-1) if a[j]*a[j+1] < 0 and abs(a[j]-a[j+1]) < np.pi]
        print(f"   theta = {float(th):.4f}: {len(cr):3d} crossings; lowest five: " + ", ".join(f"{x:.3e}" for x in cr[:5])
              + f";  mismatch range on grid [{a.min():.2f}, {a.max():.2f}], median |mismatch| {np.median(abs(a)):.2f}")
