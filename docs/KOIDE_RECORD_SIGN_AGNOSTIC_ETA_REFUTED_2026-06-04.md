---
claim_id: koide_record_sign_agnostic_eta_refuted_2026-06-04
claim_type_author_hint: open_gate
---

# Koide Record Sign-Agnostic Eta Route Diagnosis

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** open_gate (readout-route diagnosis)
**Status:** source-only route diagnosis. This note does not approve a new
axiom, primitive, admission, readout rule, or verdict. It records runner-backed
facts about sign-sensitive and sign-blind Koide readouts.
**Primary runner:** [`scripts/koide_record_sign_agnostic_eta_refuted_2026_06_04.py`](../scripts/koide_record_sign_agnostic_eta_refuted_2026_06_04.py)
**Cached log:** [`logs/runner-cache/koide_record_sign_agnostic_eta_refuted_2026_06_04.txt`](../logs/runner-cache/koide_record_sign_agnostic_eta_refuted_2026_06_04.txt)

## Claim Boundary

The runner checks four narrow facts:

1. signed trace, unsigned absolute-value sum, log-absolute-determinant, and
   `eta = sum(sign(lambda_k))` are each additive over direct sums;
2. squaring removes a single sign, so a post-Born magnitude readout cannot
   recover the sign;
3. `eta` is too coarse to reconstruct the real-valued signed denominator:
   two positive spectra have the same `eta` but different `Q`;
4. the observed charged-lepton square-root comparator is sign-homogeneous, so
   signed and unsigned square-root readouts coincide on that comparator.

These checks diagnose routes. They do not select a readout functional. They do
not establish `Q = 2/3` from the framework, and they do not prove that every
future signed-readout route is impossible.

## Source Links

The Record axiom scope referenced here is
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md). The `Q` lever
used for the final route boundary is the upstream algebra identity in
[`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md).

## What This Does Not Claim

- It does not adopt signed trace as the Koide readout.
- It does not adopt unsigned magnitude as the Koide readout.
- It does not use the observed charged-lepton masses as derivation inputs.
- It does not classify the sign choice as an axiom or primitive.
- It does not close the `r = 1/2` or holomorphic-polarization gate.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is narrow: this note may be cited to say that Record
additivity alone does not distinguish the tested additive sign-sensitive and
sign-blind functionals, and that the `eta` count is not enough to reconstruct
the signed Koide denominator. It may not be cited as a closed no-go against
all future signed readout derivations.
