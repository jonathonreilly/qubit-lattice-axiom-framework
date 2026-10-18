"""OBS-3 R1: flat-light-column realisations (PREREG S5). W_u e1 = f1 and W_u V e1 = f2, both flat (|.|^2 = 1/3).
Checks the FIXED rows over the full bracket x placements x splits x carriers, then side rows."""
import numpy as np, itertools, sys
from obs3_core import *
np.set_printoptions(precision=3, linewidth=160)
P = print
V = INPUTS['pdg24']['V']
f1 = np.ones(3) / np.sqrt(3)

def flat_partner(t, sgn):
    z = 3 * V[0, 0] - np.exp(1j * t)
    if abs(z) > 2: return None
    a0 = np.angle(z); da = np.arccos(abs(z) / 2)
    return np.array([np.exp(1j * t), np.exp(1j * (a0 + sgn * da)), np.exp(1j * (a0 - sgn * da))]) / np.sqrt(3)

def cperp(a, b):
    n = np.conj(np.cross(a, b)); return n / np.linalg.norm(n)

def build_Wu(t, sgn, phi):
    f2 = flat_partner(t, sgn)
    if f2 is None: return None
    v1 = V[:, 0]; e1 = np.array([1, 0, 0], complex)
    w = v1 - V[0, 0] * e1; g = f2 - V[0, 0] * f1
    wh = w / np.linalg.norm(w); gh = g / np.linalg.norm(g)
    n = cperp(e1, wh); h = cperp(f1, gh)
    A = np.column_stack([e1, wh, n]); B = np.column_stack([f1, gh, h * np.exp(1j * phi)])
    return B @ A.conj().T

def checks(Wu):
    Wd = Wu @ V
    return dict(unit=np.abs(Wu @ Wu.conj().T - np.eye(3)).max(), ckm=np.abs(Wu.conj().T @ Wd - V).max(),
                u1=np.abs(np.abs(Wu[:, 0])**2 - 1 / 3).max(), d1=np.abs(np.abs(Wd[:, 0])**2 - 1 / 3).max(),
                eps_t=np.abs(np.abs(Wu[:, 2])**2 - 1 / 3).max(), eps_c=np.abs(np.abs(Wu[:, 1])**2 - 1 / 3).max(),
                eps_b=np.abs(np.abs(Wd[:, 2])**2 - 1 / 3).max(), eps_s=np.abs(np.abs(Wd[:, 1])**2 - 1 / 3).max())

if __name__ == '__main__':
    # 1. scan the construction family (t, sign, phi) for the top-column non-flatness
    best = None
    for sgn in (+1, -1):
        for t in np.linspace(-np.pi, np.pi, 181):
            for phi in np.linspace(0, 2 * np.pi, 73)[:-1]:
                Wu = build_Wu(t, sgn, phi)
                if Wu is None: continue
                c = checks(Wu)
                if best is None or c['eps_t'] < best[0]:
                    best = (c['eps_t'], t, sgn, phi)
    P(f"construction family: min over (t, sign, phi) of top-column non-flatness max_c ||W_u,ct|^2 - 1/3| = {best[0]:.4f} at t={best[1]:.3f} sign={best[2]} phi={best[3]:.3f}")
    from scipy.optimize import minimize
    res = minimize(lambda x: checks(build_Wu(x[0], best[2], x[1]))['eps_t'] if build_Wu(x[0], best[2], x[1]) is not None else 9,
                   [best[1], best[3]], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-12, maxiter=4000))
    tE, phiE, sgnE = res.x[0], res.x[1], best[2]
    WuE = build_Wu(tE, sgnE, phiE); cE = checks(WuE)
    P(f"refined: eps_t = {cE['eps_t']:.5f}; checks: unitarity {cE['unit']:.1e}, W_u^dag W_d - V {cE['ckm']:.1e}, |W_u1|^2 flat to {cE['u1']:.1e}, |W_d1|^2 flat to {cE['d1']:.1e}; eps_c {cE['eps_c']:.4f} eps_s {cE['eps_s']:.4f} eps_b {cE['eps_b']:.4f}")
    P("W_u (E1) =\n", WuE, "\n|W_u|^2 =\n", np.abs(WuE)**2, "\n|W_d|^2 =\n", np.abs(WuE @ V)**2)
    np.save('escape_E1_Wu.npy', WuE)
    # 2. FIXED rows for E1 with Hermitian textures (X = W) and with X = F, over everything
    reals = {'E1-herm': dict(Wu=WuE, Xu=WuE, Xd=WuE @ V), 'E1-XF': dict(Wu=WuE, Xu=F, Xd=F)}
    for prefix, Ns in (('yuk_kin', (48, 96)),):
        for N in Ns:
            worst = {k: 0.0 for k in reals}; side_worst = {k: {} for k in reals}; side_best = {k: {} for k in reals}
            for (m, D) in BRACKET:
                tabs = get_tabs(N, m, D)
                for name, base in reals.items():
                    for car in ('M1', 'M2'):
                        for var in ('sym', 'int', 'ext'):
                            for y0mode in ('trace', 'selective'):
                                for sq in (1.0, 0.45):
                                    o = evaluate(dict(base, carrier=car, var=var, y0mode=y0mode), tabs, scale_q=sq)
                                    fr, rr = fixed_ratio(o)
                                    worst[name] = max(worst[name], fr)
                                    for k, v in side_ratio(o).items():
                                        side_worst[name][k] = max(side_worst[name].get(k, 0), v)
                                        side_best[name][k] = min(side_best[name].get(k, 1e99), v)
            for name in reals:
                P(f"N={N} {name}: max FIXED-row ratio over bracket x placements x splits x carriers x coupling scale = {worst[name]:.2e}")
                P("    side rows ratio [min, max]: " + "  ".join(f"{k} [{side_best[name][k]:.1e},{side_worst[name][k]:.1e}]" for k in side_worst[name]))
    # 3. primary-point detail for E1-herm, M2 and M1
    tabs = get_tabs(96, '0.025', '0.5')
    for car in ('M1', 'M2'):
        o = evaluate(dict(reals['E1-herm'], carrier=car, var='sym', y0mode='trace'), tabs)
        P(f"E1-herm {car} primary (N=96 m0=0.025 D=0.5 sym trace low-scale):")
        for nm in ('u', 'c', 't', 'd', 's', 'b', 'e'):
            x = o[nm]
            P(f"   {nm:2s} c-ring {x['cring']:+.2e} d-ring {x['dring']:+.2e} | traceless c_jj {x['can']} d_jj {x['dan']}")
        for f, (iso, tet, r) in o['fields'].items():
            P(f"   field {f:2s} universal iso {iso:+.3e} tet {tet:+.3e} |residual|max {np.abs(r).max():.2e}")
