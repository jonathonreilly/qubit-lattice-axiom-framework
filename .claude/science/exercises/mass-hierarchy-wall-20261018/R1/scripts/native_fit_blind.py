"""R1 Test B2: sector-blind placements (the generation label is shared by all
components of a generation, as for a lattice-native label).
 blind   : Q = u^c = d^c = L = e^c = V
 chiralL : Q = L = V, u^c = d^c = e^c = internal (triv3)
Same Yukawa construction, data and control as native_fit.py.
"""
import sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import native_fit as nf
import native_menu as nm

def score(logs, logV, reps, obs, mode):
    lu, ld, le, lc = (np.log(obs[k]) for k in ['up', 'dn', 'le', 'ckm'])
    it = reps.index('triv3')
    best = (1e9, None)
    per_t = []
    for t, (su, sd, se) in enumerate(nf.TRIPLES):
        bt = 1e9
        for a, V in enumerate(reps):
            if mode == 'blind':
                q, u, d, l, e = a, a, a, a, a
            else:
                if V == 'triv3': continue
                q, u, d, l, e = a, it, it, a, it
            up = nf.halfspread(logs[q, u, su] - lu)
            dn = nf.halfspread(logs[q, d, sd] - ld)
            lep = nf.halfspread(logs[l, e, se] - le)
            ck = np.abs(logV[q, u, d, t] - lc).max(-1)
            tot = np.maximum(np.maximum(up, dn), np.maximum(lep, ck))
            f = float(np.exp(tot.min()))
            bt = min(bt, f)
            if f < best[0]: best = (f, (V, t, nf.EPS[int(np.argmin(tot))]))
        per_t.append(bt)
    return best, per_t

if __name__ == '__main__':
    pre = []
    for sig, dname, n, reps in nf.classes():
        logs, Us = nf.precompute(sig, n, reps)
        logV = nf.ckm_logs(Us, len(reps))
        pre.append((sig, dname, reps, logs, logV, nm.lv_order(sig, n, nm.group_for([sig]))))
    rng = np.random.default_rng(11)
    ctrl = []
    for i in range(300):
        obs = {}
        for sec in ['up', 'dn', 'le']:
            r21 = 10 ** rng.uniform(-4, 0); r32 = 10 ** rng.uniform(-4, 0)
            obs[sec] = [r21 * r32, r32, 1.0]
        obs['ckm'] = list(10 ** rng.uniform(-3, -0.3, size=3))
        ctrl.append(obs)
    for mode in ['blind', 'chiralL']:
        print(f'\n##### mode {mode}')
        for tag, obs in nf.DATA.items():
            allbest = (1e9, None)
            for sig, dname, reps, logs, logV, lv in pre:
                b, pt = score(logs, logV, reps, obs, mode)
                if b[0] < allbest[0]: allbest = (b[0], (sig, dname, lv) + b[1])
            print(f'{tag}: best x{allbest[0]:.2f} at {allbest[1]}')
        cb = []
        for obs in ctrl:
            cb.append(min(score(logs, logV, reps, obs, mode)[0][0] for sig, dname, reps, logs, logV, lv in pre))
        cb = np.array(cb)
        print(f'control (300): fit within x3 {np.mean(cb <= 3):.3f}, x5 {np.mean(cb <= 5):.3f}, x10 {np.mean(cb <= 10):.3f};'
              f' quantiles 10/50/90 {np.round(np.quantile(cb, [0.1, 0.5, 0.9]), 1)}')
        sys.stdout.flush()
