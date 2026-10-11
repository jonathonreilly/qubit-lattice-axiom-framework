"""Independent arithmetic/symbolic checks for the C4/RE/E2 referee.

This file deliberately does not import any e2_* worker module.  Published
one-loop beta functions are entered directly, then linearized with SymPy.
"""

from math import log, log10, pi

import sympy as sp


# 1. Linearize the QED and Yukawa velocity beta functions quoted by
# Anber--Donoghue (arXiv:1102.0789), with beta = d/d ln(mu).
e2, y2, xf, xg, xb = sp.symbols("e2 y2 xf xg xb", real=True)
cf, cg, cb = 1 + xf, 1 + xg, 1 + xb

beta_cg = 4 * e2 / (3 * (4 * sp.pi) ** 2) * (cg**2 - cf**2) / (cf * cg)
beta_cf_qed = (
    8
    * e2
    / (3 * (4 * sp.pi) ** 2)
    * (cf - cg)
    * (4 * cf**2 + 3 * cf * cg + cg**2)
    / (cg * (cf + cg) ** 2)
)
beta_cb_yuk = y2 * (cb**2 - cf**2) / (8 * sp.pi**2 * cb * cf**3)
beta_cf_yuk = y2 * (cf - cb) / (6 * sp.pi**2 * cb * (cf + cb) ** 2)


def linear_coeff(expr, variable):
    """Coefficient at the Lorentz-invariant point."""
    return sp.simplify(sp.diff(expr, variable).subs({xf: 0, xg: 0, xb: 0}))


print("AD QED linearization, beta=d/dln(mu):")
print("  beta(c_gamma) coefficient of (x_gamma-x_f) =", linear_coeff(beta_cg, xg))
print("  beta(c_f) coefficient of (x_f-x_gamma) =", linear_coeff(beta_cf_qed, xf))
print("  relative rate for d/dL, L=ln(Lambda/mu) =", sp.simplify(e2 / (2 * sp.pi**2)))
print("AD Yukawa linearization, beta=d/dln(mu):")
print("  beta(c_b) coefficient of (x_b-x_f) =", linear_coeff(beta_cb_yuk, xb))
print("  beta(c_f) coefficient of (x_f-x_b) =", linear_coeff(beta_cf_yuk, xf))


# 2. Integrated weak-coupling suppressions.
MPL, TEV = 1.22e19, 1.0e3
LPT = log(MPL / TEV)
alpha_qed_ir = 1 / 128
ainv_qed_uv = 128 - 2 / (3 * pi) * LPT
S_qed = (ainv_qed_uv / 128) ** 3

nf, alpha_s_ir = 6, 0.0885
b0 = 11 - 2 * nf / 3
alpha_s_uv = 1 / (1 / alpha_s_ir + b0 / (2 * pi) * LPT)
qcd_rate = nf / 3 + 16 / 9
qcd_power = 2 * qcd_rate / b0
S_qcd = (alpha_s_uv / alpha_s_ir) ** qcd_power

print("Integrated suppressions M_Pl -> TeV:")
print(f"  QED Nf=1: alpha_UV={1/ainv_qed_uv:.8f}, S={S_qed:.6f}")
print(f"  QCD nf=6: alpha_s_UV={alpha_s_uv:.8f}, power={qcd_power:.8f}, S={S_qcd:.6f}")


# 3. Power-law exponents in the conventions used in E2.
def gny_z(n_dirac, epsilon=1):
    return (4 * n_dirac + 2 / 3) * epsilon / (2 * (2 * n_dirac + 3))


print("Power-law exponents:")
print(f"  GNY ND=1: {gny_z(1):.9f}; ND=2: {gny_z(2):.9f}")
print("  large-N singlet in d=3: 4-d = 1")
print(f"  QED3 nonsinglet N(two-component)=4: {64/(5*pi*pi*4):.9f}")
print(f"  GN nonsinglet N=4: {16/(15*pi*pi*4):.9f}")
print(f"  QED3 comparator in four-component convention: {32/(5*pi*pi*2):.9f}")


# 4. Photon-cone identity.  Expand the exact quadratic-form result to first
# order in the bare split eps, keeping the matter speed equal to one.
eps, e0sq, X = sp.symbols("eps e0sq X", positive=True)
c0 = 1 + eps
a = 1 / (e0sq * c0) + X
b = c0 / e0sq + X
cg_exact = sp.sqrt(b / a)
linear_photon_factor = sp.simplify(sp.diff(cg_exact, eps).subs(eps, 0))
print("Photon-cone identity:")
print("  d(c_gamma)/d(eps) at eps=0 =", linear_photon_factor)
print("  e_IR^2/e_UV^2 =", sp.simplify(1 / (1 + e0sq * X)))


def photon_scan(kind, per_species, p1, alpha_max):
    best = (1.0, None, None)
    for n_species in range(1, 4000):
        ainv_uv = 128 - per_species * n_species * LPT
        if ainv_uv < 1 / alpha_max:
            break
        suppression = (ainv_uv / 128) ** (1 + p1 / n_species)
        if suppression < best[0]:
            best = (suppression, n_species, 1 / ainv_uv)
    print(
        f"  {kind}, alpha_UV<={alpha_max:.6g}: "
        f"S_min={best[0]:.6e}, N={best[1]}, alpha_UV={best[2]:.6f}"
    )


photon_scan("Dirac", 2 / (3 * pi), 2, 1)
photon_scan("scalar", 1 / (6 * pi), 6, 1)
photon_scan("scalar", 1 / (6 * pi), 6, 4 * pi)


# 5. Bound arithmetic.  These are conditional on the bound values supplied
# to E2; only the LHAASO number was independently established by the F2 referee.
d0 = 8.55e-3
bounds = (
    ("LHAASO", 2.66e-19, 1.4e6),
    ("neutrino", 1.0e-20, 1.0e6),
    ("UHECR", 4.4e-23, 1.0e11),
)
print("Required power laws (conditional on quoted bounds):")
for label, bound, energy in bounds:
    decades = log10(MPL / energy)
    z_required = log10(d0 / bound) / decades
    ainv_uv_at_energy = 128 - 2 / (3 * pi) * log(MPL / energy)
    qed_value = d0 * (ainv_uv_at_energy / 128) ** 3
    print(
        f"  {label}: decades={decades:.6f}, z={z_required:.6f}, "
        f"QED-evolved split={qed_value:.6e}, miss={qed_value/bound:.6e}"
    )


# 6. Graviton dimensional arithmetic.  These numbers do not prove that the
# relevant operator is nonzero or that the model-profile estimate is universal.
print("Graviton dimensional arithmetic:")
print(f"  growth of (m/E)^2 to TeV = {(MPL/TEV)**2:.6e}")
for z in (0, 2):
    print(f"  assumed shell-profile share below Lambda/10, z={z}: {0.1**(4+z):.6e}")
for ndof in (100, 1000):
    rate = ndof / (192 * pi**2)
    print(f"  Sakharov estimate Ndof={ndof}: integrated rate={rate:.6f}, exp(-rate)={sp.N(sp.exp(-rate), 8)}")
