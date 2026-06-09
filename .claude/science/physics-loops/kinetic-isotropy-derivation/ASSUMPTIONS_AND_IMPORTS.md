# Assumptions and Imports — kinetic-isotropy derivation loop

## Allowed premise set (verified against live ledger 2026-06-09)

| Authority | claim_id / registry entry | live status | role |
|---|---|---|---|
| Lattice, Quantum, Record | `minimal_axioms` (MINIMAL_AXIOMS_2026-06-05.md) | axiom premise node | base |
| Scale reference | `scale_reference_primitive` | approved primitive | units only — NOT under attack |
| Adjacency license | `lattice_nn_light_cone_note` | **retained** | the one-step dependency relation R and the R-local update form |
| Single-clock Stone uniqueness | `single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10` | **retained** | clock structure |
| Single-clock scope boundary | `single_clock_uniqueness_scope_boundary_2026-06-06` | retained_no_go | scope guard |
| Clock-rate no-go | `POST_RECORD_CLOCK_RATE_INTERFACE` / `RECORD_CLOCK_RATE_NORMALIZATION_GATE` | check live | records give COUNT not unit |

## Conditional/lower-grade structures (usable only with explicit conditionality)

| Authority | live status | hazard |
|---|---|---|
| Spacing tie a_tau=a_s (`min_time_step_tied_...`) | **audited_renaming** | NOT a derivation — it is a definition per the audit verdict. Do not cite as "derived ratio". |
| Per-plaquette enumeration note | unaudited (landed on main as support) | D2 cites the TARGET primitive — circular, unusable as input |
| Durability theorem (`record_durability_derives_granularity_not_weight_...`) | unaudited | usable as conditional support only |
| B4 stability note (`emergent_lorentz_radiative_stability_discrete_tick_b4_...`) | unaudited | check whether it ASSUMES c_t=c_s (likely cites the primitive — circular) |
| Anisotropy gate no-go | unaudited | two-coefficient counting — safe as framing |

## Forbidden imports

- Observed Lorentz-invariance bounds, PDG/astrophysical anisotropy limits
  (comparators only, never proof inputs).
- The kinetic_isotropy_primitive itself and ANY note citing it
  (circularity): per-plaquette D2, EMERGENT_POINCARE_FREE_SECTOR_..., the
  anisotropy gate's 2026-06-09 premise-supplied update paragraph.
- New axioms / new primitives / new Tier-A nodes (no-new-axiom rule).
- Literature values as derivation inputs (reprove-and-cite only).

## Counterfactual pass (implicit choices that could hide routes)

1. **"xi is one number."** Implicit: a single matter carrier. Counterfactual:
   per-sector xi_A — opens the sector-relative route (universality vs overall
   calibration split). Direction: decomposition route R6.
2. **"The update is a Hamiltonian exponential e^{-a_tau H}."** Counterfactual:
   the one-tick update is a strictly-local unitary (QCA) — quasi-energy is
   periodic; the time direction enters ONLY through tick iteration. Direction:
   the saturation route R2 and the licensed-kernel family R1 must be built in
   the QCA/transfer picture, not assumed-Hamiltonian.
3. **"c_t and a_tau are independently meaningful."** Counterfactual: only the
   combination entering the dispersion is registrable; the Record axiom
   supplies NO time metric (verbatim), so time-direction normalization may be
   pure calibration up to artifact-shape residuals. Direction: R6.
4. **"The Euclidean block Z^3 x Z_tau is given."** Counterfactual: the block is
   CONSTRUCTED from the licensed update; its temporal links are one-tick kernel
   factors, its spatial structure lives inside each kernel factor. The
   hypercubic symmetry question is then about the KERNEL's internal structure,
   not about a pre-given 4D lattice. Direction: R1.
5. **"Saturation (group velocity = front) is a dynamics fact."**
   Counterfactual: it is a REGISTRABILITY fact — an under-saturated sector's
   dependency on the far edge of R is amplitude-suppressed but support-present;
   does any record distinguish "uses the whole license" from "uses part"?
   Direction: R2.
