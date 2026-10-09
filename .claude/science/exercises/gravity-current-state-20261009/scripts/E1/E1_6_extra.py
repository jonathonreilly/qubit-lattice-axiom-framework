"""E1 extra 4D runs.
 evo  : eps=0.2 diamond T=11: coarse (Gaussian lam=1) and element growth of closed-loop
        deviation vs tc -> exponential vs power law; renewal prediction
        gamma_rms = 0.5*sqrt(3.35*kappa*eps) with kappa = Var(b1)/(eps S) measured.
 irexp: stratified targets in tau_b bins to fit Var(b1) ~ tau^p (eps=0.1, T=16).
 strain: per-realization response of b1 to a constant TT spatial shear
        A_s = diag(1, e^s, e^-s, 1) of the metric (points fixed; order from A_s P);
        elements restricted to the g_s-diamond so the law is exactly s-independent.
 winL : Gaussian windows up to lam=2.2 at fixed centre (eps=0.2).
"""
import numpy as np, time, sys
from math import sqrt, pi, log
from bd_core import sprinkle4d, bd4d_weights, csr_apply, evolve, _shell4d
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 99)
which = sys.argv[1]


def taub(P): return np.sqrt(np.maximum(P[:, 0]**2 - (P[:, 1:]**2).sum(1), 0))


if which == "evo":
    eps, T, nreal, lam = 0.2, 11.0, 6, 1.0
    tcs = [4.5, 5.5, 6.5, 7.5, 8.5]
    rec = {tc: ([], [], [], []) for tc in tcs}
    t0 = time.time()
    for r in range(nreal):
        P = sprinkle4d(1/eps, T, rng); tb = taub(P)
        allx = np.arange(len(P))
        ip, ix, w = bd4d_weights(P, allx, eps)
        phi = evolve(ip, ix, w, allx, np.ones(len(P)), tb < 3.0)
        dO = csr_apply(ip, ix, w, np.ones(len(P))) - 1.0; dC = phi - 1.0
        rr = np.sqrt((P[:, 1:]**2).sum(1))
        for tc in tcs:
            dt = P[:, 0] - tc
            sel = (np.abs(dt) < 2.5*lam) & (rr < 2.5*lam) & (tb >= 3.0)
            wt = np.exp(-(dt[sel]**2 + rr[sel]**2)/(2*lam*lam))
            rec[tc][0].append((wt*dO[sel]).sum()/wt.sum()); rec[tc][1].append((wt*dC[sel]).sum()/wt.sum())
            rec[tc][2].append(sqrt((dO[sel]**2).mean())); rec[tc][3].append(sqrt((dC[sel]**2).mean()))
        print(f"  realization {r} N={len(P)} [{time.time()-t0:.0f}s]", flush=True)
    prev = None
    for tc in tcs:
        a = [np.array(x) for x in rec[tc]]
        # rms over realizations (mean zero) is a more stable estimator with few realizations
        cO = sqrt((a[0]**2).mean()); cC = sqrt((a[1]**2).mean())
        s = f"   tc={tc}: coarse rms open={cO:.4f} closed={cC:.4f} | element rms open={a[2].mean():.3f} closed={a[3].mean():.3f}"
        if prev is not None:
            s += f" | d ln(coarse closed)/dtc={log(cC/prev[0]):.3f} d ln/d ln tc={log(cC/prev[0])/log(tc/prev[1]):.2f}"
        prev = (cC, tc); print(s, flush=True)

elif which == "irexp":
    eps, T = 0.1, 16.0
    bins = [(3.0, 3.5), (4.5, 5.0), (6.5, 7.0), (9.0, 9.5), (12.0, 12.5), (14.5, 15.0)]
    vals = {b: [] for b in bins}
    t0 = time.time()
    for r in range(2):
        P = sprinkle4d(1/eps, T, rng); tb = taub(P)
        tg = []
        for b in bins:
            c = np.nonzero((tb >= b[0]) & (tb < b[1]))[0]
            tg += list(rng.choice(c, size=min(60, c.size), replace=False))
        tg = np.sort(np.array(tg))
        ip, ix, w = bd4d_weights(P, tg, eps)
        b1 = csr_apply(ip, ix, w, np.ones(len(P))) - 1.0
        for b in bins:
            m = (tb[tg] >= b[0]) & (tb[tg] < b[1]); vals[b] += list(b1[m])
        print(f"  realization {r} N={len(P)} [{time.time()-t0:.0f}s]", flush=True)
    xs, ys = [], []
    for b in bins:
        v = np.array(vals[b]); tm = 0.5*(b[0]+b[1])
        print(f"   tau~{tm:5.2f} n={v.size} Var b1={v.var():8.3f} (+-{v.var()*sqrt(2/v.size):.3f})  Var/tau^2={v.var()/tm**2:.4f}")
        xs.append(log(tm)); ys.append(log(v.var()))
    p = np.polyfit(xs[2:], ys[2:], 1)
    print(f"   fit Var b1 ~ tau^p over tau>=6.75: p = {p[0]:.2f}")

elif which == "strain":
    eps, T = 0.1, 8.0
    svals = [1e-4, 1e-3, 1e-2, 3e-2, 1e-1]
    Tbig = T*1.25
    acc = {s: [] for s in [0.0] + svals}
    t0 = time.time()
    for r in range(6):
        # sprinkle in a larger diamond; for each s keep points inside the g_s diamond I(0,(T,0))
        P0 = sprinkle4d(1/eps, Tbig, rng)
        P0[:, 0] -= (Tbig - T)/2  # centre: bottom at -(Tbig-T)/2
        # targets: fixed coordinate points near the axis at t in [6,7]
        for s in [0.0] + svals:
            A = np.array([1.0, np.exp(s), np.exp(-s), 1.0])
            Q = P0*A  # eta-picture coordinates A P
            r_ = np.sqrt((Q[:, 1:]**2).sum(1))
            inside = (r_ < Q[:, 0]) & (r_ < T - Q[:, 0])
            idx = np.nonzero(inside)[0]
            Qi = Q[idx]; order = np.argsort(Qi[:, 0]); Qi = Qi[order]; idx = idx[order]
            orig = P0[idx]
            sel = np.nonzero((orig[:, 0] > 5.8) & (orig[:, 0] < 6.6) &
                             (np.sqrt((orig[:, 1:]**2).sum(1)) < 0.6))[0]
            if s == 0.0:
                keyset = set(idx[sel])
            # use the same physical points as targets for all s
            tg = np.array(sorted([k for k in range(len(idx)) if idx[k] in keyset]))
            ip, ix, w = bd4d_weights(Qi, tg, eps)
            b1 = csr_apply(ip, ix, w, np.ones(len(Qi))) - 1.0
            lab = idx[tg]
            acc[s].append(dict(zip(lab, b1)))
        print(f"  realization {r}  [{time.time()-t0:.0f}s]", flush=True)
    base = acc[0.0]
    for s in svals:
        d = []; m0 = []; ms = []
        for r in range(len(base)):
            for k, v in base[r].items():
                if k in acc[s][r]:
                    d.append(acc[s][r][k] - v); m0.append(v); ms.append(acc[s][r][k])
        d = np.array(d)
        print(f"   s={s:7.0e}: n={d.size} <b1(s)>={np.mean(ms):+.3f} <b1(0)>={np.mean(m0):+.3f}"
              f"  <Delta>={d.mean():+.4f}+-{d.std()/sqrt(d.size):.4f}  sd(Delta)={d.std():.4f}"
              f"  sd/sqrt(s)={d.std()/sqrt(s):.3f}  sd/s={d.std()/s:.2f}  frac(Delta=0)={np.mean(np.abs(d)<1e-12):.2f}", flush=True)

elif which == "winL":
    eps, tc = 0.2, 6.5
    for lam, nreal in [(1.0, 24), (1.4, 16), (1.8, 10), (2.2, 8)]:
        T = tc + 2.5*lam + 0.3
        means = []; whites = []; t0 = time.time()
        for r in range(nreal):
            P = sprinkle4d(1/eps, T, rng)
            dt = P[:, 0] - tc; rr = np.sqrt((P[:, 1:]**2).sum(1))
            sel = np.nonzero((np.abs(dt) < 2.5*lam) & (rr < 2.5*lam))[0]
            ip, ix, w = bd4d_weights(P, sel, eps)
            b1 = csr_apply(ip, ix, w, np.ones(len(P))) - 1.0
            wt = np.exp(-(dt[sel]**2 + rr[sel]**2)/(2*lam*lam))
            means.append((wt*b1).sum()/wt.sum()); whites.append((wt**2*b1**2).sum()/wt.sum()**2)
        means = np.array(means); sd = sqrt((means**2).mean()); sdw = sqrt(np.mean(whites))
        print(f"   lam={lam:4.2f} targets~{len(sel)} rms b_lam={sd:.4f} (+-{sd/sqrt(2*nreal):.4f}) indep-pred={sdw:.4f}"
              f" ratio={sd/sdw:.2f} rms*lam^2={sd*lam*lam:.4f} [{time.time()-t0:.0f}s]", flush=True)
