"""K2 part 2b: the O(kappa^2) Killing-sector closure on Z^4 (Euclidean).

At O(kappa^2), on matter at h = 0, gauge consistency needs, for lattice Killing fields
xi, eta (translations c, rotations w):  [L_xi, L_eta] phi = L_{C(xi,eta)} phi + (trivial: N*E).
(i)  exact real-space commutator of the constructed pseudo-rotation and pseudo-translation:
     [L_w, D_rho] = - w_{nu rho} S_rho D_nu    (S = average of the two neighbours, symbol cos k)
(ii) certificate that  R_rho = [L_w,D_rho] - (sum_s c_{rho s} D_s)  is NOT in the ideal (A)
     for any constants c (A = Euclidean kinetic symbol; (A) prime => test on complex shell A=0).
(iii) general mechanism on the real Lorentzian slice S_R (k_4 = iE): f(S_R) is compact, the
     Wick-rotated (4,j) rotation is a boost; the pulled-back boost field blows up where df is
     singular, even with the best quasi-local normalisation lambda (f.f = const on S_R).
"""
import numpy as np, itertools
rng = np.random.default_rng(11)
D = 4
def sh(F, mu, n): return np.roll(F, -n, axis=mu)
def Dsym(F, mu): return 0.5 * (sh(F, mu, 1) - sh(F, mu, -1))
def Savg(F, mu): return 0.5 * (sh(F, mu, 1) + sh(F, mu, -1))

print("== (i) exact real-space commutator on an open box (compact support) ==")
n = 12
X = np.indices((n,) * D).astype(float)
def Lw(F, a, b):  # w_ab = +1, w_ba = -1:  L = sum_{nu,mu} w_{nu mu} x_mu D_nu = x_b D_a - x_a D_b
    return X[b] * Dsym(F, a) - X[a] * Dsym(F, b)
worst = 0.0
for (a, b) in [(0, 1), (3, 1), (2, 3)]:
    for rho in range(D):
        phi = np.zeros((n,) * D); phi[3:-3, 3:-3, 3:-3, 3:-3] = rng.integers(-9, 10, size=(n - 6,) * D)
        lhs = Lw(Dsym(phi, rho), a, b) - Dsym(Lw(phi, a, b), rho)
        # prediction: -w_{nu rho} S_rho D_nu ; w_{a b}=1, w_{b a}=-1
        pred = np.zeros_like(phi)
        if rho == b: pred = pred - 1.0 * Savg(Dsym(phi, a), rho)   # w_{a rho}=w_ab=+1, nu=a
        if rho == a: pred = pred + 1.0 * Savg(Dsym(phi, b), rho)   # w_{b rho}=w_ba=-1, nu=b
        worst = max(worst, np.abs(lhs - pred).max())
print("max |[L_w, D_rho] phi - (-w_{nu rho} S_rho D_nu phi)| =", worst)
print("A translation would be -w_{nu rho} D_nu; the extra factor S_rho (cos k_rho) is the")
print("Euclidean twin of C3's Q_ca = cos k_c sin k_a.")

print("\n== (ii) ideal-membership certificate on the complex shell A(k)=0 ==")
def shell_points(m2, N, scale=0.8):
    pts = []
    while len(pts) < N:
        kj = rng.normal(size=3) * scale + 1j * rng.normal(size=3) * 0.3
        c4 = 1 + 0.5 * (np.sum(2 - 2 * np.cos(kj)) + m2)
        k4 = np.arccos(c4 + 0j)
        k = np.concatenate([kj, [k4]])
        A = np.sum(2 - 2 * np.cos(k)) + m2
        if abs(A) < 1e-10:
            pts.append(k)
    return np.array(pts)
for m2 in (0.0, 0.25, 1.0):
    P = shell_points(m2, 400)
    worst_rel = []
    for (a, b) in [(3, 0), (0, 1)]:   # (4,1) 'Euclidean boost' plane and a spatial plane
        w = np.zeros((D, D)); w[a, b] = 1; w[b, a] = -1
        for rho in range(D):
            R = np.array([-sum(w[nu, rho] * np.cos(k[rho]) * np.sin(k[nu]) for nu in range(D)) for k in P])
            B = np.array([[np.sin(k[s]) for s in range(D)] for k in P])   # allowed: constants * D_s
            c, *_ = np.linalg.lstsq(B, R, rcond=None)
            rel = np.linalg.norm(B @ c - R) / max(np.linalg.norm(R), 1e-300)
            if np.linalg.norm(R) > 1e-12:
                worst_rel.append(rel)
    print(f"m2={m2}: best constant-c fit of [L_w,D_rho] by translations on 400 shell points: "
          f"relative residual min/max = {min(worst_rel):.3f} / {max(worst_rel):.3f}")
print("Nonzero residual on the shell => [L_w, D] is not translation + trivial (A prime).")

print("\n== (iii) why no local choice fixes it: the real Lorentzian slice S_R (k_4 = iE) ==")
# nearest-neighbour A, translation symbols f = lambda * grad A (symmetric-T form, see report)
# choose the best quasi-local lambda: f.f (Minkowski) = -mu^2 const on S_R.
m2 = 0.25
def slice_data(kj):
    s2 = np.sum(2 - 2 * np.cos(kj), axis=-1) + m2
    E = np.arccosh(1 + s2 / 2)
    gA = 2 * np.sin(kj)                       # dA/dk_j (real)
    g4 = 2 * np.sinh(E)                       # dA/dk_4 = 2 sin(iE) = 2i sinh E -> imaginary part
    return E, gA, g4
# 1D cut along k1 (k2=k3=0): f_1 = lam*2 sin k1, g = lam*2 sinh E, lam = mu/(2 sqrt(sinh^2E - sin^2 k1))
ks = np.linspace(1e-4, np.pi, 20001)
kj = np.stack([ks, 0 * ks, 0 * ks], axis=-1)
E, gA, g4 = slice_data(kj)
for label, lam in [("lambda = 1/2 (f = sin k, the constructed T)", 0.5 * np.ones_like(ks)),
                   ("lambda = mu/|grad A|_Mink (best quasi-local; f.f const)", 1.0 / np.sqrt(g4**2 - gA[:, 0]**2))]:
    f1 = lam * gA[:, 0]; g = lam * g4
    df1 = np.gradient(f1, ks)
    # boost in (4,1) plane acting on (g, f1): d/deta (g, f1) = (f1, g); pulled back: V^1 = g / (df1/dk1)
    V1 = g / df1
    i0 = np.argmin(np.abs(df1))
    print(f"{label}:\n   f1 range on the cut [{f1.min():.4f},{f1.max():.4f}] (bounded: S_R compact);"
          f" Minkowski f.f varies in [{(f1**2-g**2).min():.4f},{(f1**2-g**2).max():.4f}]\n"
          f"   df1/dk1 vanishes at k1 = {ks[i0]:.4f} where g = {g[i0]:.4f} != 0  ->  max |V^1| on grid = {np.abs(V1).max():.3e}")
print("=> the boost field needed for closure is singular at an interior point of S_R: no local")
print("   (analytic) pseudo-rotation can realise it. General proof (report): f(S_R) is compact,")
print("   boost orbits of timelike vectors are not; any analytic V on compact S_R has a complete flow.")
