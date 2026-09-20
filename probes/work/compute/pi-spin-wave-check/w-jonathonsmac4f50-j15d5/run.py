#!/usr/bin/env python3
"""C:pi-spin-wave-check:a1   worker w-jonathonsmac4f50-j15d5 (claude-opus-5)

Does the reversible law's spin-wave kernel reproduce the formation kernel?
Sphere menu: Z(S) = 4 pi sinh(beta|S|)/(beta|S|), pi(s) proportional to exp(sum_x log Z(S_x)),
S_x the sum of the n records in a symmetric neighbourhood of x (n = 7 here: {0, +-e_1, +-e_2, +-e_3}).

A1  the expansion to second order in the transverse fluctuations, with the exact coefficient
A2  the sphere's own measure contributes a second-order term too; both versions are given
N1  the Hessian of -log pi at the aligned configuration, by finite differences on the block-circulant row,
    Fourier-diagonalised and compared with sigma^2/(1 - phi^2) mode by mode at beta = 2 and 6
"""
import time
from itertools import product
import numpy as np
import sympy as sp

t0 = time.time()
def A_l(x): return 1.0 / np.tanh(x) - 1.0 / x

# ---------------------------------------------------------------- A1 the expansion
b, n_, a, t = sp.symbols("beta n a t", positive=True)
Z = 4 * sp.pi * sp.sinh(b * a) / (b * a)
dlogZ = sp.simplify(sp.diff(sp.log(Z), a))
print(f"A1 d/da log Z(a) = {sp.simplify(dlogZ)} = beta A(beta a) with A(x) = coth x - 1/x:",
      sp.simplify(dlogZ - b * (sp.coth(b * a) - 1 / (b * a))) == 0)
print("A1 write s_x = (theta_x, sqrt(1 - |theta_x|^2)), theta in R^2. Then for a symmetric neighbourhood of size n")
print("A1   |S_x| = n - (1/2) sum_{y in N(x)} |theta_y|^2 + (1/2n) |sum_{y in N(x)} theta_y|^2 + O(theta^4),")
print("A1 and since |S_x| - n is already second order, only the first derivative of log Z contributes:")
print("A1   sum_x log Z(S_x) = const + beta A(n beta) sum_x (|S_x| - n) + O(theta^4).")
print("A1 In Fourier (phi(k) = (1/n) sum_{offsets} e^{i k.delta}, real for a symmetric set) the bracket is")
print("A1   (1/n)|n phi|^2 - n = -n (1 - phi^2), so  -log pi = (1/2N) sum_k lambda(k) |theta(k)|^2 with")
print("A1   lambda(k) = beta A(n beta) n (1 - phi(k)^2)    -> the coefficient is beta' = beta A(n beta), not A(n beta)")
print("A1 The claimed formation kernel is sigma^2/(1 - phi^2) with sigma^2 = A(n beta)/(n beta), i.e. an inverse")
print("A1 stiffness n beta (1 - phi^2)/A(n beta). Their ratio is")
print("A1   [1/lambda] / [sigma^2/(1-phi^2)] = 1/A(n beta)^2, the same in every mode,")
print("A1 and 1/A(x)^2 = 1 + 2/x + O(1/x^2), so the two agree to leading order in 1/(n beta) and differ at the")
print("A1 relative order 2/(n beta) - the same order as the quartic terms dropped from the expansion.")
x = sp.Symbol("x", positive=True)
print("A1 exactly A(x) = 1 - 1/x + 2/(e^{2x} - 1):",
      sp.simplify(sp.expand((sp.coth(x).rewrite(sp.exp) - 1 / x) - (1 - 1 / x + 2 / (sp.exp(2 * x) - 1)))) == 0)
print("A1 so up to e^{-2x}, 1/A(x)^2 = 1/(1 - 1/x)^2 = 1 + 2/x + 3/x^2 + ... :",
      sp.series(1 / (1 - 1 / x) ** 2, x, sp.oo, 4).removeO().equals(1 + 2 / x + 3 / x ** 2 + 4 / x ** 3))
for nb in (14, 42):
    print(f"A1   at n beta = {nb}: A = {A_l(nb):.6f}, 1/A^2 = {1/A_l(nb)**2:.6f} (1 + 2/(n beta) = {1+2/nb:.6f})")

# ---------------------------------------------------------------- A2 the sphere's own measure
print("A2 the uniform measure on the sphere is dtheta/sqrt(1 - |theta|^2), which adds +|theta_x|^2/2 to log pi,")
print("A2 i.e. subtracts exactly 1 from lambda(k) in the coordinates theta. With it,")
print("A2   lambda_measure(k) = beta A(n beta) n (1 - phi(k)^2) - 1,")
print("A2 which matters only where 1 - phi^2 is not small: it is a large-k correction, not a long-wave one.")

# ---------------------------------------------------------------- N1 the Hessian
OFF = [(0, 0, 0)] + [tuple(v if j == i else 0 for j in range(3)) for i in range(3) for v in (1, -1)]
N_PRED = len(OFF)
print(f"N1 neighbourhood {OFF} of size n = {N_PRED}")
def minus_log_pi(theta, L, beta, jacobian):
    """theta: (L,L,L,2); s = (theta, sqrt(1-|theta|^2)); returns -sum_x log Z(beta |S_x|) (+ measure term)"""
    lon = np.sqrt(np.clip(1 - (theta ** 2).sum(-1), 0, None))
    s = np.concatenate([theta, lon[..., None]], axis=-1)
    S = sum(np.roll(s, (-o[0], -o[1], -o[2]), axis=(0, 1, 2)) for o in OFF)
    aa = np.linalg.norm(S, axis=-1)
    val = -np.sum(np.log(np.sinh(beta * aa) / (beta * aa)))
    if jacobian: val += -np.sum(0.5 * np.log(np.clip(1 - (theta ** 2).sum(-1), 1e-300, None))) * -1
    return float(val)
def hessian_row(L, beta, jacobian, h=2e-4):
    """the block-circulant first row: H[(0,c), (x,c')] for all x, by central differences"""
    row = np.zeros((L, L, L, 2, 2))
    base = np.zeros((L, L, L, 2))
    for c in range(2):
        for x in product(range(L), repeat=3):
            for cp in range(2):
                tp = base.copy(); tm = base.copy(); tpm = base.copy(); tmp = base.copy()
                tp[(0, 0, 0) + (c,)] += h; tp[x + (cp,)] += h
                tm[(0, 0, 0) + (c,)] -= h; tm[x + (cp,)] -= h
                tpm[(0, 0, 0) + (c,)] += h; tpm[x + (cp,)] -= h
                tmp[(0, 0, 0) + (c,)] -= h; tmp[x + (cp,)] += h
                f = (minus_log_pi(tp, L, beta, jacobian) + minus_log_pi(tm, L, beta, jacobian)
                     - minus_log_pi(tpm, L, beta, jacobian) - minus_log_pi(tmp, L, beta, jacobian)) / (4 * h * h)
                row[x + (c, cp)] = f
    return row
for L in (4, 6):
    g = np.meshgrid(*([2 * np.pi * np.arange(L) / L] * 3), indexing="ij")
    phi = sum(np.cos(sum(o[j] * g[j] for j in range(3))) for o in OFF) / N_PRED
    for beta in (2.0, 6.0):
        for jac in (False, True):
            row = hessian_row(L, beta, jac)
            Hk = np.fft.fftn(row, axes=(0, 1, 2))       # 2x2 matrix per mode
            lam = np.real(0.5 * (Hk[..., 0, 0] + Hk[..., 1, 1]))
            aniso = float(np.max(np.abs(Hk[..., 0, 0] - Hk[..., 1, 1])) + np.max(np.abs(Hk[..., 0, 1])))
            pred = beta * A_l(N_PRED * beta) * N_PRED * (1 - phi ** 2) - (1.0 if jac else 0.0)
            s2 = A_l(N_PRED * beta) / (N_PRED * beta)
            claimed = np.where(1 - phi ** 2 > 1e-12, s2 / np.where(1 - phi ** 2 > 1e-12, 1 - phi ** 2, 1), np.inf)
            modes = sorted({tuple(sorted((min(i, L - i), min(j, L - j), min(m, L - m)))) for i, j, m in
                            product(range(L), repeat=3)})
            print(f"N1 L={L} beta={beta} {'with' if jac else 'without'} the sphere measure term: "
                  f"Hessian isotropy residual {aniso:.2e}, A(n beta)={A_l(N_PRED*beta):.6f}, "
                  f"1/A^2={1/A_l(N_PRED*beta)**2:.4f}")
            for mode in (modes if L == 4 else []):
                idx = (mode[0], mode[1], mode[2])
                if 1 - phi[idx] ** 2 < 1e-12: continue
                lh = lam[idx]; lp = pred[idx]
                print(f"N1   k=2pi{mode}/{L}: 1-phi^2={1-phi[idx]**2:.4f} Hessian lambda={lh:.5f} "
                      f"expansion={lp:.5f} (ratio {lh/lp:.5f}) | 1/lambda={1/lh:.5f} claimed kernel="
                      f"{claimed[idx]:.5f} (ratio {(1/lh)/claimed[idx]:.5f})")
            rats = [(1 / lam[m]) / claimed[m] for m in modes if 1 - phi[m] ** 2 > 1e-12]
            hess = [lam[m] / pred[m] for m in modes if 1 - phi[m] ** 2 > 1e-12]
            print(f"N1 L={L} beta={beta} {'with' if jac else 'without'} the measure term: Hessian/expansion over "
                  f"the {len(hess)} modes {min(hess):.6f} to {max(hess):.6f}; (1/lambda)/claimed kernel "
                  f"{min(rats):.5f} to {max(rats):.5f}" + ("" if jac else f", against 1/A^2 = {1/A_l(N_PRED*beta)**2:.5f}"))
print(f"SUMMARY: expanding log pi about the aligned configuration gives lambda(k) = beta A(n beta) n (1 - phi^2) "
      f"(the coefficient is beta A(n beta), and the sphere's own measure subtracts exactly 1), so the reversible "
      f"law's spin-wave kernel is the formation kernel sigma^2/(1-phi^2) times 1/A(n beta)^2 = 1 + 2/(n beta) + ...: "
      f"the same in every mode, 1.1597 at beta=2 and 1.0494 at beta=6 for n=7, which the numerical Hessian on a 4^3 "
      f"torus reproduces mode by mode; the two agree to the order the expansion controls; {time.time()-t0:.0f}s")
