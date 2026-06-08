# Handoff

Branch: `physics-loop/picard-fuchs-finite-window-boundary-20260608`

Target claim:
`plaquette_v1_picard_fuchs_ode_all_order_proof_note_2026-05-09`

What changed:

- The historical all_order note now states the finite-window boundary supported
  by the runner.
- Nearby Picard-Fuchs consumer notes no longer describe the companion as
  standalone all-order closure.
- The source-packet manifest now checks for finite-window boundary semantics
  and explicitly requires the JSON to report all-order/minimality as false.
- Runner caches and JSON outputs were refreshed.

Verification:

```text
SUMMARY: FINITE-WINDOW BOUNDARY PASS=5 FAIL=0
SUMMARY: SOURCE PACKET MANIFEST PASS=54 FAIL=0
```

Remaining blocker:

An auditable all-degree `R=3,D=2` bridge theorem is still absent. This branch
does not attempt to close it.

Next action:

Open a PR for reviewer extraction and independent re-audit. Do not edit
`docs/audit/**`.
