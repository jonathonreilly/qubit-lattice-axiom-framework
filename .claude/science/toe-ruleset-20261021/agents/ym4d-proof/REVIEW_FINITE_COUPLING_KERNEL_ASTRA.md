# Independent review of the finite-coupling scalar kernel

The frozen [source](FINITE_COUPLING_KERNEL_ASTRA.md), SHA256
`c85ce075fdae1249b520089a462c8cf3107c0b26901d4dcd55a78c48b78ebc8b`,
is sound at its stated scalar-kernel and local preintegration scope. No
blocking mathematical finding or required source correction was found.
The proof establishes the fixed-neighborhood, probability-Haar SU(N)
factorization and all fixed mixed derivatives in FK2/FK16, together with
the stated S4-prime local bounds and the explicitly restricted CB14
composition. It does not establish an integrated nonlinear RG remainder,
continuum existence, or a physical continuum mass gap.

This is one source-unit review, not whole-PR approval, a main-landing gate,
an audit verdict, or a retained-grade assignment. The coordinator retains
Git, current-main preservation, combined validation, locks and shared status.
I changed only this report and `checks/review_finite_coupling_kernel_*`.

## Independence and frozen evidence

This is Codex reviewing Codex in a separate context, with no author role in
this target. Astra/max was the requested configuration; runtime backend
identity is not independently observable. No cross-family or blind-source
independence is claimed. All 590 source lines were read, including section 9's
aggregate diagnostic results, before independent numerical criteria were
written. The author scientific code and raw results were opened only after
the independent analytic reconstruction, implementation and results were
frozen at 22:56:53 UTC on 2026-10-29.

The [independent evidence receipt](checks/review_finite_coupling_kernel_independent_receipt.json)
has SHA256 `7e5931b5f86550066324ad2f2b137ef360440f8ae4ca50b71e2f4af8103ecfab`.
It binds the [independent reconstruction](checks/review_finite_coupling_kernel_independent.md),
[preregistered numerical criteria](checks/review_finite_coupling_kernel_criteria.md),
independent implementation and actual execution evidence. A launcher parent
directory index was corrected by inspection before any execution; its record
is preserved. No scientific criterion or tolerance was changed.

The author [receipt](checks/finite_coupling_kernel_receipt.json), SHA256
`1c8fe7055cbda74b167d73346a58e0c118362ccfd4c74988fdb7c55ab8725e0a`,
binds 12 artifacts. Every artifact hash and size matches. All 17 author input
pins also match. The [author read manifest](checks/finite_coupling_kernel_read_manifest.json)
has SHA256 `627122351b7005245f5c88248acb6b06decd1b2721c88eff8ab2935c01c25dce`.
These pin checks identify bytes; they do not assert complete reading of every
author-listed file. Actual reviewer ranges are in the
[review read manifest](checks/review_finite_coupling_kernel_read_manifest.json).

The selected methodology revision is
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`. Installed skill entry points were
read, their full differences from this revision were read, and applicable
references were taken from that same revision. [PROCESS_LIGHT.md](PROCESS_LIGHT.md)
controls this new lane's research-log format. Entry HEAD was
`0baee60a3999d599e706ca58fef9a0f64ffc2322`; the coordinator subsequently
preserved the author packet at `9658cc870d82401001e56b29f351aec5f5f58fa1`.
The target and consumed input bytes remained unchanged.

## Mathematical assessment

**Constrained saddle and global cycle, FK3–FK9 (source 53–155).** The
contraction follows from differentiating the matrix-exponential series in
complex HS norm. Its uniqueness ball is large enough to identify the two
solutions on overlapping unitary charts. The nonzero scalar difference
`E-F=2 lambda I` is required by the SU constraint; it was not replaced by
an unconstrained polar condition. On physical data the contraction preserves
su(N). The holomorphic top-form/Stokes argument translates the entire compact
cycle, so it has no omitted chart faces. The global odd-trace estimate has a
valid separate argument outside the small eigenangle cap and covers central
elements. Consequently the real-part drop holds on the full translated group,
with a uniform positive margin in the stated complex-t sector.

**Full-colour Laplace error, FK10–FK16 (source 157–280).** The Hessian bound
is a complex operator-norm bound, obtained by testing the bilinear trace form
on independent complex colour vectors. The logarithm-series branch fixes the
full D-dimensional determinant. The Haar density is the determinant of the
exponential differential, including its evenness and quadratic coefficient;
its probability normalization `h_N` is retained. On the symmetric real ball,
the odd cubic times the even Haar factor integrates to zero exactly. The
finite exponential remainder, multiplied by the Gaussian, is controlled by
moments of degrees 2,4,6. Outside that ball, a principal logarithm of norm less
than r would necessarily be traceless, which justifies the global tail split.
The remaining group and Gaussian tails have the claimed exponential bounds.
This proves an actual uniform relative `O(1/t)` estimate, rather than
integrating an uncontrolled formal series.

The Gaussian constant in FK15 is `h_N (2pi)^(D/2) (det H)^(-1/2)` in the
stated HS Lebesgue convention. The fixed parameter margin and the t-disc
of radius t/4 lie within the proved holomorphic domain. In particular,
`arcsin(1/4)<pi/6` and `|z|>=3t/4>=3t0/2` when `t>=2t0`.
Joint Cauchy estimates therefore give the claimed mixed derivatives.
No small-complex-t conclusion is needed or inferred.

**Actual fields and local sums, FK17–FK23 (source 267–442).** The doubled
means are the mean of words and the mean of inverse words. Negative fine
edges in the left chart are `U0^-1 exp(-x)`; neither complex conjugation nor
inverse of the arithmetic mean is substituted. Each actual paired contour
has length at most `5L-4`, lies in its lifted two-block brick, and equals the
coarse link at the brick lift. The far seam at T=2 is excluded correctly.
Thus arbitrary real holonomies are compatible with the fixed local complex
chart. The joint coarse/fine variation keeps both mean matrices inside it.

There are at most `(8L-7)L^3<8L^4` positive fine links in one such support,
and at most eight coarse readers for any fine link. Anchoring one scalar
colour coordinate leaves at most `(D n_c)^(q-1)` choices for the others;
Cauchy's multi-index factorial is bounded by q!. This yields FK22,
including the same column estimate by derivative symmetry. The original
`24 L^4` divisor is retained. These counts apply before composition with
a stationary background and are not all-depth or source-reader estimates.
The unsubtracted vacuum is extensive, as the source states.

FK23 matches the actual [CB14 source branch](COVARIANT_SOFT_BACKGROUND_ASTRA.md).
Its chart is the same left free-link chart with zero tree displacements;
its source is the original Wilson epsilon and kappa remains fixed. CB14
gives `||a_(u,epsilon)||sup<=4RG delta_V` on its stated fixed source
polydisc. The additional `delta_V<=a/(16RG)` puts that image in the new
a/4 ball, while `delta_V<=delta_star` retains every CB hypothesis.
The pointwise Cauchy corollary follows. No holomorphic integrated partition
function, source-local summability, or all-depth stationary map is supplied
by this composition. The standalone scalar theorem does not depend on CB.

**Finite-u spread and determinant, FK18–FK24 (source 301–313,434–464).**
I rebuilt the [F6–F9](SOFT_FLUCTUATION_COVARIANCE_ASTRA.md) differentiation
using common-path Haar invariance. I also checked the determinant Hessian by
a distinct algebraic route, without taking its value from a t-asymptotic:
at alignment, for real tangent variations, `S'=0`, `tr S''=-average ||theta_tau-q||^2`, and completeness
gives `sum_a T_a^2=-(D/N)I`. Hence

    Tr_colour H'' = (D/N^2) tr S'',
    (log A)'' = -(N/2) Tr_colour H''
              = D/(2N) average ||theta_tau-q||^2.

Subtracting the tree Hessian and this determinant from the exact kernel
Hessian gives FK24. The coordinate-Haar precision `N^2/(6u)I` remains
separate. The FLOW coordinate change contributes `N^(q/2)` per q-jet;
UL9's additional division of tree energy by N is a different convention.
The positive half-log of the normalizer covariance determinant is already
present in [UL10](UNIFORM_ONE_LOOP_COUPLING_ASTRA.md); adding log A again
would double count it. FK24 makes no such addition.

The consumed STEP55 INV/PR/NZ arguments were read together with S5–S7 and
[CODEX_REVIEW_STEP R6](CODEX_REVIEW_STEP.md). In particular the rejected
ordinary-quaternion plus sign was not reused. CJ1, the FLOW normalization,
UL9–UL12, and the selected original BFT/NODEA/HINT2 passages were read only
to their stated interface scopes; no whole-file or full-theory confirmation
is inferred from those selected reads.

## Numerical evidence, failures and surviving mutation

The independent run passed 21/21 finite diagnostics. It used a separately
derived SU(3) Fourier projection expressed as a sum of Bessel determinants,
not the author's two-angle quadrature implementation. Exact bivariate
Gaussian moments independently gave 324,360,1080 and the Haar/quartic
contributions -6,+5. At t=32,64,128 the normalized tE values were
-1.07447915,-1.03544666,-1.01731397. The two winding cutoffs differed by at
most `7.1e-36` relatively. The scalar SU constraint has the independently
derived limiting derivative `t partial_lambda^2 E -> -10/3`; the t=128
value was -3.35917745, and the two finite-difference resolutions agreed
within `2.4e-14` before multiplication by t. Dropping lambda gives zero
and fails that criterion. Wrong leading dimension also fails its criterion.
These wrong-model controls are algebraic witnesses; they are not described
as executable mutations of the author program.

The independent geometry enumeration covered all 64 coarse-link labels on
the L=3,T=2 torus: 1944 paired words per direction, maximum length 11,
459 reader links per brick and maximum reader incidence 8. A wrapping brick
with arbitrary noncommuting SU(2) coarse holonomies had zero reported
baseline-word error. Analytic reasoning, not these finite samples, establishes
the general N,L,volume statement. The sampled t values are not certified to
exceed the theorem's deliberately conservative t0.

The author provenance is internally consistent and was checked mechanically:
the 49% free-memory gate failed before its child launch, the preserved sign
amendment at 22:27:29 UTC lies between that failure and the sole actual run
at 22:28:02, and reversing its exact condition change reconstructs the old
program hash. The old and new criteria hashes also match. The sign correction
is mathematically correct: `E=-3/(8t)+...` gives a coefficient `-3/8` in
`1-c_2=3/(2t)-3/(8t^2)+...`. It does not loosen the tolerance.
The original stdout equals its result file byte for byte.

The original total comprises 30 ordinary rows and five named wrong-model
witnesses. One reviewer-owned replay reproduced all 35 scientific check rows
and every scientific detail exactly. Only the output basename and routine runtime
metadata differ. Then actual executable source substitutions produced:

| Substitution | Outcome |
| --- | --- |
| Wrong quaternion vector sign | 31/35; Haar/translation checks fail |
| Remove traceless projection from saddle | 30/35; determinant and SU saddle fail |
| Delete Weyl Vandermonde | 32/35; eight-colour remainders fail |
| Double full-colour Hessian | 34/35; Hessian comparison fails |
| Multiply the actual means by4 | 34/35; fixed-domain check fails |
| Invert the mean instead of averaging inverses | 34/35; inverse distinction fails |
| Double the standalone cubic coefficient | 34/35; opposite-parity comparison fails |
| Delete lambda from the actual Weyl phase | 35/35; **survives** |

**Recorded coverage limit, author checker line 97.** The final substitution
replaces `+1j*lam*np.sin(ang).sum(axis=0)/3` by zero in `weyl3`. The complex
samples are tested only for grid convergence, so both grids can share that
error. The separate wide odd-cubic algebra probe still uses lambda and does
not detect this substitution. The survivor's
[source](checks/review_finite_coupling_kernel_author_erase_weyl_scalar.py),
[result](checks/review_finite_coupling_kernel_author_erase_weyl_scalar_results.json)
and [raw run](checks/review_finite_coupling_kernel_author_erase_weyl_scalar_run01_stdout.txt)
are preserved. This limits the sensitivity of the author's 35/35 claim; it
does not falsify the correctly written FK7/FK10 proof. The pre-exposure
independent lambda-derivative calculation above covers the omitted term.
No original success was restamped or strengthened, and no survivor was
converted into a detected mutation. The initial prediction that the
standalone double-cubic mutation might survive was disproved and preserved.

All reviewer numerical children passed their resource gates, used one
library thread and nice 10, and ran under 60-second wall/55-second CPU caps
with a resident-memory watchdog below 2 GiB. The independent child used
54% native free memory, load 1.83, 0.804 seconds and 101,088 KiB sampled peak RSS.
Author replay/mutation children used 55–56% native free memory and completed
in less than0.5 seconds each; their highest sampled peak was158,608 KiB.
All intentional failures, gates, raw stdout/stderr and the survivor are kept.
No additional broad replay was needed after these checks.

## Literature and disposition boundary

[Pemantle–Wilson](https://arxiv.org/abs/0903.3585) was consulted for comparison
with analytic complex-saddle contour deformation. The finite parameter-uniform
estimate and Gaussian normalization were rebuilt in the reviewed argument;
no published asymptotic statement was substituted for the needed uniform
inequality. Credit for the multiscale small/large-field architecture remains
with [Bałaban](https://doi.org/10.1007/BF01215223) and
[Dimock](https://arxiv.org/abs/1108.1335). The latter source concerns d=3 scalar
phi4. Neither attribution supplies the missing interacting d=4 SU(N) estimate.
No PDF was created or committed by this reviewer.

Proof obligations are closed at the stated scalar analytic scope, with FK23
using the explicitly matched CB14 provider. Mathematical normalizations and
the supplied Wilson/S4-prime model remain explicit; no framework axiom,
primitive, empirical target or physical identification was introduced.
The runner has the recorded coverage limitation, compensated at unit level
by independent analytic and numerical evidence. There is no negative theorem
or claimed impossibility here. No Lean claim, audit status or new ledger row
is issued. No target repair, Git mutation, full pipeline or integration gate
was performed by this reviewer.

The next mathematical interface remains a connected interacting remainder
estimate in the actual support-size/source norm, including the hard/history
complements and finite-u marginal projection. FK2/FK21/FK23 do not provide it.
They also do not establish all-depth nonlinear control, the continuum limit,
or a positive physical continuum mass gap. This source verdict approves only
the frozen scalar theorem and its stated local consequences for preservation
and further research. The [final receipt](checks/review_finite_coupling_kernel_receipt.json)
binds this report, source identities, actual read coverage and all evidence.

VERDICT: LAND
