"""bridge_fit.py -- the two-parameter background-subtracted fit
      dW/ds_e - dW_flat/ds_e  =  A (dVol/ds_e - dVol_flat/ds_e) + B dS_Regge/ds_e
with  A_pred = -E_3(m^2 tau0)/(32 pi^2 tau0^2),  B_pred = -E_2(m^2 tau0)/(96 pi^2 tau0)
(from W = -(1/2) int_tau0^inf (dtau/tau) e^{-tau m^2}(4 pi tau)^-2 int sqrt(g)(1 + tau R/6),
 and int sqrt(g) R = 2 S_Regge).  Massless limit: A_pred = -1/(64 pi^2 tau0^2),
 B_pred = -1/(96 pi^2 tau0)  <=>  G_ind = 12 pi tau0 per real scalar."""
import numpy as np, scipy.special as sp
from bridge_geom import *
from bridge_spec import dW_multi

def preds(tau0, m2):
    E3 = sp.expn(3, m2*tau0) if m2 > 0 else 0.5
    E2 = sp.expn(2, m2*tau0) if m2 > 0 else 1.0
    return -E3/(32*np.pi**2*tau0**2), -E2/(96*np.pi**2*tau0)

def fit2(y, x1, x2):
    X = np.stack([x1, x2], 1)
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    r1 = y - x1*(y@x1)/(x1@x1); r2 = x2 - x1*(x2@x1)/(x1@x1)
    pr = float(r1@r2/np.sqrt((r1@r1)*(r2@r2)))
    res = y - X@coef
    return float(coef[0]), float(coef[1]), pr, 1-res@res/(y@y)

def channels(L, amp, nk, alphas, settings, verbose=False):
    """One flat Bloch pass + one per polarisation; returns per-polarisation
    (y, x1, x2) arrays for every setting."""
    S0 = edge_s(L, 0.0, nk, alphas[0]); g0 = geometry(S0, L)
    dW0 = dW_multi(S0, L, settings, geom=g0, verbose=verbose)
    ch = []
    for al in alphas:
        S = edge_s(L, amp, nk, al); g = geometry(S, L)
        dW = dW_multi(S, L, settings, geom=g, verbose=verbose)
        ch.append(dict(al=al, x1=(g['dVol']-g0['dVol']).ravel(),
                       x2=(g['dReg']-g0['dReg']).ravel(),
                       y=[(dW[t]-dW0[t]).ravel() for t in range(len(settings))]))
    return ch

def summarise(L, nk, settings, ch, tag=''):
    """Per-polarisation and JOINT (stacked, each channel scaled to unit |x1|) fits."""
    out = []
    for t, (tau0, m2, imp) in enumerate(settings):
        Ap, Bp = preds(tau0, m2)
        rows = []
        for c in ch:
            n = np.linalg.norm(c['x1'])
            rows.append((c['y'][t]/n, c['x1']/n, c['x2']/n))
        for nm, (y, x1, x2) in list(zip([str(c['al']) for c in ch], rows)) + \
                               [('JOINT', tuple(np.concatenate([r[i] for r in rows]) for i in range(3)))]:
            A, B, pr, R2 = fit2(y, x1, x2)
            out.append(dict(L=L, nk=nk, tau0=tau0, m2=m2, improved=imp, pol=nm,
                            A=A, B=B, Ar=A/Ap, Br=B/Bp, pr=pr, R2=R2,
                            ry1=float(y@x1/np.sqrt((y@y)*(x1@x1))),
                            ry2=float(y@x2/np.sqrt((y@y)*(x2@x2))),
                            tk2=tau0*(2*np.pi*nk/L)**2, tag=tag))
    return out

def run(L, amp, nk, alpha, settings, verbose=False):
    ch = channels(L, amp, nk, [alpha], settings, verbose=verbose)
    return [r for r in summarise(L, nk, settings, ch) if r['pol'] == 'JOINT']

HDR = (f"{'L':>4} {'nk':>3} {'tau0':>6} {'imp':>4} {'tau0k2':>7} {'pol':>14} "
       f"{'A/Apred':>9} {'B/Bpred':>9} {'part r':>8}")
def line(d):
    return (f"{d['L']:>4} {d['nk']:>3} {d['tau0']:>6.2f} {str(d['improved'])[0]:>4} "
            f"{d['tk2']:>7.3f} {str(d.get('pol','')):>14} {d['Ar']:>9.4f} {d['Br']:>9.4f} "
            f"{d['pr']:>8.4f}")
