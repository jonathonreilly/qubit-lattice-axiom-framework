"""OBS-3: re-check the escape realisations with range-2 corner symbols (g_c^2), theta in {0.5, 1}, N = 48 and 96."""
import numpy as np
from obs3_core import *
P = print
V = INPUTS['pdg24']['V']
WuE = np.load('escape_E1_Wu.npy')
zg = np.load('univ_B_gen.npz')
zA = np.load('univ_A_M1.npz')
reals = {'E1 flat-light (Hermitian textures)': dict(Wu=WuE, Xu=WuE, Xd=WuE @ V),
         'B-gen equal-modulus': dict(Yu=zg['Yu'], Yd=zg['Yd'], Wu=zg['Wu'], Xu=zg['Xu'], Wd=zg['Wd'], Xd=zg['Xd']),
         'A M1 diag-constant (W_u = F)': dict(Wu=zA['Wu_0'], Xu=zA['Xu_0'], Xd=zA['Xd_0'], only='M1'),
         'OBS-2 branch B (control)': dict(Wu=F, Xu=F, Xd=F @ V)}
for name, base in reals.items():
    worst_f, worst_rel, dmin, dmax = 0, 0, 1e99, 0
    for N in (48, 96):
        for (m, D) in BRACKET:
            tabs = {}
            I = {}
            for var in ('sym', 'int', 'ext'):
                I[var], syms = load_kin(N, m, D, var, prefix='yuk3_kin')
            opt, cov = load_flav(N, m, D)
            tabs = dict(I=I, syms=syms, opt=opt)
            for car in ('M1', 'M2'):
                if base.get('only') and car != base['only']: continue
                for var in ('sym', 'int', 'ext'):
                    for y0mode in ('trace', 'selective'):
                        for th in (0.5, 1.0):
                            o = evaluate(dict(base, carrier=car, var=var, y0mode=y0mode, theta=th), tabs)
                            fr = fixed_ratio(o)[0]; worst_f = max(worst_f, fr)
                            dmin = min(dmin, abs(o['d']['cTT'])); dmax = max(dmax, abs(o['d']['cTT']))
                            for f in ('Q', 'uc', 'dc'):
                                iso, tet, r = o['fields'][f]; worst_rel = max(worst_rel, np.abs(r).max() / abs(iso))
    P(f"{name:38s}: range-2 symbols: max FIXED ratio {worst_f:.2e}; |c_TT^d| in [{dmin:.1e}, {dmax:.1e}]; max |residual|/|universal| (Q,uc,dc) {worst_rel:.1e}")
