---
claim_id: isotropic_collapse_on_the_cubic_frustum_carrier_has_a_stationary_point_at_every_tick_and_no_bounce_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "On the supplied isotropic cubic-frustum Lorentzian Regge carrier with the register's fixed-step tick (T = sig x mean edge, sig = sin(eps0)/sqrt3) and the response law stationary in the edges only: the edge equation runs from -infinity to +infinity across the Lorentzian window at every tick, so, given an admissible prior slab (positive edges, |u| < 1/sqrt2) and finite dust content, it has a stationary point at that tick, and since the root lies in the window this holds at every tick by induction; and l_(k+1)/l_k > r_b = (1 - sin(eps0)/sqrt6)/(1 + sin(eps0)/sqrt6), so zero size is reached at no finite tick; a bounce needs a negative dark constant. Finite diagnostics on the same carrier: the root is unique in 60 sampled states, dust collapse ends in a null crush with Hl -> sqrt2 and edge ratio r_b per tick, and the dark constant it makes is positive, about 0.165 sig^2 M l_c per cube in three runs. Estimates for black holes are dimensional supplied-unit comparisons, printed uncounted: no exterior dynamics, exterior persistence, Hawking emission or exclusion of delayed bounces is computed. Global root uniqueness and the sign of the dark constant for every initial state are not shown. Anisotropic and inhomogeneous collapse are not treated."
upstream_dependencies:
  - minimal_axioms
  - independent_rederivation_of_six_candidate_law_theorems_with_corrected_scopes_bounded_theorem_note_2026-10-21
runner: scripts/isotropic_collapse_on_the_cubic_frustum_carrier_has_a_stationary_point_at_every_tick_and_no_bounce_2026_10_22.py
---

# Isotropic collapse on the cubic-frustum carrier has a stationary point at every tick, and a bounce needs a negative dark constant

Claim type: bounded_theorem.
Primary runner: `scripts/isotropic_collapse_on_the_cubic_frustum_carrier_has_a_stationary_point_at_every_tick_and_no_bounce_2026_10_22.py`.

Model status (2026-11-14). The update law (CL-1), with its fixed-step tick and crushed-cube clause, and the response law (CL-3) of the originating three-law register are used here as supplied conditional model definitions with zero premise weight. The originating register text is not in this repository, and these clauses are not the entries of the same number in [docs/CANDIDATE_LAWS.md](CANDIDATE_LAWS.md). No clause is adopted. The exact frustum law used is item 6 of [INDEPENDENT_REDERIVATION_OF_SIX_CANDIDATE_LAW_THEOREMS_WITH_CORRECTED_SCOPES_BOUNDED_THEOREM_NOTE_2026-10-21.md](INDEPENDENT_REDERIVATION_OF_SIX_CANDIDATE_LAW_THEOREMS_WITH_CORRECTED_SCOPES_BOUNDED_THEOREM_NOTE_2026-10-21.md) (#9902, carried in this PR).

The update law fixes each cube's tick as one fraction of its own light crossing and ends with a clause: a cube for which the response law (CL-3) has no stationary point keeps its edges and stops ticking. This note asks whether that clause ever acts in homogeneous isotropic collapse, and whether collapse can bounce or continue through zero size. Everything is computed on one supplied carrier: the isotropic cubic-frustum Lorentzian Regge model with the tick read at mid-slab, T = sig (l_k + l_(k+1))/2, sig = sin(eps0)/sqrt3, the lapse following the edges, and the response law varied in the edges only. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of this.

## Statement

On that carrier, with u_k the slab's rapidity variable (|u_k| < 1/sqrt2 is the Lorentzian window) and s_k = sqrt(1 - 2u_k^2):

1. The edge equation dS/dl_k = 12 l_k (atanh u_k - atanh u_(k-1)) + 4 phi_k (1.5 sig p_k s_k + 3 u_k l_(k+1)/s_k) + 4 phi_(k-1) (1.5 sig p_(k-1) s_(k-1) - 3 u_(k-1) l_(k-1)/s_(k-1)) - M sig, with phi = arcsin(u^2/(1 - u^2)) and p the slab's edge sum, runs from -infinity as u_k -> -1/sqrt2 to +infinity as u_k -> +1/sqrt2, as -/+ 3 sqrt2 pi l_(k+1)/s_k, with all other terms bounded. So, given an admissible prior slab (positive edges, |u_(k-1)| < 1/sqrt2) and finite dust content M, the response law has a stationary point at that tick; the root lies inside the window, so the next prior slab is admissible and the statement holds at every tick by induction from an admissible first slab.
2. |u| < 1/sqrt2 gives l_(k+1)/l_k > r_b = (1 - sin(eps0)/sqrt6)/(1 + sin(eps0)/sqrt6) > 0, so l_k >= l_0 r_b^k and zero size lies at no finite tick. On the limiting sequence the remaining proper time is exactly l_k/sqrt2: the cell shrinks at sqrt2 edges per light crossing.
3. With the tick following the edges a radiation phase -C T/lbar = -C sig per slab does not depend on the edges, so radiation leaves the edge equation and enters only through the first slab. The action is homogeneous of degree 2, so the map of ratios is scale-free: there is one collapse orbit for every size.
4. A(u) = (pi/2 - 2 arctan s)/s vanishes only at u = 0 (A > 0 elsewhere in the window, since s < 1 there), so with dust M > 0 a slab that turns around needs total energy M + D/lbar = 0, that is a negative dark constant D. Reaching zero size in one tick needs |u| = 1/sig >= sqrt3 > 1/sqrt2 for every step, outside the window, so continuation through zero size is unavailable.
5. Hence the update law's crushed-cube clause never acts in homogeneous isotropic collapse on this carrier, from an admissible first slab. Instead the carrier freezes in proper terms: the proper tick sig l, the rest phase m sig l and the remaining proper time l/sqrt2 all fall by about r_b per tick. That the odds keep their unitary half-ticks and records are written every half-tick is the supplied tick's reading, not computed here.
6. In the three dust runs (finite diagnostics) the dark constant made is positive, so those runs do not bounce. Whether every initial state makes D >= 0 is not shown.

## Derivation

Item 1 is the Schlaefli form of the variation of the per-slab action 6 p T g(u) - M T plus the hinge term 6 l^2 Delta atanh, with s_k as the unknown. Only the 3 u_k l_(k+1)/s_k term diverges at the null faces, with the sign of u_k; continuity and the intermediate value theorem then give a root. Item 2 follows from l_(k+1)/l_k = (1 + sig u_k)/(1 - sig u_k) with sig = sin(eps0)/sqrt3 and |u_k| < 1/sqrt2. Item 3 is direct from the mid-slab read. Item 4 uses that the first slab fixes the lapse equation with zero dark constant, so a turning point needs D/lbar = -M.

The dark constant. With the lapse fixed by the update law, the response law has no lapse equation; its integral D = (6 p A - M) lbar is one constant per cube that need not stay at its initial value of zero. The runs below show it does not.

## Checks

The runner ends with `TOTAL: PASS=11 FAIL=0` in about 41 to 45 s and exits nonzero if any counted check fails. Its three estimate lines (D1 to D3) are printed with an ESTIMATE prefix and not counted.

Exact identities (checked numerically):
- The closed-form edge equation agrees with a complex-step derivative of the action to 3e-14 on 6 random states, and the ratio of the equation to its leading divergence at s = 1e-30 is 1.000000000000 on both faces in 12 states.
- The remaining proper time over l_k on the limiting sequence is 0.707106781187 (= 1/sqrt2) for sig = sin(eps0)/sqrt3 at sin(eps0) = 0.0075, 0.04 and 0.3.
- The radiation term in dS/dl is exactly 0; u sequences of a radiation collapse at scale 1 and 1e-25 agree to 0 over 401 ticks.
- min 1/sig over sin(eps0) in (0, 1] is 1.7321 = sqrt3.

Finite diagnostics (supplied carrier, dust M = 1 per cube, kappa = 1, l_c = M/12):
- Uniqueness: one root over the whole Lorentzian window in each of 60 sampled states (sig 0.0043 to 0.17, M 1e-3 to 1e3, l 1e-3 to 1e2, any u_(k-1)). This is sampled, not proved.
- The general-relativity stage: at sig = 0.1706, 0.0499, 0.0231 the ticks at which Hl reaches 0.3, 1 and 1.3 are 158/191/198, 372/483/509 and 442/682/737, against the expansion law's 158/190/198, 372/483/508 and 441/682/737; the general-relativity crunch (A = u^2) would come at ticks 198, 510 and 739. The cell reaches its Hubble radius at l = 2.01, 2.13 and 2.10 l_c.
- The null crush: Hl -> sqrt2 and s_(k+1)/s_k -> r_b^2 to 2e-15, 3e-15 and 3e-15; one decade of l per 10, 32 and 70 ticks (ln10/ln(1/r_b) = 9.5, 32.6, 70.5); 351, 1047 and 1925 ticks to s = 1e-30, with a root at every tick.
- The dark constant made: D/(sig^2 M l_c) = 0.1677, 0.1657, 0.1643, positive in all three runs; only 0.232, 0.229 and 0.220 of it exists at Hl = 0.5.
- Radiation collapse at sig = 0.0231 also ends in the null crush (s = 1e-30 at tick 1494) with C_final/C_initial = 1.000178.
- At sin(eps0) = 0.04, r_b = 0.967873.
- The time-mirrored slice at Hl = 1 is not stationary: its residual over 12 l atanh|u| is +2.993, +2.880, +2.878.
- A(u) > 0 on a 2801-point grid of the window except at u = 0, where A = 0 (check C2, with the exact argument of item 4).

## Estimates against measurement

These use the supplied unit map (cube edge 2 sqrt(8 pi) l_P) and measured numbers. They are dimensional comparisons, not theorems and not computations of exterior dynamics; the runner prints them as uncounted ESTIMATE lines (2026-11-14, hold finding 9).
- Collapse from neutron-star density (5e17 kg/m^3): H0 l0/c = 9.0e-39, so the null crush starts at a/a0 = 8.2e-77, at a density of about 9e245 kg/m^3 (2e149 Planck densities), after about 9.6e39 ticks; the proper time left is about 4e-119 s.
- For a 10 solar-mass hole, (l/r_s)^2 = 3e-77, and the general-relativity evaporation time is 2.1e70 yr, about 5e121 ticks. Exterior persistence and Hawking emission are not computed on this homogeneous carrier; this line compares scales only.
- A time-symmetric bounce, which item 4 and the three runs do not produce here, would on a supplied re-emergence model re-emerge as a white hole after about (r_s/c) ln(r_s/l): 8.7e-3 s for 10 solar masses, 1.3e-2 s for Cyg X-1 against its observed persistence of 1.9e9 s, and 4e3 s for Sgr A* against 9e8 s. No bounce history or delayed-bounce route is computed or excluded.

## Boundary

Supplied: the isotropic cubic-frustum carrier, the mid-slab tick read, the dust phase -M T and radiation phase -C T/lbar, a zero initial dark constant, kappa = 1, the unit map and the measured numbers. Forced on that carrier: a stationary point at every tick, no finite-tick zero size, the sqrt2 shrink rate and r_b, and the need for a negative dark constant to bounce. Diagnostic only: uniqueness of the root (60 sampled states) and the sign and size of the dark constant made (three runs; weakly start-dependent). Not claimed: global root uniqueness; that every initial state makes a non-negative dark constant; exterior persistence, Hawking emission or the exclusion of any delayed bounce (dimensional estimates only); anything about anisotropic (Kasner-type) crushes or inhomogeneous junctions, where whether a stationary point always exists is open, so the crushed-cube clause is kept as a guard there; any statement about the interior's physical reading; the value of eps0.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): unchanged; they fix none of the carrier, tick or content.
- Supplied model (originating three-law register, not in this repository; stated here as conditional definitions with zero premise weight): the update law's fixed-step tick and crushed-cube clause, and the response law's stationary total phase. [docs/CANDIDATE_LAWS.md](CANDIDATE_LAWS.md) does not contain these clauses.
- [INDEPENDENT_REDERIVATION_OF_SIX_CANDIDATE_LAW_THEOREMS_WITH_CORRECTED_SCOPES_BOUNDED_THEOREM_NOTE_2026-10-21.md](INDEPENDENT_REDERIVATION_OF_SIX_CANDIDATE_LAW_THEOREMS_WITH_CORRECTED_SCOPES_BOUNDED_THEOREM_NOTE_2026-10-21.md) (#9902, carried in this PR): item 6, the exact cubic-frustum law the carrier is built on.

## How to run

```
python3 scripts/isotropic_collapse_on_the_cubic_frustum_carrier_has_a_stationary_point_at_every_tick_and_no_bounce_2026_10_22.py
```

Needs numpy, scipy and mpmath. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120` with an internal alarm, runs in about 45 s, prints about 6.3 kB and ends with `TOTAL: PASS=11 FAIL=0`; it exits nonzero if any counted check fails.
