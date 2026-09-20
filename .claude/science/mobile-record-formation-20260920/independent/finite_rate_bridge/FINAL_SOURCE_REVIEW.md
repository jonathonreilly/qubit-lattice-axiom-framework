# Final scientific source review: finite-rate and spatial continuation

Completed 2026-09-20. **Confirmed within the stated mathematical scope; no
unresolved actionable findings remain.** This is scientific scrutiny, not
audit, retained-status application, or a landing decision.

Final sources read and confirmed:

* `docs/MOBILE_RECORDS_FINITE_RATE_CONTROL_AND_SPATIAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-20.md`:
  SHA-256 `423eba32f704e510331bfbb6dba78ea0a35db129854547b155fd76f27248d917`.
* `scripts/mobile_records_finite_rate_spatial_bridge_2026_09_20.py`:
  SHA-256 `c81de898311789470c834686ecfb5287b96d1fe73c7ae60cab4f3f9ec686af0e`.

The complete original sources and the complete subsequently extended sources
were read. A source-identity check caught the concurrent extension, so the
new material was included before confirmation. The final claim-scope edit
was checked in this same review: reversing precisely that edit reproduces
the completely read extended note hash
`b73efa1f8977ed12a478a10f33fb6b54e930a5e5471be88864f9f8ab69829460`.
The runner hash was checked before and after the recorded execution suite.

## Resolved finding

After adding the general content-eigenfunction extension, the machine-readable
scope's following sentence could be read as extending the Duhamel bound to
that entire family. The body correctly restricted that bound. The final
scope now explicitly limits the Duhamel result to the j-family with
`0<=j<1` on regular tori. This resolves the finding and matches equations
(15)--(17); the general-chi extension retains only its local generator and
Fourier identities. No substantive error was found in the eigenvalue formulas.

## Mathematical coverage and independent evidence

**Finite-rate bounds and correction.** The main bound and hazard-clock
representation match the independently derived, previously sealed results
in `REPORT.md`. The note's operator S is precisely the same weighted
projection operator restricted to mean-zero functions. It is self-adjoint,
with `b_- I<=S<=b_+ I` there, without a commutation assumption. The waiting-time
estimate follows from the weighted centering constant and Cauchy--Schwarz.
The Poisson expansion follows from the correctly ordered resolvent identity;
its quadratic remainder has the stated powers of epsilon, gap and hazard.
The signed first-order approximation has mass one, sufficient for the
half-L1 observable bound even when it is not a probability distribution.

New independent exact checks tested the Poisson remainder and waiting-time
bound on 30 small-chain cases, including a noncommuting three-state example.
For the six-site pair class, a different gap certificate uses the principal
cofactor of
`diag(pi)L-(2/5)(diag(pi)-pi*pi^T)`; all 14 Sylvester pivots are positive.
The form kills constants, so this proves the requested Poincare lower bound
without using the primary runner's mean-zero basis. The hazard variance is
`233/1369`. At epsilon `1/1000`, the independent six-orbit calculation gives

```
pre-birth TV       = 2615080197282/52497899773319383,
first-order error = 723791280601527/1178577849911020148350.
```

The third-birth derivative is `-16823/29030544`, both from the Poisson solve
and by differentiating the exact rational probability function sealed before
the primary continuation was read. The note's numerical values agree.

**Graph ratio and accessibility.** The second-birth law is exactly static
for every epsilon because the first single-record law is stationary and its
total hazard is constant. The spanning-tree leaf argument correctly proves
connectivity for indistinguishable occupied sites; its induction preserves
the remaining target occupancy and does not move frozen leaves. It is used
only for the identical-pair class, so disconnected different-content sectors
on a path cause no hidden assumption. The wedge sum, insertion multiplicity,
forest partition and binomial identity give the displayed ratio. The
bounded-degree, fixed-j deficit is O(n^-2) at fixed three records; no
positive-density or accumulated-event limit follows. The additional
covariance estimate is explicitly conditional on its uniform bounds.

Independent direct sums agree on 12 path, cycle, star and ladder cases.
A triangle at j=1/2 instead gives ratio `73/78`, whereas the formula outside
its domain would give `18/19`; this confirms that triangle-freeness must
remain a hypothesis. The cycle deficit and limiting coefficient `1/6`
follow directly from the stated counts.

**Vacancy response.** The all-density W=1 first-moment generator matches
the sealed independent derivation, with no factorization assumption.
The Fourier decay, integrated initial-perturbation response and diffusive
scaling have the correct factors of one-half and six. For positive kappa,
an independent characteristic-root calculation verifies the infinite-chain
kernel using
`rho=1+kappa-sqrt(kappa(kappa+2))` and amplitude
`1/sqrt(kappa(kappa+2))`: the recurrence, unit impulse and total mass
`1/kappa` all hold. Here `0<rho<1`; the integral is not asserted at kappa=0.
Positive kappa makes the bounded operator invertible by a convergent Neumann
series, justifying uniqueness. This is an initial-response operator identity,
not a physical source or an interacting infinite-volume conclusion.

**Local field, remainder and Duhamel bound.** The local formula and Fourier
symbol agree with `FIELD_MOMENT_CHECK.md`, sealed before primary-source access.
Each true vacancy hop changes a field component by at most one; each linear
hop term contributes at most one in absolute value. Only two birth contents
contribute to a chosen vector component. These facts give the conservative
C_z bound, while the residual vanishes on the radius-two one-record domain.
Taking expectations gives an exact inhomogeneous finite-dimensional equation.
For `0<=j<1`, its heat coefficient is nonnegative and the maximum-norm
semigroup bound is the stated scalar exponential, proving the Duhamel
inequality. It remains conditional on p_2(t), whose smallness is not proved.
The nonzero dense residual and isotropic-ensemble qualification are retained.

**Neutral-menu extension.** Symmetry gives the single-neighbor birth sum
`sum_a chi(a)W(a,b)=(W chi)(b)`; centering gives zero when there is no
occupied neighbor. This proves the local eigenfunction identity, with the
same isolated-hop argument. Five independent modes were checked
symbolically for arbitrary positive raw p,q,r, not only at the five runner
examples. Their eigenvalues, all three numerical examples, and spatial
multipliers are correct. General chi amplitudes and pair-weight maxima are
not silently inserted into the vector-specific remainder bound.

The new PR #8546 paragraph is explicitly provenance and imports no theorem
needed by this note. The normalized modes are defined and derived locally;
the paragraph does not adopt a physical scale or convert a fixed-density
motion observation into a formation result. I did not repeat the author's
inspection of that PR or independently certify its reported observations.

## Execution and source boundaries

The final primary runner exited 0 with `TOTAL: PASS=22 FAIL=0`. All eight
declared mutations exited 1 and failed their declared families. The
oversized-gap mutation also failed the Poisson family. Full evidence:

* `PRIMARY_BRIDGE_RUN.log`, `PRIMARY_BRIDGE_EXECUTION.json`, and
  `bridge_mutation_logs/` contain the final runner and mutation results.
* `REVIEW_EXTRA_CHECKS.py`, `REVIEW_EXTRA_RESULTS.json`, and
  `REVIEW_EXTRA_RUN.log` contain the additional independent calculations.
* `BOUND_SEAL.json` and `FIELD_SEAL.json` remain unchanged. The earlier
  milestone note and runner were hash-checked against their prior review
  receipt and are unchanged; their review was not redundantly repeated.
* `FINAL_SOURCE_REVIEW_SEAL.json` pins this report, final source identities,
  execution receipts and independent check code.

The runner's exact finite computations support the examples and certificates;
the general inequalities and graph claims rely on the proofs reviewed above.
Its Fourier matrix checks use floating arithmetic at the stated tolerance;
the independent prior side-four checks and analytical Fourier derivation
provide separate exact support. Repository-wide lint, canonical-cache
generation, bibliography/novelty searches and formal audit are outside this
scientific review. No primary source, Git state, PR, or audit record was
modified by this reviewer, and no redundant frozen source copies were made.
