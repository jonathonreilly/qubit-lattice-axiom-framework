# Independent review of the LGF adoption in TSE55

2026-10-29. Reviewer: Codex, fresh restricted consumer-review context, with no
part in the coordinator's edits. **Same-family review.** The assignment requests
Astra/max; the report does not infer independence from a model label. The
producer review was required reading, so this is not blind to its conclusion.

**No blocking defect found in the frozen consumer amendment.** The adoption
matches the proved scalar/free library, including the added torus-range
sentence. This verdict covers that amendment only. It supplies no new result
for the interacting Wilson measure, continuum existence, or physical continuum
mass gap, and grants no audit or retained status.

## Frozen scope and read coverage

All paths below are relative to this report's directory. The reviewed unit is
the complete TSE55 delta from commit
`88130072aa683af83562ecc78a64dcc71fe75c4c` to the working source with SHA-256
`a894d1b2439a7b83311175c9e6e30f6fb52cc015a74c6be7e839be8192a7869a`.
This includes committed amendment `51fca25c21dd5233294555ddc21ca0801627f6a0`
and the uncommitted explicit torus-range sentence. The original TSE55 hash is
`d02cc8b265c20da5fc59812a59d68e12d3c9a550d9f9df0890db1c61a38f7340`.
The [frozen source diff](checks/review_lgf_consumer_source.diff), applied to that
original source, preserves the exact reviewed amendment.

Read all 605 lines of [LGF](LGF.md), all 331 lines of
[REVIEW_LGF](REVIEW_LGF.md), the entire consumer diff, and the complete adoption
receipt. Read TSE55 lines 1–260, 417–478, 518–578 and 620–723, covering the
objects, weights, signs, free kernel, amended FREE argument, direct theorem
interface, all amended status summaries and the remaining-condition statements.
An all-file LGF/import/status search checked the other references. Read
CODEX_REVIEW_TSE lines 125–182, including the relevant R9, R11 and R12 findings,
and LINEAR_PACKAGE lines 1–96 for the lattice/form conventions. This is not a
new whole-TSE55 proof review; the historical review's other findings remain.

| Bound source | SHA-256 |
|---|---|
| TSE55.md | `a894d1b2439a7b83311175c9e6e30f6fb52cc015a74c6be7e839be8192a7869a` |
| LGF.md | `40ea604c79f17027129628bc8b31f5fd6209da21dded864bf45a422dad24505e` |
| REVIEW_LGF.md | `d6c9b4f4352bc2693ffdcabfbfa375dfc05dfa584bdd826a6a9afd1ae7ea455b` |
| CODEX_REVIEW_TSE.md | `b70b1236e525fe5e3c83cd99b9f7142801a0a215f7e4a34879cdca50917d3edf` |
| LINEAR_PACKAGE.md | `0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad` |
| PROCESS_LIGHT.md | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |
| checks/full_proof_lgf_consumer_adoption.json | `595daa2d7d5f3067b6ef80388d943a20e98f9b8c469239d251e623914c67db13` |

Applied AGENTS, SCIENCE_WORKFLOW, PROCESS_LIGHT and the applicable review-loop
references. Review-loop and its references were read from fetched main
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`; the local AGENTS, workflow and
freshness procedure match that revision. The fetched planning instruction is
`56c5c0ab64f532c5784e895b2f9aa6894fa334e0` and supplies no mathematics.
The axiom memo and primitive registry were read; this is a theorem in an
explicit mathematical lattice/Gaussian setting and uses no framework primitive
to infer a physical Yang–Mills statement.

## Analytic checks

1. **Operator, Fourier measure and zero mode — confirmed.** TSE55 200–212
   reproduces LGF (1)–(5). Acting on exp(i xi.x) gives
   `sum_j(2-2 cos xi_j)=4 sum_j sin²(xi_j/2)`, with leading symbol `|xi|²`.
   Thus `Delta=8(I-P)` and `c_4=1/(4 pi²)` have the required relative factor.
   Finite Fourier orthogonality with weight `T^-4` gives exactly
   `Delta G_T=delta_0-T^-4` and zero counting mean. Both defined differences
   approximate positive partial derivatives; repeated indices and their
   uncentered stencils are within LGF's theorem. The torus corrections are
   separately `T^-2`, `T^-3`, `T^-4`. TSE55 no longer asserts an uncorrected
   all-orders torus estimate.

2. **Grouped images and lattice correction — confirmed.** TSE55 213–219
   retains the base `Phi(z)` in S_T, subtracts each image constant, and groups
   complete signed-permutation orbits. In an orbit, the Hessian trace terms
   cancel because `8/4-2=0`; odd Taylor terms cancel by inversion. The surviving
   fourth-order remainder is summable as `|n|^-6` in four dimensions.
   Away from the source, `-sum partial_j² K_T=-T^-4`; a radial quadratic has
   `-sum partial_j²(b|z|²)=-8b`. This independently fixes the positive
   coefficient `b=1/(8T^4)`. The local identity is not a claim that the
   polynomial itself is periodic. The cited shell construction explicitly
   keeps the continuum modes `k=T l`, `l!=0`, which contribute `+a_*T^-4` to
   f_T and therefore `-a_*T^-4` to E_T. No lattice image sum is substituted
   without that prescription.

3. **Hodge operator, free-law scope and curvature signs — confirmed.**
   TSE55 138–156 and 220–225 agree with LGF 488–548. With the counting inner
   product, `(nabla_j^+)*=-nabla_j^-`, and the exterior/interior
   anticommutator reduces `dd*+d*d` to the scalar graph Laplacian. On the
   gauge quotient the action is `||dB||²/2`; the pushed-forward covariance
   is `d Delta_1^-1 d*`, the exact-two-form projector. Gauge and harmonic
   link directions are killed by d. No coupling or colour factor is absorbed
   into this one-colour, coupling-one statement.
   Expanding the two curls directly, the y forward difference of G_T(x-y)
   is a negative z backward difference. The four coefficients of the mixed
   Hessians are therefore `(-delta_nu,sigma, +delta_nu,rho,
   +delta_mu,sigma, -delta_mu,rho)`, matching TSE55's `-X/(4 pi²)`.
   These are plaquette base points in lattice units, not plaquette centers
   or physical coordinates. As an algebraic sign/normalization check, summing
   the six diagonal orientation kernels gives
   `3(delta_0(z)-T^-4)`, as follows directly from the scalar Poisson equation.

4. **Squared-kernel error — confirmed on its stated domain.** Put
   `B=2^1002`, `E=G^F-D`, and use `|D|<=2^12 r^-4`. Then
   `|2DE|<=2^1015(r^-9+r^-4 T^-4)`. Also, for `r>=1`, `r^-10<=r^-9`
   and `r^-5 T^-4<=r^-4 T^-4`; for `r<=T/4`,
   `T^-8<=r^-4 T^-4/256`. Hence
   `E²<=B²[r^-9+(2+1/256)r^-4 T^-4]`.
   Both terms fit under the stated `2^2010(r^-9+r^-4 T^-4)`.
   This is a direct algebraic check, not a numerical fit to the producer.

5. **New support-to-torus range sentence — confirmed.** From TSE55 101 and
   143–144, a nonzero w_f(p) has a corner x in supp f_lambda; similarly q
   has y in supp g_lambda. Write their base points in fine lattice units as
   `x_p=x/a-v_p`, `x_q=y/a-v_q`. Each corner offset v has 0/1 components in
   its two plane axes. Thus every component of `v_p-v_q` is in {-1,0,1} and
   `|v_p-v_q|<=2`, also for different plaquette planes. Consequently
   `D_- lambda/a-2 <= r <= D_+ lambda/a+2`.
   The existing separation requirement `L^(K-m)>=4/D_-` implies `r>=2`.
   With `a=L^-K<=1`, `lambda=L^-m<=1`, `T=R/a`, and the new threshold,
   `a r<=D_+ lambda+2a<=D_++2<=2(D_++1)<=R/4`.
   Therefore every weighted pair obeys `1<=r<=T/4`.
   The retained support condition `R>=8 rho_F` allows compatible local lifts
   of the corners and base points; since also R>=8, their bounded shifts do
   not introduce a torus-wrapping ambiguity. Increasing R_0 preserves any
   stronger input threshold and makes no change to the fixed-m, then K/R,
   then m limit order. As in the existing review's R9, level indices are
   nonnegative and input thresholds must be retained when taking maxima.

6. **Units at the FREE interface — confirmed.** Combining the squared error
   with the displayed weight-sum bound gives exactly the claimed scale
   structures: `lambda^8 a^-8 (a/lambda)^9=a/lambda`, and
   `lambda^8 a^-8 (a/lambda)^4(a/R)^4=(lambda/R)^4`.
   This checks compatibility of the supplied kernel input with FREE's error
   terms. It does not re-prove FREE's separate test-function replacement or
   Riemann-sum argument, nor the rest of the interacting theorem.

## Status and remaining boundaries

All changed LGF status references in TSE55 are consistent: the paragraph at
200–228, usage list at 448, named input at 473–478, input inventory at 569,
claim inventory at 655, and coordinator summary at 698 point to the local
proved scalar/free library and its actual review. The amended paragraph and
named-input entry explicitly restrict what the import supplies. The old
numeric-check inventory correctly continues to say those old checks do not
test LGF; it is not an uncorrected import-status assertion.

LGF, REVIEW_LGF and historical CODEX_REVIEW_TSE are byte-identical to their
versions at the original comparison commit. In particular R11 has not been
rewritten to claim earlier verification. R9 remains a conditional assembly,
and R12's outstanding matching obligations are untouched. PL-1L, the other
FREE/TS hypotheses, H_int as a whole, nonlinear flow, continuum construction
and physical continuum mass gap receive no promotion from this amendment.
No whole-TSE55 clearance or resolution of its other historical findings is
implied. Balaban and Dimock remain credited for the broader gauge-theory lane.

One review iteration; no material findings requiring correction, no source
fixes, and no skipped identified consumer defect. Import inventory: explicit
mathematical operator, counting/Fourier, boundary and Gaussian-law conventions;
proved local scalar/free theorem; no fitted, measured or load-bearing external
literature value. The consumer matching obligation is CLOSED within this
scope; downstream interacting claims remain CONDITIONAL/OPEN as above.
Audit separation is preserved. No new audit claim ID or verdict is authored.

No numerical experiment, FFT, interval computation or scientific runner was
needed or executed. Python was used only for source/diff/identity bookkeeping.
Hash verification, exact historical-file preservation and the focused
`git diff --check` passed. No formal proof-assistant run or combined branch
pipeline is claimed; branch integration validation remains the coordinator's
separate operation. No commits, pushes, source changes, audit/ledger writes
or lock changes were made. Only this report and its `checks/review_lgf_consumer_*`
artifacts were created. The [receipt](checks/review_lgf_consumer_receipt.json)
binds those artifacts and source identities. Changed relevant source bytes,
premises or consumer interactions require affected confirmation.

VERDICT: LAND
