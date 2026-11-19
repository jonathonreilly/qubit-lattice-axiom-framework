---
claim_id: copy_selective_mass_and_mirror_pair_square_on_the_cube_tick_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the cube tick of the candidate laws register, a supplied copy-selective mass that keeps the 12 tetrahedral turns leaves one light Dirac copy without tuning but stays vector-like; the response law's link-mediated terms conserve mode number and cannot gap the mirror alone; a supplied anomaly-allowed mirror pair square needs the exact chiral SU(2)s that exist only at step pi/2 and mu = 0, outside the register's step bound; no chirality, gapped mirror phase or adopted rule is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/copy_selective_mass_and_mirror_pair_square_on_the_cube_tick_2026_10_21.py
---

# A copy-selective mass and a mirror pair square on the cube tick

Claim type: bounded_theorem.
Primary runner: `scripts/copy_selective_mass_and_mirror_pair_square_on_the_cube_tick_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its cube tick carries two degenerate copies of each species. This note asks whether a term acting on one copy can either leave a single light copy or gap a mirror and leave a chiral family. The first works but gives no chirality. The second is allowed by every anomaly but needs a step the register excludes. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the supplied terms.

## Statement

1. A three-fold turn acts on the two copies as diag(w, w^2) at every step. The 12 even (tetrahedral) turns keep the copy sign and the 12 odd turns flip it. No internal twist restores the odd turns, and time reversal and particle-hole swap the copies.
2. A supplied copy mass M on one copy keeps the 12 tetrahedral turns, translations, inversion and the chiral map. At K = 0 the light copy keeps the species mass and the other gets the species mass plus M, without tuning. The result stays vector-like.
3. Every link-mediated term of the register's response law conserves the mode number N, and number-conserving terms cannot gap the mirror alone.
4. A supplied pair square on the mirror is anomaly-allowed, but the exact chiral SU(2)s it needs exist only at step pi/2 with mu = 0.

## Derivation

Copies. An antiunitary that commutes with a three-fold turn maps w to w^2, so time reversal and particle-hole swap the copies, while inversion and the chiral map keep them. The block-local commutant of the tick is span{1, eps} only at step pi/2 with mu = 0, and scalars at every other step. So no internal copy swap exists, and a copy-selective term must break the odd turns, time reversal and particle-hole. Time reversal combined with C4 survives.

Tetrahedral turns suffice at the free level. Under T alone the velocity, mass and Weyl-cone tensors have the same invariants as under O. T adds a parity-odd xyz tensor and a spin term s_a d_abc k_b k_c, and the chiral map forbids both. With the copy mass the light band has no helicity splitting, and its anisotropy enters at relative order K^2 (dimension 6), the same order as the fully covariant tick. A strong-coupling projection onto the light copy deviates from the exact band as K^3.

Mirror gapping. Links attach only to exactly conserved currents, so every matter-matter term they induce conserves N. At step pi/2 the light family carries U(1)_N x SU(2)_even^2 = +4 and the mirror -4, the same structure as the B+L anomaly, so by cited anomaly matching an N-conserving term cannot gap the mirror while keeping the weak SU(2). A gapping term must change N by 4, which is a change to the update law rather than a consequence of the response law.

Pair square. The pair square on the mirror breaks the plain three-fold turn, but keeps the turn combined with exp(-2 pi i N/3), under which the mirror is neutral and the light pair square is not. One copy of a rung-1 cell is 8 internal states times (L on one sublattice, R on the other), 16 Weyl fields, one family with nu^c. X = 5(B-L) - 4Y is 1 mod 4 on all 16, so the count is 16, which is 0 mod 16, and the cited Z16 condition allows gapping. Without nu^c it would be 15. For N stacked families the window index is 4N mod 3 (argued with cited inputs, not proved for interacting ticks), so the top of the light band at K = pi(1,1,1) is protected unless N is 0 mod 3. This does not select a family number.

The step. The exact chiral SU(2)s need step pi/2 and mu = 0, where the band reaches quasi-energy pi. The register's vacuum bound is a step below 0.04, where the band maximum is 0.08. Among two-partition single-generator ticks the only cube-covariant sublattice-even generator is g5, a face-diagonal spin-3/2 hop, and its tick is gapless along whole body diagonals, so it has no cone.

## Checks

The runner gives 31 PASS and 0 FAIL. These are finite diagnostics of supplied models.

- Tick: unitary, covariant under 24 of 24 turns, bands exactly fourfold, cos w = A<cos K> - (cos 2b - cos mu)/2 at steps pi/2, 0.3 and 0.04 to 3e-15, with speeds 0.57735, 0.17062, 0.02309.
- Copy character (2, 2, 0, 1, 0), the E irrep; copy sign broken at O(K^2) (slopes 2.0); commutant dimensions [2, 1, 1, 1, 1].
- Copy mass: all 12 tetrahedral turns kept, odd-turn residual at least 0.16; light mass 0.1 and heavy 0.1 + M; anisotropy slopes 2.0 and projection slopes 3.0.
- Step pi/2: the 0 and pi windows hold the same pieces, and the Z3 x SU(2)_even^2 sum is 4 per family per window. The window index is 1, 2, 0, 1, 2, 0 for 1 to 6 families. The band reaches 3.142 against 0.080 at the register bound.
- g5 tick: 33 of 729 grid zeros on the body diagonals, band maximum 0.200.
- 0+1D toy: a copy-selective Fidkowski-Kitaev quartic on the 8 mirror Majoranas gives a unique mirror state with gap 2 and leaves the light 2^4 multiplet untouched (Fock dimension 256). Only 8 same-sign Majoranas are uniquely gapped. In a two-half-tick circuit copy mixing splits the light multiplet only at order t^4 (slopes 4.004, 4.017), Floquet gap 0.88 at t = 0.1.
- 1+1D toy: chirality equals sublattice on the swap tick. With a supplied Z3 standing in for the turn, one mirror cannot be gapped under the plain Z3 and can under the twisted one, and three mirrors under the plain Z3 have an explicit Lagrangian with Smith form all 1.

No interacting 1+1D or 3D diagonalisation of the gap was run; the 1+1D gap rests on the cited Haldane criterion.

## Against measurement (estimates)

A dimension-5 cubic birefringence of order (alpha/4 pi)/M_lat, about 1e-22 per GeV, would be excluded by about 1e12 against the GRB bound; the chiral map forbids it, so the rule must keep that map. One light copy removes the doubled electron g-2 term and the doubled N_nu. A mirror mass capped near 0.08 per tick is up to about 1e18 GeV, above LHC limits near 1.5 TeV on extra quarks and leptons. At step pi/2 SU(2)_odd is exact, so its link would be massless unless the rule breaks it, against W_R above about 6 TeV.

## Boundary

Supplied: the form of the copy mass, M and which copy is heavy, the pair square, the rung-1 labels, step pi/2 for the mirror-gapping section, the toys' Z3 and the measured bounds with M_lat near M_P/3. Cited, not rederived: anomaly matching, Z16, crystalline equivalence and the Haldane criterion. The copy mass keeps 12 of the 24 proper turns, so adopting it would need an owner decision on the covariance clause. Whether the chiral map survives with links coupled is not checked. The mirror pair square is not available within the register's step bound, so the result is negative for chirality at small step. No chirality, gapped mirror phase or adopted rule is established.
