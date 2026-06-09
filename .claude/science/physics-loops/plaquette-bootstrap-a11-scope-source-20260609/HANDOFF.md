# Plaquette Bootstrap A11 Scope/Source Repair Handoff

## Target

`plaquette_bootstrap_framework_integration_note_2026-05-03`

Prior audit blocker:

```text
scope_too_broad: narrow BB1 to Wilson-loop observables proven to lie in A11's A_+^(2) surface and include the mixed-cumulant authority, or remove the beta=6 estimate from the audited theorem scope.
```

## Repair Summary

The note now scopes BB1 to the retained-bounded A11 `A_+^(2)` surface and names the Gauge OS Step 1 companion as the Wilson-loop membership/reflection-Hermiticity source. It also cites the retained mixed-cumulant onset theorem directly and demotes the beta=6 substitution to a formal diagnostic, not a theorem or bound.

The runner adds a Section 0 manifest check that fails if the note reverts to the broad Wilson-loop claim or beta=6 theorem wording.

## Verification

```text
python3 scripts/frontier_plaquette_bootstrap_framework_integration.py
python3 scripts/cached_runner_output.py scripts/frontier_plaquette_bootstrap_framework_integration.py
python3 -m py_compile scripts/frontier_plaquette_bootstrap_framework_integration.py
git diff --check
git diff --name-only -- docs/audit
```

No audit-ledger files should be changed by this PR.
