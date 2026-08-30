# Block26 execution history

## Preregistered and independently challenged stage

The runner source and amended preregistration packet were committed at
`82e940b22742112f606049756f37a7debc29c42a`. Three independent static scopes
returned `SAFE` on the science bytes before target import or execution,
conditional only on the expected frozen-hash refresh and separate source pin.
The final committed runner source has SHA-256
`c728895b949f2e4db7adc3d810fe6d026fdb53431db354282faf52b3fbd6e72f`.

The separate source pin and checkpoint state were committed at
`3bc2c336c8`. Forty-three literal declared inputs produced the content
fingerprint below. No target import or execution occurred before both pins
were present.

## Initial content-bound run

```text
source SHA-256: c728895b949f2e4db7adc3d810fe6d026fdb53431db354282faf52b3fbd6e72f
input fingerprint: d11cbc8773aa727a21b2011b3c3d4d7792816880e22a1d80a1cfa3b551a297a7
initial cache: logs/runner-cache/admissibility_d4_existing_qubit_lease_autonomy_gate_2026_08_30_initial.txt
initial cache SHA-256: d0656a29e6e987e19783f31ea2fbd983501d66e01f6c70c88bea9eeed7f418b9
elapsed: 528.61 seconds
exit: 0
stderr: empty
TOTAL: PASS=24 FAIL=0
```

The aggregate comprises 23 named science checks plus one mutation gate. All
25 designated physical, geometric, routing, no-go-demotion, and scope
mutations were rejected. The run emitted only the conditional positive
terminal. It did not emit an arbitration no-go, axiom amendment, obligation
retirement, TOE-score movement, or closure claim.

Postexecution claim, panel, review, and state updates change declared inputs.
This initial cache remains historical evidence; a final content-bound
reproduction to the non-overwriting canonical cache is required before PR
delivery.

## Final content-bound reproduction

The reconciled result packet and refreshed frozen-input manifest were
committed at `e6081b33781d916588171e98e0df11bcc5f7bc8e`. The science source
outside the three refreshed manifest hashes remained byte-identical to the
green initial source. The final state and source repin were committed at
`6015be4d90` before execution.

```text
source SHA-256: 977b26b38eb46b71c2cccccc9e84a6b0679af56e5d0d1a3f32a3fd659558d087
input fingerprint: fc1a37a36858dbd97ef485c950fd4b70ede8c102d065164ab99c3fe8b4faecc2
canonical cache: logs/runner-cache/admissibility_d4_existing_qubit_lease_autonomy_gate_2026_08_30.txt
canonical cache SHA-256: 789d9a3323a33ffaaddd9af0e04a1584c876113d4bcd7efdf37d2a2c5689e2b1
elapsed: 531.82 seconds
exit: 0
stderr: empty
TOTAL: PASS=24 FAIL=0
```

The reproduction repeats all `23` named science checks, all `25` designated
mutation rejections, all seven derived witnesses, all five substantive
resolution lines, and the exact positive-only terminal. The runner and all
`43` declared inputs remained unchanged across execution; the canonical cache
is fresh.
