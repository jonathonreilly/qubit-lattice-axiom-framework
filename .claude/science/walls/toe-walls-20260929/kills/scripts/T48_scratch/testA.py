import numpy as np, sys, json, time
from scipy.optimize import least_squares
from common import *

def observables(R, tu, td):
    Uu, du, ru = dressed_U(R, tu)
    if ru > 1e-8: return None
    Ud, dd, rd = dressed_U(R, td)
    if rd > 1e-8: return None
    a, J = ckm_from(Uu, Ud)
    return dict(Vus=a[0,1], Vcb=a[1,2], Vub=a[0,2], J=J)

def loss_vec(o):
    return np.array([np.log(o["Vus"]/OBS["Vus"]), np.log(o["Vcb"]/OBS["Vcb"]), np.log(o["Vub"]/OBS["Vub"]), np.log(max(o["J"],1e-30)/OBS["J"])])

def fit_unconstrained(tu, td, nsamp=5000, npolish=12, seed_=0):
    rng = np.random.default_rng(seed_)
    def f(x):
        R = seed(*x)
        o = observables(R, tu, td)
        if o is None: return np.ones(4)*8
        return np.clip(loss_vec(o), -8, 8)
    cands = []
    for k in range(nsamp):
        x = [rng.uniform(0.02,1.2), rng.uniform(0.02,1.2), rng.uniform(0.0,1.2), rng.uniform(0,2*np.pi)]
        r = f(x); cands.append((np.max(np.abs(r)), x))
    cands.sort(key=lambda c: c[0])
    best = None
    for c0, x0 in cands[:npolish]:
        sol = least_squares(f, x0, bounds=([0,0,0,-2*np.pi],[1.6,1.6,1.6,4*np.pi]), xtol=1e-12, ftol=1e-12, max_nfev=150)
        c = np.max(np.abs(sol.fun))
        if best is None or c < best[0]: best = (c, sol.x, sol.fun)
    return best

def circ_score(o):
    l = loss_vec(o)
    return max(np.max(np.abs(np.exp(l[:3])-1)), np.abs(l[3])/np.log(2)*0.25)

def scan_circulant(tu, td, nrho=60, nphi=61):
    best = None; nfeas = 0; ntot = 0
    for rho in np.linspace(0.02, 1.3, nrho):
        for phi in np.linspace(0, np.pi, nphi):
            ntot += 1
            o = observables(circ_seed(rho, phi), tu, td)
            if o is None: continue
            nfeas += 1
            sc = circ_score(o)
            if best is None or sc < best[0]: best = (sc, rho, phi, o)
    # polish
    def f(x):
        o = observables(circ_seed(*x), tu, td)
        if o is None: return np.ones(4)*8
        l = np.clip(loss_vec(o), -8, 8); return l
    sol = least_squares(f, [best[1], best[2]], bounds=([0.01,-np.pi],[1.6,2*np.pi]), xtol=1e-12, ftol=1e-12, max_nfev=200)
    o2 = observables(circ_seed(*sol.x), tu, td)
    if o2 is not None and circ_score(o2) < best[0]:
        best = (circ_score(o2), sol.x[0], sol.x[1], o2)
    return best, nfeas, ntot

def theta_e12(R, te):
    Ue, de, re_ = dressed_U(R, te)
    if re_ > 1e-8: return None, None
    a = np.abs(Ue)
    return float(np.degrees(np.arcsin(min(1.0, a[0,1]/np.sqrt(a[0,0]**2+a[0,1]**2))))), a[0]

results = {}
t00 = time.time()
for sname in ("MZ", "LOW"):
    for p in (1.0, 0.5):
        tu = np.array(MASSES[sname]["u"])**p; td = np.array(MASSES[sname]["d"])**p; te = np.array(MASSES[sname]["e"])**p
        key = f"{sname}_p{p}"
        c, x, res = fit_unconstrained(tu, td)
        R = seed(*x); o = observables(R, tu, td)
        th12, row = theta_e12(R, te)
        r12, r23, r13, th = x
        rec = dict(unconstrained=dict(max_abs_log_err=float(c), r12=float(r12), r23=float(r23), r13=float(r13), theta=float(th),
                                      r23_over_r12=float(r23/r12), r13_over_r12=float(r13/r12), obs=o, lepton_theta_e12_deg=th12))
        print(f"[{time.time()-t00:.0f}s] {key} UNCONSTRAINED: max|log err|={c:.3g}  r12,r23,r13,theta={np.round(x,3)}  r23/r12={r23/r12:.3f} r13/r12={r13/r12:.3f}"
              f"  obs={ {k: float(f'{v:.3g}') for k,v in o.items()} }  lepton theta_e12={th12}", flush=True)
        (sc, rho, phi, oc), nfeas, ntot = scan_circulant(tu, td)
        th12c, _ = theta_e12(circ_seed(rho, phi), te)
        rec["circulant"] = dict(score=float(sc), rho=float(rho), phi_deg=float(np.degrees(phi)), obs=oc, lepton_theta_e12_deg=th12c, feasible_frac=nfeas/ntot)
        print(f"    CIRCULANT best worst-rel-err={sc:.3f} (feasible {nfeas}/{ntot}) rho={rho:.3f} phi={np.degrees(phi):.1f}deg  obs={ {k: float(f'{v:.3g}') for k,v in oc.items()} }  lepton theta_e12={th12c}", flush=True)
        results[key] = rec
json.dump(results, open("testA_results.json","w"), indent=1, default=float)
