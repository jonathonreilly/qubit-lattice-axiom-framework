# Quark C3-Oriented Ward Splitter Algebraic Core Split

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status:** exact-support source-side algebraic split; `audit_required_before_effective_retained=true`; `bare_retained_allowed=false`.
**Status authority:** independent audit lane only. This note does not set or predict an audit outcome and does not edit audit ledgers, queues, Tier-A registries, publication-status surfaces, active review queues, lane registries, or front-door status files.
**Primary runner:** [`scripts/frontier_quark_c3_oriented_ward_splitter_algebraic_core_split_2026_06_18.py`](../scripts/frontier_quark_c3_oriented_ward_splitter_algebraic_core_split_2026_06_18.py)
**Cached log:** [`logs/runner-cache/frontier_quark_c3_oriented_ward_splitter_algebraic_core_split_2026_06_18.txt`](../logs/runner-cache/frontier_quark_c3_oriented_ward_splitter_algebraic_core_split_2026_06_18.txt)

## Purpose

The audited conditional row for
`QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md` (context
handle, not a citation-graph dependency) separates two facts:

1. the finite-dimensional `C3` normal-form algebra is valid; and
2. physical carrier provenance and quark-sector source/readout semantics are
   separate gates.

This note isolates only the first fact. It starts from the already retained
finite-dimensional `C^3` operator surface of
[`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
and proves the local `C3` Ward splitter theorem on that surface. It does not
derive physical species, quark masses, a staggered physical carrier,
Grassmann/CAR semantics, source laws, readout laws, or Yukawa ratios.

## Load-Bearing Input Surface

Use only the following retained finite-dimensional input:

```text
V = H_hw=1 = span(X1, X2, X3) = C^3,
C X1 = X2, C X2 = X3, C X3 = X1, C^3 = I.
```

The translation-character projectors from the same parent separate
`X1`, `X2`, and `X3`, so a readout diagonal in that basis has the form
`diag(x,y,z)`.

No physical realization of this carrier is used in the proof below. The open
physical-realization program remains relevant to broader quark-mass closure,
but it is not a load-bearing input to this algebraic split.

## Theorem

Let `C` be the oriented order-three cycle above. The Hermitian endomorphisms
of `V` that commute with `C` are exactly

```text
W(a,b,c) = a I + b (C + C^2) + c (C - C^2)/(i sqrt(3)),
```

with `a,b,c in R`.

If `R` is any reflection satisfying `R C R = C^2`, then the splitter

```text
K_C3 = (C - C^2)/(i sqrt(3))
```

is reflection-odd:

```text
R K_C3 R = -K_C3.
```

In the Fourier basis diagonalizing `C`, the eigenvalues are

```text
lambda_0 = a + 2 b,
lambda_+ = a - b + c,
lambda_- = a - b - c.
```

Thus generic `c != 0` splits the unbroken-`S_3` doublet into two cyclic
Fourier channels. At `c = 0`, the doublet remains degenerate.

Finally, if a readout is required to be both diagonal in the
translation-character generation basis and `C3`-equivariant, cyclic covariance
forces

```text
diag(x,y,z) = diag(x,x,x).
```

The oriented `C3` splitter and the generation-basis diagonal readout are
therefore distinct structures.

## Proof

The complex commutant of a single order-three cyclic permutation on `C^3` is
the algebra of circulants:

```text
u I + v C + w C^2.
```

Hermiticity imposes `u in R` and `w = conjugate(v)`. Writing

```text
v = b - i c / sqrt(3),  w = b + i c / sqrt(3)
```

gives the stated real basis

```text
I, C + C^2, (C - C^2)/(i sqrt(3)).
```

The reflection statement follows immediately from `R C R = C^2`. The spectrum
follows by evaluating the same polynomial on the three eigenvalues
`1`, `omega`, and `omega^2` of `C`. The diagonal-readout boundary follows
because commuting `diag(x,y,z)` with the transitive cycle forces
`x = y = z`.

## What This Split Does Not Claim

- It does not derive or retain quark masses.
- It does not derive `y_u/y_t`, `y_c/y_t`, `y_d/y_t`, `y_s/y_t`, or
  `y_b/y_t`.
- It does not supply a source law for `a`, `b`, or `c`.
- It does not identify cyclic Fourier channels with physical quark Yukawa
  channels.
- It does not close any physical staggered-carrier, fermion-field,
  Grassmann/CAR, CKM, PMNS, Koide, hadron, or species-semantics gate.
- It introduces no new axiom, primitive, admission, normalization,
  comparator, fitted value, or measured input.

## Relation To The Parent Conditional Row

The parent block-06 note remains the broader Lane 3 support/boundary surface.
This split gives the reviewer and auditor a clean source artifact for the
algebraic part of that row: the only load-bearing carrier input is the
retained finite-dimensional `C^3` operator surface from the three-generation
observable theorem. Physical carrier provenance and quark-specific
source/readout laws remain separate gates.

## Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
target_claim_id: quark_c3_oriented_ward_splitter_support_note_2026-04-28
target_blocker_text: "the load-bearing C3 normal-form algebra is valid, but the source note directly cites the staggered-Dirac realization gate, which is not retained-grade in this packet"
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This split isolates exact local C3 algebra only; physical carrier provenance and quark source/readout bridges remain outside the claim."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner Certificate

The runner verifies:

- the three-generation observable parent is the retained finite-dimensional
  carrier authority;
- the parent block-06 note has been rewired away from a load-bearing
  physical-carrier gate citation;
- the complex `C3` commutant has dimension three;
- the Hermitian `C3` commutant has the stated three-real-parameter basis;
- the oriented splitter is Hermitian, `C3`-equivariant, and reflection-odd;
- the closed-form spectrum matches numerical eigenvalues;
- generation-basis diagonal plus `C3` covariance forces a scalar readout;
- observed quark masses, fitted Yukawa entries, CKM mass input, and physical
  source laws are absent from the proof inputs.
