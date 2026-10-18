"""R2 / L2: clustered overlaps.  Three generations sit within a distance delta of each
other, the overlap kernel K(x, y) is smooth on a scale sigma = 1, delta << 1.

(a) singular-value orders vs delta: collinear (1D) vs C3 triangle (2D), Gaussian vs
    exponential (cusp) kernel.
(b) the shape invariant kappa = m2^2/(m1 m3) in the clustered limit; check the closed
    form kappa = 2 G(xi) G(eta), G = |xi_perp|^3/|Vandermonde| >= sqrt2, for the Gaussian.
(c) CKM when up and down share the doublet cluster: scaling of |Vus|, |Vcb|, |Vub|.
"""
import numpy as np
np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(7)

def gauss(x, y):
    d = np.atleast_1d(x - y)
    return np.exp(-0.5 * d @ d)

def expo(x, y):
    d = np.atleast_1d(x - y)
    return np.exp(-np.sqrt(d @ d))

def lattice_expo(x, y):  # Manhattan-distance tail, as for a lattice Green function
    return np.exp(-np.sum(np.abs(np.atleast_1d(x - y))))

def mat(K, X, Y):
    return np.array([[K(x, y) for y in Y] for x in X])

def sv(M):
    return np.linalg.svd(M, compute_uv=False)

print("(a) log-log slopes of singular values vs delta (delta = 1e-2 .. 1e-3)")
xi = np.array([-1.0, 0.0, 1.0]); eta = np.array([-0.7, 0.2, 1.1])
tri = [np.array([np.cos(t), np.sin(t)]) for t in 2 * np.pi * np.arange(3) / 3]
tri2 = [np.array([np.cos(t + 0.4), np.sin(t + 0.4)]) * 1.3 + np.array([0.2, -0.1]) for t in 2 * np.pi * np.arange(3) / 3]
for name, K in [("gauss", gauss), ("expo", expo), ("lattice-expo", lattice_expo)]:
    for geo in ["collinear", "triangle"]:
        out = []
        for dl in [1e-2, 1e-3]:
            if geo == "collinear":
                X = [np.array([dl * a]) + 0.3 for a in xi]; Y = [np.array([dl * b]) for b in eta]
            else:
                X = [dl * p + np.array([0.3, 0.1]) for p in tri]; Y = [dl * p for p in tri2]
            out.append(np.log(sv(mat(K, X, Y))))
        slope = (out[1] - out[0]) / np.log(1e-3 / 1e-2)
        print(f"    {name:13s} {geo:9s} slopes {slope}")

print("\n(b) kappa = m2^2/(m1 m3) in the clustered limit, Gaussian kernel, L and R collinear, no offset")
def G(p):
    p = np.asarray(p, float); pp = p - p.mean()
    V = (p[1] - p[0]) * (p[2] - p[0]) * (p[2] - p[1])
    return np.linalg.norm(pp) ** 3 / abs(V)
for _ in range(5):
    a = np.sort(rng.normal(size=3)); b = np.sort(rng.normal(size=3))
    dl = 2e-3
    s = sv(mat(gauss, [np.array([dl * t]) for t in a], [np.array([dl * t]) for t in b]))
    print(f"    numeric {s[1]**2/(s[0]*s[2]):9.4f}   2 G G = {2*G(a)*G(b):9.4f}")
ts = np.linspace(0.01, 0.99, 981)
print("    min_t G(0,t,1) =", f"{min(G([0, t, 1]) for t in ts):.5f}", " sqrt2 =", f"{np.sqrt(2):.5f}", " => kappa_Gauss >= 4 (no offset)")

print("    with a centre offset c between the L and R clusters (Gaussian, equal spacing):")
for c in [0.0, 0.3, 0.6, 1.0, 1.5, 2.0, 3.0]:
    dl = 2e-3
    s = sv(mat(gauss, [np.array([dl * t + c]) for t in xi], [np.array([dl * t]) for t in xi]))
    print(f"      c = {c:3.1f}  kappa = {s[1]**2/(s[0]*s[2]):9.4f}")
# generic analytic kernel: kappa is set by Taylor coefficients -> any value
vals = []
for _ in range(2000):
    co = rng.normal(size=(4, 4))
    K = lambda x, y, co=co: float(sum(co[m, n] * x[0] ** m * y[0] ** n for m in range(4) for n in range(4)))
    dl = 1e-2
    s = sv(mat(K, [np.array([dl * t]) for t in xi], [np.array([dl * t]) for t in xi]))
    vals.append(s[1] ** 2 / (s[0] * s[2]))
vals = np.array(vals)
print("    generic analytic kernel (random Taylor coeffs, equal spacing): kappa percentiles 5/50/95 =",
      np.percentile(vals, [5, 50, 95]))

print("\n(c) CKM with a shared doublet cluster (Gaussian, collinear).  delta_Q, delta_u, delta_d, offsets c_u, c_d")
def ckm(dQ, du, dd, cu, cd, shapeQ=xi, shapeu=xi, shaped=xi):
    XQ = [np.array([dQ * t]) for t in shapeQ]
    Mu = mat(gauss, XQ, [np.array([du * t + cu]) for t in shapeu])
    Md = mat(gauss, XQ, [np.array([dd * t + cd]) for t in shaped])
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)
    V = np.abs(Uu.T @ Ud)  # rows/cols ordered heavy, mid, light
    return su, sd, V
for (dQ, du, dd, cu, cd) in [(0.05, 0.05, 0.05, 0.0, 0.0), (0.05, 0.05, 0.05, 0.5, -0.5),
                             (0.02, 0.02, 0.02, 0.5, -0.5), (0.1, 0.1, 0.1, 0.5, -0.5), (0.05, 0.02, 0.1, 0.8, -0.3)]:
    su, sd, V = ckm(dQ, du, dd, cu, cd)
    print(f"    dQ={dQ} du={du} dd={dd} cu={cu} cd={cd}: m_u/m_t {su[2]/su[0]:.2e} m_c/m_t {su[1]/su[0]:.2e} "
          f"m_d/m_b {sd[2]/sd[0]:.2e} m_s/m_b {sd[1]/sd[0]:.2e} |Vus|~V[1,2]={V[1,2]:.3e} |Vcb|~V[0,1]={V[0,1]:.3e} |Vub|~V[0,2]={V[0,2]:.3e}")

# random scan: distribution of |Vcb|/|Vus| and |Vub|/(|Vus||Vcb|) over clustered collinear configurations
r1, r2, ok = [], [], 0
for _ in range(4000):
    dQ, du, dd = 10 ** rng.uniform(-2, -0.7, size=3)
    cu, cd = rng.uniform(-1.5, 1.5, size=2)
    sh = [np.sort(rng.normal(size=3)) for _ in range(3)]
    su, sd, V = ckm(dQ, du, dd, cu, cd, *sh)
    if V[1, 2] > 0 and V[0, 1] > 0:
        r1.append(V[0, 1] / V[1, 2]); r2.append(V[0, 2] / (V[1, 2] * V[0, 1]))
r1, r2 = np.array(r1), np.array(r2)
print("    random clustered configs: |Vcb|/|Vus| percentiles 5/50/95 =", np.percentile(r1, [5, 50, 95]),
      " fraction <= 0.55 :", f"{np.mean(r1 <= 0.55):.3f}", " (observed 0.18)")
print("    |Vub|/(|Vus||Vcb|) percentiles 5/50/95 =", np.percentile(r2, [5, 50, 95]), " (observed ~0.40)")
