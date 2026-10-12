# Independent referee report — C5 R6-3

## VERDICT: CONFIRMED WITH CORRECTIONS

The fixed readings survive: the cocompact $L_7$ Lorentz-random lattice has
**SUB-VOLUME** ensemble count variance for the stated sharp diamonds and
flat-truncated cones, and literal item (d) is **REFUTED** because its open
condition $0<|q^2|<c$ does not remove null spectral weight.  The corrected
two-sided-gap lemma is valid after filling two technical steps.  Corrections
are required to the advertised numerical exactness, the proof constant, one
past-cone quadrature, the spacelike-cone sketch, the numerical coefficient of
the counterexample, the superposition claim, and the cosmological/epoch scope.

Independent checks are in `referee_checks.py` and `referee_checks.out`.  The
fixed labels are those at `TESTS.md:3130-3135` and were not altered.

## 1. Variance formula, unfolding, shell densities, and dual class number

**Confirmed, with the missing normalization argument made explicit.**  Torus
Parseval gives

\[
  \operatorname{Var}_u N(W)=\rho^2\sum_{G\in L_7^*\setminus\{0\}}
  |\widehat{1_W}(gG)|^2,
\]

and the scaling in `R6-3_report.md:148-161` is correct.  On a timelike shell
the real stabilizer is compact $SO(3)$, so its arithmetic stabilizer is
finite.  On a spacelike shell the stabilizer is $SO^+(1,2)$; its arithmetic
intersection is not finite but is a finite-covolume lattice.  Unfolding each
of the finitely many arithmetic orbits therefore contributes its stabilizer
covolume, and summing those weights is precisely the Siegel weight/local-density
formula.  This is the content needed behind `R6-3_report.md:150-153`, not an
assumption that every stabilizer is finite.  The normalization agrees with the
[Eskin--Rudnick--Sarnak weight formula](https://www.math.tau.ac.il/~rudnick/papers/siegelmass.pdf).

The class-number step is also valid, although “hence so does its dual” is too
compressed.  The original integral form $A=\langle-7,1,1,1\rangle$ has
square-free determinant $-7$, hence one class in its genus.  The operation
$A\mapsto 7A^{-1}=\langle-1,7,7,7\rangle$ respects integral equivalence and
local equivalence and is involutive on these genera.  It therefore bijects the
original genus classes with the scaled-dual genus classes.  This supplies the
missing justification at `R6-3_report.md:153`.

The density normalization and good-prime factors in
`scripts/r63_siegel_dual.py:1-56` reproduce.  Exact independent enumeration
modulo $p=3,5,11,13$ gives
$\alpha_p(1)=1-\chi_{-7}(p)/p^2$ to machine equality
(`referee_checks.out:7-11`).  The worker's exact bad-prime congruence counts and
large-box shell counts then support the displayed $C_t^*$ values
(`scripts/r63_siegel_dual.out:1-22`).  The resulting shell identity is exact
modulo the recalled Siegel theorem; decimal coefficients obtained after
truncating that identity are not exact.

## 2. Diamond transform and Theorem D

**The theorem and the $16\pi^3$ leading coefficient are confirmed; the
claimed numerical proof constant is not.**  Direct Gauss--Legendre evaluation
of the defining four-dimensional window integral agrees with the closed
diamond transform at $10^{-14}$ relative accuracy
(`referee_checks.py:19-49`; `referee_checks.out:1-3`).  The three bounds in
`R6-3_report.md:190-203` give the right split:

- bounded rapidity contributes $O(M^{-2})$;
- $1\lesssim\eta\lesssim\tfrac12\log |M|$ contributes a bounded amount per
  unit rapidity and hence the logarithm;
- the near-null tail contributes $O(M^{-2})$.

Thus $J_D(M)=O((1+\log|M|)/M^2)$.  In the intermediate range,
$\delta=k-\omega=\pm\sqrt{|M|}e^{-\eta}$ and the waist endpoint gives
$F\sim-\sin(k/2)/(4\delta)$.  Phase averaging therefore gives shell
integrand $32\pi^3/M^2$ per unit $\eta$ over a range of length
$\tfrac12\log|M|$, yielding

\[
  J_D(M)=\frac{16\pi^3\log|M|}{M^2}+O(M^{-2})
\]

for either sign.  This independently explains the fits at
`scripts/r63_Jtable.out:33-34`.  The wording at `R6-3_report.md:208` should use
an $O(M^{-2})$ remainder: the fitted $B$ is not an exact two-term identity.

The specific statement $K\le1.7\times10^4$ at
`R6-3_report.md:186` is unsupported by its cited calculation.  A dense scan of
the *same proved pointwise envelope* used in `scripts/r63_misc.py:20-31` reaches
$2.0004\times10^4$ near spacelike $M=165$, and $1.9628\times10^4$ at
$M=200$ (`referee_checks.out:12-14`).  This does not hurt the theorem: take a
larger explicit analytic constant.  For $0<|M|<64$, the closed transform and
the same regional bounds make $J_D$ finite on the compact interval.  The
table's $J_D<2.4$ is a numerical check, not the proof of compact-interval
finiteness (`R6-3_report.md:398`).

It follows that

\[
 \operatorname{Var}N(D_T)=O(T^2\log T).
\]

The leading coefficient is exactly the convergent series
$32\pi^3\rho^2\sum_{t\ne0}C_t^*/(ct)^2$; $0.1665$ is its numerical
evaluation, not an exact decimal (`scripts/r63_variance.py:38-58`).

## 3. Past-cone bound and rare-frame dominance

**The $O(T^3)$ result is correct after repairing the sketch.**  The closed
cone transform agrees with direct integration at ordinary momenta
(`referee_checks.out:4-5`).  At spacelike $\omega=0$, however, the base term
cannot be bounded separately: its $1/\omega$ singularity cancels against the
cone term.  The sentence at `R6-3_report.md:230` must apply to the combined
transform.  Write

\[
 h_\omega(r)=\frac{r(e^{-i\omega r}-e^{-i\omega})}{\omega},\qquad
 \widehat P(\omega,k)=\frac{4\pi}{ik}\int_0^1h_\omega(r)\sin(kr)\,dr.
\]

Here $h(0)=h(1)=0$, $h'(1)=-ie^{-i\omega}$, and
$h''=(-2i-\omega r)e^{-i\omega r}$.  If $|\omega|\le k/2$, two integrations
by parts followed by nonstationary bounds at $k\pm\omega$ give
$|\widehat P|\le Ck^{-3}$.  Outside that region, the same
$k\pm\omega$ split as for the diamond gives
$O((1+\log m)m^{-2})$.  On a timelike shell the flat-base contribution obeys

\[
 \int_{\mathbb R^3}\frac{|\widehat B_1(k)|^2}{(m+k^2)^{3/2}}\,d^3k
 \le m^{-3/2}(2\pi)^3|B_1|,
\]

and the remainder is $O((1+\log m)m^{-2})$.  Hence
$J_P(\pm m)=O(m^{-3/2})$, which, together with the shell-weight bound in item
5, proves $\operatorname{Var}N(P_T)=O(T^3)$.

Two numerical corrections are material:

- `scripts/r63_formfactor.py:83-105` switches the whole shell integral to a
  phase average when $\sqrt{|M|}>2\,\texttt{ompeak}$, thereby losing the narrow
  timelike rest-point peak.  The supplied table itself drops from
  $|M|^{3/2}J_P=1040.07$ at $3.16\times10^8$ to $59.05$ at $10^9$, rather
  than tending to $1039.03$ (`scripts/r63_Jtable.out:60-66`;
  `referee_checks.out:15-16`).
- The same closed-form implementation is cancellation-unstable near the
  origin: it returns $1.19469$ instead of the cone volume $\pi/3=1.04720$
  (`scripts/r63_formfactor.out:4-5`; `referee_checks.out:6`).

`scripts/r63_variance.py:27-45` avoids the first defect by inserting the
asymptotic formula above $10^8$.  Therefore the values at cosmological $T$
are asymptotic extrapolations, not independent direct checks.  Likewise,
$0.4847$ is not an exact computed decimal: the exact leading coefficient is
the convergent negative-shell series; the program evaluates only
$|t|\le4000$ (giving $0.48137$) and replaces the tail by its mean density
(`scripts/r63_variance.out:29-40`; `scripts/r63_variance.py:39-45`).

The rare-frame mechanism is nevertheless correct.  The timelike leading term
comes from fixed spatial $k=O(1)$ while shell mass is $m\asymp T^2$, i.e.
rapidity $O(T^{-1})$.  Such a three-dimensional neighborhood has Haar
probability $O(T^{-3})$, and its large conditional variance supplies the
ensemble $T^3$ mean.  The heavy tails and aligned split show this mechanism
(`R6-3_report.md:272-287`; `scripts/r63_cone_trim.out:1-18`).  They do **not**
prove the suggested typical-frame $T^2\log T$ law: every fixed-$K$ trim in
that output leaves a positive $T^3$ coefficient, and one must take $K\to
\infty$ after the asymptotic limit.  Applying a typical-frame conjecture to
our cosmic realization is therefore open.

## 4. Null-lattice counterexample and Heath--Brown

**The counterexample is valid; $0.042$ is an estimate, not a certified lower
bound.**  The integral group of
$Q=-x_0^2+x_1^2+x_2^2+x_3^2$ is a nonuniform arithmetic lattice, so its
Lorentz quotient has finite Haar volume.  A random affine translate is simple,
stationary and Lorentz-invariant in law.  Its non-null reciprocal vectors obey
$|q^2|\ge(2\pi)^2$, while its null vectors are allowed by the literal strict
inequality in `TESTS.md:3125`.

There are finitely many primitive null cusp orbits; each parabolic stabilizer
has finite covolume, and the multiples contribute $\sum_{n\ge1}n^{-2}<\infty$
because null-cone measure scales quadratically.  Thus the null orbital
coefficient $b$ is finite and positive.  The null shell contributes exactly
$bJ_D(0)T^6$, while Theorem D controls the non-null shells.  This proves

\[
  \operatorname{Var}N(D_T)\ge c_0T^6\quad(c_0>0),
\]

and also gives finite local second moments.  Equivalently, in a cusp coordinate
the shift-averaged second-moment contribution grows only $O(y)$ against Haar
density $y^{-3}dy$, an integrable tail.  Constant intensity across the frame
components also means there is no extra atom at $q=0$.

The Heath--Brown use is correct.  The determinant/discriminant class of this
quaternary form is $-1$, not a rational square, so the zero count is $X^2$,
not $X^2\log X$; this is the nonsquare case of Heath--Brown's quaternary
asymptotic (see the [original 1996 paper record](https://ora.ox.ac.uk/objects/uuid:bbd3c62f-f010-44b5-8be5-87e903fb0084)).
The finite counts through $X=1500$ support $bJ_D(0)\simeq0.0421$
(`scripts/r63_misc.py:33-47`; `scripts/r63_misc.out:13-19`), but no error bound
on that limiting constant is supplied.  Record the rigorous coefficient as
$c_0>0$, with $0.0421$ a numerical estimate.

The narrow negative-claim stress test passes: finite-volume quotient, positive
and finite cusp density, finite second moments, admissibility under the literal
strict inequality, and the possible logarithmic alternative were each checked.
The result is only an ensemble diamond counterexample; it is not a no-go for
all strict-lensing-silent processes, per-realization counts, or other windows.

## 5. Corrected Lemma V-prime

**Confirmed after two proof repairs.**  Finite local second moments imply that
the Bartlett measure is translation-bounded: choose a compactly supported test
function whose Fourier transform is bounded below on a fixed Euclidean ball;
modulation moves that ball while the random integral remains bounded by the
same $N(|f|)\in L^2$.  For invariant radius $s=\sqrt{|M|}$, a fixed-radius
ball centered at a shell rest point intersects an $M$-interval of width
$O(s)$, while its invariant shell volume is $\gtrsim s^{-1}$.  Translation
boundedness therefore gives

\[
 \nu\{M:|M-s^2|\le Cs\}=O(s).
\]

Summing these intervals up to invariant square $X$ yields
$\nu([-X,X])=O(1+X)$, filling the step sketched at
`R6-3_report.md:307`.  Integration by parts then gives both

\[
 \int_{|M|\ge c}\frac{1+\log|M|}{M^2}\,d\nu(M)<\infty,
 \qquad
 \int_{|M|\ge c}|M|^{-3/2}\,d\nu(M)<\infty.
\]

The orbit decomposition at `R6-3_report.md:306` should first distinguish
future and past timelike hyperboloids as well as the two null half-cones.
Spectral inversion symmetry for a real random measure equates the future/past
weights, which then permits the worker's both-sheet convention.  The assumed
gap removes both null half-cones, and mean ergodicity removes the zero atom.

The Gaussian domination sentence at `R6-3_report.md:305` is not valid as
written because a Gaussian mollifier has unbounded support and is not dominated
by $N(A_1)$.  Use the standard $L^2$ extension of the covariance spectral
identity to compactly supported indicators, or compact mollifiers plus an
explicit $L^2$ limit.  With this repair, the diamond estimate from item 2,
the cone estimate from item 3, and Schwartz decay for smooth windows prove

\[
 \operatorname{Var}N(D_T)=O(T^2\log T),\quad
 \operatorname{Var}N(P_T)=O(T^3),\quad
 \operatorname{Var}N(w(\cdot/T))=O(T^{-n})\ \text{for every }n.
\]

Thus corrected Lemma V-prime is **DERIVED**.  It is genuinely stronger in its
hypothesis than strict lensing silence because it gaps timelike shells too.

For the still-open one-sided question, one auxiliary statement is false:
independent superposition adds spectra but does not necessarily add *white*
spacelike weight; the superposition of two independent gapped LRL processes is
an immediate counterexample to that wording (`R6-3_report.md:332-337`).
Thinning and Cox modulation do add the stated white term.  Also, a volume law
only along a sequence forces corresponding subsequential spectral contribution
arbitrarily near $M=0$; it does not by itself prove the unrestricted liminf
claimed at `R6-3_report.md:330-331`.  These corrections leave strict lensing
silence **OPEN**.

## 6. Lambda arithmetic, direction, and epoch scaling

**The arithmetic and “too large” direction are correct, conditionally.**  Under
the imported H1/H2/H4 equalities,

\[
 \Delta\Lambda=\bar\ell_P^2\rho/\sqrt{\operatorname{Var}N},
\]

so reducing count variance makes the inferred $\Delta\Lambda$ larger, not
smaller.  Independent arithmetic gives
$1.4113\times10^{30}\Lambda_{\rm obs}$ for the flat cone and
$1.3660\times10^{59}\Lambda_{\rm obs}$ for the equal-volume diamond
(`referee_checks.py:148-167`; `referee_checks.out:17-19`), matching
`R6-3_report.md:357-363` to rounding.

The correct reading is therefore: **under H1, H2 and H4, and using the
ensemble variance of these flat windows as the cosmological count, the LRL site
mechanism predicts fluctuations vastly larger than observed and is excluded as
an everpresent-Lambda magnitude mechanism.**  H1, H2 and H4 are named heuristic
imports, not consequences of the minimal axioms; the actual FRW embedding and
count-volume bridge remain unsupplied.  This conclusion does not concern the
mean Lambda and does not exclude the independently thinned B-prime-plus record
layer (`R6-3_report.md:367-370`).

The exponents at `R6-3_report.md:364-365` are correct for a homothetically
scaled flat cone or diamond:
$\Delta\Lambda\propto T^{-3/2}$ and
$\Delta\Lambda\propto(T\sqrt{\log T})^{-1}$, respectively.  Comparing them
with $H^2\propto T^{-2}$ assumes a power-law epoch with $H\asymp T^{-1}$.
It is not a proved FRW-window calculation and is not universal in a
Lambda-dominated epoch.  The safe conclusion is failure of everpresent
tracking in that homothetic proxy, not an all-epoch cosmological theorem.

## 7. Fixed readings and final disposition

- **LRL count: SUB-VOLUME — confirmed.**  Sharp diamonds obey
  $O(T^2\log T)$; flat-truncated cones obey $O(T^3)$ after the repaired
  combined-transform estimate; smooth dilations are super-polynomially small.
  The coefficients $0.1665$ and $0.4847$ are numerical estimates of exact
  convergent series, not exact certified decimals.
- **Literal item (d): REFUTED — confirmed.**  The nonuniform Lorentz-random
  isotropic lattice satisfies the literal non-null gap but has positive null
  orbital weight and hence $c_0T^6$ diamond variance.
- **Corrected two-sided-gap Lemma V-prime: DERIVED — confirmed with the proof
  repairs in item 5.**
- **Strict lensing silence: OPEN — confirmed.**  No classical process with only
  near-null timelike Bartlett weight was constructed or excluded.
- **Cosmological consequence: conditional/bounded, not framework-derived.**
  “Everpresent-Lambda magnitude excluded on LRL sites under H1/H2/H4” is the
  strongest permissible recording, with the flat-window and ensemble scope
  explicit.

## Strongest correct statement

For the cocompact, null-free $L_7$ Lorentz-random lattice, the exact Haar shell formula implies sharp-diamond variance $O(T^2\log T)$, flat-truncated-cone variance $O(T^3)$, and $O(T^{-n})$ variance for every $n$ under smooth compactly supported dilations, so its ensemble site count is **SUB-VOLUME**; more generally the same bounds hold for a stationary Lorentz-invariant random measure with finite local second moments, no zero atom, and a two-sided invariant spectral gap that includes the punctured null cone.  The literal item (d) omits that null exclusion and is **REFUTED** by the Lorentz-random isotropic integer lattice, whose positive finite null orbital weight gives $\operatorname{Var}N(D_T)\ge c_0T^6$ for some $c_0>0$ (numerically about $0.0421$).  Strict lensing silence alone remains **OPEN** because it permits timelike weight accumulating toward the null cone.  Under the imported H1/H2/H4 equalities and the flat-window ensemble proxy, the LRL site variances make $\Delta\Lambda$ about $1.4\times10^{30}$ (cone) or $1.4\times10^{59}$ (equal-volume diamond) times the observed value—too large, with non-everpresent epoch scaling in that proxy—but this is not an FRW construction, a statement about the mean Lambda, or an exclusion of independently randomized inert records.
