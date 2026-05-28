#!/usr/bin/env python3
"""
First-principles probe: Koide ratio Q = 2/3 for charged leptons.

Goal: starting ONLY from the framework axioms
  A1: per-site qubit, local algebra M_2(C) = Cl(3,0)   (the "2")
  A2: lattice sites form Z^3                            (the "3")
identify what forces the charged-lepton sqrt-mass packet to sit at
the extremal/constraint value Q = 2/3, WITHOUT assuming 2/3 as a target.

This script does NOT read prior Koide work. It establishes from scratch:
  (1) the empirical value of Q from PDG charged-lepton masses,
  (2) the exact geometric reformulations of "Q = 2/3",
  (3) the Z_3-Fourier (generation) decomposition and the equipartition
      reading,
  (4) the general dimension-d formula Q = 2/d and why d=3,
  (5) candidate native variational principles that single out Q = 2/3,
      tested numerically.

Pure-stdlib (math only). No numpy dependency required.
"""

import math
import cmath

# ----------------------------------------------------------------------
# (1) Empirical anchor: PDG charged-lepton masses (MeV). For reference
#     only -- the derivation does not use these values, only checks
#     against them at the end.
# ----------------------------------------------------------------------
M_E = 0.51099895000      # electron, MeV
M_MU = 105.6583755       # muon, MeV
M_TAU = 1776.86          # tau, MeV


def koide_Q(masses):
    """Q = sum(m_i) / (sum sqrt(m_i))^2."""
    s = [math.sqrt(m) for m in masses]
    return sum(masses) / (sum(s) ** 2)


def report(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ----------------------------------------------------------------------
# (2) Geometric reformulation.
#     Let s_i = sqrt(m_i) >= 0, s = (s_1,s_2,s_3) in R^3, 1 = (1,1,1).
#     Q = |s|^2 / (s . 1)^2.
#     With theta = angle(s, 1):  s.1 = |s| sqrt(d) cos(theta), d=3.
#     => Q = 1 / (d cos^2 theta).
#     "Q = 2/3"  <=>  cos^2 theta = 1/2  <=>  theta = 45 deg.
# ----------------------------------------------------------------------
def geometric_facts(masses):
    s = [math.sqrt(m) for m in masses]
    d = len(s)
    norm_s2 = sum(x * x for x in s)
    dot_s1 = sum(s)
    cos2 = (dot_s1 ** 2) / (d * norm_s2)
    theta_deg = math.degrees(math.acos(math.sqrt(cos2)))
    Q = norm_s2 / (dot_s1 ** 2)
    # decomposition into democratic (parallel to 1) + traceless parts
    mean = dot_s1 / d
    s_par = [mean] * d
    s_perp = [s[i] - mean for i in range(d)]
    norm_par2 = sum(x * x for x in s_par)
    norm_perp2 = sum(x * x for x in s_perp)
    return {
        "d": d, "Q": Q, "cos2theta": cos2, "theta_deg": theta_deg,
        "norm_par2": norm_par2, "norm_perp2": norm_perp2,
        "perp_over_par": norm_perp2 / norm_par2,
        "Q_from_cos2": 1.0 / (d * cos2),
    }


# ----------------------------------------------------------------------
# (3) Z_3-Fourier (generation) decomposition.
#     The three generations carry a natural Z_3 label (cube roots of 1).
#     Write the packet as a function on Z_3 and Fourier-transform:
#       s_k = A * (1 + r cos(delta + 2 pi k/3)),  k=0,1,2.
#     Then  sum s_k = 3A  (k=+-1 modes sum to 0),
#           sum s_k^2 = 3 A^2 (1 + r^2/2),
#       =>  Q = (1 + r^2/2)/3.
#     "Q = 2/3" <=> r^2 = 2 <=> r = sqrt(2).
#     Equipartition reading: power in k=0 (mean) mode = power in k=+-1
#     (fluctuation doublet) modes.
# ----------------------------------------------------------------------
def z3_fourier_packet(A, r, delta):
    return [A * (1.0 + r * math.cos(delta + 2.0 * math.pi * k / 3.0))
            for k in range(3)]


def z3_power_split(A, r, delta):
    """Returns (power_mean, power_fluct, Q, all_nonneg).

    The clean identity Q = (1 + r^2/2)/3 holds ONLY while every s_k >= 0,
    because the physical sqrt-mass is |s_k|. We therefore compute Q
    directly from the (signed) packet treated as sqrt-masses and flag
    when the non-negativity cone is exited."""
    s = z3_fourier_packet(A, r, delta)
    mean = sum(s) / 3.0
    power_mean = 3.0 * mean * mean            # k=0 mode power
    power_fluct = sum((x - mean) ** 2 for x in s)  # k=+-1 modes power
    all_nonneg = all(x >= 0 for x in s)
    # Q with s_k treated directly as sqrt-mass (exact when all_nonneg):
    Q_signed = sum(x * x for x in s) / (sum(s) ** 2)
    return power_mean, power_fluct, Q_signed, all_nonneg


# ----------------------------------------------------------------------
# (5a) Candidate native variational principle A: MAXIMUM ENTROPY of the
#      "amplitude distribution" p_i = s_i / sum(s_j) subject to a fixed
#      second-moment constraint? Test: does maximizing Shannon entropy
#      of p under the geometric constraint land on cos^2 = 1/2? (It does
#      NOT in general -- record the result honestly.)
#
# (5b) Candidate native variational principle B: the packet is a
#      *qubit-induced* 2-level object embedded in d=3 generation space.
#      A single qubit has a 2-dim state space; its expectation vector on
#      3 mutually unbiased / Z_3-symmetric axes saturates
#      |<sigma>|=1 (pure state) giving a fixed ratio. Test the
#      Bloch-vector construction below.
# ----------------------------------------------------------------------
def bloch_z3_projection():
    """
    Project a single pure-qubit Bloch vector onto three coplanar axes
    at 120 deg (Z_3-symmetric frame in the plane orthogonal to a fixed
    quantization axis). With an offset 'a' along the quantization axis
    (the trace/democratic part) and transverse magnitude 'b', the three
    'readings' are
        s_k = a + b cos(delta + 2 pi k /3).
    For a PURE qubit state the Bloch vector has unit length: a^2 + b^2 = 1
    (with a = cos(alpha), b = sin(alpha) the polar parametrization).
    Map a = A, b = A r  => r = b/a = tan(alpha).
    r = sqrt(2) <=> tan(alpha)=sqrt(2) <=> cos^2(alpha)=1/3, sin^2=2/3.
    i.e. the transverse (fluctuation) Bloch power is exactly TWICE the
    longitudinal -> Q=2/3. Report what pins alpha.
    """
    results = []
    for alpha_deg in [0, 30, 45, 54.7356, 60, 90]:
        alpha = math.radians(alpha_deg)
        a = math.cos(alpha)
        b = math.sin(alpha)
        if a == 0:
            continue
        r = b / a
        s = [a + b * math.cos(2.0 * math.pi * k / 3.0) for k in range(3)]
        if any(x < 0 for x in s):
            Q = None
        else:
            Q = koide_Q([x * x for x in s])
        results.append((alpha_deg, r, Q, a * a, b * b))
    return results


def main():
    report("(1) EMPIRICAL ANCHOR -- Q from PDG charged-lepton masses")
    Q_emp = koide_Q([M_E, M_MU, M_TAU])
    print(f"  m_e   = {M_E} MeV")
    print(f"  m_mu  = {M_MU} MeV")
    print(f"  m_tau = {M_TAU} MeV")
    print(f"  Q_empirical = {Q_emp:.8f}")
    print(f"  2/3         = {2/3:.8f}")
    print(f"  deviation   = {abs(Q_emp - 2/3)/(2/3)*100:.4f} %")

    report("(2) GEOMETRIC REFORMULATION -- Q = 1/(d cos^2 theta)")
    g = geometric_facts([M_E, M_MU, M_TAU])
    print(f"  d (generations)          = {g['d']}")
    print(f"  Q                        = {g['Q']:.8f}")
    print(f"  cos^2(theta)             = {g['cos2theta']:.8f}   (1/2 = {0.5})")
    print(f"  theta                    = {g['theta_deg']:.4f} deg  (45 deg target)")
    print(f"  Q from 1/(d cos^2)       = {g['Q_from_cos2']:.8f}  (consistency)")
    print(f"  |s_perp|^2 / |s_par|^2   = {g['perp_over_par']:.6f}   (1.0 = equipartition)")
    print("  => 'Q=2/3' is EXACTLY 'fluctuation power = mean power' (45 deg).")

    report("(3) Z_3-FOURIER PACKET -- Q = (1 + r^2/2)/3, r=sqrt(2) gives 2/3")
    print("  (delta=0, aligned with a generation, keeps the packet in the")
    print("   non-negativity cone for r<=2)")
    for r in [0.0, 1.0, math.sqrt(2), 2.0]:
        pm, pf, Q, ok = z3_power_split(1.0, r, 0.0)
        flag = "" if ok else "  <-- LEFT s>=0 CONE (Q invalid)"
        print(f"  r={r:6.4f}: power(mean)={pm:7.4f} power(fluct)={pf:7.4f} "
              f"ratio={pf/pm if pm else float('nan'):6.4f}  Q={Q:.6f}{flag}")
    print("  => r=sqrt(2) is precisely the equipartition point pf=pm, Q=2/3.")
    # delta-independence check WITHIN the non-negativity cone
    print("  Q vs Z_3 phase delta at r=sqrt(2) (only delta keeping s>=0 are exact):")
    for d in [0.0, 0.3, 0.6, 1.047]:  # 1.047 ~ pi/3
        pm, pf, Q, ok = z3_power_split(1.0, math.sqrt(2), d)
        flag = "exact (s>=0)" if ok else "OUTSIDE cone -> |s| used, not exact"
        print(f"    delta={d:.3f}: Q={Q:.6f}   [{flag}]")
    print("  => WITHIN the cone Q=2/3 exactly, independent of delta (Plancherel).")
    print("  => Non-negativity of sqrt-mass is a genuine constraint, not cosmetic.")

    report("(4) GENERAL DIMENSION -- equipartition gives Q = 2/d")
    print("  cos^2 theta = 1/2 (mean power = fluctuation power) =>")
    for d in [1, 2, 3, 4, 6]:
        print(f"    d={d}:  Q = 2/d = {2.0/d:.6f}")
    print("  d=3 (three generations from Z^3 / Cl(3)) => Q = 2/3.")
    print("  The '2' is the equipartition factor; need to pin it to A1.")

    report("(5b) QUBIT-BLOCH PROJECTION -- does A1 force the split?")
    print("  Pure-qubit Bloch vector (|n|=1) read on a Z_3 frame:")
    print("  alpha_deg |   r=b/a   |    Q     | a^2(long) | b^2(trans)")
    for alpha_deg, r, Q, a2, b2 in bloch_z3_projection():
        qs = f"{Q:.6f}" if Q is not None else "  (neg s) "
        print(f"   {alpha_deg:7.3f} | {r:8.5f} | {qs} | {a2:.5f}  | {b2:.5f}")
    print("  Note: Q=2/3 occurs at alpha=54.7356 deg = arccos(1/sqrt3),")
    print("  i.e. b^2 = 2/3, a^2 = 1/3: transverse Bloch power EXACTLY")
    print("  twice longitudinal. This is the tetrahedral / magic angle.")
    print("  WEAKEST LINK: what pins alpha to the magic angle? (see note)")


if __name__ == "__main__":
    main()
