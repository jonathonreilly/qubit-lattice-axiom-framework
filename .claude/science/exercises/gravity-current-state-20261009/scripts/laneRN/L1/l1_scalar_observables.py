"""Lane RN / L1, scalar part 2: static pull, universality, light bending (gamma), TT self-energy at q->0,
and O(kappa) closure diagnostics of the matter constraint algebra.

General couplings: H = H_N(J,g) + H_m + n (S/ks + T00) + N_j(-(J/ks) G_j + P_j) + c' h_ij T_ij.
First-class closure at O(sqrt kappa) forces c' = -ks/J (checked identities in l1_scalar_stress.py).
Static dust source: g R(h) + S^T n / ks = 0, S(h)/ks = -T00.  For h = 2 psi delta:
   psi = ks T00/(4 qhat^2),  n = -2 g ks psi.   (lattice: k -> qhat = 2 sin(k/2), 09-14 note convention)
"""
import numpy as np

AX = (0, 1, 2)
print("=== 1. Static pull from the lattice constraints (GR point J=2ks, g=1/(2ks), ks=16 pi G, G=1) ===")
Lb = 96
k1 = 2 * np.pi * np.fft.fftfreq(Lb)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
qh2 = sum((2 * np.sin(K / 2)) ** 2 for K in (KX, KY, KZ))
qh2[0, 0, 0] = np.inf  # neutralising background (zero mode removed)
ks = 16 * np.pi
g = 1 / (2 * ks)
M = 1.0
T00k = M * np.ones_like(qh2)  # point source at origin
psi = np.real(np.fft.ifftn(ks * T00k / (4 * qh2)))
n = -2 * g * ks * psi
# compare to -G M / r ; subtract the uniform-background (periodic) offset using a large-r reference via
# the known lattice Green function: report r*n along axis and body diagonal
for lab, pts in (("axis", [(r, 0, 0) for r in (2, 4, 8, 12, 16)]), ("diag", [(r, r, r) for r in (1, 2, 4, 6, 8)])):
    vals = []
    for p in pts:
        r = np.sqrt(sum(c * c for c in p))
        # periodic correction: remove the r^2 background term of a neutral torus (Ewald) by differencing vs continuum
        vals.append((r, n[p], -M / r))
    print(lab, " ".join(f"r={r:5.2f}: n={v:+.5f} (-GM/r={c:+.5f})" for r, v, c in vals))
print("psi + n = 0 identically:", np.max(np.abs(psi + n)))
print("(differences from -GM/r at small r are the lattice Green function's cubic O(a^2/r^2) terms plus the")
print(" finite-torus neutralising background ~ r^2/L^3; the 1/r tail is the standard lattice Coulomb law.)")

print("\n=== 2. Passive response: exact one-particle frequency in a constant background (n, h=2 psi delta) ===")
# H_k = 1/2 [(1+n) - 3*2c'psi*(-1)...]: build from the T_jj symbols of l1_scalar_stress (per-mode, k and -k combined)
def omega_eff(k, m, nval, psival, J=2 * ks, gg=g, kss=ks):
    c = -kss / J
    s2 = (2 * np.sin(k / 2)) ** 2
    w2 = m * m + s2.sum()
    A = np.array([-m * m + np.cos(k[j]) * s2[j] - sum(s2[i] for i in AX if i != j) for j in AX])
    # H = (1+n) H_m + c * sum_j h_jj T_jj ,  T_jj = 1/2|pi|^2 + 1/2 A_j |phi|^2
    cpi = (1 + nval) + c * 2 * psival * 3
    cphi = (1 + nval) * w2 + c * 2 * psival * A.sum()
    return np.sqrt(cpi * cphi), np.sqrt(w2)

eps = 1e-7
for m in (0.0, 0.3, 1.0):
    for kv in ([1e-3, 0, 0], [0.3, 0, 0], [0.3, 0.3, 0.3], [1.0, 0, 0]):
        k = np.array(kv, float)
        if m == 0 and np.allclose(k, 0):
            continue
        wn, w0 = omega_eff(k, m, eps, 0.0)
        wp, _ = omega_eff(k, m, 0.0, eps)
        dn = (wn - w0) / (eps * w0)  # coefficient of n
        dp = (wp - w0) / (eps * w0)  # coefficient of psi
        pred = -np.sum(np.sin(k) ** 2) / w0**2 * (-2 * ks / (2 * ks)) * (-1)  # -sum sin^2/w^2 at GR point
        # potential seen with psi = -n (GR static solution): dw/w = n*(dn - dp)
        print(f"m={m:3.1f} k={kv}: dw/w = {dn:+.6f} n {dp:+.6f} psi  -> with psi=-n: {dn-dp:+.6f} n"
              f"   [sum sin^2 k/w^2 = {np.sum(np.sin(k)**2)/w0**2:.6f}]")

print("\n=== 3. gamma for general (J, g, ks): light sees n(1 + 1/(J g)); gamma = 1/(J g) = (c_matter/c_grav)^2 ===")
for Jg in (1.0, 0.9, 1.1):
    J = 2 * ks
    gg = Jg / J
    # static: n = -2 gg ks psi ; light: dw/w = n + 2 c' psi * (f.v/w), c' = -ks/J, f.v/w -> 1
    psi_ = 1.0
    n_ = -2 * gg * ks * psi_
    light = n_ + 2 * (-ks / J) * psi_
    print(f"J g = {Jg:.2f}: (light potential)/(massive potential) = {light/n_:.4f} = 1+gamma, gamma = {light/n_-1:.4f}")

print("\n=== 4. O(k^2 a^2) cubic anisotropy of the light-bending factor gamma_eff(k) = sum sin^2 k_j / omega^2 (m=0) ===")
for kmag in (0.1, 0.3, 0.6):
    for lab, dirn in (("axis", [1, 0, 0]), ("face", [1, 1, 0]), ("diag", [1, 1, 1])):
        k = kmag * np.array(dirn, float) / np.linalg.norm(dirn)
        ge = np.sum(np.sin(k) ** 2) / np.sum((2 * np.sin(k / 2)) ** 2)
        pred = 1 - 0.25 * np.sum(k**4) / np.sum(k**2)
        print(f"|k|={kmag}: {lab}: gamma_eff = {ge:.6f}  (1 - sum k^4/(4k^2) = {pred:.6f})")

print("\n=== 5. Universality: active and passive couplings both through T00 = energy density ===")
for m in (0.2, 0.8, 1.5):
    k = np.array([1e-4, 0, 0])
    wn, w0 = omega_eff(k, m, eps, 0.0)
    wp, _ = omega_eff(k, m, 0.0, eps)
    print(f"m={m}: passive coefficient of n per unit rest energy = {(wn-w0)/(eps*w0):.8f}, of psi = {(wp-w0)/(eps*w0):.2e};"
          f" active: sources S/ks = -T00, one quantum at rest has sum T00 = omega = {w0:.4f}, sum T_ij = 0")

print("\n=== 6. TT self-energy at q -> 0 from the LINEAR coupling only (paramagnetic, vacuum, per site) ===")
for Nb in (48, 96):
    kk = 2 * np.pi * (np.arange(Nb) + 0.5) / Nb  # offset grid avoids k=0
    KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing="ij")
    for m in (0.0, 0.5, 1.0):
        w2 = m * m + sum((2 * np.sin(K / 2)) ** 2 for K in (KX, KY, KZ))
        w = np.sqrt(w2)
        XE = np.sin(KX) ** 2 - np.sin(KY) ** 2       # h = eps diag(1,-1,0), coupling -1/2 h.T
        XT = 2 * np.sin(KX) * np.sin(KY)              # h_xy = h_yx = eps
        # E0(eps) = sum_k 1/2 sqrt(w^2 - eps X): d2E0/deps2 per site = -1/8 <X^2/w^3>  (k,-k pair counted via 1/2)
        cE = -np.mean(XE**2 / w**3) / 8
        cT = -np.mean(XT**2 / w**3) / 8
        print(f"Nb={Nb} m={m}: d2E0/deps2 per site: E-channel {cE:+.6f}, T2-channel {cT:+.6f}  (ratio {cE/cT:.4f}; isotropic would need XE^2 avg = XT^2 avg/... )")
print("Both channels are nonzero and unequal: the linear-order first-class coupling leaves a cubic-anisotropic")
print("TT 'mass' at O(kappa) unless an O(h^2) seagull is added.  Ward identity for constant strain: with")
print("U = exp(-i sum xi.P), xi_i = h_ij x_j/2, U H_m U^+ = H_m - 1/2 h.sum T + O(h^2) [identity (M)], so E0 is h-independent")
print("iff the O(h^2) term equals 1/2[S,[S,H_m]]; then Pi_TT(0) = para + seagull = 0 by the f-sum identity.")
