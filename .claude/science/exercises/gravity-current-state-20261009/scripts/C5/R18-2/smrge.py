"""R18-2 SM running module (two-loop RGEs, one-loop lambda_eff).

Conventions: V = lam (|H|^2 - v^2/2)^2, m_h^2 = 2 lam v^2 at tree level; gY = SM hypercharge coupling
(g1_GUT = sqrt(5/3) gY); t = ln(mu/GeV).  All beta-function coefficients are my transcription of the
standard two-loop SM results (Machacek-Vaughn / Luo-Wang-Xiao / Buttazzo et al. appendix): RECALLED.
Matching at mu = M_t: Buttazzo et al. 2013 NNLO fit formulas: RECALLED.

Optional extras (used by probes c, d):
  - real singlet S with V += (lHS/2)|H|^2 S^2 + (lS/4) S^4 above m_S (one-loop for singlet couplings);
  - n5 vector-like Dirac fermions in the SU(5) 5-rep above M_F (one-loop gauge shift db_i = 2/3 each).
"""
import numpy as np
from scipy.integrate import solve_ivp

K = 1.0 / (16 * np.pi**2)
MP = 1.22089e19         # 1/a for a = l_P (Planck mass), GeV
MPRED = 2.435e18        # reduced Planck mass (sensitivity only)


def matching(Mt, Mh, als, MW=80.369):
    """Buttazzo et al. 2013 NNLO MS-bar couplings at mu = M_t (RECALLED fit formulas)."""
    dt = Mt - 173.34
    das = (als - 0.1184) / 0.0007
    dW = (MW - 80.384) / 0.014
    lam = 0.12604 + 0.00206 * (Mh - 125.15) - 0.00004 * dt
    yt = 0.93690 + 0.00556 * dt - 0.00042 * das
    g3 = 1.1666 + 0.00314 * das - 0.00046 * dt
    g2 = 0.64779 + 0.00004 * dt + 0.00011 * dW
    gY = 0.35830 + 0.00011 * dt - 0.00020 * dW
    return np.array([gY, g2, g3, yt, lam])


def beta_sm(y, loops=2):
    gY, g2, g3, yt, lam = y[:5]
    a, b, c, t2, L = gY**2, g2**2, g3**2, yt**2, lam
    bgY = K * 41 / 6 * gY**3
    bg2 = K * (-19 / 6) * g2**3
    bg3 = K * (-7) * g3**3
    byt = K * yt * (4.5 * t2 - 17 / 12 * a - 9 / 4 * b - 8 * c)
    blam = K * (24 * L**2 - 6 * t2**2 + 3 / 8 * (2 * b**2 + (b + a)**2) + L * (12 * t2 - 9 * b - 3 * a))
    if loops >= 2:
        K2 = K**2
        bgY += K2 * gY**3 * (199 / 18 * a + 4.5 * b + 44 / 3 * c - 17 / 6 * t2)
        bg2 += K2 * g2**3 * (1.5 * a + 35 / 6 * b + 12 * c - 1.5 * t2)
        bg3 += K2 * g3**3 * (11 / 6 * a + 4.5 * b - 26 * c - 2 * t2)
        byt += K2 * yt * (-12 * t2**2 + t2 * (131 / 16 * a + 225 / 16 * b + 36 * c - 12 * L) + 6 * L**2
                          + 1187 / 216 * a**2 - 0.75 * a * b + 19 / 9 * a * c - 23 / 4 * b**2 + 9 * b * c - 108 * c**2)
        blam += K2 * (-312 * L**3 - 144 * L**2 * t2 - 3 * L * t2**2 + 30 * t2**3 + 80 * L * c * t2 - 32 * c * t2**2
                      + L**2 * (108 * b + 36 * a) + L * t2 * (22.5 * b + 85 / 6 * a)
                      - 73 / 8 * L * b**2 + 39 / 4 * L * a * b + 629 / 24 * L * a**2
                      - 8 / 3 * a * t2**2 - 9 / 4 * b**2 * t2 + 21 / 2 * a * b * t2 - 19 / 4 * a**2 * t2
                      + 305 / 16 * b**3 - 289 / 48 * b**2 * a - 559 / 48 * b * a**2 - 379 / 48 * a**3)
    return [bgY, bg2, bg3, byt, blam]


def gamma_h(y):
    gY, g2, g3, yt = y[:4]
    return K * (3 * yt**2 - 9 / 4 * g2**2 - 3 / 4 * gY**2)


def rhs_factory(loops=2, singlet=None, n5=0, MF=None):
    """singlet = dict(mS=..) : singlet couplings are y[5]=lHS, y[6]=lS, active for mu > mS.
    n5 vector-like Dirac 5-plets active for mu > MF (one-loop gauge shift)."""
    def rhs(t, y):
        db = beta_sm(y, loops)
        out = list(db) + [0.0, 0.0, 0.0]
        gY, g2, g3, yt, lam = y[:5]
        # Higgs field anomalous dimension integral Gamma (one loop)
        out[7] = gamma_h(y)
        if n5 and t > np.log(MF):
            dbi = 2.0 / 3.0 * n5
            # GUT-normalized db1 = 2/3 n5  ->  SM-normalized dbY = (5/3) * 2/3 n5
            out[0] += K * (5.0 / 3.0) * dbi * gY**3
            out[1] += K * dbi * g2**3
            out[2] += K * dbi * g3**3
        if singlet is not None and t > np.log(singlet['mS']):
            lHS, lS = y[5], y[6]
            out[4] += K * 0.5 * lHS**2
            out[5] = K * lHS * (12 * lam + 6 * lS + 4 * lHS + 6 * yt**2 - 4.5 * g2**2 - 1.5 * gY**2)
            out[6] = K * (18 * lS**2 + 2 * lHS**2)
        return out
    return rhs


def run(Mt, Mh, als, mu_max=1e20, loops=2, singlet=None, n5=0, MF=None, npts=600, MW=80.369):
    """Run from M_t to mu_max. For the singlet, the tree-level threshold
    lam_H = lam_SM + lHS^2/(4 lS) is applied at mu = mS (two-stage integration)."""
    y0 = list(matching(Mt, Mh, als, MW)) + [0.0, 0.0, 0.0]
    t0, t1 = np.log(Mt), np.log(mu_max)
    ts = np.linspace(t0, t1, npts)
    f = rhs_factory(loops, singlet, n5, MF)
    if singlet is None:
        sol = solve_ivp(f, (t0, t1), y0, t_eval=ts, rtol=1e-9, atol=1e-12, method='DOP853')
        return sol.t, sol.y
    tS = np.log(singlet['mS'])
    ts1 = ts[ts < tS]
    s1 = solve_ivp(f, (t0, tS), y0, t_eval=np.append(ts1, tS), rtol=1e-9, atol=1e-12, method='DOP853')
    yS = s1.y[:, -1].copy()
    lHS, lS = singlet['lHS'], singlet['lS']
    yS[4] = yS[4] + lHS**2 / (4 * lS)
    yS[5], yS[6] = lHS, lS
    ts2 = ts[ts > tS]
    s2 = solve_ivp(f, (tS, t1), yS, t_eval=np.insert(ts2, 0, tS), rtol=1e-9, atol=1e-12, method='DOP853')
    T = np.concatenate([s1.t[:-1], s2.t])
    Y = np.concatenate([s1.y[:, :-1], s2.y], axis=1)
    return T, Y


def lam_eff(T, Y, oneloop=True):
    """One-loop Landau-gauge lambda_eff(h) at mu = h (top, W, Z; Goldstone/Higgs dropped),
    times exp(4 Gamma). V_eff ~ lam_eff h^4 / 4."""
    gY, g2, g3, yt, lam = Y[:5]
    Gam = Y[7]
    le = lam.copy()
    if oneloop:
        a, b, t2 = gY**2, g2**2, yt**2
        le = le + K * (-3 * t2**2 * (np.log(t2 / 2) - 1.5)
                       + 3 / 8 * b**2 * (np.log(b / 4) - 5 / 6)
                       + 3 / 16 * (a + b)**2 * (np.log((a + b) / 4) - 5 / 6))
    return np.exp(4 * Gam) * le, le
