# PR Backlog

Status: PR created.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3238

Planned title:

```text
[physics-loop] picard-fuchs-finite-window-boundary bounded-support
```

Planned verification:

```bash
python3 scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py
python3 scripts/frontier_su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.py
git diff --check
git diff --name-only -- docs/audit
```
