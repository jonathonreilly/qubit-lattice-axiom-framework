"""OBS-4 core: corner-basis quark mass matrices of OBS-3's exact escape realisations -> carrier couplings in the
mass basis -> tree-level dF=2 Wilson coefficients -> minimum carrier mass M* (PREREG.md rules 1-8).

Copied (not imported) from OBS-3: the texture formula (univ.py:78-85), the inputs (obs3_core.py:145-169).
Corners: index 0,1,2 = x,y,z (hw1 momenta Q_x=(pi,0,0), ...).  Carrier K_c (c = x,y,z) = Q_c' + Q_c'' carries the
pair {(c',c''),(c'',c')}; carrier '0' (momentum 0, H_0) carries the diagonal.
Normalisation: <phi_K^0> = v_K, sum v_K^2 = VEV^2, VEV = 174.1 GeV; Y^(K) = P_K(M)/v_K couples to the canonically
normalised complex neutral field.  Degenerate heavy H,A at M: H_eff = C4 (qbar_L^i q_R^j)(qbar_R^i q_L^j),
C4 = - sum_K Yhat^K_ij conj(Yhat^K_ji) / M^2  (i,j) = (s,d),(b,d),(b,s) down; (c,u) up.
"""
import numpy as np

# ------------------------------------------------------------------ inputs (obs3_core.py:145-169, copied)
def rot(t12, t23, t13, d):
    s12, c12, s23, c23, s13, c13 = np.sin(t12), np.cos(t12), np.sin(t23), np.cos(t23), np.sin(t13), np.cos(t13); e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 / e], [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])

def ckm_wolfenstein(lam, A, rb, eb):
    s12 = lam; s23 = A * lam**2
    z = A * lam**3 * (rb + 1j * eb) * np.sqrt(1 - A**2 * lam**4) / (np.sqrt(1 - lam**2) * (1 - A**2 * lam**4 * (rb + 1j * eb)))
    s13 = abs(z); d = np.angle(z)
    return rot(np.arcsin(s12), np.arcsin(s23), np.arcsin(s13), d)

w3 = np.exp(2j * np.pi / 3)
F = np.array([[w3**(c * j) for j in range(3)] for c in range(3)]) / np.sqrt(3)
MU = np.array([2.16e-3, 1.2730, 172.57]); MD = np.array([4.70e-3, 0.0935, 4.183])
VPDG = ckm_wolfenstein(0.22501, 0.826, 0.1591, 0.3523)
VEV = 174.1
yu, yd = MU / VEV, MD / VEV

def Jarl(Vm):
    return (Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1])).imag

# ------------------------------------------------------------------ OBS-3 texture (univ.py:78-85, copied)
def texture(p, sym=False, d120=False):
    r = p[0]
    if sym:
        a, b, c = p[1:4]; ph = np.array([[0, a, b], [a, 0, c], [b, c, 0]])
    else:
        ph = np.zeros((3, 3)); ph[0, 1], ph[0, 2], ph[1, 0], ph[1, 2], ph[2, 0], ph[2, 1] = p[1:7]
    Z = np.exp(1j * ph); Z[np.diag_indices(3)] = np.exp(r) * (np.exp(2j * np.pi * np.arange(3) / 3) if d120 else 1)
    return Z

def svd_sorted(Z):
    U, s, Vh = np.linalg.svd(Z); idx = np.argsort(s)
    return U[:, idx], s[idx], Vh.conj().T[:, idx]

def masses_from_p(p, d120=False):
    """exact B-gen(120) mass matrices (GeV) from the parameter vector (univ.py:119-123: scale to y_t, y_b)."""
    Zu, Zd = texture(p[:7], False, d120), texture(p[7:], False, d120)
    su = np.linalg.svd(Zu, compute_uv=False).max(); sd = np.linalg.svd(Zd, compute_uv=False).max()
    return Zu * (MU[2] / su), Zd * (MD[2] / sd)

# ------------------------------------------------------------------ mass basis in PDG phase convention
def mass_basis(Mu, Md, Vtarget=VPDG):
    """returns dict: Wu, Xu, mu, Wd, Xd, md with Wu^dag Mu Xu = diag(mu) etc. and Wu^dag Wd rephased to Vtarget."""
    Wu, su, Xu = svd_sorted(Mu); Wd, sd, Xd = svd_sorted(Md)
    Vp = Wu.conj().T @ Wd
    al = np.angle(Vp[:, 0]) - np.angle(Vtarget[:, 0])
    be = al[0] - np.angle(Vp[0, :]) + np.angle(Vtarget[0, :])
    Da, Db = np.diag(np.exp(1j * al)), np.diag(np.exp(1j * be))
    Wu, Xu, Wd, Xd = Wu @ Da, Xu @ Da, Wd @ Db, Xd @ Db
    V = Wu.conj().T @ Wd
    return dict(Wu=Wu, Xu=Xu, mu=su, Wd=Wd, Xd=Xd, md=sd, V=V, rephase_res=np.abs(V - Vtarget).max())

# ------------------------------------------------------------------ carriers
SUPPORT = {'0': [(0, 0), (1, 1), (2, 2)], 'x': [(1, 2), (2, 1)], 'y': [(0, 2), (2, 0)], 'z': [(0, 1), (1, 0)]}
CARRIERS = ['0', 'x', 'y', 'z']

def project(M, K):
    P = np.zeros_like(M)
    for (i, j) in SUPPORT[K]:
        P[i, j] = M[i, j]
    return P

def hat(M, W, X):
    return W.conj().T @ M @ X

def carrier_hats(Mu, Md, mb):
    """mass-basis images (GeV) of each carrier's support projection: Phat_u[K], Phat_d[K]."""
    Pu = {K: hat(project(Mu, K), mb['Wu'], mb['Xu']) for K in CARRIERS}
    Pd = {K: hat(project(Md, K), mb['Wd'], mb['Xd']) for K in CARRIERS}
    return Pu, Pd

# index pairs (i,j): coefficient of (qbar_L^i q_R^j)(qbar_R^i q_L^j) is Yhat_ij conj(Yhat_ji)
ROWS = {  # name: (sector, i, j, part, Lambda_TeV)  -- INP 1002.0900 Table 1 LR rows (PREREG rule 5)
    'K_Re': ('d', 1, 0, 'Re', 1.8e4), 'K_Im': ('d', 1, 0, 'Im', 3.2e5),
    'D_Re': ('u', 1, 0, 'Re', 6.2e3), 'D_Im': ('u', 1, 0, 'Im', 1.5e4),
    'Bd_Re': ('d', 2, 0, 'Re', 1.9e3), 'Bd_Im': ('d', 2, 0, 'Im', 3.6e3),
    'Bs_abs': ('d', 2, 1, 'abs', 3.7e2),
}

def pair_sum(Ph, vev, i, j):
    """sum_K Yhat^K_ij conj(Yhat^K_ji) with Yhat^K = Phat^K / v_K (GeV-units cancel: dimensionless)."""
    s = 0j
    for K in CARRIERS:
        if vev[K] == 0:
            continue
        s += Ph[K][i, j] * np.conj(Ph[K][j, i]) / vev[K]**2
    return s

def mstar_rows(Pu, Pd, vu, vd, scale=1.0):
    """M*_row in TeV for each INP row; vu, vd: dict carrier -> vev (GeV) seen by the up / down couplings."""
    out = {}
    for name, (sec, i, j, part, Lam) in ROWS.items():
        Ph, vv = (Pu, vu) if sec == 'u' else (Pd, vd)
        z = pair_sum(Ph, vv, i, j) * scale**2
        x = {'Re': abs(z.real), 'Im': abs(z.imag), 'abs': abs(z)}[part]
        out[name] = Lam * np.sqrt(x)
    return out

def max_coupling(Mu, Md, vu, vd):
    m = 0.0
    for K in CARRIERS:
        if vu[K] > 0: m = max(m, np.abs(project(Mu, K)).max() / vu[K])
        if vd[K] > 0: m = max(m, np.abs(project(Md, K)).max() / vd[K])
    return m

# ------------------------------------------------------------------ own direct dF=2 (PREREG rule 5, secondary)
MZ, AS_MZ, MT, MB_TH = 91.1876, 0.118, 172.57, 4.183

def b0(nf): return 11 - 2 * nf / 3

def alpha_s(mu):
    """one-loop alpha_s with thresholds at m_b, m_t (and m_c = 1.273 below)."""
    def run(a0, m0, m1, nf): return 1 / (1 / a0 + b0(nf) / (2 * np.pi) * np.log(m1 / m0))
    if mu >= MZ:
        if mu <= MT: return run(AS_MZ, MZ, mu, 5)
        a_t = run(AS_MZ, MZ, MT, 5); return run(a_t, MT, mu, 6)
    if mu >= MB_TH: return run(AS_MZ, MZ, mu, 5)
    a_b = run(AS_MZ, MZ, MB_TH, 5)
    if mu >= 1.273: return run(a_b, MB_TH, mu, 4)
    a_c = run(a_b, MB_TH, 1.273, 4); return run(a_c, 1.273, mu, 3)

def run_C4(M, mu, gamma=-16.0):
    """LO: C(mu) = C(M) prod [alpha(hi)/alpha(lo)]^(gamma/(2 beta0)) across thresholds (M >= mu)."""
    pts = [M] + [t for t in (MT, MB_TH) if mu < t < M] + [mu]
    f = 1.0
    for hi, lo in zip(pts[:-1], pts[1:]):
        mid = np.sqrt(hi * lo); nf = 6 if mid > MT else (5 if mid > MB_TH else 4)
        f *= (alpha_s(hi) / alpha_s(lo)) ** (gamma / (2 * b0(nf)))
    return f

HBAR = 6.582119569e-25  # GeV s
MESON = {  # m_P, f_P (GeV), (m_q1+m_q2) at mu_had (GeV), B4, mu_had, dm_exp (GeV), allowances (Re, Im) as fractions
    'K':  dict(m=0.497611, f=0.1557, mq=0.0908, B4=0.903, mu=3.0, dm=3.484e-15, eps=2.228e-3),
    'D':  dict(m=1.86484, f=0.2120, mq=0.990, B4=1.0, mu=3.0, dm=0.00407 * HBAR / 410.3e-15),
    'Bd': dict(m=5.27966, f=0.1900, mq=4.183, B4=1.0, mu=4.183, dm=0.5069e12 * HBAR),
    'Bs': dict(m=5.36692, f=0.2303, mq=4.263, B4=1.0, mu=4.183, dm=17.765e12 * HBAR),
}

def me_Q4(P):
    d = MESON[P]
    return 0.5 * (d['m'] / d['mq'])**2 * d['m']**2 * d['f']**2 * d['B4']

def direct_ratios(z_over_M2, P, M):
    """z_over_M2 = sum Yhat Yhat* / M^2 (GeV^-2) at scale M.  Returns observable/allowance ratios (>1 fails)."""
    d = MESON[P]
    C = -z_over_M2 * run_C4(M, d['mu'])
    M12 = C * me_Q4(P) / (2 * d['m'])
    out = {}
    if P == 'K':
        out['dmK'] = abs(2 * M12.real) / d['dm']
        out['epsK'] = 0.94 * abs(M12.imag) / (np.sqrt(2) * d['dm']) / (0.2 * d['eps'])
    elif P == 'D':
        out['dmD'] = abs(2 * M12) / d['dm']
        out['phiD'] = abs(2 * M12.imag) / (0.1 * d['dm'])
    else:
        out['dm' + P] = abs(2 * M12) / (0.3 * d['dm'])
    return out
