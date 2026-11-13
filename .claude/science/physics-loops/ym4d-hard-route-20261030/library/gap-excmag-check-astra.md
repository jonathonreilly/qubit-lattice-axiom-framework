# Repo search

Codex, OpenAI gpt-6-astra, xhigh; 2026-11-13; source checkout
`4f462ad994ca68acaf67adfe67617f509f3ccce7`. Research check, not an audit;
this text grants no status. The task-specific prior file does not exist.
The November 8 repo-search digest was read in full and used as a locator.
No item there covers this check. No matching owner row was found in
`open-registry.md` for EXC-W, excmag, empty-line, flux tension, magnetic
residual, or carrier switch. This checks row 888; it starts no proof lane.

The five requested refs in `/Users/jonreilly/Projects/Physics` were searched:

| Ref | Revision read |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Completed statement query, `git grep -n -i -E`, Markdown/TeX, cap 65:
`EXC-W|gap-excmag|flux free.energy|empty.line probability|magnetic residual|spin.5/2.*carrier`.
There were 15 hits, all repetitions of these three paths across the five refs:

* `docs/NATIVE_WEAK_ELECTRIC_DEFECT_DENSITY_NOTE_2026-09-08.md:116`:
  its defect D mixes flux blocks, so its fixed-flux free energy is not a
  sector decomposition. Different native model; no EXC bound supplied.
* `docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md:76`:
  fixed-flux free-energy minimization equals an auxiliary Fock-trace flux
  optimization, without a unitary equivalence. Different native model.
* `docs/work_history/repo/review_feedback/pr8051-native-optimal-flux-evidence/originals/native-zero-penalty-flux-selection-root/pr8051-originals-native-zero-penalty-flux-selection-root-DERIVATION.md:18`:
  the same auxiliary-trace statement, not separate evidence.

No direct target hit occurred. The identical query outside this lane in the
sparse checkout returned no hit. Initial broad queries containing `EMPTY)`
or `electric.flux|spin.network` reached their caps amid unrelated records;
they are locators, not completed absence searches.

Within the lane the direct sources already supply much of the task:

| Source | Exact existing statement and closeness |
|---|---|
| `gap-filter-ls-opus.md:128-155` (Claude Opus 5.5), EXP | `partial_s log p = a Delta(s)/s`; sector traces increase with s. Exact identity used here, not new. |
| Same, 170-185 | EXC is an integral lower bound; **EXC-W is pointwise** `Delta(s)>=delta L_i` on the whole boost interval. Exact consumer; its distinction matters below. |
| `gap-exc-astra.md:299-350` (Codex) | Full-trace electric reference has `J^el/L_i -> gamma`, with explicit uniform error (20). Exact prior input. |
| Same, 365-393 | `J_beta=J^el+integral(d_S^mag-d_1^mag)` at the magnetic cut. Exact prior identity; already locates the open response. |

Index first: `sa-index/README.md`, searches of chunks, obligations, and
`ca-full/` for EXC-W, electric flux, spin network, empty line, flux tension,
Bessel and GL3/GL4; neighbouring rows `chunk-02.md:83-96` and
`obligations.md:58-74`; then outline `YM4_sketch_500.tex:2195-2243`.
Ethan Sussman and Levent Alpoge, with Claude and Codex as text authors,
already prove GL3/GL4: `c_j=2 exp(-beta) I_(2j+1)(beta)/beta`, positivity,
factorial decay and adjacent-ratio bounds. Dividing by c_0 gives this
note's r_j. These are cited inputs, not re-derived results. The targeted
CA index query found no match. This is search coverage, not a claim that
all differently named account results were excluded. Source revision
`31a47c543775` is supplied by the owner. No Balaban estimate is imported.

# Check record

Here `N` means the note under check, `library/gap-excmag-max.md`, at the
checkout pin above. Each verdict concerns its stated mathematics, not
repository standing. `FAILS` can mean a specified inference fails; it need
not mean the underlying SU(2) conjecture has a counterexample. All scalars
z^(na) are removed consistently when comparing unnormalized traces.

## 1. Magnetic bound versus EXC-W — HOLDS AFTER CORRECTION

N:62-66,162,291. The exact identity is

\[
 R(b)=J_b-J^{el},\qquad
 J_b={1\over a}\log{p_{S,b}\over p_{1,b}}.
\]

Write `J^el=gamma L_i+e_a`, with `e_a=o(L_i)` uniformly by prior (20).
Then the finite-size equivalence is precisely

\[
 R(b)\ge-\theta\gamma L_i
 \quad\Longleftrightarrow\quad
 J_b\ge(1-\theta)\gamma L_i+e_a.
\]

A positive uniform lower limit of `J_beta/L_i` is equivalent to such a
bound **eventually in a**, after spending a fixed part of the margin on
`e_a`. A limit inferior alone says nothing about the finitely many smaller
tori. Uniformity in beta, twists and aspect ratios must be inside the
limit inferior. Gamma is positive and bounded away from zero on the
specified compact window.

There is also a coefficient change in N. Its initial row-881 target uses
`gamma_min`, while the claimed equivalence later uses `gamma(beta)`.
For the original target, the exact right side is instead

\[
 J_\beta\ge[\gamma(\beta)-\theta\gamma_{\min}]L_i+e_a.
\]

A positive uniform area gain alone does not imply this stronger bound
on a varying-beta interval. For example, at a beta with
`gamma(beta)>gamma_min`, a limiting gain kappa satisfying
`0<kappa<gamma(beta)-gamma_min` is positive but has
`R/L_i -> kappa-gamma(beta)<-gamma_min`. This is an algebraic failure
of equivalence, not a counterexample for the actual model. Fix beta,
use gamma(beta) in the magnetic threshold, or retain the stronger
beta-dependent margin explicitly. Do not identify the original
`gamma_min` target with the weaker integrated area condition.

The further identification with row 872's literal EXC-W is wrong. EXP
identifies this bound with an **integrated area bound** on Delta. Row 872
requires `Delta(s)>=delta L_i` at every s. That pointwise assertion implies
the integrated bound; the converse does not follow. A positive integral
can coexist with zero or negative Delta on a subinterval. Proposition 6.1
below even gives this distinction within the electric reference: its area
gain is positive, while Delta(1)/L_i tends to zero. Call the weaker
condition integrated EXC-W, or state it explicitly; do not silently
redefine the cited EXC-W. Neither form is proved at b=beta here.

## 2. R as a flux free-energy difference — HOLDS

N:46-60, with prior `gap-exc-astra.md:365-381`. Define the odd-flux cost
`f_s(b)=-a^(-1) log p_(s,b)`. Trace differentiation gives

\[
 \int_0^b d^{mag}_{s,u}\,du=f_s(0)-f_s(b),\qquad
 R(b)=[f_1(b)-f_S(b)]-[f_1(0)-f_S(0)].
\]

This fixes the sign and normalization of the free-energy description.
The flux cost uses the full partition function in its denominator.
Since `0<p<=1` and the electric lower bound (19) holds,

\[
 \int_0^b d^{mag}_{s,u}\,du
 \le(-\log q_s)L_i+{n\over a}\log(1+\epsilon_s(a)).
\]

The last term tends to zero uniformly. This is an upper bound for **each
single-model response**, not by itself an upper bound for their difference
R. A lower bound on the unboosted response, supplied by Theorem 9.3, is
needed for that conclusion. This distinction repairs the brief's wording
that might otherwise attach M3 directly to R.

## 3. Theorem 3.3: second derivative — HOLDS

N:78-110, with the window `23/10<=beta<=13/5` fixed as in N's setting.
This verdict covers the displayed asymptotics with `o(1)`, not an exact
finite-volume equality to the leading term. Its numerical table is checked
separately below.

Differentiating `Tr((K exp(bM))^a)` twice, rather than using the author's
half-multiplier derivative, gives

\[
 Z_\sigma''(0)=a\sum_{k=0}^{a-1}
       \operatorname{Tr}(P_\sigma M K^k M K^{a-k}).
\]

The first derivative vanishes: a fundamental plaquette changes each of its
four edge spins by one half. Two different plaquettes cannot restore every
edge spin when all periods are at least three. Thus only equal plaquettes
survive the second derivative, and their twist signs square to one.
For an unordered pair with weight ratio x, its two orientations contribute
`w^a(1+2x+...+2x^(a-1)+x^a)`. This verifies S1, including the factor a.

For a line in spin j, integrate the three off-line edges of a touching
plaquette first. In `V_(1/2) tensor V_j`, the two summands have dimensions
`d_(j-1/2)` and `d_(j+1/2)`. Schur orthogonality therefore gives squared
amplitudes `d_J/(8 d_j)` after the factor `x=chi_(1/2)/2`. Their sum is
1/4. An off-line plaquette also has squared amplitude 1/4. This verifies
Lemma 3.2 and gives exactly N's D formulas. There are `4 L_i` touching
plaquettes, with no double counting. The common off-line contribution
cancels in odd minus all.

The remainder estimate is adequate at the two endpoints. An odd physical
assignment contains a simple odd cycle. At every cycle vertex, omit its
two cycle dimensions in the invariant-tensor bound. Then
`m(j)<=product_(e outside cycle) d_j(e)^2`. For either endpoint, the largest
half-integer weight q has a fixed gap to the others, uniformly in beta.
Consequently `u=sum_(j half-integer) w_j^a=q^a(1+O(rho^a))`, `rho<1`.
The cycle counts in N:110 bound non-straight cycles relative to a straight
one by a polynomial times an exponentially decreasing quantity. Off-cycle
excitations cost `(1+epsilon)^n-1`, also exponentially small. Removing
nonleading homogeneous lines leaves the stated one- or two-class formula.
The polynomial factor from two insertions does not defeat either bound.
This justifies the absolute `o(1)`, despite division by a small odd trace.

The limit of g_a is v(x) for all local ratios, uniformly below one. Hence

\[
 R(0)=R'(0)=0,\qquad
 R''(0)=4L_i\pi_5(D_{5/2}-D_{1/2})+o(1).
\]

For the sign, GL4 gives `r_2<0.024`, while `q_S>r` and
`x_3<=x_2<r_2 r^2`. The positive part of the difference is less than
`0.0123 r^2`; its first negative term alone is at least `r^2/8`.
The difference is strictly negative. No computation is an input.

The claim that only neighbouring plaquettes respond is a statement about
the leading dilute-line term. The exact finite-torus answer also contains
the exponentially small excited-configuration terms. In particular it is
not exactly `4 L_i D` at finite a.

## 4. Theorem 3.3's displayed values — HOLDS AFTER CORRECTION

N:112-117 and 127-133. The exact D formulas hold. At beta=2.3 the first
numeric table has inaccurate last digits. At beta=2.6 the quoted values
have the right scale; the last-place precision should not be overstated.
The following deliberately loose decimal bounds come from finite rational
arithmetic, not a numerical run:

| beta | D_(1/2) | D_(5/2) | 4(D_(5/2)-D_(1/2)) |
|---|---|---|---|
| 23/10 | 0.024333 < D < 0.024335 | -0.027363 < D < -0.027360 | -0.206792 < value < -0.206772 |
| 13/5 | 0.028265 < D < 0.028267 | -0.038686 < D < -0.038684 | -0.267812 < value < -0.267796 |

Thus safe quoted values are `(0.02433,-0.02736)` and
`(0.02827, about -0.038685)`. The rounded response coefficients -0.2068
and -0.2678 survive. Neither these decimals nor a b-star extrapolation
is needed to prove the derivative formula or its negative sign.

Here is reproducible written arithmetic for the bounds. For
`t=beta^2/4`, put

\[
 A_n(t)=\sum_{k\ge0}{n!t^k\over k!(n+k)!},\quad
 B_n(t)=\sum_{k=0}^{8}{n!t^k\over k!(n+k)!},\quad
 T_{n,9}={n!t^9\over9!(n+9)!}.
\]

Successive omitted terms have ratio at most `t/[10(n+10)]`, so

\[
 B_n<A_n<B_n+{T_{n,9}\over1-t/[10(n+10)]}.
\]

Use `r=(beta/4)A_2/A_1`, `r_1=(beta^2/24)A_3/A_1`,
`r_2=(beta^4/1920)A_5/A_1`, `r_3=(beta^6/322560)A_7/A_1`.
The finite-group coefficient is

\[
 q_S={\sinh\beta+4\sinh(\beta/2)
       \over\cosh\beta+3+8\cosh(\beta/2)}.
\]

For cosh and sinh use their positive series through k=8. Bound the tail
by its first omitted term divided by one minus the next-term ratio.
At `x<=13/5`, those ratios are at most `x^2/(19*20)` for cosh and
`x^2/(20*21)` for sinh. Substitution gives these intermediate rational
bounds (each displayed endpoint is a terminating decimal, hence rational):

| beta | r | r_1 | r_2 | r_3 | q_S |
|---|---|---|---|---|---|
| 23/10 | (0.47927907,0.47927909) | (0.16647114,0.16647119) | (0.0099268,0.0099271) | (0.0002962,0.0002966) | (0.4841271,0.4841272) |
| 13/5 | (0.52034209,0.52034212) | (0.19947366,0.19947371) | (0.0148021,0.0148024) | (0.0005565,0.0005571) | (0.5281990,0.5281993) |

For the final substitution it is convenient to use

\[
 D_{1/2}={r^2\over8(1-r^2)}
  +{3r_1r^2\over8(1-r_1r^2)}-{r^4\over2(1-r^4)},
\]
\[
 D_{5/2}={5x_2\over24(1-x_2)}
  +{7x_3\over24(1-x_3)}-{r^4\over2(1-r^4)}.
\]

All denominators are positive. Bounding each positive term above and below
and reversing the bounds on the negative term yields the first table.
For an explicit check of the disputed first entry, the beta=2.3 sums begin
`A_1=1+0.66125+1.74900625/12+2.313060765625/144+...` and
`A_2=1+1.3225/3+1.74900625/24+2.313060765625/360+...`.
They give `r` near 0.4792790783 and D_(1/2) near 0.02433366.
The first q_S entry is near 0.48412714, not 0.48414. The later table's
q_S near 0.48413 and gamma near 0.01006 correct that earlier typo.

## 5. Proposition 6.1 — HOLDS AFTER CORRECTION

N:203-211. The uniform logistic formula is correct after filling the
uniform remainder argument below. Theorem 3.3's endpoint proof cannot
simply be reused uniformly through `s=s_c`: there its crude sum
`u^L=(r^a+(s r_(5/2))^a+...)^L` has a factor `2^L`. Its fixed spectral-gap
argument no longer applies. Also, the other half-integer weights need be
below the **larger** carrier by a uniform factor, not below both carriers
as N's proof says.

Here is the missing bound. Let `q=max(r,s r_(5/2))<1`, uniformly on the
compact `(beta,s)` domain. Then `sum_half (w_j/q)^a<=3` for all sufficiently
large a, uniformly in s. All half-integer spins other than 1/2 and 5/2
are below q by a common factor less than one.

Choose a simple odd cycle g in any contributing assignment. Let F be its
set of nonzero edges outside g. At a vertex untouched by F, the two cycle
spins must agree, by the degree-two intertwiner rule. At most `2|F|`
vertices are touched. If F is nonempty, this cuts the cycle into at most
`2|F|` constant-spin runs (or one run if none is touched). A run of length
h has total half-integer weight at most `3 q^(ah)`. With
`m(j)<=product_(e outside g) d_j(e)^2`, summing the assignments of F costs
at most

\[
 q^{a|g|}\big[(1+9\epsilon_s(a))^n-1\big].
\]

If F is empty, the whole cycle has one constant spin. On each straight
cycle its contribution is exactly
`r^(a L_i)+(s r_(5/2))^(a L_i)` plus the uniformly smaller homogeneous
spins. The non-straight cycle counts in N:110 now use q^a, with at most a
factor 3 for their homogeneous spin, rather than `(2q^a)^|g|`.
Their sum relative to a straight cycle is exponentially small, uniformly
in s. Since `epsilon_s(a)<=C q_max^a` and `n=O(a^3)`, the same is true for
nonempty F. Multiplication by `N<=n` preserves convergence to zero.
This proves, uniformly in s,

\[
 \Delta_0(s)=L_i\,{(s/s_c)^{aL_i}\over1+(s/s_c)^{aL_i}}+o(1).
\]

The leading integral is exactly

\[
 {1\over a}\log{1+(S/s_c)^{aL_i}\over1+(1/s_c)^{aL_i}}
       =\gamma L_i+o(1).
\]

At `s=s_c` the leading count is `L_i/2`. Uniform convergence to a sharp
step at that point is not claimed; the transition width in log s is
`1/(a L_i)`. Away from the transition the two one-sided limits hold.
Finally, the upper interval occupies the fraction
`(S-s_c)/(S-1)=(1-exp(-gamma))/(1-1/S)` of `[1,S]`.
It is about 1.0% at beta=2.3 and 1.5% at beta=2.6. Replace the window-wide
phrase "the last one per cent" by "the last roughly one to one-and-a-half
per cent", or retain the exact formula.

## 6. Proposition 7.5 — HOLDS

N:251-277. Work on the odd Hilbert subspace and put
`Y_q=L^(1/2) Q_q L^(1/2)`. Both Y's are positive and their sum is L.
The Schatten-a triangle inequality directly yields

\[
 (\operatorname{Tr}_-L^a)^{1/a}
 \le(\operatorname{Tr}_-Y_0^a)^{1/a}
    +(\operatorname{Tr}_-Y_1^a)^{1/a}.
\]

Compression gives the corresponding lower bound by either summand's
trace. The nonzero spectra of `L^(1/2)Q L^(1/2)` and `QLQ` agree.
Moreover `Q_0 L_(S,b) Q_0=L_(0,b)`. These facts prove H1 without
assigning signs to individual cyclic words. EXP's monotonicity of full
and odd unnormalized traces then gives H2 and H0 exactly as printed.
Splitting Q_1 into the orthogonal "first high edge" projections and using
compression below H_e proves H3 by the same norm inequality.

The conclusion is about these compressed operators. It does not prove
that the interacting odd sector is a disjoint mixture of a spin-1/2
sheet and a spin-5/2 sheet. In particular, t_1 includes arbitrary
configurations with a high edge, even when that edge is unrelated to the
winding line. Nor do positive compression traces provide a positive
multi-time spin-history expansion. N's stated warning about the extensive
vacuum response is appropriate. None of H1-H3 supplies a crossing.

## 7. Theorem 9.3 — HOLDS

N:315-341, including Lemmas 9.1 and 9.2. The comparison keeps the gauge
projection and all spatial twists.

For `W Phi=chi_c(U_l) Phi`, with Phi independent of line edges, Haar
orthogonality gives `W*W=1`. Each individual line edge is Haar even under
the density `|chi_c(U_l)|^2`, because another line edge can be integrated
first. Each plaquette touching the line contains exactly one line edge.
Thus its conditional mean under that density is zero, for every fixed
outside field, regardless of its twist sign. Jensen gives the conditional
integral of `exp(b M_l)` at least one. Together with
`K^(1/2)W=w_c^(L_i/2) W K^(1/2)`, this gives the quadratic-form inequality

\[
 W^*LW\ge w_c^{L_i}L^{(l)}.
\]

W interchanges the two cut parities. Min-max applied to its odd-sector
compression, followed by the increasing scalar function `lambda^a`,
gives `Z_- >= w_c^(a L_i) Z_+^(notl)`. This uses trace monotonicity of
powers, not the generally false operator monotonicity of X -> X^a.

For s=1, the full link-integral density is pointwise positive. Removing
the `4 a L_i` touching spatial factors costs at most `exp(4abL_i)`.
Integrating each line-edge temporal chain gives
`sum_j r_j^a chi_j(P_x) chi_j(P_y)`, bounded above by
`1+epsilon_1(a)`. The remaining density is positive. Its temporally
centre-twisted integral is also positive, so
`Z_+^(notl)>=Z^(notl)/2`. These operations prove exactly

\[
 p_{1,b}\ge {1\over2}(1+\epsilon_1(a))^{-L_i}
                   (r e^{-4b})^{aL_i}.
\]

Combining this with both sides of prior (19) gives the explicit finite-size
lower bound for `I_1(b)=integral_0^b d_1^mag`:

\[
 I_1(b)\ge-4bL_i-{1\over a}\log {n\choose L_i}
 -{L_i\over a}\log C-{n+L_i\over a}\log(1+\epsilon_1(a))
 -{\log2\over a}.
\]

Since `L_i/a<=2`, this implies N's
`-4bL_i-2 log(12Ca^3)-o(1)`. M3 supplies the upper bound.
These are uniform in twists and admissible aspect ratios.
The raw inequality holds for every allowed size; the notation o(1)
describes its large-a simplification.

For completeness, the exact upper consequence for R includes `-J^el`:

\[
 R(b)\le(-\log r+4b)L_i+{L_i\over a}\log(1+\epsilon_1(a))
             +{\log2\over a}-J^{el}.
\]

Dropping `-J^el` is justified eventually by the positive electric
asymptotic. Prior (20) alone does not prove `J^el>=0` for every small
torus. N's asymptotic upper bound is unaffected.

## 8. Proposition 9.4 — HOLDS

N:349-359. Put `Pi=Pi_0^l P_+`, `Y=L^(1/2)Pi L^(1/2)` and `Z=Tr L^a`.
Schatten Holder, with exponents a and a/(a-1), gives

\[
 \pi_0^+Z=\operatorname{Tr}(Y L^{a-1})
 \le[\operatorname{Tr}(Pi L Pi)^a]^{1/a}Z^{1-1/a}.
\]

This verifies the direction and normalization of the key bound:
`Tr(Pi L Pi)^a >= (pi_0^+)^a Z`. Pointwise multiplier comparison gives
`Pi L Pi <= exp(4bL_i) P_+ L^(l) P_+`. Trace-power comparison and Lemma 9.1
therefore give precisely

\[
 p_{s,b}\ge\big(w_c^{L_i}e^{-4bL_i}\pi_0^+(s,b)\big)^a.
\]

No pointwise positivity of the boosted temporal kernel is used here.
The genuine one-slice probability is at the kinetic cut. EMPTY as stated,
including its **even-sector** condition, suffices for finite flux tension.
It also implies VAC-S with `C_1=e^(4b)/c_3`.

N:361's support for EMPTY at s=1 needs a small correction: saying "either
p or pi_0^+ is at least half" does not alone prove a lower bound on
pi_0^+. The required even-sector bound does follow directly. Inserting
Pi_0^l at one time slice replaces the line's temporal kernels by 1. The
remaining untwisted and centre-twisted Wilson densities are positive.
Thus `Tr(Pi_0^l Theta L^a)>=0`, and

\[
 \pi_0^+(1,b)\ge\tfrac12\Pr(l\text{ empty})
 \ge\tfrac12(z e^{-\beta})^{L_i}
 \ge(2^{-1/3}z e^{-\beta})^{L_i},\qquad L_i\ge3.
\]

This argument is unavailable for s=S's signed temporal density. EMPTY
for the boosted model remains an open input, not a conclusion of FT.

## 9. Carrier crossing at b-star — FAILS as an inference

N:123-124,151-164,223-225,240,294-308 and the final RESULT. This verdict
rejects the inference from second-order data. It does not refute a
crossing in the actual model.

Let `c=2(D_(1/2)-D_(5/2))>0`. The asserted carrier advantage begins
`h(b)=gamma-c b^2+O(b^4)`. The two even analytic functions

\[
 h_-(b)=\gamma-cb^2,\qquad
 h_+(b)=\gamma\exp(-cb^2/\gamma)
\]

have exactly this same value and second derivative at zero. The first
crosses zero; the second stays positive. Both have Taylor expansions
uniform on every compact real interval. Thus even a uniform convergent
expansion through the proposed crossing is insufficient without a
quantified remainder that forces opposite signs at two points. The
phrase "the expansion parameter is small" bounds no coefficient.
There is likewise no deduction that the switch stays absent all the way
to b=beta. A later reversal is not excluded by the second-order data.

There is a second missing step. At b>0, spin 1/2 and spin 5/2 are not
separate conserved sectors of this SU(2) transfer operator. They share
the same centre parity. Plaquette multiplication changes spin labels;
Q_0 does not commute with the transfer. Separate tensions labelled by
those two carriers, their thermodynamic limits, and a maximum-of-two-
branches formula have not been constructed. H1 is a compression bound,
not that construction. An abelian analogue with distinct charge-winding
sectors does not supply it. Finite-volume partition functions are analytic
and positive for real b; a nonanalytic limiting crossing requires proof.

What remains valid is the local decrease of R for each sufficiently large
fixed torus, on a possibly volume-dependent neighbourhood of zero. The
quantity `sqrt(gamma/c)` is a quadratic extrapolation, roughly 0.31-0.34,
not an established crossing location. Delete statements that the electric
gain *is* erased, that the limiting free energy *is* nondifferentiable
there, or that its continuation *fails* on this basis. Their status is an
unproved scenario. An exponentially small but positive remaining fraction
would, in any event, still allow a mathematical constant theta<1;
"visibly below 1" is not a quantified replacement for that requirement.
The group-blind erasure claim inherits the same missing implication.

## 10. DRESS — HOLDS AFTER CORRECTION

N:227-237 and 303. In the positive one-slice spin law at the **kinetic**
cut, define

\[
 \Delta_\beta(s)=\sum_e\big[
   \Pr_{s,\beta}(j_e\in\{5/2,7/2,\ldots\}\mid-)
  -\Pr_{s,\beta}(j_e\in\{5/2,7/2,\ldots\})\big].
\]

EXP gives the exact identity

\[
 \int_1^S\Delta_\beta(s){ds\over s}=J_\beta.
\]

Therefore the displayed DRESS inequality is exactly the **integrated**
area comparison `J_beta>=kappa L_i`, with its chosen finite-size or
asymptotic quantifiers stated explicitly. It is well-defined without any
carrier-crossing hypothesis. It implies
`p_(1,beta)<=exp(-kappa a L_i)`, using `p_(S,beta)<=1`.
It is equivalent, with the size qualifications in section 1, to the
magnetic bound using gamma(beta). It is not a weaker way to prove that
bound. The original gamma_min target on a varying-beta interval is
stronger, as section 1 explains.

The appended claim "with the odd sector carried by the spin-1/2 sheet
for every s" is an additional unproved assertion. It is not part of EXP,
and no unique fundamental sheet is selected by conditioning only on odd
parity. Remove it from the equivalence. The law measures edge spins on
one slice; a positive law of complete temporal plaquette sheets has not
been established for the signed boosted density. Keep "dressing of the
fundamental sheet" as a proposed interpretation only. Also do not identify
this integrated inequality with row 872's stronger pointwise EXC-W.

# Coverage and delivery

Additional method-source reads complete the search record above:

* `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106-149`,
  located through the November 8 digest, already gives the simple-loop
  eigenvalue `r_f^b`, Haar variance 1/4 for SU(2), and a rank-one
  convolution lower bound. It distinguishes operator positivity from
  pointwise kernel positivity. This is prior local algebra, not a bound
  on the present normalized winding-sector ratio. It is credited, not
  repeated as new work.
* `origin/main:docs/GAUGE_WILSON_COMPACT_CUBE_LOW_ELECTRIC_SPECTRUM_RITZ_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md:37-63`,
  found by the broad method query, already states the degree-two
  intertwiner matching rule. It treats an SU(3) compact cube, not this
  boosted SU(2) torus. Only the representation-theoretic rule is reused;
  none of its computed multiplicities enters this check.
* The completed five-ref method query
  `one.bond convolution|rank.one convolution|empty.line|flux tension|second.order magnetic`
  returned only 24 unrelated formatting/lineage hits, below its cap 50.
  The relevant soft-route source above was located through the prior digest.

Read N in full, with all load-bearing steps of the requested statements
checked as recorded above. Recalled Ginibre/Seiler facts and the GUIDE
runs are not premises of any verdict here. No GUIDE script was executed
or certified. No computer-assisted proof, numerical experiment, audit,
status update, source repair, public post or remote push was performed.
Only this requested report was written. It remains at the requested lane
path for the lead; the source note and FINISH were not edited.

RESULT: HOLDS for the exact flux-response identities, Theorem 3.3's derivative formula, Proposition 7.5, Theorem 9.3 and Proposition 9.4; HOLDS AFTER CORRECTION for the EXC-W identification, gamma_min versus gamma(beta), and size quantifiers, the coefficient table, Proposition 6.1's uniform proof and percentage, and DRESS's interpretation; FAILS for inferring the carrier crossing or erasure from second-order data. Isotropic EXC and the boosted EMPTY bound remain open; this research check grants no status.
