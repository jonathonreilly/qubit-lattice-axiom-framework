#!/usr/bin/env python3
"""Direct test of Lemma LW on a small torus, abelian, U = 1.
Criteria, written before the run. For (d, s) in {(2,3), (2,5), (2,9), (3,3)}, with s = L^j (s = 9 is L = 3, j = 2),
random level-j bond field h on a torus of N level-j cells:
 (a) d Wh_1 h = Wh_2 d h on fine plaquettes: max error < 1e-10;
 (b) Q^o Wh_1 h = T h, with T the product of tau(P_i), by FFT: max error < 1e-10;
 (c) ||Wh_2 B||^2 <= ||B||^2 on random B: ratio <= 1 + 1e-10;
 (d) H := Wh_1 T^-1 h has Q^o H = h: max error < 1e-10, and ||d H||^2 / ||d h||^2 <= 256.
 Control: replace tau by 1 in (b): the error must exceed 1e-3, so the test can fail.
FAIL is kept. Abelian at U = 1 only; a nonabelian background is not tested.
"""
import numpy as np, itertools, resource, sys
rng = np.random.default_rng(1)
def rss_ok(): return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 2e9
def tent_w(x, s):
    m = x // s; f = (x % s) / s
    return m, f
def lift1(h, s, N, d):
    F = N * s
    H = [np.zeros((F,) * d) for _ in range(d)]
    for mu in range(d):
        for x in itertools.product(range(F), repeat=d):
            m = [xi // s for xi in x]
            f = [(xi % s) / s for xi in x]
            others = [i for i in range(d) if i != mu]
            v = 0.0
            for bits in itertools.product((0, 1), repeat=d - 1):
                w = 1.0
                y = list(m)
                for b, o in zip(bits, others):
                    w *= f[o] if b else 1 - f[o]
                    y[o] = (m[o] + b) % N
                v += w * h[mu][tuple(y)]
            H[mu][x] = v / s
    return H
def curl(A, mu, nu):
    return np.roll(A[nu], -1, mu) - A[nu] - np.roll(A[mu], -1, nu) + A[mu]
def lift2(B, s, N, d, mu, nu):
    F = N * s
    out = np.zeros((F,) * d)
    others = [i for i in range(d) if i not in (mu, nu)]
    for x in itertools.product(range(F), repeat=d):
        m = [xi // s for xi in x]
        f = [(xi % s) / s for xi in x]
        v = 0.0
        for bits in itertools.product((0, 1), repeat=len(others)):
            w = 1.0
            y = list(m)
            for b, o in zip(bits, others):
                w *= f[o] if b else 1 - f[o]
                y[o] = (m[o] + b) % N
            v += w * B[tuple(y)]
        out[x] = v / s ** 2
    return out
def Qo(H, s, N, d):
    r = (s - 1) // 2
    F = N * s
    out = [np.zeros((N,) * d) for _ in range(d)]
    # prefix over box and line by rolling
    for mu in range(d):
        A = H[mu].copy()
        # line sum along mu
        L = np.zeros_like(A)
        for t in range(s):
            L += np.roll(A, -t, mu)
        # box average in all directions, centred
        for nu in range(d):
            B = np.zeros_like(L)
            for t in range(-r, r + 1):
                B += np.roll(L, -t, nu)
            L = B / s
        out[mu] = L[tuple(slice(0, F, s) for _ in range(d))]
    return out
def tau(P, s): return 1 - (s ** 2 - 1) * (1 - np.cos(P)) / (4 * s ** 2)
def T_apply(h, s, N, d, inv=False, control=False):
    grids = np.meshgrid(*[2 * np.pi * np.fft.fftfreq(N) for _ in range(d)], indexing='ij')
    sym = np.ones_like(grids[0])
    for g in grids: sym = sym * tau(g, s)
    if control: sym = np.ones_like(sym)
    if inv: sym = 1 / sym
    return [np.real(np.fft.ifftn(np.fft.fftn(c) * sym)) for c in h]
ok = True
for d, s in ((2, 3), (2, 5), (2, 9), (3, 3)):
    N = 4
    h = [rng.normal(size=(N,) * d) for _ in range(d)]
    H = lift1(h, s, N, d)
    e_a = 0.0
    ratio_c = 0.0
    for mu, nu in itertools.combinations(range(d), 2):
        dh = np.roll(h[nu], -1, mu) - h[nu] - np.roll(h[mu], -1, nu) + h[mu]
        e_a = max(e_a, np.max(np.abs(curl(H, mu, nu) - lift2(dh, s, N, d, mu, nu))))
        B = rng.normal(size=(N,) * d)
        ratio_c = max(ratio_c, np.sum(lift2(B, s, N, d, mu, nu) ** 2) / np.sum(B ** 2))
    q = Qo(H, s, N, d)
    Th = T_apply(h, s, N, d)
    Tc = T_apply(h, s, N, d, control=True)
    e_b = max(np.max(np.abs(a - b)) for a, b in zip(q, Th))
    e_ctl = max(np.max(np.abs(a - b)) for a, b in zip(q, Tc))
    hi = T_apply(h, s, N, d, inv=True)
    H2 = lift1(hi, s, N, d)
    q2 = Qo(H2, s, N, d)
    e_d = max(np.max(np.abs(a - b)) for a, b in zip(q2, h))
    num = sum(np.sum(curl(H2, m, n) ** 2) for m, n in itertools.combinations(range(d), 2))
    den = sum(np.sum((np.roll(h[n], -1, m) - h[n] - np.roll(h[m], -1, n) + h[m]) ** 2) for m, n in itertools.combinations(range(d), 2))
    print(f"d={d} s={s} a={e_a:.2e} b={e_b:.2e} ctl={e_ctl:.3f} c={ratio_c:.4f} d={e_d:.2e} curl_ratio={num/den:.3f}", flush=True)
    if e_a > 1e-10 or e_b > 1e-10 or ratio_c > 1 + 1e-10 or e_d > 1e-10 or num / den > 256 or e_ctl < 1e-3:
        ok = False
    if not rss_ok(): print("RSS cap"); sys.exit(2)
print("PASS" if ok else "FAIL")
