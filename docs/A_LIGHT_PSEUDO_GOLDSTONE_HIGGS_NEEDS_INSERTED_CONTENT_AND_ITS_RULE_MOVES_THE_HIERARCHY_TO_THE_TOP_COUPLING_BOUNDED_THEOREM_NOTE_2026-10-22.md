---
claim_id: a_light_pseudo_goldstone_higgs_needs_inserted_content_and_its_rule_moves_the_hierarchy_to_the_top_coupling_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the candidate laws' structure (one 16 per family and its mirror, link, rishon and edge registers, the tick's two copies with the copy mass) and the SU(4)/Sp(4) light-Higgs content (2)_0 + (1)_+1/2 + (1)_-1/2 carried by a two-valued index: (A) no structure of the laws contains that content. No family or mirror mode is a Y = 0 doublet or a Y = +-1/2 singlet, every charge is in Z/3 while the content needs Q = +-1/2, registers are centre-blind, and the tick's copies are not an Sp(2) index because the copy mass's commutant is u(1) + u(1). The Lorentz-scalar pair is flavour-antisymmetric only with an Sp(2)-singlet index (exact Grassmann identity). A rule supplying the content therefore inserts observed structure and FAILS the anti-smuggling gate. (B) Conditional on the inserted content: the coset algebra, anomaly freedom and v = f sin theta are exact; the gauge and top invariants are linear in sin^2 theta, so a species-mass term is needed for an interior angle, with sensitivity 2 cot^2 theta; m_H = 125.1 GeV needs a FITTED top cutoff Lt/f of about 2; the mean-field binder gives m_H >= 429 GeV with the top term cut at the binder's cutoff; and a cell-local Yukawa-type term gives either m_t of about 1e-25 GeV or a 1e-30 cancellation. (C) The scale f needs a FITTED 1/alpha_cell(Sp2) of 32.8 to 33.8, a 1e-28 near-critical quartic, or a coarse rung that photon-dispersion bounds exclude. (D) The estimates against measurement (kappa_V and S, T bounds on xi) are separate."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - transmutation_removes_the_weak_scale_tuning_but_only_colour_binds_a_doublet_pair_and_no_rule_vacuum_has_a_misalignment_angle_bounded_theorem_note_2026-10-22
  - the_mirror_pair_condensate_breaks_the_weak_group_at_its_own_scale_and_its_only_vacuum_angle_runs_to_colour_breaking_bounded_theorem_note_2026-10-22
runner: scripts/a_light_pseudo_goldstone_higgs_needs_inserted_content_and_its_rule_moves_the_hierarchy_to_the_top_coupling_2026_10_22.py
---

# A light pseudo-Goldstone Higgs needs inserted content, and its rule moves the hierarchy to the top coupling

Claim type: bounded_theorem.
Primary runner: `scripts/a_light_pseudo_goldstone_higgs_needs_inserted_content_and_its_rule_moves_the_hierarchy_to_the_top_coupling_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its owner decision 3 is open: "the 8 new Weyl modes per cell a light Higgs needs". The [weak-scale note](TRANSMUTATION_REMOVES_THE_WEAK_SCALE_TUNING_BUT_ONLY_COLOUR_BINDS_A_DOUBLET_PAIR_AND_NO_RULE_VACUUM_HAS_A_MISALIGNMENT_ANGLE_BOUNDED_THEOREM_NOTE_2026-10-22.md), C3, and the [mirror-condensate note](THE_MIRROR_PAIR_CONDENSATE_BREAKS_THE_WEAK_GROUP_AT_ITS_OWN_SCALE_AND_ITS_ONLY_VACUUM_ANGLE_RUNS_TO_COLOUR_BREAKING_BOUNDED_THEOREM_NOTE_2026-10-22.md), D2 to D3, fix what a narrow 125 GeV scalar with v = f sin theta needs: the content (2)_0 + (1)_+1/2 + (1)_-1/2, carried by a two-valued antisymmetric index (8 Weyl modes per cell), condensing to SU(4)/Sp(4).

This note asks two questions. First, does any structure already in the laws give that content, so that it follows rather than being chosen? The candidates are the tick's two copies, the families and mirrors, and the registers. Second, if the content is supplied, does the resulting rule (AX-6) produce theta, m_H and f, or are they fitted? The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

## Statement

A. Derivation attempt.

1. Exact. Take one family 16 and its mirror 16bar. Their SU(2)_L doublets have Y in {+-1/6, +-1/2} and their singlets have Y in {0, +-1/3, +-2/3, +-1}. Every electric charge lies in Z/3. The content needs Q = +-1/2 on every mode, so no family or mirror mode is one of them.
2. Exact. Link, rishon and edge registers are blind to the SU(2) centre (Ad(-g) = Ad(g)), so no register configuration at any zoom is a doublet (weak-scale B1, rederived). The new doublet would have to be fermion modes.
3. Exact. Try the tick's two copies as the index. The copy mass (an extra M on s = -1) commutes only with u(1) + u(1) inside u(2), not with Sp(2). So the index is not a symmetry of the update, and CL-1's link rule gives no Sp(2). The s = -1 copy also sits at the cell rung, so at f it has decoupled.
4. Exact (Jordan-Wigner operator identity). The eps_spin pair of single modes is flavour-symmetric, which gives no SU(4)/Sp(4) (mirror-condensate D3). It becomes antisymmetric only with an Sp(2)-singlet two-valued index. With one mode per site, that index needs 8 new sites per cell, and no clause of the laws carries them. The tilings and their step signs (the eps sectors) act on the same mode at different half-ticks, so they are not internal modes.
5. Cited. Every embedding of the SU(4)/Sp(4) structure in the mirror 16 breaks colour or charge at its EW-safe end (mirror-condensate D4). On the Spin(10) pair-square vacuum S^9, the only angle runs to colour breaking (mirror-condensate C3).

Gate result for option (a): no structure of the laws yields the content. A rule that supplies it inserts content because of its observed charges, which fails gate criterion (2). The rule is reported as a FAILURE and is not adopted.

B. Conditional test (the inserted content is assumed only to see whether the physics would work).

1. Exact. SU(4)/Sp(4) has 5 broken generators at every theta. Q is kept at every theta. theta = 0 keeps SU(2)_L x U(1)_Y. m_W^2(theta)/m_W^2(pi/2) = sin^2 theta, so v = f sin theta.
2. Exact. At theta = 0 the Goldstones are one Y = 1/2 doublet (SU(2) Casimir 3/4, Y^2 = 1/4) and one neutral singlet eta.
3. Exact. With the index, the Y, Y^3, SU(2)_L^2 Y and Sp(2)^2 Y anomalies vanish, and both Witten counts are even (2 and 4). Without the index, the single (2)_0 has an odd SU(2)_L Witten count. The index's Sp(2) is a symmetry of the update, so CL-1's link rule makes it a link factor. It confines, so only integer-charge composites are free.
4. Exact. The top's Yukawa-type term (q t^c)(D S+), contracted with eps over SU(2)_L and the index, is gauge-invariant and gives m_t = y f sin theta exactly. The top's O(y^2) invariant and the gauge O(g^2) invariant are both linear in sin^2 theta, so together they have no interior minimum. The gauge part alone aligns to theta = 0 and the top part alone to pi/2.
5. Exact algebra. Adding the Sp(4)-keeping species mass of the new modes gives V = -A sin^2 theta - B cos theta. Then cos theta* = B/(2A), V''(theta*) = 2A sin^2 theta*, and d ln xi/d ln B = -2 cot^2 theta*. The vacuum-angle sensitivity is 38, 98 and 798 at xi = 0.05, 0.02 and 0.0025. B is FITTED.
6. Finite diagnostic. Take the one-loop sea energy with a 4D cutoff Lt on the top and W/Z terms, and tune B to the minimum. Then m_H(Lt/f = 1, 2, 3, 5, 10; xi = 0.05) = 84, 124, 162, 241 and 447 GeV. Getting 125.1 GeV needs Lt/f = 2.03 (xi = 0.05), 1.78 (xi = 0.02) or 2.81 (m_t = 150 GeV). These values are FITTED.
7. Finite diagnostic (mean-field binder, N_hc = 2). f/Lambda <= 0.105, so a top term cut at the binder's cutoff gives m_H >= 429 GeV, about 3.4 times measured. If the top term is cut at the constituent mass instead, m_H runs from about 430 GeV down to 60 GeV (with the cutoff at the cell). Getting 125 needs Lambda/m = 17.9, which is FITTED.
8. Estimate. The laws have one scale, M. A cell-local Yukawa-type term with coefficient 1/M^2 gives m_t = <psi psi>_M/M^2, about 1e-25 GeV. If its coefficient is raised to fit m_t, the top's mass becomes local up to the cell, and holding m_H at 125.1 GeV then needs a cancellation of about 2e-30. AX-6 therefore moves the hierarchy from the Higgs mass term to the top's coupling.

C. The scale f.

1. Exact, then estimate. The index's Sp(2) has b0 = 6 and b1 = 29. f/M = 2^-n needs n = 49.5 to 51.0, that is 1/alpha_cell = 32.8 to 33.8 (FITTED), with sensitivity 35. The per-mode plaquette-count readings give n = 9.5, 19.0, 38.0, 75.9, ..., which miss. A cell coupling equal to SU(2)_L's (1/alpha_2(M) = 44.9) gives n = 67.8, which puts f far below v. This agrees with the sibling one-gap-scale probe's finding that the 8-mode Sp(2) sector run from a common cell coupling gives f < v. Its working window needed Sp(4) with 16 Weyl modes (f of about 7 to 10 TeV), and top partners close it. Under the gate, any rank or mode count chosen to land on v is FITTED.
2. Estimate. A quartic binder at the cell without a gauge factor needs (g - g_c)/g_c of about 1e-28 (FITTED).
3. Estimate against measurement. Suppose the sector sits on a coarse rung, so that f = 2^-n M by an integer. Its block lattice then enters the photon's dispersion through the charged constituents' loop, at a quadratic Lorentz-violation scale of about Lambda_B/sqrt(alpha/3pi). With E_QG2 above about 1e11 GeV, this needs Lambda_B > 3e9 GeV, that is rung n <= 31. A TeV rung (n of about 51) is excluded.

## Estimates against measurement (conditional on the inserted content)

| quantity | result | measured comparison |
|---|---|---|
| kappa_V = kappa_t = cos theta | xi <= 0.051 (f >= 1.09 TeV) | kappa_V = 1.035 +- 0.031 |
| S, T (IR running with Lambda = 4 pi f, plus constituent S) | xi = 0.05: dS = 0.018, dT = -0.037, dchi2 = 14.0; bound xi <= 0.016 (f >= 1.93 TeV) | S = -0.05 +- 0.07, T = 0.00 +- 0.06, rho = 0.93 (approximate, U = 0) |
| T at tree level | 0 (custodial Sp(4)) | consistent |
| m_H | 84 to 447 GeV over Lt/f = 1 to 10; >= 429 GeV with the mean-field cutoff | 125.1 only at the FITTED Lt/f of about 2 |
| m_t from a cell-local term | about 1e-25 GeV | 172.6 |

## Candidate rule text (tested; FAILS the gate; not adopted)

> "AX-6 (light Higgs sector). Each cell carries eight further fermion-mode sites in a further matter role: four flavours with SU(2)_L x U(1)_Y charges (2)_0 + (1)_+1/2 + (1)_-1/2, each carried by a two-valued index; the tick acts on them as on any species, and their index is a symmetry of the update, so CL-1's link rule gives it an Sp(2) link register. Each cell applies the pair square of these modes (the Pfaffian of their index-singlet Lorentz-scalar pair, the k = 3 member of the register's pair-square family), the Yukawa-type term coupling the top's q t^c to their pair D S+, and their species mass aligned with the pair (D, D) + (S+, S-). The weak doublet is the pseudo-Goldstone of their Sp(4)-keeping pair condensate, and its vacuum angle is the stationary point of CL-3's total phase."

Gate report.
1. Measured numbers chosen (FITTED): B (vacuum angle); Lt/f of about 2 or Lambda/m = 17.9 (m_H); 1/alpha_cell(Sp2) = 32.8 to 33.8 (f); the Yukawa-type coefficient (m_t). None of these counts.
2. Observed structure inserted by name: yes. The charges (2)_0 + (1)_+-1/2 are chosen because a neutral EW-safe end with a Y = 1/2 pseudo-Goldstone is observed, and the Sp(2) index is chosen for pseudoreality. FAIL.
3. Prediction the rule was not built for: kappa_V = kappa_t = cos theta (a common deviation), a neutral singlet eta, and integer-charge composites only (from Sp(2) confinement). All are UNTESTED beyond the bounds above.
4. Axiom bent: Lattice ("no site is privileged"), through the new role sites, of the same kind as AX-2. The one-qubit-per-site clause is kept because each mode is its own site. A coarse-rung variant would also touch Admissibility, but C3 excludes it.

Smuggling check. Supplied: the content and charges, the index, the top term, the species mass, the 4D sharp cutoff, the mean-field binder, the gamma0/(2 b0) enhancement and the 1e11 GeV dispersion bound. Forced given the content: the coset, the doublet's quantum numbers, v = f sin theta, the anomaly freedom, the Sp(2) link (by CL-1's link rule), the linearity theorem and T = 0 at tree level.

## Notes used or contradicted

- weak-scale (draft): B1, C3 and the Sp(2) readings are rederived. Its candidate's open items are now computed: the angle needs a FITTED B with sensitivity 2 cot^2 theta, and m_H needs a FITTED top cutoff.
- mirror-condensate-ew (draft): D2 to D4 are used. Its "two-valued index, perhaps the tick's two copies" is tested and fails (A3).
- one-gap-scale (sibling probe, not read here; result relayed by the coordinator): consistent with C1.
- main: VACUUM_CRITICAL_STABILITY_NOTE (a pseudo-Goldstone Higgs needs f >> Lambda_EW): consistent.

## What a light-Higgs law must now do

1. Produce a Q = +-1/2, pseudoreal-index content from site, neighbour or update structure, or produce another coset with a neutral EW-safe end, without naming charges.
2. Give the top a coupling whose theta-dependence switches off near 2 f while being born at the cell. In a non-walking sector this needs an operator dimension of about 1 for psi psi, or about 5/2 for top partners.
3. Fix f without a fitted cell coupling.

## Boundary

A1 to A4 and B1 to B5 are exact algebra or operator identities. B6 and B7 use one-loop sea energies with a supplied sharp cutoff and a mean-field binder. C and the table are estimates. Nothing here excludes content that some future rule derives from site structure, and nothing here derives v, m_H or m_t.
