"""Functions of s4_adversarial_fit.py (verbatim copy of its definitions) for reuse by s4b."""

import itertools
import sys
import numpy as np
from scipy.optimize import least_squares
from w3lib import Checker, PAULI, wilson_weyl_map, smooth_grid, w3_from_fields

rng = np.random.default_rng(7)

def V2_on_grid(N, offset=0.0):
    k = 2 * np.pi * (np.arange(N) + offset) / N
    K1, K2, K3 = np.meshgrid(k, k, k, indexing='ij')
    U, _ = wilson_weyl_map(2.0)(K1, K2, K3)
    return np.stack([K1.ravel(), K2.ravel(), K3.ravel()], 1), U.reshape(-1, 2, 2)

def hops(r):
    return np.array(list(itertools.product(range(-r, r + 1), repeat=3)))

def coeffs_to_A(p, nh):
    z = p[:nh * 4] + 1j * p[nh * 4:]
    return z.reshape(nh, 2, 2)

def build(r, Nf, Nu):
    H = hops(r)
    nh = len(H)
    kf, Vf = V2_on_grid(Nf, 0.5)
    ku = 2 * np.pi * np.array(list(itertools.product(range(Nu), repeat=3))) / Nu
    Cf = np.exp(1j * kf @ H.T)   # (Kf, nh)
    Cu = np.exp(1j * ku @ H.T)
    return H, nh, Cf, Vf, Cu

def residual_and_jac(p, nh, Cf, Vf, Cu, w):
    A = coeffs_to_A(p, nh)
    Uf = np.einsum('kn,nij->kij', Cf, A)
    Uu = np.einsum('kn,nij->kij', Cu, A)
    Rf = (Uf - Vf).reshape(len(Cf), 4)
    Ru = (Uu @ np.conj(np.swapaxes(Uu, 1, 2)) - np.eye(2)).reshape(len(Cu), 4)
    res = np.concatenate([Rf.real.ravel(), Rf.imag.ravel(), w * Ru.real.ravel(), w * Ru.imag.ravel()]) / np.sqrt(len(Cf))
    # Jacobian. Params: Re A[n,i,j] then Im A[n,i,j].
    Kf, Ku = len(Cf), len(Cu)
    Jf = np.zeros((Kf, 2, 2, nh, 2, 2), complex)
    for i in range(2):
        for j in range(2):
            Jf[:, i, j, :, i, j] = Cf
    Jf = Jf.reshape(Kf * 4, nh * 4)
    Jf = np.concatenate([Jf, 1j * Jf], 1)
    Ud = np.conj(np.swapaxes(Uu, 1, 2))
    Ju = np.zeros((Ku, 2, 2, nh, 2, 2, 2), complex)
    for i in range(2):
        for j in range(2):
            for t, alpha in enumerate((1.0, 1j)):
                c = alpha * Cu  # (Ku, nh)
                # (E_ij U^dag)_{ab} = delta_ai Ud_{jb};  (U E_ji)_{ab} = U_{aj} delta_bi
                Ju[:, i, :, :, i, j, t] += c[:, None, :] * Ud[:, j, :][:, :, None]
                Ju[:, :, i, :, i, j, t] += np.conj(c)[:, None, :] * Uu[:, :, j][:, :, None]
    Ju = Ju.reshape(Ku * 4, nh, 4, 2)
    Ju = np.concatenate([Ju[..., 0].reshape(Ku * 4, nh * 4), Ju[..., 1].reshape(Ku * 4, nh * 4)], 1)
    J = np.concatenate([Jf.real, Jf.imag, w * Ju.real, w * Ju.imag], 0) / np.sqrt(len(Cf))
    return res, J

def evaluate(p, H, nh, r):
    A = coeffs_to_A(p, nh)
    # unitarity error at random momenta
    K = rng.uniform(0, 2 * np.pi, (3000, 3))
    U = np.einsum('kn,nij->kij', np.exp(1j * K @ H.T), A)
    uerr = np.abs(U @ np.conj(np.swapaxes(U, 1, 2)) - np.eye(2)).max()
    # sup distance to V_2 on a fine offset grid
    kq, Vq = V2_on_grid(40, 0.37)
    Uq = np.einsum('kn,nij->kij', np.exp(1j * kq @ H.T), A)
    sup = np.linalg.norm(Uq - Vq, ord=2, axis=(1, 2)).max()
    mind = np.abs(np.linalg.det(Uq)).min()
    # W3 via GL formula with matrix inverse, grid N=40 and 56 for convergence
    ws = []
    for N in (40, 56):
        k = 2 * np.pi * (np.arange(N) + 0.5) / N
        KK = np.array(list(itertools.product(k, k, k)))
        C = np.exp(1j * KK @ H.T)
        Ug = np.einsum('kn,nij->kij', C, A).reshape(N, N, N, 2, 2)
        dU = [np.einsum('kn,nij->kij', C * (1j * H[:, b])[None, :], A).reshape(N, N, N, 2, 2) for b in range(3)]
        ws.append(w3_from_fields(Ug, dU, unitary=False))
    return uerr, sup, mind, ws

