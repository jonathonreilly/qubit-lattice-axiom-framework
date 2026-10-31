"""ba1 (BFT lane A): degree-0 lattice CZ kernels inside one coarse unit, sup->sup versus coarse-Hoelder->sup.
Criteria: checks/ba1_criteria.md (written before this script). Kernels, quantities and criteria as stated there.
"""
import os, sys, time, resource
import numpy as np

NS = [6, 9, 12, 18, 27, 36, 54]
ALPHAS = [0.5, 0.25]


def kernels(N):
    p = 2 * np.pi * np.arange(N) / N
    nu = np.exp(1j * p) - 1.0
    ph = (np.abs(nu) ** 2)
    ph_half = ph[: N // 2 + 1]
    # broadcast shapes: axes (1,2,3,4); last axis halved for irfftn
    n1 = nu.reshape(N, 1, 1, 1)
    n2 = nu.reshape(1, N, 1, 1)
    a1 = ph.reshape(N, 1, 1, 1)
    a2 = ph.reshape(1, N, 1, 1)
    a3 = ph.reshape(1, 1, N, 1)
    a4 = ph_half.reshape(1, 1, 1, N // 2 + 1)
    phi = a1 + a2 + a3 + a4
    phi[0, 0, 0, 0] = 1.0
    out = {}
    s12 = (n1 * np.conj(n2)) / phi
    s12[0, 0, 0, 0] = 0.0
    out['K12'] = np.fft.irfftn(s12, s=(N,) * 4, axes=(0, 1, 2, 3))
    del s12
    s11 = (a1 + a2) / phi - 0.5
    s11[0, 0, 0, 0] = 0.0
    out['K11'] = np.fft.irfftn(s11.astype(complex), s=(N,) * 4, axes=(0, 1, 2, 3))
    del s11, phi
    return out


def dist(N):
    y = np.arange(N)
    y = np.minimum(y, N - y).astype(float) ** 2
    return np.sqrt(y.reshape(N, 1, 1, 1) + y.reshape(1, N, 1, 1) + y.reshape(1, 1, N, 1) + y.reshape(1, 1, 1, N))


def boxsum_max(K, N):
    # max over R < N/2 of |sum_{|y|_inf <= R} K(y)|
    y = np.arange(N)
    yi = np.minimum(y, N - y)
    linf = np.maximum(np.maximum(yi.reshape(N, 1, 1, 1), yi.reshape(1, N, 1, 1)),
                      np.maximum(yi.reshape(1, 1, N, 1), yi.reshape(1, 1, 1, N)))
    best = 0.0
    for R in range(0, (N - 1) // 2 + 1):
        if 2 * R + 1 > N:
            break
        best = max(best, abs(K[linf <= R].sum()))
    return best


def holder_lower(g, N, alpha):
    # lower bound for the pointwise alpha-Hoelder seminorm: axis and main-diagonal shifts of lengths 1, 2, 4, ...
    best = 0.0
    L = 1
    while L <= N // 2:
        for sh in [(L, 0, 0, 0), (0, L, 0, 0), (L, L, 0, 0), (L, L, L, L)]:
            d = np.max(np.abs(np.roll(g, sh, axis=(0, 1, 2, 3)) - g))
            best = max(best, d / (np.sqrt(sum(s * s for s in sh)) ** alpha))
        L *= 2
    return best


def main():
    t0 = time.time()
    print('ba1 start', time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()))
    res = {}
    for N in NS:
        Ks = kernels(N)
        r = dist(N)
        nz = r > 0
        for name, K in Ks.items():
            S1 = np.abs(K).sum()
            CK = (r[nz] ** 4 * np.abs(K[nz])).max()
            tot = K.sum()
            A = {a: (np.abs(K[nz]) * r[nz] ** a).sum() / N ** a for a in ALPHAS}
            bs = boxsum_max(K, N)
            # sup-worst source at x = 0: g(y) = sign K(-y); then (K*g)(0) = S1 exactly. Its Hoelder seminorm equals that of
            # sign K (a reflection), so the lower bound is computed on sign K.
            g = np.sign(K)
            resp0 = S1
            hc = N ** 0.5 * holder_lower(g, N, 0.5)
            res[(N, name)] = dict(S1=S1, CK=CK, A=A, bs=bs, tot=tot)
            print(f'N={N:3d} {name}: S1={S1:.6f} C_K={CK:.6f} A_0.5={A[0.5]:.6f} A_0.25={A[0.25]:.6f} '
                  f'maxbox={bs:.3e} sumK={tot:.1e} K(0)={K[0,0,0,0]:.6f} | worst-src resp(0)={resp0:.6f} '
                  f'[g]^c_0.5>={hc:.3f} ratio<={resp0/hc:.4f}')
            sys.stdout.flush()
        del Ks, r, nz
    print('--- criteria ---')
    ok_all = True
    for name in ['K12', 'K11']:
        S = [res[(N, name)]['S1'] for N in NS]
        inc = all(S[i + 1] > S[i] for i in range(len(S) - 1))
        a1 = inc and (S[-1] - S[0] >= 0.5)
        sl = np.polyfit(np.log(NS[2:]), S[2:], 1)[0]
        A = {N: res[(N, name)]['A'][0.5] for N in NS}
        big = [A[N] for N in NS if N >= 18]
        a2 = abs(A[54] - A[27]) <= 0.15 * A[54] and max(big) <= 1.25 * min(big)
        a3 = res[(54, name)]['CK'] <= 1.2 * res[(27, name)]['CK']
        print(f'{name}: A1 {"PASS" if a1 else "FAIL"} (increasing={inc}, S1(54)-S1(6)={S[-1]-S[0]:.4f}, '
              f'slope dS1/dlnN (N>=12) = {sl:.4f}); A2 {"PASS" if a2 else "FAIL"} '
              f'(|A54-A27|/A54={abs(A[54]-A[27])/A[54]:.4f}, max/min(N>=18)={max(big)/min(big):.4f}); '
              f'A3 {"PASS" if a3 else "FAIL"} (C_K54/C_K27={res[(54,name)]["CK"]/res[(27,name)]["CK"]:.4f})')
        ok_all = ok_all and a1 and a2 and a3
    print('overall', 'PASS' if ok_all else 'FAIL (see lines above)')
    pk = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30  # bytes on macOS
    print(f'elapsed {time.time()-t0:.1f} s, peak RSS {pk:.3f} GB')
    print('ba1 end', time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()))


if __name__ == '__main__':
    main()
