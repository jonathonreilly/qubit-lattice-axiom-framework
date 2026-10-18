"""Reviewer check of Prop. E: W3[V_M] by three methods independent of the worker's code.
(a) trace formula on the UNNORMALISED W = f + i g.sigma in GL(2) (scalar-invariance of W3 used, also tested);
(b) S^3 degree form deg = (1/2pi^2) int det[d, d1 d, d2 d, d3 d]/|d|^4;
(c) signed preimage count of a random regular value q in S^3 (Newton from a start grid, deduplicated).
"""
import sys, itertools, numpy as np
from scipy.optimize import fsolve
from rlib import S, Ck, w3_GL, grid
ck = Ck()
def fields(M, K):
    K1,K2,K3 = K
    d = np.stack([M-np.cos(K1)-np.cos(K2)-np.cos(K3), np.sin(K1), np.sin(K2), np.sin(K3)], -1)
    dd = []
    for b,Kb in enumerate(K):
        v = np.zeros_like(d); v[...,0] = np.sin(Kb); v[...,1+b] = np.cos(Kb); dd.append(v)
    return d, dd
def toW(d):
    return d[...,0,None,None]*S[0] + 1j*sum(d[...,a+1,None,None]*S[a+1] for a in range(3))
def w3_trace_unnorm(M, N):
    d, dd = fields(M, grid(N, 0.5))
    return w3_GL(toW(d), [toW(x) for x in dd]).real
def w3_trace_norm(M, N):
    # normalised U = W/|d| with derivative via product rule, then same GL formula
    d, dd = fields(M, grid(N, 0.5)); n = np.linalg.norm(d, axis=-1)
    U = toW(d)/n[...,None,None]
    dU = [toW(x)/n[...,None,None] - toW(d)*((d*x).sum(-1)/n**3)[...,None,None] for x in dd]
    return w3_GL(U, dU).real
def deg_form(M, N):
    d, dd = fields(M, grid(N, 0.5))
    J = np.stack([d]+dd, -1)  # columns d, d1d, d2d, d3d
    return (np.linalg.det(J)/np.linalg.norm(d,axis=-1)**4).mean()*(2*np.pi)**3/(2*np.pi**2)
def preimage_degree(M, q, starts=10):
    q = q/np.linalg.norm(q)
    # orthonormal complement of q
    B = np.linalg.svd(q[None,:])[2][1:]
    def F(k): return B @ fields(M, [np.array(x) for x in k])[0]
    roots = []
    for s in itertools.product(*(2*np.pi*(np.arange(starts)+0.25)/starts,)*3):
        sol, info, ier, _ = fsolve(F, np.array(s), full_output=True, xtol=1e-13)
        if ier != 1: continue
        sol = np.mod(sol, 2*np.pi)
        d, dd = fields(M, [np.array(x) for x in sol])
        if np.linalg.norm(B @ d) > 1e-10 or d @ q <= 0: continue
        if any(np.linalg.norm(np.angle(np.exp(1j*(sol-r)))) < 1e-6 for r in roots): continue
        roots.append(sol)
    sg = []
    for r in roots:
        d, dd = fields(M, [np.array(x) for x in r])
        sg.append(np.sign(np.linalg.det(np.stack([d]+dd, -1))))
    return int(round(sum(sg))), len(roots)
rng = np.random.default_rng(2026)
expected_worker = {4.0: 0, 2.0: -1, 0.0: 2, -2.0: -1, 0.5: 2}
for M in (2.0, 0.0, 4.0, -2.0):
    tr = [w3_trace_unnorm(M, N) for N in (16, 32, 48)]
    trn = w3_trace_norm(M, 48)
    dg = [deg_form(M, N) for N in (16, 32, 48)]
    pre = [preimage_degree(M, rng.normal(size=4)) for _ in range(2)]
    print(f'M={M:+.1f}: trace(W unnormalised) N=16,32,48 {tr[0]:+.10f} {tr[1]:+.10f} {tr[2]:+.10f}; trace(normalised) {trn:+.10f}; '
          f'degree form {dg[0]:+.10f} {dg[1]:+.10f} {dg[2]:+.10f}; preimage (deg, #roots) {pre}', flush=True)
    ck(f'M={M}: trace-formula W3 converged to integer {round(tr[2])} (|N=32 - N=48| < 1e-8, dist to int < 1e-8)',
       abs(tr[1]-tr[2]) < 1e-8 and abs(tr[2]-round(tr[2])) < 1e-8)
    ck(f'M={M}: scalar invariance W3[W] = W3[W/|W|]', abs(tr[2]-trn) < 1e-8)
    ck(f'M={M}: worker value W3 = {expected_worker[M]} reproduced', round(tr[2]) == expected_worker[M])
    ck(f'M={M}: degree form and preimage count agree with each other and with W3 = +deg (det[d,d1d,d2d,d3d] orientation; run 1 guessed -deg, wrong)',
       round(dg[2]) == pre[0][0] == pre[1][0] == round(tr[2]))
sys.exit(ck.total())
