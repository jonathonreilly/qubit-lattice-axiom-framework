"""T65 Test 3: the non-local exit (S5). X(q) = I - P_TT(qhat) on Sym^2(R^3): TT massless, all
other polarisations massive. How much real-space range does that need?"""
import numpy as np
N = 48
rng = np.random.default_rng(0)
# orthonormal basis of Sym^2 (6-dim)
B = []
for i in range(3):
    M = np.zeros((3, 3)); M[i, i] = 1; B.append(M)
for i, j in [(0,1),(0,2),(1,2)]:
    M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1 / np.sqrt(2); B.append(M)
B = np.array(B)
def PTT(qh):
    P = np.eye(3) - np.outer(qh, qh)
    out = np.zeros((6, 6))
    for b in range(6):
        h = B[b]
        r = P @ h @ P - 0.5 * P * np.trace(P @ h)
        out[:, b] = [np.sum(B[a] * r) for a in range(6)]
    return out
def X_of(p):
    n = np.linalg.norm(p)
    if n < 1e-12: return None
    return np.eye(6) - PTT(p / n)
# X on the torus grid with lattice momentum p_i = sin(q_i)
qs = 2 * np.pi * np.fft.fftfreq(N)
Xq = np.zeros((N, N, N, 6, 6))
avg = np.zeros((6, 6)); cnt = 0
# vectorised P_TT
QX, QY, QZ = np.meshgrid(qs, qs, qs, indexing='ij')
p = np.stack([np.sin(QX), np.sin(QY), np.sin(QZ)], -1)
nrm = np.linalg.norm(p, axis=-1)
nrm[0, 0, 0] = 1.0
qh = p / nrm[..., None]
P = np.eye(3) - qh[..., :, None] * qh[..., None, :]                    # (...,3,3)
Bt = B                                                                  # (6,3,3)
PB = np.einsum('...ij,bjk,...kl->...bil', P, Bt, P) - 0.5 * P[..., None, :, :] * np.einsum('...ij,bji->...b', P, Bt)[..., None, None]
PTTm = np.einsum('aik,...bik->...ab', Bt, PB)                          # (...,6,6): <B_a|P_TT B_b>
Xq = np.eye(6) - PTTm
# value at q=0: angular average of the limit (any choice is measure zero; use trace-average)
Xq[0, 0, 0] = np.mean(Xq.reshape(-1, 6, 6)[1:], axis=0)
K = np.real(np.fft.ifftn(Xq, axes=(0, 1, 2)))                          # K[r] 6x6, r on torus
r_idx = np.fft.fftfreq(N, 1.0 / N).astype(int)
RX, RY, RZ = np.meshgrid(r_idx, r_idx, r_idx, indexing='ij')
R2 = RX**2 + RY**2 + RZ**2
# tail decay of K(r): shell-RMS of ||K||_F vs |r|
Kf = np.sqrt(np.sum(K**2, axis=(-1, -2)))
rs = np.sqrt(R2)
shells = np.arange(3, 22)
rms = [np.sqrt(np.mean(Kf[(rs >= s) & (rs < s + 1)]**2)) for s in shells]
a = -np.polyfit(np.log(shells + 0.5), np.log(rms), 1)[0]
print(f"tail: shell-RMS ||K(r)||_F ~ r^-a with a = {a:.2f} (fit r = 3..21)")
def symbol(qvec, Rc):
    sel = R2 <= Rc * Rc
    ph = np.cos(qvec[0] * RX[sel] + qvec[1] * RY[sel] + qvec[2] * RZ[sel])
    return np.tensordot(ph, K[sel], axes=(0, 0))
def exact(qvec):
    pv = np.sin(np.array(qvec))
    return X_of(pv), pv / np.linalg.norm(pv)
def subspace_values(Xs, qh_):
    Pt = PTT(qh_); w, U = np.linalg.eigh(Pt); TT = U[:, w > 0.5]; OT = U[:, w < 0.5]
    lam_tt = np.max(np.linalg.eigvalsh(TT.T @ Xs @ TT))
    lam_p = np.min(np.linalg.eigvalsh(OT.T @ Xs @ OT))
    return lam_tt, lam_p
dirs = {'(100)': np.array([1., 0, 0]), '(110)': np.array([1., 1, 0]) / 2**.5, '(111)': np.array([1., 1, 1]) / 3**.5}
print("\nrho = lambda_TT / lambda_partner of the range-R truncation (ideal 0):")
print("  |q|   dir    " + "  ".join(f"R={R:>2d}" for R in [1, 2, 3, 4, 6, 8, 12, 16, 22]))
res = {}
for qn in [0.4, 0.2, 0.1]:
    for dn, d in dirs.items():
        row = []
        for Rc in [1, 2, 3, 4, 6, 8, 12, 16, 22]:
            Xs = symbol(qn * d, Rc)
            lt, lp = subspace_values(Xs, d)      # qhat for lattice p differs by O(q^2); use d
            row.append(lt / lp if lp > 0 else np.inf)
        res[(qn, dn)] = row
        print(f"  {qn:.1f}  {dn}  " + "  ".join(f"{v:5.2f}" for v in row))
# smallest R with rho <= 0.1, per |q| (worst direction), and product R*|q|
print("\nsmallest tested R with rho<=0.1 in all three directions:")
Rlist = [1, 2, 3, 4, 6, 8, 12, 16, 22]
for qn in [0.4, 0.2, 0.1]:
    ok = [Rc for j, Rc in enumerate(Rlist) if all(res[(qn, dn)][j] <= 0.1 for dn in dirs)]
    print(f"  |q|={qn}: R_min = {ok[0] if ok else '> 22'}   R*|q| = {ok[0]*qn if ok else float('nan'):.2f}")
# finer scan of rho(R) at |q|=0.2 (100)
print("\nrho vs R at |q|=0.2 along (100), R = 1..24:")
d = dirs['(100)']
print("  " + " ".join(f"{Rc}:{(lambda t: t[0]/t[1])(subspace_values(symbol(0.2*d, Rc), d)):.2f}" for Rc in range(1, 24)))
# sanity: untruncated symbol at a grid momentum equals X(q)
iq = (3, 2, 1)
qv = np.array([qs[i] for i in iq])
Xt = symbol(qv, 100)
Xe, _ = exact(qv)
print(f"\nsanity: |symbol(all r) - X(q)| at grid q = {np.abs(Xt - Xe).max():.2e}")
