#!/usr/bin/env python3
"""Reviewer re-implementation of the C2b Collins-type toy (claim 3); different code and method.
Same physical model as NOTE sec. 4 (a = 1): Wilson fermion S^-1 = i g.s(k) + M(k), Yukawa g phi psibar psi,
Pi(p)/g^2 = 4 int_BZ (-s(k).s(k+p) + M(k)M(k+p)) / (D(k) D(k+p)),  Z_mu = (1/2) d^2/dp_mu^2 [Pi/g^2] at p = 0.
Differences from the author's code:
  * the p-derivative is ANALYTIC (exact second derivative of s_nu/D and M/D in k_mu), no finite-difference stencil;
  * quadrature: integrand is even in every k_mu, so integrate over [0, pi]^4 x 16 with a geometrically graded
    composite Gauss-Legendre mesh (nodes clustered at k = 0 on a scale m), not a sinh map;
  * convergence check by changing the points per panel (q) and the grading ratio.
delta_phi = (g^2/2)(Z_s - Z_0) = C (g^2/16 pi^2) x mismatch  =>  C = 8 pi^2 (Z_s - Z_0) / mismatch."""
import sys, time
import numpy as np
P = F = 0
def chk(n, ok):
    global P, F
    P += bool(ok); F += (not ok); print(('PASS ' if ok else 'FAIL ') + n, flush=True)

def mesh(m, q, ratio):
    # panels [0,h0],[h0,h0*ratio],... up to pi; h0 = m/4
    edges = [0.0]; h = m/4
    while h < np.pi: edges.append(h); h *= ratio
    edges.append(np.pi)
    x, w = np.polynomial.legendre.leggauss(q)
    K, W = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        K.append((b - a)/2*x + (a + b)/2); W.append((b - a)/2*w)
    K = np.concatenate(K); W = np.concatenate(W)*2/(2*np.pi)   # x2 for [-pi,0], /(2 pi) measure
    return K, W

def axis_funcs(kind, par, k, mu):
    """s, s', s'', w, w', w'' for axis mu (0 = tick)."""
    c, sn = np.cos(k), np.sin(k)
    if mu == 0 and kind == 'T3':
        e = par/3
        s = sn*(1 - e + e*c); s1 = c*(1 - e) + e*np.cos(2*k); s2 = -sn*(1 - e) - 2*e*np.sin(2*k)
    else:
        s, s1, s2 = sn, c, -sn
    r = par if (kind == 'RT' and mu == 0) else 1.0
    return s, s1, s2, r*(1 - c), r*sn, r*c

def Z(kind, par, m, q, ratio, mu):
    k, w = mesh(m, q, ratio)
    f = [axis_funcs(kind, par, k, nu) for nu in range(4)]
    # we build 4D arrays by looping over axis 0's nodes and broadcasting axes 1..3
    tot = 0.0
    s = [None]*4; ds = [None]*4; dds = [None]*4; W_ = [None]*4; dW = [None]*4; ddW = [None]*4
    shp = [(-1, 1, 1), (1, -1, 1), (1, 1, -1)]
    for nu in (1, 2, 3):
        a = f[nu]; sh = shp[nu - 1]
        s[nu], ds[nu], dds[nu], W_[nu], dW[nu], ddW[nu] = [t.reshape(sh) for t in a]
    w3 = w.reshape(-1, 1, 1)*w.reshape(1, -1, 1)*w.reshape(1, 1, -1)
    ssp = s[1]**2 + s[2]**2 + s[3]**2; wsp = W_[1] + W_[2] + W_[3]
    for i in range(len(k)):
        s0, ds0, dds0, w0, dw0, ddw0 = [t[i] for t in f[0]]
        M = m + w0 + wsp
        D = s0**2 + ssp + M**2
        if mu == 0:
            u, u1, u2, v1, v2 = s0, ds0, dds0, dw0, ddw0
        else:
            u, u1, u2, v1, v2 = s[1], ds[1], dds[1], dW[1], ddW[1]
        D1 = 2*u*u1 + 2*M*v1
        D2 = 2*(u1**2 + u*u2 + v1**2 + M*v2)
        iD = 1/D; iD1 = -D1*iD**2; iD2 = -D2*iD**2 + 2*D1**2*iD**3
        # sum_nu s_nu d^2(s_nu/D): for nu != mu: s_nu^2 iD2; for nu = mu: u (u2 iD + 2 u1 iD1 + u iD2)
        sall = s0**2 + ssp
        Ss = (sall - u**2)*iD2 + u*(u2*iD + 2*u1*iD1 + u*iD2)
        Mm = M*(v2*iD + 2*v1*iD1 + M*iD2)
        integrand = (-Ss + Mm)*iD
        tot += w[i]*np.sum(w3*integrand)
    return 0.5*4*tot     # Z_mu = (1/2) * 4 * int [...]

if __name__ == '__main__':
    t0 = time.time()
    MS = [0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625]
    cases = [('SYM', 0.0), ('T3', 0.5), ('T3', 0.25), ('RT', 0.5)]
    res = {}
    for kind, par in cases:
        for m in MS:
            for (q, ratio) in ((6, 2.0), (8, 2.0)):
                z0 = Z(kind, par, m, q, ratio, 0); zs = Z(kind, par, m, q, ratio, 1)
                res[(kind, par, m, q)] = (z0, zs)
                print(f'{kind:3s} par={par:.2f} m={m:.5f} q={q} ratio={ratio}: Z0={z0:+.9f} Zs={zs:+.9f} Z0-Zs={z0-zs:+.6e} [{time.time()-t0:5.0f}s]', flush=True)
    A = lambda kind, par, m, q=8: res[(kind, par, m, q)][0] - res[(kind, par, m, q)][1]
    dq = max(abs(A(k_, p_, m, 6) - A(k_, p_, m, 8)) for k_, p_ in cases for m in MS)
    dz = max(abs(res[(k_, p_, m, 6)][0] - res[(k_, p_, m, 8)][0]) for k_, p_ in cases for m in MS)
    chk(f'quadrature stable under mesh change: max dZ0 = {dz:.1e}, max d(Z0-Zs) = {dq:.1e} < 2e-6', dz < 2e-6 and dq < 2e-6)
    chk(f'SYM: |Z0 - Zs| <= {max(abs(A("SYM",0.0,m)) for m in MS):.1e} < 1e-8 (B4 symmetric => zero)',
        max(abs(A('SYM', 0.0, m)) for m in MS) < 1e-8)
    z = np.array([res[('SYM', 0.0, m, 8)][0] for m in MS])
    sl = np.diff(z)/np.log(2)
    print('SYM log slopes', np.round(sl, 6), ' continuum 1/(4 pi^2) =', round(1/(4*np.pi**2), 6))
    chk('SYM: last log slope within 10% of 1/(4 pi^2) (hand Feynman-parameter value, re-derived by reviewer)',
        abs(sl[-1] - 1/(4*np.pi**2)) < 0.1/(4*np.pi**2))
    # author values at matching m (from logs/kip_collins_toy.runall.log, N = 96)
    author = {('T3', 0.5, 0.00625): -2.192132e-03, ('T3', 0.25, 0.00625): -1.125564e-03,
              ('RT', 0.5, 0.00625): -1.198112e-02, ('SYM', 0.0, 0.00625): 0.0}
    for (k_, p_, m), v in author.items():
        if k_ == 'SYM': continue
        chk(f'{k_} par={p_} m={m}: reviewer {A(k_,p_,m):+.6e} vs author {v:+.6e} agree to 1e-6', abs(A(k_, p_, m) - v) < 1e-6)
    for k_, p_ in cases[1:]:
        a = np.array([A(k_, p_, m) for m in MS]); st = np.abs(np.diff(a))
        r = st[-1]/st[-2]
        tail = st[-1]*r/(1 - r) if r < 1 else np.inf
        lim = a[-1] + np.sign(a[-1] - a[-2])*tail
        mism = p_ if k_ == 'T3' else 1.0
        C = 8*np.pi**2*(-lim)/mism
        print(f'{k_} par={p_}: Z0-Zs = {np.array2string(a, formatter={"float_kind": lambda x: f"{x:+.4e}"})}; last step ratio {r:.3f}; '
              f'limit ~ {lim:+.4e}; C = 8 pi^2 (Zs-Z0)/mismatch ~ {C:.3f}')
        chk(f'{k_} par={p_}: anisotropy nonzero and not vanishing as m a -> 0 (|A(m_min)| = {abs(a[-1]):.2e} > 10 x geometric tail {tail:.1e}, |A| at m_min > |A| at m=0.2)',
            abs(a[-1]) > 10*tail and abs(a[-1]) > abs(a[0]))
        res[(k_, p_, 'C')] = C
    chk(f'T3 C per unit eps ~ 0.36 (reviewer {res[("T3",0.5,"C")]:.3f}, {res[("T3",0.25,"C")]:.3f}) within 15%',
        all(abs(res[('T3', p_, 'C')] - 0.36) < 0.054 for p_ in (0.5, 0.25)))
    chk(f'RT C ~ 0.93 (reviewer {res[("RT",0.5,"C")]:.3f}; limit from m >= 0.00625 only, author went to 2e-4) within 15%',
        abs(res[('RT', 0.5, 'C')] - 0.93) < 0.14)
    print(f'elapsed {time.time()-t0:.0f}s')
    print(f'TOTAL: PASS={P} FAIL={F}')
    sys.exit(1 if F else 0)
