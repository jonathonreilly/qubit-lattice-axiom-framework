"""R19-27 (a)-(b): the state-dependent vacuum enthalpy on V1, with per-site (H-cov-dilated) versus Lorentz-invariant counterterms.

Setting: R19-21's D1 root Dirac edge (b_f, r) = (0.915438682, 0.568280847), Wilson-type mass, per 4-component field,
zero-point e(mu) = -2<E>, E^2 = sum S^2 + (mu + sum W)^2 (lattice units, per cell).  H-cov dilation (same law at a new spacing,
the hypothesis of R19-21's p = (e - m e')/3): rho_sea(n, m) = e(m l)/l^4, l = n^{-1/3}, m physical.
Identity E1 (r1927_identities): W = n d rho/dn.  Taylor: e(mu) = e0 + eps1 mu + eps2 mu^2 + eps3 mu^3 + O(mu^4 log mu), and the
mu^k term scales as n^{(4-k)/3}, so W_k = ((4-k)/3) rho_k.
  * LI counterterm (fixed in physical units, w = -1): W_ct = 0, so the state-dependent W is the sea's: R19-21's Delta W.
  * per-site counterterm (fixed in lattice units, same law at a new spacing): rho_ct = -sum_{k<=3} eps_k (m l)^k / l^4 has the same
    n-scaling term by term, so W_ct cancels W_sea through k = 3; the remainder is the n^0 (LI) CW term m^4 log(m l).
Checks: (1) eps_1..eps_3 and grid convergence; (2) FD-in-n enthalpy of the state-dependent part for both schemes at moderate mu,
the per-site/LI ratio scaling ~ mu^3; (3) the remainder is CW-like: R(mu)/mu^4 vs log mu slope ~ -1/(8 pi^2) (approximate).
"""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'recheck', 'arch', 'R18-5'))
from dirac import D1, kgrid
law = D1(0.915438682, 0.568280847)
out = []
def P(s):
    print(s, flush=True); out.append(s)
def bz(N, f):
    """BZ mean of f(X, Wt) chunked over the first axis (memory)."""
    k = kgrid(N); s, w = law.S(k), law.W(k)
    tot = 0.0
    S23 = s[None, :, None]**2 + s[None, None, :]**2; W23 = w[None, :, None] + w[None, None, :]
    for i in range(N):
        tot += f(s[i]**2 + S23, w[i] + W23).sum()
    return tot / N**3
def e_of(mu, N): return bz(N, lambda X, Wt: -2*np.sqrt(X + (mu + Wt)**2))
P('D1 root edge (b_f, r) = (0.915438682, 0.568280847); W vanishes for |k| < b_f = %.3f (IR is pure Dirac)' % law.b)
P('(1) Taylor coefficients of e(mu) = -2<E> per 4-component field (BZ means):')
co = {}
for N in (64, 96, 128):
    e0 = e_of(0.0, N)
    e1 = bz(N, lambda X, Wt: -2*Wt/np.sqrt(X + Wt**2))
    e2 = bz(N, lambda X, Wt: -X/(X + Wt**2)**1.5)
    e3 = bz(N, lambda X, Wt: X*Wt/(X + Wt**2)**2.5)
    co[N] = (e0, e1, e2, e3)
    P('  N=%3d: e0 = %+.7f  eps1 = %+.7f  eps2 = %+.6f  eps3 = %+.6f' % (N, e0, e1, e2, e3))
e0, eps1, eps2, eps3 = co[128]
P('  (R19-21 r1921_enthalpy.out: e0 = -3.2055621, eps1 = e\'(0) = -0.6923204 -> reproduced)')
P('  n-scaling: eps1 term ~ n^1 (w = 0), eps2 ~ n^(2/3) (w = -1/3), eps3 ~ n^(1/3) (w = -2/3); W_k = ((4-k)/3) rho_k')

P('\n(2) state-dependent enthalpy Delta W = W(n; m) - W(n; 0) by finite differences in n (lattice sums at mu = m n^(-1/3)), N = 128, n0 = 1:')
N = 128; dl = 2e-3
def rho_state(n, m, scheme):
    l = n**(-1/3); mu = m*l
    r = (e_of(mu, N) - e0)/l**4
    if scheme == 'site': r -= (eps1*mu + eps2*mu**2 + eps3*mu**3)/l**4      # counterterm fixed in lattice units
    elif scheme == 'LI': r -= (eps1*m + eps2*m**2 + eps3*m**3)              # fixed in physical units, tuned at n0 = 1 (l0 = 1)
    return r
rows = []
for m in (0.4, 0.2, 0.1, 0.05):
    res = {}
    for sch in ('none', 'LI', 'site'):
        rp, rm, r0 = rho_state(np.exp(dl), m, sch), rho_state(np.exp(-dl), m, sch), rho_state(1.0, m, sch)
        res[sch] = (r0, (rp - rm)/(2*dl))                                  # (rho_state, W_state = d rho/d ln n)
    rows.append((m, res))
    P('  m l0 = %.3f:  sea only: rho %+.3e W %+.3e | LI ct: rho %+.3e W %+.3e | per-site ct: rho %+.3e W %+.3e | W_site/W_LI = %+.2e'
      % (m, res['none'][0], res['none'][1], res['LI'][0], res['LI'][1], res['site'][0], res['site'][1], res['site'][1]/res['LI'][1]))
P('  check W_LI = eps1 m + (2/3) eps2 m^2 + (1/3) eps3 m^3 + O(m^4):')
for m, res in rows:
    pred = eps1*m + (2/3)*eps2*m**2 + (1/3)*eps3*m**3
    P('    m = %.3f: W_LI %+.6e  predicted %+.6e  (diff %.1e ~ m^4 = %.1e)' % (m, res['LI'][1], pred, res['LI'][1] - pred, m**4))
rat = [abs(r['site'][1]/r['LI'][1]) for _, r in rows]; ms = [m for m, _ in rows]
sl = np.polyfit(np.log(ms), np.log(rat), 1)[0]
P('  log-log slope of |W_site/W_LI| vs m: %.2f  (mu^3 x log expected: ~3)' % sl)

P('\n(3) the remainder R(mu) = e(mu) - e0 - eps1 mu - eps2 mu^2 - eps3 mu^3 (per-site scheme leaves only this):')
P('    continuum Coleman-Weinberg comparator (RECALLED): R ~ -(1/8 pi^2) mu^4 log mu + B mu^4, slope -1/(8pi^2) = %.5f' % (-1/(8*np.pi**2)))
for N2 in (96, 128, 160):
    c = (e_of(0.0, N2), bz(N2, lambda X, Wt: -2*Wt/np.sqrt(X + Wt**2)), bz(N2, lambda X, Wt: -X/(X + Wt**2)**1.5), bz(N2, lambda X, Wt: X*Wt/(X + Wt**2)**2.5))
    mus = np.array([0.15, 0.2, 0.3, 0.4]); R = np.array([e_of(mu, N2) - c[0] - c[1]*mu - c[2]*mu**2 - c[3]*mu**3 for mu in mus])
    s, b = np.polyfit(np.log(mus), R/mus**4, 1)
    P('    N=%3d: R/mu^4 at mu = %s: %s ; fitted slope d(R/mu^4)/d log mu = %+.5f' % (N2, mus, np.array2string(R/mus**4, precision=5), s))

# ---- physical numbers at l = l_P (as R19-21) ----
MP = 1.22089e19; rhoL = 1.134e-123
dirac = {'t': (172.69, 3), 'b': (4.18, 3), 'c': (1.27, 3), 's': (0.0934, 3), 'd': (0.00467, 3), 'u': (0.00216, 3),
         'tau': (1.77686, 1), 'mu': (0.10566, 1), 'e': (0.000511, 1)}
S1 = sum(n*m for m, n in dirac.values())/MP; S4 = sum(n*m**4 for m, n in dirac.values())          # S4 in GeV^4
P('\n(4) physical sizes, l = l_P (R19-21 masses), symmetric phase minus broken phase:')
P('  LI counterterms:        Delta W = -eps1 sum(n m l) = %+.3e per cell = %.2e rho_Lambda  (R19-21: +3.043e-17, 2.68e106)' % (-eps1*S1, -eps1*S1/rhoL))
P('  per-site counterterms:  Delta W (powers k = 1..3) = 0 identically; log level W_4 = sum n m^4/(24 pi^2) = %.3e GeV^4' % (S4/(24*np.pi**2)))
rr = (np.pi**2/30)*106.75*159.5**4
P('    vs rho_rad(T_c = 159.5 GeV) = %.3e GeV^4: ratio %.1e (zero under the full line of constant physics)' % (rr, S4/(24*np.pi**2)/rr))
# LI counterterm: Higgs tadpole drift on V1
v, mH = 246.22, 125.25; S1G = sum(n*m for m, n in dirac.values())
for lab, ell in (('l = l_P', 1/MP), ('l = (1 TeV)^-1', 1e-3), ('l = (10 GeV)^-1', 0.1)):
    dlnv = 3*abs(eps1)*S1G/(ell**3*mH**2*v**2)
    P('  LI counterterms, %-16s: |d ln v / d ln a| from the uncancelled tadpole drift = %.2e per e-fold' % (lab, dlnv))
ell_min = (3*abs(eps1)*S1G/(mH**2*v**2*1.4e-6))**(1/3)
P('  needs l > %.2f GeV^-1 = %.2e m to keep |d ln v/d ln a| < 1.4e-6 (clock-level, RECALLED: |mu_dot/mu| ~ 1e-16/yr over H0)' % (ell_min, ell_min*1.9733e-16))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
