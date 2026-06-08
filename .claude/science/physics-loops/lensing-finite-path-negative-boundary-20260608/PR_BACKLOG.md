# PR Backlog

Status: PR created.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3239

Planned title:

```text
[physics-loop] lensing-finite-path-negative-boundary no-go
```

Planned verification:

```bash
python3 scripts/lensing_analytical_finite_path.py
python3 scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py
git diff --check
git diff --name-only -- docs/audit
```
