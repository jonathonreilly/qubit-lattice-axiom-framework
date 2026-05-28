#!/usr/bin/env python3
"""
First-principles probe (part 2): what FORCES the charged-lepton packet
to Q = 2/3 ?  Searches for a native variational / balance principle on
A1 (qubit, the "2") + A2 (Z^3, the "3"), tested numerically.

Key reformulation found here (verified, not imported):
  Define p_k = sqrt(m_k) / sum_j sqrt(m_j)   (a probability vector on the
  d generations).  Then

      Q = sum_k m_k / (sum_k sqrt(m_k))^2 = sum_k p_k^2

  so Q is EXACTLY the purity / inverse-participation-ratio (Simpson
  index) of the sqrt-mass distribution p.  Hence:

    * Q in [1/d, 1]; Q = 1/d  <=> p uniform (all generations equal,
      i.e. the Z_d-democratic / tracial reference packet);
      Q = 1  <=> p a delta (one generation).
    * n_eff := 1/Q = participation number = "effective # of mass states".
    * Q = 2/3  <=>  n_eff = 3/2 = d / 2 = (Z^3 dim) / (qubit dim).

Two independent native balance principles are tested for whether they
single out 2/3, and (crucially) shown to COINCIDE only at d = 3.
"""

import math
from itertools import product


def koide_Q(masses):
    s = [math.sqrt(m) for m in masses]
    return sum(masses) / (sum(s) ** 2)


def Q_from_p(p):
    """p a probability vector (sum=1, p_k>=0): Q = sum p_k^2 (purity)."""
    return sum(x * x for x in p)


def report(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


def main():
    # ---- (I) Q is the purity of the sqrt-mass distribution -----------
    report("(I) IDENTITY  Q = purity of sqrt-mass distribution p_k")
    M = [0.51099895, 105.6583755, 1776.86]
    s = [math.sqrt(m) for m in M]
    Z = sum(s)
    p = [x / Z for x in s]
    print(f"  p (sqrt-mass fractions) = "
          f"[{p[0]:.5f}, {p[1]:.5f}, {p[2]:.5f}]  sum={sum(p):.5f}")
    print(f"  purity sum p_k^2        = {Q_from_p(p):.8f}")
    print(f"  Koide Q                 = {koide_Q(M):.8f}   (identical)")
    print(f"  n_eff = 1/Q             = {1/koide_Q(M):.6f}   (target 3/2)")
    print("  => Q is literally the purity / inverse participation ratio.")
    print("  => n_eff = 3/2 = (#generations d=3) / (qubit dim = 2).")

    # ---- (II) range endpoints = native reference states --------------
    report("(II) RANGE  Q in [1/d, 1]: endpoints are the two A1+A2 limits")
    for d in [2, 3, 4]:
        uniform = [1.0 / d] * d
        delta = [1.0] + [0.0] * (d - 1)
        print(f"  d={d}:  Q_min (uniform/tracial)={Q_from_p(uniform):.6f}"
              f"   Q_max (single gen)={Q_from_p(delta):.6f}")
    print("  Q_min = 1/d : Z_d-democratic packet = diagonal of tracial ref.")
    print("  Q_max = 1   : one generation = maximal symmetry breaking.")

    # ---- (III) two balance principles, and d=3 coincidence -----------
    report("(III) TWO NATIVE BALANCE PRINCIPLES -- coincide ONLY at d=3")
    print("  P_equi : equipartition (mean-mode power = fluctuation power)")
    print("           => cos^2 theta = 1/2 => Q_equi = 2/d")
    print("  P_mid  : arithmetic midpoint of allowed range [1/d, 1]")
    print("           => Q_mid = (1/d + 1)/2 = (1+d)/(2d)")
    print()
    print("   d |  Q_equi=2/d |  Q_mid=(1+d)/2d |  agree?")
    for d in [2, 3, 4, 5, 6]:
        q_equi = 2.0 / d
        q_mid = (1.0 + d) / (2.0 * d)
        agree = "YES <==" if abs(q_equi - q_mid) < 1e-12 else "no"
        print(f"   {d} |   {q_equi:.6f}  |    {q_mid:.6f}    |  {agree}")
    print("  Algebra: 2/d = (1+d)/(2d)  <=>  4 = 1+d  <=>  d = 3 (unique).")
    print("  => The two independent balance principles AGREE only for d=3,")
    print("     and their common value is exactly 2/3.")

    # ---- (IV) honesty check: Q is NOT a free extremum ----------------
    report("(IV) HONESTY -- Q is NOT a free extremum (it is a balance pt)")
    # scan Z_3-symmetric family s_k = 1 + r cos(2pi k/3), r in [0,2]
    print("  Free extrema of Q over the positivity cone are the ENDPOINTS")
    print("  Q=1/3 (r=0) and Q=1 (r->2). 2/3 is interior => needs a")
    print("  selection principle, not free optimization of Q itself.")
    best = (None, -1)
    worst = (None, 2)
    for i in range(0, 2001):
        r = 2.0 * i / 2000.0
        sk = [1 + r * math.cos(2 * math.pi * k / 3) for k in range(3)]
        if any(x < 0 for x in sk):
            continue
        q = sum(x * x for x in sk) / (sum(sk) ** 2)
        if q > best[1]:
            best = (r, q)
        if q < worst[1]:
            worst = (r, q)
    print(f"  scan: Q_min={worst[1]:.5f} at r={worst[0]:.3f};"
          f"  Q_max={best[1]:.5f} at r={best[0]:.3f}")

    # ---- (V) the balance point as a fixed/critical relation ----------
    report("(V) BALANCE POINT as 'one qubit of distinguishability'")
    print("  n_eff = 1/Q. Q=2/3 => n_eff = 3/2.")
    print("  log2(n_eff) = log2(3/2) = "
          f"{math.log2(1.5):.6f} bits (sub-1-bit), while")
    print("  the FULL range gives log2 of effective states between")
    print(f"  log2(1)=0 (one gen) and log2(3)={math.log2(3):.4f} (democratic).")
    print("  Midpoint-in-Q  <=>  n_eff = d/2: the participation number is")
    print("  the generation count divided by the qubit dimension. The '2'")
    print("  is A1's qubit dimension; the '3' is A2's lattice dimension.")

    # ---- (VII) A1 FORCING: pure-qubit identity/Pauli HS equipartition --
    report("(VII) A1 FORCES EQUIPARTITION via PURE-STATE qubit purity")
    print("  A1: per-site state is a qubit  rho = (I + n.sigma)/2.")
    print("  Hilbert-Schmidt split:  Tr(rho^2) = Tr((I/2)^2) + Tr(((n.s)/2)^2)")
    print("                                    = 1/2          + |n|^2 / 2")
    for nmag in [0.0, 0.5, 1.0]:
        trace_part = 0.5
        pauli_part = nmag * nmag / 2.0
        purity = trace_part + pauli_part
        eq = "EQUIPARTITION" if abs(trace_part - pauli_part) < 1e-12 else ""
        print(f"   |n|={nmag:.1f}: HS(identity)={trace_part:.3f}  "
              f"HS(Pauli/fluct)={pauli_part:.3f}  Tr(rho^2)={purity:.3f}  {eq}")
    print("  => |n|=1 (PURE state) <=> identity-power = Pauli-power = 1/2.")
    print("  => A pure qubit has EQUAL democratic vs fluctuation HS-power.")
    print("  CLAIM: the charged-lepton sqrt-mass packet inherits this")
    print("  identity/Pauli split (democratic-mode power = fluctuation-mode")
    print("  power) BECAUSE a persistent particle is a PURE qubit excitation")
    print("  (|n|=1), not a mixed one. That is exactly cos^2 theta = 1/2,")
    print("  hence Q = 2/d, and with d=3 (A2 / Cl(3)), Q = 2/3.")
    print("  [This identification is the WEAKEST LINK -- see derivation note.]")

    # ---- (VI) novel prediction probe: d=4 would break consistency ----
    report("(VI) NOVEL PREDICTION -- exactly 3 Koide-coherent generations")
    print("  If a charged-fermion Z_d-democratic packet must satisfy BOTH")
    print("  balance principles (equipartition AND range-midpoint), then")
    print("  consistency REQUIRES d=3:")
    for d in [3, 4]:
        q_equi, q_mid = 2.0 / d, (1.0 + d) / (2.0 * d)
        print(f"    d={d}: Q_equi={q_equi:.4f} vs Q_mid={q_mid:.4f}"
              f"  -> {'consistent' if abs(q_equi-q_mid)<1e-9 else 'INCONSISTENT'}")
    print("  PREDICTION: no 4th charged-lepton generation can form a")
    print("  Koide-coherent triple at Q=2/3; the d=3 selection is a")
    print("  consistency condition of the two balance principles.")


if __name__ == "__main__":
    main()
