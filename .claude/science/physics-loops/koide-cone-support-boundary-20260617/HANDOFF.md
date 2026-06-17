# Handoff

Branch: `codex/koide-cone-support-boundary-20260617`

This PR repairs the source-side boundary for
`charged_lepton_koide_cone_algebraic_equivalence_note`.

What changed:

- The source note now states exact-support status with bounded downstream reuse.
- The exact Fourier/Plancherel theorem is unchanged.
- The note no longer presents the carrier context as retained-grade source
  authority.
- The runner now checks the source-status firewall and still reports
  `KOIDE_FORCING_RESOLVED=FALSE`.

Checks run:

- `python3 scripts/frontier_charged_lepton_observable_curvature.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_charged_lepton_observable_curvature.py`
- `python3 -m py_compile scripts/frontier_charged_lepton_observable_curvature.py`

Not done:

- No audit-loop run.
- No audit ledger, queue, publication, or front-door edits.
- No review-loop run; reviewer owns that step.
