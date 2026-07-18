# DM Leptogenesis PMNS Minimum-Information Source Law

**Type:** open_gate
**Claim boundary:** downstream selector diagnostic / open selector gate; not a
selector theorem and not retained PMNS-branch authority
**Date:** 2026-04-16; 2026-06-12 numerical-match firewall repair; 2026-06-18
open-gate source repair
**Primary runner:** [`scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py`](../scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py)
**Cached output:** [`logs/runner-cache/frontier_dm_leptogenesis_pmns_mininfo_source_law.txt`](../logs/runner-cache/frontier_dm_leptogenesis_pmns_mininfo_source_law.txt)
**Framework baseline:** Lattice, Qubit, Admissibility, and Record, with the
one-qubit operator algebra on the `Z^3` lattice.

## Scope and honest framing

This note documents the consequences of **adopting** a downstream selector
law on a supplied finite matrix/transport fixture. The selector law, seed
surface, column index, and physical interpretation are explicit conditions;
none is derived here from the baseline framework.

The note is therefore a **conditional** result:

> IF the minimum-information selector law (defined below) is adopted as a
> downstream definition on the fixed supplied seed surface, and IF the finite
> fixture column index `i_* = 0` and all transport inputs are supplied, THEN
> the companion runner finds one reproducible feasible, interior, locally
> stationary off-seed candidate after imposing `eta_{i_*} / eta_obs = 1`.

The deriving-the-selector question — does the baseline framework itself force the
information cost `I_seed` (or some equivalent functional) to be the correct
selector? — is **not** answered here. No theorem cited by this row closes that
physical selector bridge.

## Source repair for re-audit (2026-06-18)

The prior top-level `bounded_theorem` label overstated what this row can
source. The audited load-bearing move is the **definition** of a selector
objective plus the imposed `eta_{i_*} / eta_obs = 1` equality constraint; the
runner computes consequences of that definition. It does not derive the
selector objective or equality constraint from the framework.

The repaired audit surface is therefore:

- **Open selector gate:** `I_seed` and the supplied-column equality constraint
  remain supplied/adopted selector data.
- **Conditional numerical diagnostic:** given that supplied selector surface,
  the runner computes a feasible local candidate at the supplied column.
- **No retained-grade promotion:** this row must not be cited as a retained
  selector theorem, baseline PMNS-branch closure, or derivation of `I_seed`.

## Definition of the law

On the fixed supplied seed surface with

- `xbar = 0.5633333333333334`
- `ybar = 0.30666666666666664`

define the information-deformation cost

`I_seed = D_KL(x/sum(x) || x_seed/sum(x_seed))`
`       + D_KL(y/sum(y) || y_seed/sum(y_seed)) + (1 - cos delta)`

where

- `x_seed = (xbar, xbar, xbar)`
- `y_seed = (ybar, ybar, ybar)`.

The normalization is part of the adopted definition. Then:

1. adopt the finite-fixture column index `i_* = 0`
2. among all positive off-seed sources on that same seed surface satisfying
   `eta_{i_*} / eta_obs = 1`, seek local stationary candidates for `I_seed`.

This is the adopted selector law for the off-seed `5`-real source. It is a
choice of objective imported from information geometry. It is **not** derived
from `Cl(3)` on `Z^3`.

## Conditional output

If the law and all finite-fixture inputs are adopted, the runner returns the
following feasible local SLSQP candidate:

- `x_min = (0.47937029, 0.43463700, 0.77599271)`
- `y_min = (0.23114281, 0.39486835, 0.29398884)`
- `delta_min ~ 0`

so the off-seed source is

- `xi_min = (-0.08396304, -0.12869633, 0.21265938)`
- `eta_min = (-0.07552386, 0.08820168, -0.01267783)`
- `delta_min ~ 0`

and the resulting flavored transport values are

`eta / eta_obs = (1.0, 0.50519888, 0.78233530)`.

Conditional on the supplied index `i_* = 0`, the equality residual at column
`0` is at numerical precision. The runner also verifies successful local-solver
termination, interiority relative to its parameter bounds, a nonzero constraint
gradient, and an independent finite-difference KKT residual below `1e-5`.

## What this note does claim

- the minimum-information functional `I_seed` is a well-defined downstream
  selector definition on the fixed supplied seed surface
- conditional on adopting `I_seed`, `i_* = 0`, and the listed fixtures, the
  runner finds a feasible, interior, locally stationary off-seed `5`-real
  candidate satisfying the imposed `eta_{i_*} / eta_obs = 1` constraint
- the candidate has the computed value `I_seed = 0.058549869343`; this scalar
  is not compared with an uncomputed reference candidate

The runner output is a local constrained-optimization diagnostic. It is not a
proof of global minimality, global uniqueness, global stationarity
classification, a physical column selector, or minimum-selector derivation
from the baseline framework. The bounded initialization search carries no
extremal or column-selection authority.

## What this note does NOT claim

- it does **not** claim that `I_seed` follows from the Lattice + Qubit +
  Admissibility + Record baseline
- it does **not** claim that the minimum-information functional is the
  unique correct selector; comparisons with other supplied objectives are
  conditional diagnostics rather than selector authority
- it does **not** close the baseline-framework chain for the PMNS-assisted `N_e`
  branch

## Why this note is still useful

The note records the conditional finite-fixture calculation in three ways:

1. it gives a fully explicit, runner-reproducible local-search definition
2. it exhibits one off-seed feasible local candidate with small computed KL
   deformation and near-zero phase, without promoting that observation to a
   global or physical conclusion
3. it provides a finite-fixture baseline for comparisons with other supplied-objective
   diagnostics, without promoting any comparison to selector authority

The note is therefore kept as bounded support rather than positive-theorem
authority. No physical closure bridge is cited or load-bearing here; this note
is used only as a downstream conditional numerical diagnostic.

## Runner imports (transparency)

The runner imports the following local helpers from the same repository, but
repository locality does not make their inputs framework-derived:

- [`scripts/dm_leptogenesis_exact_common.py`](../scripts/dm_leptogenesis_exact_common.py):
  the numerical fixtures
  `PLAQ_MC = 0.5934`, `g_bare = 1`, `M_PL = 1.2209e19`,
  `G_WEAK = 0.653`, `ETA_OBS = 6.12e-10`, `k_A = 7`, `k_B = 8`,
  `gamma = 1/2`, `E1 = sqrt(8/3)`, `E2 = sqrt(8)/3`, and `K00 = 2`,
  together with the stated thermal, entropy, radiation, and sphaleron formulas
- [`DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md): transport
  equations, source and washout profiles, boundary data, discretized kernel,
  and column functional
- [`DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md): active
  finite eigensolve packet map
- [`DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md): supplied
  matrix-chart construction

The seed pair, `I_seed`, supplied column `i_* = 0`, the finite seeded
initialization protocol, and the imposed ratio equality are additional explicit
conditions of this row. Every listed item is a conditional fixture or
comparator here, not a framework derivation or physical authority.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py
```

## 2026-05-19 audit-conditional repair

This block narrows the source scope of the note to match what the
runner actually verifies and explicitly admits the information-geometric
selector as an imported assumption rather than a framework-derived
object.

### Explicit imported condition

The information-deformation cost

`I_seed = D_KL(x/sum(x) || x_seed/sum(x_seed))`
`       + D_KL(y/sum(y) || y_seed/sum(y_seed)) + (1 - cos delta)`

and its use as the selection objective on the off-seed `5`-real source
are **imported from information geometry**. They are **not** derived from
the Lattice + Qubit + Admissibility + Record baseline. Any
language elsewhere in this note that could be read as implying the
selector emerges from the baseline framework is to be read through this
explicit condition: the selector is a downstream definition, adopted
here, with no claim to primitive-level derivation.

In particular:

- the **functional form** of `I_seed` (KL on the seed columns plus
  `(1 - cos delta)` phase deformation cost) is a definition from
  information geometry, not a primitive
- the **choice** to search using `I_seed` (as opposed to any other consistent
  cost) is a supplied definition, not a primitive
- the **seed columns** `x_seed = (xbar, xbar, xbar)` and
  `y_seed = (ybar, ybar, ybar)`, their normalization for KL, and the column
  index `i_* = 0` are supplied finite-fixture inputs

### Narrowed source scope (open_gate)

After this repair, the source-side claim of this note is narrowed to the
following bounded conditional numerical diagnostic:

> **Bounded conditional diagnostic.** Given (a) the imported
> information-geometric selector `I_seed`, (b) the supplied finite-fixture
> column `i_* = 0`, and (c) all transport and matrix-chart inputs, the local
> constrained optimization problem
>
> "seek local stationary candidates for `I_seed` over positive off-seed
>  sources on the fixed supplied seed surface subject to
>  `eta_{i_*} / eta_obs = 1`"
>
> has the runner-verified feasible, interior, locally stationary candidate
> reported above (`I_seed = 0.058549869343`, supplied column `0`,
> `delta_min ~ 0`).

The runner does not prove that this point is a global minimizer or the unique
global stationary point on the equality manifold. It verifies local-solver
success, feasibility, interiority, constraint regularity at the candidate, and
a numerical KKT residual under the adopted selector and imposed `eta_obs`
equality.

Everything outside this local constrained diagnostic on the supplied column
(including the broader question of whether `I_seed` is the *correct*
selector, whether the baseline framework selects it over alternatives,
or whether the PMNS-assisted `N_e` branch closes from primitives) is
**explicitly out of source scope** for this note.

### Caveats

- this note is an `open_gate` with explicit imported/adopted selector
  assumptions; it is not a positive-theorem or bounded-theorem authority for
  the PMNS-assisted `N_e` branch
- no physical closure bridge is cited or load-bearing here; this note remains
  only a downstream finite-fixture diagnostic
- the constrained-opt diagnostic asserted above is conditional on the imported
  selector, the supplied column index, and the imposed
  `eta_{i_*} / eta_obs = 1` constraint; none of those bridge a baseline
  framework derivation here

## 2026-05-22 audit-graph hygiene: no-retained-parent science backlog

The minimum-information source law is an explicit selector definition (a
supplied choice, not a derived primitive). No framework derivation of the selector
is cited or load-bearing in this note.

Dependent rows that import this row as the `minlaw` selector comparator remain
conditional on the selector-law definition; this source note provides no
physical promotion.

A former stationary-classification parent reference is withdrawn. The
historical row now proves only an abstract Hermitian-product
conjugation-parity theorem for an explicitly supplied matrix family, so it is
not a parent or authority for the present source-law diagnostic.
