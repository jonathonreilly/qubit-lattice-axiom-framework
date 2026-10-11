"""V3 control: honest free-SCALAR seagull (RN L1 / V1 free flow) evaluated as a LOCAL bulk operator.

H = 1/2 sum_x [pi^2 + m^2 phi^2 + sum_j (d_j phi)^2];  P_i(x) = 1/2 (pi_x + pi_{x+e_i}) (phi_{x+e_i} - phi_x) at X = x + e_i/2
K = 1/2 sum_ij hhat_ij sum_x (X_j - c) P_i(x)  == RN L1's K_h = 1/2 h X P (flow velocity eps/2*hhat*sin k); the factor 1/2 enters
    through add(Km, ..., 0.5*w*s1*s2) since add(a,b,v) already gives v z_a z_b.  V1/W1 normalisation (velocity eps*sin k) = 4x.
Weyl quadratic forms 1/2 z^T M z, z = (phi, pi), [z_a, z_b] = i J_ab:  -i[A,B] = 1/2 z^T (A J B - B J A) z  (no c-number).
T1 = -i[K,H], T2 = -[K,[K,H]] built exactly on an open N^d block; bulk (translation-invariant) kernels read at the centre,
evaluated on a periodic L^d grid in k-space: E0/site = 1/(4 L^d) sum_k sum |eig(J M(k))|.
Compared: paramagnetic (linear-only) Hessian; honest seagull <0|T2|0>/site; full; f-sum prediction (full = 0);
Jacobian prediction  E0/site = 1/2 <omega(Phi^{-1} k)>_k.
"""
import numpy as np, scipy.sparse as sp, itertools, sys, time
HH = {'E': np.diag([1., -1., 0.]), 'T2': np.array([[0, 1., 0], [1., 0, 0], [0, 0, 0]]), 'D': np.eye(3)}

def build(d, N, m, ch):
    shape = (N,)*d; n = N**d
    idx = np.arange(n).reshape(shape); coords = list(np.ndindex(shape)); cen = (N-1)/2.0
    hh = HH[ch][:d, :d]
    Hm = sp.lil_matrix((2*n, 2*n)); Km = sp.lil_matrix((2*n, 2*n))
    def add(M, a, b, v):   # add v * z_a z_b symmetrised into 1/2 z^T M z  => M_ab += v, M_ba += v
        M[a, b] += v; M[b, a] += v
    for x in coords:
        i0 = idx[x]
        add(Hm, n+i0, n+i0, 0.5); add(Hm, i0, i0, 0.5*m*m)
        for j in range(d):
            y = list(x); y[j] += 1
            if y[j] < N:
                i1 = idx[tuple(y)]
                # 1/2 (phi_y - phi_x)^2
                add(Hm, i1, i1, 0.5); add(Hm, i0, i0, 0.5); add(Hm, i0, i1, -1.0)
                X = np.array(x, float); X[j] += 0.5
                for jj in range(d):
                    w = hh[j, jj]*(X[jj]-cen)
                    if w == 0: continue
                    # w * 1/2 (pi_x + pi_y)(phi_y - phi_x)
                    for (pa, s1) in [(n+i0, 0.5), (n+i1, 0.5)]:
                        for (fb, s2) in [(i1, 1.0), (i0, -1.0)]:
                            add(Km, pa, fb, 0.5*w*s1*s2)
    # note: 1/2 z^T M z with M_ab = M_ba = v gives v z_a z_b (a != b) and v z_a^2 (a == b, added twice -> 2v*1/2)
    return Hm.tocsr(), Km.tocsr(), idx, n

def Jmul_left(M, n):   # J M with J = [[0, I], [-I, 0]]
    M = M.tocsr()
    top = M[n:, :]; bot = -M[:n, :]
    return sp.vstack([top, bot]).tocsr()

def comm_matrix(A, B, n):  # matrix of -i[A,B]:  A J B - B J A
    return (A @ Jmul_left(B, n) - B @ Jmul_left(A, n)).tocsr()

def bulk_kernels(M, idx, N, d, n, R):
    c = tuple([N//2]*d); i0 = idx[c]
    ker = {}
    err = 0.0
    c1 = list(c); c1[0] += 1; i1 = idx[tuple(c1)]
    for (ra, rb, name) in [(0, 0, 'ff'), (0, 1, 'fp'), (1, 0, 'pf'), (1, 1, 'pp')]:
        row = M.getrow(ra*n + i0).toarray().ravel(); row1 = M.getrow(ra*n + i1).toarray().ravel()
        kk = {}
        for r in itertools.product(range(-R, R+1), repeat=d):
            y = tuple(np.array(c) + np.array(r)); y1 = tuple(np.array(c1) + np.array(r))
            if all(0 <= v < N for v in y1):
                v = row[rb*n + idx[y]]; v1 = row1[rb*n + idx[y1]]
                err = max(err, abs(v - v1))
                if abs(v) > 1e-13: kk[r] = v
        ker[name] = kk
    return ker, err

def symbol(ker, L, d):
    k1 = 2*np.pi*np.arange(L)/L
    K = np.stack(np.meshgrid(*([k1]*d), indexing='ij'), -1).reshape(-1, d)
    S = np.zeros((K.shape[0], 2, 2), complex)
    for (a, b, name) in [(0, 0, 'ff'), (0, 1, 'fp'), (1, 0, 'pf'), (1, 1, 'pp')]:
        for r, v in ker[name].items():
            S[:, a, b] += v*np.exp(1j*K @ np.array(r, float))
    return S, K

Jk = np.array([[0, 1], [-1, 0]], complex)
def e0(S):
    ev = np.linalg.eigvals(np.einsum('ab,kbc->kac', Jk, S))
    return 0.25*np.abs(ev).sum()/S.shape[0], np.max(np.abs(ev.real))

def flow_inv(p, eps, hh, nsteps=200):
    x = p.copy(); h = 1.0/nsteps
    def rhs(x): return -eps*(np.einsum('ij,...i->...j', hh, np.sin(x)))
    for _ in range(nsteps):
        a1 = rhs(x); a2 = rhs(x+h/2*a1); a3 = rhs(x+h/2*a2); a4 = rhs(x+h*a3)
        x = x + h/6*(a1+2*a2+2*a3+a4)
    return x

def hess(f, de):
    vals = {e: f(e) for e in [-de, -de/2, 0, de/2, de]}
    D = lambda e: (vals[e]+vals[-e]-2*vals[0])/e**2
    return (4*D(de/2)-D(de))/3

if __name__ == '__main__':
    d = int(sys.argv[1]); N = int(sys.argv[2]); L = int(sys.argv[3]); m = float(sys.argv[4])
    chans = sys.argv[5].split(',')
    t0 = time.time()
    for ch in chans:
        hh = HH[ch][:d, :d]
        H, K, idx, n = build(d, N, m, ch)
        T1 = comm_matrix(K, H, n); T2 = comm_matrix(K, T1, n)
        kH, eH = bulk_kernels(H, idx, N, d, n, 2)
        k1, e1 = bulk_kernels(T1, idx, N, d, n, 4)
        k2, e2 = bulk_kernels(T2, idx, N, d, n, 6)
        S0, Kg = symbol(kH, L, d); S1, _ = symbol(k1, L, d); S2, _ = symbol(k2, L, d)
        E00, rre = e0(S0)
        # honest seagull: <0| 1/2 z^T T2 z |0> per site = 1/2 Tr(T2(k) G(k)) averaged; G from S0 = diag(w^2, 1): G_ff = 1/(2w), G_pp = w/2
        w = np.sqrt(np.real(S0[:, 0, 0]))
        sg = np.mean(0.5*(np.real(S2[:, 0, 0])/(2*w) + np.real(S2[:, 1, 1])*w/2))   # Hessian of eps^2/2 <T2> = <T2>; <1/2 z T2 z>
        para = hess(lambda e: e0(S0 + e*S1)[0], 0.01)
        full = hess(lambda e: e0(S0 + e*S1 + 0.5*e*e*S2)[0], 0.01)
        def jac(Lg):
            k1g = 2*np.pi*np.arange(Lg)/Lg
            P = np.stack(np.meshgrid(*([k1g]*d), indexing='ij'), -1).reshape(-1, d)
            return hess(lambda e: 0.5*np.sqrt(m**2 + (4*np.sin(flow_inv(P, e, hh)/2)**2).sum(1)).mean(), 0.02)
        print(f'scalar d={d} N={N} L={L} m={m} ch={ch}: transl err H {eH:.1e} T1 {e1:.1e} T2 {e2:.1e}; E0/site {E00:.6f} (check 1/2<w> {0.5*w.mean():.6f})')
        print(f'   paramagnetic Hessian/site = {para:+.8e}  (this IS RN L1 normalisation; V1 norm x4: {4*para:+.8e})')
        print(f'   honest seagull/site       = {sg:+.8e}  (f-sum would give {-para:+.8e})')
        print(f'   full Hessian/site         = {full:+.8e}  (para+sg {para+sg:+.8e});  V1 norm x4: {4*full:+.8e}')
        print(f'   Jacobian prediction (V1 norm, velocity eps sin k; divide by 4 for RN L1) = same grid {jac(L):+.8e};  L=40 {jac(40):+.8e}   [{time.time()-t0:.0f}s]')
        sys.stdout.flush()
