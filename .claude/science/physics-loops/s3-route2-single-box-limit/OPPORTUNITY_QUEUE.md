# Opportunity Queue

## Ranked Next Opportunities

1. **Route-2 nonblind E-center finite-size/convergence bridge**
   - Goal: generate a multi-size measured E-center scan or prove a convergence
     law that makes `q_E -> 15/8` exact rather than single-box support.
   - Retained-positive probability: medium.
   - Missing imports: box-size data or theorem.
   - Runner availability: parent measured-calibration runner and cache exist;
     needs extension.
   - Review landability: high if framed as exact-support or no-go.

2. **Route-2 source/readout derivation of the typed magnitude bridge**
   - Goal: derive `|gamma_T(center)/gamma_E(center)| = R_conn = 8/9` from a
     nonblind source/readout primitive instead of importing it.
   - Retained-positive probability: medium-low but high upside.
   - Missing imports: typed nonblind source primitive.
   - Runner availability: block52/block53 surfaces provide direct checks and
     no-go boundaries.

3. **E-center fingerprint consumer map**
   - Goal: locate downstream consumers that can use the block54 fingerprint
     as an acceptance test without claiming endpoint derivation.
   - Retained-positive probability: low-medium.
   - Missing imports: downstream consumer selection.
   - Runner availability: block54 runner and parent exact-readout runners.

4. **Alternative source-domain primitive search**
   - Goal: search retained atlas/tool surfaces for a primitive that is not
     E-center-blind and can distinguish the target endpoint.
   - Retained-positive probability: low-medium.
   - Missing imports: nonblind primitive.
   - Runner availability: broad atlas search plus targeted checks.

## Recommendation

Use opportunity 1 for the next `/goal`.  It directly attacks the blocker
exposed by block55 and is more likely to move the audit than another boundary
around the same single-box datum.

