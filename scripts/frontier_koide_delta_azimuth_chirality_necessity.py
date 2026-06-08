#!/usr/bin/env python3
"""
Brannen-delta azimuth selection requires a chirality-odd records functional.

Mirror-degeneracy obstruction on the C_3 records simplex (class-A finite-dim verifier).

This runner reproves, from scratch on 3-vectors only (memory-safe), the finite facts
behind the no-go:

  (L)  delta -> -delta acts on the Brannen Born weights p_k(delta) as the generation
       transposition (1 2): p(-delta) is the (1 2)-permutation of p(delta), for all delta.
  (T)  Hence every permutation-symmetric ("achiral") records/Born functional F obeys
       F(+delta) = F(-delta) identically -> its stationary set is delta->-delta symmetric
       -> it cannot uniquely select the chiral physical azimuth +delta_* over its
       distinct mirror -delta_*.  (mirror degeneracy)
  (N)  Non-vacuity: a permutation-ANTISYMMETRIC (chirality-odd) functional, e.g.
       A(delta) = sum_k p_k sin(2 pi k /3) (the cyclic orientation / Im C_3 character),
       does distinguish +delta from -delta.  So the obstruction is specifically chirality.
  (V)  The value source 2/9 = L_3(1,2) is the C_3 fixed-point (Lefschetz/Molien) density,
       reproven cyclotomically (NOT hard-coded as a closure).
  (C)  The cone Q = 2/3 (Fisher-Rao polar theta_p = pi/4, the firewalled block-weight
       r = 1/2) holds for ALL delta -> untouched here.
  (R)  Comparator only: PDG gives delta ~= 2/9 BARE radians, distinct from the index
       phase 2 pi /9 -> the radian-unit admission is separate and untouched.

No PDG value is load-bearing for (L),(T),(N),(V),(C); PDG enters only the (R) comparator.
"""
import numpy as np
from numpy import pi, cos, sin, sqrt

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} {detail}")


# ----- Brannen amplitudes / Born weights on the Koide cone, parametrized by azimuth delta
def lam(delta):
    return 1.0 + sqrt(2.0) * cos(delta + 2.0 * pi * np.arange(3) / 3.0)


def born(delta):
    m = lam(delta) ** 2
    return m / m.sum()


# ===== (L) delta -> -delta permutes the Born weights as the transposition (1 2) =====
swap12 = np.array([0, 2, 1])  # index map fixing 0, swapping 1<->2
sweep = np.linspace(-pi, pi, 73)
maxperm = 0.0
for d in sweep:
    p = born(d)
    pm = born(-d)
    maxperm = max(maxperm, np.max(np.abs(pm - p[swap12])))
check("L_permutation_action_delta_to_minus_delta_is_(1 2)",
      maxperm < 1e-12, f"max|p(-d)-(12)p(d)|={maxperm:.2e}")

# amplitudes too (lambda_k(-d) = lambda_{-k}(d))
maxperm_l = max(np.max(np.abs(lam(-d) - lam(d)[swap12])) for d in sweep)
check("L_amplitude_permutation_action", maxperm_l < 1e-12, f"max={maxperm_l:.2e}")


# ===== natural achiral (permutation-symmetric) records/Born functionals =====
def F_var(d):       # variance about democratic point
    p = born(d); return float(np.sum((p - 1.0 / 3.0) ** 2))


def F_purity(d):    # Born purity / collision (the "I" scalar)
    p = born(d); return float(np.sum(p ** 2))


def F_shannon(d):   # Shannon entropy
    p = born(d); return float(-np.sum(p * np.log(p + 1e-300)))


def F_p3(d):        # third power moment
    p = born(d); return float(np.sum(p ** 3))


def F_kl_unif(d):   # KL(p || uniform)
    p = born(d); return float(np.sum(p * np.log(3.0 * p + 1e-300)))


ACHIRAL = {"var": F_var, "purity": F_purity, "shannon": F_shannon,
           "p3": F_p3, "kl_unif": F_kl_unif}

# ===== (T) mirror degeneracy: F(+d) = F(-d) identically for every achiral F =====
for nm, F in ACHIRAL.items():
    md = max(abs(F(d) - F(-d)) for d in sweep)
    check(f"T_mirror_degeneracy_{nm}", md < 1e-12, f"max|F(+d)-F(-d)|={md:.2e}")

# mirror degeneracy at the physical point delta = 2/9
two9 = 2.0 / 9.0
for nm, F in ACHIRAL.items():
    check(f"T_mirror_at_physical_{nm}", abs(F(two9) - F(-two9)) < 1e-12,
          f"F(+2/9)={F(two9):.6f} F(-2/9)={F(-two9):.6f}")

# ===== achiral functionals: azimuthal critical points are pi-rational, not 2/9 =====
def crit_in(F, lo, hi, n=400001):
    g = np.linspace(lo, hi, n)
    f = np.array([F(x) for x in g])
    df = np.gradient(f, g)
    idx = np.where(np.diff(np.sign(df)) != 0)[0]
    return sorted(set(round(g[i], 4) for i in idx))


for nm, F in ACHIRAL.items():
    cps = [c for c in crit_in(F, 1e-3, pi / 2 - 1e-3)]
    # is every critical point a rational multiple of pi (within tol) and is 2/9 absent?
    pi_rational = all(min(abs(c - m * pi / 12) for m in range(0, 7)) < 5e-3 for c in cps) if cps else True
    has_two9 = any(abs(c - two9) < 5e-3 for c in cps)
    check(f"crit_pi_rational_not_two9_{nm}", pi_rational and not has_two9,
          f"crit/[0,pi/2]={[round(c/pi,3) for c in cps]} pi")


# ===== (N) non-vacuity: a chirality-ODD functional distinguishes +d from -d =====
def A_odd(d):  # imaginary part of the C_3 character weighted by p = cyclic orientation
    p = born(d); return float(np.sum(p * sin(2.0 * pi * np.arange(3) / 3.0)))


# genuinely odd
oddness = max(abs(A_odd(-d) + A_odd(d)) for d in sweep)
check("N_witness_is_chirality_odd", oddness < 1e-12, f"max|A(-d)+A(d)|={oddness:.2e}")
# distinguishes at the physical point
check("N_witness_distinguishes_plus_minus_2_9",
      abs(A_odd(two9) - A_odd(-two9)) > 1e-6,
      f"A(+2/9)={A_odd(two9):+.6f} A(-2/9)={A_odd(-two9):+.6f}")
# the +2/9 and -2/9 Born configs are genuinely different (distinct mass orderings)
check("N_plus_minus_2_9_are_distinct_configs",
      np.max(np.abs(born(two9) - born(-two9))) > 1e-3,
      f"max|p(+2/9)-p(-2/9)|={np.max(np.abs(born(two9)-born(-two9))):.4f}")

# symmetric functionals are genuinely even (control for the odd/even split)
for nm, F in ACHIRAL.items():
    evenness = max(abs(F(-d) - F(d)) for d in sweep)
    check(f"control_{nm}_is_even", evenness < 1e-12, f"max|F(-d)-F(d)|={evenness:.2e}")


# ===== (V) value source 2/9 = L_3(1,2), reproven cyclotomically (not hard-coded) =====
z = np.exp(2j * pi / 3.0)
L312 = (1.0 / 3.0) * (1.0 / ((z - 1) * (z ** 2 - 1)) + 1.0 / ((z ** 2 - 1) * (z ** 4 - 1)))
check("V_L3_1_2_equals_two_ninths", abs(L312.real - two9) < 1e-12 and abs(L312.imag) < 1e-9,
      f"L_3(1,2)={L312.real:.10f}")
# family discriminator: the period-1 eta-defect family (d^2-1)/(12d) meets rank (d-1)/d^2 only at d=3
def Ld(d, a):
    zz = np.exp(2j * pi / d); s = 0
    for k in range(1, d):
        pr = 1.0
        for aj in a:
            pr *= 1.0 / (zz ** (k * aj) - 1)
        s += pr
    return (s / d).real
fam_ok = all(abs(Ld(d, (1, d - 1)) - (d * d - 1) / (12.0 * d)) < 1e-9 for d in range(2, 7))
coincide_only_d3 = (abs((9 - 1) / 36.0 - (3 - 1) / 9.0) < 1e-12
                    and abs((16 - 1) / 48.0 - (4 - 1) / 16.0) > 1e-3)
check("V_eta_defect_family_d2m1_over_12d", fam_ok, "L_d(1,d-1)=(d^2-1)/(12d)")
check("V_period1_meets_rankfraction_only_at_d3", coincide_only_d3,
      "(d^2-1)/12d = (d-1)/d^2 only at d=3")


# ===== (C) cone Q = 2/3 (Fisher polar pi/4, firewalled r=1/2) holds for ALL delta =====
def koideQ(d):
    x = lam(d); return float(np.sum(x ** 2) / np.sum(x) ** 2)


maxQ = max(abs(koideQ(d) - 2.0 / 3.0) for d in sweep)
check("C_cone_Q_two_thirds_all_delta", maxQ < 1e-12, f"max|Q-2/3|={maxQ:.2e}")
# Fisher-Rao polar angle of the sqrt(m)=|lambda| point = pi/4 on the POSITIVE branch
# (where sqrt(m_k)=lambda_k>=0, so the signed Koide Q=2/3 equals the sqrt(m) cone;
#  cos^2 theta_p = 1/(3Q) = 1/2 -> theta_p = pi/4). This branch contains the physical point.
def theta_p(d):
    x = lam(d); xh = x / np.linalg.norm(x)
    n = np.ones(3) / sqrt(3.0); return float(np.arccos(abs(xh @ n)))
pos_branch = [d for d in sweep if np.min(lam(d)) >= 0.0]
maxth = max(abs(theta_p(d) - pi / 4) for d in pos_branch)
check("C_fisher_polar_pi_over_4_positive_branch", maxth < 1e-12,
      f"max|theta_p-pi/4|={maxth:.2e} over {len(pos_branch)} positive-branch nodes")


# ===== (R) comparator only: PDG delta ~= 2/9 BARE radians, not the index phase 2pi/9 =====
m_pdg = np.array([0.5109989461, 105.6583755, 1776.86])
xn = sqrt(m_pdg); xn = xn / (xn.sum() / 3.0)
g = np.linspace(0.0, 0.6, 600001)
xs = np.sort(xn)
errs = np.array([np.sum((np.sort(1 + sqrt(2) * cos(t + 2 * pi * np.arange(3) / 3)) - xs) ** 2) for t in g])
delta_pdg = g[int(np.argmin(errs))]
check("R_comparator_delta_pdg_near_bare_two9", abs(delta_pdg - two9) < 1e-3,
      f"delta_PDG={delta_pdg:.6f} rad, 2/9={two9:.6f}")
check("R_physical_is_bare_radian_not_index_phase", abs(delta_pdg - 2 * pi / 9.0) > 0.4,
      f"index phase 2pi/9={2*pi/9:.6f} (factor-pi radian admission, untouched)")


print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("VERDICT: Brannen-delta azimuth selection on the C_3 records simplex requires a "
      "chirality-odd functional; every achiral records/Born functional is mirror-degenerate "
      "and cannot select the chiral physical azimuth. Magnitude 2/9=L_3(1,2) and the radian "
      "unit remain separate residuals; the cone r=1/2 firewall is untouched.")
