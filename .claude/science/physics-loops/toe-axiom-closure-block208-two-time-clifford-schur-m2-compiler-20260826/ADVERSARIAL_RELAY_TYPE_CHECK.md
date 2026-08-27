# Adversarial Relay And Type Check

Verdict: **PASS with qualifications** on frozen source bytes.

```text
note sha256:   31486ea1c14607be4c58352f62e4c47518450e551229a338c4237d5e6fa681ca
runner sha256: 5f363347df0fe5356ae544f8cbf5f902e71072761642dfc4407d71a9b3425024
primary:       10/10
mutations:     38/38 rejected
```

The checker independently confirmed relay normalization, the componentwise
score `3 delta r delta_ij`, both Fourier displacement signs, literal actual
reverse under `(z,u)->(zu,u^-1)`, radial/exterior scaling, the four temporal
weights, the `1/8` witness, and absence of a `p/q` argument in the relay law.

The no-side-channel result is narrow.  The fixture still externally prepares
phase/radial `M2` inputs, and the host supplies the time coordinate, branch
placement `t+delta`, incoming/outgoing carrier, tensor-leg typing and routing.
No formation, locking or permanence rule is executed.

The checker found and caused correction of one substantive overclaim: the 36
endpoint output states are full-rank and pairwise overlapping, so distinct
contents are not 36 perfectly distinguishable one-qubit Records.  The final
note/runner now classify the construction as a mathematically labeled CP
instrument with Record readout open.  It also caused the scalar relay score to
be written correctly as a componentwise score.

Non-blocking hardening: the primary relay's `temporal_target` is assembled from
the four columns and inherited weights, so that local residual is partly
self-confirming.  The adversarial checker independently formed full source
minus the 14 spatial columns in forward and actual reverse and obtained the
same four-column result and witness.  The structurally independent campaign
checker is required to retain that stronger construction.

This is an independent science check, not `review-loop`, an audit verdict, or
retained status.

After this frozen scientific pass, the source note received only cache/checker
links, an independent-check receipt, and section renumbering.  The same checker
verified that delta as `PASS` with no scientific widening or contradiction;
the final note SHA is
`1f64b32a6d0b9c1fd4e176c4bee1b990e9b7135c1033223a9cdae6f473de8492`.
