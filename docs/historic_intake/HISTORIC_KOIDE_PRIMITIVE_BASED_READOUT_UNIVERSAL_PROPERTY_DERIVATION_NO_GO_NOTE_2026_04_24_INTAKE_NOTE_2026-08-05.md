# Historic intake: Koide primitive-based readout universal-property derivation no-go

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The quotient's universal property applies only to functors already constant on fibres, and the retained embedded source category still admits the label-visible functor p = (1/3, 2/3) (giving Q = 1, K_TL = 3/8), so the implication 'fibre-constant based primitive functor -> Q = 2/3 and delta = 2/9' is correct but its premise is exactly the law being derived.

Original verdict: Rejected for retained-only derivation — assuming fibre constancy is assuming the Q part of the law; the residual is a retained factorization theorem for the physical readout.
Scope: Tests whether category-theoretic universal property alone forces the new law; no target import.
Escape conditions (negative claims): CONDITIONAL_CLOSURE_IF_FACTORING_BASED_PRIMITIVE_FUNCTOR=TRUE; the note prescribes testing any future route by whether it excludes the explicit (1/3, 2/3) functor.

## Why pulled (supervisor decision, on the record)

The circularity named exactly: the quotient's universal property applies only to functors already constant on fibres — assuming fibre constancy IS assuming the Q half; blocks retained-only promotion of the whole closure family.

## Provenance (pinned)

- Original path: `docs/KOIDE_PRIMITIVE_BASED_READOUT_UNIVERSAL_PROPERTY_DERIVATION_NO_GO_NOTE_2026-04-24.md`
- Source commit: `7b2531e0084b600dbf3d410d117c568a230c5f88`
- git blob: `f840c7716407f1abddfad98663d7b5fd6bd60f03`
- sha256: `a0b922d83739e7bd5210a7a57d51ed07d6b2e60bfda9bb05030afb8def28f080`
- Lines: 161; runners named: scripts/frontier_koide_primitive_based_readout_universal_property_derivation_no_go.py

## Attached evidence (registered with, not as, this claim)

- `docs/KOIDE_PRIMITIVE_BASED_READOUT_CLOSURE_THEOREM_NOTE_2026-04-24.md` — Fifth closure route under a new law; countermodels given.
- `docs/KOIDE_PRIMITIVE_BASED_READOUT_NATURE_REVIEW_NOTE_2026-04-24.md` — Review: passes as new-law, fails retained-only.
- `docs/KOIDE_PRIMITIVE_BASED_READOUT_RETENTION_NO_GO_NOTE_2026-04-24.md` — First retained-only audit blocking promotion.

## Flags carried

Names the circularity explicitly ('circular assumption: exact').

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
