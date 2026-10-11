"""S2 operator-level cross-check (V3 method) for a NON-SEPARABLE momentum density.
Momentum density P_i(x) = sum_r w_r pi_x phi_{x+r} placed at X = x + r/2 (placement is irrelevant: shifts add c*P_tot, which commutes with H).
Symbol convention: p(k) = -i sum_r w_r e^{i k.r}  (V3's P_x = 1/2(pi_x+pi_{x+e})(phi_{x+e}-phi_x) has p = sin k).
K = 1/2 sum_ij hhat_ij sum_x (X_j - c) P_i(x)  (RN L1 normalisation).  T1 = -i[K,H], T2 = -[K,[K,H]] built exactly on an open N^d block,
bulk kernels copied onto a periodic L^d torus, full Hessian of E0/site(H + eps T1 + eps^2/2 T2) compared with the Jacobian quadratic form."""
import numpy as np, scipy.sparse as sp, sys, time
from v3_free_scalar_seagull_copy import Jmul_left, comm_matrix, bulk_kernels, symbol, e0, hess, HH
from s2_core import quad_forms, kg_vac

def stencil(kind, d):
    """returns dict r->w for P_x."""
    if kind == 'sin':
        r1 = [0]*d; r1[0] = 1; r2 = [0]*d; r2[0] = -1
        return {tuple(r1): 0.5, tuple(r2): -0.5}
    if kind == 'diag':   # p_x = sin kx prod_{j>0} cos kj
        out = {}
        import itertools
        for sg in itertools.product([1, -1], repeat=d):
            out[tuple(sg)] = sg[0]*0.5**d
        return out
    raise ValueError

def build(d, N, m, ch, sten):
    shape = (N,)*d; n = N**d
    idx = np.arange(n).reshape(shape); coords = list(np.ndindex(shape)); cen = (N-1)/2.0
    hh = HH[ch][:d, :d]
    Hm = sp.lil_matrix((2*n, 2*n)); Km = sp.lil_matrix((2*n, 2*n))
    def add(M, a, b, v):
        M[a, b] += v; M[b, a] += v
    for x in coords:
        i0 = idx[x]
        add(Hm, n+i0, n+i0, 0.5); add(Hm, i0, i0, 0.5*m*m)
        for j in range(d):
            y = list(x); y[j] += 1
            if y[j] < N:
                i1 = idx[tuple(y)]
                add(Hm, i1, i1, 0.5); add(Hm, i0, i0, 0.5); add(Hm, i0, i1, -1.0)
        for i in range(d):                       # component P_i: permute stencil axes 0 <-> i
            for r, w in sten.items():
                rr = list(r); rr[0], rr[i] = rr[i], rr[0]
                y = tuple(np.array(x) + np.array(rr))
                if not all(0 <= v < N for v in y): continue
                X = np.array(x, float) + 0.5*np.array(rr, float)
                for jj in range(d):
                    c = 0.5*hh[i, jj]*(X[jj]-cen)*w
                    if c == 0: continue
                    # c * pi_x phi_y : add(a,b,v) gives v z_a z_b ; pi and phi at different (or same) sites commute -> fine
                    add(Km, n+i0, idx[y], 0.5*c) if False else None
                    Km[n+i0, idx[y]] += c; Km[idx[y], n+i0] += c   # gives c*pi_x*phi_y in 1/2 z^T M z
    return Hm.tocsr(), Km.tocsr(), idx, n

if __name__ == '__main__':
    t0 = time.time()
    for d, N, L in [(2, 22, 64), (3, 13, 24)]:
        for kind in ['sin', 'diag']:
            for m in [1.0]:
                for ch in ['E', 'T2']:
                    sten = stencil(kind, d)
                    H, K, idx, n = build(d, N, m, ch, sten)
                    T1 = comm_matrix(K, H, n); T2 = comm_matrix(K, T1, n)
                    Rr = 2 if kind == 'diag' else 1
                    kH, eH = bulk_kernels(H, idx, N, d, n, 2)
                    k1, e1 = bulk_kernels(T1, idx, N, d, n, 2*Rr+1)
                    k2, e2 = bulk_kernels(T2, idx, N, d, n, 4*Rr+2)
                    S0, _ = symbol(kH, L, d); S1, _ = symbol(k1, L, d); S2, _ = symbol(k2, L, d)
                    para = hess(lambda e: e0(S0 + e*S1)[0], 0.01)
                    full = hess(lambda e: e0(S0 + e*S1 + 0.5*e*e*S2)[0], 0.01)
                    t = (1,)+(0,)*(d-1) if kind == 'sin' else (1,)*d
                    Q = quad_forms(d, L, [t], lambda Kk: kg_vac(Kk, m), chans=(ch,))   # same grid? core uses midpoint grid
                    Qf = quad_forms(d, 64 if d == 3 else 256, [t], lambda Kk: kg_vac(Kk, m), chans=(ch,))
                    print(f"d={d} N={N} L={L} p={kind:4s} m={m} {ch:2s}: transl.err T1 {e1:.1e} T2 {e2:.1e} | operator para {para:+.6e} full {full:+.8e} | "
                          f"Jacobian form (continuum) {Qf[ch][0,0]:+.8e}   [{time.time()-t0:.0f}s]")
                    sys.stdout.flush()
