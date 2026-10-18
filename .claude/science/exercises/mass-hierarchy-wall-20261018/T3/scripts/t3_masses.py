"""Mass levels at the realised D2h vacua: M_f = a_f (1 + beta_f J + gamma_f diag(ehat(t*))), real, free per sector.
Score = R1/T (max over sectors of half-spread of log(m/obs), and |log|V|-log V_obs| for us, cb, ub). Control: 200 random spectra."""
import re, numpy as np
from t3_landau import ehat
ts = []
for f in ('../t3_AN.out', '../t3_AW.out'):
    for line in open(f):
        if 'D2h realised rho' in line:
            ts += [float(x) for x in re.search(r't\*=\[([^\]]*)\]', line).group(1).split(',')]
ts = np.radians(sorted(set(ts)))
print(f'realised D2h t* set (deg): {np.round(np.degrees(ts),1).tolist()}')
x = np.concatenate([-np.geomspace(1e-4, 1e3, 50)[::-1], [0.0], np.geomspace(1e-4, 1e3, 50)])
B, G = np.meshgrid(x, x, indexing='ij'); B = B.ravel(); G = G.ravel()
J = np.ones((3, 3)); I = np.eye(3)
def prep(t):
    e = ehat(t)
    M = I + B[:, None, None] * J + G[:, None, None] * np.diag(e)
    w, O = np.linalg.eigh(M)
    order = np.argsort(np.abs(w), -1)
    w = np.take_along_axis(np.abs(w), order, -1)
    O = np.take_along_axis(O, order[:, None, :], -1)
    good = w[:, 0] > 1e-30
    return np.log(np.where(good[:, None], w, 1e-300)), O, good
PRE = [prep(t) for t in ts]; PRE0 = prep(0.0)
DATA = {'MZ': ([1.27e-3, 0.619, 171.7], [2.90e-3, 0.055, 2.89], [0.48657e-3, 0.102718, 1.74624]),
        'GUT': ([0.48e-3, 0.235, 74.0], [1.14e-3, 0.022, 1.00], [0.469652e-3, 0.0991466, 1.68558]),
        'MIX': ([2.16e-3, 1.27, 172.69], [4.67e-3, 0.0934, 4.18], [0.511e-3, 0.1057, 1.777])}
CKM = np.log([0.225, 0.041, 0.0037])
def hs(d): return 0.5 * (d.max(-1) - d.min(-1))
def best(up, dn, le, ck, pre, K=300, detail=False):
    lw, O, good = pre
    su = np.where(good, hs(lw - np.log(up)), np.inf); sd = np.where(good, hs(lw - np.log(dn)), np.inf)
    sl = np.where(good, hs(lw - np.log(le)), np.inf).min()
    iu = np.argsort(su)[:K]; idn = np.argsort(sd)[:K]
    Ou = O[iu]; Od = O[idn]
    Vus = np.abs(np.einsum('ui,di->ud', Ou[:, :, 0], Od[:, :, 1]))
    Vcb = np.abs(np.einsum('ui,di->ud', Ou[:, :, 1], Od[:, :, 2]))
    Vub = np.abs(np.einsum('ui,di->ud', Ou[:, :, 0], Od[:, :, 2]))
    lv = np.log(np.maximum(np.stack([Vus, Vcb, Vub], -1), 1e-300))
    sc = np.abs(lv - ck).max(-1)
    tot = np.maximum(np.maximum(su[iu][:, None], sd[idn][None, :]), np.maximum(sc, sl))
    k = np.unravel_index(np.argmin(tot), tot.shape)
    if detail:
        return tot[k], dict(su=su[iu][k[0]], sd=sd[idn][k[1]], sl=sl, V=np.exp(lv[k]))
    return tot[k]
def search(up, dn, le, ck, pres):
    return min(best(up, dn, le, ck, p) for p in pres)
print('\n=== real data, D2h t* set (search over t* in the realised set) ===')
for tag, (up, dn, le) in DATA.items():
    vals = [best(up, dn, le, CKM, p, detail=True) for p in PRE]
    i = int(np.argmin([v[0] for v in vals])); v = vals[i]
    print(f'{tag}: best factor x{np.exp(v[0]):.2f} at t*={np.degrees(ts[i]):.1f} deg; per part up x{np.exp(v[1]["su"]):.2f} dn x{np.exp(v[1]["sd"]):.2f} '
          f'lep x{np.exp(v[1]["sl"]):.2f}  |Vus,Vcb,Vub| {np.round(v[1]["V"],4)}')
    v0 = best(up, dn, le, CKM, PRE0, detail=True)
    print(f'     tetragonal t*=0 (same search): best factor x{np.exp(v0[0]):.3g}; |Vus,Vcb,Vub| {np.round(v0[1]["V"],6)}')
# tetragonal: shared eigenvector check
lw, O, good = PRE0
anti = np.array([0, 1, -1]) / np.sqrt(2)
ov = np.abs(np.einsum('gij,i->gj', O, anti)).max(-1)
print(f'tetragonal t*=0: fraction of grid points where some eigenvector is exactly (0,1,-1)/sqrt2: {np.mean(ov > 1 - 1e-9):.4f}')
print('\n=== random control (200 spectra, R1 generator, seed 7), same search ===')
rng = np.random.default_rng(7); res = []
for c in range(200):
    sp = []
    for f in range(3):
        r21, r32 = 10 ** rng.uniform(-4, 0, 2); sp.append([r21 * r32, r32, 1.0])
    ck = np.log(10 ** rng.uniform(-3, np.log10(0.5), 3))
    res.append(search(*sp, ck, PRE))
res = np.exp(np.array(res))
print(f'control best factors: quantiles 10/50/90% = {np.round(np.quantile(res,[.1,.5,.9]),2)}; fraction within x3: {np.mean(res<=3):.3f}')
for tag, (up, dn, le) in DATA.items():
    r = np.exp(search(up, dn, le, CKM, PRE)); print(f'   {tag}: real x{r:.2f}; controls at least as good: {np.mean(res<=r):.3f}')
