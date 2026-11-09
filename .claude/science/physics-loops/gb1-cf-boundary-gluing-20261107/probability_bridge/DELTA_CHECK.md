# SOURCE-EXPOSED clarification-delta check

Scope: validate only the recorded clarification delta after `SOURCE_CHECK.md`.
This is not a new independent derivation, numeric job, or audit. Earlier receipts
were preserved unchanged. Source root:
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/probability_bridge`.

## Exact source validation

The current files match the declared final SHA-256 hashes:

- `RESULT.md`: `63f289a3745e06d80e6efe8189074f7c50f41bb8da19321a39ae8487ee5fde52`.
- `ASSUMPTIONS.md`: `2194bce37b90b4a8e01a5db6d9f5df10452bc28409dc36d956f9d9251e2314d9`.
- `source_delta.json`: `9eeb61b86951ac400c05ec0367e31080804ffcc3f31c9e359b613508abd04991`.

A deterministic read-only Python check applied all five RESULT replacements and
all three ASSUMPTIONS replacements in reverse, asserting each specified occurrence
count. It reproduced exactly the previously reviewed hashes:

- RESULT: `70dd5037ba567a9d2547f297944de55be022b229cc7e868496542c2090d2a30f`.
- ASSUMPTIONS: `6e445f7facaca490b30eaca96736e4f36185ce66ed58a360a7cd9e4c10af6c07`.

Applying the forward replacements then reproduced both current texts exactly.
The source files themselves were never rewritten by this validation.

## Substantive disposition

All changed wording and its surrounding argument were inspected. The correction
resolves the scope/provenance finding in `SOURCE_CHECK.md`:

- E0 explicitly supplies normalized record-event probabilities per device context.
- One forming site's local law is distinguished from a multi-record joint law,
  which must be separately supplied or derived.
- No probability space jointly covering different device contexts is inferred.
- The common fixed preparation now explicitly governs E0–E3. Within-context
  additivity comes from E0; E2 identifies effect probabilities across contexts;
  the unchanged universal E3 supplies every summable pair's common realization.
- The theorem, remaining constructive target, and assumption ledger consistently
  identify E0–E3 as conditional premises. They do not present the joint-law
  assumption as derived from one-site Admissibility.
- “Complex-algebra isomorphisms” now states the exact scalar-trace invariance scope.

No remaining issue was found in this clarification delta. The earlier mathematical
checks carry forward because reversal recovered their exact reviewed source and
the inspected changes are confined to these corrections. The unresolved physical
effect bridge, preparation selection, and other verification limits recorded in
`SOURCE_CHECK.md` remain; this delta validation grants no scientific status.

## Preserved receipts

Hash verification confirmed these files remain byte-for-byte unchanged:

- `INDEPENDENT.md`: `cf73c8a3aa2a7e6ec36bba981e22a0969025b77b893dce28e77a1458059caef3`.
- `CHECKPOINT.md`: `73fbc5d86ed7558ba518e13be6fdb1a4d7fa487fb88f8787d31a92a497b0ccf4`.
- `SOURCE_CHECK.md`: `08cd2d666ea159619ed6acd1585ca884cf4192cd85961b1cda24438d8f052c41`.
