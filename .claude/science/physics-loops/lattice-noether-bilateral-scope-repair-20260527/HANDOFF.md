# Handoff

## What Moved

The lattice-Noether bilateral identity row now cites a retained-bounded
finite-Grassmann Berezin determinant authority and narrows the generator
scope to site-local/internal generators.

## Files

- `docs/LATTICE_NOETHER_CARRIER_INDEPENDENT_BILATERAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-17.md`
- `scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py`
- `.claude/science/physics-loops/lattice-noether-bilateral-scope-repair-20260527/`

## Verification

- `PYTHONPATH=scripts python3 scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py`
  - `Overall verdict: PASS`
- `python3 scripts/vocab_lint.py --report-only docs/LATTICE_NOETHER_CARRIER_INDEPENDENT_BILATERAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-17.md scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py .claude/science/physics-loops/lattice-noether-bilateral-scope-repair-20260527/*.md`
  - clean
- `git diff --check`
  - clean
- `bash docs/audit/scripts/run_pipeline.sh`
  - complete; row reset to `unaudited`, `claim_type=bounded_theorem`, no open deps

## Draft PR

https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2112

## Remaining Blockers

Lattice-index-shifting Ward currents require a separate theorem and are
not claimed here.

## Next Action

Proceed to the next ledger-order conditional row.
