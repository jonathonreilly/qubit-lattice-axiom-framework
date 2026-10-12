"""C5 R5-4 (4): 1+1 analogue, coined unitary link walk: where in (m, theta) does the law have l^2 solutions?
Same model as r54_1p1_walk.py (c). For each rapidity theta in [0, eta0] and mass m on a grid, the mismatch angle
between the +inf-decaying and -inf-decaying directions at site 0 (projective iteration, phases mod 2pi at 60 digits).
Zero crossings in m give the masses m_j(theta) at which the walk's fibre equation has an l^2 solution.
An exact covariant mass shell would be a branch with m_j(theta) constant in theta. Gamma covariance forces only
m_j(theta + eta0) = m_j(theta) (checked by including theta = eta0)."""
import mpmath as mp, numpy as np
mp.mp.dps = 60
K = 3; g = ((2, 1), (3, 2)); eta = mp.acosh(2)
def mul(g, v): return (g[0][0]*v[0] + g[0][1]*v[1], g[1][0]*v[0] + g[1][1]*v[1])
N = 18
D = {0: (1, 0)}; w = (1, 0)
for n in range(1, N+4): w = mul(g, w); D[n] = w
w = (1, 0); gi = ((2, -1), (-3, 2))
for n in range(1, N+4): w = mul(gi, w); D[-n] = w
def phases(m, th):
    q0, q1 = -mp.sqrt(K)*m*mp.cosh(th), m*mp.sinh(th)
    return {n: float(mp.fmod(q0*D[n][0] + q1*D[n][1], 2*mp.pi)) for n in D}
def mismatch(m, th, zeta):
    c, s = np.cos(zeta), np.sin(zeta); ph = phases(m, th)
    def T(n):
        e = np.exp(-1j*ph[n]); return np.array([[e/c, -s/c], [-s/c, np.conj(e)/c]])
    rng = np.random.default_rng(1)
    wp = rng.normal(size=2) + 1j*rng.normal(size=2)
    nc = int(mp.nint(th/eta))          # matching site at the stationary point; window [nc-N, nc+N] (exactly Gamma-covariant)
    for n in range(nc+N-1, nc-1, -1):
        wp = np.linalg.solve(T(n), wp); wp /= np.linalg.norm(wp)
    wm = rng.normal(size=2) + 1j*rng.normal(size=2)
    for n in range(nc-N, nc):
        wm = T(n) @ wm; wm /= np.linalg.norm(wm)
    zp, zm = wp[1]/wp[0], wm[1]/wm[0]
    return np.angle(zp/zm), abs(abs(zp) - 1), abs(abs(zm) - 1)
for zeta in (1.2,):
    ths = [eta*i/24 for i in range(25)] + [eta*mp.mpf('0.3'), eta*mp.mpf('1.3')]
    ms = np.linspace(0.02, 1.0, 1200)
    print(f"zeta = {zeta}, k = {K}, eta0 = {float(eta):.5f}, N = {N}; first three masses m_j(theta) with an l^2 solution (zero crossings in m):")
    branch1 = []
    for th in ths:
        a = np.array([mismatch(mp.mpf(m), th, zeta)[0] for m in ms])
        cr = [i for i in range(len(ms)-1) if a[i]*a[i+1] < 0 and abs(a[i]-a[i+1]) < np.pi]
        roots = []
        for i in cr[:3]:
            lo, hi = mp.mpf(ms[i]), mp.mpf(ms[i+1]); flo = a[i]
            for _ in range(30):
                mid = (lo+hi)/2; fm = mismatch(mid, th, zeta)[0]
                if fm*flo < 0: hi = mid
                else: lo, flo = mid, fm
            roots.append(float((lo+hi)/2))
        branch1.append(roots[0] if roots else np.nan)
        print(f"   theta = {float(th):.4f}: crossings in (0.02, 1.0): {len(cr):3d};  m_1..3 = " + ", ".join(f"{r:.6f}" for r in roots))
    b = np.array(branch1[:25])
    print(f"   lowest-crossing mass over the 25 theta in [0, eta0]: min {np.nanmin(b):.4f}, max {np.nanmax(b):.4f}; "
          f"m_1(theta=0) = {b[0]:.8f}, m_1(theta=eta0) = {b[24]:.8f}; m_1(0.3 eta0) = {branch1[25]:.8f}, m_1(1.3 eta0) = {branch1[26]:.8f}")
