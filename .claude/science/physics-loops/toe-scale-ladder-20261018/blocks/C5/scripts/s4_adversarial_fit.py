"""C5 s4: adversarial test of Theorem K and its distance corollary.

Corollary D (NOTE.md): if U is a finite-range unitary walk and V any continuous map T^3 -> U(2) with
W3[V] != 0, then sup_k ||U(k) - V(k)|| >= 1 (operator norm). Otherwise (1-t)U + tV is invertible
for all t and W3[U] = W3[V] != 0, contradicting Theorem K.

Test: target V_2 (analytic, O-covariant, W3 = -1 in our convention). Unconstrained Laurent
coefficients on stencil {-r..r}^3 (no product structure assumed, no symmetry imposed), least squares
fit to V_2 plus a unitarity penalty w * (U U^dag - 1) on an exact (4r+1)^3 grid (U U^dag - 1 has
degree <= 2r per axis, so vanishing there means vanishing identically). Continuation in w.
Prediction stated before running: as the unitarity residual -> 0, sup||U - V_2|| stays >= 1 and
W3 (GL formula, U^{-1} by matrix inversion) of the fitted invertible U is -1 only while the
unitarity residual is not small; the w -> infinity endpoints have W3 = 0.
Also a control: the plain Fourier truncation of V_2 is a Laurent polynomial INVERTIBLE matrix
(inverse not finite range) and carries W3 = -1, showing that Theorem K needs a polynomial inverse.
"""
import itertools
import sys
import numpy as np
from scipy.optimize import least_squares
from w3lib import Checker, PAULI, wilson_weyl_map, smooth_grid, w3_from_fields

ck = Checker()
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

results = []
for r, Nf, Nu, starts in ((1, 10, 5, 3), (2, 8, 9, 2)):
    H, nh, Cf, Vf, Cu = build(r, Nf, Nu)
    # Fourier truncation of V_2 (projection onto the stencil using a fine grid)
    kq, Vq = V2_on_grid(32, 0.0)
    Ftr = np.einsum('kn,kij->nij', np.conj(np.exp(1j * kq @ H.T)), Vq) / len(kq)
    p_tr = np.concatenate([Ftr.real.ravel(), Ftr.imag.ravel()])
    uerr, sup, mind, ws = evaluate(p_tr, H, nh, r)
    print(f'r={r} Fourier truncation of V_2: unitarity err {uerr:.3f}, sup||U-V2|| {sup:.3f}, min|det| {mind:.3f}, '
          f'W3(GL; N=40,56) = {ws[0].real:+.6f}, {ws[1].real:+.6f}')
    ck.check(f'control r={r}: the truncated (invertible, NOT unitary) Laurent matrix carries W3 = -1 (GL formula)',
             mind > 1e-3 and abs(ws[1] + 1) < 1e-3 and abs(ws[1] - ws[0]) < 1e-3)
    inits = [('truncation', p_tr)] + [(f'random{s}', rng.normal(scale=0.2, size=2 * nh * 4)) for s in range(starts)]
    for lab, p0 in inits:
        p = p0.copy()
        for w in (0.3, 3.0, 30.0, 300.0, 3000.0):
            sol = least_squares(lambda q: residual_and_jac(q, nh, Cf, Vf, Cu, w)[0], p,
                                jac=lambda q: residual_and_jac(q, nh, Cf, Vf, Cu, w)[1],
                                method='trf', max_nfev=300, xtol=1e-12, ftol=1e-12, gtol=1e-12)
            p = sol.x
            uerr, sup, mind, ws = evaluate(p, H, nh, r)
            l2 = np.sqrt(np.mean(np.abs(np.einsum('kn,nij->kij', Cf, coeffs_to_A(p, nh)) - Vf) ** 2) * 4)
            print(f'  r={r} start={lab:10s} w={w:7.1f}: unit.err {uerr:.2e}  L2fit {l2:.3f}  sup||U-V2|| {sup:.3f}  '
                  f'min|det| {mind:.2e}  W3(N=40,56) {ws[0].real:+.4f} {ws[1].real:+.4f}', flush=True)
            results.append((r, lab, w, uerr, sup, mind, ws))

# assertions (prediction stated in the docstring)
for (r, lab, w, uerr, sup, mind, ws) in results:
    if uerr < 1e-3:
        ck.check(f'[empirical, not implied by Thm K for inexact unitarity] r={r} {lab} w={w}: unitary to {uerr:.1e} => sup||U - V_2|| = {sup:.3f} >= 1 - (unitarity slack)', sup >= 1 - 2 * uerr - 1e-9)
        ck.check(f'[empirical] r={r} {lab} w={w}: nearly unitary fit has W3 = 0 (got {ws[1].real:+.4f})', abs(ws[1]) < 1e-2)
neardone = [x for x in results if x[3] < 1e-3]
ck.check(f'continuation reached nearly unitary fits for every start ({len(neardone)} of {len(results)} stages with err < 1e-3)',
         len({(x[0], x[1]) for x in neardone}) == len({(x[0], x[1]) for x in results}))
sys.exit(ck.total())
