# Handoff

Branch: `physics-loop/koide-toy-a5-framework-split-20260617`

This PR repairs one part of the Koide toy row's conditional perimeter. The old
packet treated `(A5)` as a single local admission containing both the numeric
APS scalar `2/9` and the endpoint/readout transfer. Current main already has
retained-bounded framework arithmetic for the C3 fixed-locus `2/9`, so this
branch splits:

```text
A5-num       = eta_APS = 2/9 from retained-bounded C3 fixed-locus arithmetic.
A5-transfer  = admitted toy endpoint/readout transfer.
```

What moved:

- The numeric `2/9` component is no longer a local toy admission.
- The runner now reports `SUMMARY: PASS=36 FAIL=0` and emits
  `ETA_APS_FRAMEWORK_SOURCED=2/9`.

What did not move:

- `(A1)-(A4)` remain admitted toy premises.
- `(A5-transfer)` remains admitted.
- No Koide closure, retained-grade no-go, audit verdict, or ledger edit is
  asserted.

Next action:

Open a ready review PR. The auditor can decide whether this hash drift is
enough to re-audit the row with a smaller local admission set.
