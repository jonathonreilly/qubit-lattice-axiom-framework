# Summary

Registers a source-side bounded runner for `mass_spectrum_derived_note`.

The new wrapper executes the current mass-spectrum validation commands: quark packet `PASS=46`, charged-lepton cross-reference `PASS=11`, neutrino sector `PASS=19`, and cosmology cascade `PASS=23`, for aggregate `PASS=99 FAIL=0`. It also checks that the note keeps the important caveats: no full quark retention, no charged-lepton derivation, and no live-surface `eta` derivation.

# Artifacts

- `docs/MASS_SPECTRUM_DERIVED_NOTE.md`
- `scripts/mass_spectrum_derived_bounded_probe.py`
- `logs/runner-cache/mass_spectrum_derived_bounded_probe.txt`
- generated audit surfaces under `docs/audit/`
- branch-local handoff pack under `.claude/science/physics-loops/audit-unblock-block149-20260621/`

# Boundary

This PR keeps the row `bounded_theorem` / `unaudited` / `effective_status: unaudited`. It does not apply audit verdicts, does not update repo-wide lane/status authority surfaces, and does not claim full mass-spectrum retention.

The reviewer lane may update or cherry-pick this PR against fast-moving `main`; this branch is not intended to keep refreshing itself after opening.

# Verification

- `python3 scripts/mass_spectrum_derived_bounded_probe.py` -> `SUMMARY: PASS=20 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/mass_spectrum_derived_bounded_probe.py --check-only --push-mode none --allow-non-main` -> cache fresh
- `python3 docs/audit/scripts/audit_lint.py --strict` -> strict lint OK
- `python3 -m py_compile scripts/mass_spectrum_derived_bounded_probe.py scripts/frontier_quark_mass_ratio_review.py scripts/frontier_mass_ratio_lepton_sector.py scripts/frontier_neutrino_mass_derived.py scripts/frontier_cosmology_from_mass_spectrum.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py`
- `git diff --check`
