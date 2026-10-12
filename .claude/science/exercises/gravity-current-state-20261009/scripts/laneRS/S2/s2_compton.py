"""Compton (fermion + photon -> fermion + photon) at O(e^2): s- and u-channel with the FULL one-body resolvent
(hole-theory Z-graphs included) + seagull.  (a) generic invertibility of T_C on (+band x transverse pol);
(b) trace reduction => scalar f(k)+g(p) invariant; odd null spaces: Compton alone, and Compton + Moller jointly.
Fermion basis sin(2n.k) (|n|<=Rf), photon basis sin(n.p) (|n|<=Rp).  usage: python s2_compton.py d m Rf Rp ns"""
import sys, time, numpy as np
from s2_core import *
d = int(sys.argv[1]); m = float(sys.argv[2]); Rf = int(sys.argv[3]); Rp = int(sys.argv[4]); ns = int(sys.argv[5])
rng = np.random.default_rng(23 + d); S = Stag(d, m); t0 = time.time()
def compton_T(k, p, kq, pq):
    U, Uq = S.Uplus(k), S.Uplus(kq); E = eps(k, m)
    Ep, Eq = transverse(p, d), transverse(pq, d)
    ks, ku = wrapr(k + p), wrapr(k - pq)
    Rs = np.linalg.inv((E + omega(p))*np.eye(S.nn) - S.h(ks))
    Ru = np.linalg.inv((E - omega(pq))*np.eye(S.nn) - S.h(ku))
    npl = U.shape[1]; npol = Ep.shape[1]
    T = np.zeros((npl*npol, npl*npol), complex)
    for l in range(npol):
        Va_s = sum(Ep[i, l]*S.vert(k, p, ks, i) for i in range(d)); Va_u = sum(Ep[i, l]*S.vert(ku, p, kq, i) for i in range(d))
        for lq in range(npol):
            Ve_s = sum(Eq[j, lq]*S.vert(ks, -pq, kq, j) for j in range(d)); Ve_u = sum(Eq[j, lq]*S.vert(k, -pq, ku, j) for j in range(d))
            SG = -sum(Ep[i, l]*Eq[i, lq]*S.seag(k, p - pq, kq, i) for i in range(d))
            M = Uq.conj().T @ (Ve_s @ Rs @ Va_s + Va_u @ Ru @ Ve_u + SG) @ U
            for a in range(npl):
                for c in range(npl):
                    T[a*npol + lq, c*npol + l] = M[a, c]
    return T/np.sqrt(4*omega(p)*omega(pq))
def sample_compton(nsamp, mode):
    out = []; g = np.linspace(-np.pi, np.pi, 1601); tries = 0
    while len(out) < nsamp and tries < nsamp*300:
        tries += 1
        if mode == 'low':
            k = wrapr(rng.normal(0, 0.4, d)); p = wrapf(rng.normal(0, 0.6, d)); p0 = wrapf(rng.normal(0, 0.6, d))
        else:
            k = rng.uniform(-np.pi/2, np.pi/2, d); p = rng.uniform(-np.pi, np.pi, d); p0 = rng.uniform(-np.pi, np.pi, d)
        if omega(p) < 0.05: continue
        Etot = eps(k, m) + omega(p); ax = rng.integers(d)
        P = np.tile(p0, (len(g), 1)); P[:, ax] = g
        fv = eps(wrapr(k + p - P), m) + omega(P) - Etot
        idx = np.nonzero(np.sign(fv[:-1])*np.sign(fv[1:]) < 0)[0]
        for ii in idx:
            a, b = g[ii], g[ii+1]
            def F(t):
                x = p0.copy(); x[ax] = t; return eps(wrapr(k + p - x), m) + omega(x) - Etot
            fa = F(a)
            for _ in range(70):
                c = 0.5*(a+b); fc = F(c)
                if np.sign(fa)*np.sign(fc) <= 0: b = c
                else: a, fa = c, fc
            pq = p0.copy(); pq[ax] = 0.5*(a+b); pq = wrapf(pq)
            if np.max(np.abs(wrapf(pq - p))) < 1e-3 or omega(pq) < 0.05: continue
            kq = wrapr(k + p - pq)
            out.append((k, p, kq, pq))
            if len(out) >= nsamp: break
    return out
samp = sample_compton(ns//2, 'generic') + sample_compton(ns//2, 'low')
print(f"d={d} m={m}: {len(samp)} Compton shells ({time.time()-t0:.1f}s)", flush=True)
Bf = odd_basis(d, Rf); Bp = odd_basis(d, Rp)
rat = []; rows = []; mags = []
for (k, p, kq, pq) in samp:
    T = compton_T(k, p, kq, pq); sv = np.linalg.svd(T, compute_uv=False); rat.append(sv[-1]/sv[0]); mags.append(sv[0])
    assert abs(eps(k, m) + omega(p) - eps(kq, m) - omega(pq)) < 1e-12
    rows.append(np.concatenate([np.sin(2*Bf@k) - np.sin(2*Bf@kq), np.sin(Bp@p) - np.sin(Bp@pq)]))
rat = np.array(rat)
print(f"T_C is {T.shape[0]}x{T.shape[1]}: max-sv median {np.median(mags):.3e} min {np.min(mags):.3e}; min-sv/max-sv min {rat.min():.2e}, 1st pct {np.percentile(rat,1):.2e}, median {np.median(rat):.2e}", flush=True)
A = np.array(rows)/np.sqrt(len(rows)); nf = len(Bf)
def report(name, A, ncol):
    sv = np.linalg.svd(A, compute_uv=False)
    print(f"  {name}: cols {ncol}, rows {A.shape[0]}, null dim {nullity(sv, ncol)}; sv min {sv[-1]:.3e} max {sv[0]:.3e} ratio {sv[-1]/sv[0]:.3e}", flush=True)
    return sv
report("Compton alone, odd (f, g)", A, A.shape[1])
# Compton + Moller jointly
mol = sample_moller(S, ns, rng, mode='generic') + sample_moller(S, ns//2, rng, mode='lowE')
Am = np.array([np.concatenate([np.sin(2*Bf@k1) + np.sin(2*Bf@k2) - np.sin(2*Bf@k3) - np.sin(2*Bf@k4), np.zeros(len(Bp))]) for (k1, k2, k3, k4) in mol])/np.sqrt(len(mol))
report("Compton + Moller, odd (f, g)", np.vstack([A, Am]), A.shape[1])
# photon-only part after Moller fixes f's odd part = 0: g alone on Compton shells
report("Compton with f odd = 0, odd g alone", A[:, nf:], len(Bp))
# continuum-like control: replace lattice dispersions? -> analytic note only.  e=0 control: no rows -> everything passes (trivial).
print(f"time {time.time()-t0:.1f}s")
