# Independent hostile review of K4CORR2

**HOLD: the requested uniform renormalized coefficient bound is missing.**
The formal expansion, the explicitly restricted diagram bounds, the finite
bare-regulator bound and the conditional positivity arguments pass at their
stated scopes. They do not supply the full Yang–Mills Cbar or instantiate its
positive coupling window. I found no mathematical defect in those partial
results. There is one minor equation-locator correction below.

This review executes `briefs_q/K4CORR2/REVIEW.md`, independently of authorship,
in a fresh context. It is **same-family Codex review**, not cross-family
review or an audit. The current REVIEW brief controls this review's output:
only `REVIEW_K4CORR2.md` is edited. No commits or audit-status changes are made.
Balaban and Dimock retain credit for constructive RG; no estimate of theirs
is an unstated premise here.

The reviewed 568-line manuscript has SHA-256
`f7af21719921a45f7ada8f82ab8a8f2bd1db5d37f86ba282d6b725a452323b25`.

All manuscript line numbers below refer to that version. The checker hash is
`e7ea27dd531baf36d6d08e1be125bd24be6625781ea7daa86a9642ce79f609c1`.

| Author item | Verdict and manuscript lines | Fix or completion requirement |
|---|---|---|
| 1. Write the normalized order-g² term with the separated tests | **PASS FORMAL; actual observable identification OPEN**, 25–118. The five connected families and the ratio coefficient are correct. K4CORR did not define a complete regulator to reproduce. | B1: complete the renormalized prescription and finite matching before treating the diagnostic as the requested Yang–Mills coefficient. |
| 2. Bound every class and give explicit uniform Cbar | **PARTIAL / HOLD**, 120–409. C_ext and C_star bound proper subsets; C_bare bounds only the bare model at fixed cutoffs. C_rem is not supplied. | B1: give an explicit bound for the complete matched renormalized combination, including the omitted complement and regulator removal. |
| 3a. Give the non-cancellation window and rate | **PASS CONDITIONAL; requested uniform window OPEN**, 302–325, 419–461. The bare window and the formula 1/(2 Cbar) are valid at their respective scopes. | B1 must supply the finite uniform Cbar needed to instantiate the requested window. Correct the minor locator at line 14 to equations (21)–(24). |
| 3b. Name the higher-order and nonperturbative estimate needed for actual YM | **PASS as a sufficient input formulation**, 463–529. K4RATIO-REM, Q-LOW, the trajectory bounds and moment convergence imply the stated positive witness. | No additional proof of these downstream inputs is required merely to satisfy this naming request. They must remain OPEN until produced. |
| Exact arithmetic and evidence | **PASS within algebraic scope**, 531–568 and the check artifacts. The 97 author assertions reproduce; 79 independent assertions pass. | Preserve the separation between algebra checks and the missing interacting estimate. No audit grade follows. |

## Re-derived mathematical findings

**R1 — Observable, free normalization and regulator: PASS at the stated
scope.** Locations: 25–70, equations (1)–(3).

The temporal coordinate alone gives support separation at least
`1−2/10000>1/2`. Expansion of a trace-normalized plaquette gives
`s(U_p)=a⁴ mathcal F_mu,nu²/(4N)+o(a⁴)`. The four clover copies in each
ordered plane then give `e=mathcal F²/(4N)`. Matching the action
`u e/2=mathcal F²/(4g_std²)` yields `g_std²=2N h²`; after the canonical
field rescaling, `e=h²(f+sqrt(2N)h C)²/2`. These factors agree with CUMUL
173–192, K4CORR 52–64 and FLOW 573–587.

Differentiating `D(z)=1/(4pi²|z|²)` gives the curvature kernel
`G(z)=Lambda²(I−2zz^T/|z|²)/(pi²|z|⁴)`. The exterior square is orthogonal,
so `||G(z)||=1/(pi²|z|⁴)` and `tr(G(z)G(−z))=6/(pi⁴|z|⁸)`.
The quadratic cumulants have two pairings at n=2, and three undirected
four-cycles with 16 leg assignments per cycle at n=4. This reproduces
CUMUL (C10)–(C11), including their d and coupling powers.

For the smooth tests, I checked CUMUL's whole-support proof, not just its
centre value. The displacement error is at most 1/2500; the rescaled edge
operator error is less than 1/250, and the four-edge error is less than
`(251/250)⁴−1<1/60`. The centre coefficient is `169/108`, hence
`9971/6480<A<10309/6480`; also
`12(2500/2501)⁸<=B0<=12(2500/2499)⁸`. These imply the manuscript's
free intervals and `R0>3/(338d)` without any bump quadrature.

LGF 60–72 gives the heat integral used in (3), with lower limit rescaled
from 1 to delta². Its Fourier kernel is `exp(−delta²|p|²)/|p|²`;
the singularity at zero is integrable in four dimensions. The bounded
interaction region and smooth heat cutoff make all stated bare coefficient
integrals finite. K4CORR 304–309 explicitly leaves the regulator, IR/zero-mode
prescription, subtractions and matching unspecified; REVIEW_K4CORR 176–206
and 295–304 confirm this. The manuscript reports that limitation correctly.

Fix: none to the diagnostic or free claims. B1 is required for the
renormalized Yang–Mills identification.

**R2 — Expansion, connected normalization and ratio: PASS FORMAL.**
Locations: 74–118, equations (4)–(6).

The action expansion gives cubic and quartic coefficients s/2 and s²/4;
the insertion expansion gives s and s²/2. Integration by parts in
`bar c(−partial.D)c` gives the written ghost vertex with its stated
covariant-derivative convention. Ghost contractions retain Grassmann signs.

Write the normalized source generator as
`log <exp(sum t_i X_i0 + h A_t + h² B_t)>0` minus its value at t=0.
Its h² coefficient is `<B_t>_t+kappa_t(A_t,A_t)/2`. Distinct-source
differentiation gives F1 through F5 with signs `+,+,−,−,+`.
The two orderings cancel the half for distinct X1 insertions and for
the X1/V1 cross term. The repeated bulk V1 contribution retains its half.
This argument applies to the even ghost vertices as well. Deterministic
centering adds only source-linear terms and cannot delete a quadratic
tadpole remainder.

Expansion of `(A4+x D4)/(A2+x D2)²` yields exactly
`R/R0=1+x(D4/A4−2D2/A2)+...`. The full reversal symmetry is explicitly
assumed before writing an even-power formal remainder; no analytic error
estimate follows from it. A common multiplicative source factor cancels
as F⁴/F⁴. Under K4CORR's conditional RG equation, the order-h² logarithms
are `L4=8b0` and `L2=4b0`, so they cancel as well. Neither cancellation
evaluates the finite graph combination or nonmultiplicative matching.

Fix: none to the formal identity. Keep its symbolic counterterms and
matched-limit premise separate from an evaluated coefficient; see B1.

**R3 — Component ledger and pairing counts: PASS.** Locations: 122–174.

The generator normalization gives `||T^a||_HS=1/sqrt(2)`.
The commutator bound is `||[T^a,T^b]||_HS<=1`, hence
`|−2i tr([T^a,T^b]T^c)|<=sqrt(2)<=2`. Counting the ordered Lorentz
indices, the two terms in each f, and the independent color indices gives
`L0=32d`, `L1=128Nd³`, `L2=64Nd⁵`, `T1=(64+16)Nd³`, `T2=32Nd⁵`.
Using s<=2N and s²=2N makes these valid upper bounds, not diagram values.

Each Wick pairing decomposes uniquely into connected vertex components;
the cumulant partition sum removes precisely the disconnected ones.
Inclusion-exclusion for chosen self-pairs gives the quoted no-self formula.
Even ghost monomials factor over disconnected components, and their allowed
contractions are a signed subset of the unsigned bosonic majorant.

Independently of the author's pairing and partition routines, I enumerated
integer multigraphs with off-diagonal multiplicities m_ij and l_i loops,
subject to `2l_i+sum_(j!=i)m_ij=ell_i`. A connected graph carries

    weight = prod_i ell_i! / [prod_(i<j) m_ij! prod_i (2^l_i l_i!)].

Assigning labelled half-edges to these edges proves this integer weight.
Summing it over connected graphs, with and without loops, gives:

| Family | n=2: all / no-self | n=4: all / no-self |
|---|---:|---:|
| F1 | 12 / 0 | 576 / 288 |
| F2 | 15 / 6 | 720 / 360 |
| F3 | 90 / 36 | 7200 / 4176 |
| F4 | 72 / 24 | 5760 / 3456 |
| F5 | 720 / 360 | 86400 / 55296 |

All 20 comparisons agree. The F4 star condition m_i,bulk=1 gives 1152,
also directly `4!·2⁴·3`. Fix: none. These remain majorants, not evaluated
gauge/ghost amplitudes.

**R4 — Finite external and star subfamilies: PASS.** Locations: 178–248,
equations (8)–(12).

For m=0,1,2, the derivative bound
`2^m(m+1)! r^(−2−m)` is at most 4,32,384 respectively when r>=1/2.
Thus H=512 bounds each primitive external contraction. The no-self F1/F2
counts give precisely B4 and B2 in (9). For example, their two B4 monomials
have coefficients `9·2^73` and `135·2^73`, multiplying Nd⁸ and N²d⁸.
Dividing by the positive free lower bounds using pi<4 gives (10).

For the star, each bulk-external edge has one derivative, bounded by
`4|y−x_i|^-3`. On the cell nearest x_i, another distance is at least
sigma/2: otherwise the triangle inequality and nearest-point property
contradict separation. The r<=1 integral is bounded by `32·4⁹`; for r>1
all four distances are at least r, giving `2pi²/8<4`.
Consequently the four-cell total is less than
`4(32·4⁹+4)<2^26`. Multiplication by `1152 T2 L0⁴·4⁴ H²` yields
`9·2^84 Nd⁹`; free normalization gives `C_star=3·2^101 Nd⁸`.
This estimate covers infinite volume for this subset.

Fix: none to these bounds. The omitted self-pairs and internal families
cannot be assigned these constants. C_safe is not Cbar; B1 remains open.

**R5 — Complete bare majorant and its own denominators: PASS at fixed
regulators.** Locations: 250–325, equations (13)–(17).

Direct heat differentiation gives LGF (21). Integrating its bound from
delta² to infinity costs at most `16 delta^(−2−m)`, for m<=2.
An edge contributes two inverse powers of delta and every derivative one.
The five total UV powers are therefore `(4n,4n,4n+4,4n+4,4n+8)`.
Multiplying the connected counts by `(n,binom(n,2),n,1,1/2)` gives
`(24,15,180,72,360)` for n=2 and
`(2304,4320,28800,5760,43200)` for n=4. These reproduce every multiplier
in (13); source volumes cost one and each bulk vertex costs V. This
majorant includes both cubic species and self-pairs, but excludes ct.

For the free-denominator comparison, setting q=r²/8 gives the scalar
second-derivative error

    16 integral_0^(delta²) t^-3 exp(−q/t) dt
      =16q^-2(1+q/delta²) exp(−q/delta²)
      <=768q^-5 delta^6 <2^35 delta^6.

The factor 24 for four scalar terms and six matrix rows is below the
chosen operator-error constant `2^40`. On the separated supports,
`||G||<=16`, while `E<=2^-80<1` for delta<=2^-20.
The four-cycle error is bounded by `3·16d·6·4E·17³<2^23 dE`;
the two-cycle error by `12dE(32+E)<2^9 dE`. Thus (14) follows with
the claimed half-free margins. It is essential that the denominator is
A2_delta and the leading numerator is A4_delta here.

The inverse lower bounds give `2^18/(3d)` and `2^10/(11d)` in (15).
Then `|c_bare|x<1/2` proves (17) for the truncated ratio polynomial.
The text correctly distinguishes that polynomial from the quotient of
separately truncated series and from any full measure.

Fix: none at finite-regulator scope. Because all M4 monomials are positive
and have delta exponents at least 16, halving delta multiplies its bound
by at least 2^16; the nonzero V² delta^-24 term also destroys uniformity.
This proves failure of this bound, not divergence of the renormalized
coefficient. It cannot discharge B1.

**R6 — Collision diagnostics and subtraction lemma: PASS locally;
complete renormalized enclosure OPEN.** Locations: 329–415, (18)–(20).

The heat integral at zero is `1/(16pi² delta²)`. In the stated SU(2)
quartic monomial, contracting one squared factor leaves that constant
times a quadratic field; scalar centering does not remove it.
Also `partial_mu D=−z_mu/(2pi²r⁴)`, so
`sum_mu |partial_mu D|²=1/(4pi⁴r⁶)`. Polar integration gives exactly
`(epsilon^-2−rho^-2)/(4pi²)` in (18). A two-vertex ghost loop can remain
connected to every external insertion through its two gauge legs. Thus
external separation does not eliminate this bulk collision. The note
does not infer an uncancelled divergence of the renormalized tensor sum.

For the subtraction lemma, apply one-dimensional Taylor's integral
remainder to `t -> phi(tz)`. The multinomial sum is bounded by
`|z|_1^(k+1) M_(k+1)<=(2|z|)^(k+1) M_(k+1)`.
Division by `(k+1)!` and radial integration against `|z|^(-4-k)` leave
`2pi² rho`, bounded by `32rho`. This proves the constants 64,64,128/3.
The stated derivative norm is needed; overlapping collisions can make
that norm singular. No compatible forest, finite local terms, matched
counterterms or complete IR bound is supplied for (5).

Fix: B1. Equation (20) only defines the missing complement. Nothing in
the supplied bounds restricts its size; an explicit finite C_rem must be
produced or the whole renormalized combination bounded another way.
This is an unfinished route, not a no-go theorem. The BPHZ references
are method attribution, not substitute estimates.

**R7 — Conditional window and FLOW rate: PASS CONDITIONAL.** Locations:
419–461, (21)–(24); minor locator at line 14.

With a fixed finite |c|<=Cbar, `x<1/(2Cbar)` gives
`R^[1]>R0/2>3/(676d)`. FLOW F-ll, 425–429, gives the displayed E_m
after setting the terminal u to U and adding U to the error envelope.
For `|u−v|<=E<=v/2`,

    |1/u−1/v| <= E/[v(v−E)] <= 2E/v²,    1/u<=2/v.

This is uniform on the full stated domain, not a finite sample check.
Since E_m=O(log m) and `v_m=B log(1/lambda_m)`, the isolated correction
has exactly (23)'s log-log error rate. The common-scale independence of c
and all FLOW hypotheses remain explicit inputs. FLOW 4824–4851 confirms
the remaining open UNIV requirements.

The sufficient condition v_m>4Cbar is implied by
`m>768 Cbar/(11N²)`, using pi²<16 and log L>1 for odd L>=3.
It does not replace E_m<=v_m/2 or establish actual trajectory constants.
Fix: B1 before instantiation. Separately, change the summary's equation
range at line 14 from (22)–(24) to **(21)–(24)**, since (21) contains
the uniform coupling window. This locator issue is nonbinding scientifically.

**R8 — Original-law remainder and fixed-scale positivity: PASS as a
sufficient conditional statement.** Locations: 463–529, (25)–(29).

For 0<x<=1/2, `x²(1+log(1/x))<=x²+x<=3x/2` and
`exp(−S/x)<=2x²/S²<=x/S²`. Therefore the remainder is at most
`Tx+eta`, with `T=3H/2+J/S²`. Equation (27) makes this at most 1/4
and |c|x strictly less than 1/2, so `R/R0>1/4`.
Independently Q-LOW gives `Q>=A2 x²/2>0`, whence
`P=RQ²>A4 x⁴/16`. This proves the factor 1/16 and the ratio bound
`3/(1352d)` in (28).

At one fixed m_star, the same trajectory's upper bound on u yields
(29). A common convergent set of the centred fourth moment and all six
covariances passes the polynomial lower bound to the limit, with a
non-strict inequality and a strictly positive constant. A ratio alone
would not suffice if its denominator vanished. CUMUL 392–425 and 526–556
state the needed common-sequence and coupling conditions.

K4MATCH (5), 107–140, has exactly `1+4+3+6=14` increment terms; its
source recursion at 159–174 also requires terminal integration. The
manuscript retains those terms and the original-law matching, background,
large-field and exterior obligations. K4MATCH (24), 507–525, is indeed
an alternative sufficient estimate. The constants H,J,S,x0 are not
produced, and the exponential term is a proposed sufficient bound, not
an imported instanton result.

Fix: none to this input formulation. Before claiming actual-YM positivity,
prove these named estimates or a sufficient alternative. A fixed 1/2 bound
in Q-LOW is enough for the positive witness; it does not by itself prove
the sharper relative two-point asymptotic CUMUL (C19). The present result
does not discharge that asymptotic. The exclusion of Gaussianity is only
for the field e; a free underlying theory with composite e remains possible.

## Source and evidence checks

All ten source digests in `checks/k4corr2_sources.json`, all artifact digests
listed in `checks/k4corr2_verification.json`, and the three checker-source
digests in the recorded run receipt match the files read in this review.
Available timestamps put the criteria at 05:27:33 UTC, before the checker
and original result at 05:30:42 UTC on 2026-10-30. This is consistency of
the supplied evidence, not a claim to reconstruct unavailable git history.
The saved stderr is empty, and the result separately reports the scientific
target as OPEN / NOT PASSED.

The material local locators were checked directly: CUMUL (C1)–(C2) and
(C14)–(C16), LGF (6), (21), (25), (41), K4CORR §§3–5, REVIEW_K4CORR R6/B1,
FLOW F-ll/F-tune/§15/§110, and K4MATCH (5)/(24). Their scopes match their
uses, apart from the small equation-range issue in R7. In particular, LGF
(41) is a free-curvature comparison, not an interaction estimate.

The two linked primary-source abstracts identify Steffen Pottel's
[A BPHZ Theorem in Configuration Space](https://arxiv.org/abs/1706.06762)
and [Normal Products and Zimmermann Identities in Configuration Space BPHZ
Renormalization](https://arxiv.org/abs/1708.04115), as credited at 411–415.
Their abstract descriptions concern configuration-space subtraction and
normal products. No theorem or numerical enclosure from either is used to
close the manuscript's missing estimate; the local Taylor bound was rebuilt
above. No memory-only statement carries weight.

The prior `checks/k4corr2_review.md` ends HOLD and its final-version note
binds the same 568-line manuscript hash. Thus the summary at 561–568 is
accurate. This review's conclusions rest on the derivations and executions
reported here, not on that earlier review's approval. No GO, NO-GO,
retained-grade claim or audit status is established. HOLD records incomplete
scientific work, not an obstruction to a better renormalized calculation.

## Verification criteria recorded before execution

1. Replay `checks/k4corr2_exact.py` without writing outputs or bytecode.
   All 97 registered assertions, graph records and scientific-completion
   fields must match the saved run, excluding resource telemetry.
2. Independently enumerate degree-constrained multigraphs and weight each by
   `prod_i ell_i! / (prod_(i<j) m_ij! prod_i 2^l_i l_i!)`.
   Connectivity and exclusion of loops must reproduce all 20 counts in
   manuscript lines 162–168; the four-support star count must be 1152.
   This calculation must not import the author's pairing or partition code.
3. Independently check the rational whole-support free bounds, all bare-family
   multiplicities and UV powers, the conversion to the displayed constants,
   the heat-error endpoint margins, and the stated positivity margins. Accept
   only exact integer/Fraction comparisons. Written analytic derivations,
   including uniformity in the stated domains, remain necessary.
4. Keep scientific acceptance separate: the calculation does not pass the
   requested uniform Yang–Mills bound unless the full matched renormalized
   complement has an explicit cutoff-independent enclosure.

Use one serial numerical child, nice at least 10, all five BLAS/thread settings
equal to one, five existing numerical locks opened read-only and held
exclusively, native free memory at least 30%, all load averages below 8, and
monitored combined RSS below 800 MiB. Use no RLIMIT_AS, pools or output files.
Any failed execution must be reported here.

**Execution result.** At 2026-10-30T05:51:55Z, the unchanged author checker
passed all 97 assertions. Its complete assertion records, graph records and
scientific-completion fields exactly matched the saved run. A separately
written child calculation, importing none of the author implementation,
passed 79 assertions: all 20 graph-count comparisons, the star count,
bare multipliers and UV powers, free-support intervals, majorant constants,
heat-error margins, Taylor factors and positivity constants. These checks
support the printed proofs; they evaluate no renormalized YM integral.

There were two sequential numerical child executions, never a pool or
concurrent numerical workers. Both had exit code zero and empty stderr.
The effective nice level was 20; all five thread settings were one. All
five existing locks were opened read-only and held exclusively. Native
free memory was 53%, every load average was at most 2.09765625, and the
maximum monitored combined RSS bound was 36,208,640 bytes. Pre/during/post
resource gates passed. No RLIMIT_AS or numerical output-file write was
used. No reviewer numerical run failed. Resource decimals are telemetry;
all scientific arithmetic used integers and Fractions.

## Binding fixes and disposition

**B1 — Supply the actual uniform coefficient enclosure and instantiate its
window.** At 66–89, 273–275 and 389–409, complete an explicit renormalized
prescription and its finite matching to the unflowed clover observable in
FLOW units. Bound the full `D4/A4−2D2/A2`, or bound both matched coefficients
sufficiently, including tadpoles, bulk/bulk and insertion collisions,
compatible overlapping subtractions, finite local terms, the ghost/gauge
identities and the IR limit. Exhibit a finite rational/interval-certified
Cbar independent of removed cutoffs and the common short scale. Supplying
such a C_rem in (20) would suffice. Then give the resulting positive
uniform order-h² threshold, rather than the vanishing bare threshold.

This is a substantive missing calculation. Relabeling C_safe, setting
unspecified finite counterterms to zero, or extrapolating C_bare cannot
repair it. The completion failure affects author items 2 and 3a, and the
claimed use of item 1 as an actual matched Yang–Mills coefficient.

**Downstream obligation, not an extra completion demand in this brief:**
before promoting the conditional witness to actual-YM positivity, produce
K4RATIO-REM and Q-LOW, or adequate alternatives, together with their common
trajectory and moment limit. The brief asks to name this remainder input,
and that portion is satisfied. Do not turn its deliberately OPEN status
into a claim that the present sufficient formulation is incorrect.

The line-14 locator correction is nonbinding and does not affect B1.
Preserve the present partial results and OPEN labels. They are useful
bounded results, but the requested uniform Cbar and instantiated Yang–Mills
coupling window have not been obtained.

Final file-integrity check: all 3,742 pre-existing files in the working
folder are unchanged. The sorted path/content SHA-256 aggregate, excluding
this review, remains
`86f9d739cbd55361fa8380dba6e64832aeb76afe2661ddfde7731d560da70cba`.
The manuscript hash still matches the reviewed version, and the checked
local Markdown links resolve. Only this review was created; no commits were
made.

VERDICT: HOLD
