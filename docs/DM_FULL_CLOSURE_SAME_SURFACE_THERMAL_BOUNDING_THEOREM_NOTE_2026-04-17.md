# DM Full Closure Same-Surface Thermal Bounding Theorem

**Claim type:** bounded support note
**Status:** conditional supplied-premise interval support
**Date:** 2026-04-17  
**Date of scope repair:** 2026-05-30
**source-note proposal only:** this note is a source-note candidate; audit verdict and effective status are independent-audit outputs.
**Type:** conditional / support
**Status authority:** independent audit lane only.
**Branch:** `codex/dm-thermal-review-2026-04-17`  
**Script:** `scripts/frontier_dm_full_closure_same_surface_thermal_bounding_theorem.py`

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "supplied-premise interval composition over helper-returned live-DM constants and enclosures"
hypothetical_axiom_status: null
admitted_observation_status: "ETA_OBS / OMEGA_DM_OBS comparator inputs are supplied by helper packet"
proposal_allowed: false
proposal_allowed_reason: "The local interval arithmetic closes, but the 64:1 bridge, live-DM constants, and selector/completeness premises remain supplied rather than retained."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Question

Can the same-surface DM thermal layer be represented as a rigorous interval
composition theorem on the current framework surface?

## Answer

Yes, with an explicit supplied-premise boundary.

The local runner proves a rigorous **interval evaluation/bounding** statement
after the following inputs are supplied by the cited upstream/helper packet:

1. the continuum integral representation on the `x_f = 25` slice,
2. monotonicity in the selected coupling `alpha`,
3. positive-series / tail enclosure machinery,
4. the 64:1 same-surface channel-weight bridge,
5. the live-DM plaquette / eta-omega constants,
6. the packet-completeness and selector-boundary premise.

The branch-local claim is the composition theorem over those supplied inputs:
given the endpoint constants and certified helper enclosures, the interval
arithmetic, disjointness, target bracketing, and one-scalar root bracketing all
close in the visible runner. This row does not derive the supplied live-DM
premise packet from framework primitives.

## 2026-05-30 Audit Scope Repair

The latest audit verdict was `audited_conditional`:

```text
missing_bridge_theorem: supply retained one-hop authorities for the 64:1
same-surface channel-weight bridge, the live-DM plaquette/eta-omega constants,
and the packet-completeness/selector premise, then re-audit the same runner
composition.
```

This repair does not introduce those missing authorities as new axioms. It
narrows the theorem to the retained part visible in the artifact: a deterministic
interval composition over explicitly supplied helper outputs and upstream
premises. The stronger "same-surface DM closure" status remains conditional on
separate retained authority for the listed premise packet.

## Certified Current-Bank Output Over Supplied Endpoints

On the supplied current-bank same-surface endpoints:

- `alpha_lo = 0.090667836017286`
- `alpha_hi = 0.092264992618360`

the exact thermal ratio is enclosed rigorously by:

- `R(alpha_lo) in [5.442019867867, 5.442019867931]`
- `R(alpha_hi) in [5.482855571890, 5.482855571936]`

Therefore, after fixing `Omega_b` from `eta_obs`,

- `Omega_DM(alpha_lo) in [0.267709052538, 0.267709052541]`
- `Omega_DM(alpha_hi) in [0.269717881594, 0.269717881596]`

and the current-bank interval obstruction follows within the supplied packet:

- the current bank carries distinct exact endpoint images,
- the target lies between them,
- but the current bank still does not furnish a selector law.

## Certified One-Scalar DM-Family Root Over Supplied Family

On the supplied one-scalar same-surface admitted family

`alpha(sigma) = alpha_lo + sigma (alpha_hi - alpha_lo)`,

exact monotonicity plus the certified endpoint/bisection enclosures force a
unique root interval:

- `sigma in [0.145076095756643, 0.145078095756643]`
- equivalently
  `alpha in [0.090899545261282, 0.090899548455595]`

with a narrow certified width produced by the theorem runner.

So the admitted DM-side family is no longer only numerically supported inside
the supplied packet; it has a certified unique root interval on the thermal
layer itself.

## Honest Status

- current-bank selector closure: still **no**
- thermal layer: **rigorous supplied-premise evaluation/bounding**, not just support
- admitted one-scalar DM-side family: has a **certified unique root interval**
- remaining flagship question:
  whether the current exact bank itself can be made to select a value, or
  whether the DM-side one-scalar family must remain an admitted extension
- remaining audit question:
  whether the 64:1 bridge, live-DM constants, and packet-completeness/selector
  premises can be supplied by retained one-hop authorities.

## Command

```bash
python3 scripts/frontier_dm_full_closure_same_surface_thermal_bounding_theorem.py
```

## Audit Dependency And Supplied-Premise Links

This section records explicit upstream authority citations and supplied
premise boundaries named by audit feedback for
`dm_full_closure_same_surface_thermal_bounding_theorem_note_2026-04-17`.
The load-bearing boundary is broader than the imported certification routines:
the current packet also does not derive the 64:1 same-surface channel-weight
bridge, the live-DM plaquette / eta-omega constants, or the
packet-completeness / selector premise. The visible runner delegates the
certified ratio and root enclosures to common modules and then performs
algebraic / bracketing checks on their returned values. This source repair
therefore narrows the claim scope to a supplied-premise interval-composition
theorem. Independent audit owns any current verdict or effective status after
this source change.

One-hop authorities cited:

- [`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md`](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md)
  — audit row:
  `dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16`.
  Upstream/supplied authority for the continuum integral representation
  on the `x_f = 25` slice underlying ingredient (1) of the supplied packet.
- [`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_MONOTONICITY_THEOREM_NOTE_2026-04-17.md`](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_MONOTONICITY_THEOREM_NOTE_2026-04-17.md)
  — audit row:
  `dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17`.
  Upstream/supplied authority for monotonicity in the selected coupling
  `alpha` underlying ingredient (2) of the supplied packet and the
  unique-root-interval consequence on the admitted family.
- [`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SERIES_TAIL_SUPPORT_NOTE_2026-04-17.md`](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SERIES_TAIL_SUPPORT_NOTE_2026-04-17.md)
  — audit row:
  `dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17`.
  Upstream/supplied authority for positive-series / tail-enclosure machinery
  underlying ingredient (3) of the supplied packet.
- `DM_FULL_CLOSURE_SAME_SURFACE_NUMERATOR_SELECTOR_BOUNDARY_NOTE_2026-04-16.md`
  — audit row:
  `dm_full_closure_same_surface_numerator_selector_boundary_note_2026-04-16`.
  Sibling boundary reference for the current-bank no_go that this
  bounded theorem explicitly preserves in its "Honest Status" section.
- `DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_SELECTOR_SENSITIVITY_BOUNDARY_NOTE_2026-04-16.md`
  — audit row:
  `dm_full_closure_same_surface_thermal_selector_sensitivity_boundary_note_2026-04-16`.
  Sibling boundary reference for the sensitivity boundary that frames
  the admitted-family root interval against the no-current-bank-selector
  conclusion.

Open upstream gaps registered for independent audit:

- the continuum integral representation authority;
- the monotonicity authority;
- the positive-series / tail-enclosure authority;
- the 64:1 same-surface channel-weight bridge;
- the live-DM plaquette / eta-omega constants;
- the packet-completeness / selector premise;
- the sibling current-bank no_go boundary.

The runner-checked content of this note (the certified
`R(alpha_lo)`, `R(alpha_hi)` enclosures; the certified
`Omega_DM(alpha_lo)`, `Omega_DM(alpha_hi)` intervals; and the
certified one-scalar root interval
`sigma in [0.145076..., 0.145078...]` /
`alpha in [0.090899545..., 0.090899548...]`) is verified composition
over the cited authorities' returned values and the algebraic /
bracketing checks performed in the local runner. The cite chain and helper
packet supply the upstream certification routines and live-DM premises whose
retained source chain remains pending for independent audit.

## Honest auditor read

Prior audit feedback observed that the restricted packet does not
include the load-bearing derivations or source for the imported
certification routines and that the visible runner delegates those
steps to external common modules. The cite-chain repair above wires the
three ingredient-level upstream authorities, the sibling no_go, and the
sensitivity boundary as the explicit cite chain for this bounded
theorem. The 2026-05-30 repair also records the 64:1 channel-weight,
live-DM-constant, and selector/packet-completeness premises as supplied rather
than derived. Closing those upstream rows is the path to a stronger chain;
local rewriting of this note does not by itself close that gap.

## Scope of this rigorization

This repair is a supplied-premise interval-composition scope repair with an
explicit upstream gap registration. It does not change the algebraic interval
content or runner output. It prevents the bounded theorem from importing
unretained live-DM premises as if they were already derived.
- [dm_full_closure_same_surface_numerator_selector_boundary_note_2026-04-16](DM_FULL_CLOSURE_SAME_SURFACE_NUMERATOR_SELECTOR_BOUNDARY_NOTE_2026-04-16.md)
