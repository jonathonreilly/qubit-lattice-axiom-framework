"""OBS-1 R1: one-loop U(1) strain response of a corner mass on X2's walker (PREREG.md, R1 plan).
Toy Dirac on the walker: H(k) = tau_z x sigma.s(k) + tau_x x m(k), s_a = sin phi^f_a(k_a), m(k) = m0 + Delta*(1 - sum cos phi^f_a)/2.
Vector-like U(1), NN photon d_a(q) = 2 sin(phi^g_a(q)/2), Feynman gauge, continuous (Euclidean) time.
SF strain: tan phi^f = tan k e^{t h_a/2} (walker), tan(phi^g/2) = tan(q/2) e^{t h_a/2} (photon). Units: lattice, e^2 = 1.
Sigma0(p) = -sum_k w [sum_a V_a M V_a - M] + seagull;  M = H/(2E Om (E+Om));  Sigma1 = -sum_k w [sum_a V_a V_a - 1]/(2 Om (E+Om)^2)
seagull = (1/2) sum_a sum_q w T_a/(2 Om(q)),  T_a = [h_a(p+q) + h_a(p-q) - 2 h_a(p)]/d_a(q)^2.
delta ln m_pole = Sigma0_mass/m0 + c (c = identity part of Sigma1); mass part = Tr(tau_x Sigma0)/4.
Grid: photon momentum per axis q = u|u|/pi (clustered at q = 0), u midpoint grid, weight = Jacobian/N^3; k = p - q."""
import numpy as np, sys, time
t0 = time.time()
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]
TZS = [np.kron(sz, S) for S in SIG]          # tau_z x sigma_a
TX = np.kron(sx, s0)                          # tau_x x 1
I4 = np.eye(4)

def phif(k, th):   # walker flow, th = t*h_aa
    return np.arctan2(np.sin(k) * np.exp(th / 2), np.cos(k))
def phig(q, th):   # photon flow, q in (-pi, pi)
    return 2 * np.arctan(np.tan(q / 2) * np.exp(th / 2))
def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi

def h_axis(ka, a, th, Delta):
    """per-axis part of H (4x4 per point): tau_z sigma_a sin phi + tau_x (-Delta/2) cos phi"""
    ph = phif(ka, th)
    return np.sin(ph)[..., None, None] * TZS[a] + (-0.5 * Delta * np.cos(ph))[..., None, None] * TX

def sigma(p, hdiag, t, m0, Delta, N, want_sg=True):
    th = [t * hdiag[a] for a in range(3)]
    u = -np.pi + (np.arange(N) + 0.5) * 2 * np.pi / N
    qg = u * np.abs(u) / np.pi; jac = 2 * np.abs(u) / np.pi
    S0 = np.zeros((4, 4), complex); S1 = np.zeros((4, 4), complex); wsum = 0.0; ward = 0.0
    hp = [h_axis(np.array(p[a]), a, th[a], Delta) for a in range(3)]
    # slab over the x photon momentum
    qy, qz = np.meshgrid(qg, qg, indexing='ij'); jyz = np.outer(jac, jac).ravel()
    qy = qy.ravel(); qz = qz.ravel()
    for ix in range(N):
        q = [np.full(qy.shape, qg[ix]), qy, qz]
        w = jac[ix] * jyz / N**3
        k = [p[a] - q[a] for a in range(3)]
        hk = [h_axis(k[a], a, th[a], Delta) for a in range(3)]
        d = [2 * np.sin(phig(wrap(q[a]), th[a]) / 2) for a in range(3)]
        Om = np.sqrt(d[0]**2 + d[1]**2 + d[2]**2)
        phk = [phif(k[a], th[a]) for a in range(3)]
        ssq = sum(np.sin(x)**2 for x in phk)
        mk = m0 + Delta * (1 - sum(np.cos(x) for x in phk)) / 2
        E = np.sqrt(ssq + mk**2)
        H = sum(hk) + (m0 + 0.5 * Delta) * TX
        M = H / (2 * E * Om * (E + Om))[:, None, None]
        V = [(hp[a] - hk[a]) / d[a][:, None, None] for a in range(3)]
        if ix == N // 3:
            Hp = sum(hp) + (m0 + 0.5 * Delta) * TX
            ward = np.abs(sum(d[a][:, None, None] * V[a] for a in range(3)) - (Hp - H)).max()
        VMV = sum(V[a] @ M @ V[a] for a in range(3))
        S0 -= np.einsum('p,pij->ij', w, VMV - M)
        VV = sum(V[a] @ V[a] for a in range(3))
        S1 -= np.einsum('p,pij->ij', w, (VV - I4) / (2 * Om * (E + Om)**2)[:, None, None])
        if want_sg:
            # seagull: photon momentum q, T_a(p; q)
            for a in range(3):
                Ta = (h_axis(p[a] + q[a], a, th[a], Delta) + h_axis(p[a] - q[a], a, th[a], Delta) - 2 * hp[a]) / (d[a]**2)[:, None, None]
                S0 += 0.5 * np.einsum('p,pij->ij', w / (2 * Om), Ta)
        wsum += w.sum()
    return S0, S1, wsum, ward

def dlnm(p, hdiag, t, m0, Delta, N, base=None):
    S0, S1, wsum, ward = sigma(p, hdiag, t, m0, Delta, N)
    mpart = np.trace(TX @ S0).real / 4
    c = np.trace(S1).real / 4
    if base is not None:
        mpart -= base
    return mpart / m0 + c, mpart, c, S0, wsum, ward

if __name__ == '__main__':
    N = int(sys.argv[1]); m0 = float(sys.argv[2]); Delta = float(sys.argv[3]); dt = 0.02
    p = [np.pi, 0.0, 0.0]
    print(f"N={N} m0={m0} Delta={Delta} dt={dt}", flush=True)
    base = {}
    for lab, hd in (('0', (0, 0, 0)), ('xx+', (1, 0, 0)), ('xx-', (-1, 0, 0)), ('yy+', (0, 1, 0)), ('yy-', (0, -1, 0)), ('zz+', (0, 0, 1)), ('zz-', (0, 0, -1))):
        hdd = tuple(x * dt for x in hd)
        b0 = None
        if Delta != 0:   # additive (m0-independent) mass from the mirror-gap proxy: subtract the m0 = 0 value
            S0z, _, _, _ = sigma(p, hd, dt, 0.0, Delta, N)
            b0 = np.trace(TX @ S0z).real / 4
        dl, mp, c, S0, ws, ward = dlnm(p, hd, dt, m0, Delta, N, base=b0)
        base[lab] = dl
        offd = np.abs(S0 - (np.trace(TX @ S0) / 4) * TX - (np.trace(S0) / 4) * I4).max()
        print(f"  h={lab:4s} dlnm={dl:+.8e} mass_part={mp:+.6e} c={c:+.6e} additive_base={0.0 if b0 is None else b0:+.4e} other_comps={offd:.1e} wsum={ws:.6f} ward={ward:.1e}  ({time.time()-t0:.0f}s)", flush=True)
    Cpar = (base['xx+'] - base['xx-']) / (2 * dt); Cy = (base['yy+'] - base['yy-']) / (2 * dt); Cz = (base['zz+'] - base['zz-']) / (2 * dt)
    print(f"RESULT N={N} m0={m0} Delta={Delta}: dlnm0={base['0']:+.6e}  C_par={Cpar:+.6e} C_perp(y)={Cy:+.6e} C_perp(z)={Cz:+.6e}  K=C_par-C_perp={Cpar - 0.5*(Cy+Cz):+.6e}  trace-response={Cpar+Cy+Cz:+.6e}", flush=True)
