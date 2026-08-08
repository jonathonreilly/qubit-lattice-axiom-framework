# Scale-Axis Planck-Anchor Self-Consistency — Scoping Note

**Date:** 2026-06-05
**Claim type:** meta (scoping)
**Status:** scoping note. Adds no axiom, no theorem, no numerical prediction,
no audit verdict. Sets **no** audit/effective status. The independent audit
lane owns any status. Owner-authorized exploration.
**Primary runner:** [`scripts/cl3_scale_axis_planck_anchor_selfconsistency_2026_06_05.py`](../scripts/cl3_scale_axis_planck_anchor_selfconsistency_2026_06_05.py)
**Cache:** [`logs/runner-cache/cl3_scale_axis_planck_anchor_selfconsistency_2026_06_05.txt`](../logs/runner-cache/cl3_scale_axis_planck_anchor_selfconsistency_2026_06_05.txt)

## Question

The framework has a single dimensionful input: the lattice scale `a^{-1}`
(the `scale_reference_primitive`). The axiom-minimality posture explicitly
does **not** assert `a/l_P = 1`; the self-consistency that the natural unit
equals the Planck length is a **separate open gravity derivation**
(`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23` item **S**;
`PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23` §1).

Does the framework's emergent gravity **fix** `a = l_Planck` with no extra
dimensionful input or tuned factor (self-consistency **closes**)? Or is
`a = l_P` an independent assumption (**open**)?

**Honesty guard.** "Closes" = the framework's *own* emergent G, set equal to
the observed/derived gravitational coupling, forces `a = l_P` with **no** extra
input. If it needs one dimensionful import or a tuned dimensionless factor, it
is **open** (assumed), not derived.

## Verdict

**OPEN-SELF-CONSISTENCY.** `a = l_P` is **assumed / anchored, not derived**
from the framework's own content. This is a verification (not a change) of the
existing posture: the Planck-mass anchor is **taken, not yet derived**; the
closure `a/l_P = 1` is the open gravity lane, available only as a *conditional*
theorem whose entire forward chain is `unaudited` on `origin/main`.

The runner makes this precise on **two** distinct candidate routes. Both reduce
to importing exactly **one** dimensionful fact the dimensionless `Cl(3)`-on-`Z^3`
core cannot emit.

## Why (dimensional / self-consistency computation)

The one-qubit operator algebra on `Z^3` is purely dimensionless; `a` (length)
is the sole dimensionful primitive. By Buckingham-Pi, every derived quantity is
dimensionless or carries an integer power of `[a]`. A *second* independent
dimensionful number cannot be emitted — so any closure `a = l_P` must import one
dimensional fact (the ordinary content of
`PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27`).

### Route A — G from lattice dynamics, then demand `G_emergent = G_observed`

The retained-`bounded` gravity chain (`gravity_clean_derivation_note`,
`newton_law_derived_note`, `gravity_law_cleanup_note`,
`self_consistency_forces_poisson_note`, all `retained_bounded` on `origin/main`)
closes **only in lattice units**: it yields a **dimensionless** coupling
`G_lat = 1/(4π)` (bare Green) or `G_lat = 1` (carrier-normalized). It carries no
`[L],[M],[T]`.

An exhaustive `[-3,3]^4` integer-power search over `{a, c, M_lat, ħ}` confirms
the SI carry must reference the lattice scale: the candidates are
`a^2 c^3/ħ`, `ħ c/M_lat^2`, `a c^2/M_lat`, `a^{-1} c^0 M_lat^{-3} ħ^2` — every
one uses `a` or `M_lat` (and `M_lat = a^{-1}` in natural units); **none** is
buildable from `c, ħ` alone. The canonical form is the Planck form
`G_SI = G_lat · ħc/M_lat^2`.

Demanding `G_SI = G_observed` and solving gives
`M_lat = sqrt(G_lat · ħc / G_observed)`, which is **algebraically `M_Pl`** (up
to `sqrt(G_lat)`). [CHECK-ONLY: with CODATA `G`, this returns
`M_lat = 2.176e-8 kg = M_Pl` to `rel_err ~ 1.6e-7`.]

This is **circular**: `G_lat` is dimensionless, so the only way `G_SI` acquires
a value is by importing one dimensionful number (`G`, equivalently `M_Pl` or
`l_P`); setting `a^{-1} = sqrt(ħc/G)` is the **definition** `M_lat := M_Pl`, not
an independent second constraint. Degree-of-freedom count: **1** dimensionful
unknown (`a`), **0** dimensionful equations from the (dimensionless) lattice ⇒
underdetermined. **Route A does not close.**

### Route B — Bekenstein-Hawking horizon-density match (the framework's actual route)

The framework's genuine self-consistency theorem is
`PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24`: **`(BP) ⇒ a/l_P = 1`**.
Mechanism: the primitive event cell gives a **derived dimensionless** coefficient
`c_cell = Tr((I_16/16) P_A) = rank(P_A)/16 = 4/16 = 1/4`. Equating same-surface
densities `c_cell/a^2 = 1/(4 l_P^2)` gives `a^2 = 4 c_cell l_P^2 = l_P^2`, hence
`a/l_P = 1`.

Here the dimensionful input enters explicitly: the RHS `1/(4 l_P^2)` **is** the
Bekenstein-Hawking area-law density with `l_P^2 = ħG/c^3`. So `l_P` (hence `G`)
is imported via the **carrier-identification premise BP** ("the primitive
one-step boundary count *is* the microscopic carrier of the standard
gravitational area/action density"). The **derived** part is only the
dimensionless `c_cell = 1/4`; `a/l_P = sqrt(4 c_cell)` lands on `1` only via the
**joint** statement (derived `c_cell = 1/4`) **AND** (open `BP`). **Route B is a
genuine self-consistency *relation*, but conditional on an open dimensionful
import.**

## Ledger cross-check (`git show origin/main:docs/audit/data/audit_ledger.json`, 2026-06-05)

- **The entire `(BP) ⇒ a/l_P = 1` forward chain is `unaudited`:**
  `planck_scale_conditional_completion_note_2026-04-24`,
  `planck_boundary_density_extension_theorem_note_2026-04-24`,
  `planck_primitive_coframe_boundary_carrier_theorem_note_2026-04-25`,
  `planck_link_local_first_variation_p_a_forcing_theorem_note_2026-04-30`,
  `planck_source_unit_normalization_support_theorem_note_2026-04-25`,
  `planck_primitive_clifford_majorana_edge_derivation_theorem_note_2026-04-30`
  (`audited_renaming` in prose, ledger row `unaudited`),
  `bh_quarter_wald_noether_framework_carrier_theorem_note_2026-04-29`, and the
  three `planckP1/P2/P3` narrowings (all `unaudited`). The `planckP4` G_Newton
  self-consistency sharpening is also `unaudited`.
- **What is `retained_bounded`:** the *internal/dimensionless* gravity chain
  (`gravity_clean_derivation_note`, `gravity_full_self_consistency_note`,
  `gravity_law_cleanup_note`, `newton_law_derived_note`,
  `wave_equation_gravity_note`, `self_consistency_forces_poisson_note`). These
  close only to **lattice units**; none carries a dimensionful scale, so none
  pins `a` in SI.
- **What is `retained_no_go` (scale not forced by symmetry/structure alone):**
  `planck_finite_response_no_go_note_2026-04-24`,
  `planck_parent_source_hidden_character_no_go_note_2026-04-24`,
  `planck_boundary_orientation_incidence_no_go_note_2026-04-30`.
- **Meta (no status):** `planck_mass_conventional_anchor_meta_note_2026-05-27`,
  `admitted_input_registry_tier_a_note_2026-05-23`.

**Gravity-note audit-status flag (honesty).** The closure leans on the
`PLANCK_SCALE_CONDITIONAL_COMPLETION` chain, which is **`unaudited`** end-to-end.
The memory-noted "corrected propagator" / "gravity 2.0" line has **no ledger
row** and is **not** load-bearing or retained — it must not be cited as
retained content. Only the dimensionless lattice-units gravity rows above are
`retained_bounded`.

## What this opens (next paths)

The missing ingredient is *exactly one dimensionful import*: the carrier
identification **BP** that says the primitive `Z^3` boundary count is the
microscopic Bekenstein-Hawking carrier. The next paths this scoping makes
explicit:

1. **Derive BP** (substrate boundary count ⇒ BH area-density carrier) from the
   `Cl(3)`/`Z^3` baseline — this is the single dimensionful gate; with it,
   `c_cell = 1/4` (already derived) closes `a/l_P = 1` and the anchor becomes
   *derived*. The `planckP1/P2/P3` narrowings target sub-pieces of BP
   (substrate-to-`P_A`, hidden-character `δ=0`, orientation) and would need
   independent retained-grade audit.
2. **Audit-or-reground the forward chain.** Every forward step is `unaudited`,
   not no-go; promotion is an audit-lane action, not a new mechanism.
3. **Classification (deferred, per item S):** decide whether the one
   Planck-mass anchor is an *admitted empirical import* or a *framework-native
   unit declaration* — orthogonal to the dimensionless physics either way.

## Boundaries

- Sets no audit/effective status; promotes nothing; retires no admission.
- Uses no PDG/CODATA value as a derivation input (CODATA `G, ħ, c, M_Pl` appear
  CHECK-ONLY to confirm dimensional identities).
- Adds no axiom, primitive, or import; changes no row's grade.
- Does not assert closure: the verdict is the *current state*
  (OPEN-SELF-CONSISTENCY), not a claim that the closure is impossible. The
  `(BP) ⇒ a/l_P = 1` relation remains a live route to a derived anchor.

## Cross-references (plain-text, non-load-bearing)

- `ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` (item S — the anchor)
- `PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md` (package posture)
- `PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md` (`(BP) ⇒ a/l_P = 1`)
- `PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27.md` (one-anchor meta)
- `G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4.md`
- `GRAVITY_CLEAN_DERIVATION_NOTE.md` (lattice-units closure)
- `PLANCK_FINITE_RESPONSE_NO_GO_NOTE_2026-04-24.md`,
  `PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO_NOTE_2026-04-24.md`,
  `PLANCK_BOUNDARY_ORIENTATION_INCIDENCE_NO_GO_NOTE_2026-04-30.md`

## Validation

```bash
python3 scripts/cl3_scale_axis_planck_anchor_selfconsistency_2026_06_05.py
```

Expected: 16 PASS / 0 FAIL; `VERDICT: OPEN-SELF-CONSISTENCY`.
