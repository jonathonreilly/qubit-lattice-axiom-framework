# Handoff

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4402

Branch: `codex/frw-c2-entropy-bookkeeping-20260618`

Commit: `426581cb64c9`

This is stacked on PR #4401:

https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4401

The block proves finite C2 source-free entropy bookkeeping and records exact
negative controls for entropy injection and wrong `g_*S` scaling. It does not
prove the real leptogenesis-to-CMB window is source-free and does not derive
the `g_*S(T)` table.

Verification run before PR:

```bash
python3 scripts/frontier_frw_c2_entropy_bookkeeping_2026_06_18.py
python3 scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_frw_c2_entropy_bookkeeping_2026_06_18.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_frw_adiabatic_expansion_cosmological_backdrop_open_gate.py
```

Review-loop was not run; the user delegated review-loop and landing cleanup to
the Codex reviewer.

No audit ledger/result/status/publication/lane-registry files were edited.
