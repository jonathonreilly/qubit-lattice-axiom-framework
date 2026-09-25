---
claim_id: round_three_synthesis_the_photon_from_four_sides_the_formation_clocks_the_text_admits_and_a_three_dimensional_charge_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "A synthesis of seven open blocks (open PRs 9161, 9163, 9169, 9171, 9164, 9166, 9168), all supplied models with finite diagnostics and none adopted. The runner recomputes one exact identity per block with its own code path: the Feynman numerator 2 u_0 s^2 on the exact 2^3 flip component (864 states, E_0 = -9.026721, to 1e-9); the zone average 3 of the transverse weight and the vanishing longitudinal combination on ice samples (to 1e-15); the RK clause D - A annihilating the uniform vector on that component (to 1e-15, lowest eigenvalue zero); the lattice Maxwell covariance (1/2) sqrt(K/U) (C^T C)^{1/2} on 4^3 equal to A |s(k)| (1 - g g^+) with kernel N + 2 (to 1e-15); rate functionals of the menu odds invariant under menu dephasing while purity and coherence rates move by 0.49 and 0.98; the hyperhoneycomb site set on the 4x4x8 torus trivalent with axis bonds, connected, bipartite, half the points; the two fits of the four-size series (nu = 0.341, chi^2 5.06; S_0 = 0.392, a = 0.189, chi^2 3.82); and the register of fourteen decision points. What the blocks found: the pure-ring point's transverse fluctuations at the smallest momentum are about a third of the uniform-ice constant (0.692, 0.557, 0.575, 0.510 on 4^3-10^3 against 1.5), the missing weight sits at the zone corner without growing, the redistribution switches on continuously from the RK point, no size-independent Gaussian photon fits the numbers, and the four-size series is fitted mildly better by a constant plus a linear term than by a power; the axiom text admits every formation-rate class and a rate reads only registered content iff it is invariant under menu dephasing; the hyperhoneycomb composite network embeds in the doubled cubic lattice with an exact SU(2) charge and one Weyl pair. No power law, gap value, phase, thermodynamic limit, reading or construction is adopted or asserted."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
runner: scripts/round_three_synthesis_one_identity_per_block_and_the_register_2026_09_24.py
---

# Round-three synthesis: the photon from four sides, the formation clocks the text admits, and a three-dimensional charge

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** a synthesis of open blocks, exact identities recomputed, finite diagnostics quoted; unaudited.

## Result

The round-two synthesis (open PR 9155) left the photon of the pure-ring
point as the one sector whose diagnostics narrowed without deciding, and
five sectors with their prices in supplied structure. Round three attacked
the photon from four sides in one session and, through three probes run in
parallel, the formation clock and the charged matter network. This note
collects what is exact, what is a finite diagnostic, what each costs, and
what stays open; the runner recomputes one identity per block.

**The photon (open PRs 9161, 9163, 9169, 9171, 9166).**
- *Exact.* The Feynman numerator is `2u_0 s²` in every state, so the
  photon bound is one pure structure factor per momentum (9161). Parseval
  and the exact Gauss law fix the zone average of the transverse weight at
  3, so any suppression at small `k` is a redistribution (9163). At `V = g`
  the projector's local energy vanishes identically and it samples uniform
  ice, an exact anchor for the estimator chain (9169). The non-compact
  lattice Maxwell theory with the ring model's Gauss law has the covariance
  `A|s(k)|(1 − ĝĝ*)` with no size dependence at fixed `k`, and its magnetic
  stiffness is fixed by the sum rule (9166).
- *Finite diagnostics.* `S_T(k_min) = 0.692, 0.557, 0.575, 0.510`
  (`± 0.013, 0.022, 0.028, 0.046`) on 4³–10³ against the uniform-ice 1.5:
  a fall, a level step, a fall; the weight goes to the zone corner
  `(π,π,π)`, doubled on 4³ and 6³ without growing; the redistribution
  switches on continuously from the RK point (axis 1.52 → 0.73, corner
  3.07 → 7.6 on 4³) while the ring expectation moves only 0.27 → 0.29; no
  size-independent Gaussian fits the six 8³-and-below numbers
  (`χ²/dof = 33/4`), and the fixed-`k` growth with size lies outside any
  Gaussian; the mode at each `k_min` decays as one exponential with rate
  1.5, 0.9, 0.5, 0.4; the four-size series is fitted mildly better by
  `S_0 + a·k` (`S_0 = 0.39`, `χ² = 3.8`) than by a power (`ν = 0.34`,
  `χ² = 5.1`); the bound's exponent in `k` is 1.45.
- *Price.* No new structure: D-gauss, D-roles, D-ring, and the RK potential
  D-RK for the sweep; the Gaussian theory is a supplied comparison
  (D-Gauss-comparator), not a premise.
- *What it means, on the small tori.* The pure-ring state differs from the
  RK state exactly where a photon would show it — the momentum dependence
  of the transverse fluctuations — and its Feynman bound falls faster than
  `1/L`, but no power is resolved: a residual constant near a quarter of
  the pinch-point weight would make the bound quadratic at long
  wavelengths; a fading one leaves the linear term as the photon. The 12³
  run (open PR 9171, addendum) shows the smallest-momentum series is
  contaminated by a finite-size suppression that weakens with `L`, so the
  separator is `S_T(k)` at fixed `k` extrapolated in `L`, not the series.

**Formation (open PR 9164).**
- *Exact.* A rate reads only registered content iff it is invariant under
  the menu dephasing channel `ρ → P₊ρP₊ + P₋ρP₋`; constant, law and odds
  clocks pass, purity and coherence clocks fail. Record-determined rates
  are constant between neighbour record events and reduce to the landed
  constant clock, with a closed form for the precessing site. The
  covariant span `{1, |r|², (r·n)²}` contains a coherence-reading rate, so
  covariance alone does not settle the landed open item.
- *Price.* Six clock classes recorded (D-form-const, -law, -records, -odds,
  -state, -time) and the register reading D-register; the text admits all
  and fixes none, as the axioms document itself says of the rate.

**Charge in three dimensions (open PR 9168).**
- *Exact.* The hyperhoneycomb (10,3)-b graph embeds in the doubled cubic
  lattice with every bond on a lattice axis and three of six neighbours
  used, the selection made entirely by which composite sites are
  unrecorded; the total matter spin commutes with the Hamiltonian; the
  eight-qubit star spectrum equals the three-flavour free-Majorana one.
- *Finite diagnostics.* The flux-free bands have a nodal line that the
  time-reversal-odd term splits into exactly two Weyl points of opposite
  chirality: a charged Weyl pair. A six-valent cubic network needs four
  qubits per site and shows a zero-energy surface or an eightfold node, no
  Weyl points.
- *Price.* Per 4×4×8 cell, 8 of 16 composite sites recorded and 12 flavour
  records on 48 links (D-comp, D-axes/D-flavour); bond block 4×2×2.

**Corrections made in round three.** Open PR 9144's remark that a
three-site flux would have exposed a sign in the reduction was withdrawn
(the spectrum is even in the odd coupling on three or four sites; the sign
is a convention, observation of open PR 9168). The landed clock runner's
"tilted" menu axis is not perpendicular to the field (cosine 0.424); the
claim stands and a comment repair is queued (observation of open PR 9164).

**Three lessons.** First, the estimator matters as much as the model: the
mixed projector estimator is 25 % off for the structure factor, forward
walking along lineages fixes it, and the RK point checks the whole chain
exactly. Second, a first pass at low statistics suggested a flat bound
times `L`; the six-mode statistics did not support it and the check that
had asserted it failed as designed — no note is framed on a 1.5-sigma
point. Third, exact bookkeeping (a sum rule, a zero-mode identity, a
dephasing criterion) turns a numerical puzzle into a question with a
definite next measurement.

## Setting and decision points

Every block uses the four axioms' lattice and record structure with the
supplied dynamics clause of open PR 9040 in its ring form (D-ring) under
the exact Gauss law (D-gauss) with one role per site class (D-roles); the
sweep adds the RK potential (D-RK); the formation blocks add the clock
classes and the register reading; the charge block adds the composite-site
choice and record-selected flavours; the Gaussian theory is a supplied
comparison. The register printed by the runner lists fourteen decision
points. None is adopted.

## Recomputed identities (the runner)

| Block | Identity recomputed | Result |
|---|---|---|
| 9161 | `⟨O†(H − E_0)O⟩ = 2u_0 s²` on the exact 2³ component | 3.008907 both sides |
| 9163 | zone average of `T(k)` is 3; longitudinal combination vanishes | 4·10⁻¹⁶; 3·10⁻¹⁵ |
| 9169 | `(D − A)·1 = 0` on the component; lowest eigenvalue 0 | 0; −2·10⁻¹⁵ |
| 9166 | `(1/2)√(K/U)(CᵀC)^{1/2} = A|s|(1 − ĝĝ*)` on 4³; kernel `N + 2` | 2·10⁻¹⁵; 66 |
| 9164 | menu-dephasing invariance of odds and law rates; purity, coherence move | 10⁻¹⁶; 0.49, 0.98 |
| 9168 | hyperhoneycomb site set on 4×4×8: trivalent, connected, bipartite, half the points | 64 of 128 sites, degree 3 |
| 9171 | the two fits of the four-size series | `ν = 0.341, χ² 5.06`; `S_0 = 0.392, a = 0.189, χ² 3.82` |
| — | the register | 14 decision points |

## What stays open

- The photon's power. An auxiliary 12³ run (open PR 9171, addendum) gave
  `S_T(π/6) = 0.496 ± 0.057`, on both fits' predictions, but showed the
  structure factor growing with the torus at fixed momentum
  (`S_T(π/3)`: 0.557 on 6³ → 0.778 on 12³; `S_T(π/2)`: 0.69 → 0.9 from 4³
  to 12³) with flat forward-walking lags: the smallest-momentum series
  mixes the `k`-dependence with a weakening finite-size suppression, and
  the observable to extrapolate is `S_T(k)` at fixed `k` (16³ and 18³ at
  a precision of 0.03, with 250–500 walkers and lags growing with the
  torus); the late-time gap on the larger tori.
- Which formation-rate class the framework favours, beyond what the text
  admits; whether D-register is binding.
- The hyperhoneycomb network's ground-state flux sector and its gauging
  (the link class is taken by flavour records); the hyperoctagon embedding.
- Independent checks of every block; all are self-checked.

## Prior art

As in the blocks: Feynman 1954; Rokhsar and Kivelson 1988; Trivedi and
Ceperley 1990; Hermele, Fisher and Balents 2004; Benton, Sikora and Shannon
2012; Kitaev 2006; Yao and Lee 2011; Mandal and Surendran 2009; Hermanns
and Trebst 2014; O'Brien, Hermanns and Trebst 2016; Lieb 1994. All cited as
prior art, not as premises.

## Checks

The runner has 8 checks and all pass in about 3 seconds, single-threaded;
the table above lists them.

## Independent check

None yet. The runner uses its own code paths for the identities (the probe
blocks' definitions are copied where a construction is theirs, and stated
as such); the finite numbers are quoted from the blocks' certified caches.

## What this does not do

- It adopts no clause, reading, construction, comparison or method.
- It claims no power law, gap value, phase, thermodynamic limit or physical
  identification; every finite number is a supplied-model diagnostic with
  the errors stated in its block.
