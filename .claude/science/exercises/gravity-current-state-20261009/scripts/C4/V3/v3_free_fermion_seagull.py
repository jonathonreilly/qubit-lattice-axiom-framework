"""V3 (lane RV3): honest free-fermion seagull check for the staggered fermion under the density-transport strain flow.

Setting (S1/RN L1 conventions):
  h = sum_{x,j} (i/2) eta_j(x) (c_x^dag c_{x+j} - h.c.) + m sum_x eps(x) n_x
  P_j = sum_x (c_x^dag c_{x+2e_j} - h.c.)/(4i)   (symbol 1/2 sin 2p_j, scalar, [h,P_j]=0), density placed at X = x + e_j
  K = sum_{ij} hhat_ij sum_x (X_j - c_j) P_i(x)   (W1/V1 normalization: flow velocity eps*hhat*f, f = 1/2 sin 2p;
                                                     RN L1's K_h = 1/2 h X P is 1/4 of these Hessians)
  H(eps) = e^{-i eps K} H e^{i eps K} = H + eps T1 + eps^2/2 T2,  T1 = -i[K,h],  T2 = -[K,[K,h]]   (one-body, exact matrices)
Method: build T1, T2 EXACTLY on an open N^d block (sparse), read their bulk kernels at a central cell (checked translation
invariant by 2), copy them onto a periodic L^d torus, and compute the half-filled ground energy per site of
   h + eps T1            (linear-only coupling: 'paramagnetic' Hessian)
   h + eps T1 + eps^2/2 T2  (unitary coupling with its local seagull: full Hessian)
and the honest seagull <sea|T2|sea>/site. No f-sum identity is assumed anywhere.
Predictions compared:  (a) f-sum: full Hessian = 0;  (b) Jacobian anomaly: E_sea/site = -1/2 <omega(Phi^{-1} p)>_p, whose
Hessian is -1/2 * sum_p d^2/deps^2 omega(Phi_eps^{-1}(p)) on the same torus grid (Phi = flow p' = eps hhat f).
"""
import numpy as np, scipy.sparse as sp, itertools, sys, time

def build(d, N, m, ch):
    shape = (N,)*d
    idx = np.arange(N**d).reshape(shape)
    coords = np.array(list(np.ndindex(shape)))
    cen = (N-1)/2.0
    H = sp.lil_matrix((N**d, N**d), dtype=complex)
    Pd = [sp.lil_matrix((N**d, N**d), dtype=complex) for _ in range(d)]   # first-moment-weighted P_i, per moment axis j
    hh = HH[ch][:d, :d]
    Kmat = sp.lil_matrix((N**d, N**d), dtype=complex)
    for n, x in enumerate(coords):
        H[n, n] += m*(-1)**int(x.sum())
        for j in range(d):
            eta = (-1)**int(x[:j].sum())
            y = x.copy(); y[j] += 1
            if y[j] < N:
                ny = idx[tuple(y)]
                H[n, ny] += 0.5j*eta; H[ny, n] += -0.5j*eta
            y2 = x.copy(); y2[j] += 2
            if y2[j] < N:
                ny2 = idx[tuple(y2)]
                X = x.astype(float); X[j] += 1.0          # bond centre
                for jj in range(d):
                    w = hh[j, jj]*(X[jj]-cen)              # hhat_{i=j, jj} (X_jj - c)
                    if w != 0:
                        Kmat[n, ny2] += w/(4j); Kmat[ny2, n] += -w/(4j)
    return H.tocsr(), Kmat.tocsr(), coords, idx

HH = {'E': np.diag([1., -1., 0.]), 'T2': np.array([[0, 1., 0], [1., 0, 0], [0, 0, 0]]), 'D': np.eye(3)}

def bulk_kernel(M, coords, idx, N, d, R):
    """kernel rows at the 2^d central cell sites; check translation invariance by 2e_j"""
    c0 = N//2 - 1 if (N//2) % 2 else N//2
    c0 = c0 - (c0 % 2)
    ker = {}
    err = 0.0
    for A in itertools.product([0, 1], repeat=d):
        x0 = np.array([c0 + a for a in A]); n0 = idx[tuple(x0)]
        row = M.getrow(n0).toarray().ravel()
        kA = {}
        for r in itertools.product(range(-R, R+1), repeat=d):
            y = x0 + np.array(r)
            if np.all(y >= 0) and np.all(y < N):
                v = row[idx[tuple(y)]]
                if abs(v) > 1e-13: kA[r] = v
        ker[A] = kA
        # translation check: x0 + 2 e_0
        x1 = x0.copy(); x1[0] += 2; n1 = idx[tuple(x1)]
        row1 = M.getrow(n1).toarray().ravel()
        for r, v in kA.items():
            y = x1 + np.array(r)
            if np.all(y >= 0) and np.all(y < N):
                err = max(err, abs(row1[idx[tuple(y)]] - v))
    return ker, err

def periodic(ker, L, d):
    shape = (L,)*d
    idx = np.arange(L**d).reshape(shape)
    M = np.zeros((L**d, L**d), dtype=complex)
    for x in np.ndindex(shape):
        A = tuple(int(v) % 2 for v in x); n = idx[x]
        for r, v in ker[A].items():
            y = tuple((np.array(x) + np.array(r)) % L)
            M[n, idx[y]] += v
    return M

def sea_energy(Hm):
    w = np.linalg.eigvalsh(Hm)
    return w[w < 0].sum(), w

def flow_inv(p, eps, hh, nsteps=200):
    """Phi_eps^{-1}(p): integrate p' = -eps hhat^T f(p), f = 1/2 sin 2p, componentwise velocity v_j = sum_i hhat_ij f_i"""
    x = p.copy(); h = 1.0/nsteps
    def rhs(x): return -eps*(np.einsum('ij,...i->...j', hh, 0.5*np.sin(2*x)))
    for _ in range(nsteps):
        a1 = rhs(x); a2 = rhs(x+h/2*a1); a3 = rhs(x+h/2*a2); a4 = rhs(x+h*a3)
        x = x + h/6*(a1+2*a2+2*a3+a4)
    return x

def jac_pred(L, d, m, ch, de=0.02):
    hh = HH[ch][:d, :d]
    k1 = 2*np.pi*np.arange(L)/L
    P = np.stack(np.meshgrid(*([k1]*d), indexing='ij'), -1).reshape(-1, d)
    def E(e):
        q = flow_inv(P, e, hh)
        return -0.5*np.sqrt(m**2 + (np.sin(q)**2).sum(1)).mean()
    vals = {e: E(e) for e in [-de, -de/2, 0, de/2, de]}
    D = lambda e: (vals[e]+vals[-e]-2*vals[0])/e**2
    return (4*D(de/2)-D(de))/3

if __name__ == '__main__':
    d = int(sys.argv[1]); N = int(sys.argv[2]); L = int(sys.argv[3]); m = float(sys.argv[4])
    chans = sys.argv[5].split(',') if len(sys.argv) > 5 else ['E', 'T2']
    t0 = time.time()
    for ch in chans:
        H, K, coords, idx = build(d, N, m, ch)
        # checks: [h, P_total] in bulk via K with hhat=0 not available; check T1 bulk translation invariance instead
        T1 = (-1j*(K@H - H@K)).tocsr()
        T2 = (-(K@T1 - T1@K)*1j*1j*(-1)).tocsr()    # -[K,[K,h]] = -[K, i T1]... see below
        # careful: T1 = -i[K,h]  =>  [K,h] = i T1  =>  T2 = -[K,[K,h]] = -i [K, T1]
        T2 = (-1j*(K@T1 - T1@K)).tocsr()
        kH, eH = bulk_kernel(H, coords, idx, N, d, 3)
        k1_, e1 = bulk_kernel(T1, coords, idx, N, d, 4)
        k2_, e2 = bulk_kernel(T2, coords, idx, N, d, 6)
        rng1 = max(max(max(abs(np.array(r))) for r in kk) for kk in k1_.values())
        rng2 = max(max(max(abs(np.array(r))) for r in kk) for kk in k2_.values())
        Hp = periodic(kH, L, d); T1p = periodic(k1_, L, d); T2p = periodic(k2_, L, d)
        herm = max(np.abs(T1p-T1p.conj().T).max(), np.abs(T2p-T2p.conj().T).max())
        nsite = L**d
        E0, w0 = sea_energy(Hp)
        gap = np.min(np.abs(w0))
        # seagull expectation <sea|T2|sea>: Tr(P_- T2)
        w, V = np.linalg.eigh(Hp); Vm = V[:, w < 0]
        sg = np.real(np.trace(Vm.conj().T @ T2p @ Vm))/nsite     # = d^2/deps^2 of <sea| eps^2/2 T2|sea>
        t1diag = np.real(np.trace(Vm.conj().T @ T1p @ Vm))/nsite
        def hessian(f, de):
            vals = {e: f(e) for e in [-de, -de/2, 0, de/2, de]}
            D = lambda e: (vals[e]+vals[-e]-2*vals[0])/e**2
            return (4*D(de/2)-D(de))/3
        de = 0.01
        para = hessian(lambda e: sea_energy(Hp + e*T1p)[0]/nsite, de)
        full = hessian(lambda e: sea_energy(Hp + e*T1p + 0.5*e*e*T2p)[0]/nsite, de)
        jp = jac_pred(L, d, m, ch)
        jinf = jac_pred(64 if d < 3 else 32, d, m, ch)
        print(f'd={d} N={N} L={L} m={m} ch={ch}: kernel transl. err H {eH:.1e} T1 {e1:.1e} T2 {e2:.1e}; ranges T1 {rng1} T2 {rng2}; '
              f'herm err {herm:.1e}; sea gap {gap:.3f}; <T1>/site {t1diag:+.2e}')
        print(f'   paramagnetic (linear-only) Hessian/site = {para:+.8e}')
        print(f'   honest seagull <sea|T2|sea>/site       = {sg:+.8e}')
        print(f'   f-sum seagull would be                  = {-para:+.8e}')
        print(f'   full unitary Hessian/site               = {full:+.8e}   (para+seagull = {para+sg:+.8e})')
        print(f'   Jacobian-anomaly prediction (same grid) = {jp:+.8e};  continuum (L={64 if d<3 else 32}) {jinf:+.8e}   [{time.time()-t0:.0f}s]')
        sys.stdout.flush()
