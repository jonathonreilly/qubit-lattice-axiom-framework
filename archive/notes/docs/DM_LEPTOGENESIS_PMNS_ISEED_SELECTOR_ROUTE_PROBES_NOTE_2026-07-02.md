# DM/Leptogenesis PMNS: I_seed Selector Route Probes — Computed Witnesses Locating the Adopted Selector's Non-Baseline Content (2026-07-02)

**Type:** bounded_theorem
**Claim type:** bounded_theorem (bounded support diagnostic of an existing adopted-selector gate)
**Scope boundary:** the bounded theorem content is the three computed finite
probes P1-P3 locating choices and contingencies inside the adopted selector
fixture. It does not derive `I_seed`, the favored-column rule, or the equality
constraint from the four-axiom baseline, and it does not establish a
framework-wide no-go.
**Audit boundary:** the independent audit lane owns all `audit_status` and
`effective_status` verdicts.

## Claim (support-grade route diagnosis; no promotion)

Three refutation-shaped, machine-checked probes locate choices and
contingencies inside the adopted minimum-information source selector fixture,
using the gate note's supplied fixed-sum seed surface, adopted `I_seed`
functional, and supplied finite transport map:

1. **P1 (finite-fixture contingency of the favored column):** two supplied
   positive points on the *same* fixed-sum seed surface robustly
   transport-favor *different* columns, with an explicit top-two separation
   threshold.
2. **P2 (modality-weighting dependence of the information functional):** the
   argmin of the `I_seed` functional over an explicit finite off-seed candidate
   bank flips under a legitimate positive reweighting of its x-modality and
   y-modality KL blocks — the equal-modality weighting inside `I_seed` is a
   weighting principle doing selective work.
3. **P3 (independence of the equality constraint):** the anchoring equality
   `eta_{i_*} / eta_obs = 1` is not implied by the note's other premises — explicit
   supplied positive models satisfy every other tested premise with ratio ≠ 1.

This note promotes nothing and authors no audit status. It gives the
already-scoped gate three named finite diagnostics. It does not prove those
diagnostics are pairwise-independent derivation walls.

## Context: the gate being mapped

The gate note
[DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md)
states a two-step selection law: (1)
determine the finite-fixture flavor column `i_*` from the supplied transport
map; (2) among positive off-seed sources on the supplied fixed-sum seed surface
satisfying `eta_{i_*}/eta_obs = 1`, minimize
`I_seed = D_KL(x||x_seed) + D_KL(y||y_seed) + (1 - cos delta)`.

That note scopes its own audit surface explicitly:

> - **Open selector gate:** `I_seed` and the favored-column equality constraint
>   remain supplied/adopted selector data.
> - **Exact conditional diagnostic:** given that supplied selector surface, the
>   runner computes a low-cost off-seed closure source on the favored column.
> - **No retained-grade promotion:** this row must not be cited as a retained
>   selector theorem, baseline PMNS-branch closure, or derivation of `I_seed`.

and states that the selector objective and constraint are a "choice of objective
imported from information geometry. It is **not** derived from the current
four-axiom framework baseline."
This note takes that scope as given and asks which finite choices can be
isolated computationally. Direct inspection of the current four axiom
statements (Lattice, Qubit, Admissibility, Record) finds no definition of this
information functional or observational anchoring equality. That premise check
does not exclude every possible future bridge theorem.

The seed surface, uniform `I_seed`, and transport map are reused from the gate
row. P2 intentionally constructs a positive reweighting as a diagnostic
variation:

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

### P1 — the favored column i_* is contingent on the supplied finite point

**Hypothesis (refutable):** two supplied positive points on the same fixed-sum
seed surface transport-favor different columns with top-two separation greater
than `1e-6`. A FAIL would leave that finite-fixture contingency unsupported on
the tested grid.

**Witness (computed):** assignment A favors column 0 at
`x = [0.413591, 0.152152, 1.124257]`,
`y = [0.238737, 0.032310, 0.648954]`, `delta = 0.6`
(`eta/eta_obs = [1.049296, 0.642490, 0.632491]`, top-two margin
`0.406805941`); assignment B favors column 1 at
`x = [1.124257, 0.413591, 0.152152]`,
`y = [0.648954, 0.238737, 0.032310]`, `delta = 0.6`
(`eta/eta_obs = [0.632491, 1.049296, 0.642490]`, top-two margin
`0.406805941`). Both pass the fixed-sum mean checks at `1e-12`.

**Reading:** step (1) of the adopted law depends on which supplied finite point
is evaluated. The runner does not certify either point as a law-admissible
framework realization and makes no claim under the `realized_state` primitive.

### P2 — the I_seed functional presupposes a modality-weighting principle

**Hypothesis (refutable):** over the same finite bank of supplied positive off-seed
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

**Reading:** even prior to the constraint, the adopted objective embeds a
weighting choice. This is the second named finite diagnostic.

### P3 — the equality constraint is an independent imposed premise

**Hypothesis (refutable):** the equality `eta_{i_*}/eta_obs = 1` is not implied
by the note's other premises (supplied fixed-sum seed surface + positive source +
transport-favored-column identification). A FAIL (every tested positive
on-surface favored-column model forcing ratio = 1) would have left the
independence claim unsupported on the tested models.

**Witness (computed):** a supplied positive off-seed source
`x = [0.940049, 0.283137, 0.466814]`, `y = [0.166053, 0.451379, 0.302568]`,
`delta = 0.4` — on-surface, positive, `i_* = 0`,
`eta_{i_*}/eta_obs = 0.908774422` (deviation −0.091225578). This model
satisfies every other tested premise of the law with ratio ≠ 1.

**Reading:** the equality does not follow from the other premises; it is exactly
the "favored-column equality constraint" the gate scope names as
supplied/adopted — an observation-anchoring premise imposed independently.

## Route diagnosis: three separately named diagnostics

The adopted selector fixture exposes:

1. **Finite-point contingency of `i_*`** (P1) — transport-facing: the favored
   column changes between separated supplied points on the tested surface.
2. **Modality weighting inside `I_seed`** (P2) — information-geometry-facing:
   the equal-weight combination of the two KL blocks is an unstated selection
   principle.
3. **The anchoring equality** (P3) — observation-facing:
   `eta_{i_*}/eta_obs = 1` is independent of the other premises tested by the
   explicit finite witnesses.

These are separately named diagnostics, not a proved pairwise-independent wall
decomposition. Closing or replacing any one would change the adopted gate, but
this finite note does not rank them or prove that no common bridge could address
more than one.

## Supplied-point premise discipline

Every point used by the probes is an explicit supplied positive point on the
fixed-sum seed surface, evaluated pointwise. No measure, ensemble, typicality,
or genericity claim is made. The note does not establish law admissibility and
therefore does not invoke the `realized_state` primitive. The modality weighting
examined in P2 is an intentional diagnostic variation, not a framework premise.

## Scope and honest framing (what this note does not do)

- It does **not** derive `I_seed`, the modality weighting, the favored-column
  rule, or the equality constraint from the axioms. The gate note's open
  selector gate stands exactly as scoped there.
- It does **not** author or predict audit grades.
- It claims only the bounded finite diagnostics stated above and proposes no
  retained-grade promotion.
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
  — `flavored_column_functional` and the finite flavored transport kernel,
  conditional on supplied equations, profiles, boundary data, and packet; the
  probes do not inherit a physical yield or canonical-packet derivation.
- [DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md)
  — `active_packet_from_h` (active-sector packet from the effective h).
- [DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md)
  — `canonical_h` (the canonical source-to-h interface).

Context only (no dependency edge intended):
`DM_LEPTOGENESIS_PMNS_CONSTRAINED_OPTIMIZATION_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-17.md`
isolates the calculus identity of the constrained argmin step; P2 here is
complementary (it probes the functional's weighting, not the constrained
optimization algebra).
