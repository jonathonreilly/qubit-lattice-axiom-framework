---
claim_id: two_endpoint_gauss_law_invariance_profile_bounded_theorem_note_2026-06-05
claim_type_author_hint: bounded_theorem
---

# Two-Endpoint Gauss-Law Invariance Profile (Bounded Theorem)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-05
**Type:** bounded theorem
**Status:** source note awaiting independent audit handling.
**Primary runner:**
[`scripts/audit_companion_two_endpoint_gauss_law_invariance_profile_bounded_2026_06_05.py`](../scripts/audit_companion_two_endpoint_gauss_law_invariance_profile_bounded_2026_06_05.py)
**Cached log:**
[`logs/runner-cache/audit_companion_two_endpoint_gauss_law_invariance_profile_bounded_2026_06_05.txt`](../logs/runner-cache/audit_companion_two_endpoint_gauss_law_invariance_profile_bounded_2026_06_05.txt)

## Claim

Condition on the following explicit finite model:

- two endpoint matter qubits `A` and `B`;
- two link-end qubits `a` and `b`, one incident at each endpoint;
- the U(1) endpoint Gauss generators
  `G_A = sigma_z(A) + sigma_z(a)` and
  `G_B = sigma_z(b) + sigma_z(B)`;
- the SU(2) endpoint generators
  `S_A^i = (sigma_i(A) + sigma_i(a)) / 2` and
  `S_B^i = (sigma_i(b) + sigma_i(B)) / 2`.

In that model, the three natural link-transport operators have endpoint
invariance counts `0`, `1`, and `2`:

1. the bare link-end transport is variant at both endpoints;
2. the `A`-dressed half-link is invariant at `A` but variant at `B`;
3. the fully dressed Wilson-type line is invariant at both endpoints.

The U(1) invariant algebra is exactly the commutant of `{G_A, G_B}` and has
dimension `36` inside the full four-qubit operator algebra. The SU(2) endpoint
generators show the same qualitative boundary: the bare link-end transport is
variant at both endpoints, while the double-singlet Wilson-type observable is
invariant at both endpoints.

This is bounded because the two-link-end carrier and the endpoint Gauss
generators are model conventions in this note. They are not supplied by the
Lattice, Qubit, Admissibility, and Record axioms.

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  repo baseline Lattice + Qubit + Admissibility + Record language. The axiom
  baseline chain-satisfies as an approved premise; it is not a source of bounded
  status.
- The two-link-end carrier and the U(1)/SU(2) endpoint Gauss-generator
  definitions above are explicit bounded inputs for this note.
- [`QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md`](QUBIT_LINK_U2_CONNECTION_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-06-04.md)
  is the nearby link-connection algebra boundary. This note does not enlarge
  that result.

## What This Does Not Claim

- It does not derive gauge invariance of observables from the Record axiom.
- It does not identify all gauge-invariant algebra elements with physical observables.
- It does not derive the endpoint Gauss generators from Lattice + Qubit +
  Admissibility + Record.
- It does not derive gauge dynamics, an action, gauge bosons, coupling values,
  beta functions, electroweak symmetry breaking, or color SU(3).
- It does not require or establish a repo-wide quantum-link ontology.

The safe downstream use is only the bounded finite-algebra statement:
under the stated endpoint-Gauss conventions, endpoint dressing raises the
commutation profile from zero endpoints to one endpoint to both endpoints, and
the invariant algebra is the corresponding commutant.

## Runner Certificate

The runner verifies:

1. the bare, half-dressed, and fully dressed U(1) link operators have endpoint
   invariance profiles `[false, false]`, `[true, false]`, and `[true, true]`;
2. the endpoint-invariance count is monotone `0 -> 1 -> 2`;
3. the U(1) invariant algebra dimension is `36`;
4. the SU(2) endpoint generators make the bare link-end transport variant at
   both endpoints;
5. the SU(2) double-singlet Wilson-type observable is invariant at both
   endpoints;
6. this source note keeps the axiom-level, observable-identification,
   dynamics, and color claims out of scope.

Run:

```text
python3 scripts/audit_companion_two_endpoint_gauss_law_invariance_profile_bounded_2026_06_05.py
```

Expected result:

```text
SUMMARY: PASS=18 FAIL=0
```
