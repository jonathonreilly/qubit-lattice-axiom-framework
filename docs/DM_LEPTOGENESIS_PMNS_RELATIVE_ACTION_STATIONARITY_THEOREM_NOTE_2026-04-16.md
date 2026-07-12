# DM Leptogenesis PMNS Relative-Action Stationarity Theorem

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-16 (2026-05-18: claim_scope formalized as
positive-cone logdet Legendre identity + sampled local numerical
branch check conditional on missing helper machinery, per audit
verdict boundary instruction).
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-18 narrowing):** the load-bearing content
of this note is **(i) the positive-cone logdet Legendre identity** on
the explicitly-stated positive-cone surface, and **(ii) a sampled
local numerical branch check** on the runner's tested points,
**conditional on the missing helper machinery** (observable-relative
action law + W_rel/H_seed/eta + favored-column closure construction).
These two pieces hold as exact algebraic identity + sampled
numerical verification respectively, conditional on the helper-
runner imports `scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py`
behaving as named. The note **does NOT** independently retain those
helper imports or derive the underlying W_rel/H_seed/eta/favored-
column structure from `Cl(3)` on `Z^3`. The audit verdict's repair
sub-target ("include scripts/.../observable_relative_action_law.py
and a theorem deriving W_rel, H_seed, eta, and favored-column closure
from the foundation, then re-audit") remains separate
open work.
**Status authority:** independent audit lane only.
**Script:** `scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py`
**Framework convention:** the current foundation is Lattice, Qubit,
Admissibility, and Record.

## Question

After the PMNS-assisted `N_e` flavored-DM route was reduced to the fixed seed
surface plus one off-seed selector, was the remaining selector law still an
extra postulate?

More sharply:

- the conditional packet supplies the scalar generator
  `W = log|det(D+J)| - log|det D|`
- the fixed `N_e` seed pair is supplied by the helper packet
- the favored closure column is returned by the imported transport calculation
- observed closure is reached conditionally by minimizing

`S_rel(H_e || H_seed) = Tr(H_seed^{-1} H_e) - log det(H_seed^{-1} H_e) - 3`

The remaining issue was whether this stationarity/minimization step was merely
an extra selector ansatz.

## Bottom line

The positive-cone Legendre identity is exact once its log-det generator is
supplied. It defines `S_rel`; it does not derive a physical rule that selects
the constrained minimum. The exact independence boundary is proved in
[`DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md).

On the supplied fixed `N_e` seed surface and imported favored closure column,
sampled constrained solves expose more than one stationary branch, but only one
branch is the unique lowest-action closure branch among all sampled feasible
starts. That branch is a strict local minimum under sampled near-exact
closure-preserving perturbations.

## Exact effective-action identity

Write the seed-normalized charged Hermitian block as

`Y = H_seed^(-1/2) H_e H_seed^(-1/2)`.

Then the seed-relative bosonic action is

`S_rel(Y) = Tr(Y) - log det(Y) - 3`.

For Hermitian source matrices `K > -I`, define the seed-normalized scalar
observable generator

`W_rel(K) = log det(I + K)`.

Then

`S_rel(Y) = sup_K [ W_rel(K) - Tr(KY) ]`

with unique maximizer

`K_* = Y^(-1) - I`.

So `S_rel` is the exact Legendre dual of the supplied generator on the positive
charged block. This closes the algebraic identity only. The selector objective
and its physical minimization remain separate supplied conditions.

## Closure-surface stationarity

On the refreshed DM branch:

1. the fixed charged seed parameterization is supplied
2. the favored closure column is returned by the imported transport-extremal
   calculation
3. the flavored observed-closure condition is supplied:

`eta_{i_*}(H_e) / eta_obs = 1`

Given the supplied minimum-action law, its conditional PMNS-assisted closure
source satisfies:

`delta[ S_rel(H_e || H_seed) - lambda (eta_{i_*}(H_e)/eta_obs - 1) ] = 0`,

with the calculator choosing the lowest-action sampled solution of this
equation. The word “physical” is not implied by the KKT equation.

The script verifies:

- the constrained Euler-Lagrange equation
- positive tangent Hessian on the selected closure branch
- more than one sampled stationary branch
- uniqueness of the lowest-action branch across all sampled feasible starts
- strict local minimality under sampled near-exact closure-preserving
  perturbations

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

The numerical-closure branch of this note (the "Numerical result on the
current branch" section below, and Parts 2-3 of
`scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py`)
depends on the helper module
`scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py`
for the seed matrix `H_SEED`, the active-source parameterization, the
favored-column construction via `eta_columns_from_active` / `best_eta_from_params`,
and the seed-relative action `relative_action_h`. The audit verdict
explicitly says the algebraic positive-cone Legendre identity closes on
its own (it is fully self-contained in the section "Exact effective-action
identity" above and in Part 1 of the runner). The functions below are
inlined verbatim from the helper module so that the numerical-branch
computation is visible inside the restricted packet without requiring
external resolution of the helper import. They are reproduced for
visibility only; the load-bearing implementation lives in the helper
module file path above.

Provenance: copied verbatim from
`scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py`
at branch `physics-loop/audited-cond-dm-lepto-pmns-action-2026-05-18`,
2026-05-18.

### H_seed (supplied fixed N_e seed matrix)

```python
from frontier_dm_leptogenesis_pmns_projector_interface import canonical_h

XBAR_NE = 0.5633333333333334
YBAR_NE = 0.30666666666666664
X_SEED = np.full(3, XBAR_NE, dtype=float)
Y_SEED = np.full(3, YBAR_NE, dtype=float)
H_SEED = canonical_h(X_SEED, Y_SEED, 0.0)
H_SEED_INV = np.linalg.inv(H_SEED)
```

### Active-source parameterization (input to eta / favored-column / W_rel)

```python
def soft3(u: float, v: float, total: float) -> np.ndarray:
    logits = np.array([u, v, 0.0], dtype=float)
    logits -= np.max(logits)
    weights = np.exp(logits)
    weights /= np.sum(weights)
    return total * weights


def build_active_from_params(params: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    ax, ay, bx, by, delta = np.asarray(params, dtype=float)
    x = soft3(ax, ay, 3.0 * XBAR_NE)
    y = soft3(bx, by, 3.0 * YBAR_NE)
    return x, y, float(delta)
```

### eta computation (flavored asymmetry on the fixed seed surface)

```python
from dm_leptogenesis_exact_common import (
    C_SPH,
    D_THERMAL_EXACT,
    ETA_OBS,
    S_OVER_NGAMMA_EXACT,
    exact_package,
)
from frontier_dm_leptogenesis_flavor_column_functional_theorem import (
    flavored_column_functional,
    flavored_transport_kernel,
)
from frontier_dm_leptogenesis_pmns_active_projector_reduction import active_packet_from_h

PKG = exact_package()
Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL = flavored_transport_kernel(PKG.k_decay_exact)


def eta_columns_from_active(x: np.ndarray, y: np.ndarray, delta: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    h_e = canonical_h(x, y, delta)
    packet = active_packet_from_h(h_e).T
    etas = np.array(
        [
            S_OVER_NGAMMA_EXACT
            * C_SPH
            * D_THERMAL_EXACT
            * PKG.epsilon_1
            * flavored_column_functional(packet[:, idx], Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL)
            / ETA_OBS
            for idx in range(3)
        ],
        dtype=float,
    )
    return h_e, packet, etas
```

### Favored-column construction (transport-extremal class)

```python
def best_eta_from_params(params: np.ndarray) -> float:
    x, y, delta = build_active_from_params(params)
    _h, _packet, etas = eta_columns_from_active(x, y, delta)
    return float(np.max(etas))


# Favored column i_* is selected as the argmax of etas at the
# transport-extremal source on the fixed seed surface. The extremal
# source itself is found by differential_evolution maximizing
# best_eta_from_params:
#
#     result = differential_evolution(
#         lambda p: -best_eta_from_params(np.asarray(p, dtype=float)),
#         bounds=[(-4,4)]*4 + [(-pi, pi)],
#         seed=0, maxiter=20, popsize=10, polish=False,
#     )
#     x_opt, y_opt, delta_opt = build_active_from_params(result.x)
#     _h, _packet, etas_opt = eta_columns_from_active(x_opt, y_opt, delta_opt)
#     i_star = int(np.argmax(etas_opt))
#
# On the current refreshed DM branch this yields i_star == 0.
```

### W_rel / seed-relative action (numerical branch evaluation)

```python
def relative_action_h(h_e: np.ndarray) -> float:
    m = H_SEED_INV @ h_e
    sign, logdet = np.linalg.slogdet(m)
    if sign <= 0:
        raise ValueError("relative-action matrix left the positive branch")
    return float(np.trace(m).real - logdet - 3.0)
```

The Legendre-dual identity itself (`S_rel(Y) = sup_K [ log det(I+K) - Tr(KY) ]`
with `K_* = Y^{-1} - I`) is the algebraic positive-cone identity already
established in the "Exact effective-action identity" section above; it is
self-contained and does not require any helper code. The functions
inlined above are exactly the numerical-branch machinery required to (i)
construct the favored column `i_*`, (ii) evaluate `eta_{i_*}` along
candidate sources, and (iii) evaluate `S_rel` on those sources. With them
the "Numerical result on the current branch" values below are reproducible
from inside the restricted packet.

## Numerical result on the current branch

The stationary source is the same observable-relative-action closure source:

- `x_stat = (0.471675, 0.553811, 0.664514)`
- `y_stat = (0.208063, 0.464383, 0.247554)`
- `delta_stat ~ 0`

and it gives exact closure on the favored column:

- `eta / eta_obs = (1.0, 0.75917896, 0.48458840)`

So the old exact one-flavor miss

- `eta_obs / eta = 5.297004933778`

is removed inside the supplied observed-closure calculation. This is not a
prediction of `eta_obs` and not a derivation of the selector.

## What this closes

This closes the positive-cone dual identity and records sampled conditional
stationarity/local-minimum evidence. It does not close the selector principle:
“choose the lowest-action closure branch” remains the supplied law tested by
the numerical parts.

## What this does not claim

This note does **not** claim:

1. a branch-global analytic proof that no second disconnected closure component
   exists anywhere else on the full seed surface
2. a full PMNS microscopic solve beyond the current branch
3. a framework derivation of the physical minimum-action selector

The current theorem is:

- exact at the Legendre-dual algebra level
- branch-exact at the closure equation level
- sampled lowest-action branch / local-minimum evidence on the conditional
  closure patch

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16](DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md)
  (exact selector-independence boundary; negative dependency, not positive
  selector authority)
- [dm_leptogenesis_pmns_relative_action_conditional_calculator_note_2026-07-12](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_CONDITIONAL_CALCULATOR_NOTE_2026-07-12.md)
  (conditional numerical helper and supplied objective)
- [dm_leptogenesis_pmns_projector_interface_note_2026-04-16](DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md)
- [dm_leptogenesis_pmns_active_projector_reduction_note_2026-04-16](DM_LEPTOGENESIS_PMNS_ACTIVE_PROJECTOR_REDUCTION_NOTE_2026-04-16.md)
- [dm_leptogenesis_flavor_column_functional_theorem_note_2026-04-16](DM_LEPTOGENESIS_FLAVOR_COLUMN_FUNCTIONAL_THEOREM_NOTE_2026-04-16.md)
