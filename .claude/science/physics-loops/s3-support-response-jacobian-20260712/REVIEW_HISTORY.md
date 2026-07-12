# Review History

- Primary finite-operator runner: `PASS=10 FAIL=0 TOTAL=10`.
- Iteration 1 used parallel code/math, physics/retention/labeling, and
  import/governance/audit-compatibility reviewers.
- Iteration-1 findings: two formula/documentation bugs, underdeclared protocol
  conditions, overbroad Jacobian/nonzero language, stale premise/status
  vocabulary, and weakly scoped firewall checks. All were addressed in the
  fix pass; iteration 2 is pending.
- Independent math check: the preexisting helper pipeline reproduced both
  endpoint vectors, both normalizations, `delta_gap=1/6`, and `Xi` to at most
  `5.421e-20` endpoint-vector difference and `1.388e-17` normalization
  difference. An independent old-lattice construction verified
  `H[(1/6)d_center]=e0-arm_mean` with zero residual at sizes 7, 9, and 15.
- Sibling-runner pin sweep: `frontier_quark_endpoint_readout_constraints.py`
  passed `14/14`; `frontier_carrier_orbit_invariance.py` passed `65/65` after
  preserving the historical bounded/non-exact scope markers. The separate
  `frontier_v_even_theorem_retention.py` run has one preexisting prototype-note
  phrase failure unrelated to this changed note.
- Required `review-loop` iteration 2: pending.
- Independent audit: required; not performed by this science block.

## Promotion value gate

| Gate | Answer |
|---|---|
| V1 specific obstruction | The quoted blocker says the derivative was only a new symbol over named inputs, with no first-principles computation or independent algebraic closure. This block supplies a self-contained finite-protocol endpoint computation plus the exact `1/6` lemma. |
| V2 new derivation | The new artifact inlines the finite Green operator, shell normalization, interpolation/probe conventions, and ADM evaluation; computes every endpoint value; derives the four-evaluation coefficient; and proves the local support-gap and affine-uniqueness lemmas. |
| V3 already completable by the audit lane? | No. The prior restricted surface did not expose a self-contained endpoint computation or the finite-protocol conditions needed to reproduce it. Framework primitives do not select this ADM readout, so the result must be reviewed strictly as the declared bounded protocol rather than inferred from the axioms. |
| V4 non-trivial marginal content | Yes. The endpoint coefficient requires repeated finite-lattice solves and sampled Einstein-tensor evaluation; it is not a textbook identity or renamed definition. |
| V5 one-step prior-cycle variant | No. The closest landed May 2026 presentation imported helper endpoints and formed a quotient. This block replaces that load-bearing import path with an inlined evaluation, exact local support lemma, explicit conditions, and independent controls. |
