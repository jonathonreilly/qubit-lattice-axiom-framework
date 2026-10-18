"""Addendum to t3_landau (post-hoc analysis of the same model; see REPORT deviations):
D2h onset strain and its Lorentz-violation size, K-criterion radius vs edge, +-10% robustness, BZ convergence."""
import sys, numpy as np
from t3_landau import *
wilson = sys.argv[1] == 'W'; M = int(sys.argv[2]) if len(sys.argv) > 2 else 16
S, C = bz_axis(M); S2, C2 = bz_axis(24)
lams = fib_sphere(120); etas = [1/3, 1/2, 1.0, 2.0, 3.0]
def maxshift(eta, lam, rho):
    v0 = np.ones((3, 3)) + (eta - 1) * np.eye(3); tt = np.linspace(0, 2*np.pi, 361)
    return (np.abs(velocities(eta, lam, rho*np.ones_like(tt), tt) - v0) / v0).max()
def d2h_set(eta, lam, SS, CC):
    R = run_coupling_A(eta, lam, SS, CC, wilson)
    cls = np.array([classify(t) for t in R['tstar']])
    return R, cls
print(f'=== {"A-W" if wilson else "A-N"} detail, M={M} ===')
q4pos = []; c6pos = []; rK_over_edge = []; onset = []; n_any = 0; ntot = 0; cases = []
for eta in etas:
    for li, lam in enumerate(lams):
        R, cls = d2h_set(eta, lam, S, C); ntot += 1
        q4pos.append(R['q'][2] > 0); c6pos.append(R['c'][0] > 0)
        if R['c'][0] > 0:
            rK_over_edge.append((abs(R['b'][0]) / (4 * R['c'][0])) ** (1/3) / R['re'])
        if (cls == 'D2h').any():
            n_any += 1; k = int(np.argmax(cls == 'D2h')); r0 = R['rr'][k]
            onset.append((r0 / R['re'], maxshift(eta, lam, r0)))
            cases.append((eta, lam, R, cls))
rK = np.array(rK_over_edge)
print(f'couplings: {ntot}; q4>0 fraction {np.mean(q4pos):.2f}; c6>0 fraction {np.mean(c6pos):.2f}')
print(f'K radius rho_K=(|b3|/4c6)^(1/3) (sixth-order truncation, c6>0 only) in units of rho_edge: '
      f'quantiles 5/25/50/75/95% = {np.round(np.quantile(rK,[.05,.25,.5,.75,.95]),2)}; fraction rho_K < rho_edge: {np.mean(rK<1):.3f}')
print(f'couplings with ANY admissible rho giving a D2h angular minimum (angle-blind tree potential allowed): {n_any}/{ntot}')
if onset:
    on = np.array(onset)
    print(f'   D2h onset rho/rho_edge: min {on[:,0].min():.2f}, median {np.median(on[:,0]):.2f};  '
          f'max relative fermion-speed shift at onset |dv|/v0: min {on[:,1].min():.2f}, median {np.median(on[:,1]):.2f}')
print('--- robustness (+-10% on each of l1,l2,l3,eta; 8 perturbations) and BZ convergence (M=24) for D2h cases ---')
for eta, lam, R, cls in cases:
    rr = R['rr']; js = np.where(cls == 'D2h')[0]
    surv = 0
    for p in range(4):
        for sgn in (+1, -1):
            lam2 = lam.copy(); eta2 = eta
            if p < 3: lam2[p] *= (1 + 0.1 * sgn)
            else: eta2 = eta * (1 + 0.1 * sgn)
            R2, c2 = d2h_set(eta2, lam2, S, C); surv += (c2 == 'D2h').any()
    R3, c3 = d2h_set(eta, lam, S2, C2)
    print(f'eta={eta:.3g} lam=({lam[0]:+.2f},{lam[1]:+.2f},{lam[2]:+.2f}) D2h for rho/rho_edge in [{rr[js[0]]/R["re"]:.2f},{rr[js[-1]]/R["re"]:.2f}] '
          f't* {np.degrees(R["tstar"][js[0]]):.1f}..{np.degrees(R["tstar"][js[-1]]):.1f} deg; perturbations keeping D2h: {surv}/8; '
          f'M=24: D2h at {int((c3=="D2h").sum())} rho points (M=16: {len(js)}), b3 {R3["b"][0]:+.3g} ({R["b"][0]:+.3g}), c6 {R3["c"][0]:+.3g} ({R["c"][0]:+.3g})')
