"""R19-32 s2 (pre-registered 07:33Z): operator checks of the many-body builder + probe (a) (Lemma K for the covariant model).
 (i) H Krein-self-adjoint and Hermitian; (ii) CCR-consistency of chi^+ vs D below the top: <low| [H, D(k)] + w D(k) |low>;
 (iii) Lemma-K formulas (proved in report):
   [D_n(k), D_m(k')^K] = -d (u_k u_k' - v_k v_k')/L sum_{x,A} chat_nA conj(chat_mA) eta_A e^{-i(k-k')(x+o_A)} Ptop_{A,x}
   [D_n(k), D_m(k')]   = -d (u_k v_k' - v_k u_k')/L sum_{x,A} chat_nA chat_mA eta_A e^{-i(k+k')(x+o_A)} Ptop_{A,x}
   (identity parts cancel by nullness / by w_k = w_{-k}); check residual of these identities.
"""
import numpy as np, scipy.sparse as sp, sys, itertools
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from mb import *
for (sec, L, tw, d, nu) in [('vecx', 2, -1, 3, 1.0), ('vecx', 3, -1, 3, 1.0), ('vecx', 3, 1, 3, 1.0), ('scal', 2, -1, 2, 1.0), ('scal', 1, -1, 3, 2.0)]:
    S = Sector(sec, L, d, nu, tw)
    H = S.H; Et = sp.diags(S.eta)
    sa = abs(Et@H.conj().T@Et - H).max(); herm = abs(H.conj().T - H).max()
    Dl = [(r, j) for j in range(L) if S.ws[j] > 1e-12 for r in range(len(S.rows))]
    resK = 0; resC = 0; normsC = []; normsK = []
    Ptop = {}
    for A in range(S.nf):
        P = np.zeros((d, d)); P[d-1, d-1] = 1
        for x in range(L): Ptop[(A, x)] = S.emb(P, S.slot(A, x))
    uv = {}
    for j in range(L):
        w = S.ws[j]
        if w < 1e-12: continue
        uv[j] = (0.5*(np.sqrt(w/nu) + np.sqrt(nu/w)), 0.5*(np.sqrt(w/nu) - np.sqrt(nu/w)))
    for (n, j), (m, jp) in itertools.product(Dl, Dl):
        Dn = S.D(n, j); Dm = S.D(m, jp); k = S.ks[j]; kp = S.ks[jp]
        (u, v), (up, vp) = uv[j], uv[jp]
        C1 = Dn@S.Kad(Dm) - S.Kad(Dm)@Dn
        F1 = sum(S.chat[n, A]*np.conj(S.chat[m, A])*S.etas[A]*np.exp(-1j*(k - kp)*(x + S.offs[A]))*Ptop[(A, x)] for A in range(S.nf) for x in range(L))
        F1 = -d*(u*up - v*vp)/L*F1
        resK = max(resK, abs(C1 - F1).max()); normsK.append(abs(C1).max())
        C2 = Dn@Dm - Dm@Dn
        F2 = sum(S.chat[n, A]*S.chat[m, A]*S.etas[A]*np.exp(-1j*(k + kp)*(x + S.offs[A]))*Ptop[(A, x)] for A in range(S.nf) for x in range(L))
        F2 = -d*(u*vp - v*up)/L*F2
        resC = max(resC, abs(C2 - F2).max()); normsC.append(abs(C2).max())
    # chi^+ consistency: below-top block, [H, D] + w D restricted to states with all occupations <= d-3
    occ = np.zeros(S.dim, int); idx = np.arange(S.dim)
    for s in range(S.ns):
        occ = np.maximum(occ, (idx // S.d**(S.ns - s - 1)) % S.d)
    low = np.where(occ <= d - 3)[0] if d >= 3 else np.array([], int)
    fr = 0
    for (n, j) in Dl:
        Dn = S.D(n, j); X = (H@Dn - Dn@H + S.ws[j]*Dn)
        if len(low): fr = max(fr, abs(X[np.ix_(low, low)]).max())
    print(f"{sec} L={L} twist={tw} d={d} nu={nu}: dim {S.dim}; H Krein-s.a. {sa:.1e}, Hermitian {herm:.1e}; ws={np.round(S.ws,4)}")
    print(f"   Lemma-K identity residuals: [D,D^K] {resK:.1e} (max|[D,D^K]| {max(normsK):.3f}), [D,D] {resC:.1e} (max|[D,D]| {max(normsC):.3f});"
          f" frequency |<low|[H,D]+wD|low>| = {fr:.1e}")
