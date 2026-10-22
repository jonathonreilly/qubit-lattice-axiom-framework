---
claim_id: supplied_chiral_terms_keep_a_z4_of_b_minus_l_and_leave_strong_cp_unfixed_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Conditional on one supplied chiral family (Q, u, d, L, e, n) with a doublet H and the supplied term list (Yukawa-type terms, a uddn-class term and (nu^c)^4): the exact abelian symmetry of the term list, computed on the integer lattice of field charges by Smith normal form, is U(1)_Y x Z4, and on every hypercharge-, colour- and SU(2)-admissible operator the Z4 is that of B - L, so B changes only with Delta(B - L) = 0 mod 4: Delta B = Delta L first at dimension six and Delta B = 1, Delta L = -3 first at dimension ten among the 610 enumerated operators, while neutron-antineutron oscillation, Majorana neutrino masses and neutrinoless double beta decay are forbidden at every order in a vacuum that keeps the Z4; with a Majorana nu^c nu^c term instead the group is U(1)_Y x Z2 and the oscillation is allowed. The doublet's phase cancels from arg det(Y_u Y_d); an exact antiunitary kept by every term makes Yukawa-type terms real in its basis (arg det 0 or pi, J = 0); a Nelson-Barr block form gives a real determinant with J nonzero (finite diagnostic). Nucleon lifetimes against Super-K are estimates with a supplied unit map. Strong CP is not fixed by the rules."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/supplied_chiral_terms_keep_a_z4_of_b_minus_l_and_leave_strong_cp_unfixed_2026_10_22.py
---

# Supplied chiral terms keep a Z4 of B - L and leave strong CP unfixed

Claim type: bounded_theorem.
Primary runner: `scripts/supplied_chiral_terms_keep_a_z4_of_b_minus_l_and_leave_strong_cp_unfixed_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) gives each bond a link register valued in the update's symmetries, read with every register transformed and every fixed coefficient fixed. Fifth-force tests then require terms that break every abelian species number except hypercharge, and the register lists them for chiral content: Yukawa-type terms through a doublet, a uddn-class term and the right-handed-neutrino term (nu^c)^4. This note asks which baryon- and lepton-number-changing processes that term list allows, and whether the rules fix the strong CP angle theta_bar = theta - arg det(Y_u Y_d). The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the chiral content nor the terms, and the register's update is not yet chiral. Every result here is conditional on the supplied content and terms.

## Statement

Fields are left-handed Weyl fields Q, u, d, L, e, n (u = u^c and so on, n = nu^c) and the doublet H, with the usual hypercharges, colour triality and SU(2) doublet content. The supplied terms are Q u H, Q d H*, L e H*, L n H (Yukawa-type), n^4, and u d d n (optionally also u u d e).

1. Without a baryon-number-changing term (Yukawa-type terms and n^4) the abelian group is U(1)^2 x Z4, B is an exact U(1) of the term list, and no operator with Delta B != 0 is allowed at any order.
2. With u d d n added (with or without u u d e) the exact abelian group is U(1)_Y x Z4. The Z4 charges are 1 on every Weyl field and 2 on H, that is mode number mod 4 with H counted by the Yukawa-type terms; on every hypercharge-, colour- and SU(2)-admissible operator this equals B - L mod 4. So an operator is allowed exactly when Delta(B - L) = 0 mod 4.
3. Hence Delta B = Delta L = 1 is allowed at dimension six (u d d n gives p -> pi+ nubar and n -> pi0 nubar; u u d e and QQQL give p -> e+ pi0), Delta B = 1 with Delta L = -1 (n -> e- pi+, dimension seven) is forbidden, and Delta B = 1 with Delta L = -3 first appears at dimension ten.
4. Neutron-antineutron oscillation (Delta B = 2, Delta L = 0, Delta(B - L) = 2), Majorana neutrino masses (n n, LLHH) and neutrinoless double beta decay (Delta L = 2, Delta(B - L) = -2) are forbidden at every order while the vacuum keeps the Z4, so neutrinos are Dirac. With a Majorana term n n in place of n^4 the group is U(1)_Y x Z2 and the oscillation is allowed at dimension nine: the ban comes from the (nu^c)^4 form.
5. The doublet's phase enters Q u H and Q d H* with opposite signs, so arg det(Y_u Y_d) does not depend on it for any number of families; a response-set doublet cannot fix theta_bar.
6. If the update keeps an exact antiunitary under which every term is invariant, the Yukawa-type coefficients are real in its basis: arg det(Y_u Y_d) is 0 or pi and the quark-mixing invariant J is exactly 0. Generic complex coefficients give J != 0 and a uniformly distributed arg det.
7. Finite diagnostic (supplied model): in a Nelson-Barr block form, three light down-type copies and one heavy vector-like copy with real CP-even masses and CP broken only in one off-diagonal heavy-light block, the determinant is real while J != 0 when the CP-odd mixing is comparable to the heavy mass, and J -> 0 when it is small.

## Derivation

Abelian group. Each term is invariant under a phase rotation exactly when its charge sum vanishes, so the group of abelian symmetries is the dual of the integer lattice spanned by the term contents on the seven fields. The runner computes the Smith normal form D = U A V of the integer term matrix; the number of zero diagonal entries counts the U(1) factors and each diagonal entry d > 1 gives a Z_d, with charges read from the columns of V. An operator with integer field content e is allowed exactly when e lies in the term lattice, which the same form decides.

Selection rule. On hypercharge-neutral, colour-singlet operators with an even number of doublets, mode number counted with H at 2 and B - L agree mod 4; the runner verifies this on all enumerated operators. With u d d n present the only discrete factor is that Z4, so items 3 and 4 follow from Delta(B - L) mod 4. Neutron-antineutron operators have Delta(B - L) = 2 and n n, LLHH have Delta(B - L) = -2; the Majorana term n n instead reduces the Z4 to Z2, under which both are even.

Strong CP. Rotating H by e^(i phi) multiplies Y_u by e^(i phi) and Y_d by e^(-i phi); the determinant of the product changes by e^(3 i phi) e^(-3 i phi) = 1 for three families, and likewise for any number. An antiunitary symmetry kept by every term fixes the coefficients to be real in its basis, so the determinant is real and every rephasing invariant vanishes. In the Nelson-Barr form the mass matrix is block triangular with a real light block and real heavy mass, so its determinant is real, while the complex heavy-light entries feed CP violation into the light mixing through the light eigenvectors.

## Checks

The runner ends with `TOTAL: PASS=14 FAIL=0` in about 1 s.

Exact checks:
- Enumeration: 610 operators with Delta B != 0 and dimension at most 10, built from four or six Weyl fermions, up to four doublets and at most one derivative, with zero hypercharge, colour triality zero, an even number of doublets and a left/right count compatible with a Lorentz scalar (necessary conditions).
- Yukawa-type terms with n^4: U(1)^2 x Z4 with Z4 charges (0, 0, 0, 3, 1, 1, 0) on (Q, u, d, L, e, n, H); no Delta B != 0 operator allowed.
- With u d d n, and with u d d n and u u d e: U(1)^1 x Z4 with Z4 charges (1, 1, 1, 1, 1, 1, 2); allowed exactly when Delta(B - L) = 0 mod 4 on all 610 operators; the lowest allowed dimension is 6 for (|Delta B|, Delta L) = (1, 1) and 10 for (1, -3); (1, -1) is not allowed.
- Mode number mod 4 (H at 2) equals B - L mod 4 on all 610 operators.
- The 6 enumerated u d d u d d-class operators (Delta B = 2, Delta L = 0) are all forbidden with n^4 and all allowed with n n, where the group is U(1)^1 x Z2 and the allowed classes are (1, -3) at dimension 10, (1, -1) at 7, (1, 1) at 6, (1, 3) at 9 and (2, 0) at 9.
- LLHH and n n lie outside the term lattice with n^4 and LLHH lies inside it with n n.

Identities and finite diagnostics (checked numerically):
- Doublet phase: over 20 random phases with random complex 3 x 3 Yukawa-type matrices, the maximum shift of arg det(Y_u Y_d) is 3e-16.
- Antiunitary: 200 samples of real 3 x 3 coefficients in a random unitary basis give maximum J = 6e-16 and arg det within 1e-12 of 0 or pi; 200 generic complex samples give median J = 0.03.
- Nelson-Barr block form (200 samples each, light block of size 0.01, heavy mass 1): median J = 8.9e-03 when the CP-odd mixing is of order the heavy mass and 4.3e-08 when it is 1e-3 of it; in both cases arg det lies within 1e-12 of 0 or pi.

## Estimates against measurement

All of these are estimates with supplied inputs: the unit map (G = a^2/(8 pi) per cell, 2.11e18 GeV per radian per tick, so 1/a = 2.435e18 GeV), the nucleon matrix elements W and enhancement A from lattice QCD, the measured bounds and masses.

- A dimension-six term with coefficient g a^3 per tick at the site scale (Lam = 2.62e18 GeV), or read one per 2 x 2 x 2 cell (Lam = 9.25e17 GeV), gives at g = 1 central lifetimes of 2.8e45 yr (p -> e+ pi0), 1.1e46 yr (p -> nubar K+), 1.4e45 yr (p -> pi+ nubar) and 2.8e45 yr (n -> pi0 nubar). In the worst case (cell scale, A = 3, largest W) they are 1.1e43, 1.8e43, 5.3e42 and 1.1e43 yr against the bounds 2.4e34, 5.9e33, 3.9e32 and 1.1e33 yr, a minimum margin of 4.4e8; the largest allowed coefficients are 2.1e4, 5.5e4, 1.2e5 and 9.8e4.
- In that worst case a unit-coefficient term must sit within 7 rungs of the sites (Lam_min = 6.4e15 GeV, the scale on rung k being Lam/2^k).
- With a coefficient g of about 0.01, taken from a separate supplied baryogenesis fit, tau(p -> pi+ nubar) is about 1e49 yr, beyond the Hyper-Kamiokande reach of about 1e35 yr: no nucleon decay is predicted to be seen.
- The neutron-antineutron bound tau > 4.7e8 s is consistent with item 4; a signal at ESS or NNBAR would exclude the (nu^c)^4 form.
- theta_bar: with d_n = 2.4e-16 theta_bar e cm and d_n < 1.8e-26 e cm, |theta_bar| < 7.5e-11; a uniformly distributed phase lands there with probability 2.4e-11, so generic order-one Yukawa-type phases are excluded, while an exact antiunitary would give J = 0 against the measured nonzero quark-mixing CP phase.
- theta is physical: the eta' (958 MeV) lies above the no-anomaly bound sqrt3 m_pi = 234 MeV, and the Witten-Veneziano relation needs chi^(1/4) = 179 MeV. A massless up quark is excluded (m_u/m_d = 0.47(2)). Link registers are valued only in exact symmetries and U(1)_A is anomalous, so no link or response-set field relaxes theta_bar.

## Boundary

Supplied: the chiral content of one family and its three-fold copy, the Standard-Model links, the term list (Yukawa-type terms, u d d n, u u d e, n^4 or n n), the vacuum's keeping of the Z4, the antiunitary and the Nelson-Barr block form as hypotheses, the unit map, the coefficient g, the matrix elements W and A, and every measured input. Forced, given those: the group U(1)_Y x Z4 with the Z4 of B - L, the selection rule Delta(B - L) = 0 mod 4, the lowest dimensions listed among the enumerated operators, the bans on neutron-antineutron oscillation, Majorana masses and neutrinoless double beta decay, the cancellation of the doublet phase, and reality under an exact antiunitary. Not claimed: that the register's update contains these terms or is chiral (it is not yet), that it keeps any antiunitary or has a Nelson-Barr structure (no law forbids the opposite off-diagonal block), any value of theta_bar, operators beyond the enumerated class (eight or more fermions, more doublets or derivatives), the effect of sphalerons beyond Delta B = Delta L = 3 per three families, or nucleon lifetimes beyond supplied-unit estimates. Strong CP is not fixed by the rules. The Nelson-Barr result is a sampled finite diagnostic of a supplied model, not a theorem about the register's tick.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records; they fix none of the inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's link registers valued in the update's exact symmetries, and the term list it requires for chiral content. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/supplied_chiral_terms_keep_a_z4_of_b_minus_l_and_leave_strong_cp_unfixed_2026_10_22.py
```

Needs numpy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s, prints about 4.9 kB and ends with `TOTAL: PASS=14 FAIL=0`.
