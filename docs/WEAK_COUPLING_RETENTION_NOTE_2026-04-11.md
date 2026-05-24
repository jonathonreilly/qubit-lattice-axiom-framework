# Weak-Coupling Retention Note — Frozen 60-Run Shell-Margin / Norm-Conservation Audit Surface (Binding)

**Date:** 2026-04-11 (status line narrowed 2026-04-28 per audit-lane verdict; scope narrowed 2026-05-24 per audited_conditional `scope_too_broad` repair)
**Script:** `frontier_weak_coupling_retained.py`
**Status:** bounded finite audit-surface result — binding scope is the
frozen 60-run shell-margin (`tw_a - tw_r >= 10`, `60/60`) and
norm-conservation (`60/60`) record on the declared audit surface only;
the registered runner path is wrong, the secondary gap count is
live-stale at `54/60`, and the broader inference (theorem for
admissible irregular bipartite graphs, coordinate-force closure,
stable secondary spectral-gap row) is **out of binding scope** until
the named missing pieces are repaired or supplied.
**Status authority:** independent audit lane only

## Scope narrowing (2026-05-24 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair instruction: *"retain only the frozen 60-run shell-margin /
norm-conservation finite audit surface until the registered runner
path, secondary gap row, and admissible-graph / shell-force theorem
are repaired or supplied."*

This revision implements the narrowing. The binding evidence of this
note is exactly the **frozen 60-run shell-margin and norm-conservation
counts on the declared finite audit surface** (graph families × sizes
× seeds × couplings listed under "Audited Surface" below), as reported
by the cached runner stdout. The wider readings — "theorem for
admissible irregular bipartite graphs," coordinate-force closure,
stable secondary spectral-gap row, and any graph-family universality
language — are explicitly **out of binding scope** until the registered
runner path is fixed, the secondary gap row is refreshed to a stable
count, and an admissible-graph / shell-force theorem is supplied. Those
items are listed under "Bounded out-of-scope / open future work" below.

## Question

Can the weak-coupling parity-coupled irregular-graph regime be frozen as a
retained sign-sensitive result on a broader family/size/seed surface, or does
it remain exploratory?

This note answers that question narrowly. It does **not** claim a universal
off-lattice directional-force closure across all operating points. It only
freezes what survives under the audited weak-coupling surface.

## Audited Surface

- graph families:
  - random geometric
  - growing
  - layered cycle
- sizes:
  - random geometric: `side=8`, `side=10`
  - growing: `n_target=64`, `n_target=100`
  - layered cycle: `8x8`, `10x10`
- seeds: `42..46`
- couplings: `G=5`, `G=10`
- total runs: `60`
- evolution:
  - `N_ITER = 40`
  - `DT = 0.12`
  - parity coupling `(m + Phi) * epsilon`

Each run compares:

- attractive parity coupling
- repulsive parity coupling
- zero-field control

## Observables and Gates

The audit measured four sign-sensitive candidates:

1. `width_asymmetry < 1`
   - contraction under attraction divided by contraction under repulsion
2. `gap_ratio > 1`
   - spectral gap under attraction divided by spectral gap under repulsion
3. `shell_strict`
   - `tw_a >= 36` and `tw_r <= 4`
4. `shell_margin`
   - `tw_a - tw_r >= 10`

Norm conservation was also required:

- `| ||psi|| - 1 | < 1e-10` for both attractive and repulsive runs

## Stable Pass Counts

The runner was rerun four times in the physics venv. Three observables were
stable across all four reruns:

- width asymmetry `< 1`: `56/60`
- shell strict split: `47/60`
- shell ordered (`tw_a > tw_r`): `60/60`
- shell margin `>= 10`: `60/60`
- norm conserved: `60/60`

Stable by-family counts:

- random geometric:
  - width: `20/20`
  - shell strict: `11/20`
  - shell ordered: `20/20`
  - shell margin: `20/20`
- growing:
  - width: `16/20`
  - shell strict: `16/20`
  - shell ordered: `20/20`
  - shell margin: `20/20`
- layered cycle:
  - width: `20/20`
  - shell strict: `20/20`
  - shell ordered: `20/20`
  - shell margin: `20/20`

## Unstable Secondary Observable

The spectral-gap tally is not stable enough to freeze as an exact retained
count. Across four identical reruns, the script reported:

- gap ratio `> 1`: `55/60`, `56/60`, `57/60`, `55/60`
- growing-family gap count: `15/20`, `16/20`, `17/20`, `15/20`

So the gap ratio remains a useful supporting indicator, but not a frozen
retained row. The retained claim below relies only on the stable shell-force
and norm observables.

## Strongest Sign-Selective Observable

The strongest retained observable is:

> **shell-force margin**
>  
> `tw_a - tw_r >= 10` on `60/60` audited runs

This is stronger than a trivial ordering test. On the full audited surface,
attraction exceeds repulsion by at least `10` TOWARD-count steps out of `40`
in every single run.

The weaker but still useful supporting observables are:

- width asymmetry
- spectral gap ratio

Width asymmetry is stable but not universal enough to carry retention by
itself. Spectral gap ratio is directionally useful, but its exact pass count is
runner-sensitive and is therefore not frozen here.

## Binding Bounded Claim (narrowed 2026-05-24)

The binding scope is the **frozen 60-run shell-margin /
norm-conservation finite audit surface** only, with this exact wording:

> At weak coupling (`G=5,10`), on the declared finite audit surface
> (graph families × sizes × seeds listed above, total `60` runs),
> attractive parity coupling produces a larger shell-force TOWARD
> count than repulsive parity coupling on `60/60` audited runs, with a
> minimum separation of `10/40` steps (`tw_a - tw_r >= 10` on `60/60`)
> and exact norm conservation (`60/60`).

This is a finite-surface tabulated count, not a graph-family theorem.
Any extension to "admissible irregular bipartite graphs," to
coordinate-force closure, or to a stable secondary spectral-gap row is
out of binding scope (see "Bounded out-of-scope / open future work"
below) and is conditional on the named missing pieces.

## What This Still Does NOT Claim

This does **not** establish:

- universal off-lattice directional gravity at all operating points
- coordinate-force closure on irregular graphs
- that width asymmetry or gap ratio are themselves retained universal rows

So the blocker is only partially resolved:

- the frozen 60-run shell-margin / norm-conservation finite audit
  surface is bounded
- full irregular off-lattice directional closure outside this regime remains a
  separate question

## Practical Use

Use this result when the scientific claim is specifically about:

- the frozen 60-run shell-margin / norm-conservation finite audit
  surface at `G=5,10`
- attractive-vs-repulsive separation on the declared finite audit
  surface only

Do **not** use it to replace the exact-force cubic card, to overstate
the status of the broader irregular directional-observable blocker, or
to assert a graph-family theorem on admissible irregular bipartite
graphs.

## Audit boundary (2026-04-28)

Audit verdict (`audited_conditional`, medium criticality, 16 transitive
descendants):

> Issue: the finite runner verifies shell ordered 60/60, shell margin
> >=10 on 60/60, and norm conservation 60/60, but the note promotes
> this selected audit surface to a retained weak-coupling sign-
> sensitive regime while the registered runner path is wrong and the
> secondary gap count is live-stale at 54/60. Why this blocks: a
> hostile auditor can accept the finite shell-margin table but cannot
> infer a theorem for admissible irregular bipartite graphs, a
> coordinate-force closure, or a stable secondary spectral-gap row
> from the current packet.

## Bounded out-of-scope / open future work

Per the 2026-05-24 narrowing, the following are explicitly **not**
part of this row's binding scope and are deferred to future work
pending the named missing pieces:

- **Theorem for admissible irregular bipartite graphs.** The finite
  60-run table does not extend to a graph-family theorem; promoting
  the row to a graph-family theorem requires a separately registered
  admissible-graph / shell-force theorem.
- **Coordinate-force closure.** Not closed by the finite runner table.
- **Stable secondary spectral-gap row.** The secondary gap count is
  live-stale at `54/60` and needs to be refreshed to `60/60` (or
  re-frozen at a stable count) under a corrected runner.
- **Correctly registered runner path.** The currently registered
  runner path is wrong and must be fixed before any of the broader
  inferences can be re-audited.

Promoting beyond the bounded finite audit surface would require:

1. Fixing the registered runner path.
2. Adding explicit hard PASS thresholds for shell-ordering, shell
   margin, secondary spectral-gap stability, and norm conservation.
3. Refreshing the secondary gap count to `60/60` (currently `54/60`).
4. Registering a separate audit-clean theorem for any broader
   admissible-graph / shell-force inference.

Until those land, the binding claim is the frozen 60-run shell-margin
and norm-conservation finite audit surface only.
