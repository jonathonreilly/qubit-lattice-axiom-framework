# Assumptions And Imports

Allowed inputs in the new runner:

- Hermitian pencil matrices already used by the A-BCC finite-scan lane.
- Retained sigma set `(2,1,0)`, `(2,0,1)`, `(0,1,2)`, `(1,2,0)`.
- PMNS central angle target `(0.307, 0.0218, 0.545)`.
- Active chamber inequality `delta + q_+ >= sqrt(8/3)`.
- Bounded finite coordinate box `[-50,50]^3`.

Retired import for the repaired finite-scan claim:

- The live runner does not import the archived five-basin coordinate chart or
  expected C_base/C_neg labels as inputs.

Still open:

- No interval/root-isolation theorem excludes all additional narrow basins.
- The old out-of-chamber chart is preserved as historical provenance only, not
  as the primary proof surface.
