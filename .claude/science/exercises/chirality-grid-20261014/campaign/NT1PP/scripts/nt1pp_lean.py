"""NT-1'' memory-lean drop-in for nt1p_lib.dq_dA (same formula, no (N, n^2) Phi array). Import AFTER nt1p_lib and call patch().
R_raw[p, x, l]: dS_aa = 2 Re sum_{i+, j-} C_ij Vp_ai conj(Vm_aj) X^l_ij  ->  2 Re sum_i Vp_ai (conj(Vm) Y_l^T)_ai, Y_l = C o X^l."""
import numpy as np
import nt1p_lib
from nt1p_lib import s3


def dq_dA_lean(S, th, w, V):
    P, N = w.shape; n = N // 2
    assert np.all((w > 0).sum(1) == n)
    Vp = V[:, :, n:]; Vm = V[:, :, :n]; wp = w[:, n:]; wm = w[:, :n]
    C = 2.0 / (wp[:, :, None] - wm[:, None, :])
    e = np.exp(1j * th)
    Vp5 = Vp.reshape(P, S.ns, 2, n); Vm5 = Vm.reshape(P, S.ns, 2, n)
    gF = s3[None] @ S.Fb; gB = s3[None] @ S.Bb
    cF = 1j * e[:, :, None, None] * gF[None]; cB = -1j * np.conj(e)[:, :, None, None] * gB[None]
    Rr = np.zeros((P, N, S.nl)); LC = 16; cVm = np.conj(Vm)
    for l0 in range(0, S.nl, LC):
        sl = slice(l0, min(l0 + LC, S.nl)); fr = S.frm[sl]; to = S.to[sl]
        X = np.einsum('plai,plab,plbj->plij', np.conj(Vp5[:, fr]), cF[:, sl], Vm5[:, to], optimize=True)
        X += np.einsum('plai,plab,plbj->plij', np.conj(Vp5[:, to]), cB[:, sl], Vm5[:, fr], optimize=True)
        Y = X * C[:, None]                                                   # (P, l, n, n)
        Z = cVm[:, None] @ np.swapaxes(Y, 2, 3)                              # (P, l, N, n): sum_j conj(Vm_aj) Y_ij
        Rr[:, :, sl] = np.swapaxes(2 * np.real(np.einsum('pai,plai->pla', Vp, Z)), 1, 2); del X, Y, Z
    return -0.5 * (Rr[:, 0::2] + Rr[:, 1::2])


def patch():
    nt1p_lib.dq_dA = dq_dA_lean
