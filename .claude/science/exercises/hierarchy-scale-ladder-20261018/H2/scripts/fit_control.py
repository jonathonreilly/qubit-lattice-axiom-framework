#!/usr/bin/env python3
"""HIER-2 A1/A2: free-integer FN fit control and the sector-blind bound.

m_i = Lam * eps^{n_i}, integers n_i >= 0. Two continuous parameters (Lam, eps).
Comparator masses recalled (see PREREG.md); no fetch.
"""
import numpy as np

SETS = {
    'MZ':  dict(u=1.27e-3, c=0.619, t=171.7, d=2.90e-3, s=0.055, b=2.89,
                e=0.48657e-3, mu=0.102718, tau=1.74624),
    'GUT': dict(u=0.48e-3, c=0.235, t=74.0, d=1.14e-3, s=0.022, b=1.00,
                e=0.469652e-3, mu=0.0991466, tau=1.68558),
    'MIX': dict(u=2.16e-3, c=1.27, t=172.69, d=4.67e-3, s=0.0934, b=4.18,
                e=0.511e-3, mu=0.1057, tau=1.777),
}
SECT = {'up': ['u', 'c', 't'], 'down': ['d', 's', 'b'], 'lep': ['e', 'mu', 'tau']}
ORDER = ['u', 'c', 't', 'd', 's', 'b', 'e', 'mu', 'tau']
EPS = np.exp(np.linspace(np.log(1e-3), np.log(0.9), 1500))


def best_fit(x, s, nlam=4000):
    """x: log masses; s = -ln eps > 0. Returns (min over Lam of max |dev|, n vector, maxn).
    Lam' scanned over one period above x.max() (so the heaviest has n in {0,1})."""
    lam = x.max() + np.linspace(-s, s, nlam)
    r = (lam[:, None] - x[None, :]) / s
    n = np.clip(np.rint(r), 0, None)
    dev = np.abs(lam[:, None] - x[None, :] - n * s)
    mx = dev.max(axis=1)
    k = int(np.argmin(mx))
    return mx[k], n[k].astype(int), lam[k]


def scan(x, F):
    lf = np.log(F)
    ok = []
    for e in EPS:
        s = -np.log(e)
        d, n, lam = best_fit(x, s)
        if d <= lf + 1e-12:
            n = n - n.min()  # shift so the lightest exponent offset is minimal (Lam absorbs it)
            ok.append((e, int(n.max()), n, d))
    return ok


def report_free(name, m):
    print(f"\n=== set {name}: free integers, all 9 masses")
    x = np.log(np.array([m[k] for k in ORDER]))
    for F in (3, 10):
        ok = scan(x, F)
        if not ok:
            print(f"  x{F}: no fit for eps in [1e-3, 0.9]")
            continue
        es = np.array([o[0] for o in ok])
        Nstar = min(o[1] for o in ok)
        best = min(ok, key=lambda o: (o[1], o[3]))
        print(f"  x{F}: fits exist for {len(ok)}/{len(EPS)} eps grid points; eps range [{es.min():.4f}, {es.max():.4f}]"
              f"; fraction of eps in [1/9, 0.9] that fit: {np.mean([o[0] >= 1/9 for o in ok]) if ok else 0:.3f} of fits")
        print(f"     smallest max exponent N* = {Nstar}; example eps={best[0]:.4f}, n(u,c,t,d,s,b,e,mu,tau)={best[2].tolist()}, max dev factor {np.exp(best[3]):.2f}")
        # check: every eps >= 1/F^2 fits (step <= 2 ln F)
        thr = 1 / F**2
        grid_hi = EPS[EPS >= thr]
        nfit_hi = sum(1 for o in ok if o[0] >= thr)
        print(f"     eps >= 1/F^2 = {thr:.4f}: {nfit_hi}/{len(grid_hi)} grid points fit (expected all: step <= 2 ln F)")
    for sec, ks in SECT.items():
        xs = np.log(np.array([m[k] for k in ks]))
        ok = scan(xs, 3)
        if ok:
            Ns = min(o[1] for o in ok)
            b = min(ok, key=lambda o: (o[1], o[3]))
            print(f"  sector {sec} alone x3: N*={Ns}, example eps={b[0]:.4f} n={b[2].tolist()} dev x{np.exp(b[3]):.2f}")


def report_blind(name, m):
    print(f"\n=== set {name}: sector-blind (n_g and Lam common to up, down, lepton)")
    for g, trip in enumerate([('u', 'd', 'e'), ('c', 's', 'mu'), ('t', 'b', 'tau')]):
        v = [m[k] for k in trip]
        print(f"  generation {g+1} {trip}: spread max/min = {max(v)/min(v):.1f}  (x3 needs <= 9; x10 needs <= 100)")
    # best achievable common fit: each generation predicted at Lam eps^{n_g}; deviation over all 9
    x = np.log(np.array([[m['u'], m['d'], m['e']], [m['c'], m['s'], m['mu']], [m['t'], m['b'], m['tau']]]))
    best = (np.inf, None)
    for e in EPS:
        s = -np.log(e)
        lam = x.max() + np.linspace(-s, s, 3000)
        # for each generation choose the integer n_g minimising its worst deviation
        worst = np.zeros_like(lam)
        ns = []
        for g in range(3):
            r = (lam[:, None] - x[g][None, :]) / s
            cand = np.stack([np.floor(r.mean(axis=1)) + j for j in (-1, 0, 1, 2)], axis=1)
            cand = np.clip(cand, 0, None)
            dev = np.abs(lam[:, None, None] - x[g][None, None, :] - cand[:, :, None] * s).max(axis=2)
            jbest = dev.argmin(axis=1)
            worst = np.maximum(worst, dev[np.arange(len(lam)), jbest])
            ns.append(cand[np.arange(len(lam)), jbest])
        k = int(np.argmin(worst))
        if worst[k] < best[0]:
            best = (worst[k], (e, [int(n[k]) for n in ns]))
    print(f"  best sector-blind fit: max deviation factor x{np.exp(best[0]):.1f} at eps={best[1][0]:.4f}, n(gen1,gen2,gen3)={best[1][1]}")
    print("  CKM: sector-common coefficients give M_u = c M_d, so U_u = U_d and V_CKM = 1 (no mixing) -- see check below")


def ckm_blind_check():
    rng = np.random.default_rng(1)
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Mu, Md = 2.7 * A, 0.4 * A
    Uu = np.linalg.svd(Mu)[0]; Ud = np.linalg.svd(Md)[0]
    V = Uu.conj().T @ Ud
    off = np.abs(V - np.diag(np.diag(V))).max()
    print(f"\n=== CKM with sector-common texture (M_u = 2.7 A, M_d = 0.4 A, random A): max |offdiag V| = {off:.2e}")


def random_control(F=3, nsamp=400, seed=7):
    rng = np.random.default_rng(seed)
    m = SETS['MZ']
    lo, hi = np.log(min(m.values())), np.log(max(m.values()))
    sub = EPS[(EPS >= 0.02) & (EPS <= 0.6)][::5]
    hits = 0; hits_hi = 0
    for _ in range(nsamp):
        x = rng.uniform(lo, hi, 9)
        anyfit = False; fit_hi = False
        for e in sub:
            d, n, lam = best_fit(x, -np.log(e), nlam=800)
            if d <= np.log(F) + 1e-12:
                anyfit = True
                if e >= 1/9:
                    fit_hi = True
        hits += anyfit; hits_hi += fit_hi
    print(f"\n=== random-spectrum control (9 log-uniform masses over the observed range, {nsamp} draws):")
    print(f"  fraction with a free-integer x{F} fit for some eps in [0.02, 0.6]: {hits/nsamp:.3f}; with eps >= 1/9: {hits_hi/nsamp:.3f}")


if __name__ == '__main__':
    for nm, m in SETS.items():
        report_free(nm, m)
    for nm, m in SETS.items():
        report_blind(nm, m)
    ckm_blind_check()
    random_control()
