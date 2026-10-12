"""R4-3 check D2: robustness of the tube sign changes to errors in the shell densities nu_N.
A density error dnu_N shifts K by the u-independent amount sum_N w_N dnu_N 4 pi K1(k tau)/(k tau).
Bound it for |dnu_N/nu_N| <= 1e-3 (the empirical nu_N agree with the counting estimator to <= 0.8% and
are expected good to ~3e-4) and compare with |K| at the bracketing kappas of each zero (r43_tube_zero.out)."""
import numpy as np
from scipy.special import k1
D = np.load("r43_S_arrays.npz"); Ns = list(D["Ns"]); S = D["S"]; kaps = D["kaps"]
taus = np.sqrt(-np.array(Ns, float))
nus = S[:, -1, :].mean(1) / (4 * np.pi * k1(kaps[-1] * taus) / (kaps[-1] * taus))
pick = [-1, -2, -3, -5, -7]; idx = [Ns.index(p) for p in pick]
A = np.array([nus * taus**-2, nus, nus * np.log(taus), nus * taus**2, nus * taus**2 * np.log(taus)])[:, idx]
w = np.linalg.solve(A, [0, 0, 0, 0, 1.0])
for k, Kbr in [(0.584, 25.8), (0.438, 45.6), (0.506, 3.5), (0.213, 440.0), (0.160, 527.4)]:
    bound = sum(abs(wi) * nus[j] * 1e-3 * 4 * np.pi * k1(k * taus[j]) / (k * taus[j]) for wi, j in zip(w, idx))
    LI = np.pi / 4 * k * k
    print(f"kappa={k:.3f}: |K| at direction 0 = {Kbr*LI:.3f};  bound on density-error shift (|dnu/nu|<=1e-3) = {bound:.3f}")
