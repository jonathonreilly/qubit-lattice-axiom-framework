---
claim_id: source_resolved_exact_green_pocket_note
claim_type_author_hint: bounded_theorem
claim_scope: >-
  Conditional on GREEN-KERNEL-PARAMS, the declared finite fixture
  deterministically satisfies local declared hard bars when computed through
  the cited foundational Lattice3D/propagate/K implementation surface at its
  declared-run scope; the premise values and hard-bar windows are supplied,
  not derived.
---

# Source-Resolved Exact Green Pocket

**Date:** 2026-04-05 (audit-narrowing refresh: 2026-05-10;
conditional recut: 2026-07-07)
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:**
[`scripts/source_resolved_exact_green_pocket.py`](../scripts/source_resolved_exact_green_pocket.py)
**Status authority:** independent audit lane only. The
`bounded_theorem` label is a source-side claim-boundary declaration, not
an audit verdict.

## Safe Statement

The load-bearing statement is conditional, finite, and fixture-level:

If `GREEN-KERNEL-PARAMS` is supplied, then the declared exact-lattice
fixture, computed through the imported foundational implementation surface
from
[`MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md`](MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md),
deterministically satisfies the following hard bars:

- zero-source reduction: `|zero_delta| <= 1e-12`
- TOWARD sign: `4/4` Green-kernel rows have positive centroid shift
- Green-kernel `F~M` exponent window: `0.95 <= alpha_green <= 1.05`
- mean ratio window: `1.10 <= mean |green/inst| <= 1.40`
- computed declared-scale gain:
  `FIELD_TARGET_MAX / ref_max` matches the supplied `DECLARED_GAIN` within
  `5e-7` and lies in `(0, 100)`

No claim in this note derives the Green kernel, its parameter values, the
source geometry, the gain, the hard-bar windows, size transfer, a continuum
limit, or self-consistent field dynamics.

## Named Conditional Premises

> GREEN-KERNEL-PARAMS (named conditional premise): the Green-kernel and fixture
> parameters are SUPPLIED as declared values -- kernel mu = 0.08, eps = 0.5,
> calibrated gain 2.131774 (selected at the declared scale), lattice h = 0.5,
> W = 3, L = 20, the declared four-node boundary-clipped source cluster, and
> source strengths {0.001, 0.002, 0.004, 0.008}. Not derived: no landed route
> derives these values; the gain is observable-calibrated at the declared
> scale, and that calibration is quarantined inside this premise.

These premises are named only so the conditional fixture theorem can be
audited without treating the values as selected, natural, or derived.

## Exact Identities (Unconditional)

For any fixed lattice, fixed source-node list, and fixed kernel parameters
accepted as inputs by the runner, the raw source-resolved field is linear in
the scalar source strength:

```text
field_s(layer, i) =
  average_source_nodes s * exp(-mu * (rho + eps)) / (rho + eps)
```

Therefore `field_0(layer, i) = 0` at every lattice site, before any numerical
threshold is applied. The zero-source Green channel supplied to propagation is
the zero field, so the runner's zero-source reduction compares the propagated
zero-field replay with the same free propagation baseline.

The finite loops over layers, plane nodes, source nodes, and source strengths
have no random branch, no fitted input selection, and no network or external
data dependency. Their arithmetic consequences are deterministic consequences
of the supplied fixture and the cited declared-run implementation surface.

## Conditional Chain

Under `GREEN-KERNEL-PARAMS`, the runner evaluates the declared finite fixture
as follows:

1. Build the exact lattice with `h = 0.5`, `W = 3`, and `L = 20`.
2. Build the declared boundary-clipped source cluster, which has four in-bounds
   source nodes on this fixture.
3. Use supplied kernel parameters `mu = 0.08`, `eps = 0.5`, and supplied
   gain `2.131774`.
4. Replay source strengths `{0.001, 0.002, 0.004, 0.008}`.
5. Check the hard bars listed in the Safe Statement.

The conditional conclusion is only that this supplied finite fixture satisfies
those hard-bar inequalities when computed by the runner. It is not a parameter
selection theorem.

## Runner Readout and Motivation Exhibit

The frozen table and fit readouts below are load-bearing only where they feed
the hard bars in the Safe Statement: `zero_delta`, TOWARD count,
`alpha_green`, `mean_ratio`, and the computed declared-scale gain check.

Calibration replay comparisons are motivation-tier evidence only.
No value here is derived framework content.

The frozen pocket uses:

- exact lattice with `h = 0.5`, `W = 3`, `L = 20`
- fixed cross5 source cluster clipped at the boundary, leaving 4 in-bounds
  source nodes
- source strengths `s = 0.001, 0.002, 0.004, 0.008`
- kernel `exp(-mu rho_eps) / rho_eps`, with
  `rho_eps = sqrt(dx^2+dy^2+dz^2) + eps`, `mu = 0.08`, `eps = 0.5`
- supplied calibrated gain `2.131774`

Reduction check:

- zero-source dynamic shift: `+0.000000e+00`

Frozen readout:

| `s` | instantaneous deflection | Green-kernel deflection | ratio | max `|f|` |
| --- | ---: | ---: | ---: | ---: |
| `0.0010` | `+1.713544e-03` | `+2.139974e-03` | `1.249` | `2.5e-03` |
| `0.0020` | `+3.440703e-03` | `+4.279367e-03` | `1.244` | `5.0e-03` |
| `0.0040` | `+6.936763e-03` | `+8.557985e-03` | `1.234` | `1.0e-02` |
| `0.0080` | `+1.410179e-02` | `+1.712572e-02` | `1.214` | `2.0e-02` |

Fitted exponents:

- instantaneous `F~M`: `1.01`
- Green-kernel `F~M`: `1.00`

Any nearest-rational scan, calibration replay, imported live value, or extra
observable comparison associated with this fixture belongs only to the
motivation tier unless it is restated above as a conditional hard bar.

## Unconditional Boundary

### Source Boundary (2026-06-12, Preserved)

**Boundary:** numerical-match / bounded support only. Effective status is
audit-derived; this source records only the claim boundary.

The load-bearing numerical pocket depends on runner-selected modeling inputs:
the Green-like kernel form and parameters, the boundary-clipped source cluster,
and the calibrated gain. This note may be cited only for the declared small
exact-lattice family and its runner-backed table. It may not be cited as a
derivation of the Green kernel, field dynamics, amplitude normalization,
source geometry, continuum transfer, or size-transfer law.

Promotion beyond numerical-match support requires a separate theorem deriving
the kernel, parameters, source geometry, and gain from retained framework
dynamics.

The 2026-07-07 recut preserves this as an unconditional no-go boundary:
supplying the values as `GREEN-KERNEL-PARAMS` does not derive them.

### Audit Boundary (2026-05-10, Preserved)

The independent audit verdict on this row's prior active hash was
`audited_conditional` (codex-gpt-5.5, fresh_context, 2026-05-10) with
`chain_closes: false`. In paraphrase, that audit named two issues:

1. The exact-lattice construction, propagation rule, centroid readout, `K`,
   source constants, and instantaneous comparator were delegated to
   `scripts.minimal_source_driven_field_probe`, but that source was not in the
   restricted packet or cited as a one-hop authority.
2. The runner printed values without explicit threshold checks, so the audit
   packet could not verify load-bearing observables against tolerances.

The audit's `notes_for_re_audit_if_any` recorded a `runner_artifact_issue`
repair class: include the minimal source-driven helper source or a
self-contained reduced runner exposing `Lattice3D`, `propagate`, `K`, source
constants, centroid readout, and instantaneous comparator, then rerun and
re-audit the bounded pocket.

The 2026-05-10 rigorize pass selected that repair target by:

1. Citing the upstream foundational authority chain explicitly so the audit
   packet can route through `MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE`.
2. Adding hard-bar threshold assertions to the runner so load-bearing values
   are verified against explicit tolerances rather than only printed.
3. Disclosing the runner-selected modeling inputs as tuned support, not
   derived from the repo baseline.

### Conditional Recut (2026-07-07)

This recut re-types the matched values as supplied premises:
`GREEN-KERNEL-PARAMS` names the kernel parameters, gain, lattice size, clipped
source cluster, and source strengths as premise content. The load-bearing
claim is now the exact conditional algebra and deterministic hard-bar outcome
of the declared finite fixture under those premises. Calibration replay
comparisons remain motivation-tier evidence only.

PATH A, deriving the Green-kernel form and calibration gain from repo dynamics,
is still theorem-level work and remains deferred to a separate promotion
attempt.

## Residuals / Open Derivation Targets

The following are not closed by this note:

- deriving the Green kernel form `exp(-mu rho_eps) / rho_eps`
- deriving `mu = 0.08` and `eps = 0.5`
- deriving the supplied calibrated gain `2.131774`
- deriving the boundary-clipped four-node source cluster as a required
  geometry
- deriving the hard-bar windows from retained framework dynamics
- proving any size-transfer or continuum result
- promoting the source-resolved channel to a self-consistent field equation

## Citation Contract (Audit-Gated)

The runner imports `Lattice3D`, `propagate`, `K`, `SOURCE_Z`,
`SOURCE_STRENGTHS`, `_centroid_z`, `_instantaneous_field_layers`, and
`_fit_power` from `scripts/minimal_source_driven_field_probe.py`. The source
note for that imported surface is
[`MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md`](MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md).

That foundational note states its load-bearing content is "the declared-run
computation only" and says it does not claim a framework derivation of its
telegraph rule or calibration values. This Green pocket uses only the cited
`Lattice3D` / `propagate` / `K` implementation surface at that declared-run
scope; it does not import or derive Green-kernel parameters, gain, or hard-bar
windows from that note.

The one-hop foundational and sibling notes are:

- [`docs/MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md`](MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md)
  - foundational `Lattice3D` / `propagate` / `K` source authority, used at
    its audited declared-run scope.
- `docs/SOURCE_RESOLVED_EXACT_GREEN_H025_POCKET_NOTE.md`
  - companion `h = 0.25` Green pocket on a smaller family. See-also
    cross-reference; backticked to break cycle-0012 in the citation graph.
- `docs/SOURCE_RESOLVED_EXACT_GREEN_SCALING_NOTE.md`
  - companion scaling note, cited only at its audited scope. See-also
    cross-reference; not a load-bearing authority for this base pocket.
- `docs/SOURCE_RESOLVED_EXACT_GREEN_SELF_CONSISTENT_NOTE.md`
  - downstream self-consistent extension. See-also cross-reference; not a
    load-bearing authority for this base pocket.
- `docs/SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md`
  - downstream propagating-Green sibling. See-also cross-reference; backticked
    to break cycle-0013 in the citation graph.

The h025 companion note's artifact-chain list already cites this base pocket
as upstream; the load-bearing citation direction is h025 -> this pocket, not
vice versa. The propagating-Green sibling says this exact-Green sibling is
useful context, not a load-bearing authority for that packet.

The bounded inheritance for this note's load-bearing claim is the imported
foundational surface above plus the named conditional premises. This source
does not set audit-lane status.

## Firewall

This note may not be cited as a derivation of the Green kernel.
This note may not be cited as a derivation of field dynamics.
This note may not be cited as a derivation of amplitude normalization.
This note may not be cited as a derivation of source geometry.
This note may not be cited as a derivation of continuum transfer.
This note may not be cited as a derivation of a size-transfer law.
This note may not be cited as a derivation from the Quantum one-site local
algebra.
This note may not be cited as a derivation from the Lattice `Z^3` baseline.
This note may not be cited for a self-consistent dynamical field equation.
This note may not be cited to promote the source-resolved Green channel to a
retained field-theoretic theorem.
This note may not be cited as deriving the Green-kernel form, parameters, or
gain from retained framework dynamics.
The named premises may not be cited as derived.

## Artifact chain

**Primary runner:**
[`scripts/source_resolved_exact_green_pocket.py`](../scripts/source_resolved_exact_green_pocket.py)

- [`cache`](../logs/runner-cache/source_resolved_exact_green_pocket.txt)
- imported infrastructure:
  [`scripts/minimal_source_driven_field_probe.py`](../scripts/minimal_source_driven_field_probe.py)
  (`Lattice3D`, `propagate`, `K`, `SOURCE_Z`, `SOURCE_STRENGTHS`,
  `_centroid_z`, `_instantaneous_field_layers`, `_fit_power`)

## Verification

Verification is by the deterministic offline runner:
[`scripts/source_resolved_exact_green_pocket.py`](../scripts/source_resolved_exact_green_pocket.py).
The generated runner transcript is
[`runner-cache transcript`](../logs/runner-cache/source_resolved_exact_green_pocket.txt).

The runner now separates load-bearing hard-bar checks from motivation-tier
calibration evidence, verifies parser-visible note metadata and primary-runner
extraction, and ends with a fatal `TOTAL: PASS=N FAIL=0` banner when all
load-bearing, premise, parser, and text checks pass.
