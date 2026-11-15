# Second independent hostile review of WT0

Reviewer: Codex, fresh context, 2026-10-29. Same-family review; I authored
none of the reviewed work. Earlier verdicts were treated as assertions to
test, not premises. No numerical or symbolic runner was executed.

**No material defect found in W_T0's explicitly conditional, marked-system
result.** This confirms the reduction at its stated scope. It does not
construct Yang–Mills, discharge the original e-only F1, or establish
non-freeness under arbitrary observable identifications.

Source revision: checkout HEAD
`9658cc870d82401001e56b29f351aec5f5f58fa1`; WT0 landing commit
`364ea2b6eccd044b34ada4eb551ea1d08dd6b8a6`.
The locally available `origin/main` is
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`; remote freshness was not checked.
The six requested source identities are:

| File | SHA-256 |
|---|---|
| W_T0.md | `eaf064445948aed7096e7d4e53c20ed4407d1c87458943feb52f3d7638f2e804` |
| W_T0_LOG.md | `0d6cac09733448908c4be4fae5d80e137387fcc4ed97154a873df8fe5eb4b324` |
| REVIEW_W_T0.md | `29b66e03a01ba9d98613fc18ab978a770677a88d2219b0d7fb34db9f2197cd68` |
| HINT2_55.md | `e617800fa0426a6099b5b6966cf383d118eeed33f363b5c9ff866108a6537dbf` |
| CODEX_REVIEW_HINT2.md | `062186c586903dc179ecbb50e78f102094dec23d41fadf5d63151b58c15586a8` |
| ASSEMBLY55.md | `253ea55619c7fd09d278add27b840c989a2a35160eb22a0385ea700f01fac9c7` |

All thirteen dependency hashes in W_T0_LOG.md:100–112 match the inspected
files. References below are relative to this working folder unless stated
otherwise. They bind to these bytes, not to historical line-number guesses.

## Findings ranked by severity

**Critical/high/medium: none against the claimed WT0 result. Binding fixes:
none.** The following inherited evidence defects remain relevant to how the
result may be used; WT0 already avoids relying on them.

1. **Low — some inherited checks cannot detect the error suggested by their
   labels.** `checks/h2_55_a.py:110–119` contracts the sign-flipped tensor
   with Bianchi. The added term still has a symmetric pair of momenta
   contracted with an antisymmetric epsilon, so its contraction is zero
   identically. That control cannot fire. The recorded FAIL is correctly
   retained at `checks/h2_55_a_out.txt:13,35–36`; the separate Gram control
   at `checks/h2_55_a2.py:10–18` can detect the sign change. Also,
   `checks/h2_55_d.py:46–77` selects its threshold using `ge_pow` and then
   tests that same predicate. A shared error in that predicate can survive
   the threshold and predecessor checks. These are not independent
   certificates of the separation theorem.

   **Fix/disposition:** preserve the failed receipt and classify D2 as a
   search-implementation check. Use the tensor contraction and threshold
   proofs below as evidence. This agrees with the limitations at
   CODEX_REVIEW_HINT2.md:196–207; no WT0 edit is required. The relevant A6
   integration checks are discriminating arithmetic checks, but they do
   not test any YM moment, mixed OS, or sharp-time existence assumption.

2. **Low — upstream wording must not override WT0's narrower corrections.**
   HINT2_55.md:302 uses the wrong magnetic tree coefficient if its `g`
   retains FLOW's convention; :312 and :555–556 say that only sharp-time
   witnesses give reconstructed numbers. ASSEMBLY55.md:494–497 presents
   instanton-strength control as necessary. WT0 corrects these at
   W_T0.md:312–334 and :417–452, :760–764. In particular, failure of a
   proposed upper estimate cannot prove divergence of the actual mean or
   necessity of that particular large-field bound.

   **Fix/disposition:** when consolidating those sources, use
   `N(N²−1)g_FLOW²/(16π²)`, replace “only” by “one sufficient route,” and
   state LF-inst as a sufficient route conditional on transport and event
   bounds. Those corrections are already present in WT0. They are not
   new binding defects in the landed reduction.

## Independent reconstruction of the load-bearing argument

**Cutoff observable, normalization, and RP
(W_T0.md:24–65, :90–120).** Expanding an anti-Hermitian plaquette gives
`Re tr(1−exp(a²F)) = −a⁴ tr(F²)/2 + o(a⁴)`.
With `−tr(TᵃTᵇ)=δ_ab/2`, the density in (3) therefore tends formally to
`t² Σ_(i,j,a)(F_ijᵃ)²/4`. Matching the quadratic Wilson action gives
`u=2N/g_std²`, hence `g_std²=2N g_FLOW²`, consistent with FLOW.md:24–26.
This is a convention calculation, not an estimate on random continuum
fields. The flow's metric/time normalization is explicitly specified.

The finite link manifold is compact, so the smooth flow has no finite-time
escape. Its vector field uses only that slice and is gauge-equivariant.
There are three spatial plaquettes and each contributes at most `4N`
to the unscaled density, giving `12N τ²`. It is an upper bound, not a
claim of simultaneous attainability, and grows with the cutoff.

For site reflection, split the action into the two closed halves with
half the boundary action on each. At boundary links `u`, let `I_j(u)` be
the half partition function and `C_jF(u)` its normalized half expectation.
The boundary marginal has density proportional to `I_j(u)²`. Thus

    q_j(bF,cG) = E_boundary[conj(b C_jF) c C_jG].

This proves positivity and
`q_j(bF,bF) ≤ ||b||_∞² q_j(F,F)`, also for finite sums of such vectors.
For boundary-only functions the form is their ordinary boundary L²
pairing. This re-establishes the actual site-reflection mechanism, without
using an Osterwalder–Seiler verdict as proof. Strictly positive-time
e-test approximants have the required support eventually, as specified
in OSLEAF55.md:292–306. The argument is not a multiplier bound for a
general insertion at positive time.

**Limit passage and common boundary extension
(W_T0.md:124–214).** For nonnegative `X_j` with second moments at most C,
the contribution to the mean above M is at most `C/M`. Weak convergence
of bounded truncations therefore gives convergence of the means; applying
it to `min(X_j²,M)` and increasing M gives `E X²≤C`. The rare-spike
example in the note correctly rules out convergence of second moments.

Coordinatewise Markov bounds with summable error probabilities give a
compact product containing all but an arbitrarily small amount of mass.
Finite-dimensional extraction and consistency give the countable joint
law. It can be extracted on a subsequence of the original e-test sequence.
No probability law for coincident e-products is needed.

The multiplier bound above and Cauchy–Schwarz bound every mixed Gram
entry on the countable test/truncation family. A common diagonal limit
retains positivity; the assumed e-test continuity estimates extend the
form. Its restriction to e-tests is unchanged, so the null quotient gives
an isometric copy of the original e-Hilbert space. On boundary-only
vectors the form is L²(ν). Consequently the truncations of X are Cauchy,
their limiting vector has norm squared `∫X²dν`, and its vacuum pairing
is `∫X dν`. The squared norm need not equal `lim_j E X_j²`.

Crucially, this construction alone is not the positive-time reconstructed
magnetic field. W_T0.md:373–390 and :507–513 explicitly assume that
ALG-B/SHARP-B identify the same truncation law and boundary form with the
strong sharp-time limit. There is no hidden deduction of that assertion
from MOM2-B, and no silent identification with the e-cyclic subspace.

**Free comparator and its domain
(W_T0.md:220–334).** For a spatial momentum p, the curl covariance has
two transverse magnetic modes, each with eigenvalue
`|p|²/(2 sqrt(|p|²+s))`. Writing `H_i=ε_ijk F_jk/2`, the composite is
`t² Σ_i H_iᵀ M H_i/2` after spatial heat smoothing. Its expectation is

    t² ∫ρ_M(ds) ∫d³p/(2π)³
        |p|² exp(−2t|p|²)/(2 sqrt(|p|²+s)).

The radial measure and `v=sqrt(t)|p|` give exactly (13). At s=0,
`∫v³ exp(−2v²)dv=1/8`, so the coefficient is `1/(32π²)` per unit
observed spectral mass. For large σ the kernel is bounded above and
below by positive constants times `σ^(−1/2)`; on `[0,1]` it is bounded
and bounded away from zero. This proves the precise condition (14),
including the observed-color restriction when M has a kernel.

Pointwise decrease in `ts` proves monotonicity; monotone convergence as
t decreases proves the UV limit even for infinite total spectral mass.
Diagonalizing the finite Gaussian quadratic form gives
`B=Σ λ_i Z_i²`, with λ_i≥0 and independent standard Gaussians, whence
`E B²=(Σλ_i)²+2Σλ_i²≤3(E B)²`. Thus finite mean supplies the claimed
Gaussian vacuum vector. Positive mixtures with the stipulated moments
retain the ordering; the added constant-profile sectors do too.

This proof uses the spectral representation as the definition of the
marked comparator class. It does not derive it for every interacting
field or every abstract free realization. Euclidean contact terms are
not being restricted to sharp time and quietly discarded: the compared
observable is explicitly the canonical reconstructed one. A nonzero
positive polynomial contact cannot be integrated in frequency after only
spatial smoothing. A divergent unobserved color does not invalidate an
otherwise finite observed composite.

**Uniform separation and order of limits
(W_T0.md:40–84, :343–390, :458–559).** Put
`A=c_-/U_+(m_0)>0`. Since `U_-(m)→∞` and `ϑ−1<0`, choose one finite
`m_1>m_0` with `C_+U_-(m_1)^(ϑ−1)≤A/2`. This choice precedes the
cutoff and volume limits. For every admissible `K≥m_1+d_0` and R,

    y_0 := f_(K,R)^B(t_0) ≥ A,
    y_1 := f_(K,R)^B(t_1) ≤ A/2.

The lower inequality uses the upper coupling bracket; the upper inequality
uses the lower bracket and a negative exponent. The constants do not
depend on K or R. Joint mean convergence passes both inequalities to one
state. For the all-grid UV conclusion, first take the cutoff limit at each
fixed m, then let m grow. No bound uniform in m on the second moments and
no interchange with a moving cutoff-scale flow time is used.

Every allowed comparator has `z_0≤z_1`. Hence its positive-part witness
vanishes, while the YM witness is at least `A/2`. Moreover
`(y_0−z_0)−(y_1−z_1)≥A/2`, so at least one absolute coordinate difference
is at least `A/4`. These constants are correct uniformly over the entire
specified comparator class, without bounding its masses or normalization.
The witness is Lipschitz in the two mean coordinates. Moment continuity
along the controlled sequence, not weak convergence alone, is what is used.

Conversely, `ρ=(32π²y/(N²−1)) I δ_0` gives a Maxwell member with any
prescribed positive single-scale value y. This directly defeats the
author brief's universal single-scale gap and justifies WT0's explicit
replacement. It is not a relabelling of that false assertion.

For the sphere route the two errors on each of the first j coordinates
are each at most `1/j`, giving a diagonal error at most `2/j`. This is
valid after the fixed-R limits and common radius-uniform extension bounds
are supplied. It neither produces a sphere magnetic flow nor supplies
uniformity from bounds whose constants depend on R.

**Common algebra, support, and imports
(W_T0.md:565–745).** The e-domain has only the permitted separated
products. A time delta and a generic `e(f)²` are not elements of that
domain. The two constant Cartan-curvature configurations have identical
scalar curvature square but different magnetic square; this defeats an
algebraic identification on that smooth configuration domain, not a
state-specific closure theorem.

The heat kernel has tails at every spatial distance. Perturbing a distant
connection changes its smoothed curl, so the quadratic magnetic observable
cannot have fixed compact spatial support. A tilted full hyperplane also
crosses both time halves, regardless of its center time. Adjoining normal
labels gives the stated E(4) action on labels, not state invariance or a
unitary action of all Euclidean rotations on one OS Hilbert space.

Given the actual mixed maps, common seminorm bounds, symmetry identities,
support-compatible RP, and completion estimates stipulated in ALG-B,
diagonal extraction plus density passes the corresponding identities and
inequalities. Second moments alone do not supply that contract. The
common OS realization is an assumption of T0-OS, not a reconstructed
multi-field theorem smuggled in through OSLEAF's status labels.

The large-field arithmetic was also rebuilt: amplification `L^(4r)` and
the assumed event probability give a geometric ratio
`L^(4−c_LF β_-)`, with prefactor `exp(c_LF R_F)`. The specified L² triangle
method instead has ratio `L^(4−c_LF β_-/2)`. Thus the sufficient thresholds
are respectively `>4` and `>8`, under the separately assumed decomposition.
Neither event bounds nor decomposition follow from F-B. The convention
conversion of the supplied instanton action is `(4π²/N)u`. The numerical
one-loop slope and the remembered instanton-survival assertions are not
needed in the separation proof. WT0 expressly excludes their use at
:437–452. The source checks against SRCCD55.md:339–368 and
../ym4d-existence/EXISTENCE.md:235–247, :617–633, :1137–1155, :1205–1229 confirm that none
of those sources supplies the missing B moments or sharp-time theorem.

## Word-for-word consumers and actual fulfillment

All six consumer excerpts in W_T0.md:755–758 match the source words after
only whitespace, Markdown emphasis, and escaped table pipes are normalized.
The two additional status quotations at :760–762 match too. No words,
punctuation, or mathematical symbols were substituted in this comparison.

| Consumer source | Exact scope of the verified handoff |
|---|---|
| ASSEMBLY55.md:137–146 (N1F) | Closure works on one common domain and sequence, conditional on the mixed contract; the contract itself is not produced. |
| ASSEMBLY55.md:199–202 (N5) and PANEL_P1.md:63 | The two-scale finite-moment margin is supplied conditionally. Strict local support and identification of the named free class with OWN-free remain open. |
| ASSEMBLY55.md:390–400 (F1) | The enlarged marked boundary-system reduction is valid. The original e-only implication remains unproved, exactly as W_T0.md:756 says. |
| CODEX_REVIEW_P4.md:286–296 | Fixed physical scales and the conditional uniform margin are compatible with the required order of limits. Sphere approximants and radius-uniform mixed estimates remain assumptions. |

In particular, localization (32) for the YM state alone cannot give an
approximation uniform over all comparator normalizations. The warning at
W_T0.md:732–737 is necessary and correct. I found no consumer quotation
mismatch and no claim that this unresolved strict-local requirement has
been fulfilled.

## Explicit verification limits and recovery

**Re-derived in this review:**

- Plaquette/coupling normalization, finite cutoff support and boundedness.
- Site RP, bounded boundary multiplication, joint extraction, first-moment
  passage, and the boundary-vector norm.
- The Gaussian magnetic integral, exact integrability domain, monotonicity,
  UV limit, and fourth moment.
- Both separation constants, their quantifier order, and the single-scale
  Maxwell counterexample.
- The inter-scale L⁴ bound from action dissipation and conditional sphere
  diagonal.
- The algebraic and support obstructions and conditional OS closure steps.
- The two large-field geometric-series thresholds.
- By static inspection, why the bad Bianchi control is blind and why D2
  is not an independent proof.

**Not re-derived or certified:**

- Any YM F-tune, TS, MOM2-B, SHARP-B, or ALG-B estimate.
- A sphere magnetic construction, comparator-uniform localization, or
  generation of the enlarged theory by e.
- Unrestricted tensor Källén–Lehmann or OS-to-Wightman reconstruction,
  including OSLEAF's full REC/EXT/GROW package.
- The full upstream RG, source, Balaban, or Dimock analysis.
- HINT2's separate all-subtraction, nonlinear-flow/gauge-parameter, and
  wrapped-normal theorems.
- Historical provenance and resource use of the old check runs.

Relevant source statements and code were inspected, not promoted by
citation. The [KQR abstract](https://arxiv.org/abs/2104.02090v2) was opened
for provenance only; no theorem from it carries this verdict.

All of W_T0.md, its log, and the earlier WT0 review were read. The requested
HINT2/ASSEMBLY passages and necessary cited premises were read at bounded
offsets. The h2_55_a/a2/b/c/d criteria, implementations and result records
were inspected without execution; known truncated reads were supplemented
at the required offsets. No new numeric PASS totals are claimed.

Recovery checkpoint: the source identities above, the unchanged thirteen
log receipts, and the explicit unproved interfaces in W_T0.md:343–390 and
:647–745. Reopen the affected conclusions if those sources or the comparator
identification change. This review writes only REVIEW2_WT0.md; no source,
log, editable prompt, skill, ledger, or commit is changed.

VERDICT: CONFIRM
