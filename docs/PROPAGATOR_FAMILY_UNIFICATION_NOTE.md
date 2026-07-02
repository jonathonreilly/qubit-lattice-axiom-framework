# Propagator Family Unification Note

**Date:** 2026-04-05 (bounded scaffold bridge refresh: 2026-06-17)
**Status:** bounded scaffold bridge / synthesis support; not an audit verdict

**Primary runner:** `scripts/propagator_family_scaffold_bridge.py`
**Cached runner output:** [`logs/runner-cache/propagator_family_scaffold_bridge.txt`](../logs/runner-cache/propagator_family_scaffold_bridge.txt)

**Status authority and audit hygiene (2026-06-17):**
This note is now paired with a bounded scaffold bridge runner. The
runner checks, from repository source, that the cited wavefield,
complex-action, and electrostatics lanes use a common factorized
edge-update scaffold: scalar fields are built outside the propagator,
sampled at edge endpoints, and then enter the edge action or attenuation
slot while the geometry-first path-sum prefactor remains separate.

The bridge is intentionally narrow. It certifies source-level scaffold
identity only; it is not a continuum theorem, not a full electromagnetism
derivation, not a self-gravity derivation, and not a geometry-generic
transfer theorem. The existing fixed-field runner
[`scripts/FIXED_FIELD_FAMILY_UNIFICATION.py`](../scripts/FIXED_FIELD_FAMILY_UNIFICATION.py)
continues to carry the stronger same-grown-row comparison between the
signed-source and complex-action companions.

Firewall summary: this is a bounded scaffold bridge; it is not a
continuum theorem, not a full electromagnetism derivation, and the
independent audit lane remains authoritative.

Independent audit lane status remains authoritative. This source note
does not retag itself, does not set an effective status, and does not
claim retained-grade propagation before the upstream rows and this
bounded bridge are independently audited.

## Artifact chain

This note is a synthesis of `main` notes plus the bounded scaffold bridge
runner above:

- [`docs/SOURCE_RESOLVED_WAVEFIELD_MECHANISM_NOTE.md`](SOURCE_RESOLVED_WAVEFIELD_MECHANISM_NOTE.md) — runner-backed exact-lattice mechanism row; independent audit still required
- [`docs/CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE.md`](CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE.md) — retained-bounded parent context
- [`docs/CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md`](CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md) — retained-bounded grown-row complex-action companion on the current audit surface
- [`docs/ELECTROSTATICS_CARD_NOTE.md`](ELECTROSTATICS_CARD_NOTE.md) — retained scalar sign-law card on the current audit surface
- [`docs/ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE.md`](ELECTROSTATICS_SUPERPOSITION_PROXY_NOTE.md) — retained scalar superposition proxy on the current audit surface
- [`scripts/FIXED_FIELD_FAMILY_UNIFICATION.py`](../scripts/FIXED_FIELD_FAMILY_UNIFICATION.py) — same-grown-row signed-source / complex-action comparison
- [`scripts/propagator_family_scaffold_bridge.py`](../scripts/propagator_family_scaffold_bridge.py) — bounded source-level scaffold bridge for this synthesis

Statuses listed above are source-facing context only. The author of any
future re-audit should confirm current status against the audit ledger
rather than this static prose.

## One-line read

The common scaffold structure is a fixed propagator on a causal graph, with a
scalar coupling that changes how edges contribute without changing the basic
path-sum form.

That is the narrow unification claim here.

## Common propagator skeleton

Across the cited lanes, the shared shape is:

- a graph or ordered-lattice family
- a path-sum or stepwise transport rule
- a baseline propagation kernel that remains the same family-to-family
- a scalar coupling that modifies the edge contribution in a controlled way
- a zero-coupling or null-control reduction that must recover the baseline

In symbolic form, the cited lanes all look like a variant of:

```text
amplitude(edge) = baseline_propagator(edge) × scalar_coupling(edge)
```

The exact details differ by lane, but the review-safe common point is that the
coupling is scalar and multiplicative at the edge level, not a change to the
overall transport architecture.

## What each cited lane contributes

### Wavefield lane

The wavefield mechanism keeps the baseline propagator fixed and promotes a
phase-sensitive detector-line observable.

Runner-backed behavior:

- exact zero-source reduction survives
- the detector-line phase ramp is coherent
- the ramp coefficient depends on source depth and source strength
- weak-field `F~M` stays near unity on the exact family

Interpretation:

- the scalar coupling here acts as a phase-sensitive transport control
- the important observable is not raw attenuation, but a stable phase ramp

### Complex-action lane

The complex-action carryover keeps the same ordered transport family and adds
a scalar action deformation:

```text
S = L(1 - f) + iγLf
```

Runner-backed behavior:

- exact `gamma = 0` reduction survives
- Born stays machine-clean on the frozen exact field and the grown-row companion
- increasing `gamma` drives a `TOWARD -> AWAY` crossover
- detector escape falls sharply as the scalar coupling grows

Interpretation:

- the scalar coupling acts like a phase / absorption deformation of the same
  fixed propagator
- the narrow source-backed claim is structural crossover, not geometry-independence

### Electrostatics scalar-sign lane

The electrostatics card keeps the same ordered-lattice transport family but
changes the source polarity.

Runner-backed behavior:

- sign antisymmetry is clean
- opposite-sign superposition cancels to printed precision
- dipole orientation flips the sign of the response
- the charge response is linear on the tested range
- screening strongly attenuates the response

Interpretation:

- the scalar coupling acts like a sign selector on the same transport skeleton
- the source-backed claim is electrostatics-like sign structure, not full Maxwell
  theory

## What is actually unified

The bounded scaffold bridge is:

- same underlying path-sum / transport scaffold
- same requirement for a null or zero-coupling reduction
- same use of a scalar coupling to alter edge-level transport
- same review discipline: the promoted observable must survive the baseline
  check

The runner-backed wording is deliberately "scaffold bridge", not a
framework-wide operator-equality theorem. It is enough to justify using
"propagator family" as an organizing and bounded bridge term once the
upstream runner-backed rows pass independent audit; it is not enough to
close continuum, geometry-generic, or physical-unification claims.

## What is not unified yet

This note does **not** claim:

- geometry-generic transfer from exact lattices to all generated families
- a derivation of the scalar couplings from one principle
- full electromagnetism
- continuum closure
- self-gravity as a retained mechanism
- QNM / BMV / horizon thermodynamics as retained claims
- a single flagship theorem that forces belief on its own

The missing step is still a stronger bridge between families, not a new
taxonomy of existing results.

## Safe conclusion

The narrow review-safe statement is:

- the cited wavefield, complex-action, and electrostatics runners share a
  source-checked factorized edge-update scaffold
- the difference between them is captured by scalar data attached at the
  edge-action or edge-attenuation slot, not by replacing the path-sum
  transport scaffold
- the fixed-field runner gives the strongest same-row support for the
  signed-source / complex-action pair
- the synthesis remains bounded scaffold support until the remaining
  upstream rows and this bridge pass independent audit

That is the strongest unification description currently supported on
`main`. It is bounded scaffold support, not a full unification theorem.

## Audit-aware repair path

The audit lane's stated cheapest repair (see `audit_ledger.json`,
`notes_for_re_audit_if_any` for `propagator_family_unification_note`):

1. audit the runner-backed source-resolved wavefield mechanism dependency;
2. audit the bounded scaffold bridge runner added here;
3. only after those steps is the synthesis itself eligible for re-audit at
   anything stronger than `audited_conditional`.

Until those steps land, this note must be cited only as a non-load-bearing
bounded scaffold support, never as full chain closure for any descendant
claim.
