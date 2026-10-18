"""K1: does R5's orbit lemma need SUPPLIED breaking, or can the fixed rule choose the residual group itself?
GEN-2: real CKM on orientation (rod) generations needs an Eg vacuum order.  Eg order parameter
Q = rho (cos t, sin t); strains e_i = sqrt(2/3) rho cos(t - 2 pi i/3) (traceless diagonal).
Most general O_h-invariant Landau free energy through 6th order:
   V = a rho^2 + b rho^3 cos3t + rho^4 + g rho^6 + c rho^6 cos6t   (cos3t: the E x E x E invariant)
t = n pi/3 -> tetragonal D4h (two strains equal: 1+2 levels); other t -> D2h (three distinct)."""
import numpy as np
rng = np.random.default_rng(1)
rho = np.linspace(1e-3, 2.0, 400)[:, None]; t = np.linspace(0, 2 * np.pi, 721)[None, :]
def vmin(a, b, c, g=0.5):
    V = a * rho**2 + b * rho**3 * np.cos(3*t) + rho**4 + g * rho**6 + c * rho**6 * np.cos(6*t)
    i = np.unravel_index(np.argmin(V), V.shape)
    return V[i], rho[i[0], 0], t[0, i[1]]
def residual(r, th):
    e = np.sqrt(2/3) * r * np.cos(th - 2*np.pi*np.arange(3)/3)
    gaps = np.abs(np.subtract.outer(e, e))[np.triu_indices(3, 1)]
    return ("D2h" if gaps.min() > 1e-3 * r else "D4h"), e
n, cnt = 3000, {"D2h": 0, "D4h": 0, "sym": 0}
pred_ok = 0
for _ in range(n):
    a = rng.uniform(-2, 0); b = rng.uniform(-1, 1); c = rng.uniform(-0.3, 0.3)
    v, r, th = vmin(a, b, c)
    if r < 0.02: cnt["sym"] += 1; continue
    kind, _ = residual(r, th); cnt[kind] += 1
    # analytic: at fixed rho the angular part b rho^3 u + c rho^6 (2u^2-1), u = cos3t, has an interior
    # minimum (D2h) iff c > 0 and |b| < 4 c rho^3
    pred = "D2h" if (c > 0 and abs(b) < 4 * c * r**3) else "D4h"
    pred_ok += (pred == kind)
print(f"random O_h-invariant Landau coefficients (n={n}): ordered-phase residual groups {cnt}")
print(f"   analytic criterion (c>0, |b|<4c rho^3) matches the numerical minimum in {pred_ok}/{n-cnt['sym']} ordered cases")
v, r, th = vmin(-1.0, 0.05, 0.2)
kind, e = residual(r, th)
print(f"example a=-1, b=0.05, c=0.2: rho={r:.3f}, t={np.degrees(th):.1f} deg -> {kind}, strains e = {np.round(e, 4)}")
# consequences on the two generation placements, first order in the order parameter
m0, k = 1.0, 0.3
print("   rod (axis-label) generations, M = m0*1 + k*diag(e): levels", np.round(np.sort(m0 + k * e), 4),
      "-> three levels, all at FIRST order in rho (equal insertion order, no exponent ladder)")
print("   corner generations: translations keep M diagonal; Eg splits the diagonal -> three levels, but M_u, M_d both"
      " diagonal -> CKM = 1")
