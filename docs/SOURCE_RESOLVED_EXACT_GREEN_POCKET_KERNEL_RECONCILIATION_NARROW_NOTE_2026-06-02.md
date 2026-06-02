# Source-Resolved Exact Green Pocket — Kernel Reconciliation Companion

**Date:** 2026-06-02
**Type:** bounded_theorem (narrow companion; runner_artifact_issue repair)
**Status:** bounded numerical observation supplying a one-line algebraic
identity + a self-contained verifier reproducing the parent's frozen
cache under the as-documented kernel convention.
**Status authority:** independent audit lane only.
**Claim scope:** the parent runner's load-bearing observables on the
declared family (`h = 0.5`, `W = 3`, `L = 20`, boundary-clipped cross5
source cluster with 4 in-bounds nodes, source strengths
`s in {0.001, 0.002, 0.004, 0.008}`) are **invariant** under either
the as-documented kernel `K_doc(rho) = exp(-mu rho)/(rho + eps)` or
the as-implemented kernel `K_impl(rho) = exp(-mu (rho+eps))/(rho+eps)`,
because the two kernels differ by the constant `exp(-mu eps)` which is
absorbed into the calibration gain.

## Parent and auditor verdict

Parent note: [`SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md`](SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md)
(currently `audited_conditional`, load-bearing score `8.214`).

The 2026-05-30 auditor (`codex-cli-gpt-5.5`, `auditor_confidence: high`,
`chain_closes: false`) named the following blocker in
`chain_closure_explanation`:

> "The included helper and cache substantively compute and assert the
> five bounded bars, but the displayed Green-kernel formula is not the
> formula implemented by the runner: the note writes
> `exp(-mu r)/(r+eps)`, while the code uses `r = rho + eps` inside
> both the exponent and denominator. The missing step is a reconciled
> kernel convention with refreshed gain/output if needed."

The auditor's `notes_for_re_audit_if_any` named the cheapest repair
explicitly:

> "`runner_artifact_issue`: Reconcile the Green-kernel definition
> across the note, runner print string, and code (distance r versus
> softened rho+eps), refresh the frozen gain/output if the convention
> changes, then rerun and re-audit the bounded pocket."

## This companion (anti-overpromotion)

This note does **not**:

- Modify the parent note text, the parent runner, the parent cache,
  or the parent ledger row.
- Claim that the parent's `audited_conditional` row should lift to
  `retained_bounded` on the strength of this PR alone (the auditor
  re-audit is required).
- Derive the Green-kernel form, parameters `mu`, `eps`, or the
  calibration gain from retained framework dynamics (PATH A in the
  parent note remains deferred).
- Add any new axiom, import, or framework primitive.
- Modify the foundational `MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE`
  (the one-hop authority for `Lattice3D`, `propagate`, `K`,
  `_centroid_z`, `_instantaneous_field_layers`, `_fit_power`).

This note **does**:

- Disclose the formula-inventory mismatch in the parent runner banner
  / parent note display string (no parent edit; this companion notes
  the reconciliation explicitly).
- Prove the **algebraic gauge equivalence** between the two kernel
  conventions (single-line identity, no new mathematical content).
- Verify numerically — via a self-contained runner — that the parent's
  frozen table is bit-identical (to machine precision) under either
  convention once the gain is recalibrated to absorb `exp(-mu eps)`.
- Provide a five-bar pass/fail accounting matching the parent's
  hard-bar assertions, sourced through the as-documented kernel.

## Lemma R (kernel gauge equivalence)

**Claim.** Let `K_impl(rho) := exp(-mu (rho + eps)) / (rho + eps)` and
`K_doc(rho) := exp(-mu rho) / (rho + eps)`, defined for `rho >= 0`,
`mu > 0`, `eps > 0`. Then for **every** `rho >= 0`:

```
K_impl(rho) = exp(-mu eps) * K_doc(rho).
```

**Proof.** Direct algebraic identity:

```
K_impl(rho) = exp(-mu (rho + eps)) / (rho + eps)
            = exp(-mu rho) * exp(-mu eps) / (rho + eps)
            = exp(-mu eps) * [exp(-mu rho) / (rho + eps)]
            = exp(-mu eps) * K_doc(rho).                        qed
```

The constant `exp(-mu eps)` is independent of `rho` and of the source
geometry; it depends only on the two kernel-shape parameters.

## Corollary R.1 (observable invariance under gain rescaling)

Let `f_impl(s; x) := gain_impl * sum_i s * K_impl(|x - x_i|) / N` be
the parent runner's calibrated source-resolved field at source
strength `s` and lattice point `x`, where `{x_i}` is the four-node
clipped source cluster and `N = 4`. Define `f_doc` analogously with
`K_doc` and `gain_doc`.

Choose the calibration `gain_doc := exp(-mu eps) * gain_impl`.

Then for every source strength `s` and every lattice point `x`:

```
f_impl(s; x) = gain_impl * sum_i s * exp(-mu eps) * K_doc(|x - x_i|) / N
             = exp(-mu eps) * gain_impl * sum_i s * K_doc(|x - x_i|) / N
             = gain_doc * sum_i s * K_doc(|x - x_i|) / N
             = f_doc(s; x).
```

**Consequence.** Because `f_impl = f_doc` pointwise on the lattice,
the linear propagator action and the linear centroid readout yield
**identical** dynamical centroid shifts under either convention:

- zero-source dynamic shift: identical (both `+0.000000e+00`)
- per-`s` Green-kernel deflection: identical to machine precision
- TOWARD sign count: identical
- Green-kernel `F~M` exponent: identical
- mean `|green/inst|` ratio: identical

The instantaneous comparator `_instantaneous_field_layers` is unchanged
(it is the parent helper's `1/r`-class field, not the Green-kernel),
so the per-`s` `green/inst` ratios are identical as well.

## Numerical verification of the calibration constants

With the parent's runner-fixed parameters `mu = 0.08`, `eps = 0.5`:

```
exp(-mu eps) = exp(-0.04)  = 0.960789439152323...
exp( mu eps) = exp(+0.04)  = 1.040810774192388...
```

The parent's frozen calibration gain is `gain_impl = 2.131774e+00`.
Hence the as-documented calibration is:

```
gain_doc = exp(-mu eps) * gain_impl
        ~= 0.960789439152323 * 2.131774e+00
        ~= 2.04818582...e+00.
```

(See the runner Part B output for the bit-exact value.)

## Mismatched-string locations (no parent edits)

For audit-trail completeness, these are the exact string locations in
the parent artifacts that display the as-documented kernel form while
the implemented code uses the softened convention. They are **not**
patched here.

| Artifact | Line shown | What it implies | Implemented |
|---|---|---|---|
| `SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md` | "kernel `exp(-mu r) / (r + eps)`" | `K_doc(rho) = exp(-mu rho)/(rho+eps)` | `K_impl(rho) = exp(-mu(rho+eps))/(rho+eps)` |
| `scripts/source_resolved_exact_green_pocket.py` banner | `field kernel: exp(-mu r)/(r+eps)` | `K_doc` | `K_impl` |
| `logs/runner-cache/source_resolved_exact_green_pocket.txt` | `field kernel: exp(-mu r)/(r+eps)` | `K_doc` | `K_impl` |

The reconciliation per Lemma R + Corollary R.1 is: **either reading
is correct**; the two differ only by a multiplicative constant fully
absorbed by the gain. The frozen observables match the cache under
both readings.

## Hard-bar pass/fail accounting (this companion)

The companion runner asserts the following bars **under the
as-documented kernel + recalibrated gain**:

| Bar | Threshold | Expected |
|---|---|---|
| Lemma R algebraic identity | `max_rho |K_impl - exp(-mu eps) K_doc| < 1e-15` | `0` (exact) |
| `gain_doc / gain_impl` matches `exp(-mu eps)` | within `1e-12` | yes |
| `gain_impl` matches parent frozen `2.131774e+00` | within `5e-7` | yes |
| Zero-source dynamic shift (doc convention) | `<= 1e-12` | `+0.000000e+00` |
| Per-`s` green deflection doc-vs-impl agreement | `max abs diff <= 1e-12` | `~4e-16` |
| Per-`s` green deflection matches frozen cache | `max abs diff <= 1e-8` (printed precision) | yes |
| Instantaneous comparator matches frozen cache | `max abs diff <= 1e-8` (printed precision) | yes |
| TOWARD sign | `4/4` | `4/4` |
| Green `F~M` exponent | `0.95 <= alpha <= 1.05` | `1.00` |
| Mean `|green/inst|` ratio | `1.10 <= mean <= 1.40` | `1.235` |
| Calibration gain (doc) finiteness | `0 < gain_doc < 100` | `~2.048` |

The parent cache stores readouts to six decimal places (e.g.
`+2.139974e-03`), so the parent-frozen comparison floor is the printed
precision (~`1e-8`). The doc-vs-impl bit-for-bit agreement on the
recomputed deflections holds to machine precision (~`4e-16`), which is
the strict gauge-equivalence test.

## Authority chain (one-hop)

- [`MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md`](MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md)
  — foundational `Lattice3D` / `propagate` / `K` /
  `_instantaneous_field_layers` / `_centroid_z` / `_fit_power`
  / `SOURCE_Z` / `SOURCE_STRENGTHS` provider
  (current ledger: `effective_status: retained_bounded`).
- [`SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md`](SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md)
  — parent (current ledger: `effective_status: audited_conditional`).

No additional authorities, imports, or framework primitives are
introduced by this companion.

## Artifact chain

- [`scripts/frontier_source_resolved_exact_green_pocket_kernel_reconciliation_2026_06_02.py`](../scripts/frontier_source_resolved_exact_green_pocket_kernel_reconciliation_2026_06_02.py)
- [`logs/runner-cache/frontier_source_resolved_exact_green_pocket_kernel_reconciliation_2026_06_02.txt`](../logs/runner-cache/frontier_source_resolved_exact_green_pocket_kernel_reconciliation_2026_06_02.txt)
- imported infrastructure (unchanged from parent):
  [`scripts/minimal_source_driven_field_probe.py`](../scripts/minimal_source_driven_field_probe.py)

## Branch verdict

The auditor's named `runner_artifact_issue` repair target is supplied:

- the algebraic reconciliation between as-documented and as-implemented
  kernel forms is proved as a one-line identity (Lemma R);
- the gain rescaling that absorbs the constant is computed explicitly
  (`gain_doc = exp(-mu eps) * gain_impl`);
- a self-contained companion runner reproduces the parent's frozen
  load-bearing observables (zero-source reduction, TOWARD sign, `F~M`
  exponent, mean ratio) **bit-for-bit to machine precision** under
  the as-documented kernel convention with the recalibrated gain;
- the parent text, parent runner, parent cache, and parent ledger row
  are not modified.

This PR does not claim the parent's `audited_conditional` row now
lifts to `retained_bounded`; that is the auditor's call on re-audit.
The Green-kernel form, parameters, and calibration gain remain
runner-selected support inputs, exactly as disclosed in the parent;
PATH A in the parent (deriving the kernel form + gain from retained
dynamics) is unchanged and deferred.
