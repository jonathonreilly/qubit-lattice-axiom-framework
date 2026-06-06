# Handoff

This branch repairs the YT Ward tadpole-cancellation conditional row.

Changed:

- The parent note now withdraws the broken `YT_EW_COLOR_PROJECTION_THEOREM.md`
  D14/D15/sqrt-readout citation.
- The parent note now cites the 2026-06-06 premise-derivation packet and its
  cache.
- The parent algebra runner prose no longer describes D1/D2 as imported from
  the broken retained authority.
- Three runner caches are fresh.

Checks:

```text
python3 scripts/cached_runner_output.py scripts/audit_companion_yt_ward_ratio_tadpole_cancellation.py --check-only
python3 scripts/cached_runner_output.py scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py --check-only
python3 scripts/cached_runner_output.py scripts/frontier_yt_tadpole_cancellation_premise_derivation_2026_06_06.py --check-only
```

Remaining blocker:

```text
n_link(y_t) = n_link(g_s)
```

That equality remains tied to the `H_unit` / same-1PI structural route.

