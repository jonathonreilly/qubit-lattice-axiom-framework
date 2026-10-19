---
claim_id: scale_ladder_gravity_records_to_geometry_lossless_passing_and_the_tick_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Finite checks of stated toy rules on the cubic grid (and the Kuhn complex for the Ward check), supplied-model framing. (1) For the linear response to one record of the nearest-neighbour rule d = sign*keep*avg(d) + delta on a 96^3 torus: lossless lean-away (sign -1) equals (-1)^r times lossless averaging to 4e-16; a loss eps = 1 - keep screens the response with decay lengths 2.32 (eps = 0.03) and 4.04 (eps = 0.01), ratio 1.74. (2) On 2x2x2 blocks, the plain block mean of the averaging response at block distance 6 is 0.0247 and that of lean-away 6.5e-8; the chessboard-weighted block mean reverses them. (3) On a 41^3 grid with pace pinned to 1 on the boundary and each empty site the average of its 6 neighbours, records that subtract a fixed amount give a 1/r coefficient per record of 0.00524 for 1, 19 and 33 records; records that hold pace 0.5 give 0.176 for 1 and 1.022 for 33. (4) On the Kuhn complex, through the least-squares metric reading of its 15 edge classes, a lattice vertex displacement equals a continuum gauge change: a transversely projected source has Ward residual <= 2e-15, and the unprojected e_t e_t source has residual >= 0.70 (relative to |k||T|) at two momenta. (5) The lean-away-in-time rule u+ = 2u - u- + (1/n^2) lap u, at light speed 1 site per tick, blows up for n = 1 sub-step per tick and is stable for n = 2, with speeds 1.00/1.05/1.05 (axis/face/body, half-site resolution). (6) With half the sites updating at random each step the wave does not propagate; with all sites updating together at random tick lengths in [0.15, 0.55] it propagates at 0.99/0.99/1.04. (7) In 1D, m u_tt = (k u_x)_x through a well Phi (min -0.02, width 120): lapse-only weights (m = 1/N, k = N) delay a pulse by 6.0 (integral |Phi| = 6.02); weights m = a^3/N, k = N a (a = 1 - Phi) delay it by 12.5. (8) At t = 30, the continuous-time two-component rule i psi_t = (sum_j sigma_j sin k_j) psi from a point has 0.32 of |psi|^2 in 0.6t-1.1t, 6.1e-4 beyond 1.1 t and 9.4e-8 beyond 1.3 t; the real rule u_t = lap u has a monotone profile. (9) Record growth (each empty site with a recorded neighbour forms with probability p per tick, fixed seed): body/axis extent 0.579 at p = 1 and 0.978 at p = 0.05, axis speeds 1.00 and 0.134. Not claimed: that any of these rules is the framework's law, nonlinear or interacting statements, a derivation from the axioms, a physical identification, or that the owner has adopted any clause other than the one stated in the note."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
runner: scripts/scale_ladder_gravity_records_to_geometry_lossless_passing_and_the_tick_2026_10_18.py
---

# Records to geometry under lossless passing, and the tick

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite checks of stated toy rules.

**Owner decision recorded here.** It is a working law clause, not axiom text:

> **Decision 1 (owner-adopted working clause, 2026-10-18):** "Influence passes from site to site
> without loss."

The owner adopted it on the basis of item 1: any loss screens the long-range 1/r.

Everything else here is an exploration of owner instincts. The explorations cover:
- how a site's odds depend on its neighbours;
- what a record does to its surroundings;
- what sources gravity;
- how time and the tick enter.

None of them is adopted.

## Question

PR #9822 places the gravity carrier on the sites at the 2-site rung. This note asks what in the
record stack could supply that carrier's ingredients:
- the potential;
- its source;
- the time structure;
- light bending.

It uses only nearest-neighbour rules for odds and records.

## Result (stated toy rules)

1. **Loss screens gravity.**
   - One record's influence under lossless averaging falls as 1/r.
   - Lossless lean-away (a site leans away from its neighbours) gives the same profile with a
     chessboard sign.
   - A loss ε per step screens the response, with range proportional to 1/√ε (ratio 1.74
     against √3).
   - This is the basis of Decision 1.
2. **One rung out.** A plain block reading sees the averaging profile and misses lean-away. A
   chessboard reading sees lean-away. A rule's long-range content survives zooming out only
   when it is read in the right channel.
3. **Mass that adds up.**
   - Under averaging, records that drain a fixed amount of pace give the same 1/r coefficient
     per record, so mass is additive.
   - Records that hold a pace behave like a conductor: their "mass" grows with the cluster's
     size, not its count.
4. **The source must be conserved.**
   - Through a least-squares metric reading, a lattice displacement of the Kuhn complex is
     exactly a continuum gauge change.
   - So a conserved source satisfies the Ward identity to rounding.
   - A source that appears without a current, like a record count at a formation event, fails
     it at O(1).
   - Gravity's linear equations therefore admit a source only if formation moves conserved
     content rather than creating it.
5. **Ticks.**
   - A lean-away-in-time rule (lean with neighbours in space, away from your own previous tick)
     is a wave rule with a light cone.
   - At light speed 1 site per tick it is unstable with one sub-step per tick, and stable with
     two.
   - So influence must run at least √3 (in practice two) times faster than the tick at which
     light crosses one site.
6. **Random time.**
   - Per-site random clocks stop the wave.
   - Coherent random tick lengths carry it at equal speed in all directions.
7. **Full light bending.**
   - Lapse-only weights delay a pulse by ∫|Φ|.
   - The weights of the isotropic weak-field metric (m = a³/N ≈ 1 + 4|Φ|, k = N·a ≈ 1) delay
     it by twice that.
   - In rule terms, the full bending needs records to leave neighbour passing alone and raise
     each site's weight on its own past.
8. **Continuous time.**
   - A continuous-time complex two-component rule carries waves with a cone, leaking less than
     1e−7 beyond 1.3t, with no explicit memory rule.
   - A real first-order rule only diffuses.
   - A site's value and its previous-tick value combine into one complex amplitude.
9. **The record cone.** Records that can form only next to records spread as a diamond when
   formation is certain. They spread as a nearly round, slower front when formation odds are
   small.

## Reading (interpretation, not claims)

**A candidate chain from records to linearised gravity**, built on Decision 1:
- possibilities change continuously as complex amplitudes, losing no influence;
- records drain pace by a fixed amount each, which gives Newton's 1/r with additive mass;
- formation moves conserved content, which keeps gravity's equations consistent;
- near records each site weighs its own past more, which gives the full light bending and, in
  the continuous form, a slower local phase (redshift);
- the record cone stays inside the light cone.

**What is still open.**
- These are toy rules, not the framework's law.
- The geometry's own action (Regge, PR #9822) is supplied.
- The tick question (Q6) remains the owner's.

## Premises

- **Axioms used.** Lattice and Qubit (the complex two-component structure in item 8).
- **Primitive used.** The kinetic-isotropy primitive, which puts the tick on the same footing
  as space.
- **Owner working clause.** Decision 1.
- **Supplied.** All the toy rules.
- **Standard facts used.**
  - Discrete Green functions.
  - The CFL stability bound.
  - The Ward identity.
  - Lieb–Robinson-type tails.

## Relation to prior work

Citations are from memory and were not checked against the primaries.

- **The CFL stability bound.** Courant, Friedrichs and Lewy (1928).
- **Lieb–Robinson bounds.** Lieb and Robinson (1972).
- **Shapiro delay.** Shapiro (1964).
- **Eden growth.** Eden (1961).
- **Asynchronous integrators.** Lew, Marsden, Ortiz and West (2003).
- **Wolfram-style emergence.** Mentioned by the owner as a comparison.
- **Repository precedents.**
  - The 2026-09-03 formation-rate bridge note.
  - The note that a chessboard of clocks is invisible.
- **New here.** The combination of these checks with Decision 1 into a chain from records to
  linearised gravity.

## No-Go Discipline Gate

- **N1 — routes.**
  - Nonlinear rules.
  - Other tick schemes.
  - Other conserved contents.
- **N2/N3 — scope.**
  - Single grids and seeds.
  - Linear response.
- **N4 — inputs.** The thresholds are printed by the runner.
- **N5 — wording.** "Gravity" in the reading names the supplied carrier's role, not a physical
  identification.
- **N6/N7 — strongest objections.**
  - Each rule is chosen, not derived.
  - Item 4 tests linear consistency only.
- **N8 — earlier claims.** Builds on #9822. It does not change it.

## Verification

```bash
python3 scripts/scale_ladder_gravity_records_to_geometry_lossless_passing_and_the_tick_2026_10_18.py
```

Expected: `TOTAL: PASS=9 FAIL=0` (about 10 seconds).

## Load-bearing sources

- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
