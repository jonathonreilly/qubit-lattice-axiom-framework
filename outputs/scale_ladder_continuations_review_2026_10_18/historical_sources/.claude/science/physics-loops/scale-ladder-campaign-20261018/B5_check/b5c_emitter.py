"""B5 independent check: single emitter (onsite d) coupled by a positive block of
weight gam to the end of a 1D receiver chain (hopping g, M sites), one-excitation
sector.  Positive-block implementation: every edge e contributes w_e(I - hop_e),
so H_P(w) = C(w) I - sum w_e hop_e, C(w)=sum_e w_e (global scalar).
Error classes (each alone):
  SB : source bond gam -> gam(1+eps)
  SO : emitter onsite 0 -> d (absolute)
  RB : all receiver bonds g -> g(1+eps) (common relative)
Metrics on the COMPLETE single-excitation vector at sup over t in {T,1.5T,2T}:
  act : || e^{-itH_P(w)}psi0 - e^{-itC(w)} T0(t) ||   (repo: actual scalar)
  nom : || e^{-itH_P(w)}psi0 - e^{-itC(w0)} T0(t) ||  (nominal clock)
  pop : || |psi_act| - |T0| ||                       (phase-blind)
T0(t)=e^{-it(H_P(w0)-C(w0))}psi0 nominal centered evolution.
Tolerance = error parameter at which the metric reaches budget E (bisection in log).
Independent code path: scipy expm_multiply, own Hamiltonian, own bisection.
"""
import numpy as np, scipy.sparse as sp, sys, json
from scipy.sparse.linalg import expm_multiply
E = 1e-2

def ham(gam, g, M, d=0.0, rb=1.0):
    n = M + 1
    off = np.r_[gam, np.full(M - 1, g * rb)]
    diag = np.zeros(n); diag[0] = d
    H = sp.diags([diag, -off, -off], [0, 1, -1], format='csr')  # centered (no C)
    C = off.sum()
    return H, C

def evolve(H, psi0, ts):
    return [expm_multiply(-1j * H * t, psi0) for t in ts]

def errs(gam, g, M, T, kind, x, cache):
    ts = [T, 1.5 * T, 2 * T]
    key = (gam, g, M, T)
    H0, C0 = ham(gam, g, M)
    psi0 = np.zeros(M + 1, complex); psi0[0] = 1
    if key not in cache:
        cache[key] = evolve(H0, psi0, ts)
    nom = cache[key]
    if kind == 'SB': H1, C1 = ham(gam * (1 + x), g, M)
    elif kind == 'SO': H1, C1 = ham(gam, g, M, d=x)
    elif kind == 'RB': H1, C1 = ham(gam, g, M, rb=1 + x)
    act = evolve(H1, psi0, ts)  # centered actual; true state = e^{-itC1} * act
    out = {'act': 0, 'nom': 0, 'pop': 0}
    for t, a, b in zip(ts, act, nom):
        out['act'] = max(out['act'], np.linalg.norm(a - b))             # e^{-itC1} common
        out['nom'] = max(out['nom'], np.linalg.norm(np.exp(-1j*t*(C1-C0)) * a - b))
        out['pop'] = max(out['pop'], np.linalg.norm(np.abs(a) - np.abs(b)))
    return out

def tol(gam, g, M, T, kind, metric, cache):
    lo, hi = 1e-12, 1.0
    if errs(gam, g, M, T, kind, hi, cache)[metric] < E: return float('inf')
    for _ in range(40):
        mid = np.sqrt(lo * hi)
        if errs(gam, g, M, T, kind, mid, cache)[metric] < E: lo = mid
        else: hi = mid
        if hi / lo < 1.02: break
    return np.sqrt(lo * hi)

if __name__ == '__main__':
    g = 1.0
    res = []
    # (a) fixed lam, vary T;  (b) fixed lam*T, vary lam
    plan = [('fixT', 0.2, Tl) for Tl in (12.5, 25, 50, 100)] + [('fixLT', gm, 25) for gm in (0.4, 0.2, 0.1)]
    for tag, gam, Tl in plan:
        lam = gam**2 / g          # amplitude decay rate at band centre
        T = Tl / lam
        M = int(1.15 * 2 * g * 2 * T) + 60
        cache = {}
        row = dict(tag=tag, gam=gam, lam=lam, T=T, M=M)
        for kind in ('SB', 'SO', 'RB'):
            for metric in ('act', 'nom', 'pop'):
                row[f'{kind}_{metric}'] = tol(gam, g, M, T, kind, metric, cache)
        res.append(row)
        print(json.dumps({k: (f'{v:.3e}' if isinstance(v, float) else v) for k, v in row.items()}), flush=True)
    json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else 'b5c_emitter.json', 'w'), indent=1)
