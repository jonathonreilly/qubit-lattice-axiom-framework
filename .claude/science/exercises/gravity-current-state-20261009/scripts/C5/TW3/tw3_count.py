"""TW-3 probe (d): counting.
(1) Weyl count per SM generation (with/without nu_R) mod 16.
(2) Staggered edge (3D Hamiltonian, continuous time): 1 complex mode/site per field, 2 Dirac tastes/field.
    Onsite Theta acts as T (A sites) or T with sign (B sites): Z8 per site (tw3_fk.out) =>
    an onsite Theta-symmetric unique gapped state needs (2 x #fields) = 0 mod 8 Majoranas/site.
(3) Content per generation if each component field of the 16 is one staggered field:
    2 tastes x (16 + 16bar) Weyl; light = 16; to remove = 48.
(4) First-order strong-coupling gap of an FK lattice: Delta_f = 14W - max_k eps_u(k) + O(t^2/W);
    the strain coefficient for the 3D staggered band with traceless strain.
"""
from fractions import Fraction as F
import numpy as np

gen = {"Q": 6, "u^c": 3, "d^c": 3, "L": 2, "e^c": 1}
w15 = sum(gen.values())
print("Weyl per generation: SM", w15, "; with nu_R", w15 + 1)
for ng in (1, 3):
    print(f"  {ng} gen: SM {ng * w15} (mod 16 = {ng * w15 % 16}); +nu_R {ng * (w15 + 1)} (mod 16 = {ng * (w15 + 1) % 16})")

print("\nStaggered fields per site and the onsite Z8 (Majoranas/site = 2 x fields):")
for nf in range(1, 9):
    maj = 2 * nf
    print(f"  {nf} field(s): {maj} Majoranas/site, mod 8 = {maj % 8}; Dirac tastes {2 * nf}; Weyl {4 * nf};"
          f" onsite symmetric gapping {'possible' if maj % 8 == 0 else 'impossible'}")

print("\nOne generation, one staggered field per component of the 16 (16 fields):")
nf = 16
print(f"  Weyl content: 2 tastes x (16 + 16bar) = {2 * 32}; light wanted 16; to gap {2 * 32 - 16} = {(2 * 32 - 16) // 16} x 16")
print(f"  Majoranas/site = {2 * nf} = {2 * nf // 8} x 8")
print("  NF-1 counting (22.5 Dirac fields / 2 tastes):", F(45, 2) / 2, "; with 3 nu_R:", F(48, 2) / 2)
print("  T1 (one staggered field per SM Dirac field, twin unwanted), with nu_R: twins =",
      F(48, 2), "Dirac =", 48, "Weyl = 3 x 16 ->", 48 % 16 == 0)

print("\nFirst-order strong-coupling single-fermion gap, 3D staggered band, traceless strain t_j = t(1+u_j):")
# eps(k) = sqrt(sum_j t_j^2 s(k_j)^2): max = smax * sqrt(sum t_j^2)
for name, uv in (("E_g (1,-1,0)", (1, -1, 0)), ("E_g (1,1,-2)/sqrt3", (1 / np.sqrt(3), 1 / np.sqrt(3), -2 / np.sqrt(3)))):
    uv = np.array(uv, float)
    f = lambda h: np.sqrt(np.sum((1 + h * uv) ** 2))
    h = 1e-4
    d2 = (f(h) + f(-h) - 2 * f(0)) / h ** 2
    print(f"  {name}: d2/du2 sqrt(sum t_j^2)/t = {d2:.6f} (analytic |u|^2/sqrt3 = {np.sum(uv**2) / np.sqrt(3):.6f});"
          " so d2_u Delta_f = -smax * that * t, independent of W")
# compare: cluster checks (L3/plaqpi: max eps = sqrt(t_x^2+t_y^2), d2 = sqrt2)
print("  2D cluster analogue (L3, plaqpi): d2_u sqrt(t_x^2+t_y^2) = sqrt2 =", np.sqrt(2))
