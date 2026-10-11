"""Independent arithmetic and representation checks for C4/RE/E1.

This does not import the worker's modules.  In particular, the cubic-singlet
count is obtained from the action of the 24 signed-permutation rotations on
homogeneous polynomials, followed by P_l = H_l (+) r^2 P_{l-2}; it does not
use the worker's SO(3)-character formula.
"""

from fractions import Fraction
from itertools import permutations, product
from math import log, pi


def parity(perm):
    return -1 if sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1


rotations = []
for perm in permutations(range(3)):
    for signs in product((-1, 1), repeat=3):
        if parity(perm) * signs[0] * signs[1] * signs[2] == 1:
            rotations.append((perm, signs))
assert len(rotations) == 24


def monomials(degree):
    return [(a, b, degree - a - b) for a in range(degree + 1) for b in range(degree - a + 1)]


def polynomial_invariants(degree):
    """Trace of the exact group projector on homogeneous degree-l polynomials."""
    trace_sum = 0
    for perm, signs in rotations:
        for powers in monomials(degree):
            image = [0, 0, 0]
            phase = 1
            for source_axis, power in enumerate(powers):
                target_axis = perm[source_axis]
                image[target_axis] += power
                phase *= signs[source_axis] ** power
            if tuple(image) == powers:
                trace_sum += phase
    return Fraction(trace_sum, len(rotations))


poly = [polynomial_invariants(l) for l in range(13)]
harmonic = [poly[l] - (poly[l - 2] if l >= 2 else 0) for l in range(13)]
print("1 cubic O singlets in harmonic spin l=0..12:", [int(x) for x in harmonic])
print("  first non-scalar cubic singlet: l=4; none at l=1,2,3")
print("  4D primary floors: vector 3; symmetric spin-2 4; symmetric spin-3 5; chiral spin-4 5; symmetric spin-4 6")


# Direct first derivatives of the published Anber-Donoghue beta functions at
# c_b=c_f=c_g=1.  Coefficients shown multiply coupling^2 * eta / pi^2.
y_b = Fraction(1, 4)
y_f = -Fraction(1, 24)
q_g = Fraction(1, 6)
q_f = -Fraction(1, 3)
print("2 AD Yukawa linear coefficients (beta_b,beta_f):", y_b, y_f)
print("  CT-weighted sum (1,6):", y_b + 6 * y_f, "; relative rate:", y_b - y_f, "g^2/pi^2")
print("  AD QED linear coefficients (beta_gamma,beta_f):", q_g, q_f)
print("  CT-weighted sum (12,6):", 12 * q_g + 6 * q_f, "; relative rate:", q_g - q_f, "e^2/pi^2")


# Independent n=2 splitting-function moments.  For d/dln(mu^2), the two
# off-diagonal momentum-transfer moments are integral z P_gq = 16/9 and
# 2*n_f integral z P_qg = n_f/3.  Converting to d/dln(mu) and alpha/(4*pi)
# multiplies the nonzero eigenvalue by four.
p_gq = Fraction(16, 9)
print("3 DGLAP n=2 off-diagonal moments: g<-q =", p_gq, "; q<-g = n_f/3")


def lam_singlet(nf):
    return 4 * (p_gq + Fraction(nf, 3))


def beta0_qcd(nf):
    return 11 - Fraction(2 * nf, 3)


nf = 6
lam = lam_singlet(nf)
b0 = beta0_qcd(nf)
d_singlet = lam / (2 * b0)
d_nonsinglet = Fraction(64, 9) / (2 * b0)
mpl = 1.22e19
alpha_tev = 0.0884
alpha_pl = 1 / (1 / alpha_tev + float(b0) / (2 * pi) * log(mpl / 1e3))
ratio_alpha = alpha_pl / alpha_tev
print("  lambda_singlet(n_f=6) =", lam, "; exponents singlet/non-singlet =", float(d_singlet), float(d_nonsinglet))
print("  alpha_s(M_Pl), singlet factor, flavor-nonsinglet factor =", f"{alpha_pl:.6f}", f"{ratio_alpha**float(d_singlet):.6f}", f"{ratio_alpha**float(d_nonsinglet):.6f}")


inv_alpha_low = 137.036
inv_alpha_high = inv_alpha_low - 2 / (3 * pi) * log(mpl / 0.000511)
qed_factor = (inv_alpha_high / inv_alpha_low) ** 3
print("  electron-only QED: 1/alpha(M_Pl), factor =", f"{inv_alpha_high:.6f}", f"{qed_factor:.6f}")
gamma_cap = float(lam) * 0.09 / (4 * pi)
print("  instantaneous singlet gamma at alpha_s=0.09 =", f"{gamma_cap:.6f}")


bounds = {"e/gamma": 2.7e-19, "nu": 1e-20, "p/gamma": 4e-23}
print("4 gamma required for delta0=1 at Lambda_s=1,10,100 TeV:")
for ls in (1e3, 1e4, 1e5):
    vals = {name: log(bound) / log(ls / mpl) for name, bound in bounds.items()}
    print(" ", f"{ls/1e3:.0f} TeV", " ".join(f"{name}={value:.4f}" for name, value in vals.items()))
high_energy = ((1.4e6, 2.7e-19), (1e11, 4.4e-23), (1e11, 9e-13))
print("  above-exit exponents (PeV gamma, proton Cherenkov, proton lattice-sign):", [round(log(b) / log(e / mpl), 4) for e, b in high_energy])
uhe_gamma2 = (1e11 / mpl) ** 2
print("  gamma=2 at 1e20 eV:", f"{uhe_gamma2:.6e}", "; ratio to 4.4e-23 bound:", f"{uhe_gamma2/4.4e-23:.6e}")


print("5 shell ansatz ratios, integral E^3 eta / integral E^3:")
for gamma in (0.7, 1, 2):
    print(" ", gamma, "->", f"{4/(4+gamma):.9f}", "; kinetic analogue", f"{2/(2+gamma):.9f}")
print("  These ratios follow only after assuming eta(E)=(E/Lambda)^gamma and a shell response linear in eta with no cancellations.")


mg = 1.3e-23
mbar = 2.435e27
mu_naive = (mg * mbar) ** 2
print("6 naive mu=(m_g Mbar_Pl)^2:", f"{mu_naive:.6e}", "eV^4; fourth root", f"{mu_naive**0.25:.3f}", "eV")
print("  PRICE_NOTE's refereed channel normalization instead quotes 2.39e8 eV^4 = (124 eV)^4.")
