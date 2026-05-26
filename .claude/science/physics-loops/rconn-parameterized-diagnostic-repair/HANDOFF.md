# Handoff

## What Changed

This PR repairs `rconn_derived_note` by narrowing it to the exact
SU(N_c) adjoint channel-fraction identity:

```text
F_adj(N_c) = (N_c^2 - 1) / N_c^2
F_adj(3) = 8/9
```

The note no longer admits matching rule M, no longer admits `kappa_EW = 0`,
and no longer treats the physical lattice connected-trace readout as part of
the theorem. The historical MC value `R_conn(MC) = 0.887 +/- 0.008` remains a
diagnostic consistency check only.

## Audit Queue Result

After `docs/audit/scripts/run_pipeline.sh`:

- `audit_status: unaudited`
- `effective_status: unaudited`
- `deps: []`
- audit queue position: 1
- ready: true
- critical row, 902 descendants

No audit verdict is applied by this PR.

## Verification

```bash
docs/audit/scripts/run_pipeline.sh
set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_rconn_parameterized_diagnostic.py | tee outputs/rconn_parameterized_diagnostic_repair_2026-05-25.txt
python3 -m py_compile scripts/frontier_rconn_parameterized_diagnostic.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/RCONN_DERIVED_NOTE.md scripts/frontier_rconn_parameterized_diagnostic.py .claude/science/physics-loops/rconn-parameterized-diagnostic-repair
git diff --check
```

Results:

- runner: `PASS=26, FAIL=0`
- pipeline: completed; target row `unaudited`, queue position 1, `deps: []`
- strict audit lint: no errors; one pre-existing Maradudin warning remains

## Remaining Blocker

A retained-grade physical theorem still needs a direct derivation of the
matching rule from the lattice connected-trace observable to the adjoint
channel fraction. This PR does not attempt that theorem.
