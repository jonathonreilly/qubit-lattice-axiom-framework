"""OBS-1 R1 (continued; same set-up as r1_loop.py, PREREG.md R1 plan).
(A) corner-selective generation mass symbol g_z(k) = (1 - cos k_z)/2 (D4[001]; = 1 at hw1 corner e_z, 0 at e_x, e_y):
    one-loop 'leak' of mu*g_z into the light corner e_x's mass, L(t) = d Sigma_mass(e_x)/d mu, and its strain derivatives
    L'_a = dL/dt for h = e_a e_a (a = x, y, z).  delta ln m(e_x) per unit strain = e^2 * L'_a * (mu/m_light).
(B) static velocity anisotropy at the light corner e_x: Z_a = d Sigma_kin,a/d q_a / v_tree,a; K_v = Z_x - Z_y.
Mass symbol m(k) = m0 + Delta*(1 - sum cos)/2 + mu*(1 - cos k_z)/2 (all separable -> unique axial divided differences)."""
import numpy as np, sys, time
from r1_loop import phif, phig, wrap, TZS, TX, I4
t0 = time.time()

def h_axis(ka, a, th, cvec):
    ph = phif(ka, th)
    return np.sin(ph)[..., None, None] * TZS[a] + (cvec[a] * np.cos(ph))[..., None, None] * TX

def sigma0(p, hdiag, t, m0, Delta, mu, N):
    th = [t * hdiag[a] for a in range(3)]
    cvec = [-(Delta + (mu if a == 2 else 0.0)) / 2 for a in range(3)]
    const = m0 + Delta / 2 + mu / 2
    u = -np.pi + (np.arange(N) + 0.5) * 2 * np.pi / N
    qg = u * np.abs(u) / np.pi; jac = 2 * np.abs(u) / np.pi
    S0 = np.zeros((4, 4), complex); S1 = np.zeros((4, 4), complex)
    hp = [h_axis(np.array(p[a]), a, th[a], cvec) for a in range(3)]
    qy, qz = np.meshgrid(qg, qg, indexing='ij'); jyz = np.outer(jac, jac).ravel(); qy = qy.ravel(); qz = qz.ravel()
    for ix in range(N):
        q = [np.full(qy.shape, qg[ix]), qy, qz]; w = jac[ix] * jyz / N**3
        k = [p[a] - q[a] for a in range(3)]
        hk = [h_axis(k[a], a, th[a], cvec) for a in range(3)]
        d = [2 * np.sin(phig(wrap(q[a]), th[a]) / 2) for a in range(3)]
        Om = np.sqrt(d[0]**2 + d[1]**2 + d[2]**2)
        phk = [phif(k[a], th[a]) for a in range(3)]
        ssq = sum(np.sin(x)**2 for x in phk)
        mk = const + sum(cvec[a] * np.cos(phk[a]) for a in range(3))
        E = np.sqrt(ssq + mk**2)
        H = sum(hk) + const * TX
        M = H / (2 * E * Om * (E + Om))[:, None, None]
        V = [(hp[a] - hk[a]) / d[a][:, None, None] for a in range(3)]
        S0 -= np.einsum('p,pij->ij', w, sum(V[a] @ M @ V[a] for a in range(3)) - M)
        S1 -= np.einsum('p,pij->ij', w, (sum(V[a] @ V[a] for a in range(3)) - I4) / (2 * Om * (E + Om)**2)[:, None, None])
        for a in range(3):
            Ta = (h_axis(p[a] + q[a], a, th[a], cvec) + h_axis(p[a] - q[a], a, th[a], cvec) - 2 * hp[a]) / (d[a]**2)[:, None, None]
            S0 += 0.5 * np.einsum('p,pij->ij', w / (2 * Om), Ta)
    return S0, S1

if __name__ == '__main__':
    N = int(sys.argv[1]); m0 = float(sys.argv[2]); Delta = float(sys.argv[3]); mode = sys.argv[4]
    dt = 0.02; mu = 0.05; p = [np.pi, 0.0, 0.0]
    if mode == 'own':   # the corner-z symbol's response at its own corner e_z = (0, 0, pi)
        p = [0.0, 0.0, np.pi]
    mass = lambda S: np.trace(TX @ S).real / 4
    if mode in ('leak', 'own'):
        L = {}
        for lab, hd in (('0', (0, 0, 0)), ('x+', (1, 0, 0)), ('x-', (-1, 0, 0)), ('y+', (0, 1, 0)), ('y-', (0, -1, 0)), ('z+', (0, 0, 1)), ('z-', (0, 0, -1))):
            Sa, _ = sigma0(p, hd, dt, m0, Delta, mu, N); Sb, _ = sigma0(p, hd, dt, m0, Delta, 0.0, N)
            L[lab] = (mass(Sa) - mass(Sb)) / mu
            print(f"  h={lab:3s} leak L = dSigma_mass(e_x)/dmu = {L[lab]:+.8e}  ({time.time()-t0:.0f}s)", flush=True)
        Lp = {a: (L[a + '+'] - L[a + '-']) / (2 * dt) for a in 'xyz'}
        print(f"RESULT-{mode.upper()} p={np.round(p,3).tolist()} N={N} m0={m0} Delta={Delta} mu={mu}: L0={L['0']:+.6e}  L'_x={Lp['x']:+.6e} L'_y={Lp['y']:+.6e} L'_z={Lp['z']:+.6e}  "
              f"traceless parts: tet_z (2z-x-y)/sqrt6 = {(2*Lp['z']-Lp['x']-Lp['y'])/np.sqrt(6):+.6e}, (x-y)/sqrt2 = {(Lp['x']-Lp['y'])/np.sqrt(2):+.6e}, "
              f"Frobenius of traceless part = {np.sqrt(sum((Lp[a]-sum(Lp.values())/3)**2 for a in 'xyz')):+.6e}", flush=True)
    else:  # velocity anisotropy at t = 0
        dq = 1e-3; Z = {}
        for a, vt in ((0, -1.0), (1, 1.0)):
            pp = list(p); pm = list(p); pp[a] += dq; pm[a] -= dq
            Sp, _ = sigma0(pp, (0, 0, 0), 0.0, m0, Delta, 0.0, N); Sm, _ = sigma0(pm, (0, 0, 0), 0.0, m0, Delta, 0.0, N)
            comp = lambda S: np.trace(TZS[a] @ S).real / 4
            Z[a] = (comp(Sp) - comp(Sm)) / (2 * dq) / vt
            print(f"  axis {a}: Z = {Z[a]:+.8e}  ({time.time()-t0:.0f}s)", flush=True)
        print(f"RESULT-VEL N={N} m0={m0} Delta={Delta}: Z_par={Z[0]:+.6e} Z_perp={Z[1]:+.6e} K_v=Z_par-Z_perp={Z[0]-Z[1]:+.6e}", flush=True)
