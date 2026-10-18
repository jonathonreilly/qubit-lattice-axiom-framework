"""OBS-4 R4b (added after PREREG; see follow-up): numerical check of the carrier-mass ceiling in X2-as-written.
Four doublets Phi_a (a = 0, x, y, z; lattice momenta 0, K_x, K_y, K_z) with exact unit translations acting as Z2xZ2
charges q = 00, 01, 10, 11 (K_x + K_y = K_z).  Most general renormalisable gauge-invariant potential:
  V = sum_a m_a^2 Phi_a^dag Phi_a  (bilinears Phi_a^dag Phi_b, a != b, are Z2xZ2-odd: forbidden)
    + sum lambda_abcd (Phi_a^dag Phi_b)(Phi_c^dag Phi_d),  q_a+q_b+q_c+q_d = 0, real lambda (CP-conserving), |lambda| <= LMAX.
Vacuum <phi_a^0> = v_a (real, sum v_a^2 = 174.1^2, each v_a >= V_MIN so that every carrier Yukawa <= sqrt(4 pi) for B-gen's
57.5 GeV up entries); m_a^2 fixed by the tadpole conditions; mass matrix = Hessian in canonical real fields.
Maximise (differential evolution) the LIGHTEST of the 12 non-Goldstone states other than the lightest neutral (h),
over lambda and the vevs, keeping a local minimum (Hessian PSD). Boundedness from below is NOT imposed (conservative
for an upper bound)."""
import numpy as np, itertools, sys, time
from scipy.optimize import differential_evolution
P = lambda *a: print(*a, flush=True)
VEV = 174.1; V_MIN = 57.5 / np.sqrt(4 * np.pi)
q = [0, 1, 2, 3]
quads = [t for t in itertools.product(range(4), repeat=4) if (q[t[0]] ^ q[t[1]] ^ q[t[2]] ^ q[t[3]]) == 0]
def orbit(t):
    a, b, c, d = t
    return {(a, b, c, d), (b, a, d, c), (c, d, a, b), (d, c, b, a)}
reps = []; seen = set()
for t in quads:
    if t in seen: continue
    o = orbit(t); seen |= o; reps.append(sorted(o))
NL = len(reps)

def lam_tensor(x):
    L = np.zeros((4, 4, 4, 4))
    for val, o in zip(x, reps):
        for t in o: L[t] = val / len(o)
    return L

def fields(xr, vev):
    """xr: (N,16) canonical real fluctuations -> Phi (N,4,2) complex; doublet a = (phi+, phi0)."""
    z = (xr[:, 0::2] + 1j * xr[:, 1::2]) / np.sqrt(2)          # (N,8)
    Phi = z.reshape(-1, 4, 2).copy()
    Phi[:, :, 1] += vev[None, :]
    return Phi

def V(xr, vev, m2, L):
    Phi = fields(xr, vev)
    B = np.einsum('nai,nbi->nab', Phi.conj(), Phi)                # B_ab = Phi_a^dag Phi_b
    v4 = np.einsum('abcd,nab,ncd->n', L, B, B).real
    v2 = np.einsum('a,naa->n', m2, B).real
    return v2 + v4

def hessian(vev, m2, L, h=1e-2):
    n = 16; E = np.eye(n) * h
    pts = [];
    for i in range(n):
        for j in range(n):
            pts += [E[i] + E[j], E[i] - E[j], -E[i] + E[j], -E[i] - E[j]]
    f = V(np.array(pts), vev, m2, L).reshape(n, n, 4)
    return (f[:, :, 0] - f[:, :, 1] - f[:, :, 2] + f[:, :, 3]) / (4 * h * h)

def tadpole_m2(vev, L, h=1e-3):
    # gradient wrt the real neutral component of each doublet (index 2a+1 -> phi0 real part is xr[:, 4a+2])
    m2 = np.zeros(4); g4 = np.zeros(4); c = np.zeros(4)
    for a in range(4):
        e = np.zeros((2, 16)); e[0, 4 * a + 2] = h; e[1, 4 * a + 2] = -h
        g4[a] = np.diff(V(e, vev, np.zeros(4), L)[::-1])[0] / (2 * h)
        c[a] = np.sqrt(2) * vev[a]                                  # d(m^2 |phi0|^2)/d x at vacuum, unit m^2
    return -g4 / c

def spectrum(x, LMAX):
    lam = x[:NL] * LMAX; th = x[NL:]
    u = np.array([np.cos(th[0]), np.sin(th[0]) * np.cos(th[1]), np.sin(th[0]) * np.sin(th[1]) * np.cos(th[2]),
                  np.sin(th[0]) * np.sin(th[1]) * np.sin(th[2])])
    vev = np.abs(u) * VEV
    L = lam_tensor(lam); m2 = tadpole_m2(vev, L)
    H = hessian(vev, m2, L); H = (H + H.T) / 2
    ev = np.linalg.eigvalsh(H)
    return ev, vev, m2

def objective(x, LMAX):
    ev, vev, m2 = spectrum(x, LMAX)
    if vev.min() < V_MIN: return 1e3 * (V_MIN - vev.min())
    if ev[0] < -1e-3 * VEV**2: return 1e2 * (-ev[0]) / VEV**2
    phys = np.sort(ev[3:])                                          # drop 3 Goldstones
    return -np.sqrt(max(phys[1], 0)) / 1e3                          # lightest state after h, TeV (maximise)

if __name__ == '__main__':
    P(f"{len(quads)} Z2xZ2-allowed index quadruples, {NL} independent real quartic couplings; V_MIN = {V_MIN:.1f} GeV")
    # sanity: random point, Goldstone count and gradient
    rng = np.random.default_rng(0); x = np.concatenate([rng.uniform(-0.2, 0.2, NL), rng.uniform(0.3, 1.2, 3)])
    ev, vev, m2 = spectrum(x, 4 * np.pi)
    g = np.array([(V(np.eye(16)[[i]] * 1e-4, vev, m2, lam_tensor(x[:NL] * 4 * np.pi)) - V(-np.eye(16)[[i]] * 1e-4, vev, m2, lam_tensor(x[:NL] * 4 * np.pi)))[0] / 2e-4 for i in range(16)])
    P(f"sanity: |grad| at vacuum {np.abs(g).max():.1e}; 3 smallest |eigenvalues| {np.sort(np.abs(ev))[:4]}")
    for LMAX in (4 * np.pi, 8 * np.pi):
        t0 = time.time()
        bounds = [(-1, 1)] * NL + [(0.0, np.pi / 2)] * 3
        res = differential_evolution(objective, bounds, args=(LMAX,), seed=int(LMAX), maxiter=int(sys.argv[1]) if len(sys.argv) > 1 else 150,
                                     popsize=12, tol=1e-8, polish=False)
        ev, vev, m2 = spectrum(res.x, LMAX); phys = np.sqrt(np.clip(np.sort(ev[3:]), 0, None))
        P(f"LMAX = {LMAX:.1f}: max over couplings/vevs of the lightest non-h state = {-res.fun:.3f} TeV ({time.time()-t0:.0f}s)")
        P(f"   vevs {np.round(vev, 1)} GeV; m_a^2 {np.round(m2 / 1e6, 3)} TeV^2; spectrum (TeV) {np.round(phys / 1e3, 3)}")
        # also the heaviest state reachable at that point and max single mass over a random sample
    # unconstrained-by-ordering check: maximise the 2nd-lightest as well as the heaviest-but-one (seesaw carrier)
