"""R15-6 step 6: sign of g for LINEAR fading-memory readers (the class the R15-4 worker is building; its formulas are
unrefereed and re-derived here).  Reader: y_j' = E - beta_j y_j, R = sum k_j y_j, E = -rho_tot' = 3h, beta_j > 4.
G_tau(x) = sum k_j x (1 - e^{-(beta_j - x) tau})/(beta_j - x);  G(x) = G_inf(x).
Identity + step response (re-derived): after latent heat Delta released at u_T into a sector of rate x (radiation 4,
dust 3), exact before, e = R - rho_nc = -Delta e^{-x tau}(1 - G_tau(x)), and V' = rho_v' - e', so for tau > 0
    g/H^2 = -e'/R,   e' = x Delta e^{-x tau} S_x(tau),   S_x(tau) := 1 - G_tau(x) + Ktil_x(tau),  Ktil_x = sum k_j e^{-(beta_j-x)tau}.
Hence g <= 0 after every drop into sector x  <=>  S_x(tau) >= 0 for all tau >= 0 (smooth releases: convolution with s' >= 0).
Lemma K (proved): if all k_j >= 0 then G is strictly increasing on [0, min beta), so G(3) = G(4) = 1 is impossible:
a linear reader exact on both dust and radiation has weights of both signs.  Below: 2- and 3-register exact designs,
min_tau S_x and the implied max g/H^2 for a fast drop of size alpha = 1 (g/H^2 ~ x (alpha/(1+alpha)) max(-S_x)).
"""
import numpy as np, itertools
taus = np.linspace(0, 30, 30001)
def design(betas, extra=None):
    b = np.array(betas, float)
    rows = [[3/(bj-3) for bj in b], [4/(bj-4) for bj in b]]; rhs = [1, 1]
    if extra is not None:   # third condition: G(2) = 1 (also exact on w = -1/3)
        rows.append([2/(bj-2) for bj in b]); rhs.append(1)
    return b, np.linalg.solve(np.array(rows), np.array(rhs, float))
def S(b, k, x):
    G = np.array([np.sum(k*x*(1-np.exp(-(b-x)*t))/(b-x)) for t in taus])
    Kt = np.array([np.sum(k*np.exp(-(b-x)*t)) for t in taus])
    return 1 - G + Kt
best = None
for b1, b2 in itertools.product([4.5, 5, 6, 8, 12, 20], [5, 6, 8, 12, 20, 40]):
    if b2 <= b1: continue
    b, k = design([b1, b2])
    s4 = S(b, k, 4.0).min(); s3 = S(b, k, 3.0).min()
    gmax = max(4*0.5*max(0, -s4), 3*0.5*max(0, -s3))
    print(f"betas=({b1},{b2}) k=({k[0]:+.3f},{k[1]:+.3f}) K(0)={k.sum():+.3f}: min S_4 = {s4:+.3f}, min S_3 = {s3:+.3f}"
          f" -> max g/H^2 after alpha=1 drop ~ {gmax:.3f}")
print("3-register designs exact on x = 2, 3, 4:")
for bs in [(5, 8, 20), (4.5, 6, 12), (6, 12, 40), (5, 10, 30)]:
    b, k = design(bs, extra=True)
    s4 = S(b, k, 4.0).min(); s3 = S(b, k, 3.0).min()
    print(f"betas={bs} k={np.round(k,3)}: min S_4 = {s4:+.3f}, min S_3 = {s3:+.3f}")
