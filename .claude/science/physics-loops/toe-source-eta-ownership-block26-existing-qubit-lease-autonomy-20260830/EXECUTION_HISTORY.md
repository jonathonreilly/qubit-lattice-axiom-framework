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

Pending postexecution packet freeze and repin.
