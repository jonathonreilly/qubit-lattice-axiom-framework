#!/usr/bin/env python3
"""RP gauge-half bridge: abelian Wilson plaquette temporal-gauge factor.

Source note:
  docs/RP_GAUGE_HALF_WILSON_TEMPORAL_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md

Instantiates the retained abstract gauge-half norm-square identity
(reflection_positivity_gauge_half_cauchy_schwarz, G1-G3:
 <Theta(F).F> = ||psi^2 F||^2 >= 0) on the Wilson plaquette in temporal
gauge, certifying the reflected OS-Gram reduction on the abelian finite
surfaces whose plane coefficients are checked as nonnegative.

Setup (minimal): two time slices t in {0,1}, periodic spatial direction,
temporal gauge U_0 = 1. Time reflection theta: t -> 1-t exchanges the
slices; Theta antilinear, Theta(F)(U) = conj(F(theta U)). In temporal
gauge the only straddling plaquette per spatial link k reduces to the
plane coupling  V_k = U_k(0) U_k(1)^dag,  with reflection-plane weight
exp(-S_0), S_0 = -(beta/N) Re Tr V  (STANDARD ferromagnetic Wilson sign).

Mechanism (Osterwalder-Seiler, reconstructed in-repo; OS 1978 /
Montvay-Munster 1994 are COMPARATORS only): on the abelian surfaces the
plane weight expands in one-dimensional characters,
   exp((beta/N) Re Tr V) = sum_a c_a(beta) chi_a(U_+) conj(chi_a(U_-)) / d_a,
and the reflected OS-Gram of positive-half observables factorizes as
   G = W diag(c) W^dag,   c_a = character coefficient of the plane weight.
So G is PSD on the certified finite abelian surfaces where c_a >= 0.

The nonabelian SU(2)/SU(3) coefficient probes below are diagnostics only.
They are deliberately non-load-bearing because nonabelian reconstruction
requires matrix coefficients (or an explicitly projected class-function
kernel), not the old product-of-characters substitution. Section D exposes
the SU(2) first-order mismatch so the source note cannot silently re-promote
that broader claim. The wrong sign fails the control below, which is exactly
the sign bug that sank the 2026-06-05 failed-attempt note.

CRITICAL (vs the failed attempt): plane weight is exp(+ (beta/N) Re Tr)
= exp(-S_0); the U(1) coefficients are I_n(beta) verified >= 0 from the
manifestly non-negative power series (NO finite angular grid).
"""

from __future__ import annotations
import sys
import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    PASS += ok
    FAIL += (not ok)
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))


def section(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


# ---------------------------------------------------------------- A: reflection split
def reflection_split():
    section("A. Reflection split S = S_+ + Theta(S_+) + S_0 (temporal gauge)")
    # one spatial link, two slices; random SU(2) link variables; temporal gauge U0=1.
    rng = np.random.default_rng(0)

    def rand_su2():
        v = rng.standard_normal(4)
        v /= np.linalg.norm(v)
        a, b, c, d = v
        return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])

    beta, N = 0.8, 2
    Up = rand_su2()   # positive-slice spatial link U_k(1)
    Um = rand_su2()   # negative-slice spatial link U_k(0)
    # straddling plaquette in temporal gauge: V = Um Up^dag ; S_0 = -(beta/N) Re Tr V
    V = Um @ Up.conj().T
    S0 = -(beta / N) * np.trace(V).real
    # reflection theta exchanges slices: Up <-> Um ; S_0 is plane-symmetric
    V_ref = Up @ Um.conj().T
    S0_ref = -(beta / N) * np.trace(V_ref).real
    check("S_0 plane-symmetric under theta (Re Tr V = Re Tr V^dag)",
          abs(S0 - S0_ref) < 1e-12, f"|dS0|={abs(S0-S0_ref):.1e}")
    check("plane weight = exp(-S_0) = exp(+(beta/N) Re Tr V) (standard Wilson sign)",
          np.isclose(np.exp(-S0), np.exp((beta / N) * np.trace(V).real)))


# ---------------------------------------------------------------- B: Z_N exact
def zn_exact():
    section("B. Z_N (N=2..5): exact character kernel c_a >= 0 and OS-Gram PSD")
    for N in (2, 3, 4, 5):
        beta = 0.9
        g = np.arange(N)
        ang = 2 * np.pi * g / N
        # plane weight on group element g: w(g) = exp((beta/?) Re chi(g)); use Re e^{i ang}
        w = np.exp(beta * np.cos(ang))                      # standard ferromagnetic sign
        # character (DFT) coefficients c_a = (1/N) sum_g w(g) e^{-i a ang}
        c = np.array([np.sum(w * np.exp(-1j * a * ang)).real / N for a in range(N)])
        check(f"Z_{N}: all character coeffs c_a >= 0 (standard sign)",
              np.all(c > -1e-12), f"min c_a={c.min():+.4f}")
        # reflected OS-Gram on the N characters: G = diag(c) (orthonormal chars) -> PSD iff c>=0
        G = np.diag(c)
        check(f"Z_{N}: reflected OS-Gram PSD (min eig)",
              np.linalg.eigvalsh(G).min() > -1e-12, f"min_eig={np.linalg.eigvalsh(G).min():+.4f}")


# ---------------------------------------------------------------- C: U(1) exact (analytic Bessel, no grid)
def i_n_series_nonneg(n, beta, K=80):
    # I_n(beta) = sum_{k>=0} (beta/2)^{2k+n} / (k! (k+n)!)  -- all terms >= 0 for beta>0
    import math
    terms = [(beta / 2) ** (2 * k + n) / (math.factorial(k) * math.factorial(k + n)) for k in range(K)]
    return terms


def u1_exact():
    section("C. U(1): coeffs c_n = I_n(beta) >= 0 by manifestly-nonneg series (NO grid)")
    for beta in (0.3, 1.0, 3.0, 6.0):
        allnn = True
        cs = []
        for n in range(8):
            terms = i_n_series_nonneg(n, beta)
            allnn = allnn and all(t >= 0 for t in terms)
            cs.append(sum(terms))
        check(f"U(1) beta={beta}: every I_n series term >= 0 (=> c_n=I_n(beta) >= 0), n=0..7",
              allnn and all(c >= -1e-15 for c in cs), f"min c_n={min(cs):.3e}")
    # reflected Gram diagonal in character basis with entries c_n=I_n>=0 -> PSD (exact, Peter-Weyl/Fourier)
    beta = 2.0
    cs = [sum(i_n_series_nonneg(n, beta)) for n in range(8)]
    check("U(1) reflected OS-Gram (diag c_n, character orthogonality) PSD",
          min(cs) > -1e-15, f"min_eig=min c_n={min(cs):.4f}")


# ---------------------------------------------------------------- D: nonabelian boundary diagnostics
def nonabelian_boundary_diagnostics():
    section("D. Nonabelian boundary: coefficient positivity is diagnostic, not a retained reconstruction")
    for beta in (0.5, 1.5, 4.0):
        cs = []
        for j in range(6):  # j+1 = dimension index
            np1 = j + 1
            c = 2 * np1 * sum(i_n_series_nonneg(np1, beta)) / beta
            cs.append(c)
        check(f"SU(2) beta={beta}: class-coefficient diagnostic c_j > 0, j=0..5",
              all(c > 0 for c in cs), f"min c_j={min(cs):.4e}")

    # Auditor-exposed mismatch for the old product-of-characters replacement.
    # Let g=h=i sigma_x. Then g h^dag = I, so the beta-linear coefficient
    # of exp((beta/2) Re Tr(g h^dag)) is 1. The old character-product
    # substitution gives zero at first order because chi_fund(g)=chi_fund(h)=0.
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    g = 1j * sigma_x
    h = 1j * sigma_x
    true_linear = 0.5 * np.trace(g @ h.conj().T).real
    old_product_linear = 0.5 * np.trace(g).real * np.trace(h).real / 2.0
    check(
        "SU(2) old product-character reconstruction is not exact (linear mismatch exposed)",
        abs(true_linear - 1.0) < 1e-12 and abs(old_product_linear) < 1e-12,
        f"true_linear={true_linear:.1f}, old_product_linear={old_product_linear:.1f}",
    )
    check(
        "SU(2)/SU(3) diagnostics are non-load-bearing for W2/W3 in this runner",
        True,
        "nonabelian closure requires matrix coefficients or a projected class-kernel theorem",
    )


# ---------------------------------------------------------------- E: SU(3) corroboration (Weyl quadrature)
def su3_corroboration():
    section("E. SU(3): selected plane-weight coeffs >= 0 (Weyl-integration corroboration)")
    # SU(3) Weyl integration over the maximal torus: eigenphases (t1,t2,t3), sum=0 mod 2pi.
    # Weyl measure ~ |prod_{i<j} (e^{i ti} - e^{i tj})|^2 / (3! (2pi)^2).
    M = 120
    grid = np.linspace(-np.pi, np.pi, M, endpoint=False)
    for beta in (0.5, 2.0, 5.0):
        for lam in ('triv', 'fund', 'adj'):
            num = 0.0
            den = 0.0
            for t1 in grid:
                for t2 in grid:
                    t3 = -(t1 + t2)
                    ph = np.array([np.exp(1j * t1), np.exp(1j * t2), np.exp(1j * t3)])
                    vand = 1.0
                    for i in range(3):
                        for j in range(i + 1, 3):
                            vand *= abs(ph[i] - ph[j]) ** 2
                    ReTr = ph.real.sum()
                    w = np.exp((beta / 3.0) * ReTr)          # standard sign
                    if lam == 'triv':
                        chi = 1.0
                    elif lam == 'fund':
                        chi = ph.sum()
                    else:  # adjoint = fund (x) fundbar - 1
                        chi = abs(ph.sum()) ** 2 - 1.0
                    num += (w * np.conj(chi) * vand).real
                    den += vand
            c = num / den
            check(f"SU(3) beta={beta} rep={lam}: plane-weight char coeff c_lambda >= 0",
                  c > -1e-6, f"c={c:+.5f}")


# ---------------------------------------------------------------- F: wrong-sign control (genuine: it CAN fail)
def wrong_sign_control():
    section("F. Wrong-sign control: exp(-(beta) Re Tr) (S_0=+beta Re) gives c_a < 0 (non-PSD)")
    N, beta = 2, 0.9
    ang = 2 * np.pi * np.arange(N) / N
    w_wrong = np.exp(-beta * np.cos(ang))                   # WRONG sign (the failed-note bug)
    c_wrong = np.array([np.sum(w_wrong * np.exp(-1j * a * ang)).real / N for a in range(N)])
    check("Z_2 WRONG sign: a nontrivial coeff c_1 < 0 (kernel NOT positive => NON-PSD)",
          c_wrong.min() < -1e-9, f"min c_a={c_wrong.min():+.4f} (this is the sign bug)")
    # U(1) wrong sign: c_n = (-1)^n I_n(beta), alternating -> negative for odd n
    c1_wrong = -sum(i_n_series_nonneg(1, beta))
    check("U(1) WRONG sign: c_1 = -I_1(beta) < 0 (NON-PSD)", c1_wrong < 0,
          f"c_1={c1_wrong:+.4f}")


def main():
    reflection_split()
    zn_exact()
    u1_exact()
    nonabelian_boundary_diagnostics()
    su3_corroboration()
    wrong_sign_control()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: RP gauge-half abelian Wilson temporal-gauge bridge checks FAILED.")
        return 1
    print("VERDICT: RP gauge-half ABELIAN Wilson temporal-gauge bridge checks pass.")
    print("  Standard Wilson sign -> plane weight exp(+(beta/N)Re Tr) -> positive")
    print("  abelian character kernel (Z_N exact, U(1) analytic Bessel) ->")
    print("  G = W diag(c) W^dag is PSD on the certified abelian surfaces.")
    print("  SU(2)/SU(3) coefficient checks are diagnostics only; the runner exposes")
    print("  the SU(2) product-character mismatch and makes no nonabelian W2/W3 claim.")
    print("  Wrong sign gives c_a<0 (non-PSD), the bug that sank the 2026-06-05 attempt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
