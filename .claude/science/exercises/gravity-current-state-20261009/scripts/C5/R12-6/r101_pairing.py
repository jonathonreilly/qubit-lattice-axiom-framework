"""R10-1 check 3 (REFUTED-direction attempt): boson-fermion pairing of the photon one-loop speed moment.

Clifford-flat Dirac field: h(k) = sum_j [S(k_j) alpha_j + W(k_j) beta_j] + m beta_0, with 7 mutually anticommuting
Hermitian matrices (8 components per site), so the velocities obey {d_j h, d_l h} = 2 delta_jl exactly iff each
curve c(k) = (S(k), W(k)) has unit speed: S'^2 + W'^2 = 1 (a = 0) and different axes use different Clifford
directions (c1 = c2 = 0).  Then eps^2 = m^2 + sum_j v(k_j), v = S^2 + W^2.
Matched complex scalar: separable band u = v (same curve), same or different mass.
Prediction (from r101_dirac_symbolic.out and Theorem T'): per 4 fermion components,
   dc_gamma(Dirac) = -<A X^2/(4E^5)>,  dc_gamma(scalar) = (1/32)<v'(k_y)^2 A/eps^5> = <A X^2/(8 eps^5)>,
so 1 Dirac(4 comp) + 2 complex scalars (or 8 comp + 4 scalars) cancel POINTWISE in k for every shape.
Both sides are computed here DIRECTLY (static P_E / P_M, finite q, Richardson), not from the moment formulas.

Curves: (W1) Wilson circle S = sin k, W = 1 - cos k (no box; v = NN Laplacian 4 sin^2(k/2));
        (BOX) unit-speed curve with S = k, W = 0 exactly on |k| <= b1: heading theta(k) = (1-rho(k))(k + c sin k),
              c fixed by closure  int cos theta = 0 (so S is periodic), rho = C^inf plateau (1 on |k|<=b1, 0 beyond b2).
Control: R8-5's BQ law (shared beta, S'^2 + W'^2 != 1): no matched scalar exists; we report its residual.
"""
import numpy as np, sys, time
from scipy.optimize import brentq
sys.path.insert(0, '.')
from r85_box_qed_copy import plateau, Law

U = 16 * np.pi ** 2

def make_box_curve(b1, b2, NG=200001):
    kg = np.linspace(-np.pi, np.pi, NG)
    rho = plateau(kg, b1, b2)
    def theta(c):
        return (1 - rho) * (kg + c * np.sin(kg))
    def closure(c):
        return np.trapezoid(np.cos(theta(c)), kg)
    c = brentq(closure, 0.0, 1.0)
    th = theta(c)
    cs, sn = np.cos(th), np.sin(th)
    dk = kg[1] - kg[0]
    S = np.concatenate([[0.0], np.cumsum(0.5 * (cs[1:] + cs[:-1]) * dk)]); S -= np.interp(0.0, kg, S)
    W = np.concatenate([[0.0], np.cumsum(0.5 * (sn[1:] + sn[:-1]) * dk)]); W -= np.interp(0.0, kg, W)
    from scipy.interpolate import CubicSpline
    fS, fW = CubicSpline(kg, S), CubicSpline(kg, W)
    fc, fs = CubicSpline(kg, cs), CubicSpline(kg, sn)
    wrap = lambda k: (k + np.pi) % (2 * np.pi) - np.pi
    curve = dict(S=lambda k: fS(wrap(k)), W=lambda k: fW(wrap(k)),
                 Sp=lambda k: fc(wrap(k)), Wp=lambda k: fs(wrap(k)), c=c,
                 Sgap=float(S[-1] - S[0]), minabs=float(np.min(np.hypot(S, W)[np.abs(kg) > 0.3])))
    return curve

def wilson_curve():
    return dict(S=np.sin, W=lambda k: 1 - np.cos(k), Sp=np.cos, Wp=np.sin, c=None, Sgap=0.0, minabs=None)

def direct_dirac_flat(cur, m, N, ns=(1, 2, 4)):
    """Direct static P_E and P_M (R8-5 formulas, r85_box_qed.py:81-118) with Clifford vectors of dimension 7:
    h = (Sx, Sy, Sz, Wx, Wy, Wz, m); x = dh/dk_y = (0, S'(ky), 0, 0, W'(ky), 0, 0).  Normalized per 4 components."""
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, W, Sp, Wp = cur['S'](k), cur['W'](k), cur['Sp'](k), cur['Wp'](k)
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    def hv(sx):
        return [S[(IX + sx) % N], S[IY], S[IZ], W[(IX + sx) % N], W[IY], W[IZ], m + 0 * IX]
    h0 = hv(0)
    E = np.sqrt(sum(c * c for c in h0))
    n0 = [c / E for c in h0]
    xvec = [0, Sp[IY], 0, 0, Wp[IY], 0, 0]
    x2 = Sp[IY] ** 2 + Wp[IY] ** 2
    xn = sum(a * b for a, b in zip(xvec, n0) if not np.isscalar(a))
    PE = np.mean((x2 - xn ** 2) / (2 * E ** 3))
    chi0 = np.mean(2 * (x2 - xn ** 2) / E)
    PMs = []
    for s in ns:
        tot = 0.0
        for sg in (+1, -1):
            h2 = hv(sg * s); E2 = np.sqrt(sum(c * c for c in h2)); n2 = [c / E2 for c in h2]
            nn = sum(a * b for a, b in zip(n0, n2))
            xn2 = sum(a * b for a, b in zip(xvec, n2) if not np.isscalar(a))
            tot += np.mean((x2 * (1 + nn) - 2 * xn * xn2) / (E + E2))
        q = 2 * np.pi * s / N
        PMs.append((chi0 - tot) / q ** 2)
    r1 = (4 * PMs[0] - PMs[1]) / 3; r2 = (4 * PMs[1] - PMs[2]) / 3
    PM = (16 * r1 - r2) / 15
    return (PM - PE) / 2, PE

def direct_scalar(cur, m, N, ns=(1, 2, 4)):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, W, Sp, Wp = cur['S'](k), cur['W'](k), cur['Sp'](k), cur['Wp'](k)
    u = S ** 2 + W ** 2; up = 2 * (S * Sp + W * Wp)
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    eps = np.sqrt(m * m + u[IX] + u[IY] + u[IZ]); w = up[IY] ** 2
    PE = np.mean(w / eps ** 5) / 16
    chi0 = np.mean(w / (4 * eps ** 3))
    PMs = []
    for s in ns:
        ep = np.sqrt(m * m + u[(IX + s) % N] + u[IY] + u[IZ])
        PMs.append((chi0 - np.mean(w / (2 * eps * ep * (eps + ep)))) / (2 * np.pi * s / N) ** 2)
    r1 = (4 * PMs[0] - PMs[1]) / 3; r2 = (4 * PMs[1] - PMs[2]) / 3
    PM = (16 * r1 - r2) / 15
    return (PM - PE) / 2, PE

if __name__ == '__main__':
    t0 = time.time()
    curves = [('Wilson circle (no box)', wilson_curve())]
    for b1, b2 in [(0.5, 1.2), (0.8, 1.6)]:
        cv = make_box_curve(b1, b2)
        curves.append(('box curve b1=%.1f b2=%.1f (c=%.4f, S-closure %.1e, min|c(k)| off 0: %.3f)' % (
            b1, b2, cv['c'], cv['Sgap'], cv['minabs']), cv))
    print('Clifford-flat Dirac (per 4 comp) vs matched complex scalar (u = S^2 + W^2): DIRECT P_M - P_E, x16pi^2')
    print('curve | m_f | m_s | N | dc(Dirac) | dc(scalar) | Dirac + 2*scalar | ratio Dirac/scalar | P_E Dirac + 2 P_E scalar (LI part, adds)')
    for lab, cv in curves:
        # unit-speed check
        kk = np.linspace(-np.pi, np.pi, 2001)
        spd = cv['Sp'](kk) ** 2 + cv['Wp'](kk) ** 2 - 1
        print('# %s : max|S\'^2+W\'^2-1| = %.1e' % (lab, np.max(np.abs(spd))))
        for mf, ms, N in [(0.5, 0.5, 64), (0.5, 0.5, 96), (0.2, 0.2, 96), (0.2, 0.6, 96), (0.05, 0.05, 128)]:
            dD, pD = direct_dirac_flat(cv, mf, N)
            dS, pS = direct_scalar(cv, ms, N)
            print('  %.2f | %.2f | %3d | %+10.6f | %+10.6f | %+.2e | %+8.4f | %+8.4f' % (
                mf, ms, N, dD * U, dS * U, (dD + 2 * dS) * U, dD / dS, (pD + 2 * pS) * U), flush=True)
    # Control: R8-5 BQ Dirac (shared beta, not unit speed): compare with a scalar on the curve (S, W) and m
    print('# control: R8-5 BQ shape S3 (not Clifford-flat).  Its moment pieces are in r101_dirac_moment.out;')
    print('#   no separable scalar band reproduces the a- and mix-moments (they do not involve eps^2 alone).')
    print('elapsed %.1fs' % (time.time() - t0))
