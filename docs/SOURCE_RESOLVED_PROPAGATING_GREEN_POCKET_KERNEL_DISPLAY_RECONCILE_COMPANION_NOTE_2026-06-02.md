# Source-Resolved Propagating Green Pocket — Kernel-Display Reconcile Companion

**Date:** 2026-06-02
**Type:** meta
**Claim type:** meta
**Status:** runner-artifact reconciliation companion; source-note proposal
only, pipeline-derived status is set after independent audit review.
**Authority role:** companion to
[`SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md`](SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md).
Reconciles the displayed Green-kernel formula in the parent note with the
kernel the registered runner actually evaluates, and shows the displayed
and executed conventions produce **bit-identical scaled fields** under the
runner's self-consistent calibration so every downstream observable in the
parent's frozen table is convention-invariant.
**Primary runner:** [`scripts/audit_companion_source_resolved_propagating_green_pocket_kernel_display_reconcile.py`](../scripts/audit_companion_source_resolved_propagating_green_pocket_kernel_display_reconcile.py)
**Cache:** [`logs/runner-cache/audit_companion_source_resolved_propagating_green_pocket_kernel_display_reconcile.txt`](../logs/runner-cache/audit_companion_source_resolved_propagating_green_pocket_kernel_display_reconcile.txt)

## Authority disclaimer

This is a source-note proposal. Pipeline-derived status is generated only
after the independent audit lane reviews the claim, dependency chain, and
runner. This note **does not modify the parent
`SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md`**, does not promote it
from `audited_conditional`, does not lift its bounded scope, and does not
add any new physics import. It only addresses the auditor's named
`runner_artifact_issue` repair target by exhibiting the bit-identity that
makes the kernel-display discrepancy a notation issue rather than a
numerical one.

## Auditor's named repair target

Ledger row `source_resolved_propagating_green_pocket_note`
(`audited_conditional`, `effective_status_reason: terminal_audit`,
load-bearing score `7.187`) records the verdict:

> The numeric table, ratios, signs, mean memory offset, and runner
> assertions are computed rather than hard-coded and agree internally.
> However, the source packet displays the Green-kernel family as
> `exp(-mu r)/(r+eps)`, while the executable code applies
> `exp(-mu*(d+eps))/(d+eps)` when `d` is the Euclidean source distance,
> so the packet does not close as written for the displayed kernel
> convention.

with `notes_for_re_audit_if_any`:

> runner_artifact_issue: reconcile the displayed Green-kernel formula
> with the executable kernel, regenerate the runner cache, and re-audit
> the same finite packet.

## The two kernels

Let `d` be the Euclidean source-to-target distance, `mu = 0.08`,
`eps = 0.5`. The two kernel conventions are:

- **Displayed** (parent note line "field kernel: `exp(-mu r)/(r+eps)`",
  reading `r = d` as Euclidean distance):
  `K_disp(d) = exp(-mu d) / (d + eps)`
- **Executed** (registered runner
  `scripts/source_resolved_propagating_green_pocket.py`,
  `_source_resolved_green_field`, the lines
  `r = math.sqrt(...) + GREEN_EPS` then
  `val += source_strength * math.exp(-GREEN_MU * r) / r`):
  `K_exec(d) = exp(-mu (d + eps)) / (d + eps)`

These differ by a uniform multiplicative constant:

```
K_exec(d) = exp(-mu * eps) * K_disp(d)
```

with `exp(-mu*eps) = exp(-0.04) ≈ 0.960789439...` independent of `d`.

The auditor is right that, as a kernel-family name, these are not the
same formula. What this companion proves is that the runner's
self-consistent calibration step strictly cancels the
`exp(-mu*eps)` factor, so the scaled fields actually fed to the
amplitude propagator are bit-identical, and every downstream observable
in the parent's frozen table is convention-invariant.

## The cancellation theorem (statement)

**Claim.** Within the parent's declared finite packet
(`h = 0.5`, `W = 3`, `L = 20`, 4 in-bounds clipped cross-source nodes,
`s ∈ {0.001, 0.002, 0.004, 0.008}`, `mix = 0.9`,
`FIELD_TARGET_MAX = 0.02`, `mu = 0.08`, `eps = 0.5`, the registered
runner's static / source-resolved Green field and same-site-memory
propagating Green field), substituting `K_disp` for `K_exec` produces
**bit-identical** scaled Green and propagating-Green fields after the
runner's `gain = FIELD_TARGET_MAX / _field_abs_max(ref_raw)` calibration
step. Consequently every entry of the parent's frozen table
(`inst`, `green`, `prop` shifts, `prop/inst`, `prop/green` ratios,
zero-source reduction, F~M exponents, TOWARD-row count, mean ratios,
causal-memory observable `prop - green`) is identical under the two
kernel conventions to floating-point precision.

## Proof

Write `c = exp(-mu*eps)`. The unscaled Green field is computed
elementwise as a sum over source nodes:

```
ref_raw_exec[layer][i] = (1/N_src) * Σ_m  s * K_exec(d_{i,m})
                       = c * (1/N_src) * Σ_m  s * K_disp(d_{i,m})
                       = c * ref_raw_disp[layer][i]
```

(linearity in the kernel; `s` and `N_src` factor out). Therefore the
absolute maxima rescale by the same factor:

```
ref_max_exec = c * ref_max_disp
```

The runner's calibration line

```
gain = FIELD_TARGET_MAX / ref_max
```

then satisfies

```
gain_exec = FIELD_TARGET_MAX / ref_max_exec
          = FIELD_TARGET_MAX / (c * ref_max_disp)
          = gain_disp / c
```

Combining,

```
gain_exec * K_exec(d) = (gain_disp / c) * (c * K_disp(d))
                      = gain_disp * K_disp(d)
```

i.e. the **calibrated** Green field is identical under both conventions.
The propagating Green field is the layer-recurrence

```
prop[0]      = green[0]
prop[layer]  = mix * prop[layer-1] + (1 - mix) * green[layer]
```

which is linear in the input field, so it inherits the same identity:
`gain_exec * prop_exec = gain_disp * prop_disp`. The instantaneous
control `_instantaneous_field_layers` uses a *different* kernel
(`1/(d + 0.1)` from a single source node) and is propagated with NO
`gain` multiplier, so it is unaffected by either Green-kernel
convention.

The amplitude propagator `Lattice3D.propagate` accepts the calibrated
field layers as input and reads them through
`lf = 0.5*(sf[si] + df[di])`, `act = L*(1.0 - lf)`,
`amps += a_i * exp(i k act) * w / L^2`. Because the calibrated field
layers are bit-identical under the two conventions, the action `act`,
the per-edge phase `exp(i k act)`, and therefore the final amplitudes
`amps` are bit-identical. Hence every observable derived from
`_centroid_z(amps, lat)` — including `green_delta`, `prop_delta`,
`prop/inst`, `prop/green`, the F~M exponents, the TOWARD count, the
mean ratios, and the `prop - green` causal-memory offset — is
bit-identical.

The zero-source reduction is unaffected because the Green field
vanishes identically at `s = 0` under either convention, so the
calibration step is irrelevant.

QED.

## What the verifier actually checks (declared observable surface)

The companion runner
[`scripts/audit_companion_source_resolved_propagating_green_pocket_kernel_display_reconcile.py`](../scripts/audit_companion_source_resolved_propagating_green_pocket_kernel_display_reconcile.py)
instantiates the same lattice / source / parameter family as the parent
runner and computes both kernel conventions side by side. It asserts:

1. **Pointwise factor identity:** for every lattice node in the test
   packet, the unscaled ratio
   `K_exec(d) / K_disp(d) = exp(-mu*eps)` to floating-point precision.
2. **Calibrated-field bit-identity:** after the parent's
   `gain = FIELD_TARGET_MAX / ref_max` step, the calibrated Green
   field arrays for the two conventions agree to floating-point
   precision.
3. **Propagating-field bit-identity:** the calibrated propagating
   Green field arrays for the two conventions agree to floating-point
   precision (linearity check on the memory recurrence).
4. **Observable invariance:** for each `s` in the parent's source
   ladder, the centroid shifts (`green_delta`, `prop_delta`), the
   ratios (`prop/inst`, `prop/green`), and the causal-memory observable
   `prop - green` agree across conventions to floating-point precision.
5. **Frozen-value reproduction:** the executed-convention numerics
   reproduce the parent's frozen table entries to the displayed
   precision (`prop/green ≈ 1.149..1.150`, etc.), confirming the
   parent's audit-lane cache row.

The runner exits 0 (`ASSERTIONS: PASS`) when all five gates hold.

## What this companion does NOT do

- It does **not modify the parent
  `SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md`**. The parent
  retains its declared kernel display and frozen-table text. The audit
  ledger row may stay at `audited_conditional` until the independent
  audit lane decides whether the bit-identity argument here is enough
  to clear the runner-artifact issue.
- It does **not promote** the parent or change its `bounded_theorem`
  scope. The parent's bounded exact-lattice positive packet stays a
  bounded exact-lattice positive packet; no continuum / GR / horizon /
  finite-speed field-equation claim is introduced.
- It does **not add a new physics import** or admission. The runner
  computes both kernel conventions on the same retained lattice
  primitive (`scripts/minimal_source_driven_field_probe.py`), invokes
  only the parent's already-cited authority chain, and asserts only an
  algebraic identity (uniform multiplicative rescaling) plus the
  runner's self-consistent calibration logic.
- It does **not** decide whether the parent should be re-displayed
  with the executed kernel form `exp(-mu*(d+eps))/(d+eps)`. That
  cosmetic choice is left for the independent audit lane / a follow-up
  edit on the parent's text.

## Independence

This companion's runner builds the two kernel evaluations from scratch
in a single script (it imports only the lattice primitive from the
already-cited retained
[`MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE`](MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md)),
so the bit-identity assertion is cross-checked at a different abstraction
than the parent runner (which only evaluates one convention). The
verifier does not call the parent runner; it reproduces the relevant
field-construction and calibration logic inline.

## Audit dependency repair links

This graph-bookkeeping section records the one load-bearing upstream
authority used by the verifier. It does not promote this note or change
the audited claim scope.

- [minimal_source_driven_field_probe_note](MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md)
- [source_resolved_propagating_green_pocket_note](SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md)
  (parent that this companion reconciles; load-bearing for the
  declared observable surface, not for any new physics statement)
