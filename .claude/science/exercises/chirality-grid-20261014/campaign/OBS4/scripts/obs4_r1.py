"""OBS-4 C1, C2, R1 (PREREG.md 'Runs'): realisations -> carrier couplings in the mass basis -> M* (INP rows),
D3 and D6 classes, equal-vev point and minimum over vevs, both coupling scales."""
import numpy as np, sys
from scipy.optimize import minimize
from obs4_core import *
np.set_printoptions(precision=4, linewidth=170, suppress=False)
P = lambda *a: print(*a, flush=True)
SQ4PI = np.sqrt(4 * np.pi)

def realisations(extra=None):
    out = {}
    for tag, d120 in (('B-gen', False), ('B-gen120', True)):
        p = np.load(f'univ_{tag.replace("-", "_")}.npz')['p']
        Mu, Md = masses_from_p(p, d120)
        out[tag + '(as fitted)'] = (Mu, Md)
    a = np.load('univ_A_M1.npz')
    for n, name in enumerate(('W_u=F', 'random W_u', 'E1 W_u')):
        Wu, Xu, Xd = a[f'Wu_{n}'], a[f'Xu_{n}'], a[f'Xd_{n}']
        out[f'A-M1#{n} ({name})'] = (Wu @ np.diag(MU) @ Xu.conj().T, Wu @ VPDG @ np.diag(MD) @ Xd.conj().T)
    if extra:
        out.update(extra)
    return out

def check_fit(Mu, Md):
    su = np.linalg.svd(Mu, compute_uv=False)[::-1]; sd = np.linalg.svd(Md, compute_uv=False)[::-1]
    Wu, _, _ = svd_sorted(Mu); Wd, _, _ = svd_sorted(Md)
    Vp = Wu.conj().T @ Wd
    return (np.sort(su) / MU - 1), (np.sort(sd) / MD - 1), np.abs(np.abs(Vp) - np.abs(VPDG)).max(), Jarl(Vp)

def physical(Mu, Md):
    """C1: if J<0 return the complex conjugate (same moduli, physical CP sign)."""
    J = check_fit(Mu, Md)[3]
    return (Mu, Md, False) if J > 0 else (Mu.conj(), Md.conj(), True)

def vev_dicts(cls, t):
    """t: positive weights; D3: (0,x,y,z) shared; D6: (0, xu,yu,zu, xd,yd,zd)."""
    t = np.abs(np.asarray(t, float)); t = t / np.linalg.norm(t) * VEV
    if cls == 'D3':
        v = dict(zip(CARRIERS, t)); return v, v
    vu = {'0': t[0], 'x': t[1], 'y': t[2], 'z': t[3]}; vd = {'0': t[0], 'x': t[4], 'y': t[5], 'z': t[6]}
    return vu, vd

def worst(Pu, Pd, cls, t, scale, Mu, Md, pen=True):
    vu, vd = vev_dicts(cls, t)
    r = mstar_rows(Pu, Pd, vu, vd, scale)
    m = max(r.values())
    if pen:
        mc = max_coupling(Mu * scale, Md * scale, vu, vd)
        if mc > SQ4PI: m *= (mc / SQ4PI) ** 4
    return m, r

def minimise(Pu, Pd, cls, scale, Mu, Md, nstart=40, seed=1):
    rng = np.random.default_rng(seed); n = 4 if cls == 'D3' else 7
    best = None
    for s in range(nstart):
        x0 = rng.uniform(-1.5, 1.5, n)
        f = lambda x: np.log(worst(Pu, Pd, cls, np.exp(x), scale, Mu, Md)[0])
        res = minimize(f, x0, method='Nelder-Mead', options=dict(xatol=1e-6, fatol=1e-8, maxiter=4000))
        if best is None or res.fun < best.fun: best = res
    m, r = worst(Pu, Pd, cls, np.exp(best.x), scale, Mu, Md, pen=False)
    vu, vd = vev_dicts(cls, np.exp(best.x))
    return m, r, vu, vd, max_coupling(Mu * scale, Md * scale, vu, vd)

if __name__ == '__main__':
    # ---------------- C1
    P("C1. rebuild from p (univ.py:78-85 formula) and check the fit")
    R = realisations()
    for name, (Mu, Md) in R.items():
        du, dd, dV, J = check_fit(Mu, Md)
        P(f"  {name:28s} m_u,c,t rel.dev {np.abs(du).max():.1e}  m_d,s,b rel.dev {np.abs(dd).max():.1e}  max||V|-|V_PDG|| {dV:.1e}  J = {J:+.4e}")
    P("  (light-mass ratios were fitted to 1e-3 weights in OBS-3; dev quoted vs PDG inputs)")
    # ---------------- C2
    P("\nC2. controls: alignment (all carriers proportional to M) and single doublet")
    Mu, Md, _ = physical(*R['B-gen(as fitted)'])
    mb = mass_basis(Mu, Md)
    P(f"  rephasing residual |W_u^dag W_d - V_PDG| = {mb['rephase_res']:.1e}; diag check |Wu^dag Mu Xu - diag| = "
      f"{np.abs(hat(Mu, mb['Wu'], mb['Xu']) - np.diag(mb['mu'])).max():.1e} GeV")
    zeta = {'0': 0.5, 'x': 0.3, 'y': 0.6, 'z': 0.55}
    worst_fc = 0
    for K in CARRIERS:
        for M_, W, X in ((Mu, mb['Wu'], mb['Xu']), (Md, mb['Wd'], mb['Xd'])):
            Yh = hat(zeta[K] * M_ / VEV, W, X); off = Yh - np.diag(np.diag(Yh))
            worst_fc = max(worst_fc, np.abs(off).max() / np.abs(Yh).max())
    P(f"  aligned control: max |off-diagonal|/|max entry| over carriers and sectors = {worst_fc:.1e}")
    Yh = hat(Mu / VEV, mb['Wu'], mb['Xu']); P(f"  single-doublet control: {np.abs(Yh - np.diag(np.diag(Yh))).max():.1e}")
    Pu, Pd = carrier_hats(Mu, Md, mb)
    sumu = sum(Pu.values()); P(f"  completeness: |sum_K Phat_u^K - diag(m_u)| = {np.abs(sumu - np.diag(mb['mu'])).max():.1e} GeV")

    # ---------------- R1
    for name, (Mu0, Md0) in R.items():
        for conj_first in (False,):
            Mu, Md, cj = physical(Mu0, Md0)
            mb = mass_basis(Mu, Md); Pu, Pd = carrier_hats(Mu, Md, mb)
            P(f"\n=== {name}{' [complex-conjugated: J<0 as fitted]' if cj else ''}; rephase res {mb['rephase_res']:.1e}")
            P("  corner-basis |M_u| (GeV) =\n" + str(np.abs(Mu)) + "\n  corner-basis |M_d| (GeV) =\n" + str(np.abs(Md)))
            for K in CARRIERS:
                for sec, Ph in (('u', Pu), ('d', Pd)):
                    A = Ph[K]; off = A - np.diag(np.diag(A))
                    P(f"  carrier {K} sector {sec}: mass-basis image |Phat| (GeV) [diag = aligned part; off = flavour-changing]\n{np.abs(A)}"
                      f"\n     ||aligned|| = {np.linalg.norm(np.diag(A)):.3e}  ||flavour-changing|| = {np.linalg.norm(off):.3e}")
            for scale in (1.0, 0.5):
                for cls in ('D3', 'D6'):
                    t_eq = np.ones(4 if cls == 'D3' else 7)
                    m_eq, r_eq = worst(Pu, Pd, cls, t_eq, scale, Mu, Md, pen=False)
                    vu, vd = vev_dicts(cls, t_eq)
                    m_min, r_min, vu_m, vd_m, mc = minimise(Pu, Pd, cls, scale, Mu, Md)
                    P(f"  [{cls}, coupling scale x{scale}] equal vevs ({vu['0']:.1f} GeV each): M* = {m_eq:.3e} TeV; rows: " +
                      ", ".join(f"{k} {v:.2e}" for k, v in r_eq.items()) +
                      f"; max carrier Yukawa {max_coupling(Mu*scale, Md*scale, vu, vd):.2f}")
                    P(f"  [{cls}, coupling scale x{scale}] min over vevs: M* = {m_min:.3e} TeV; rows: " +
                      ", ".join(f"{k} {v:.2e}" for k, v in r_min.items()) +
                      f"; vevs up {[round(vu_m[k],1) for k in CARRIERS]} down {[round(vd_m[k],1) for k in CARRIERS]} GeV; max Yukawa {mc:.2f}")
                    # single-carrier contributions (equal vevs) to see which carriers drive each row
                    if cls == 'D3' and scale == 1.0:
                        for K in CARRIERS:
                            only = {k: (vu[k] if k == K else 0.0) for k in CARRIERS}
                            # restore the coupling normalisation of carrier K at the equal-vev point
                            r1 = mstar_rows(Pu, Pd, {k: (vu[k] if k == K else 0) for k in CARRIERS},
                                            {k: (vd[k] if k == K else 0) for k in CARRIERS})
                            P(f"      carrier {K} alone (equal-vev couplings): " + ", ".join(f"{k} {v:.2e}" for k, v in r1.items()))
