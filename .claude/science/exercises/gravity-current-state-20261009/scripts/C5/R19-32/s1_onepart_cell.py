"""R19-32 s1 (pre-registered 07:22Z): CCR one-particle covariant GB on full cubic tori (probe (c),(d) at one-particle level).
For every nonzero lattice momentum of the L^3 torus (L = 2,3,4), forward-difference de Donder constraint:
 (1) nullness N_nm = sum_A c_nA conj(c_mA) eta_A = 0 (the 4 lowering parts are mutually null at CCR);
 (2) V1(k) = {e : sum_A c_nA eta_A e_A = 0}: dim, Krein inertia (expect 6, (2,0,4)); quotient dim 2, positive;
 (3) quotient = TT: projection of radical-free part onto spatial TT w.r.t. the lattice direction;
 (4) slice k || z: c_nA vanishes outside the sectors (TT unconstrained; vecx, vecy, scal closed);
 (5) static T^00 energy  -T.G.T/(2 qhat^2)  (attractive iff T.G.T > 0) and per-eigenfield split.
"""
import numpy as np, itertools, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from cov import *
print("eigenfields:", list(zip(NAMES, ETA.astype(int))))
for L in [2, 3, 4]:
    worst_null = 0; bad = 0; nk = 0; worst_tt = 0
    for j in itertools.product(range(L), repeat=3):
        if j == (0, 0, 0): continue
        k = 2*np.pi*np.array(j)/L
        c, w = constraint_coeffs(k)
        N = (c*ETA)@c.conj().T
        worst_null = max(worst_null, np.abs(N).max()/w**2)
        M = c*ETA                                     # condition M e = 0
        u, s, vh = np.linalg.svd(M); r = int((s > 1e-10*w).sum()); V = vh[r:].conj().T
        Gr = V.conj().T@np.diag(ETA)@V; ev = np.linalg.eigvalsh((Gr + Gr.conj().T)/2)
        inert = (int((ev > 1e-9).sum()), int((ev < -1e-9).sum()), int((abs(ev) <= 1e-9).sum()))
        nk += 1
        if V.shape[1] != 6 or inert != (2, 0, 4): bad += 1
        # TT check: positive eigenvectors of Gram, mapped to components, must be spatial-TT w.r.t. Re-direction n
        wv, U = np.linalg.eigh((Gr + Gr.conj().T)/2)
        pos = V@U[:, wv > 1e-9]                       # eigenfield coords of positive directions
        q = np.abs(dD(k)); n = np.sign(np.sin(k/2))*q  # real lattice direction (forward-diff modulus)
        n = n/np.linalg.norm(n)
        for col in pos.T:
            h = sum(R[I, :]@col*B[I] for I in range(10))   # component tensor
            # remove any null (gauge) admixture: compare only the part orthogonal to radical in Krein sense is not unique;
            # report the TT-violation of the spatial block after projecting out radical directions in Krein metric
        # radical-projected TT test: physical quotient basis = spatial TT tensors (eigenfield coords); check they lie in V1
        a = np.array([1., 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1., 0])
        e1 = a - (a@n)*n; e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
        for Msp in [(np.outer(e1, e1) - np.outer(e2, e2))/np.sqrt(2), (np.outer(e1, e2) + np.outer(e2, e1))/np.sqrt(2)]:
            E = np.zeros((4, 4)); E[1:, 1:] = Msp; e = R.T@comp(E)
            # constraint with complex D: TT w.r.t. |D|-direction up to phases; use exact transverse to D:
            worst_tt = max(worst_tt, 0)
    print(f"L={L}: {nk} nonzero momenta; max |N_nm|/w^2 = {worst_null:.1e}; momenta with dim V1 != 6 or inertia != (2,0,4): {bad}")
# exact-transverse TT (complex D): polarisations e with sum_j D_j* E_jn ... check at generic k that quotient is 2 and positive
print("\n(3) TT content at generic k: positive quotient directions vs complex-transverse spatial tensors")
for kv in [[0.3, 0.0, 0.0], [0.2, 0.1, 0.05], [1.0, 2.0, 0.5], [np.pi, np.pi, 0.7]]:
    k = np.array(kv); c, w = constraint_coeffs(k); M = c*ETA
    u, s, vh = np.linalg.svd(M); r = int((s > 1e-10*w).sum()); V = vh[r:].conj().T
    Gr = V.conj().T@np.diag(ETA)@V; wv, U = np.linalg.eigh((Gr + Gr.conj().T)/2)
    rad = V@U[:, np.abs(wv) <= 1e-9]; pos = V@U[:, wv > 1e-9]
    # spatial tensors E with E_0n = 0, tr E_ss = 0 and sum_j conj?(D_j) E_jn = 0  -> satisfy constraint?
    D = dD(k)
    cand = []
    for I in range(10):
        pass
    # build space of spatial symmetric traceless tensors S with D^T S = 0 (complex): solve linear system on 6 spatial comps
    sp = [(i, j) for i in range(1, 4) for j in range(i, 4)]
    A = []
    for n_ in range(1, 4):
        row = []
        for (i, j) in sp:
            E = np.zeros((4, 4)); E[i, j] = E[j, i] = 1.; row.append(D[i-1]*E[i, n_] if True else 0)
        A.append([sum(D[m-1]*(1 if (m, n_) in [(i, j), (j, i)] else 0) for m in range(1, 4)) for (i, j) in sp])
    A.append([1. if i == j else 0. for (i, j) in sp])
    A = np.array(A, complex); uu, ss, vv = np.linalg.svd(A); TTsp = vv[int((ss > 1e-10).sum()):].conj().T
    TTe = []
    for col in TTsp.T:
        E = np.zeros((4, 4), complex)
        for (i, j), x in zip(sp, col): E[i, j] = E[j, i] = x
        TTe.append(R.T@np.array([np.sum(E*b) for b in B]))
    TTe = np.array(TTe).T
    inV = np.abs(M@TTe).max()
    gram = TTe.conj().T@np.diag(ETA)@TTe
    print(f"  k={np.round(kv,3)}: dim V1={V.shape[1]}, radical {rad.shape[1]}, positive {pos.shape[1]}; complex-transverse traceless spatial tensors: {TTe.shape[1]}, in V1: {inV:.1e}, Gram eig {np.round(np.linalg.eigvalsh(gram),4)}")
print("\n(4) slice k || z: coefficient support by sector")
for kz in [np.pi/3, np.pi/2, 2*np.pi/3, np.pi, 0.1]:
    c, w = constraint_coeffs([0, 0, kz])
    sup = {s: np.round(np.abs(c[:, idx]).max(), 4) for s, idx in SECTORS.items()}
    rows = {s: [n for n in range(4) if np.abs(c[n, idx]).max() > 1e-12] for s, idx in SECTORS.items()}
    print(f"  kz={kz:.4f} w={w:.4f}: max|c| per sector {sup}; constraint rows touching sector {rows}")
    for s, idx in SECTORS.items():
        if s == 'TT': continue
        rr = rows[s]; cs = c[np.ix_(rr, idx)]
        print(f"     {s}: rows {rr}, fields {[NAMES[i] for i in idx]} eta {ETA[idx].astype(int)}, c/w =\n{np.round(cs/w, 4)}")
E00 = np.zeros((4, 4)); E00[0, 0] = 1; t = comp(E00)
print(f"\n(5) static T^00: T.G.T = {t@G@t:.4f} (>0: energy -T.G.T/(2 qhat^2) < 0, attractive 1/r); per eigenfield eta_A (R^T t)_A^2 =",
      dict(zip(NAMES, np.round(ETA*(R.T@t)**2, 4))))
