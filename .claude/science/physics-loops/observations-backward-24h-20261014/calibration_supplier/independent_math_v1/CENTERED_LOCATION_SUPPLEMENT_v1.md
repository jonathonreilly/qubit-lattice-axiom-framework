# M11 specified location versus statistical mean: narrow supplement v1

The parent identified this interpretive issue before publication. I independently derived the supplied witness and froze `LOCATION_WITNESS_PRECHECK_v1.md` (d7a469d4946a5a83f783238b2ca4b7566943da539b5da50646bfcd43864c6d66) before reading the new canonical wording. I then read the complete exact note deltas, including the previously added Review record paragraph, and the exact preserved-primary/current-primary delta. No aggregate, simulation, observation or additional physical model was run or opened. Earlier independent and canonical reports remain unchanged.

For U uniform on the unit sphere in C^N, unitary invariance gives E[U_j]=0, E[U_j U_1]=0 and E[U_j conjugate(U_1)]=delta_j1/N. Hence E[U_j Re(U_1)]=delta_j1/(2N). With R=1+kappa Re(U_1), 0<kappa<1, the radius satisfies 1-kappa<=R<=1+kappa and is strictly positive. Its direction remains U, every moment exists, yet

    E[R U] = kappa e_1/(2N) != 0.

The witness is correct, including sign and complex normalization. It demonstrates nonzero expectation with bounded errors; lack of moments is not the explanation. In the general theorem moments need not exist. The specified c*u_f is a signal/location center about which the angular law is assumed, not automatically E[y] or E[y|T]. An expectation interpretation would additionally require an integrable error with zero first moment (conditionally zero given training for the conditional interpretation), not merely finite moments. The revised wording's “additional moment condition” is correctly understood in this sense.

This distinction does not alter the scale-free proofs: the supplied signal/location term is removed pointwise and R cancels before taking a probability distribution. It does not supply a new error law, receiver calibration or scalar state. Calling the template a signal model rather than a mean model is the appropriate correction.

The source chain is now:

| Scope | SHA256 | Bytes |
| --- | --- | ---: |
| Previously reviewed note | 00310bf4a764ec80b3c00faa5eed53149fa2713184cf7a08b7ac23f156a67231 | 24860 |
| Preserved note after Review record addition | 6e321840bf78a2687fb516aca2e46da293c72c9499dd5175bf5434da017fcb10 | 25355 |
| Current note with location clarification/witness | 571c6b8f108de2c4100653f0fd2509bf33745bb02b5bdee1d2c2b2530c7d71b3 | 25871 |
| Preserved primary before terminology correction | 256f62863ff7c7f5e5aaf141bf44c03426f5711d6d45b16de8a8e58bfd29fdfd | 6163 |
| Current primary | 57f4325cc686482d33dd41e24649d0a1d083f3fd832ef4bf61db1a583f998741 | 6165 |
| Unchanged completely reviewed geometry helper | c9b1e47cbaeaa8faf31543541e983c19f23a4e4d1fdfebae88e1e0590843e7aa | 9491 |

The Review record insertion keeps earlier quantization/discrepancy results separate, says the new angular premise does not derive the missing physical bound, and leaves landing/audit to their later lanes. This is consistent with the bounded mathematical scope. The subsequent note delta adds the correct witness and replaces ambiguous mean-model labels with signal-model wording in the supplier, dependency and next-action text. It does not change the previous F laws, cone formula, coverage, geometry code or observation numbers.

The primary was outside my earlier complete-source review. I do not retrospectively claim to have checked its implementation. For this authorized narrow comparison, the complete byte diff is exactly one replacement inside `probability_interpretation`: “supplied mean/direction/cadence/ADC premises” becomes “supplied signal/direction/cadence/ADC premises.” A byte replacement assertion confirms no other primary bytes changed. Its unchanged code is outside this supplement's scientific review.

`LOCATION_SOURCE_FREEZE_v1.json` pins full source/snapshot identities; the three `LOCATION_*_DIFF_v1.patch` files preserve the complete deltas. No unresolved mathematical issue was found in these changes. No final envelope, mutation receipt, empirical result, integrated-main state or formal audit was revalidated here.
