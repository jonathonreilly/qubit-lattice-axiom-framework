"""K3: is R2's |Vcb|/|Vus| >= sqrt2 a property of clustering, or of Gaussian kernels?
Leading-order claim (K's derivation, clustered collinear limit, shared doublet cluster xi_Q):
   |Vcb|/|Vus| = G(xi_Q) * |dl_x| / |dl_x + (1/2) d(l_xxy/l_xy)|,   l = log K, d = (up) - (down),
so it equals G only when l is quadratic (Gaussian family: l_xxy = 0).  Test with two non-Gaussian kernels."""
import numpy as np
from scipy.special import erf
def G(p):
    p = np.asarray(p, float); pp = p - p.mean()
    return np.linalg.norm(pp) ** 3 / abs((p[1] - p[0]) * (p[2] - p[0]) * (p[2] - p[1]))
xi = np.array([-1.0, 0.0, 1.0])
def ckm(Ku, Kd, dQ, du, dd, xq=xi, xu=xi, xd=xi):
    X = dQ * xq
    Mu = Ku(X[:, None], (du * xu)[None, :]); Md = Kd(X[:, None], (dd * xd)[None, :])
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)
    V = np.abs(Uu.T @ Ud)
    return V[1, 2], V[0, 1], V[0, 2], su / su[0], sd / sd[0]
print("(i) cubic-log kernel K_f = exp(F_f(x-y)), F_f(u) = -(u-D)^2/2 + c_f (u-D)^3, SAME offset D for u and d")
for D, cu, cd in [(0.3, 0.3, -0.3), (0.5, 0.2, -0.2), (0.0, 0.3, -0.3), (0.8, 0.3, -0.3), (0.3, 0.0, 0.0)]:
    F = lambda c: (lambda x, y: np.exp(-(x - y - D) ** 2 / 2 + c * (x - y - D) ** 3))
    lx = lambda c: D + 3 * c * D ** 2; kap = lambda c: 6 * c / (-1 - 6 * c * D)
    dlx = lx(cu) - lx(cd); dk = kap(cu) - kap(cd)
    pred = G(xi) * abs(dlx) / abs(dlx + 0.5 * dk) if abs(dlx + 0.5 * dk) > 0 else np.nan
    for dl in (0.02, 0.005):
        if cu == cd: break
        vus, vcb, vub, su, sd = ckm(F(cu), F(cd), dl, dl, dl)
        print(f"   D={D} c=({cu},{cd}) delta={dl}: |Vus|={vus:.3e} |Vcb|={vcb:.3e} ratio={vcb/vus:.4f} (pred {pred:.4f}); "
              f"m_c/m_t={su[1]:.1e} m_u/m_t={su[2]:.1e}")
print("   (D=0.3, c_u=c_d: identical kernels -> CKM = 1, skipped)")
print("\n(ii) physical overlaps: K_f(x,y) = int psi_Q(z-x) psi_f(z-y) dz, psi_Q Gaussian, psi_f skew-normal")
print("     (same centre offset D for u_R and d_R, opposite skew a_f = +-a; flat Higgs)")
z = np.linspace(-14, 14, 5601); dz = z[1] - z[0]
def skew(t, a): return np.exp(-t ** 2 / 2) * (1 + erf(a * t / np.sqrt(2)))
def Kover(a, D, wQ=1.0):
    def K(X, Y):
        X = np.atleast_1d(X).ravel(); Y = np.atleast_1d(Y).ravel()
        PQ = np.exp(-((z[None, :] - X[:, None]) / wQ) ** 2 / 2)
        Pf = skew(z[None, :] - Y[:, None] - D, a)
        return PQ @ Pf.T * dz
    return K
for D, a in [(0.4, 1.0), (0.4, 2.0), (0.8, 1.0), (1.5, 1.0), (0.0, 1.0)]:
    vus, vcb, vub, su, sd = ckm(Kover(a, D), Kover(-a, D), 0.01, 0.01, 0.01)
    print(f"   D={D} a=+-{a}: |Vus|={vus:.3e} |Vcb|={vcb:.3e} |Vcb|/|Vus|={vcb/vus:.3f} |Vub|/(|Vus||Vcb|)={vub/(vus*vcb):.2f}; "
          f"m_c/m_t={su[1]:.1e} m_s/m_b={sd[1]:.1e}")
# random scan in the physical class: independent offsets and skews (R2's sampling style) vs co-located
rng = np.random.default_rng(5)
for label, same in (("independent offsets", False), ("co-located u_R, d_R", True)):
    r = []
    for _ in range(150):
        Du = rng.uniform(-1.5, 1.5); Dd = Du if same else rng.uniform(-1.5, 1.5)
        au, ad = rng.uniform(-3, 3, size=2)
        vus, vcb, *_ = ckm(Kover(au, Du), Kover(ad, Dd), 0.01, 0.01 * rng.uniform(0.5, 2), 0.01 * rng.uniform(0.5, 2),
                           xi, np.sort(rng.normal(size=3)), np.sort(rng.normal(size=3)))
        r.append(vcb / vus)
    r = np.array(r)
    print(f"   {label}: |Vcb|/|Vus| percentiles 5/50/95 = {np.percentile(r, [5, 50, 95]).round(3)}; "
          f"fraction <= 0.3: {np.mean(r <= 0.3):.3f}; <= 0.55: {np.mean(r <= 0.55):.3f}")
