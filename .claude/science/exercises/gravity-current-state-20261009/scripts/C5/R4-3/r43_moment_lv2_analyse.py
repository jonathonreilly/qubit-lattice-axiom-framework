"""R4-3 check B2 analysis (reads r43_S_arrays.npz written by r43_moment_lv2_compute.py).
(1) empirical shell densities nu_N from the small-kappa direction mean (equidistribution: kappa^2 S_N -> 4 pi nu_N/tau^2);
(2) moment-conditioned (d'Alembertian) shell combinations with those nu_N: LI part ~ (pi/4) kappa^2;
(3) LV = std over 32 directions u; rel LV = std/LI; log-slopes;
(4) sign of S_w(u,kappa) along each direction: a zero of the symbol on the imaginary axis p = i kappa u
    is a homogeneous solution exp(-kappa u.x) that grows toward the future (forward-tube zero = instability);
(5) best (LV-minimising) weights with 4 LI conditions; in-sample and leave-kappa-out check.
"""
import numpy as np
from scipy.special import k1
D = np.load("r43_S_arrays.npz")
Ns, S, kaps, us = D["Ns"], D["S"], D["kaps"], D["us"]
taus = np.sqrt(-Ns.astype(float))
shape = lambda k, t: 4 * np.pi * k1(k * t) / (k * t)
ik = len(kaps) - 1
nu_emp = S[:, ik, :].mean(1) / shape(kaps[ik], taus)
print("empirical nu_N (small-kappa mean) vs counting estimate:")
for N, a, b in zip(Ns, nu_emp, D["nus"]):
    print(f"   N={N:3d}: nu_emp={a:.6f}  nu_count={b:.6f}  ratio={a/b:.5f}")
nus = nu_emp
LIfull = nus[:, None] * shape(kaps[None, :], taus[:, None])   # [shell, kappa]
M = np.array([nus * taus**-2, nus, nus * np.log(taus), nus * taus**2])
nrm = nus * taus**2 * np.log(taus)
A = np.vstack([M, nrm]); b = np.array([0, 0, 0, 0, 1.0])

def report(w, label):
    Sw = (w[:, None, None] * S).sum(0)                  # [kappa, u]
    LI = (w[:, None] * LIfull).sum(0)
    lv = Sw.std(1)
    print(f"\n{label}\n   w = {np.array2string(w, precision=3, max_line_width=220)}  |w|_2 = {np.linalg.norm(w):.2f}")
    print("   kappa   LI(exact form)  (pi/4)k^2    mean_u S_w    std_u S_w    rel LV=std/|LI|   min_u S_w/LI  max_u S_w/LI")
    for i, k in enumerate(kaps):
        print(f"   {k:5.3f}  {LI[i]: .4e}  {np.pi/4*k*k: .4e}  {Sw[i].mean(): .4e}  {lv[i]:.4e}   {lv[i]/abs(LI[i]):.3e}      "
              f"{Sw[i].min()/LI[i]: .3e}   {Sw[i].max()/LI[i]: .3e}")
    sel = kaps <= 0.2
    s1 = np.polyfit(np.log(kaps[sel]), np.log(lv[sel] / np.abs(LI[sel])), 1)[0]
    s2 = np.polyfit(np.log(kaps[sel]), np.log(lv[sel]), 1)[0]
    print(f"   log-slopes for kappa <= 0.2: rel LV ~ kappa^{s1:.2f}, abs LV ~ kappa^{s2:.2f}")
    sgn = np.sign(Sw)
    nchange = int((np.abs(np.diff(sgn, axis=0)) > 0).any(0).sum())
    print(f"   directions (of {len(us)}) along which S_w(u, kappa) changes sign on the kappa grid: {nchange}")
    return Sw, LI

for pick in [[-1, -2, -3, -5, -7], [-2, -3, -5, -6, -7], [-3, -5, -7, -10, -11], [-1, -4, -6, -9, -12]]:
    idx = [list(Ns).index(p) for p in pick if p in Ns]
    if len(idx) < 5: continue
    w = np.zeros(len(Ns)); w[idx] = np.linalg.solve(A[:, idx], b)
    report(w, f"5-shell d'Alembertian, shells {pick}")
w = np.linalg.lstsq(A, b, rcond=None)[0]
report(w, f"min-norm over all {len(Ns)} shells {list(Ns)}")
# LV-minimising weights: minimise sum_{kappa,u} (S_w - mean)^2/((pi/4)k^2)^2 subject to A w = b
P = (S - S.mean(2, keepdims=True)) / (np.pi / 4 * kaps[None, :, None] ** 2)
def optw(rows):
    Q = P[:, rows, :].reshape(len(Ns), -1); H = Q @ Q.T
    nA = A.shape[0]
    K = np.block([[2 * H, A.T], [A, np.zeros((nA, nA))]])
    return np.linalg.solve(K, np.concatenate([np.zeros(len(Ns)), b]))[:len(Ns)]
wopt = optw(np.arange(len(kaps)))
report(wopt, "LV-minimising weights (in-sample, all kappas)")
# leave-small-kappa-out: fit on kappa >= 0.1, test on kappa < 0.1
rows = np.where(kaps >= 0.1)[0]
w2 = optw(rows)
Sw, LI = report(w2, "LV-minimising weights fitted on kappa >= 0.1 only (test: kappa < 0.1)")
# spectral reading: per-shell abs LV kappa*std (should be ~ const if abs LV ~ 1/kappa)
print("\nper-shell kappa*std_u(S_N) (abs LV x kappa):")
for j, N in enumerate(Ns):
    print(f"   N={N:3d}: " + " ".join(f"{k*S[j,i].std():.2e}" for i, k in enumerate(kaps)))
# which shells have (anti)correlated LV patterns?
Pc = S[:, 6, :] - S[:, 6, :].mean(1, keepdims=True)
C = np.corrcoef(Pc)
print("\nLV-pattern correlation matrix at kappa=0.1 (|c| > 0.9 listed):")
for i in range(len(Ns)):
    for j in range(i + 1, len(Ns)):
        if abs(C[i, j]) > 0.9: print(f"   N={Ns[i]} & N={Ns[j]}: {C[i,j]:+.4f}")
print("pairs with |c|>0.9 at every kappa:")
for i in range(len(Ns)):
    for j in range(i + 1, len(Ns)):
        cs = [np.corrcoef(S[i, q] - S[i, q].mean(), S[j, q] - S[j, q].mean())[0, 1] for q in range(len(kaps))]
        if min(abs(c) for c in cs) > 0.9: print(f"   N={Ns[i]} & N={Ns[j]}: " + " ".join(f"{c:+.3f}" for c in cs))
