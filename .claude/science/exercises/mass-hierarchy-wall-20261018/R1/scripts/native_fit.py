"""R1 Test B: does any native single-spurion model fit 9 masses + 3 CKM within x3?

Models: one spurion class (sigma, direction) from native_menu.SPURIONS; each of
Q, u^c, d^c, L, e^c placed in a native generation rep (triv3 = internal label,
P, P2, T1, T2, and for translation-charged spurions also S, S2).  Yukawa
Y_f(eps) = sum_k eps^k sum_j c_kj B_kj with B_kj an orthonormal basis of the
degree-k equivariant structures at the vev, c_kj complex normal (generic O(1)).
Free: eps (grid) and one overall scale per sector (generous).  CKM has no free
scale.  Score = max over the 12 observables of |log(model/obs)| after the
sector scales; pass if score <= log 3.  Three independent coefficient draws.
Control: the same menu against random spectra.
"""
import sys, itertools
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import native_menu as nm

K = 8
EPS = np.logspace(-3, np.log10(0.6), 48)
TRIPLES = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]

# data (GeV), Xing-Zhang-Zhou style running masses, recalled (not fetched)
DATA = {
  'MZ':  dict(up=[1.38e-3, 0.638, 172.1], dn=[2.82e-3, 0.057, 2.86],
              le=[0.48657e-3, 0.10272, 1.7462], ckm=[0.2250, 0.0410, 0.00382]),
  'GUT': dict(up=[0.48e-3, 0.235, 74.0], dn=[1.14e-3, 0.022, 1.00],
              le=[0.4696e-3, 0.09914, 1.685], ckm=[0.2243, 0.0480, 0.0042]),
}

def classes():
    out = []
    for sig, dirs in nm.SPURIONS.items():
        reps = (nm.GENREPS_G2 if sig in nm.TRANSLATION_CHARGED else nm.GENREPS_O) + ['triv3']
        for dname, n in dirs:
            out.append((sig, dname, n, reps))
    return out

def precompute(sig, n, reps):
    """logs[VL,VR,seed,eps,3] ascending singular values; U[VL,VR,seed,eps,3,3] left vectors (cols ascending)."""
    R = len(reps)
    logs = np.full((R, R, 9, len(EPS), 3), -80.0)
    Us = np.zeros((R, R, 9, len(EPS), 3, 3), complex)
    for a, VL in enumerate(reps):
        for b, VR in enumerate(reps):
            G = nm.group_for([sig, VL, VR])
            bases = []
            for k in range(K + 1):
                B = nm.equivariant_images(sig, VL, VR, n, k, G)
                for row in B: bases.append((k, row.reshape(3, 3)))
            if not bases: continue
            for seed in range(9):
                rng = np.random.default_rng(1000 + seed)
                coef = rng.normal(size=len(bases)) + 1j * rng.normal(size=len(bases))
                Y = np.zeros((len(EPS), 3, 3), complex)
                for c, (k, X) in zip(coef, bases):
                    Y += (EPS ** k)[:, None, None] * c * X[None]
                u, s, vh = np.linalg.svd(Y)
                s = s[:, ::-1]; u = u[:, :, ::-1]
                logs[a, b, seed] = np.log(np.maximum(s, 1e-35))
                Us[a, b, seed] = u
    return logs, Us

def ckm_logs(Us, R):
    """logV[VQ,Vu,Vd,triple,eps,3] for (us, cb, ub)."""
    out = np.zeros((R, R, R, len(TRIPLES), len(EPS), 3))
    for t, (su, sd, se) in enumerate(TRIPLES):
        Uu = Us[:, :, su]            # [VQ,Vu,eps,3,3]
        Ud = Us[:, :, sd]            # [VQ,Vd,eps,3,3]
        V = np.einsum('queji,qdejk->qudeik', Uu.conj(), Ud)   # U_u^dagger U_d
        A = np.abs(V)
        out[:, :, :, t, :, 0] = np.log(np.maximum(A[..., 0, 1], 1e-35))
        out[:, :, :, t, :, 1] = np.log(np.maximum(A[..., 1, 2], 1e-35))
        out[:, :, :, t, :, 2] = np.log(np.maximum(A[..., 0, 2], 1e-35))
    return out

def halfspread(d):
    return 0.5 * (d.max(-1) - d.min(-1))

def score_class(logs, logV, R, obs):
    """best score over placements and eps, per triple; also quark-only and lepton-only bests."""
    lu = np.log(obs['up']); ld = np.log(obs['dn']); le = np.log(obs['le']); lc = np.log(obs['ckm'])
    res = []
    for t, (su, sd, se) in enumerate(TRIPLES):
        up = halfspread(logs[:, :, su] - lu)          # [VQ,Vu,eps]
        dn = halfspread(logs[:, :, sd] - ld)          # [VQ,Vd,eps]
        lep = halfspread(logs[:, :, se] - le)         # [VL,Ve,eps]
        ck = np.abs(logV[:, :, :, t] - lc).max(-1)    # [VQ,Vu,Vd,eps]
        q = np.maximum(np.maximum(up[:, :, None, :], dn[:, None, :, :]), ck)
        qmin = q.reshape(-1, len(EPS)).min(0)
        lmin = lep.reshape(-1, len(EPS)).min(0)
        tot = np.maximum(qmin, lmin)
        e = int(np.argmin(tot))
        qi = np.unravel_index(int(np.argmin(q[..., e])), q.shape[:3])
        li = np.unravel_index(int(np.argmin(lep[..., e])), lep.shape[:2])
        res.append(dict(total=tot.min(), quark=qmin.min(), lepton=lmin.min(), eps=EPS[e], qplace=qi, lplace=li))
    return res

if __name__ == '__main__':
    pre = []
    for sig, dname, n, reps in classes():
        logs, Us = precompute(sig, n, reps)
        R = len(reps)
        logV = ckm_logs(Us, R)
        lv = nm.lv_order(sig, n, nm.group_for([sig]))
        pre.append((sig, dname, reps, logs, logV, lv))
        print(f'precomputed {sig} {dname} (LV order {lv})'); sys.stdout.flush()

    REAL = {}
    for tag, obs in DATA.items():
        print(f'\n=== real data at {tag}: best x-factor (exp score); pass iff <= 3 ===')
        best = (1e9, None)
        for sig, dname, reps, logs, logV, lv in pre:
            res = score_class(logs, logV, len(reps), obs)
            for t, r in enumerate(res):
                f = np.exp(r['total'])
                if f < best[0]: best = (f, (sig, dname, t, r))
            fs = [np.exp(r['total']) for r in res]
            fq = [np.exp(r['quark']) for r in res]
            fl = [np.exp(r['lepton']) for r in res]
            r0 = res[int(np.argmin(fs))]
            q = tuple(reps[i] for i in r0['qplace']); l = tuple(reps[i] for i in r0['lplace'])
            print(f'{sig:7s} {dname:10s} LV={str(lv):4s} total x{min(fs):8.2f} (triples {["%.1f" % x for x in fs]}) '
                  f'quark x{min(fq):7.2f} lepton x{min(fl):6.2f} eps={r0["eps"]:.3g} Q,u,d={q} L,e={l}')
        pt = np.full(len(TRIPLES), 1e9)
        for sig, dname, reps, logs, logV, lv in pre:
            for t, r in enumerate(score_class(logs, logV, len(reps), obs)):
                pt[t] = min(pt[t], np.exp(r['total']))
        REAL[tag] = (pt.min(), np.median(pt))
        lvsafe = min(np.exp(r['total']) for sig, dname, reps, logs, logV, lv in pre if lv is None
                     for r in score_class(logs, logV, len(reps), obs))
        print('LV-safe classes best:', f'x{lvsafe:.2f}', '| best per draw:', np.round(pt, 2))
        print('BEST', tag, f'x{best[0]:.2f}', best[1][0], best[1][1], 'triple', best[1][2])
        sys.stdout.flush()

    # control: random spectra through the same menu
    rng = np.random.default_rng(7)
    NCTRL = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    bests = []; meds = []
    for i in range(NCTRL):
        obs = {}
        for sec in ['up', 'dn', 'le']:
            r21 = 10 ** rng.uniform(-4, 0); r32 = 10 ** rng.uniform(-4, 0)
            obs[sec] = [r21 * r32, r32, 1.0]
        obs['ckm'] = list(10 ** rng.uniform(-3, -0.3, size=3))
        per_triple = np.full(len(TRIPLES), 1e9)
        for sig, dname, reps, logs, logV, lv in pre:
            for t, r in enumerate(score_class(logs, logV, len(reps), obs)):
                per_triple[t] = min(per_triple[t], np.exp(r['total']))
        bests.append(per_triple.min()); meds.append(np.median(per_triple))
    bests = np.array(bests); meds = np.array(meds)
    print(f'\n=== control: {NCTRL} random spectra (sector ratios log-uniform 1e-4..1, |V| log-uniform 1e-3..0.5) ===')
    for thr in [3, 5, 10, 20]:
        print(f'  fraction fit within x{thr}: {np.mean(bests <= thr):.3f}')
    print('  quantiles of best factor (10,50,90%):', np.round(np.quantile(bests, [0.1, 0.5, 0.9]), 2))
    for tag in DATA:
        b, m = REAL[tag]
        print(f'  {tag}: real best x{b:.2f} -> fraction of random spectra fit at least as well: {np.mean(bests <= b):.3f};'
              f' real median-over-draws x{m:.2f} -> random fraction {np.mean(meds <= m):.3f}')
