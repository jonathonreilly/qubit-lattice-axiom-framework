"""TW-2 (b): one-loop U(1) additive-mass strain response of the TASTE-SPLIT staggered edge, under SF, converged.

Law (tw2_alg.py): H8(k) = sum_j s(k_j) Gamma_j + m Gamma_eps + sigma cos k1 cos k2 M_110,  s = SymS(0.909103708), r = 0;
dictionary (checked, tw2_alg.out item 2): U M_110 U^dag = beta x (n3.tau), so in the n3.tau eigenbasis the 8x8 one-loop problem at P = 0
splits EXACTLY into two 4x4 F1/F3 problems (taste-blind photon, Psym vertices built linearly from H at cube corners):
   block tau = +-1:  D_tau(k) = i g.s(k) + M_tau(k),  M_tau(k) = m + tau sigma cos k1 cos k2.
At k = 0 block + has mass m + sigma (the heavy twin, e.g. mu), block - has m - sigma (the light twin, e.g. e).
One loop, Feynman gauge, P = 0, Psym, U = 1, photon Gph(2.9435) with its own separable SF flow, F1's octant panel quadrature (f3_lib.dm_gen).
Strain: uniform diagonal h = diag(h1, h2, h3) in SF units t (v = (t/2) h.p, time-1 map).  Fermion flow branch FB1 = the taste-blind staggered
band E^2 = sum s^2 (separable per-axis flows; NF-1's flow).  FB2 (each split band's own flow) differs from FB1 only through
M dM = (m + tau sigma g)(tau sigma dg): O(sigma^2, m sigma), so the O(sigma) coefficient B below is branch-independent (proved).
Strains:  'Eg'  = diag(1, -1, 0)            (NF-1/F1's registered E_g strain; B1-type under the split law's D4[001])
          'tet' = diag(-1, -1, 2)/sqrt(3)   (the other E_g component, same Q_E normalisation; A1 under D4[001] -> linear term allowed)
Coefficients (per e^2):  Sigma_tau(m, sigma; t) ~ m A(t) + tau sigma B(t) + O(mass^2);  A = singlet (NF-1's z), B = taste-split.
Light twin:  dm_light = m_l A + sigma (A - B)  with m = m_l + sigma  ->  the LEAK is  sigma (A - B), its strain parts sigma (A' - B') t + sigma (A'' - B'') t^2/2.
argv: part n hmax mph d    part in {S (singlet A), T (split B), L (light block at m = sigma + m_l), FB2}"""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
import f1_lib as L
from f3_lib import dm_gen, mkgrid
from sublum import SymS
t00 = time.time()
part = sys.argv[1]; n, hm, mph, d = int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
BF = L.ROOT[0]
A = SymS(BF); G = L.Phot(L.CPH)
g = mkgrid(BF, n, hm, mph); x, w = g.x, g.w
NRK = 4
STRAINS = {'Eg': (1.0, -1.0, 0.0), 'tet': tuple(v/np.sqrt(3) for v in (-1.0, -1.0, 2.0))}
print('TW-2 part %s; grid n=%d hmax=%.2f mph=%d (%d nodes), d=%.4f, RK4 steps %d; staggered s = SymS(%.9f), photon Gph(%.4f); per e^2, SF units'
      % (part, n, hm, mph, len(x), d, NRK, BF, L.CPH), flush=True)
allv = np.concatenate([-x[::-1], [0.0], x])


def phi1(k, th):
    """1D SF flow (time-1 map) of the taste-blind staggered band along an axis with strain rate th = t h_j."""
    if th == 0.0:
        return np.array(k, float)
    def f(y):
        return (0.5*th*A.s(y[0])*A.ds(y[0]),)
    return L.rk4(f, (np.array(k, float),), NRK)[0]


def make_cM(t, h, m, sig, tau):
    """block-tau symbol (cx, cy, cz, M) at the FB1-flowed momentum; flows tabulated on the node set (calls use nodes, 0, -nodes only)."""
    tabs = [np.interp if False else None]*3
    fl = [phi1(allv, t*hj) for hj in h]                       # odd flows, tabulated
    sv = [A.s(f_) for f_ in fl]; cv = [np.cos(f_) for f_ in fl]
    def lut(j, k, arr):
        return np.interp(k, allv, arr)
    def cM(kx, ky, kz):
        kx = kx + 0*ky + 0*kz; ky = ky + 0*kx + 0*kz; kz = kz + 0*kx + 0*ky
        c = (lut(0, kx, sv[0]), lut(1, ky, sv[1]), lut(2, kz, sv[2]))
        M = m + tau*sig*lut(0, kx, cv[0])*lut(1, ky, cv[1])
        return c[0], c[1], c[2], M
    return cM


def photon(t, h):
    return tuple(G.d(L.flowG1(G, x, hj, t, NRK)) if (t != 0 and hj != 0) else G.d(x) for hj in h)


def dm(t, h, m, sig, tau):
    return dm_gen(make_cM(t, h, m, sig, tau), *photon(t, h), x, w)


def resp(h, m, sig, tau, odd=False):
    """f0, Hessian (Richardson over d, 2d), and if odd: first derivative (Richardson) and the odd remainder."""
    f0 = dm(0.0, h, m, sig, tau)
    fp, fm = dm(d, h, m, sig, tau), (dm(-d, h, m, sig, tau) if odd else None)
    fp2, fm2 = dm(2*d, h, m, sig, tau), (dm(-2*d, h, m, sig, tau) if odd else None)
    if not odd:
        fm, fm2 = fp, fp2                                   # evenness (checked separately where claimed)
    h1 = (fp - 2*f0 + fm)/d**2; h2 = (fp2 - 2*f0 + fm2)/(2*d)**2
    g1 = (fp - fm)/(2*d); g2 = (fp2 - fm2)/(4*d)
    return f0, (4*h1 - h2)/3, (4*g1 - g2)/3, h1, h2


if part == 'S':          # singlet coefficient A = Sigma(m)/m, both strains (A' must vanish by cubic symmetry of the singlet law)
    for sn in ('Eg', 'tet'):
        h = STRAINS[sn]; out = {}
        for m in (0.0, 0.0025, 0.005, 0.01):
            f0, H, G1, h1, h2 = resp(h, m, 0.0, +1, odd=(sn == 'tet'))
            out[m] = (f0, H, G1)
            print('  %s m=%.4f: Sigma %+.10f  Hess %+.7e (d %+.7e, 2d %+.7e)  dSigma/dt %+.3e' % (sn, m, f0, H, h1, h2, G1), flush=True)
        for m in (0.0025, 0.005, 0.01):
            print('  %s m=%.4f: A = %+.6f   A\'\' = %+.6e   A\' = %+.2e' % (sn, m, (out[m][0] - out[0.0][0])/m, (out[m][1] - out[0.0][1])/m,
                                                                          (out[m][2] - out[0.0][2])/m))
elif part == 'T':        # split coefficient B = Sigma_+(m=0, sigma)/sigma
    for sn in ('Eg', 'tet'):
        h = STRAINS[sn]
        for sig in (0.0025, 0.005, 0.01, 0.02):
            f0, H, G1, h1, h2 = resp(h, 0.0, sig, +1, odd=(sn == 'tet'))
            fm0 = dm(0.0, h, 0.0, sig, -1)
            print('  %s sigma=%.4f: Sigma_+ %+.10f (Sigma_- %+.10f, sum %.1e)  B = %+.6f  B\'\' = %+.6e  B\' = %+.6e   (d %+.4e, 2d %+.4e)'
                  % (sn, sig, f0, fm0, f0 + fm0, f0/sig, H/sig, G1/sig, h1/sig, h2/sig), flush=True)
elif part == 'L':        # the light block directly at m = sigma + m_l
    for sn in ('Eg', 'tet'):
        h = STRAINS[sn]
        for sig, ml in ((0.01, 0.0), (0.01, 0.0005), (0.005, 0.0)):
            f0, H, G1, h1, h2 = resp(h, sig + ml, sig, -1, odd=(sn == 'tet'))
            print('  %s light block: sigma=%.4f m_l=%.4f (m=%.4f): Sigma_light %+.10f  Hess %+.7e  dSigma/dt %+.4e ; per sigma: %+.6f, %+.6e, %+.6e'
                  % (sn, sig, ml, sig + ml, f0, H, G1, f0/sig, H/sig, G1/sig), flush=True)
elif part == 'EV':       # evenness check of the E_g response for the split law (C2[110]-type symmetry claim)
    h = STRAINS['Eg']
    for tau in (+1, -1):
        a, b = dm(0.01, h, 0.0, 0.01, tau), dm(-0.01, h, 0.0, 0.01, tau)
        print('  Eg evenness, sigma = 0.01 block %+d: dm(+0.01) %+.14f dm(-0.01) %+.14f diff %.1e' % (tau, a, b, a - b))


SYMS = {   # functions of the flowed momenta (f1, f2, f3); every one keeps the folding sign of its class
    'one': lambda f: 1.0 + 0*f[0]*f[1]*f[2],
    'c1c2': lambda f: np.cos(f[0])*np.cos(f[1]),                                   # mass family, class 110 (main)
    'c1c2_c2k3': lambda f: np.cos(f[0])*np.cos(f[1])*np.cos(2*f[2]),               # range variant (class 110)
    'c1c2_c2k12': lambda f: np.cos(f[0])*np.cos(f[1])*0.5*(np.cos(2*f[0]) + np.cos(2*f[1])),   # range variant (class 110)
    'c1c2c3': lambda f: np.cos(f[0])*np.cos(f[1])*np.cos(f[2]),                    # twisted singlet (class 111, body diagonal)
    'c3': lambda f: np.cos(f[2]),                                                  # twisted triplet along 3 (class 001, NN hop)
}


def make_cM_g(t, h, m, gs, sig, gt, tau):
    """block symbol with M(k) = m gs(Phi k) + tau sig gt(Phi k) (FB1 flow, node-tabulated)."""
    fl = [phi1(allv, t*hj) for hj in h]
    def cM(kx, ky, kz):
        kx = kx + 0*ky + 0*kz; ky = ky + 0*kx + 0*kz; kz = kz + 0*kx + 0*ky
        f = (np.interp(kx, allv, fl[0]), np.interp(ky, allv, fl[1]), np.interp(kz, allv, fl[2]))
        c = (A.s(f[0]), A.s(f[1]), A.s(f[2]))
        M = m*SYMS[gs](f) + tau*sig*SYMS[gt](f)
        return c[0], c[1], c[2], M
    return cM


def resp_g(h, m, gs, sig, gt, tau):
    f = lambda t: dm_gen(make_cM_g(t, h, m, gs, sig, gt, tau), *photon(t, h), x, w)
    f0, fp, fm, fp2, fm2 = f(0.0), f(d), f(-d), f(2*d), f(-2*d)
    h1 = (fp - 2*f0 + fm)/d**2; h2 = (fp2 - 2*f0 + fm2)/(2*d)**2
    g1 = (fp - fm)/(2*d); g2 = (fp2 - fm2)/(4*d)
    return f0, (4*h1 - h2)/3, (4*g1 - g2)/3


if part == 'RV':         # per-unit coefficients of each symbol (m = 0, sigma small): coefficient C = Sigma/sigma, C'', C'
    s0 = 0.005
    for gt in ('c1c2', 'c1c2_c2k3', 'c1c2_c2k12', 'one', 'c1c2c3', 'c3'):
        for sn in ('Eg', 'tet'):
            f0, H, G1 = resp_g(STRAINS[sn], 0.0, 'one', s0, gt, +1)
            print('  symbol %-11s %-3s: C = %+.6f  C\'\' = %+.6e  C\' = %+.6e   (sigma = %.4f)' % (gt, sn, f0/s0, H/s0, G1/s0, s0), flush=True)
print('time %.0f s' % (time.time() - t00))
