"""OBS-4 R2: further exact B-gen / B-gen120 realisations.
 A  plain refits (OBS-3's residual, univ.py:89-99, copied; new seeds) -> B-gen#k
 B  FCNC-seeking refits: same residual plus a soft term pulling the equal-vev D3 M* down; each candidate is then
    re-polished with the pure fit residual (restoring exactness) before evaluation.
Every accepted realisation: all mass-ratio and |V_ij| pulls <= 1e-6, ||J|-J_PDG| <= 1e-3 sigma (PREREG rule 1)."""
import numpy as np, sys, time
from scipy.optimize import least_squares
from obs4_core import *
from obs4_r1 import physical, vev_dicts, minimise, worst
P = lambda *a: print(*a, flush=True)
sig = dict(ud=0.00016, us=0.00068, ub=0.000090, cd=0.00068, cs=0.00016, cb=0.00079, td=0.00019, ts=0.00077, tb=0.000034)
SIG = np.array([[sig['ud'], sig['us'], sig['ub']], [sig['cd'], sig['cs'], sig['cb']], [sig['td'], sig['ts'], sig['tb']]])
AV = np.abs(VPDG); J0, sJ = Jarl(VPDG), 0.13e-5

def fit_res(p, d120):           # univ.py:89-99 (copied), with |J|
    Zu, Zd = texture(p[:7], False, d120), texture(p[7:], False, d120)
    Wu, su, _ = svd_sorted(Zu); Wd, sd, _ = svd_sorted(Zd)
    Vp = Wu.conj().T @ Wd
    out = [np.log(su[0] / su[2]) - np.log(yu[0] / yu[2]), np.log(su[1] / su[2]) - np.log(yu[1] / yu[2]),
           np.log(sd[0] / sd[2]) - np.log(yd[0] / yd[2]), np.log(sd[1] / sd[2]) - np.log(yd[1] / yd[2])]
    out = [x / 1e-3 for x in out]
    out += list(((np.abs(Vp) - AV) / SIG).ravel())
    out.append(abs(Jarl(Vp)) / sJ - J0 / sJ)
    return np.array(out)

def mstar_eq(p, d120, scale=1.0):
    Mu, Md = masses_from_p(p, d120); Mu, Md, _ = physical(Mu, Md)
    mb = mass_basis(Mu, Md); Pu, Pd = carrier_hats(Mu, Md, mb)
    return worst(Pu, Pd, 'D3', np.ones(4), scale, Mu, Md, pen=False)[0], (Mu, Md, Pu, Pd)

def exact(p, d120):
    r = fit_res(p, d120)
    return np.abs(r[:13]).max() <= 1e-6 * max(1, 1) and abs(r[13]) <= 1e-3, np.abs(r).max()

def polish(p, d120):
    r = least_squares(fit_res, p, args=(d120,), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
    return r.x

if __name__ == '__main__':
    t0 = time.time(); rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 2024)
    nA = int(sys.argv[2]) if len(sys.argv) > 2 else 60; nB = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    found = []
    for d120 in (False, True):
        tag = 'B-gen120' if d120 else 'B-gen'
        P(f"\n=== {tag}: A plain refits ({nA} starts)")
        sols = []
        for s in range(nA):
            p0 = np.concatenate([[rng.normal(0, 0.5)], rng.normal(0, 0.3 if s % 2 else 2.0, 6),
                                 [rng.normal(0, 0.5)], rng.normal(0, 0.3 if s % 2 else 2.0, 6)])
            try:
                r = least_squares(fit_res, p0, args=(d120,), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=3000)
            except Exception:
                continue
            ok, mx = exact(r.x, d120)
            if not ok:
                continue
            m, _ = mstar_eq(r.x, d120)
            # de-duplicate by M* and |diag/off| ratio
            if any(abs(np.log(m / q[1])) < 1e-6 for q in sols):
                continue
            sols.append((r.x, m)); P(f"  #{len(sols)}: max pull {mx:.1e}, M*_eq(D3) = {m:.3e} TeV, exp(r_u) {np.exp(r.x[0]):.4f} exp(r_d) {np.exp(r.x[7]):.4f}  ({time.time()-t0:.0f}s)")
        P(f"  {len(sols)} distinct exact solutions; M*_eq range {min(q[1] for q in sols):.2e} - {max(q[1] for q in sols):.2e} TeV" if sols else "  none")
        found += [(tag, 'A', q[0], q[1]) for q in sols]
        P(f"=== {tag}: B FCNC-seeking refits ({nB} starts)")
        best = []
        for s in range(nB):
            p0 = sols[s % len(sols)][0] + rng.normal(0, 0.3, 14) if sols else rng.normal(0, 1, 14)
            def res(p):
                m, _ = mstar_eq(p, d120)
                return np.concatenate([fit_res(p, d120), [0.3 * np.log(m)]])
            try:
                r = least_squares(res, p0, xtol=1e-12, ftol=1e-12, max_nfev=1500)
                x = polish(r.x, d120)
            except Exception:
                continue
            ok, mx = exact(x, d120)
            if not ok:
                continue
            m, _ = mstar_eq(x, d120); best.append((x, m))
        best.sort(key=lambda q: q[1])
        for x, m in best[:5]:
            P(f"  candidate: M*_eq(D3) = {m:.3e} TeV (exact, max pull {exact(x, d120)[1]:.1e})")
        P(f"  {len(best)} exact FCNC-seeking solutions; lowest M*_eq {best[0][1]:.3e} TeV" if best else "  none exact")
        found += [(tag, 'B', q[0], q[1]) for q in best[:5]]
    # vev-optimised minimum (tuned) for the lowest natural realisation of each tag
    for tag in ('B-gen', 'B-gen120'):
        cand = [q for q in found if q[0] == tag]
        if not cand: continue
        x = min(cand, key=lambda q: q[3])[2]; d120 = tag == 'B-gen120'
        m, (Mu, Md, Pu, Pd) = mstar_eq(x, d120)
        for scale in (1.0, 0.5):
            mm = minimise(Pu, Pd, 'D3', scale, Mu, Md, nstart=20)
            P(f"  {tag} lowest-natural realisation, scale x{scale}: M*_eq = {m*scale:.3e} TeV; vev-optimised (tuned) M* = {mm[0]:.3e} TeV")
    np.savez('refit_solutions.npz', tags=np.array([q[0] + q[1] for q in found]), p=np.array([q[2] for q in found]),
             mstar_eq=np.array([q[3] for q in found]))
    P(f"done {time.time()-t0:.0f}s")
