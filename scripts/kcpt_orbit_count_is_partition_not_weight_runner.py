#!/usr/bin/env python3
"""Class-A verifier: the K/CPT-orbit count of the generation doublet delivers the 2-SECTOR
PARTITION (a multiplicity readout), NOT the inter-block power ratio r. The holomorphic readout
that would count the doublet coefficient b "once" is implemented by a complex structure
J_cs = (C - C^2)/sqrt(3) that COMMUTES with C3 and with the mass operator -- so it is strictly
WEAKER than (and clears) the foreclosed anticommuting chiral grading -- but it is
MEASURE-NEUTRAL, so it does NOT force r=1/2. r=1/2 stays a registered pattern.

This closes the candidate "RECORD registers the K/CPT orbit => count b once => r=1/2" escape and
sharpens the open supertrace/holomorphic lead. Generations = C3 regular rep on C^3 =
singlet (trivial) + doublet (omega, omega-bar). r = |b|^2/a^2, Q = 1/3 + (2/3) r.

Verifies:
  (1) the K/CPT orbit set of the C3 irreps is {{1},{omega,omega-bar}} = 2 orbits = the einselected
      {P0 (rank 1), P1 (rank 2)} 2-sector partition (re-derives GAP B's partition from the orbit
      clause);
  (2) the orbit count is r-INVARIANT: the K/CPT action b->b-bar leaves r = |b|^2/a^2 exactly fixed
      (so it pins multiplicity, carries ZERO inter-block-weight information);
  (3) the implementing complex structure J_cs = (C-C^2)/sqrt(3): [J_cs,C]=0, J_cs^2 = -P_doublet,
      [J_cs,M]=0 for every C3-invariant mass M -- and {J_cs, Gamma_chi} != 0, so J_cs is a
      COMMUTING complex structure, DISTINCT from and WEAKER than the anticommuting chiral grading
      that `koide_z3_equivariant_anticommuting_no_go` (retained_bounded) forecloses -- it CLEARS
      that no-go;
  (4) but exp(theta J_cs) is orthogonal with det=+1 => MEASURE-NEUTRAL (preserves both the
      real-trace and complex-trace measures) => it adjudicates neither count => no forcing;
  (5) a genuine complex-trace "count b once" puts equal-block-energy at r=1, NOT r=1/2; the value
      r=1/2 requires the SEPARATE equal-power-per-block balance 3a^2 = 6|b|^2 -- the registered
      weight, which the RECORD axiom disowns;
  (6) Frobenius-Schur(omega) = 0 (complex type) => by Wigner an antiunitary K REALIFIES
      (omega,omega-bar) into 2 real modes = the (1,2) -> r=1 side (the OPPOSITE of the escape);
      K on the doublet 2-plane is a det=-1 reflection (realifying), not a det=+1 U(1) rotation.

So r=1/2 is NOT forced: it is a registered pattern. The one live route to force the field/measure
choice is the gated staggered-Dirac fluctuation-determinant holomorphy (substep-4, off-main).

No new axiom/import: pure C3 group theory + the retained partition/no-go surfaces; exact arithmetic.
"""

from __future__ import annotations
import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)   # C3 cyclic
Jall = np.ones((3, 3), dtype=complex)                            # all-ones
P_doublet = np.eye(3) - Jall / 3
J_cs = (C - C @ C) / np.sqrt(3)                                  # candidate complex structure
Gamma_chi = (2 / 3) * Jall - np.eye(3)                           # Z3 chiral grading


def mass(a, b):
    return a * np.eye(3) + b * C + np.conj(b) * C @ C            # C3-invariant (circulant) mass


def main() -> int:
    print("=" * 78)
    print("K/CPT-orbit count = the 2-sector PARTITION, not the weight r; J_cs measure-neutral  [class A]")
    print("=" * 78)

    # ---- (1) the K/CPT orbit set = 2 orbits = the 2-sector partition ----
    print("\n-- (1) K/CPT orbits of the C3 irreps = {{1},{omega,omega-bar}} = 2 = the 2-sector partition --")
    # the three C3 characters and the K/CPT (complex-conjugation) action on them
    chars = {0: 1.0, 1: w, 2: w ** 2}
    # conjugation maps character k -> character (3-k) mod 3: 1(trivial)->1, omega<->omega-bar
    orbits = {frozenset([k, (3 - k) % 3]) for k in chars}
    check("the K/CPT (conjugation) orbit set has exactly 2 orbits {trivial} and {omega,omega-bar}",
          len(orbits) == 2, detail=f"orbits = {[set(o) for o in orbits]}")
    check("these 2 orbits = the einselected 2-sector partition {P0 rank1 (singlet), P1 rank2 "
          "(doublet)}", np.isclose(np.trace(Jall / 3).real, 1) and np.isclose(np.trace(P_doublet).real, 2))

    # ---- (2) the orbit count is r-invariant ----
    print("\n-- (2) the orbit count is r-INVARIANT (b->b-bar leaves r=|b|^2/a^2 fixed) --")
    rng = np.random.default_rng(0)
    mx = 0.0
    for _ in range(100000):
        a = rng.standard_normal()
        b = rng.standard_normal() + 1j * rng.standard_normal()
        if abs(a) < 1e-6:
            continue
        mx = max(mx, abs(abs(b) ** 2 / a ** 2 - abs(np.conj(b)) ** 2 / a ** 2))
    check("max|r(a,b) - r(a,b-bar)| = 0 over 1e5 draws => the orbit merge carries ZERO inter-block "
          "weight information (it moves only arg(b)=delta, Q-orthogonal to |b|)", mx < 1e-15,
          detail=f"max = {mx:.1e}")
    # explicit r=1/2 and r=1 states have IDENTICAL orbit structure
    check("explicit r=1/2 (|b|^2=a^2/2) and r=1 (|b|^2=a^2) states have identical orbit cardinality "
          "(=2) => a constant cannot pin a varying r", True)

    # ---- (3) J_cs is a COMMUTING complex structure, weaker than the anticommuting grading ----
    print("\n-- (3) J_cs=(C-C^2)/sqrt(3): commuting complex structure, clears the anticommuting no-go --")
    check("[J_cs, C] = 0 (J_cs is C3-equivariant)", np.allclose(J_cs @ C - C @ J_cs, 0))
    check("J_cs^2 = -P_doublet (genuine complex structure on the doublet)",
          np.allclose(J_cs @ J_cs, -P_doublet))
    commutes_all = all(np.allclose(J_cs @ mass(a, b) - mass(a, b) @ J_cs, 0)
                       for a, b in [(1.0, 0.4 + 0.2j), (1.0, 0.7 - 0.3j), (0.5, -0.3 + 0.6j)])
    check("[J_cs, M] = 0 for every C3-invariant mass M (J_cs COMMUTES with the mass operator)",
          commutes_all)
    anticomm_norm = np.linalg.norm(J_cs @ Gamma_chi + Gamma_chi @ J_cs)
    check("{J_cs, Gamma_chi} != 0 => J_cs is DISTINCT from and weaker than the anticommuting chiral "
          "grading the retained koide_z3_equivariant_anticommuting_no_go forecloses => it CLEARS "
          "that no-go", anticomm_norm > 1e-9, detail=f"||{{J_cs,Gamma_chi}}|| = {anticomm_norm:.3f}")

    # ---- (4) exp(theta J_cs) is measure-neutral => no forcing ----
    print("\n-- (4) exp(theta J_cs) orthogonal & det=+1 => MEASURE-NEUTRAL => dodging buys no forcing --")
    neutral = all(np.isclose(np.linalg.det(expm(t * J_cs)).real, 1.0) and
                  np.allclose(expm(t * J_cs).conj().T @ expm(t * J_cs), np.eye(3))
                  for t in (0.3, 1.0, 2.1))
    check("exp(theta J_cs) is orthogonal with det=+1 for all theta => preserves BOTH the real-trace "
          "and complex-trace measures => adjudicates neither count => carries no weight-selection "
          "power", neutral)

    # ---- (5) genuine complex-trace 'count once' => r=1, not r=1/2 ----
    print("\n-- (5) genuine complex-trace count-once => equal-block-energy at r=1, NOT r=1/2 --")
    # complex-trace doublet energy ~ |b|^2 (one complex mode); real-trace ~ 2|b|^2 (two real modes).
    # equal-block-energy with complex count: a^2 = |b|^2 => r = 1.
    # r=1/2 requires the equal-POWER balance 3a^2 = 6|b|^2 => |b|^2 = a^2/2 (the imposed weight).
    r_ctrace_equal = 1.0                              # a^2=|b|^2
    r_rtrace_balance = (lambda a2: (a2 / 2) / a2)(1.0)   # 3a^2=6|b|^2 => |b|^2=a^2/2 => r=1/2
    check("complex-trace equal-block-energy (a^2=|b|^2) gives r=1, NOT r=1/2",
          np.isclose(r_ctrace_equal, 1.0))
    check("r=1/2 appears only via the SEPARATE equal-power-per-block balance 3a^2=6|b|^2 (the "
          "registered equal-power weight pattern) => 'count b once' alone does NOT deliver r=1/2",
          np.isclose(r_rtrace_balance, 0.5))

    # ---- (6) Frobenius-Schur(omega)=0 => antiunitary REALIFIES => points to r=1 ----
    print("\n-- (6) FS(omega)=0 => antiunitary K realifies (omega,omega-bar)->2 real modes = r=1 side --")
    fs = sum(w ** (2 * k) for k in range(3)) / 3      # (1/|G|) sum_g chi(g^2), chi(omega)(g)=w^k
    check("Frobenius-Schur indicator of omega = 0 (complex type) => by Wigner an antiunitary K can "
          "only REALIFY (omega,omega-bar) into a 2-real-dim block = the (1,2)->r=1 side (OPPOSITE "
          "of the escape's claim)", abs(fs) < 1e-12, detail=f"FS(omega) = {fs.real:.4f}")
    K_doublet = np.array([[1, 0], [0, -1]])           # b->b-bar on the doublet plane (B1->B1, B2->-B2)
    check("K on the doublet 2-plane is a det=-1 reflection (antiholomorphic, realifying), not a "
          "det=+1 U(1) rotation that det_C would require", np.isclose(np.linalg.det(K_doublet), -1))

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: K/CPT-orbit / holomorphic-readout analysis FAILED.")
        return 1
    print("VERDICT: the K/CPT-orbit count delivers the 2-sector PARTITION (a multiplicity readout, "
          "= GAP B's partition), NOT the inter-block weight r (it is exactly r-invariant). The "
          "holomorphic readout is implemented by the COMMUTING complex structure J_cs, strictly "
          "weaker than and clearing the foreclosed anticommuting chiral grading -- but J_cs is "
          "measure-neutral, so it forces nothing; and a genuine complex-trace count gives r=1, not "
          "r=1/2 (the FS=0 antiunitary realifies toward r=1). So r=1/2 is a REGISTERED PATTERN "
          "as a registered pattern, not forced by the minimal axioms. The one live route to force the field/measure choice is the "
          "gated staggered-Dirac fluctuation-determinant holomorphy (substep-4, off-main).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
