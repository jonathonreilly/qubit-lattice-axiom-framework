#!/usr/bin/env python3
"""s1: Theorem L (W3 = - sum_boxes Ch(P_<)) on infinite-range controls with W3 != 0.

Expected values are NOT fed in: W3 is computed by the 3D integral (independent method),
the right side by certified level decomposition + lattice Chern numbers on box surfaces.
Controls: V_M = (f + i g.sigma)/|(f,g)| (C5's O-covariant analytic maps), n = 2;
coupled n = 3 and n = 4 versions C (V (+) X) with a generic constant coin C near 1.
Levels: eps = 0 and eps = pi.
"""
import sys
import numpy as np
from scipy.linalg import expm
import lib5b as L

C = L.Checker()
rng = np.random.default_rng(5)


def xvec(K, M):
    c, s = np.cos(K), np.sin(K)
    return np.concatenate([(M - c.sum(-1))[..., None], s], -1)


def VM_fun(M):
    def f(K):
        x = xvec(K, M)
        x = x / np.linalg.norm(x, axis=-1, keepdims=True)
        return x[..., 0, None, None] * np.eye(2) + 1j * sum(x[..., j + 1, None, None] * L.PAULI[j] for j in range(3))
    return f


def minnorm(M, N=64):
    k = 2 * np.pi * np.arange(N) / N
    K = np.stack(np.meshgrid(k, k, k, indexing='ij'), -1)
    m = np.linalg.norm(xvec(K, M), axis=-1).min()
    # |x| is 3-Lipschitz in sup norm of k (each |d_a x| = 1); cell half-width pi/N
    return m - 3 * np.pi / N


def VM(M):
    m = minnorm(M)
    assert m > 0
    # ||x/|x| - y/|y||| <= 2|x-y|/|x| and |x(k)-x(k')| <= 3||k-k'||_inf  =>  L = 6/m
    return L.Func(VM_fun(M), 2, 6.0 / m, f'V_{M}')


def coupled(blocks, eta, name):
    n = sum(b.n for b in blocks)
    Kh = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); Kh = (Kh + Kh.conj().T) / 2
    Cc = expm(1j * eta * Kh)

    def f(K):
        out = np.zeros(K.shape[:-1] + (n, n), complex); o = 0
        for b in blocks:
            out[..., o:o + b.n, o:o + b.n] = b(K); o += b.n
        return Cc @ out
    return L.Func(f, n, max(b.L for b in blocks), name)


def const_block(E):
    return L.Func(lambda K: np.exp(-1j * E) * np.ones(K.shape[:-1] + (1, 1)), 1, 0.0, f'e^(-i{E})')


cases = [VM(2.0), VM(0.0), VM(-2.0),
         coupled([VM(2.0), const_block(2.0)], 0.15, 'n3: C(V_2 + e^{-2i})'),
         coupled([VM(2.0), VM(-2.0)], 0.12, 'n4: C(V_2 + V_-2)'),
         coupled([VM(2.0), VM(0.0)], 0.12, 'n4: C(V_2 + V_0)')]
if len(sys.argv) > 1:
    cases = [cases[int(i)] for i in sys.argv[1].split(',')]

for W in cases:
    print(f'=== {W.name}  (n={W.n}, Lipschitz L={W.L:.3f})', flush=True)
    w48 = L.w3_grid(W, 40, 0.3); w64 = L.w3_grid(W, 56, 0.17)
    print(f'  W3 integral: N=40 {w48.real:+.8f}, N=56 {w64.real:+.8f} (imag {abs(w64.imag):.1e})')
    w3 = round(w64.real)
    C.check(f'{W.name}: W3 integral converged to an integer ({w3:+d})', abs(w64.real - w3) < 1e-3 and abs(w48.real - w64.real) < 1e-3)
    for eps in (0.0, np.pi):
        r = L.analyze_level(W, eps, N0=32, depth=4, M=24)
        print(f'  level eps={eps:.4f}: certified bad coarse cells {r["nbad"]}, components {r["ncomp"]}, clean={r["clean"]} {r["reason"]}')
        if not r['clean']:
            C.check(f'{W.name} eps={eps:.3f}: level decomposed into isolated boxes', False)
            continue
        chs = [b['ch'] for b in r['boxes']]
        C.check(f'{W.name} eps={eps:.3f}: box Chern numbers integer and mesh-stable',
                all(abs(b['ch'] - round(b['ch'])) < 1e-9 and abs(b['ch'] - b['ch2']) < 1e-9 for b in r['boxes']))
        s = round(sum(chs))
        print(f'  -> - sum Ch(P_<) = {-s:+d}   vs W3 = {w3:+d}')
        C.check(f'{W.name} eps={eps:.3f}: Theorem L, W3 = -sum Ch(P_<) ({w3:+d} = {-s:+d})', -s == w3)
        # nondegenerate Weyl nodes: -sum chi
        nod = [q for b in r['boxes'] for q in b['nodes']]
        npock = sum(b['pocket'] for b in r['boxes'])
        print(f'  boxes: {len(r["boxes"])}, of which pocket boxes (level crosses a band non-degenerately): {npock}')
        if npock == 0 and all(q['gap_others'] > 1e-3 for q in nod) and all(len(b['nodes']) >= 1 for b in r['boxes']):
            chis = [q['chi'] for q in nod]
            print(f'  nodes exactly at eps: {len(nod)}, chiralities {chis}, -sum chi = {-sum(chis):+d}')
            # boxes where every eigenvalue exp(-i eps) point is one nondegenerate node: Ch = chi
            agree = all(round(b['ch']) == sum(q['chi'] for q in b['nodes']) for b in r['boxes'])
            C.check(f'{W.name} eps={eps:.3f}: per box Ch(P_<) = sum of nodal chiralities (Lemma S)', agree)
C.total()
