# Independent hostile review of REALONLY

**Disposition: LAND for this conditional consumer-interface assessment.**
I found no material mathematical defect in the reviewed revision. Its real
replacement implications are supported; their actual Yang–Mills hypotheses
remain OPEN. This is neither approval of a completed real RG construction nor
an audit-grade, existence, non-freeness or mass-gap verdict.

This is a fresh-context, same-family Codex review, independent of authorship.
The controlling brief is `briefs_q/REALONLY/REVIEW.md`. Only this report is
written; no source fixes, commits, ledger changes or prompt edits are made.
The author's earlier output-path convention does not replace this review
brief's explicit `REVIEW_REALONLY.md` destination.

## Frozen scope and verification

All target line references below refer to the complete 592-line
`REALONLY.md`, SHA-256
`3856594faffe9b1c6beab42f38385c820f06ab7476c4cbdd6934b5bf30bac019`.
The worktree HEAD is `71ff1c12a33734f8ae305540916c117f7fceb664`.
The available `origin/main` is
`01589af3faf806b736c42dc2f3bd625e9edead9f`; refreshing main was denied at the
shared `FETCH_HEAD`. This verdict identifies the local source snapshot, not
an unverified newer remote revision. The repository reviewer procedure and
its relevant references match that available main snapshot; the installed
reviewer skill has wording drift and is not the source authority.

The two supplied manifests were checked against their files before review
and again after drafting this report; all 33 entries agreed. They cover 30
source files and three review inputs, including both author-side inspection
notes. The manifests themselves have SHA-256:

- `checks/realonly_sources.sha256`:
  `137b9b232cd489a72fdcb5081120506df526207f9378d37dea22ef7850fd0990`.
- `checks/realonly_review_input.sha256`:
  `76fe5fc0047a4342d7aa02533aac1bac9b2013611f7f580e806be311f637baee`.

I read the complete target, reconstructed its new mathematical implications,
and checked its cited consumer statements and decisive source arguments.
Author-side inspection notes were also read; their conclusions and previous
review labels were not substitutes for checking the sources. Hash agreement
establishes identity, not correctness. No numerical experiment or scientific
PASS counter was used. The checks below are written derivations and exact
examples. This does not freshly certify every unrelated lemma in the large
RG and reconstruction libraries.

## Verdicts per item

### 1. Real moment and cumulant bounds — CONFIRMED

**Target:** lines 56–91, R1–R3.

From the two signed exponential bounds,
`E exp(r|X_i|/p_i) <= 2M = A`. Expanding the nonnegative exponential
gives the asserted nth absolute moment. Hölder with n equal exponents gives
`E product |X_i| <= A n! r^-n product p_i`, with no independence assumption.
Repeating a variable proves the multiplicity version as well.

Independently counting the cumulant majorant, the unordered k-block sum of
`product |B|!` is `n! binom(n-1,k-1)/k!`. Multiplying by `(k-1)!` gives
the first R3 bound. Its remaining scalar sum is exactly

    sum_(k=1)^n A^k binom(n-1,k-1)/k = ((1+A)^n-1)/n
                                    <= A(1+A)^(n-1).

The finite nilpotent logarithm supplies the cumulant identity without an
analytic logarithm. Exponential domination justifies its interpretation as
real derivatives. The conditional-law caveat at lines 88–91 correctly
retains outer moments and the distinction between an expected supremum and
separate expectations. **Fix: none.**

### 2. Derived complex neighborhood and positivity diagnostic — CONFIRMED

**Target:** lines 93–113, R4.

For `a=sum |z_i|p_i/r`, the displayed weights sum to one. Weighted Hölder
therefore gives `E exp(Y)<=A`, and convexity on `[0,1]` gives
`E(exp(aY)-1)<=a(A-1)`. Since `|exp(w)-1|<=exp(|w|)-1`, R4 follows.
Interior exponential domination gives holomorphy. On the stated smaller
ball the denominator has modulus greater than 1/2 and the numerator of
its total variation is at most A, proving `TV<=2A`.

Here `A>=2`, so that smaller ball lies within the `a<1` domain used in the
proof. The zero direction and repeated real-base-tilt qualifications are
correct. The fair-sign example has zeros at `i*pi/(2B)` while its real MGF
is positive. It defeats positivity-only zero-freeness, not uniform R1.
The certified radius is an l1 radius, not a fixed many-source polydisc or
a coarse-field tube. **Fix: none.**

### 3. Raw clover MGF obstruction and contact scope — CONFIRMED as scoped

**Target:** lines 115–135.
**Sources:** `SRCCD55.md:215–282,926–927`;
`CODEX_REVIEW_SRCAN.md:23–38`.

The quoted lower bound preserves the source's model, even-torus and
weak-coupling restrictions. The corrected `O_f(a^2)` remainder is safely
absorbed in the target's `O_f(a)` notation. The underlying argument uses
conditionally independent sparse links, a circle-coset conditional variance,
and an event of probability at least 1/2; it does not assume positive
plaquette correlations. Its coefficient combines as
`c_v/(288 u_0^2) * 4/(16 a^4) = c_v/(1152 u_0^2 a^4)`.
For fixed nonzero real f on the stipulated logarithmic trajectory this
diverges.

R2 at n=2 would instead bound the variance of any deterministically centered
variable by `2A p(f)^2/r^2`. Uniform conditional R1 with the same centering
also bounds the unconditional second moment by averaging. These are actual
contradictions under matching premises. A bound only on good coarse fields,
a different normalization, or a counterterm-subtracted generating functional
does not satisfy those premises. The note preserves these distinctions and
does not transfer this obstruction to the sphere. **Fix: none.**

### 4. Real derivatives, finite differences and real tilted decay — CONFIRMED

**Target:** lines 137–215, especially R5 and R7.
**Sources:** `K4MATCH.md:103–187`;
`SRCAN55.md:129–154,440–459`;
`CODEX_REVIEW_SRCAN.md:40–54,225–249`.

Quotient differentiation gives `partial_i E_t G=Cov_t(G,X_i)` for
source-independent G. The conditional nilpotent expansion gives total
cumulance, including conditional singleton means. Applying the fundamental
theorem of calculus in every coordinate makes the normalized rectangular
finite difference the cube average of the mixed derivative. Its deviation
from the value at zero is at most `B sum_j E s_j=qBh/2`. The corner sum costs
`2^q epsilon`, or just epsilon when all proper coordinate faces vanish.
The choices of h and the B=0 and epsilon=0 cases are correct.

The Gaussian counterexample is a positive, normalized density. Real tilting
shifts `X_j/b` to mean `b t_j`, so the sine expectation is
`exp(-1/2) sin(b t_j)`. This reproduces R7 and its mixed derivative
`epsilon exp(-q/2)b^q`. With `b=epsilon^-1`, the real error vanishes while
the q=2 or q=4 derivative diverges. It is a valid counterexample to a bare
value-to-derivative inference, not to a bound with uniform higher derivatives.

For real CD, applying R5 to the cross-second derivative and `m=n-2`
remaining directions gives `H^(1/(n-1)) B_n^((n-2)/(n-1))`, up to constants,
and hence the stated fractional pair-distance decay. The note does not
infer the extra B_n, its order growth, or outer moments from CD. It also
keeps every RG kernel and normalizer fixed under original observable tilts.
**Fix: none.**

### 5. H_reg / OS0 / E0′ — REAL-SUFFICES, conditional; CONFIRMED

**Target:** line 37 and lines 218–292, R8–R9.
**Sources:** `REC_LIB.md:960–1054`;
`OSLEAF55.md:214–222,436–495,919–1004`;
`CODEX_REVIEW_OSLEAF.md:143–155`.

The load-bearing estimate is unconditional and all-order. It is not a
same-test MGF assertion. For `delta<1`, projecting a closest pair onto its
coincidence plane has l1 displacement at most `2delta`; along that segment
`1+|x|^2 <= 2(1+|z|^2)`. Taylor flatness gives exactly the displayed bound
with M derivatives and 5n weight powers. The weight is summable on the
four-dimensional lattice uniformly for `a<=1`.

On `c_*a<=delta<1`, the logarithmic weight is at most
`C_q^n delta^(-5n)`, canceled by M=5n. On `0<delta<c_*a`, M=4n+1 and the
crude bound leave `a^-4n delta^(4n+1)<=c_*^(4n+1)a`. Coincident points
vanish; large separation and the range `c_*a>1` have the stated direct
bounds. Thus `C^n(n!)^b0 |F|_(10n+1)` and the single all-n E0′ triple follow.
The general crude-power correction and the finite-component qualification
are appropriate.

For R9, ordered partitions give `sum_pi |pi|!<=2^(n-1)n!`.
The total-cumulance bound therefore has factorial exponent p+1. Moment
expansion over at most n! partitions adds one more. Block factorials and
capped subset weights are bounded by their full-configuration counterparts;
the centered unconditional singleton causes no extra term. This proves
`b0=p+2`, hence `beta=p+3`, under the explicit singleton-inclusive outer
hypothesis, not from higher conditional cumulants alone.

The alternative SP_lambda interface retains the scale factors, singleton
premise and the corrected interior-chart domain. I checked the tensor
localization margin and factorial bookkeeping: separation becomes lambda/4,
the Fourier sum costs `lambda^-4n (n!)^(5r/2+8)`, and composing EXT gives
the recorded `beta=b+19r/2+51`, with integer derivative-order majorants.
The source's unrestricted boundary-touching version is not silently reused.
The common hierarchy and remaining axioms stay as inputs. **Fix: none.**

### 6. PL-1L / WITNESS — REAL-SUFFICES, conditional; CONFIRMED

**Target:** line 38 and lines 179–181.
**Source:** `WITNESS.md:455–595`.

The actual target is the absolute summed second-cumulant error E11; E12
is a stronger summable producer. Total covariance retains every step and
the terminal covariance. With `X_r=u lambda^4 O_r`, the second derivative
of the real log error is `u^2(V-V_run)`. A direct jet error proves the
matching estimate; R5 with a uniform third derivative gives the weaker but
still positive relative exponent theta/3. Neither construction supplies
E12's per-scale envelope.

The source's free comparison, common sequence, actual running coupling and
unit-coefficient quantum normalization remain necessary. The note supplies
no lower YM estimate merely from positivity or moment upper bounds.
**Fix: none.**

### 7. K4MATCH — REAL-SUFFICES, conditional; CONFIRMED

**Target:** line 39 and lines 146–181, R6.
**Source:** `K4MATCH.md:149–187,292–302,308–400`.

There are fifteen nonempty subset jets. The fourth-order recursion has
partition multiplicities `1,4,3,6,1`; dropping triples or pair-pair terms
would change it. The note drops none. Pi4 kills proper-subset terms and
vanishes on coordinate faces. Its mixed derivative is precisely
`u^4(P-P_run)`, without 4!, as can also be checked on the monomial
`t_1 t_2 t_3 t_4`.

R5 at q=4 gives `O(u^(-theta/5))` for this derivative with the stated uniform
fifth-derivative input, hence R6. Direct fourth-jet matching retains theta.
These are sufficient real replacements for the complex error estimate;
they do not evaluate actual vertices, sign a perturbative correction,
establish PL-4JET, or override K4MATCH's separate brief-completion HOLD.
**Fix: none.**

### 8. Flat H_Euc / TQ2 — REAL-SUFFICES, conditional; CONFIRMED

**Target:** line 40 and lines 296–313.
**Source:** `TQ2.md:284–390,433–466`.

Finite positive real tilts make the pressure convex, with second derivative
equal to a variance density. The two secant inequalities bound differences
of expectations by the no-cusp width plus pressure-comparison errors divided
by t. Taking the common volume-first diagonal, then cutoff limit at fixed
t, then t decreasing to zero gives the stated conclusion. The moving-radius
version instead needs both quotients to vanish at the actual common radius.

NC is a cutoff-uniform thermodynamic condition; COMMON and PC are real
inputs, not consequences of convexity. Whole-product sources, all orders,
and source-dependent vacuum terms are retained. The Gaussian fourth-power
example correctly prevents deriving product-source admissibility from
ordinary polynomial moments. **Fix: none.**

### 9. Sphere H_Euc / N5B — REAL-SUFFICES, conditional; CONFIRMED

**Target:** line 41 and lines 315–324.
**Sources:** `N5B.md:153–214,475–526`; `REVIEW_N5B.md:28–75`.

Successive total covariance under the actual Markov law gives the displayed
telescoping identity. For the terminal term, subtract any scalar c from
the seam image, then apply Cauchy–Schwarz and the sup bound. After the
specified normalization this is `C(J)tau(a,J)`. Add the early absolute
covariance sum, choose J first, and then send a to zero.

No complex tilt is consumed. The note explicitly retains actual-law
dependence in E and D, every product/path and crossing datum, and BULK/ALG
for the radius/OS passage. It incorporates the cited review's binding
objection to calling the averaged hypotheses UV-only. **Fix: none.**

### 10. REC / OSLEAF — REAL-SUFFICES at the source interface; CONFIRMED

**Target:** line 42 and lines 326–333.
**Sources:** `OSLEAF55.md:214–255`; `REC_LIB.md:1080–1120`;
`REC_CONT.md:17–70,982–1018`.

The reconstruction antecedent is the same distribution hierarchy with
E0′–E3, reality and S0=1; its Hilbert/semigroup part uses the weaker stated
regularity. Complex coefficients enter the RP form by sesquilinearity.
There is no source partition function or inverse source denominator in
that antecedent. Supplying the real hierarchy with those properties
therefore supplies this interface.

Complex spacetime continuation is still a conclusion of the referenced
reconstruction, not abolished by this observation. The note does not claim
that E0 alone proves full continuation, enlarge the tensor/domain class, or
deduce a unique vacuum, contact extension or gap. This is verification of
the source-interface implication, not a new full audit of REC_CONT.
**Fix: none.**

### 11. Coupling extraction, brackets and tuning — REAL-SUFFICES, conditional; CONFIRMED

**Target:** line 43 and lines 335–354.
**Source:** `FLOW.md:155–171,285–308,409–470`.

Replacing the Cauchy output by the stated real Hessian bound leaves the
counting unchanged: at most 16 root cubes, `80^(2(n-1))` rooted animals,
`4M^4 n` second links and `(Mn)^2` for the coordinate product. Their product
is exactly the displayed `64M^6 H n^3` series, convergent for
`kappa_p>log 6400`. The derivative/sum interchange is explicitly retained;
identity-point derivative bounds alone would not justify it.

Gauge/color structure, extraction, relevant coefficients and the actual
infinite-volume convention are not supplied by that count. Given them,
the remainder estimate, telescoping flow bracket and first-exit tuning
argument use real derivatives, sums and continuity. FI-1 remains an open
producer constraint, with no future-flow circularity hidden in the
replacement. **Fix: none.**

### 12. Scalar flow response versus spatial response — CONFIRMED distinction

**Target:** line 44 and lines 356–368.
**Sources:** `SRCAN55.md:321–346`;
`CODEX_REVIEW_SRCAN.md:58–78,110–126,180–197`.

For the explicitly scalar differentiable recursion, the derivative is
`product_j(1-beta'_j)`. With `q_j=C/u_j^2<=q_*<1`, each factor lies in
`[1-q_j,1+q_j]`. Integrating the derivative of log(1-x) gives
`log(1-q_j)>=-q_j/(1-q_*)`; `log(1+q_j)<=q_j` gives the other side.
This reproduces both bounds in the note. The strict margin repairs the
earlier unjustified positive lower bound.

It is a variational bound along the stated trajectory, not automatically
a finite-perturbation window or an operator estimate for position-dependent
sources. The latter and inherited dependence remain explicitly OPEN, so
the note does not reassert the rejected reduction of LOC-e to scalar flow.
**Fix: none.**

### 13. Positive real normalized ratios — CONFIRMED at the stated reference

**Target:** lines 370–401.
**Sources:** `RD3.md:278–303,384–423`; `RD4.md:334–397`;
`CHARGE.md:153–193`.

Normalizing the same positive w gives a probability law and TV=1. The
triangle inequality and the pointwise `exp(-a)<=exp(G)<=exp(a)` prove the
two displayed comparisons. The identity-cap lower bound makes CHARGE's
actual all-cut denominator strictly positive for real V; real coefficient
tilts preserve positivity on that nonempty support.

Neither this argument nor compactness gives the missing local, derivative
or uniform inverse budgets. Conditioning a mandatory event yields L1 norm
one, not a second copy of its original probability price. The signed
two-point diagnostic gives exactly `1+(exp(a)-1)/d`. Moving-cut boundary
terms and differentiated normalizers are expressly retained. **Fix: none.**

### 14. Literal complex contract and rebuilt real cluster contract — CONFIRMED

**Target:** line 45 and lines 404–472.
**Sources:** `RD4.md:55–69,165–277,399–460`;
`LFPRICE.md:656–691`; `JMBRB.md:481–556`;
`RENEW.md:454–490`; `STEP55.md:471–508`.

The unchanged source explicitly quantifies nonreal original sources,
coarse fields and decoupling parameters. A real supremum cannot certify
that contract. COMPLEX-NEEDED is therefore correct only in the limited
sense defined at target lines 14–15.

For the proposed replacement, the finite-jet norm is submultiplicative:
Leibniz's binomial coefficient cancels the m! weight, and summing over
derivative orders is bounded by the product of the two norm sums. The
stronger hypothesis at lines 453–459 bounds the complete integrated
coefficients, including differentiated measures and selectors; pointwise
atom bounds are not substituted for it.

I reconstructed the two cluster stages. A selected atom set splits into
unique overlap components. The assumed exact factorization makes their
integrated coefficients a hard-core gas. For the first rooted sum,

    sum_(j:H_j intersects H_i) b_j <= Q |H_i|,
    v_i exp(Q |H_i|) <= b_i.

Iteration therefore bounds connected group weights at exponent mu+1 by
Q. For the logarithm, fixing the ordered Kruskal tree partitions connected
graphs into intervals; each alternating interval sum has modulus at most
one. Repeated polymer labels are allowed in this logarithmic expansion.
Marking a polymer containing the spatial root replaces 1/m! by
1/(m-1)!, and the second rooted bound spends the remaining support exponent.
The supported log norm is at most Q.

Multiplying each original atom by z retains both bounds for `|z|<2` since
`2Q<=1/2`. The connected formal identity near zero then agrees with the
finite gas throughout this disc. Real coefficients make the logarithmic
series real at z=1 and its exponential positive. This auxiliary parameter
does not assume a complex physical-source estimate. The empty-support
scalar remains outside Q with its separate nonzero/log obligation.

Finally the rooted size/type sum is the geometric series with ratio r_R,
and `|exp(-U)-1|<=exp(|U|)|U|` supplies the stated small-field contribution.
R10 is sufficient only with the joint bounds, full readers and rootwise
multiplicity already required by the contract. No actual weights or
factorization have been produced. **Fix: none.**

### 15. CHARGE, renewal and invariant norms — CONFIRMED at their stated scopes

**Target:** lines 474–516.
**Sources:** `CHARGE.md:98–265,488–545`;
`RENEW.md:149–291,398–452`;
`JMBRB.md:126–172,595–639`.

CHARGE's cap comparison has numerator exponent
`-c_delta u_0 n_0+8 kappa u_j n_(j+1)` and the denominator debit includes
the link-cap masses, `48u_j zeta^2 n_j`, and another
`8 kappa u_j n_(j+1)`. With `zeta=u_j^(-1/2)`, C10 and `u_j<=u_0`
bound their sum by half the original charge. This proves the quoted C11,
only for `j>=j_*` and the stated coupling/cut conditions. The filled-volume
identity `n_0=L^(4R)n_R` makes its correctly debited charge beat a fixed
exponential lineage bill. It does not localize C13's extensive denominator
cost or bound arbitrary insertions.

For the window estimate, split any ordered product into q consecutive
m-windows and a remainder of length s. Uniformity in the starting level
gives `B0 theta^q` without commutativity. Summing over q and s proves the
bound. A common summable lag envelope controls both birth lifetimes and
fixed-terminal accumulation by reindexing; a separate lifetime bound alone
does not do so.

The ideal real dilation has third derivative `L^(4-6)D^3F(L^-2 x)`,
giving exactly L^-2. Taylor's integral remainder gives the factor 1/6,
and vanishing jets through degree two make this seminorm a norm on the
stated subspace. For nonnegative norm-majorant constants, the final
invariant-ball arithmetic is also correct. Neither calculation supplies
the actual nonlinear RG operator.

The inherited positive-mass identity follows by integrating conditional
expectation. The RENEW witness uses an order-two SU(N) element, the odd-L
offset sum and a unique polar maximizer; its tube probability tends to one
at each fixed finite horizon as the couplings grow. It excludes a uniform
plain-forward smoothing margin on that input class, not weighted/extracted
RG bounds. The target preserves that scope. **Fix: none.**

### 16. Critical path, obstruction language and audit status — CONFIRMED

**Target:** lines 3–16 and 518–592.
**Sources:** `AUDIT.md:15–39,49–63,77–85,293–306` and the interfaces above.

The assessment leaves the joint full-return/finite-coupling-flow construction,
all-order source seed, common hierarchy, symmetry and absolute witness
estimates unclosed. No original LF-JMBR clause on D_* is promoted. The
real-only route changes a possible sufficient interface; its difficult
producer estimates may package several original obligations together.
The note does not establish that this alternative is quantitatively easier.

The negative statements have explicit witnesses or matching-premise
contradictions: the clover variance, Gaussian oscillatory error, complex
two-weight cancellation and persistent forward flux family. Failure of the
local C13 majorant is correctly distinguished from an impossibility theorem.
The N1–N8 discussion neither claims route exhaustion nor counts the remaining
obligations as independent walls. No GO/NO-GO or retained audit status is
manufactured. **Fix: none.**

## Binding fixes and source fidelity

**Binding fixes: none.** Actual-model OPEN inputs are not defects in a note
whose explicit deliverable is a classification of conditional replacement
interfaces. Any later claim of RG closure would require new evidence for
those inputs and a new review.

The numerical line locators in the consumer table point to the claimed
requirements in the frozen sources. The variance erratum, SRCAN's strict
scalar margin and local-response objections, N5B's actual-law correction,
and the reconstruction interior-support/singleton corrections were checked
and are preserved. No misquotation requiring repair was found.
The attribution-only descriptions of Dimock's
[Large fields](https://arxiv.org/abs/1212.5562) and
[Convergence](https://arxiv.org/abs/1304.0705) match the primary abstracts:
their examples concern three-dimensional scalar theory. They are not used
as four-dimensional Yang–Mills proof inputs.

For later integration, keep this report attached to the exact target hash.
`REALONLY_LOG.md` still describes a pending review at the author's proposed
`checks/realonly_review.md` path. That is pre-review bookkeeping, not an
additional scientific result; this review's explicit brief controls the
actual output path. I have left the log and all editable prompts unchanged.

VERDICT: LAND
