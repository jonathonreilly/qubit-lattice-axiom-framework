# Repo search

The target-specific prior digest is absent at `39b239180`.
The lead's `prior/repo-search-2026-11-08.md` records searches of main
and PRs 10114, 10133, 10134 and 10141 for older construction obligations.
It is not a target-specific absence proof. Its closest hit is useful:
Codex's `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, Sections 1–2, on PR 10114
at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, proves a local
ground-state density comparison and a volume-independent positive
one-step plaquette correlation. I read lines 1–175 and reuse that
argument below. The digest reports the same blob on PR 10133.
This already supplies the local lower bound; it is not new here.

On main at `a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`, I opened
`docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`,
lines 1–105. It supplies positive Wilson plane kernels on an open
temporal slab, not a comparison of periodic sector weights.
The local `gap-es1-astra.md`, Lemma 7 and Corollary 8, already gives
the fixed-box lower thermal bound and the side-three power 3/4.
The new target here is uniformity in the box size, including magnetic
backgrounds in the heavy crossed sectors. I do not repeat that example.

The closest consumer is Claude Opus 5.5's `gap-es1-opus.md`,
Sections 2 and 5, with `gap-es1-opus-check.md`'s corrections.
The polymer input is Claude Opus 5.5's `gap-sc-box.md`, Section 3,
and Claude Fable 5.2's periodic port in `gap-seed-sc.md`, Section 2.
The exact `(F-h)` and flux `(LOC)` searches in `open-registry.md`,
`open-core.md` and `l17c.md` find no other owner. The registry's
`FLOOR-P2` and `label-LOC` concern different localization statements.
Rows 752 and 757 record literature searches without an applicable
fusion or cutoff-uniform LOC theorem; those records are not proofs
of absence in the literature.

Author: **Codex gpt-6-astra max**, FINISH row 765, 2026-11-12.
Source: `39b2391804e2ec8a50b05a7be4f84e4b217cac64`.
Research text, not an audit; no standing is granted.
Marks: **PROVED** means a written argument from the named inputs,
not an independent check; **ARGUED**, **GUIDE**, **OPEN** keep their
ordinary meanings. All new arguments below remain unchecked.

## 1. Exact target and the distinction from LOC

**Definition.** Use the Wilson weight
`exp[-beta sum_p(1-eta_p tr(U_p)/2)]`, normalized Haar measure,
and twists `k` in `H^2(T^4;Z_2)`. Put

\[
 B=(a,c,d),\quad c,d\in\{a,2a\},\quad a\ge3,
 \qquad S=S_{\rm ev}(a;B),\qquad
 p_{\chi,m}=\frac{Z_{\chi,m}(a;B)}{Z_{0,0}(a;B)}.
\]

The crossed set has `chi_2=m_2=0`. Its four purely magnetic
members form `L_mag={chi=0}`. Its other twelve members have
`chi!=0`, including the members with nonzero magnetic background.

**PROVED input, reused.** The positive twisted transfer operators,
Fourier projections and crossing identities give `p>=0`, `p<=1`
and `sum_X p=4`. These are the inputs of `gap-means-max.md` 4.1–4.3
and `gap-flux-exercise.md` 8.3–8.4. Positivity refers to each
`T_{B,m}` separately; no comparison of different ground states is
silently inferred from it. The physical kernel and its ground-state
measure are those of `gap-transfer.md` Sections 1–4, 8 and 9.3.

**OPEN target outside the range proved below.** Bound every heavy
`p_z` by `K sqrt(S)` with K at most polynomial in a, with the
cutoff uniformity needed by the consumer. FUSE-suff also needs the
separate light-sector bounds `(F-l)` and small even sums.

**PROVED qualification, reused.** `gap-loop-eq-check.md` Section 5
corrects the proposed LOC implication. Write
`Ptilde=Omega^(-1)(T/lambda_0)Omega` on `L^2(pi)`, and
`Dir(f)=<f,(1-Ptilde)f>_pi`. Let r_chi be its largest eigenvalue
in a nonzero electric sector of the periodic magnetic background,
and `Theta_chi=Tr[(T/lambda_0)^(a/2) P_chi]`.
LOC asks for a real bounded f in that sector such that
`Dir(f)<=c_1(1-r_chi)||f||_2^2` and
`||f||_infinity^2 ||f||_2^2<=c_2 Var_pi(f^2)`.
It gives

\[
 p_\chi\le\Theta_\chi
       \left[S^{1/(4c)}+e^{-a/(4c)}\right],
 \qquad c=4c_1c_2.
\tag{1}
\]

It does not alone give a pure power of S. Its explicit positive-kernel
counterexample establishes that distinction. It also does not compare
different magnetic transfer operators. The argument below instead
compares the actual twisted partition functions directly.

## 2. An existing local witness bounds S from below

**PROVED consequence of the cited local witness.** Let
`r(beta)=I_2(beta)/I_1(beta)` be the normalized fundamental one-link
convolution eigenvalue. For every beta>0, every periodic rectangular
spatial box with sides at least three, and every integer t>=3,

\[
 S_{\rm ev}(t;B)\ge \eta(\beta)^t,
 \qquad
 \eta(\beta)=\frac{e^{-80\beta}r(\beta)^4}
                         {4+16r(\beta)^4}>0.
\tag{2}
\]

Here is the precise use and portability of the prior result.
Take `W=tr(U_p)/2` on one elementary spatial plaquette,
`F=W-E_pi W`, and `pi=Omega^2 dU`. Equations (4)–(11) of the
soft-route note give

\[
 \langle F\Omega,(T/\lambda_0)F\Omega\rangle
 \ge\frac{v^2e^{-4\beta(p_C+b)}}{1+v/r^b},
 \qquad v=1/4,\quad b=4.
\tag{3}
\]

That proof uses distinct loop edges, independent Haar integration,
the local ground-state ratio, and positive exterior convolution.
Each holds on a rectangular box with sides at least three.
Each spatial link meets four spatial plaquettes, so `p_C<=16`.
Using this upper bound in (3) gives exactly eta in (2).
No cube symmetry or thermodynamic limit occurs in that proof.
This extends its stated cubic, side-at-least-four domain only by
checking these geometric hypotheses; the witness proof is reused.

The elementary loop is invariant under every centre flip. Thus
`F Omega` belongs to the even space and is orthogonal to Omega.
Also `||F Omega||^2=Var_pi(W)<=1`. If r_ev is the largest even
excited eigenvalue ratio, positivity and the spectral theorem give
`eta<=r_ev ||F Omega||^2<=r_ev`. Its t-th power is one term of S.
This proves (2). This is a *lower* bound on the thermal sum, not
a lower bound on an energy gap.

**PROVED numerical simplification, by hand.** For `0<beta<=R=1/12800`,

\[
 \sqrt{\eta(\beta)}\ge\beta^2/160.
\tag{4}
\]

Indeed `r<=1` because normalized convolution is a Markov contraction.
The positive character series gives `r>=beta/(4e^beta)`:
its fundamental coefficient is at least beta/2, its dimension is two,
and the trivial coefficient is at most `e^beta`.
Consequently `eta>=e^{-84beta} beta^4/5120`.
Since `sqrt(5120)=16sqrt(20)<80` and
`e^{-42beta}>=1-42beta>=1/2`, (4) follows.

## 3. A uniform bound for the actual twisted partition functions

**PROVED, given the cited polymer estimates.** On a four-torus with
sides `n_1,...,n_4>=3`, let `V=prod n_i`, `N=6V`, and
`A_min=min_{mu<nu} n_mu n_nu`. For every centre twist k and
`0<beta<R=1/12800`, put `q=beta/R`. Then

\[
 \left|\log\frac{Z^k}{Z^0}\right|
 \le 128RVq^{A_{\min}}=\frac{V}{100}q^{A_{\min}}.
\tag{5}
\]

**Signed-activity port.** For a cocycle representative `eta_p=+/-1`,
replace the existing polymer factor `g(U_p)` by `g(eta_p U_p)`.
Here `g(V)=exp(beta tr V/2)/c_0(beta)-1`.
Haar invariance under `V -> -V` keeps the same `c_0` for either sign.
The bound `|g(eta_p U_p)|<=4|beta|` is unchanged. Connected
components still depend on disjoint sets of links. The degree bound
20 and rooted count `400^(n-1)` are unchanged on all these tori.
Thus Section 3 of `gap-sc-box.md`, with the periodic port (P) of
`gap-seed-sc.md`, gives, for every k on the same complex disc,

\[
 \log Z^k=-\beta N+N\operatorname{Log}c_0+\log\Xi_k,
 \qquad |\log\Xi_k|\le(32/3)|\beta|N.
\tag{6}
\]

These logarithms vanish at beta=0. This use requires absolute
activity estimates, not nonnegative surface coefficients.
In particular it does not assume the false SU(2) association (EP).

**Winding-area cancellation.** Expand
`exp(beta sum_p eta_p s_p)`, where `s_p=tr U_p/2`.
A degree-j monomial has plaquette multiplicities `h_p`,
`sum h_p=j`. If its Haar integral is nonzero, changing one link
`U_l -> -U_l` shows that `sum_{p containing l} h_p` is even.
The mod-two plaquette chain `b={p:h_p is odd}` is therefore closed.
Its twist sign is `(-1)^{<k,b>}`.

Use the canonical representative of k: its mu-nu stack consists
of mu-nu plaquettes at fixed mu and nu coordinates. If the total
twist sign is negative, b meets at least one of the activated
stacks an odd number of times. For that pair of directions, sum
the coefficients of b's mu-nu plaquettes over the other two
coordinates. This gives a nonzero coefficient at the chosen
cell of the mu-nu two-torus.

These projected coefficients are constant over that two-torus.
To check this directly, sum b's closed-chain equation for a
mu-link over the other two coordinates. The mu-rho and mu-sigma
terms cancel in pairs by periodicity. The remaining equation
equates the mu-nu coefficients at adjacent nu coordinates.
The nu-link equation likewise equates adjacent mu coordinates.
Every projected coefficient is therefore one. Each of the
`n_mu n_nu` cells has at least one preimage plaquette in b.
Thus `j>=|b|>=n_mu n_nu>=A_min`. This needs no classification
or enumeration of surfaces.

Consequently every coefficient below degree A_min of Z^k agrees
with that of Z^0. Their constant term is one, so their logarithms
also agree below degree A_min. The analytic difference
`D_k=log Z^k-log Z^0` has a zero of order at least A_min.
By (6), `|D_k|<=(64/3)RN` throughout `|beta|<R`.
Apply the maximum principle to `D_k(beta)/beta^A_min` on discs
of radius r<R, and let r increase to R. This proves (5).
All signs and cancellations precede the absolute-value bound.

On the shapes of Section 1, `V=a^2cd<=4a^4` and `A_min=a^2`.
It follows that

\[
 D:=\max_k\left|\log(Z^k/Z^0)\right|
 \le D_a:=\frac{a^4}{25}q^{a^2}.
\tag{7}
\]

## 4. Fourier cancellation yields F-h at strong coupling

**PROVED finite comparison, valid at any positive beta.** Define D
by (7)'s first expression, without assuming its upper bound.
For every magnetic m and every nonzero electric character chi,

\[
 0\le p_{\chi,m}\le e^D(e^D-1)\le De^{2D},
 \qquad p_{0,m}\ge e^{-2D}.
\tag{8}
\]

Proof. Write `Z^{e+m}=Z^0 exp(d_{e,m})`, where `|d_{e,m}|<=D`.
For nonzero chi the sum of `(-1)^(chi.e)` is zero. Therefore

\[
 |Z_{\chi,m}|=
 \left|\frac{Z^0}{8}\sum_e(-1)^{\chi\cdot e}
                  (e^{d_{e,m}}-1)\right|
 \le Z^0(e^D-1).
\]

The even denominator `Z_{0,0}>=Z^0 e^{-D}`.
For chi=0 use `Z_{0,m}>=Z^0 e^{-D}` and
`Z_{0,0}<=Z^0 e^D`. Positivity of the projected twisted transfer
operators supplies the nonnegative sign in (8). Finally
`e^D-1<=D e^D` proves its last upper bound. No identification
between the eigenvectors of different magnetic sectors is used.

**Theorem SC-F (PROVED from Sections 2–4).** Set

\[
 \beta_*:=\frac{1}{512\,12800^3}.
\tag{9}
\]

For `0<beta<=beta_*`, every integer `a>=3`, and all three
consumer shapes, the four sectors in L_mag are exactly the four
sectors with `p>1/2`. Every other crossed sector satisfies

\[
 p_z\le\frac{405}{2048}\sqrt{S_{\rm ev}(a;B)}
       <\sqrt{S_{\rm ev}(a;B)}.
\tag{10}
\]

Thus `(F-h)` holds with **K=1**, uniformly in size and beta in
this interval. It includes all twelve heavy crossed sectors,
including dyonic ones. It is a fixed-lattice strong-coupling result.

Proof with constants. Here `q=12800 beta<=R^2/512<1/2`.
For `a>=3`, the sequence `a^4 2^(-a^2)` decreases: its successive
ratio is at most `(4/3)^4/2^7<1`. Its initial value is `81/512<1`.
Hence `D<=D_a<1/25`, and `e^(2D)<2`.
Equations (2), (4), (7), (8) give

\[
 \begin{aligned}
 \frac{p_z}{\sqrt S}
 &\le \frac{2a^4}{25}\,
       q^{a^2}\left(\frac{160}{\beta^2}\right)^a\\
 &=\frac{2a^4}{25}
       \left(\frac{160\beta}{R^3}\right)^a
       q^{a(a-3)}
 \le\frac{2a^4}{25}(5/16)^a.
 \end{aligned}
\tag{11}
\]

The last sequence decreases, since its ratio is at most
`(4/3)^4(5/16)=80/81<1`. At a=3 it equals `405/2048`.
This proves (10). Moreover, (8) gives heavy `p<2/25<1/2`
and magnetic `p>=e^(-2D)>1-2/25>1/2`. This identifies L.
Every estimate used here holds simultaneously on the three shapes.

**Corollary SC-large (PROVED).** For each fixed `0<beta<R`,
F-h with K=1 holds on all sufficiently large consumer boxes.
An explicit sufficient threshold is

\[
 a\ge\left\lceil\max\left\{3,\frac{M}{\sigma},
                                    \frac8\sigma\right\}\right\rceil,
 \qquad \sigma=\log(R/\beta)>0,\quad M=-\log\eta(\beta)>0.
\tag{12}
\]

Indeed `4 log a<=4a<=sigma a^2/2`, so
`D_a<=exp(-sigma a^2/2)/25<1/25`. Also

\[
 \frac{p_z}{\sqrt S}
 \le\frac{2}{25}
       \exp(4\log a-\sigma a^2+Ma/2)\le 2/25<1.
\]

The same bounds identify the four light sectors.
The threshold may diverge as beta approaches R; no continuation
past R has been proved. At beta=0 the transfer is rank one,
the heavy electric weights and S are both zero, and the inequality
holds by direct substitution. No ratio by S is used at that endpoint.

**ARGUED interpretation.** The mechanism is an area-versus-length
comparison. Twist dependence requires a wrapping surface of area
at least a^2. One local even excitation already gives a thermal
contribution bounded below exponentially in a. Two separated flux
tubes need not be constructed in this range. This proves the
inequality requested by F-h, not that physical picture of fusion.

## 5. What would carry this proof to order-one coupling

**PROVED sufficient test.** At any fixed positive beta, the direct
argument proves F-h with a chosen K whenever

\[
 D e^{2D}\le K\eta(\beta)^{a/2}.
\tag{13}
\]

If also `D<1/4`, (8) identifies L_mag: its weights exceed 1/2,
and the other weights are below 1/2. For the latter assertion,
`D e^(2D)<(1/4)e^(1/2)<1/2`.
The lower bound on S in (2) and (8) prove the assertion.

**OPEN sufficient supplier at order one.** For beta in a fixed
compact interval `I=[beta_-,beta_+]` inside `(0,infinity)`, a bound

\[
 \max_k\left|\log\frac{Z^k(a,a,c,d;\beta)}{Z^0(a,a,c,d;\beta)}\right|
 \le C a^p e^{-\sigma a^2},
 \qquad 1\le C<\infty,\quad p\ge0,\quad\sigma>0,
\tag{14}
\]

uniformly in beta and the three shapes, would suffice for all
sufficiently large a, with K=1. Indeed
`eta_*=min_{beta in I} eta(beta)>0` by positivity and continuity
of the one-link integrals. With `M_*=-log eta_*`,
`C a^p exp(-sigma a^2+M_*a/2)` tends to zero. For a completely
specified threshold, take a so large that `C a^p exp(-sigma a^2)<=1/4` and
`log(2C)+p log a-sigma a^2+M_*a/2<=0`; these two elementary
conditions then hold for every larger a after their derivatives
are negative. This is the same comparison as (12).

Equation (14) is a vortex free-energy estimate selecting the
magnetic light group. It is stronger than F-h and excludes other
light-group choices. It is not a reformulation of the missing
fusion theorem, nor is it established by the strong-coupling port.
The following are attempts to supply it or bypass it.

### 5.1 Analytic continuation of the twist cancellation

**PROVED limitation of the available bound; continuation OPEN.**
The vanishing Taylor coefficients in Section 3 are exact. They
give (7) only inside the zero-free disc on which the extensive
logarithm is bounded. For beta greater than R, `q^(a^2)>1`;
the same formula no longer bounds an analytic continuation.
Finite-volume positivity on the positive real axis supplies no
size-uniform complex neighbourhood or logarithm bound.

The actual activity argument also stops quantitatively. Its
majorant uses `|w(X)|<=(4|beta|)^|X|` and the root count
`400^(|X|-1)`. The geometric series used in its Step 3 has
ratio `400 (4|beta|) exp(0.06)`. Even formally continuing that
numerical majorant to beta=1 makes its ratio exceed one; the
preceding one-plaquette lemma itself has domain `|beta|<=1/4`.
This is failure of the available estimate, not divergence of the
actual expansion and not failure of (14).

Continuing by real differentiation does not restore the lost
cancellation. Differentiation under the finite integral gives

\[
 \partial_\beta\log(Z^k/Z^0)
 =\sum_p\bigl[\eta_p\langle s_p\rangle_k
                         -\langle s_p\rangle_0\bigr].
\tag{15}
\]

Bounding each bracket by two gives an error `2N |Delta beta|`
on an interval. This is of order `a^4`, whereas (13) asks for
an exponentially small number. A uniform cancellation estimate
for the *signed, summed* shift in (15) would carry the proof.
No bound on this sum is obtained here from loop identities or
the activity estimates. No new analytic neighbourhood is proved.

### 5.2 Reflection positivity and a direct seam comparison

**PROVED comparison; the desired improvement is OPEN.** Choose
the usual cocycle stacks. A basic mu-nu twist uses
`n_rho n_sigma` plaquettes, where rho,sigma are the other axes.
Each is at most `4a^2` on these shapes. A sum of all six stacks
therefore changes at most `24a^2` plaquettes. Comparing the
positive integrands pointwise gives

\[
 D\le48\beta a^2.
\tag{16}
\]

This keeps the true twisted measure but gives the wrong size
dependence for (13). Combining it with `p<=1` leaves only
`p/sqrt(S)<=eta(beta)^(-a/2)`, an exponential prefactor.

The reflection-positive gluing inequality is Cauchy–Schwarz:
the square of a mixed reflected matrix element is at most the
product of its two diagonal matrix elements. Gluing two equal
Z_2 twists cancels the twist of the doubled region, but does not
subtract its vacuum eigenvalue. It therefore does not turn that
inequality into a lower bound on `Z_{0,0}-lambda_0^a`.
This reproduces the precise failed step already identified in
`gap-es1-opus.md` Section 6, now with the numerical loss (16).
It is not a no-go theorem about other uses of reflection positivity.

### 5.3 A bounded Polyakov trial function: the variance half

**PROVED consequence of the prior local density comparison.**
At fixed finite beta, the second LOC estimate has a constant
independent of the winding length and the spatial volume for a
simple Polyakov loop. More generally let chi have k nonzero bits,
`1<=k<=3`. Choose one simple winding loop in each of those
directions, with distinct edges, and set

\[
 f(U)=\prod_{j=1}^k\operatorname{tr} H_j(U).
\]

It is real, bounded, gauge invariant and in the chi sector.
Choose one edge from each loop. These edges enter no other chosen
loop. Conditional on all other links, their k holonomies are
independent Haar variables before inserting pi's density.
The prior note's local comparison, (2)–(4), gives a conditional
density at least `exp(-12k beta)` relative to product Haar:
the chosen edges meet at most `4k` spatial plaquettes, and the
log-density oscillation is at most `2beta(4k)+4beta k`.

Haar SU(2) has `E(tr H)^2=1` and `E(tr H)^4=2`.
For example `chi_(1/2)^2=1+chi_1` and character orthogonality
give both identities. Thus the conditional Haar moments of f
are `E f^2=1`, `E f^4=2^k`. Write `m_2=E_pi f^2`.
For every exterior configuration,

\[
 E_{\rm Haar}(f^2-m_2)^2
    =(2^k-1)+(1-m_2)^2\ge2^k-1.
\]

Integrating the conditional density lower bound proves

\[
 \operatorname{Var}_\pi(f^2)\ge e^{-12k\beta}(2^k-1),
 \qquad
 \|f\|_\infty^2\|f\|_2^2
 \le\frac{16^k e^{12k\beta}}{2^k-1}
                      \operatorname{Var}_\pi(f^2).
\tag{17}
\]

This controls c_2 for `beta<=beta_+`, independently of loop
length. It needs no clustering assumption. It does not compare
the trial energy with the lowest chi-sector energy.

**OPEN first LOC estimate.** Positivity gives only

\[
 (1-r_\chi)\|f\|_2^2\le\operatorname{Dir}(f)\le\|f\|_2^2.
\tag{18}
\]

Thus a supplied `r_chi<=1-kappa`, with kappa positive and uniform,
would give `c_1<=1/kappa`. Without it, the upper estimate here
gives `c_1<=1/(1-r_chi)`, which can grow without bound.
The issue is specifically the near-minimizer estimate when
`r_chi` approaches one. The variance bound does not solve it.
Using the lowest eigenfunction instead makes c_1 equal to one,
but (17) no longer applies to that different function.
No claim about its supremum or squared variance follows.

**PROVED finite-beta repair of the exponential remainder.** The
existing local witness also supplies the extra input missing from
the pure-power inference in row 754. If the two LOC estimates
hold, (1) and (2) imply, for `0<S<=1`,

\[
 p_\chi\le 2\Theta_\chi S^\gamma,\qquad
 \gamma=\frac{1}{4c\max\{1,M\}},\qquad
 M=-\log\eta(\beta).
\tag{19}
\]

Indeed `S>=exp(-Ma)` implies
`exp[-a/(4c)]<=S^(1/(4cM))`. Both powers in (1) are at most
`S^gamma`. This proves (19), retaining the explicit dependence
on beta, c and Theta. For S>1, `p<=1` covers the estimate after
enlarging K to at least one. It does not contradict the kernel
counterexample in the check: that kernel lacks the Wilson witness
lower bound (2) with eta bounded away from zero in its parameter.

Uniform c, Theta and M on an actual family would therefore make
electric LOC a pure-power supplier there. Equations (17)–(19)
leave its first inequality and Theta control open at order one.
Magnetic/dyonic comparison outside the strong-coupling argument
also remains open. No pure-power conclusion is obtained from
the first two LOC inequalities alone.

## 6. U(1) test and cutoff scope

**PROVED logical check, using `gap-crux-fp.md` 3b.3.** A method is
not refuted merely because it also works for U(1). The comparison
must satisfy its actual quantitative hypotheses and fail its
conclusion. The small-activity regime used here is compatible
with U(1) strong coupling. The centre-parity cancellation uses its
order-two centre subgroup and does not require pseudoreality.
The U(1) loop moments and convolution coefficient differ, so
its numerical constants must be recomputed; no SU(2) constant
is silently transferred to it.

The abstract spectral comparison, Fourier estimate (8) for a
chosen finite parity subgroup, and conditional implication (19)
also make sense for U(1). They assert fusion comparisons, not a
small even thermal sum or a gap. Therefore their extension to
U(1) does not fail Proposition T1. In particular the additional
small-even-sum and light-sector inputs in FUSE-suff remain needed.
The strong-coupling activity hypothesis is not asserted in the
U(1) Coulomb regime. No recalled numerical transition is used.

**PROVED scope of the constants.** The bounds are uniform in
the number of sites at the indicated bare Wilson couplings.
The displayed constants do not give uniform control along the
ultraviolet trajectory.
The witness (2) measures one microscopic time step. Its explicit
eta tends to zero as beta tends to infinity, and (17)'s c_2 grows.
Then M and the loss in (19) need not stay bounded. A fixed physical
box with an increasing number of microscopic links is not a
fixed-coupling application of these results.

**OPEN extension required by the consumer.** A use at an effective
order-one coupling must identify the actual coarse transfer
operator and retain its extra interactions. Calling its coupling
order one does not make its kernel a bare Wilson kernel.
One needs either (13) with a lower thermal witness on the matched
physical scale, or the actual bounded LOC near-minimizer, its
trace factor and the missing twisted-sector comparison, all with
constants uniform in the cutoff. Neither has been constructed here.

## 7. Source record and final checkpoint

The Sussman–Alpoge outline and CA-I were fetched once at
`31a47c543775`, to `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`.
I used the SA-index README, matching chunk rows and neighbours,
and obligations before reading the source. The pertinent reads
were SA 588–599, 1150–1174, 1271–1347, 2195–2257 and 2313–2336.
GL3 and GL8 give one-link and transfer provenance. The polymer
theorem is conditional on its activity criterion; its words are
“The estimate on the activities remains a separate analytic task.”
The gap passage requires an additional positive spectral estimate.
None of those passages supplies (F-h). The CA 4.12–4.19 index
has no match for fusion, thermal sums, twisted sectors, Polyakov
loops or electric flux. No whole-account absence claim is made,
and no CA-I proof is imported.

A supplementary broad main grep was stopped after unrelated
substring hits; it is not recorded as a completed absence search.
The cited main and PR passages, rather than that grep, support
the reuse decisions above. Input-blob checks against the assigned
commit and the output bookkeeping are recorded in
`/tmp/gap-fusion-astra-20261112/source-manifest.json`.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex
as the authors of their text**, for the outline/account material.
The local witness is Codex's earlier soft-route result.
The strong-coupling polymer estimates are the existing Opus and
Fable results cited above, using Dobrushin's criterion and the
Osterwalder–Seiler method. Theorem V and FUSE-suff are Opus's;
the crossing reduction is Fable's. Their proofs and checks retain
their own stated premises and scope.

**PROVED here from those inputs, not independently checked:**
the signed-activity port and winding-area estimate (5), the
size-uniform strong-coupling F-h bounds (10), (12), the variance
consequence (17), and the finite-beta conditional repair (19).
The spectral lower bound (2) reuses the earlier local witness.

**OPEN:** F-h at order-one coupling with the required cutoff
uniformity; the near-minimizer half of LOC in that regime; the
remaining light-sector and small-even-sum inputs for FUSE-suff.
The three routes tried were complex continuation, reflection-positive
seam comparison, and a local Polyakov trial function. Their exact
losses are (15), (16), and (18), respectively. A useful next step
must improve one of those losses on the actual family, rather than
repeat the already available local witness or fixed-box example.

No numerical run, enumeration, interval computation or machine
certificate discharged a statement. No pre-existing source, queue, registry,
ledger or audit file was changed. The output is also preserved in
the isolated worktree `/tmp/gap-fusion-astra-20261112/worktree`,
branch `codex/gap-fusion-astra-39b239180`; the supplied checkout's
git metadata points to another worker's worktree, so it is not used
for staging or commits.

RESULT: PROVED from the cited inputs: F-h with K=1 for all a>=3 when 0<beta<=1/(512*12800^3), and for sufficiently large a at each beta<1/12800, including all twelve heavy crossed sectors; PROVED the finite-beta variance and conditional LOC refinements (17), (19); OPEN at order-one coupling with cutoff uniformity. No mass gap or scientific status is granted.
