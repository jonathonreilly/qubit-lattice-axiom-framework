# DM Leptogenesis PMNS Minimum-Information Source Law

**Type:** open_gate
**Claim type:** open_gate
**Claim boundary:** post-axiom selector diagnostic / open selector gate; not a
selector theorem and not retained PMNS-branch authority
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Date:** 2026-04-16; 2026-06-12 numerical-match firewall repair; 2026-06-18
open-gate source repair
**Primary runner:** [`scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py`](../scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py)
**Cached output:** [`logs/runner-cache/frontier_dm_leptogenesis_pmns_mininfo_source_law.txt`](../logs/runner-cache/frontier_dm_leptogenesis_pmns_mininfo_source_law.txt)
**Framework baseline:** one-qubit operator algebra on the `Z^3` lattice.

## Scope and honest framing

This note documents the consequences of **adopting** a downstream selector
law on the charged-lepton-active `N_e` branch. The selector law itself is an
explicit definition; it is not derived here from the baseline framework.

The note is therefore a **conditional** result:

> IF the minimum-information selector law (defined below) is adopted as a
> downstream convention on the fixed native `N_e` seed surface, THEN the
> companion runner finds a reproducible low-cost off-seed source on the
> frozen seed-0 search's representative column after imposing
> `eta_{i_*} / eta_obs = 1`.

The deriving-the-selector question — does the baseline framework itself force the
information cost `I_seed` (or some equivalent functional) to be the correct
selector? — is **not** answered here. It is the subject of separate sister
notes (see the relative-action stationarity theorem and the observable
relative-action law, both of which strengthen this framing by rebuilding the
objective from a framework-internal scalar `log|det|` observable principle).

## Source repair for re-audit (2026-06-18)

The prior top-level `bounded_theorem` label overstated what this row can
source. The audited load-bearing move is the **definition** of a selector
objective plus the imposed `eta_{i_*} / eta_obs = 1` equality constraint; the
runner computes consequences of that convention. It does not derive the
selector objective or equality constraint from the framework.

The repaired audit surface is therefore:

- **Open selector gate:** `I_seed` and the representative-column equality constraint
  remain supplied/adopted selector data.
- **Exact conditional diagnostic:** given that supplied selector surface, the
  runner computes a low-cost off-seed closure source on the favored column.
- **No retained-grade promotion:** this row must not be cited as a retained
  selector theorem, baseline PMNS-branch closure, or derivation of `I_seed`.

## Definition of the law

On the fixed native charged-lepton-active seed surface with

- `xbar = 0.5633333333333334`
- `ybar = 0.30666666666666664`

define the information-deformation cost

`I_seed = D_KL(x || x_seed) + D_KL(y || y_seed) + (1 - cos delta)`

where

- `x_seed = (xbar, xbar, xbar)`
- `y_seed = (ybar, ybar, ybar)`.

Then:

1. run the frozen seed-0, 20-iteration transport search and take its
   representative maximizing column `i_*` (column `0` for this fixture; not a
   unique physical column)
2. among all positive off-seed sources on that same seed surface satisfying
   `eta_{i_*} / eta_obs = 1`, choose the one minimizing `I_seed`.

This is the adopted selector law for the off-seed `5`-real source. It is a
choice of objective imported from information geometry. It is **not** derived
from `Cl(3)` on `Z^3`.

## Conditional output

If the law is adopted, the runner-verified selection is:

- `x_min = (0.47937029, 0.43463700, 0.77599271)`
- `y_min = (0.23114281, 0.39486835, 0.29398884)`
- `delta_min ~ 0`

so the off-seed source is

- `xi_min = (-0.08396304, -0.12869633, 0.21265938)`
- `eta_min = (-0.07552386, 0.08820168, -0.01267783)`
- `delta_min ~ 0`

and the resulting flavored transport values are

`eta / eta_obs = (1.0, 0.50519888, 0.78233530)`.

Conditional on the law and frozen search fixture, the representative column
remains column `0`, and exact closure is reached there.

## What this note does claim

- the minimum-information functional `I_seed` is a well-defined post-axiom
  selector convention on the fixed native seed surface
- conditional on adopting `I_seed`, the runner finds a feasible off-seed
  `5`-real source satisfying the imposed `eta_{i_*} / eta_obs = 1` constraint
- conditional on adopting `I_seed`, the selected closure source is strictly
  closer to the seed than the canonical near-closing sample, with
  `I_seed = 0.058549869343`
- conditional on adopting `I_seed`, the selected source still respects the
  representative column selected by the frozen seed-0 search

The runner output is a calibrated constrained-optimization diagnostic. It is
not a proof of global uniqueness, global stationarity classification, or
minimum-selector derivation from the baseline framework.

## What this note does NOT claim

- it does **not** claim that `I_seed` follows from the Lattice + Quantum +
  Record baseline
- it does **not** claim that the minimum-information functional is the
  unique correct selector — alternative selectors (relative bosonic action,
  multistart selector support, analytic stationary classification) all give
  matching low-action branches on the same reduced surface, but each is its
  own conditional framing
- it does **not** close the baseline-framework chain for the PMNS-assisted `N_e`
  branch — that question is parked at the relative-action stationarity
  theorem and the observable relative-action law
- it does **not** claim that transport extremality uniquely favors column `0`;
  longer searches expose permutation-related representatives in other columns

## Why this note is still useful

The note materially strengthens the closure picture in three ways:

1. it removes the residual arbitrariness of the earlier extremal candidate
   by giving a fully explicit, runner-reproducible selector
2. it confirms that the closure source on the favored column is genuinely
   off-seed but information-cheap (small KL deformation, near-zero phase),
   which is the qualitative expectation
3. it provides a baseline against which the stronger framework-internal
   selectors (`S_rel` and KKT classification) can be benchmarked

The note is therefore kept as bounded support rather than positive-theorem
authority. The closure on the PMNS-assisted `N_e` branch should be cited
through the sister theorems whose objectives are framework-internal, with
this note used only as a post-axiom selector diagnostic.

## Runner imports (transparency)

The runner imports the following local helpers from the same repository:

- `dm_leptogenesis_exact_common`: exact thermal package, `eta_obs`, etc.
- `frontier_dm_leptogenesis_flavor_column_functional_theorem`: transport
  kernel and column functional
- `frontier_dm_leptogenesis_pmns_active_projector_reduction`: active
  packet map
- `frontier_dm_leptogenesis_pmns_projector_interface`: canonical
  charged-block construction

These are not external libraries; they are sister modules in the same
research repo. Each has its own audit status; the present note inherits
their bounds.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py
```

## 2026-05-19 audit-conditional repair

This block narrows the source scope of the note to match what the
runner actually verifies and explicitly admits the information-geometric
selector as an imported assumption rather than a framework-derived
object.

### Imported admission (explicit)

The information-deformation cost

`I_seed = D_KL(x || x_seed) + D_KL(y || y_seed) + (1 - cos delta)`

and its use as the selection objective on the off-seed `5`-real source
are **imported from information geometry**. They are **not** derived from
the Lattice + Quantum + Record baseline. Any
language elsewhere in this note that could be read as implying the
selector emerges from the baseline framework is to be read through this
explicit admission: the selector is a downstream convention, adopted
here, with no claim to primitive-level derivation.

In particular:

- the **functional form** of `I_seed` (KL on the seed columns plus
  `(1 - cos delta)` phase deformation cost) is a convention from
  information geometry, not a primitive
- the **choice** to minimize `I_seed` (as opposed to any other consistent
  cost) is a convention, not a primitive
- the **seed columns** `x_seed = (xbar, xbar, xbar)` and
  `y_seed = (ybar, ybar, ybar)` are fixed by the prior native
  charged-lepton-active seed surface; their use as reference distributions
  for KL is part of the imported selector setup

### Narrowed source scope (open_gate)

After this repair, the source-side claim of this note is narrowed to the
following bounded conditional numerical diagnostic:

> **Bounded conditional diagnostic.** Given (a) the imported
> information-geometric selector `I_seed` and (b) representative column `i_*`
> from the frozen seed-0 transport-search fixture, the
> constrained optimization problem
>
> "minimize `I_seed` over positive off-seed sources on the fixed native
>  charged-lepton-active seed surface subject to `eta_{i_*} / eta_obs = 1`"
>
> has the runner-verified feasible optimizer output reported above
> (`I_seed = 0.058549869343`, representative column `0`, `delta_min ~ 0`).

The runner does not prove that this point is the unique global stationary point
on the exact closure manifold. It verifies the calibrated constrained
optimizer output under the adopted selector and imposed `eta_obs` equality.

Everything outside this constrained-opt closure on the favored column
(including the broader question of whether `I_seed` is the *correct*
selector, whether the baseline framework selects it over alternatives,
or whether the PMNS-assisted `N_e` branch closes from primitives) is
**explicitly out of source scope** for this note.

### Caveats

- this note is an `open_gate` with explicit imported/adopted selector
  assumptions; it is not a positive-theorem or bounded-theorem authority for
  the PMNS-assisted `N_e` branch
- this note may be used only for post-axiom interpretation of the frozen
  representative-column source, not for a unique favored-column theorem
- the constrained-opt diagnostic asserted above is conditional on the imported
  selector, the frozen representative-column fixture, and the imposed
  `eta_{i_*} / eta_obs = 1` constraint; none of those bridge a baseline
  framework derivation here

## 2026-05-22 audit-graph hygiene: no-retained-parent science backlog

The audit-renaming verdict reflects that the minimum-information source
law is an explicit selector definition (a convention, not a derived
primitive). No retained framework derivation of the selector currently
exists.

**9 downstream PMNS rows import this row as the `minlaw` selector
comparator** for their constrained-optimization runners. Those chains
stay conditional on the selector-law convention until it is derived from
baseline.

**Audit-dispatch parent candidate:** If a future independent audit
evaluates whether this source-law row is a non-chain-closing
alias/decorative handle, the candidate parent is
[`DM_LEPTOGENESIS_PMNS_ANALYTIC_STATIONARY_CLASSIFICATION_THEOREM_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_ANALYTIC_STATIONARY_CLASSIFICATION_THEOREM_NOTE_2026-04-16.md)
for the stationary classification. The renaming-tier source-law row is
the explicit selector convention layered on top of that classification.
This is source-side routing context only; it does not assert an
`audit_status` or `effective_status`.

## 2026-07-12 current-baseline non-entailment result

The first-principles stretch attempt now has a separate exact negative result:
[DM Leptogenesis PMNS Minimum-Information Current-Baseline Non-Entailment No-Go](DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_CURRENT_BASELINE_NON_ENTAILMENT_NO_GO_NOTE_2026-07-12.md)
constructs one explicit model of the current four axioms and two conservative
downstream completions that disagree on the minimization principle, modality
weights, observational closure anchor, and favored column.

That companion does not positively supply the selector law. This row therefore
remains an `open_gate`, and its existing runner remains a conditional
optimizer after the law and `eta_obs` equality are supplied. Downstream
positive consumers remain conditional on a separate positive selector and
normalization bridge.
