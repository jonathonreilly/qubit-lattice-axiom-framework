"""R6-1: (1) many-body Fock check of [Q,H]=0 and [P,H]=0 for witness W (fermions, d=2, L=16);
(2) analytic comparator [Q,H_an] != 0; (3) real-space decay of the form-factor kernel (quasi-locality);
(4) the T = UV construction: P = sum p(k) n_k with p smooth periodic, p = qhat on the box;
V = T exp(-iP) has one-body symbol exp(i(k - p(k))) of winding 1 (carries the shift index)."""
import numpy as np, itertools, scipy.sparse as sp
from r61_witness_tmatrix import wrap, sstep, chi1d, f, make_disp

def build(L, Nf, modes, analytic=False, lam=3.0):
    """sparse H (free + interaction) and diagonal Q, P on the Nf-fermion space over 'modes' (list of k-index tuples)"""
    kk = 2*np.pi*np.arange(L)/L
    M = len(modes); idx = {m: i for i, m in enumerate(modes)}
    kvec = np.array([[wrap(kk[a]), wrap(kk[b])] for a, b in modes])
    disp = make_disp('NN')
    eps = disp(kvec[:, 0], kvec[:, 1])
    chi = np.ones(M) if analytic else chi1d(kvec[:, 0])*chi1d(kvec[:, 1])
    basis = list(itertools.combinations(range(M), Nf)); bidx = {b: i for i, b in enumerate(basis)}
    D = len(basis)
    # pair list per total K index
    pairs = {}
    for i in range(M):
        for j in range(i+1, M):
            K = ((modes[i][0]+modes[j][0]) % L, (modes[i][1]+modes[j][1]) % L)
            gij = chi[i]*chi[j]*(f(*kvec[i]) - f(*kvec[j]))   # amplitude for a_j a_i ordering (i<j)
            if abs(gij) > 0:
                pairs.setdefault(K, []).append((i, j, gij))
    rows, cols, vals = [], [], []
    for b, s in bidx.items():
        occ = set(b)
        for K, plist in pairs.items():
            # A_K |b>: remove (i,j) with sign; then A_K^dag: add (i2,j2)
            for (i, j, gij) in plist:
                if i in occ and j in occ:
                    lst = sorted(b)
                    # a_j a_i on |lst>, i<j: sign from positions
                    pi_ = lst.index(i); sgn = (-1)**pi_; lst.remove(i)
                    pj = lst.index(j); sgn *= (-1)**pj; lst.remove(j)
                    for (i2, j2, g2) in plist:
                        if i2 in lst or j2 in lst:
                            continue
                        l2 = sorted(lst + [j2]); s2 = (-1)**l2.index(j2)
                        l3 = sorted(l2 + [i2]); s2 *= (-1)**l3.index(i2)
                        rows.append(bidx[tuple(l3)]); cols.append(s)
                        vals.append(lam/(L*L)*np.conj(g2)*gij*sgn*s2)
    Hint = sp.csr_matrix((vals, (rows, cols)), shape=(D, D))
    H0 = sp.diags([sum(eps[list(b)]) for b in basis])
    Qx = np.array([sum(kvec[list(b), 0]) for b in basis]); Qy = np.array([sum(kvec[list(b), 1]) for b in basis])
    return H0 + Hint, Qx, Qy, kvec, basis

def p_smooth(t):
    t = wrap(t); s = np.sign(t); u = np.abs(t)
    w = sstep((0.9*np.pi - u)/(0.41*np.pi))
    return s*(u*w + (np.pi - u)*(1 - w))

if __name__ == "__main__":
    L = 16
    allmodes = [(a, b) for a in range(L) for b in range(L)]
    # N = 2, full mode set
    H, Qx, Qy, kvec, basis = build(L, 2, allmodes)
    herm = abs(H - H.getH()).max()
    C = H.tocoo(); off = C.row != C.col
    dQ = np.max(np.abs(np.stack([Qx[C.row[off]] - Qx[C.col[off]], Qy[C.row[off]] - Qy[C.col[off]]])), axis=0)
    print("W, N=2, L=16, all 256 modes: dim=%d, nnz offdiag=%d, |H-H^dag|max=%.1e, max|Q_out-Q_in| over nonzero offdiag=%.2e"
          % (H.shape[0], off.sum(), herm, dQ.max() if off.any() else 0))
    # N = 3 on box modes + 12 edge modes (spectators)
    box = [m for m in allmodes if chi1d(np.array([wrap(2*np.pi*m[0]/L)]))[0]*chi1d(np.array([wrap(2*np.pi*m[1]/L)]))[0] > 0]
    edge = [m for m in allmodes if m not in box][:0] + [(8, j) for j in range(0, 16, 2)] + [(j, 8) for j in (1, 5, 11, 13)]
    modes = box + edge
    H3, Qx3, Qy3, kv3, b3 = build(L, 3, modes)
    C = H3.tocoo(); off = C.row != C.col
    dQ3 = np.max(np.abs(np.stack([Qx3[C.row[off]] - Qx3[C.col[off]], Qy3[C.row[off]] - Qy3[C.col[off]]])), axis=0)
    comm = H3 @ sp.diags(Qx3) - sp.diags(Qx3) @ H3
    print("W, N=3, %d box + %d edge modes: dim=%d, nnz offdiag=%d, max|dQ| on nonzero=%.2e, ||[H,Qx]||_max=%.2e"
          % (len(box), len(edge), H3.shape[0], off.sum(), dQ3.max(), abs(comm).max()))
    Px = np.array([sum(p_smooth(kv3[list(b), 0])) for b in b3])
    commP = H3 @ sp.diags(Px) - sp.diags(Px) @ H3
    print("W, N=3: ||[H,P_x]||_max with P = sum p(k) n_k (p smooth periodic, = qhat on box) = %.2e" % abs(commP).max())
    # analytic comparator on L=8 full
    L8 = 8; modes8 = [(a, b) for a in range(L8) for b in range(L8)]
    Ha, Qxa, Qya, kva, ba = build(L8, 3, modes8, analytic=True)
    comm = Ha @ sp.diags(Qxa) - sp.diags(Qxa) @ Ha
    comm2 = Ha @ sp.diags(Qya) - sp.diags(Qya) @ Ha
    print("analytic comparator, N=3, L=8: dim=%d, ||[H,Qx]||_max=%.3e, ||[H,Qy]||_max=%.3e (nonzero = umklapp)" % (Ha.shape[0], abs(comm).max(), abs(comm2).max()))
    # time evolution: <Q> drift in comparator vs witness (N=3, L=8 witness too)
    import scipy.sparse.linalg as sla
    Hw8, Qxw8, Qyw8, kvw8, bw8 = build(L8, 3, modes8, analytic=False)
    rng = np.random.default_rng(1)
    for name, HH, QQ in [("witness", Hw8, Qxw8), ("analytic", Ha, Qxa)]:
        # start: 3 fermions in a Q-eigenstate with high momenta (near zone edge in x)
        psi = np.zeros(HH.shape[0], complex)
        target = [i for i, b in enumerate(bw8) if True]
        i0 = int(np.argmax(QQ))   # max Q_x configuration
        psi[i0] = 1.0
        Q0 = QQ[i0]
        out = []
        for t in [0.5, 1.0, 2.0, 4.0]:
            ph = sla.expm_multiply(-1j*t*HH, psi)
            out.append(np.real(np.vdot(ph, QQ*ph)) - Q0)
        print("  %s: start config Q_x=%.4f; <Q_x>(t)-Q_x(0) at t=0.5,1,2,4: %s" % (name, Q0, np.array2string(np.array(out), precision=4)))
    # (3) real-space decay of chi (1D) and of p (1D)
    Nn = 1 << 14
    t = 2*np.pi*np.arange(Nn)/Nn
    ch = np.fft.fft(chi1d(t))/Nn
    pc = np.fft.fft(p_smooth(t))/Nn
    print("1D Fourier coefficients |c(n)| (real-space kernel at distance n):")
    for n in [1, 4, 8, 16, 32, 64, 128, 256, 512]:
        print("  n=%4d  |chi^(n)|=%.3e  |p^(n)|=%.3e  n^-6=%.1e" % (n, abs(ch[n]), abs(pc[n]), n**-6.0))
    ns = np.array([32, 64, 128, 256]); lc = np.log(np.abs(ch[ns]))
    print("  fit log|chi^(n)| = A - c n^beta over n in 32..256: ", end="")
    best = min(((np.sum((lc - np.polyval(np.polyfit(ns**b, lc, 1), ns**b))**2), b) for b in np.linspace(0.2, 1.0, 81)))
    print("beta ~ %.2f (sub-exponential; exp-decay would be beta=1 with zero residual)" % best[1])
    # (4) winding of exp(i(k - p(k)))
    ph = np.unwrap(t - p_smooth(t))
    print("winding of V's one-body symbol exp(i(k-p(k))) over the zone: %.6f ; of exp(i p(k)): %.6f" %
          ((ph[-1] - ph[0] + (t[1]-t[0]))/(2*np.pi), (np.unwrap(p_smooth(t))[-1] - np.unwrap(p_smooth(t))[0])/(2*np.pi)))
    print("max |p(k) - k| on chi support (|k|<0.49pi): %.2e" % np.max(np.abs(p_smooth(t[np.abs(wrap(t)) < 0.49*np.pi]) - wrap(t[np.abs(wrap(t)) < 0.49*np.pi]))))
