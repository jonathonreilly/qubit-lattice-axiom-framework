# DM/Leptogenesis PMNS: I_seed Selector Route Probes — Computed Witnesses Locating the Adopted Selector's Non-Baseline Content (2026-07-02)

## Claim (support-grade route diagnosis; no promotion)

Three refutation-shaped, machine-checked probes locate **where** the non-baseline
content of the adopted minimum-information source selector lives, using the gate
note's own objects (its exact fixed native seed surface, its exact `I_seed`
functional, and its exact transport map — imported, not re-implemented):

1. **P1 (state-contingency of the favored column):** the transport-favored column
   `i_* = argmax_i eta_i` is not fixed by the axiom surface alone — two
   law-admissible realized states on the *same* fixed native seed surface
   transport-favor *different* columns.
2. **P2 (modality-weighting dependence of the information functional):** the
   argmin of the `I_seed` functional over an explicit finite off-seed candidate
   bank flips under a legitimate positive reweighting of its x-modality and
   y-modality KL blocks — the equal-modality weighting inside `I_seed` is a
   weighting principle doing selective work.
3. **P3 (independence of the equality constraint):** the anchoring equality
   `eta_{i_*} / eta_obs = 1` is not implied by the note's other premises — explicit
   admissible models satisfy every other premise with ratio ≠ 1.

**Claim type:** support-grade diagnostic of an existing adopted-selector gate.
This note derives nothing, promotes nothing, and authors no audit status. It
gives the already-scoped gate a *computed decomposition into three named
non-baseline pieces*, each a separately attackable derivation target.

## Context: the gate being mapped

The gate note
[DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md)
(non-retained; ledger `effective_status: audited_conditional` in the generated
audit ledger at the date of this note) states a two-step selection law: (1)
determine the transport-favored flavor column `i_*` from the exact
transport-extremal class; (2) among positive off-seed sources on the fixed
native seed surface satisfying `eta_{i_*}/eta_obs = 1`, minimize
`I_seed = D_KL(x||x_seed) + D_KL(y||y_seed) + (1 - cos delta)`.

That note scopes its own audit surface explicitly:

> - **Open selector gate:** `I_seed` and the favored-column equality constraint
>   remain supplied/adopted selector data.
> - **Exact conditional diagnostic:** given that supplied selector surface, the
>   runner computes a low-cost off-seed closure source on the favored column.
> - **No retained-grade promotion:** this row must not be cited as a retained
>   selector theorem, baseline PMNS-branch closure, or derivation of `I_seed`.

and states that the selector objective and constraint are a "choice of objective
imported from information geometry. It is **not** derived from `Cl(3)` on `Z^3`."
This note takes that scope as given and asks the next question: *what exactly*
about the selector is non-baseline? The answer decomposes into three pieces,
each witnessed by computation below. The diagnosis holds against the current
four-axiom baseline (Lattice, Qubit, Admissibility, Record): none of the four
supplies an information functional, a modality weighting, or an observational
anchoring equality, so the pieces named here are non-baseline against the
current base, not only the base at the gate note's date.

All probe objects are reused from the gate row, none invented:

- Seed surface: `x_seed = (xbar, xbar, xbar)`, `y_seed = (ybar, ybar, ybar)` with
  `xbar = 0.5633333333333334`, `ybar = 0.30666666666666664`.
- `I_seed` identical (same L1-normalized KL blocks, same phase term) to the gate
  runner's `info_cost`.
- Transport map `eta_i(x, y, delta)` assembled from the same module stack the
  gate runner imports (`canonical_h` → `active_packet_from_h` →
  `flavored_column_functional` with the exact package constants), with
  `eta_obs = 6.12e-10`. The eta ratios below are the note's real transport
  object, not a proxy.

## The three probes and their computed witnesses

### P1 — the favored column i_* is realized-state-contingent

**Hypothesis (refutable):** two law-admissible realized states on the same fixed
native seed surface transport-favor different columns. A FAIL (an exhaustive
on-surface grid favoring a single column everywhere) would have meant the column
is surface-rigid and step (1) of the law *is* axiom-surface data.

**Witness (computed):** assignment A favors column 0 at
`x = [0.076521, 0.076521, 1.536959]`, `y = [0.10506, 0.038649, 0.776291]`,
`delta = 0` (`eta/eta_obs = [0.468627, 0.468618, 0.219751]`); assignment B
favors column 1 at the same `x`,
`y = [0.041656, 0.041656, 0.836688]`, `delta = 0`
(`eta/eta_obs = [0.442683, 0.442683, 0.222029]`). Both verified on the fixed
native seed surface (mean-`xbar`/mean-`ybar` checks pass at 1e-12).

**Reading:** step (1) of the adopted law consumes state-contingent registered
data. Under the registered `realized_state` primitive this is pointwise-legal
but not axiom-derivable: quantities that vary across the law-admissible family
remain registered data, so no axiom-surface-only argument pins `i_*` without
importing the realized state.

### P2 — the I_seed functional presupposes a modality-weighting principle

**Hypothesis (refutable):** over the same finite bank of admissible off-seed
sources, the argmin of the uniform `I_seed` and the argmin of a legitimately
modality-weighted `I_seed^{wx,wy}` (positive weights on the x-block and y-block
KL divergences; `(1,1)` recovers `I_seed` exactly) disagree. A FAIL (coinciding
argmins) would have meant the selection is weighting-invariant.

**Witness (computed, bank of 191 explicit off-seed sources, exact seed
excluded):** uniform argmin at `x = [0.498593, 0.822041, 0.369367]`, `y` at
seed, `delta = 0`, `I_seed = 0.055557445`; modality-weighted
`(wx, wy) = (2, 0.5)` argmin at `x` at seed,
`y = [0.271423, 0.447501, 0.201075]`, `delta = 0`, `I_seed^w = 0.027778722`.
`(1,1)` reproduces the gate runner's `info_cost` exactly; both minima are
strictly positive proper information costs (each KL block is a genuine
non-negative divergence under positive weights), so the flip is not a
sign/rounding artifact. Emphasizing the x-modality over the y-modality moves the
cheapest source from an x-off-seed/y-at-seed point to an x-at-seed/y-off-seed
point.

**Precision — what P2 does and does not diagnose:** the gate note's step (2)
minimizes `I_seed` *subject to* the equality constraint
`eta_{i_*}/eta_obs = 1`; P2 evaluates the **unconstrained** argmin of the
information functional over an explicit finite bank. P2 therefore diagnoses the
weighting-dependence of the functional itself — the equal-modality weighting
`(wx, wy) = (1, 1)` inside `I_seed` is an unstated normalization choice doing
selective work before the constraint ever enters — and **not** the behavior of
the constrained selector's output under reweighting (that would require
searching the equality-constrained feasible set, which this note does not
construct).

**Reading:** even prior to the constraint, the objective embeds a weighting
principle the axioms do not supply. This is the second named piece of the
adopted content.

### P3 — the equality constraint is an independent imposed premise

**Hypothesis (refutable):** the equality `eta_{i_*}/eta_obs = 1` is not implied
by the note's other premises (fixed native seed surface + positive source +
transport-favored-column identification). A FAIL (every admissible on-surface
positive favored-column model forcing ratio = 1) would have meant the equality
is a consequence, not an imposition.

**Witness (computed):** model A = the pure seed `(x_seed, y_seed, delta = 0)` —
on-surface, positive, `i_* = 1`, `eta_{i_*}/eta_obs = 0.719082664` (deviation
−0.280917336). Model B = an off-seed admissible source
`x = [0.940049, 0.283137, 0.466814]`, `y = [0.166053, 0.451379, 0.302568]`,
`delta = 0.4` — on-surface, positive, `i_* = 0`,
`eta_{i_*}/eta_obs = 0.908774422` (deviation −0.091225578). Both satisfy every
other premise of the law with ratio ≠ 1.

**Reading:** the equality does not follow from the other premises; it is exactly
the "favored-column equality constraint" the gate scope names as
supplied/adopted — an observation-anchoring premise imposed independently.

## Route diagnosis: three separately attackable pieces

The adopted selector's non-baseline content decomposes as:

1. **State-contingency of `i_*`** (P1) — transport-facing: the favored column is
   registered data of the realized state, not axiom-surface data.
2. **Modality weighting inside `I_seed`** (P2) — information-geometry-facing:
   the equal-weight combination of the two KL blocks is an unstated selection
   principle.
3. **The anchoring equality** (P3) — observation-facing: `eta_{i_*}/eta_obs = 1`
   is an independent imposed premise tying the source to the observed asymmetry.

These are independent targets: deriving any one of the three from the four-axiom
baseline would strictly shrink this gate, and the decomposition tells a future
derivation attempt which piece it is actually attacking. This note deliberately
does not rank the three; each is the next path this diagnosis opens on its own
face.

## realized_state primitive discipline

Every realized state used by the probes is a single explicit supplied point on
the fixed native seed surface, evaluated pointwise. No measure, ensemble,
typicality, genericity, or weighting assumption is used *by the probes*; the
modality weighting examined in P2 is a diagnosed property of the adopted
functional, not a weighting adopted here. State-contingent values (which column
is favored, the eta ratios) are reported as registered data of the supplied
points.

## Scope and honest framing (what this note does not do)

- It does **not** derive `I_seed`, the modality weighting, the favored-column
  rule, or the equality constraint from the axioms. The gate note's open
  selector gate stands exactly as scoped there.
- It does **not** author or predict audit grades; the ledger citation above is
  descriptive of the generated ledger at the date of writing.
- It proposes **no** retained-grade or theorem-grade status for itself; it is
  support-grade route diagnosis.
- Each probe is refutation-shaped and could have failed (surface-rigid column /
  weighting-invariant argmin / equality forced by the other premises); a
  computed miss would have been reported as a FAIL, not disguised.
- P2's finding is scoped to the functional, not the constrained output (see the
  precision paragraph in P2).

## Runner

`python3 scripts/dm_iseed_selector_route_probes_2026_07_02.py` — prints the
witnesses quoted above and `TOTAL: PASS=3 FAIL=0`; cached at
`logs/runner-cache/dm_iseed_selector_route_probes_2026_07_02.txt`. The runner
imports the transport map from the gate runner's own module stack and excludes
the exact seed from the P2 bank so both reported minima are strictly positive.

## Cited dependencies

- [DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md)
  — the gate row under diagnosis: supplies the seed surface, `I_seed`, the
  two-step law, and the open-selector-gate scope quoted above.
- [DM_LEPTOGENESIS_EXACT_KERNEL_CLOSURE_NOTE_2026-04-15.md](DM_LEPTOGENESIS_EXACT_KERNEL_CLOSURE_NOTE_2026-04-15.md)
  — exact package constants (`epsilon_1`, `k_decay_exact`, thermal/sphaleron
  factors) used by the transport map.
- [DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md)
  — `flavored_column_functional` and the flavored transport kernel.
- [DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md)
  — `active_packet_from_h` (active-sector packet from the effective h).
- [DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md)
  — `canonical_h` (the canonical source-to-h interface).

Context only (no dependency edge intended):
`DM_LEPTOGENESIS_PMNS_CONSTRAINED_OPTIMIZATION_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-17.md`
isolates the calculus identity of the constrained argmin step; P2 here is
complementary (it probes the functional's weighting, not the constrained
optimization algebra).
