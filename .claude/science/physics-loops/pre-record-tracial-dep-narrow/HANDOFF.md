# Handoff

PR: pending

## What Changed

The source note now makes the historical A1 qubit-interpretation companion
non-load-bearing and keeps only the canonical minimal axiom document as the
framework dependency. The narrowed claim remains Steps 1-4: unique
tracial-state characterization on the one-qubit `Z^3` algebra.

The new runner checks finite-region trace uniqueness, tensor normalized trace,
inner-unitary invariance, finite maximum entropy, full Pauli-string
characterization, and the counterexample showing one-point Pauli vanishing is
too weak.

## Verification

- `python3 scripts/frontier_pre_record_reference_state_tracial_derivation.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md .claude/science/physics-loops/pre-record-tracial-dep-narrow/*.md`
- `git diff --check`
