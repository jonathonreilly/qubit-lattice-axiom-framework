"""T34 Test B: is the lane's EWSB test (G_eff vs G_crit) a robust statement, and does it give a scale?
Pre-registered in PREREGISTRATION.md.  Pure arithmetic / 1-D minimisation.  No repo file touched.

Standard strong-coupling leading order (Kawamoto & Smit 1981, Nucl. Phys. B192, 100; Kluberg-Stern,
Morel, Petersson 1983): after the Haar integral over SU(N) links, staggered fermions keep only
    S_eff = m sum_x M(x) - (1/(4N)) sum_{x,mu} M(x) M(x+mu)  (+ baryon terms),   M = chi-bar chi,
i.e. NO fermion hopping term survives.  Mean field (M M -> sigma (M + M') - sigma^2, d forward links per site):
    F(sigma) = d sigma^2/(4N) - N ln(m + d sigma/(2N)).
The coefficient 1/(4N) is quoted from the literature, not re-derived here.
"""
import numpy as np
from scipy.optimize import minimize_scalar

print("B1  reproduce the lane's numbers (docs/V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_2026-05-10.md)")
P = 0.5934; u0 = P ** 0.25
Gc = u0 ** 2 / 4
for N in (2, 3, 4):
    G = 1 / (2 * N)
    print(f"    N_c={N}:  u0={u0:.4f}  G_crit={Gc:.4f}  G_eff=1/(2N)={G:.4f}  ratio={G/Gc:.3f}  ->",
          "broken" if G > Gc else "symmetric")

print("\nB2  standard strong-coupling LO staggered mean field (no fermion hopping), chiral limit m=0")
def F(s, N, d): return d * s ** 2 / (4 * N) - N * np.log(d * s / (2 * N))
allbroken = True
for d in (2, 3, 4):
    row = []
    for N in (2, 3, 4, 5, 6):
        r = minimize_scalar(lambda s: F(s, N, d), bounds=(1e-6, 50), method="bounded", options=dict(xatol=1e-12))
        s0 = r.x; pred = N * np.sqrt(2 / d)
        interior = (F(s0, N, d) < F(1e-3, N, d)) and abs(s0 - pred) < 1e-5
        allbroken &= interior
        row.append(f"N={N}: sigma0={s0:.4f} (2N^2/d)^.5={pred:.4f} m_eff={d*s0/(2*N):.3f}")
    print(f"    d={d}: " + " | ".join(row))
N, d = 3, 4
print(f"    (N,d)=(3,4): sigma0^2={2*N*N/d:.3f}, constituent mass m_eff={np.sqrt(d/2):.4f} lattice units; F'(sigma)->-inf as sigma->0 (log): always broken")
print("    every (N,d) broken with sigma0 = N sqrt(2/d):", allbroken)

print("\nB3  scale: what does a condensate look like in lattice units, and what tuning would put it at v?")
v, MPl = 246.22, 1.2209e19
s_target = v / MPl
print(f"    v/M_Pl = {s_target:.4e}")
tune = s_target ** 2 / (4 * u0 ** 2)      # sigma_min^2 = 16(G-Gc) = 16 Gc (G/Gc-1) = 4 u0^2 (G/Gc-1)
print(f"    hybrid model: sigma_min^2 = 4 u0^2 (G/G_c - 1)  ->  required G/G_c - 1 = {tune:.3e}")
print(f"    ratio-to-criticality needed vs the lane's 0.866: fine-tuning to 1 part in {1/tune:.2e}")
print(f"    KS LO: sigma0 = {N*np.sqrt(2/d):.3f} (lattice units)  ->  m_eff*M_Pl = {np.sqrt(d/2)*MPl:.2e} GeV (Planck scale)")
print("    a supercritical NJL-type condensate is at 1/a unless the distance to criticality is ~1e-34")

print("\nB4  cross-check of the 'exponentially small scale needs a marginal coupling' reading (1-loop, ladder alpha_c)")
def decades(b0, alpha, alpha_c):
    ex = 2 * np.pi * (1 / alpha - 1 / alpha_c) / b0
    return ex, ex / np.log(10)
need = np.log(MPl / v)
print(f"    needed exponent ln(M_Pl/v) = {need:.2f}  ({need/np.log(10):.1f} decades)")
for name, b0, alpha, ac in (("SU(3), 6 flavours, alpha=1/4pi", 11 - 2 * 6 / 3, 1 / (4 * np.pi), np.pi / (3 * 4 / 3)),
                            ("SU(3), 6 flavours, alpha_LM=0.0907", 11 - 2 * 6 / 3, 0.0907, np.pi / (3 * 4 / 3)),
                            ("SU(2)_L, 12 Weyl doublets, alpha=1/4pi", 22 / 3 - (2 / 3) * 0.5 * 12, 1 / (4 * np.pi), np.pi / (3 * 3 / 4))):
    ex, dec = decades(b0, alpha, ac)
    print(f"    {name}: b0={b0:.3f}, exponent={ex:.1f} ({dec:.1f} decades)  -> Lambda/M_Pl = {np.exp(-ex):.2e}")
