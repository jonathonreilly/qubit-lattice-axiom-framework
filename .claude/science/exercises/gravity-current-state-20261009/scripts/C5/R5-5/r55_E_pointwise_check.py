"""R5-5 (E): per-frame (pointwise) check behind Lemma AE, on R4-1's saved data: for each frame, the absolute deviation
|B_g phi - Bbar phi| / l (R4-1 units a=1) over l = 6..19 (24): does any frame stay near zero at every l?  (finite-l illustration only;
Lemma AE is an asymptotic a.e. statement)"""
import numpy as np, sys
R41 = sys.argv[1]
for fn in ("r41_B_M96_seed7_eta1.0.npz", "r41_B_M96_seed23_eta0.6.npz"):
    d = np.load(f"{R41}/{fn}", allow_pickle=False); S = d['S']; I = d['I']; ells = d['ells']; C = d['C']
    NF, nl, M = S.shape; mv = np.arange(1, M+1).astype(float); Cm = C[1:M+1]
    for sh in ([1, 2, 3, 4], [1, 2, 4, 7]):
        g = np.zeros(M)
        for i, mi in enumerate(sh): g[mi-1] = 1.0/np.prod([mi-mj for j, mj in enumerate(sh) if j != i])
        g = -g/((np.pi/16)*np.sum(g*mv**2*np.log(mv))); f = g/np.where(Cm > 0, Cm, np.inf)
        big = ells >= 6
        A = np.array([np.abs(S[:, j, :] @ f - np.sum(g*I[j]))/ells[j] for j in range(nl)]).T[:, big]   # frames x l
        mx = A.max(1)
        print(f"{fn} kernel {sh}: l = {ells[big].tolist()};  per-frame max_l |dev|/l: min over frames {mx.min():.3e}, "
              f"median {np.median(mx):.3e}, max {mx.max():.3e};  frames with max_l |dev|/l < 1e-2 * median: {(mx < 1e-2*np.median(mx)).sum()}/{NF}")
