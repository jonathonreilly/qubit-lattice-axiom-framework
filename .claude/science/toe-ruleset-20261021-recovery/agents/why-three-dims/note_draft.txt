---
claim_id: untuned_all_direction_massless_crossings_select_space_dimension_equal_to_the_bloch_ball_dimension_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For translation-invariant local single-particle updates on Z^d with a finite cell and no imposed symmetry beyond translations, a two-fold level crossing has codimension beta+1 (2, 3, 5 for real, complex, quaternionic amplitudes), which is the Bloch-ball dimension of the corresponding two-level unit. Hence crossings that are (i) stable under every small local change of the update (no tuned parameter) and (ii) split linearly in every momentum direction (a cone: massless influence spreads in every direction) exist exactly when d = beta+1; for the complex qubit d = 3. At such a cone the linearisation J is invertible, its sign det J is the chirality (solid-angle degree +-1), the charges sum to zero (Nielsen-Ninomiya), and every Bloch rotation of the qubit is a momentum rotation for the emergent metric J^T J, so the identification of space rotations with qubit rotations is derived at low energy rather than supplied. Finite diagnostics on random nearest-neighbour two-level models confirm: gapped for d = 1, 2; isolated stable cones for d = 3; nodal lines with a flat direction for d = 4; point nodes at d = 2 for real amplitudes and d = 5 for quaternionic. The claim is free-particle level, assumes the stated two premises, and does not derive that untuned massless matter must exist; it also scores three other candidate selectors (minimal odd d with propagating response; Polya transience plus atomic stability; 2^d-cell Clifford counting)."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/untuned_all_direction_massless_crossings_select_space_dimension_equal_to_the_bloch_ball_dimension_2026_10_22.py
---

# Untuned all-direction massless crossings select space dimension = Bloch-ball dimension

Claim type: bounded_theorem (exact linear algebra plus cited codimension theorem) with finite diagnostics.
Runner: runner.py (20 PASS / 0 FAIL, about 3 s, peak about 210 MB). The candidate-law register has zero premise weight; axioms unchanged.

## Question

The information-minimisation framing (agents/info-min-law) leaves d = 3 supplied: neighbour information alone prefers d = 1, and the Bloch = space step of Mueller-Masanes is an inserted identification. Which structural principle, if any, selects d = 3 without inserting observed physics?

## Main result: the cone rule

**Rule CONE (proposed CL-level rule).** Massless influence needs no tuning and spreads in every direction. Precisely: the update must admit a level crossing of its single-particle spectrum that (i) survives every small translation-invariant local change of the update, with no symmetry assumed, and (ii) splits linearly in every momentum direction.

**Theorem.** Over amplitudes in R, C or H (beta = 1, 2, 4), the traceless Hermitian 2x2 matrices form a real space of dimension beta + 1 (runner A1). This dimension is both the Bloch-ball dimension and the codimension of a two-fold crossing (von Neumann-Wigner, cited; the dimension count is exact). The same codimension holds for a crossing of two of n bands and for a unitary tick, since a degenerate U(2) eigenvalue means the SU(2) part is +-1, a codimension-3 condition. Hence:
- d < beta + 1: generic updates have no crossing, so (i) fails.
- d > beta + 1: crossings form (d - beta - 1)-dimensional manifolds; along them the splitting vanishes to first order, so (ii) fails.
- d = beta + 1: crossings are isolated points with invertible J.

For the complex qubit, **d = 3**, and no other d works.

**Corollaries at a d = 3 cone (h ~ J q).**
- Chirality is sign det J, which equals the solid-angle degree of h/|h|: exactly +-1 (C1). Chirality therefore comes out of the same step; candidate (a) needed it as a separate clause.
- The charges sum to zero over the zone (C2). Mirrors are forced: the chirality wall is not removed.
- For every Bloch rotation Q, R = J^-1 Q J is an isometry of the emergent metric J^T J, and an SU(2) lift U gives U H(q) U^dag = H(R q) exactly (C3). Space rotations ARE qubit rotations at the cone. This derives the Mueller-Masanes identification at low energy, conditional on CONE. The massless mode is two-component, with its spin locked to its momentum (helicity).

## Finite diagnostics (seed 20261022)

The model is the generic nearest-neighbour two-level band h(k) = c + sum_j (a_j cos k_j + b_j sin k_j), with random a, b, c. The table lists the runner's results:

| d | class | Result |
|---|---|---|
| 1 | complex | All 12 random models are gapped (min abs(h) 0.149) (B1) |
| 2 | complex | All 12 random models are gapped (min abs(h) 0.036) (B1) |
| 3 | complex | 4 of 4 models with nodes have isolated cones, with charge patterns of 8, 2, 4 and 6 nodes, each summing to 0. The nodes survive a random 1e-2 change of every hop (B2, B3) |
| 4 | complex | Nodes appear in 9 of 12 k4 slices and continue as k4 moves. Each has a kernel direction whose splitting slope is 1.2e-4 of the transverse slope: a line with a flat direction (B4) |
| 2 | real | Point nodes exist. A complex hop eps opens a gap linear in eps (ratio 10.00 for eps = 1e-2 and 1e-3) (B5) |
| 5 | quaternionic | Kramers pairs; 10 isolated nodes with det J != 0 (B6) |

## Candidates scored

**(a) Minimal odd d with protected chiral matter, propagating gravity and gauge dynamics.**
- The chirality clause is exact: a volume element that grades the Clifford algebra exists iff D = d + 1 is even, i.e. d is odd (D1).
- Propagating polarisations are d - 1 for the photon and (d+1)(d-2)/2 for the graviton. Both are positive first at d = 3 (D2).
- The stated reason for excluding d = 1, "gauge anomalies", is WRONG: the 1+1D 3-4-5-0 theory is anomaly-free (D3). d = 1 is excluded only by the absence of propagating photons and gravitons.
- Above d = 3, the selection needs info-min minimality (fewest neighbour-address bits) to discard d = 5, 7, and so on.
- Verdict: a genuine selection given its clauses, but "the response must propagate" inserts observed gravitational waves. It is weaker than CONE, which needs neither minimality nor gravity, and which delivers chirality itself.

**(b) Bloch-ball dimension.** As an identification it is inserted (Mueller-Masanes NJP 15 053040 assume a bit that carries direction information). Under CONE it becomes a theorem: d = Bloch dimension, via the codimension equality (A1, C3). The interaction-based route to Bloch dimension 3 (Masanes, Mueller, Augusiak, Perez-Garcia) then chains to d = 3. Verdict: **upgraded to derived, conditional on CONE**.

**(c) Polya transience plus stable atoms.**
- The lattice Green function at the origin is finite iff d >= 3 (u(3) = 1.516386, return probability 0.3405; the d = 1 and d = 2 integrals diverge) (E1). This is the same statement as "an isolated source has finite field cost": an information-condition reading of the lower edge.
- Upper edge, radial Coulomb with a cutoff a -> 0:
  - d = 3 converges to -alpha^2/4 (E2).
  - d = 5 runs away (E3).
  - d = 4 is scale-free: alpha = 0.5 gives no bound state, and alpha = 2 collapses as -1/a^2 (E4).
- The upper edge uses nonrelativistic massive binding: an observed atom-type structure.
- With the relativistic kinetic term abs(p) the marginal dimension moves to d = 3 itself: hydrogen with abs(p) is stable only for alpha <= 2/pi (Herbst, cited).
- Verdict: the bracket {3} holds only with an inserted kinetic law. **Fails the gate on clause (2)**; it is an anthropic-style cross-check.
- Matches the repo's bounded lower and upper packets: DIMENSION_SELECTION_NOTE, BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20 and COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20, which keep P1-P3 admitted. Open PR #9865 narrows the same lane.

**(d) 2^d cell Clifford counting toward Spin(10).**
- The 2^d corner space carries Cl(2d) irreducibly (F1).
- With one mode per site, a cone carries 2^((d-1)/2) Weyl species per chirality: 1, 2, 4, 8 and 16 at d = 1, 3, 5, 7 and 9 (F2). Staggered Z^3 has 8 zero modes, i.e. 2 per chirality (F3).
- A 16 of one chirality arises from one mode per site only at d = 9. At d = 3 it needs 8 modes per site, which bends the Qubit axiom. "16 = 2^(d+1)" is a corner count of the 3+1 hypercube, not a species count, and the Z16 target is itself a 3+1-specific bordism fact.
- Verdict: **no selection of d = 3; circular if used**.

## Gate (rule CONE)

1. No measured number is chosen. **Pass.**
2. No observed structure is named. **Pass**, with one load-bearing structural premise: untuned massless matter exists. Neither info-min nor the axioms derive this. It names no group, particle or scale. It is the converse face of the "no unprotected light state" clause in agents/minimal-toe R4.
3. Predictions it was not built for:
   - (p1) **Space dimension = 1 + beta.** Given d = 3 measured, amplitudes must be complex, not real or quaternionic. This agrees with the Renou et al. 2021 exclusion of real QM, an independent measurement.
   - (p2) Massless fermions are two-component with helicity locked to momentum (spin 1/2).
   - (p3) Mirrors are forced.
   - (p4) Each cone carries its own metric J^T J, so one-cone universality needs a further rule. **UNTESTED** against the repo's light-cone results.
4. Axiom bent: Lattice. d becomes derived (Z^d with d = Bloch dimension) rather than supplied. Content at d = 3 is unchanged.

## What this does not close

- Free-particle level only. Interactions do not remove an isolated Weyl node at weak coupling (topological charge), but this is cited, not computed.
- Staggered fermions have symmetry-protected Dirac points in any d. The framework's own matter therefore does not select d unless CONE's "no imposed symmetry" clause is adopted. Placing the node at the Fermi level needs half filling plus inversion, which is a symmetry of Z^3 and does not lower the codimension. This is checked analytically, not numerically.
- d = 1 has generic chiral Fermi points at partial filling, a filling crossing and not a band crossing. CONE as stated (band crossing) excludes it. A filling-level reading would let d = 1 back in, and it is closed only by (a)'s propagation clause.
- Literature: Volovik's Fermi-point scenario (stable Fermi points in 3D; points unstable in 2D without symmetry) is the nearest prior work. A statement of CONE as a dimension selector was not found in abstracts; to verify.

## Relation to repo notes

- Builds on agents/info-min-law (D1, E2), agents/minimal-toe-b (R1/R2; the "chiral only in odd d" check is consistent with D1) and agents/minimal-toe (row 6, "smallest even D with Weyl and gravitational waves", which is candidate (a)).
- Agrees with agents/graph-order-3d: graph weights do not select d, and the cone rule does, through the update spectrum. That note named this as the missing ingredient.
- Its upper edge is independent of the repo's Coulomb and Bertrand packets.
- AXIOM_REDUCTION_NOTE row C1 ("d = 3 is a choice") would become "derived, conditional on CONE".
