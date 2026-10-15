"""OBS-4 R1d (added after PREREG, see PREREG_FOLLOWUP): how low can M* go in the doublet class (D3) if BOTH the exact
B-gen realisation (6-ish free directions of the exact family) AND the four vevs are tuned together for cancellation?
Joint least-squares: OBS-3 fit residual + soft log-sum-exp of the INP rows; then exact polish of p, then vev re-optimisation.
Reports the lowest M*, the cancellation |sum|/sum|terms| per meson, and the 1% vev-jitter median (tuning sensitivity)."""
import numpy as np, sys, time
from scipy.optimize import least_squares
from obs4_core import *
from obs4_r1 import physical, vev_dicts, minimise, worst
from obs4_refit import fit_res, exact, polish
P = lambda *a: print(*a, flush=True)

def rows_of(p, d120, t):
    Mu, Md = masses_from_p(p, d120); Mu, Md, _ = physical(Mu, Md)
    mb = mass_basis(Mu, Md); Pu, Pd = carrier_hats(Mu, Md, mb)
    vu, vd = vev_dicts('D3', t)
    return mstar_rows(Pu, Pd, vu, vd), (Mu, Md, Pu, Pd)

if __name__ == '__main__':
    t0 = time.time(); rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
    nst = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    rs = np.load('refit_solutions.npz'); tags = [str(t) for t in rs['tags']]
    results = []
    for s in range(nst):
        k = s % len(tags); d120 = 'gen120' in tags[k]
        x0 = np.concatenate([rs['p'][k] + rng.normal(0, 0.05, 14), rng.uniform(-0.5, 0.5, 4)])
        def res(x):
            r, _ = rows_of(x[:14], d120, np.exp(x[14:]))
            v = np.array(list(r.values())) + 1e-30
            soft = np.log(np.sum(v**8)) / 8                       # smooth max of log M*
            return np.concatenate([fit_res(x[:14], d120), [0.2 * soft]])
        try:
            sol = least_squares(res, x0, xtol=1e-12, ftol=1e-12, max_nfev=2500)
            p = polish(sol.x[:14], d120)
        except Exception as e:
            P(f"  start {s}: failed {e}"); continue
        ok, mx = exact(p, d120)
        if not ok:
            P(f"  start {s}: not exact after polish (max pull {mx:.1e})"); continue
        r, (Mu, Md, Pu, Pd) = rows_of(p, d120, np.exp(sol.x[14:]))
        mm = minimise(Pu, Pd, 'D3', 1.0, Mu, Md, nstart=12, seed=s)
        results.append((mm[0], s, tags[k], p, mm))
        P(f"  start {s} ({tags[k]}): exact (pull {mx:.1e}); M* at joint optimum {max(r.values()):.3e} TeV; after vev re-opt {mm[0]:.3e} TeV  ({time.time()-t0:.0f}s)")
    results.sort(key=lambda q: q[0])
    for m, s, tag, p, mm in results[:3]:
        _, r, vu, vd, mc = mm; d120 = 'gen120' in tag
        _, (Mu, Md, Pu, Pd) = rows_of(p, d120, np.ones(4))
        P(f"\n best start {s} ({tag}): M* = {m:.3e} TeV, rows " + ", ".join(f"{a} {b:.2e}" for a, b in r.items()) +
          f"; vevs {[round(vu[K], 1) for K in CARRIERS]} GeV; max Yukawa {mc:.2f}")
        for nm, (Ph, i, j) in (('K', (Pd, 1, 0)), ('D', (Pu, 1, 0)), ('Bd', (Pd, 2, 0)), ('Bs', (Pd, 2, 1))):
            terms = np.array([Ph[K][i, j] * np.conj(Ph[K][j, i]) / vu[K]**2 for K in CARRIERS])
            P(f"   {nm}: cancellation |sum|/sum|terms| = {abs(terms.sum())/np.abs(terms).sum():.2e}")
        base = np.array([vu[K] for K in CARRIERS]); jr = np.random.default_rng(1)
        ms = [worst(Pu, Pd, 'D3', base * (1 + 0.01 * jr.standard_normal(4)), 1.0, Mu, Md, pen=False)[0] for _ in range(200)]
        P(f"   1% vev jitter: median M* {np.median(ms):.2e} TeV; natural (equal-vev) M* {worst(Pu, Pd, 'D3', np.ones(4), 1.0, Mu, Md, pen=False)[0]:.2e} TeV")
    np.savez('tuned_solutions.npz', mstar=np.array([q[0] for q in results]), p=np.array([q[3] for q in results]),
             tags=np.array([q[2] for q in results]))
    P(f"done {time.time()-t0:.0f}s")
