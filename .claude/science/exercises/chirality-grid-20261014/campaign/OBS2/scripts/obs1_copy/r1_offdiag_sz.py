"""OBS-1 R1 (continued; set-up as r1_loop.py). Off-diagonal generation mass from an on-site Higgs/flavon condensate at
lattice momentum Q = (pi, pi, 0): operator sum_k Psi^dag(k) tau_x b0 Psi(k+Q) + h.c., pairing hw1 corners e_x and e_y.
One-loop vertex correction (first order in b0): Sigma_off = + e^2 sum_k sum_{n,n'} [sum_a V_a(p,k) P_n(k) B P_n'(k+Q) V_a(k+Q,p+Q)
 - P_n B P_n'] J(E_n(k), E_n'(k+Q), Om(p-k)),  J(E1,E2) = [I(E1)-I(E2)]/(E2-E1), I(E) = sgn E/(2 Om (|E|+Om)).
b_phys = (b0 + Sigma_off)(1 + c_x/2 + c_y/2); strain derivative of ln b_phys for h = e_a e_a."""
import numpy as np, sys, time
from r1_loop import phif, phig, wrap, TZS, TX, I4, h_axis, sigma
SZ = np.diag([1., -1]).astype(complex); SPIN = True
t0 = time.time()

def sigma_off(p, Q, hdiag, t, m0, Delta, N):
    th = [t * hdiag[a] for a in range(3)]
    u = -np.pi + (np.arange(N) + 0.5) * 2 * np.pi / N
    qg = u * np.abs(u) / np.pi; jac = 2 * np.abs(u) / np.pi
    B = np.kron(np.array([[0, 1], [1, 0]], complex), SZ) if SPIN else TX   # OBS-2: covariant hw2 condensate tau_x (x) sigma_z
    hp = [h_axis(np.array(p[a]), a, th[a], Delta) for a in range(3)]
    hpQ = [h_axis(np.array(p[a] + Q[a]), a, th[a], Delta) for a in range(3)]
    qy, qz = np.meshgrid(qg, qg, indexing='ij'); jyz = np.outer(jac, jac).ravel(); qy = qy.ravel(); qz = qz.ravel()
    S = np.zeros((4, 4), complex)
    def proj(k):
        hk = [h_axis(k[a], a, th[a], Delta) for a in range(3)]
        H = sum(hk) + (m0 + 0.5 * Delta) * TX
        ph = [phif(k[a], th[a]) for a in range(3)]
        E = np.sqrt(sum(np.sin(x)**2 for x in ph) + (m0 + Delta * (1 - sum(np.cos(x) for x in ph)) / 2)**2)
        Hn = H / E[:, None, None]
        return hk, E, [(I4 + Hn) / 2, (I4 - Hn) / 2]
    for ix in range(N):
        q = [np.full(qy.shape, qg[ix]), qy, qz]; w = jac[ix] * jyz / N**3
        k = [p[a] - q[a] for a in range(3)]; kQ = [k[a] + Q[a] for a in range(3)]
        hk, E1, P1 = proj(k); hkQ, E2, P2 = proj(kQ)
        d = [2 * np.sin(phig(wrap(q[a]), th[a]) / 2) for a in range(3)]
        Om = np.sqrt(d[0]**2 + d[1]**2 + d[2]**2)
        V = [(hp[a] - hk[a]) / d[a][:, None, None] for a in range(3)]
        Vq = [(hkQ[a] - hpQ[a]) / (-d[a])[:, None, None] for a in range(3)]   # divided difference with step (k - p) = -q
        I = lambda E: np.sign(E) / (2 * Om * (np.abs(E) + Om))
        for s1, e1 in ((0, E1), (1, -E1)):
            for s2, e2 in ((0, E2), (1, -E2)):
                diff = e2 - e1
                J = np.where(np.abs(diff) > 1e-9, (I(e1) - I(e2)) / np.where(np.abs(diff) > 1e-9, diff, 1.0), 1 / (2 * Om * (np.abs(e1) + Om)**2))
                PBP = P1[s1] @ B @ P2[s2]
                term = sum(V[a] @ PBP @ Vq[a] for a in range(3)) - PBP
                S += np.einsum('p,pij->ij', w * J, term)
    return S

if __name__ == '__main__':
    N = int(sys.argv[1]); m0 = float(sys.argv[2]); Delta = float(sys.argv[3]); dt = 0.02
    p = [np.pi, 0.0, 0.0]; Q = [np.pi, np.pi, 0.0]   # p = e_x, p + Q = (2pi, pi, 0) = e_y
    py = [0.0, np.pi, 0.0]
    res = {}
    for lab, hd in (('0', (0, 0, 0)), ('x+', (1, 0, 0)), ('x-', (-1, 0, 0)), ('y+', (0, 1, 0)), ('y-', (0, -1, 0)), ('z+', (0, 0, 1)), ('z-', (0, 0, -1))):
        So = sigma_off(p, Q, hd, dt, m0, Delta, N)
        Bm = np.kron(np.array([[0, 1], [1, 0]], complex), SZ); boff = np.trace(Bm.conj().T @ So).real / 4
        other = np.abs(So - boff * Bm).max()
        _, S1x, _, _ = sigma(p, hd, dt, m0, Delta, N, want_sg=False); _, S1y, _, _ = sigma(py, hd, dt, m0, Delta, N, want_sg=False)
        cx = np.trace(S1x).real / 4; cy = np.trace(S1y).real / 4
        res[lab] = boff + (cx + cy) / 2
        print(f"  h={lab:3s} Sigma_off/b0 = {boff:+.8e} (other comps {other:.1e})  c_x={cx:+.6e} c_y={cy:+.6e}  dln b = {res[lab]:+.8e}  ({time.time()-t0:.0f}s)", flush=True)
    Lp = {a: (res[a + '+'] - res[a + '-']) / (2 * dt) for a in 'xyz'}
    mean = sum(Lp.values()) / 3
    print(f"RESULT-OFF N={N} m0={m0} Delta={Delta}: dln b(0)={res['0']:+.6e}  L'_x={Lp['x']:+.6e} L'_y={Lp['y']:+.6e} L'_z={Lp['z']:+.6e}  "
          f"traceless Frobenius={np.sqrt(sum((Lp[a]-mean)**2 for a in 'xyz')):+.6e}  tet_z={(2*Lp['z']-Lp['x']-Lp['y'])/np.sqrt(6):+.6e}", flush=True)
