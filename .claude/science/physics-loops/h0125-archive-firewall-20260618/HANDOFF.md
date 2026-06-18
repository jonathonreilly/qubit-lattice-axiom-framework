# Handoff

## Summary

This block packages the existing H0125 archive firewall as an executable
source-side repair for the audited failed `h0125_failure_derivation` row.

## What It Moves

- The old quantified H0125 failure diagnosis remains retracted and
  non-authority.
- The archive now names a firewall runner and cached output proving the
  retraction/firewall text stays in place.
- Positive H0125 physics remains with the live reduced-family executable note,
  not this archive.

## Files

- `archive_unlanded/h0125-unverifiable-numerical-diagnostics-2026-04-30/H0125_FAILURE_DERIVATION.md`
- `archive_unlanded/h0125-unverifiable-numerical-diagnostics-2026-04-30/README.md`
- `logs/runner-cache/h0125_archive_firewall_2026_06_16.txt`
- `.claude/science/physics-loops/h0125-archive-firewall-20260618/`

## Remaining Blocker

A positive repair would still need a new executable diagnostic computing
`T_interior/T_corner`, beam sigma, detector probability with any geometric
spreading factor, and centroid SNR from the same propagation model.

## Verification

- `python3 scripts/h0125_archive_firewall_2026_06_16.py`:
  `PASS: h0125 archive firewall holds`.
- `python3 -m py_compile scripts/h0125_archive_firewall_2026_06_16.py`
  passed.
- `git diff --check` passed.
- Forbidden-path guard found no audit/status/control-plane edits.
