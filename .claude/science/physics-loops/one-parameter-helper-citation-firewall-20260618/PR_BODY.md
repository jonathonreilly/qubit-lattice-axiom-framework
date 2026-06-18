# Summary

Source-side repair for
`one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13`.

This PR adds a runner-enforced citation/use firewall so the umbrella note can
only be cited as a helper-wrapper registry / one-hop dependency handle, not as
a derivation of the five helpers, the parent one-parameter shell law, tensorial
matching, nonlinear GR closure, or any status movement authority.

# What changed

- Added a `2026-06-18` citation/use firewall to
  `docs/ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md`.
- Clarified direct source citations in
  `docs/ONE_PARAMETER_REDUCED_SHELL_LAW_NOTE.md` and
  `docs/SCALAR_TRACE_TENSOR_NO_GO_NOTE.md`.
- Extended `scripts/frontier_one_parameter_reduced_shell_law.py` to scan direct
  citations to the umbrella note and fail if they lack helper-wrapper /
  one-hop-registry qualifiers or contain helper-derivation/status-promotion
  language.
- Hardened the runner to exit nonzero on failed checks.
- Refreshed `logs/runner-cache/frontier_one_parameter_reduced_shell_law.txt`.

# Verification

```bash
python3 scripts/frontier_one_parameter_reduced_shell_law.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_one_parameter_reduced_shell_law.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_one_parameter_reduced_shell_law.py
python3 -m py_compile scripts/frontier_one_parameter_reduced_shell_law.py
git diff --check
```

Observed target runner/cache result: `PASS=17 FAIL=0`.

# Audit discipline

This PR does not audit, retag, or land anything. It does not edit audit result
files, publication effective-status files, front-door status, lane registry, or
the active review queue. Independent audit/review must decide whether this
source-side exact-support repair moves the existing row.
