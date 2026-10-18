"""R1 Test B3: detail of the best chiral-blind fit (Q=L=T2, R internal, T2 spurion generic) and control percentile."""
import sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import native_fit as nf, native_menu as nm, native_fit_blind as nb

pre = []
for sig, dname, n, reps in nf.classes():
    logs, Us = nf.precompute(sig, n, reps)
    logV = nf.ckm_logs(Us, len(reps))
    pre.append((sig, dname, reps, logs, logV))
# per-draw bests for real data
for tag, obs in nf.DATA.items():
    pts = np.full(3, 1e9)
    for sig, dname, reps, logs, logV in pre:
        b, pt = nb.score(logs, logV, reps, obs, 'chiralL')
        pts = np.minimum(pts, pt)
    print(tag, 'chiralL best per coefficient draw:', np.round(pts, 2))
# detail of T2 gen, V=T2
for sig, dname, reps, logs, logV in pre:
    if sig == 'T2' and dname == 'gen':
        a = reps.index('T2'); it = reps.index('triv3')
        obs = nf.DATA['MZ']
        for t, (su, sd, se) in enumerate(nf.TRIPLES):
            lu, ld, le, lc = (np.log(obs[k]) for k in ['up', 'dn', 'le', 'ckm'])
            up = logs[a, it, su] - lu; dn = logs[a, it, sd] - ld; lep = logs[a, it, se] - le
            ck = logV[a, it, it, t] - lc
            tot = np.maximum(np.maximum(nf.halfspread(up), nf.halfspread(dn)), np.maximum(nf.halfspread(lep), np.abs(ck).max(-1)))
            e = int(np.argmin(tot))
            def rel(d): return np.round(np.exp(d - 0.5 * (d.max() + d.min())), 2)
            print(f' draw {t}: eps={nf.EPS[e]:.4f} factor x{np.exp(tot[e]):.2f}; model/obs (after sector scale) '
                  f'up {rel(up[e])} down {rel(dn[e])} lep {rel(lep[e])} ckm(us,cb,ub) {np.round(np.exp(ck[e]), 2)}')
            print('    model mass ratios m1/m3,m2/m3: up', np.round(np.exp(logs[a, it, su, e] - logs[a, it, su, e, 2]), 6),
                  'down', np.round(np.exp(logs[a, it, sd, e] - logs[a, it, sd, e, 2]), 6))
rng = np.random.default_rng(11)
cb = []
for i in range(300):
    obs = {}
    for sec in ['up', 'dn', 'le']:
        r21 = 10 ** rng.uniform(-4, 0); r32 = 10 ** rng.uniform(-4, 0)
        obs[sec] = [r21 * r32, r32, 1.0]
    obs['ckm'] = list(10 ** rng.uniform(-3, -0.3, size=3))
    cb.append(min(nb.score(logs, logV, reps, obs, 'chiralL')[0][0] for sig, dname, reps, logs, logV in pre))
cb = np.array(cb)
for thr in [3.68, 3.85]:
    print(f'control: fraction of random spectra fit within x{thr}: {np.mean(cb <= thr):.3f}')
