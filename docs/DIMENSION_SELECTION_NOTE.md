# Dimension Selection Lower-Bound Finite-k Repair

**Date:** original dimension-selection note; 2026-05-27 lower-bound scope
repair.
**Claim type:** bounded_theorem
**Status:** finite-runner lower-bound support only. This row does not claim
that self-consistency uniquely selects `d = 3`, does not import the textbook
upper-bound side as a load-bearing premise, and does not authorize any axiom
rewrite. Independent audit owns the effective status.
**Runner:** `scripts/frontier_dimension_selection_lower_bound_parent_repair.py`

## 2026-05-27 Scope Repair

The prior note mixed two statements:

1. a finite runner lower-bound observation: the runner's attraction/mass-law
   criteria fail for `d <= 2` and pass for `d = 3,4,5`;
2. a broader unique-`d = 3` conclusion using separate orbital and atomic
   stability inputs.

Only the first statement is binding in this row. The second statement remains
context for separate upper-bound work and is not a theorem of this packet.

The finite-k sign bridge
[`DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`](DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md)
is the retained-bounded authority for the runner-specific lower-bound sign.
It differentiates the actual layer-normalized finite-k propagator used by
`scripts/frontier_dimension_selection.py`, rather than importing WKB/eikonal
ray reasoning as the load-bearing sign argument.

**Date:** 2026-04 (2026-05-28: scoped to the numerical lower-bound experiment;
the d≤3 upper bound and the analytic d-dim potential/sign bridge registered as
admitted inputs per audit path (b)).
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Status:** bounded **numerical lower-bound experiment** — self-consistency on
the tested lattice excludes `d ≤ 2` (requires `d ≥ 3` for attractive gravity
with linear mass dependence), GIVEN the analytic d-dimensional potentials as
admitted inputs. The **`d ≤ 3` upper bound** (orbital/atomic stability) and the
**axiom → analytic-potential / sign-criterion bridge** are admitted inputs, not
derived here; the unique-`d = 3` conclusion is conditional on them.

## 2026-05-28 Audit Repair (lower-bound experiment; upper bound + potential bridge admitted)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The numerical lower-bound experiment is present, but the broader d = 3
> conclusion also imports an upper bound from stable orbits/atoms that is not
> provided as a cited retained authority in this packet. The runner
> additionally measures gravity using hand-coded analytic d-dimensional
> potentials in 2D propagation, so the bridge from the stated axiom to those
> potentials and sign criterion is not closed inside the packet."*

with the offered repair: provide retained authorities or a self-contained
derivation for the `d ≤ 3` upper bound and for the analytic d-dimensional
potential/sign bridge.

This revision takes the **split/admission path** (a retained derivation of the
upper bound and of the analytic potentials from the axiom is substantive new
work, out of scope):

- **Load-bearing (in scope):** the **numerical lower-bound experiment**. On
  the tested lattice, self-consistent propagate→density→Poisson iteration plus
  the phase-coupling sign analysis shows attractive gravity with linear mass
  dependence requires `d ≥ 3` (i.e. self-consistency **excludes `d ≤ 2`**).
  This is the runner-verified content, **conditional on the analytic
  d-dimensional potentials supplied as inputs**.
- **Admitted / NON-load-bearing (split off):**
  1. **Analytic d-dimensional potential + sign bridge.** The runner uses
     hand-coded potentials (`φ ~ −M·r`, `−M·log r`, `−M/r`, `−M/r²`, …) and the
     phase-coupling sign criterion. The derivation of these from the framework
     axiom is **not closed here**; they are admitted inputs.
  2. **`d ≤ 3` upper bound.** Bertrand's stable-orbit theorem (`d = 3` is the
     only dimension with stable closed orbits under the `1/r^{d−1}` force) and
     hydrogen-like atomic stability (`d ≥ 5` unstable) are **admitted
     classical/quantum stability inputs**, not retained one-hop authorities in
     this packet.

The unique `d = 3` selection is therefore the **lower bound (numerical) ∧ the
two admitted inputs**. The note already states (§"Bounded Conclusion") that
"the script does not claim that self-consistency alone selects d = 3." No new
axiom, import, or retained bridge is introduced by this repair.

## Answer

No. The current retained/bounded result is narrower:

```text
d <= 2  -> fails the runner's attractive-gravity / beta~1 lower-bound criteria
d >= 3  -> passes those runner criteria for d = 3, 4, 5
```

Thus this row supports a finite-runner lower bound, not a unique-dimension
theorem.

## Runner Surface

For each dimension `d = 1,2,3,4,5`, the original runner:

1. builds a finite lattice or finite propagation model;
2. uses the stated analytic `d`-dimensional potential family
   - `d = 1`: `phi ~ -M r`;
   - `d = 2`: `phi ~ -M log(r)`;
   - `d >= 3`: `phi ~ -M / r^(d-2)`;
3. measures force sign, mass exponent `beta`, distance exponent `alpha`, and
   a linear-propagator Sorkin `I_3` check.

The finite-k bridge supplies the direct runner-specific sign certificate for
the detector-centroid response at the baseline geometry.

## Bounded Result

The runner output reports:

| d | attractive? | beta approx | `I_3` | lower-bound read |
|---|---|---:|---|---|
| 1 | no | 0.18 | `<1e-10` | fails |
| 2 | no | 0.27 | `<1e-10` | fails |
| 3 | yes | 1.01 | `<1e-10` | passes |
| 4 | yes | 1.05 | `<1e-10` | passes |
| 5 | yes | 1.03 | `<1e-10` | passes |

The finite-k derivative bridge independently certifies the same sign
transition for the runner's baseline centroid observable:

```text
d <= 2: negative/away response
d >= 3: positive/toward response
```

This is the bounded claim of this row.

## Non-Claims

This row does not claim:

- that `d = 3` is uniquely selected by the three runner observables;
- that the all-d analytic potential family is derived from A1+A2 alone;
- that Bertrand, Tangherlini, Ehrenfest, or atomic-stability upper bounds are
  proved in this row;
- that `Z^3` has been derived from a dimension-free axiom system;
- that any repo-wide axiom line should be rewritten;
- that observed physical dimension is an admitted data input.

## Relation To Upper-Bound Work

The separate upper-bound wrapper
`DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` combines
this lower-bound route with named external upper-bound mathematics. That
wrapper is not load-bearing for the bounded claim here. Any future attempt to
derive `d <= 3` inside the framework must be audited separately.

## What This Closes

- finite-runner lower-bound support for excluding `d <= 2` in the stated
  propagator-plus-Poisson runner surface;
- direct use of the retained-bounded finite-k centroid-sign bridge;
- removal of the unique-`d = 3` overclaim from this parent row.

## What Remains Open

- framework-internal derivation of the all-d potential family;
- uniform control over all runner geometries, `k`, source widths, and positive
  masses;
- framework-internal upper-bound derivation `d <= 3`;
- any axiom-level dimension rewrite.

## Verification

Run:

```bash
python3 scripts/frontier_dimension_selection_lower_bound_parent_repair.py
```

Expected summary:

```text
SUMMARY: PASS=29 FAIL=0
```
