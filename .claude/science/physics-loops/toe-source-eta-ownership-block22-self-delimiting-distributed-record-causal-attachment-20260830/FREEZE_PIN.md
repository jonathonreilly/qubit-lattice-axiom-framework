# Block22 freeze pin

The corrected preregistration was committed at
`d12f2fbab0ef082e40491ad05d02425d6048d628` before any Block22 target runner,
cache, or mutation existed or executed.

Frozen SHA-256 values:

```text
a96dd59352c5d047826315904b4aaa8042f685f0af0aab9ad24b08fe03eb7db0  GOAL.md
91df8d224df193d875f995d769a6becff9428328b317ecc78e834869b8a405b3  AUTHORITY_GATE.md
03c1e648dcaeca221dde31a73b307311fe000c96183f08bce80be222a81a41b3  PREFLIGHT_WITNESSES.md
05a7e32c186dd64cd0d5d4cdc68946a37082acf8dba704bfe6384cd88c90fb56  PANEL_RETURN.md
23f24a92ce3a20bcb4c3d5328b9db48f0f7755b5997e0d2f3c7fc7436395fa1e  INDEPENDENT_PREREG_ATTACK.md
2c53bdb32539b1803891c1e6a1dd242761bd30496260c602e62655fe8d2553e6  APPROACH_REGISTRY.md
7c99763028869dd6353668c14277e913a5c5c3da878f03b3bd38e1db80100140  MUTATION_PLAN.md
029b914cdd2688ead20949be42f3c095d8bc12a5b0ca546c7cf9e4541e1bad0d  NO_GO_DISCIPLINE_CHECKLIST.md
```

The primary and independent runners must verify these values before target
execution.  Post-execution adjudication, N1--N8 completion, notes, and state
updates must be written to separate unfrozen artifacts.
