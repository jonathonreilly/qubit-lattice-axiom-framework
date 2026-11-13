# Repo search

Completed check for FINISH row 873, `gap-filter-ls-check-astra`.
This is research text; it grants no scientific or audit status.
The statement verdicts below were saved as the check proceeded.

Checked by Codex (row requests gpt-6-astra, xhigh), 2026-11-13, at
`1b56f64050915487de4c1afd0c6e41685cd8fb6b`. Research check, not an audit.
Only this output is edited. No simulation or computer-assisted proof is used.
The task-specific prior file is absent. This is the requested check of row 872,
not a new attack on EXC. No matching owner was found in `open-registry.md`
for `gap-filter`, `EXC-W`, `one.slice`, `odd.sector`, `spin.5/2`, or `E17`.

Unqualified source line numbers below refer to `gap-filter-ls-opus.md`.
Local abbreviations: Q = `gap-q8test-opus.md`; QC =
`gap-q8test-check-astra.md`; H = `gap-hs-max.md`; EX =
`gap-expose-astra.md`. All are in this lane's `library/`.
The external soft-route prefix S is
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.

## Search evidence and scope

The full-repository searches used `git grep -n -i -E`, `*.md`, `*.tex`, and
`head`, on all five requested refs, including paths outside this lane:

| Ref | Revision read |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Terms: `gap-filter-ls|Proposition EXP|wrapping Wilson line|excess.high.spin|
log.derivative.{0,45}parity|EXC.{0,20}E17` (cap 60, seven lines returned).
A second completed search used `high.spin.{0,45}(filter|excess|winding)|
spin.5/2|EXC-W|log.derivative.{0,35}(transfer|sector)|
state.blind.{0,30}volume` (cap 50, four lines returned).
Neither found the target statement or its boost-response method.

The false positives were:
- `docs/EXPONENTIAL_SCALAR_FINITE_BODY_BOUNDED_THEOREM_NOTE_2026-10-14.md:400`
  on all five refs: a count of canonical excursions, unrelated to EXC.
- `pr/10114` and `pr/10133`, `S/CODEX_REVIEW_UIR.md:64`:
  the zero-momentum density is a trace-log derivative, whose integral vanishes;
  parity removes a linear momentum term. This is a momentum/tadpole argument,
  not a derivative with respect to a high-spin fugacity in a flux sector.
- The same refs, `S/REALRGA.md:493` and
  `S/checks/realrga_review_source_v1.md:487`: real logarithmic derivatives and
  moving-sector regularity require H1–H3. These concern real RG fibres, not
  the winding-sector transfer or EXC.
A preliminary broad `parity.sector` search reached its cap in unrelated
fermionic and Regge material. It supplies no negative coverage claim.

The reusable November 8 digest concerns earlier UV/history targets, not this
November 13 check. The relevant *local* prior result is
`gap-expose-astra.md:575–627`: (E17) is explicitly unproved; (E18) bounds
`p(t)` by `exp(2 beta |P| t) Tr(P_- K^t)/Tr K^t` using eigenvalue comparison.
Its extensive-cost warning is already established there, and is credited here.
The present check does not rebrand that warning as a new obstruction.

The prior digest also locates the soft-route
`pr/10114:S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:1–166`, read here.
Its section 1 gives `exp(-2 beta b)<= [psi(U)/psi(U')]/[A(U)/A(U')]
<=exp(2 beta b)` when b edges change. Section 2 gives a volume-independent
positive one-step loop correlator for the unboosted Wilson transfer.
These are relevant positivity/normalization foundations, not a winding
fraction, EXC estimate, or boosted-kernel comparison. Its stated
strong-coupling endpoint has beta<=1/32, outside the requested window.
Credit that existing Codex construction; no duplicate check is claimed.

Index-first source reading: `sa-index/chunk-02.md:80–107` identifies the
one-bond convolution, GL3, the positive transfer, and GL8. Read
`YM4_sketch_500.tex:2195–2257,2313–2371`: GL3 gives
`c_j=2 exp(-beta) I_(2j+1)(beta)/beta>0`, with factorial decay; GL8 gives
`Z=Tr L^s` for the gauge-projected half-kernel transfer. Normalizing by `c_0`
gives the `r_j` used here. These are existing foundations, not new results.
The targeted index/obligation search found no high-spin EXC or odd-winding
response theorem. It does not prove absence under every possible name.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text. Their source revision `31a47c543775` is supplied by the task;
the on-disk source folder has no Git metadata to re-verify that revision.
No Balaban estimate is used to discharge any statement in this check.

## 1. Proposition EXP — HOLDS

Source: `gap-filter-ls-opus.md:128–160`, with its Step 7 positivity repair
at 338–342. Fix a finite spatial torus, beta>0, and integer t>=1. Put
`N=N_hi`, `c=z^|E|`, and `Z_sigma(s)=Tr(P_sigma L(s)^t)`.
The input definitions were read at `gap-expose-astra.md:89–153`.

Here is a direct check avoiding the author's nonsymmetric `KB` manipulation.
For s>0, `L(s)=s^(N/2) L(1) s^(N/2)`, since N commutes with K(1).
N is bounded by |E|, so differentiation is valid in trace norm and

    s L'(s) = (N L(s) + L(s) N)/2.

The sector projector commutes with L and N. Differentiating the integer
power and cycling the trace therefore gives, in each sector and in their sum,

    s Z_sigma'(s) = t Tr(P_sigma N L(s)^t),
    d log Z_sigma / d log s = t <N>_(sigma,s).

The numerator is nonnegative: it is the trace of
`L(s)^(t/2) P_sigma N L(s)^(t/2)`. No commutation of N with B is needed.
Thus each *unnormalized sector trace* is nondecreasing. This does not give
monotonicity of p or the sign of Delta.

K(s) is positive trace class, B is bounded and strictly positive, and the
closed cut commutes with both. This proves (a). At s=0, use the normalized
spin-1/2 character on a simple wrapping line for the odd sector, and the
constant function for the even sector. Both lie in the low subspace;
`<psi,L(0)psi> >= c exp(-beta|P|)<psi,K(0)psi> > 0`.
Spectral Jensen gives `<psi,L(0)^t psi> >= <psi,L(0)psi>^t`.
Hence both constant terms Z_sigma(0) are positive.
Cyclicity gives `Z_sigma(s)=c^t Tr(P_sigma(K(s)B)^t)`, a polynomial in s.
Its logarithmic derivative stays finite at zero. Subtracting the two
logarithmic derivatives proves (c), including the integrable s=0 endpoint.
This checks (a)–(d); it asserts neither EXC nor confinement.

## 2. Lemma 3.1 — HOLDS AFTER CORRECTION

Source: 164–173. The conditional-expectation identity is right. The last
summand must be `1{j_e in {5/2,7/2,...}}`, not `1{j_e>=5/2}`.
The printed indicator also selects integer spins 3,4,..., which N does not
count. Equivalently sum `1{e in C, j_e>=5/2}`. This is a correction to the
formula, not a new estimate.

For a joint spin projection E_j, define
`mu_s(j)=Tr(E_j L(s)^t)/Tr L(s)^t`. These numbers are nonnegative and sum to
one, since the trace equals `Tr(L(s)^(t/2) E_j L(s)^(t/2))`.
Gauge invariance forces an even number of half-integer edges at each vertex;
the cut parity is the indicator O of odd winding. Thus

    Delta = E_s[N O]/p - E_s[N] = Cov_s(N,O)/p.

Expanding N as the sum of the corrected indicators proves the last equality.
The same proof gives `Delta=(1-p)(E_s[N|O]-E_s[N|1-O])`.
In particular Delta has no determined sign. The phrase “avoids the filter”
here describes an excess count; it does not identify a zero-high-spin event
or give its probability.

## 3. Proposition 3.2 — HOLDS AFTER CORRECTION at its consumer

Source: 176–198. Write `I=integral_1^s* Delta(s) ds/s`. EXP gives exactly

    p(1) = p(s*) exp(-a I),       0 < p(s*) <= 1.

Thus (a)'s displayed bound holds: EXC yields `p(1)<=exp(-c0 a)`, namely
an exponential estimate with `C=1`, polynomial exponent zero, and
`eta_new=exp(-2c0)`. EXC-W gives
`p(1)<=exp(-delta log(s*) a L_i)`. These constants are correct.
Part (b)'s equivalence with the relative bound is exact.
Part (c) follows from
`a I=log p(s*)-log p(1)<=log(1/p_min)`.
The resulting statement “EXC fails” requires a family with unbounded a,
fixed p_min>0 and uniform c0>0. A finite set of boxes gives no contradiction.

**HOLDS AFTER CORRECTION as an implication to the named consumer (E17)/(FQ).**
The eta in `gap-expose-astra.md:585–599` is tied to the *existing* lower bound
`S_ev>=eta_0^a`; see also `gap-ext-astra.md:110–128`. One cannot replace it
by the larger `eta_new` merely because EXC supplies that decay rate.
To use only these two exponential estimates in FQ requires

    c0 >= -log(eta_0)/2,

or a new matching lower bound for S_ev. Indeed their ratio is bounded only by
`exp(a[-c0-log(eta_0)/2])`, which a polynomial cannot absorb if its exponent
is positive. Decreasing eta_0 preserves its lower bound but worsens this
comparison. EXC-W does beat every fixed exponential lower-bound rate for
large a, since L_i>=a. Thus the algebraic exponential bound holds as printed;
the unrestricted claim that any positive EXC constant carries the original
consumer needs this rate condition. This check supplies neither rate.

The words “exactly when the filter carries (E17)” are valid only if “carries”
means this particular relative-response proof. They do not prove that every
possible use of the filter requires EXC. Even an exponentially small p(1)
can have p(s*)=p(1), hence I=0. For example a sector transfer independent of s
tensored with an identical boosted factor in both sectors has this property.
Consequently EXC is an additional comparative condition; E17 alone says
nothing about the boosted endpoint. No order-one SU(2) counterexample to EXC
is constructed here.

## 4. Avoidance constructions — HOLDS, with a cost correction

**A, 201–211: HOLDS with the simple-path correction already recorded at 343.**
Let gamma be simple and cross the cut an odd number of times. Its normalized
fundamental character is bounded, gauge invariant, and odd under Theta.
Hence multiplication sends the even sector into the odd sector. Each used
edge undergoes `j tensor 1/2=(j-1/2) direct-sum (j+1/2)` once, omitting
the negative-spin term when j=0. Integer
j<2 cannot become high; integer j>=2 can; a high half-integer j becomes
integer and ceases to be high. Other edges do not change. This proves the
printed support bound. The constant state maps to the nonzero spin-1/2
wrapping loop, with N=0. Nothing here says that this image has large norm
under the Gibbs law, or is the lowest odd state. The already proved one-edge
0.275 bound is an unconditional s=1 estimate for beta<=2.5, not an estimate
conditional on odd winding or uniform along the boost.

**B, 213–214: HOLDS as the existing single character-expansion term.**
The corrected normalization is `2 z^N_p r_(1/2)^(a L_i)` for the unshifted
partition difference, as `gap-q8test-check-astra.md:512–527` already records.
It is not a lower bound on the entire normalized sum. No separate proof of
that existing term is claimed here.

**C's positive trace and monotonicity, 216–217: HOLDS.**
Let Q be the all-low projection. Then `K(0)=Q K(1)` and
`L(0)=Q L(1) Q`; consequently `L(0)^t` inserts Q at every step. EXP and its
Step 7 repair give `0<Tr(P_- L(0)^t)<=Tr(P_- L(1)^t)`.
This establishes a nonzero high-free odd subspace for every time period.

**C's “cost of avoidance”, 218–219: HOLDS AFTER CORRECTION.**
The equality `log p(1)-log p(0)=t integral_0^1 Delta(s) ds/s` is exact.
Call it the *relative change of the odd fraction under truncation*.
It is not the negative log of the one-slice avoidance probability, and need
not be nonnegative. The actual one-slice avoidance probability is
`Tr(Q L(1)^t)/Tr L(1)^t`, not `Tr(L(0)^t)/Tr L(1)^t`.
For t=2, writing L in Q/(1-Q) blocks gives

    Tr(Q L^2) = Tr((Q L Q)^2) + Tr(Q L(1-Q)L Q).

The second term is `||(1-Q)LQ||_HS^2` and is generally positive when B
mixes low and high spins. This distinguishes one-slice avoidance from
compression at every step. Positivity of one-slice traces does not provide
a positive joint classical spin history: the existing warning is already
in `gap-q8test-check-astra.md:439–447`.
Even if such a history measure were supplied, the log ratio would compare
avoidance in the odd sector with avoidance in the full ensemble, rather
than give either absolute cost. Thus the existence of avoiding states does
not bound their thermodynamic weight or disprove EXC.

## 5. Step 5.1, exact rescaling — HOLDS

Source: 255–258. For a projection H,
`s^H=I-H+sH`; applying this to each commuting edge projection gives
`K(s)=s^N K(1)`. Taking commuting positive square roots gives exactly the
printed L(s), with its `z^|E|` factor retained. At s=0 interpret `0^N` as
the projection onto N=0, rather than use a logarithm. This also supplies
the direct differentiation in section 1 above.

## 6. Step 5.2, large-time interpretation — HOLDS AFTER CORRECTION

Source: 260–266. The eigenvalue derivative holds for a simple sector top:
Hellmann–Feynman and `sL'=(NL+LN)/2` give
`d log lambda_sigma/d log s=n_sigma=<psi_sigma,N psi_sigma>`.
The alternative isospectral operator must be
`z^|E| B^(1/2)K(s)B^(1/2)`; line 262 drops this scalar.
With its normalized eigenvector phi, the matching normalized psi is
`z^(|E|/2) K(s)^(1/2) B^(1/2)phi/sqrt(lambda_sigma)`.

The claimed limit of Delta needs **lambda_+>lambda_-** in addition to simple
sector tops. With fixed spatial volume and simple tops the actual limits are

    lambda_+ > lambda_-: Delta -> n_- - n_+;
    lambda_+ < lambda_-: Delta -> 0;
    lambda_+ = lambda_-: Delta -> (n_- - n_+)/2.

These follow by dividing each sector's trace and inserted trace by its top
eigenvalue to the power t. The trace-class tails vanish in this division.
At s=1 the usual strictly positive Wilson kernel supplies an even Perron
ground state. At boosted s, positive *operator* does not mean pointwise
positive *kernel*. The note proves no corresponding sector ordering there.
For the logical omission, the two scalar sectors `lambda_+=1`,
`lambda_-=r s`, `0<r<1`, already have simple tops but reverse order when
s>1/r. Their odd n is 1, even n is 0, whereas Delta tends to zero there.
This is a counterexample to the stated spectral inference, not a Wilson
counterexample.

Finally, a fixed-box limit t->infinity does not justify the joint limit
`t=a`, with spatial sizes also growing. With the extra ordering, integration
of the eigenvalue derivative measures the drop of
`log(lambda_+/lambda_-)`. Identifying the finite-time EXC integral with that
drop additionally needs control of the trace-to-ground-state error. No such
uniform control is supplied. The finite-time identity EXP remains exact.

## 7. Step 5.3, state-blind volume bound — FAILS as written

First failing line: 271, `L(s)<=s^|E| L(1)`.
Congruence by `s^(N/2)` does not preserve that proposed comparison when N
and L(1) fail to commute. A hand counterexample to the inference uses

    N=diag(0,1), K(1)=diag(1,k), B=[[1,b],[b,1]],
    k>0, 0<b<1, s>1, c=1.

These are positive transfer ingredients of exactly the algebraic form used
in the inference. Then

    s L(1)-L(s) = [[s-1, b sqrt(k)(s-sqrt(s))],
                   [b sqrt(k)(s-sqrt(s)), 0]],

whose determinant is `-b^2 k (s-sqrt(s))^2<0`. Thus it is not positive.
This small example refutes the asserted consequence of 5.1; it is not a
counterexample to SU(2) confinement. In a larger space the same obstruction
occurs whenever a maximal-N block couples to a lower-N block.

That obstruction also occurs in the actual untwisted Wilson transfer, at
every beta>0. Put n=|E|. Choose every straight coordinate circle on the spatial torus,
and let psi be the product of their spin-5/2 characters. Each edge occurs
once. Thus psi is gauge invariant, every edge has spin 5/2, and N psi=n psi.
It is nonzero at the identity configuration. Let R project onto N=n.
Every vector in R is odd under the sign flip J_e of each individual edge.
But B psi is not: near the identity, flipping one edge changes its four
spatial plaquette signs, and at the identity `B(U^e)/B(U)=exp(-8 beta)!=1`.
Since psi is nonzero there and continuous, `(1-R)B psi!=0` in L2.
The commuting, injective K(1)^(1/2) then gives `(1-R)L(1)psi!=0`.
For `D=s^n L(1)-L(s)`, one has `RDR=0`, whereas

    (1-R)D psi = sum_(m<n) [s^n-s^((n+m)/2)] 1_{N=m} L(1)psi != 0.

If D were positive, `<psi,D psi>=0` would force D psi=0, a contradiction.
All these vectors stay in psi's global parity sector because L commutes
with Theta. Thus the printed operator inequality fails on its actual
Wilson domain as well; no numerical step is involved.

**Corrected spectral statement: HOLDS.** For s>=1 and n=|E|,
`K(1)<=K(s)<=s^n K(1)`. Congruence with B^(1/2) gives

    A(1)<=A(s)<=s^n A(1),  A(s)=z^n B^(1/2)K(s)B^(1/2).

A(s) and L(s) have identical nonzero spectra in each parity sector: they
are XX* and X*X for `X=z^(n/2)B^(1/2)K(s)^(1/2)`.
The min–max principle therefore gives, for every ordered sector eigenvalue,

    lambda_(sigma,k)(1)<=lambda_(sigma,k)(s)<=s^n lambda_(sigma,k)(1).

In particular the printed top-eigenvalue upper bound survives. Summing powers
gives `Z_sigma(1)<=Z_sigma(s)<=s^(nt)Z_sigma(1)`. Independently of spectral
comparison, EXP and `0<=N<=n` give `|Delta|<=n`, hence
`|log[p(s)/p(1)]|<=nt log s`. These are valid extensive estimates.

**“Only” / “any argument bounds separately”: FAILS as an obstruction.**
From only positivity and `0<=N<=n`, the coefficient n can be sharp: a
one-dimensional sector with N=n and B=1 has lambda(s)=s^n lambda(1).
That proves sharpness for this stripped algebraic class. It does not prove
optimality among arguments using the Wilson action, locality, cancellations,
or relations between sectors. Equal high-spin factors in both sectors can
cancel exactly. The existing EX (E18) already records the crude extensive
comparison. Correct wording: “This crude comparison loses a volume factor;
this variational attempt supplies no lower bound on the excess response.”
For lambda the factor is `s^|E|`; for a t-step trace it is `s^(t|E|)`.

## 8. Localization dichotomy, including Steps 5, 6 and 8a — FAILS

Source: 276–299, 314–317, 377–382, 402–405, 426–429, and the final RESULT.
This verdict rejects the claimed inference and necessity, not the physical
possibility of flux localization.

**Conditional scaling: HOLDS AFTER CORRECTION.** If a proved bound were
`Delta(s)>=delta_0 L_i`, uniformly in geometry and s in [1,s*], with
`delta_0>0`, EXP would give EXC-W and an area exponent. A bounded-width
support statement alone gives at most an O(L_i) *upper* bound on a sum of
bounded local changes. It supplies neither its sign nor a positive lower
bound. The approximate formula in 278 cannot replace the stated uniform
inequality. For EXC only the integral must be positive; positivity at every
s is sufficient, not necessary.

Likewise an actual uniform estimate
`|Delta(s)|<=C L_i/A_perp`, with fixed s*, would give an integral O(1/a)
on the stated aspect ratios. The dimensional multiplication is right.
Its local second-order premise is not derived.

**The original symmetry argument and Step 6 repair fail.** The centre of
SU(2) multiplies a spin-j block by `(-1)^(2j)`; it does not implement the
printed `m -> -m` transformation or a continuous signed flux parameter.
Nor does `<E_e^a>=0` imply that gauge-invariant data change only quadratically.
Take any two gauge-invariant states with different high-spin probabilities
and mix their density matrices as `(1-epsilon)rho_0+epsilon rho_1`.
Both have zero electric-vector mean, while the high-spin probability changes
linearly in epsilon. A constant state and a character of a high-spin closed
loop give explicit finite-spin examples. Thus line 297's “so” is invalid.

**Step 8a does not fix the missing estimate.** No quantitative meaning of
“weakly correlated”, uniform high-order mixing estimate, or bound along the
boost is supplied. Even vanishing correlations of every proper subset of
M bits do not control their parity. For `0<q<1`, the probability law

    mu_q(x)=2^(-M)[1+(1-2q)(-1)^(x_1+...+x_M)]

has independent fair marginals on every proper subset, but odd parity has
probability exactly q. Summing over any missing bit cancels the parity term;
summing over odd strings gives q. One may choose q exponentially small,
order one, or near one. This is a hand test of the claimed probabilistic
inference, not a replacement Wilson model.

The two pictures are not an exhaustive mathematical alternative. Intermediate
scales, correlations at global parity order, and spatially distributed small
changes are not excluded. E17 bounds a single sector weight; it imposes no
conditional geometry within that sector. EXC constrains a spatially summed
covariance. Neither statement alone requires a tube, and no theorem here
makes localization necessary for every proof of EXC.

Step 5's withdrawal of the exponentially-small-*total*-response claim is
correct: a per-length dressing contribution, even with a tiny fixed
coefficient, grows with L_i. The further assertion that EXC therefore
“presupposes localization” does not follow. EXC remains open. The proposed
N1–N3 inputs may be research directions; they are not established necessary
conditions or an obstruction to using the filter.

## 9. Crossover and dressing sizes, with Step 8a — FAILS as bounds

**Kinetic coefficients and revised arithmetic: HOLDS as GUIDE arithmetic.**
At the supplied rounded beta=2.3 values,
`2(0.4793)=0.9586`, `6(0.001846)=0.011076`, and
`0.4841/0.001846` is about 262. The Step 5 correction from 0.49 to 0.484
is consistent with Q's exact finite-group formula. The resulting log is
about 5.57. These are coefficient values, not surface-tension bounds.
The quoted densities are the unverified finite-volume measurements in
`gap-hs-max.md:149–158`; this check does not certify that simulation or
its interpretation as a thermodynamic or ground-state value.

**Step 4 rigidity and the corrected “new channel” estimate: FAILS.**
Lines 225–233 infer free energies from bare character coefficients. A single
spin-5/2 plaquette can translate a straight spin-5/2 flux segment in one
specified move. That does not exhaust its propagation or dressing. Even a
fundamental spatial plaquette multiplies j=5/2 into j=2 or j=3 on shared
edges, and repeated moves and other representations are present in B.
No convergent expansion bounds their sum, multiplicities, or normalization.
The bare cost `-log r_V^(2T)` consequently gives no stated lower bound for
its effective tension. Nor does the recalled 0.14 establish the other
channel's tension here.

Even assuming the two quoted tensions, comparing one added numerator term
with one old term is not the response of the full normalized fraction:

    a integral_1^s* Delta ds/s
      = log[Z_-(s*)/Z_-(1)] - log[Z_all(s*)/Z_all(1)].

The boost changes every high channel and the vacuum, not just a single flat
plane. Step 5 correctly retracts exponential smallness of the *whole*
integral. Its residual `exp(-0.58 A)` estimate for the new channel is still
an unsupported model estimate. It does not establish order-one avoidance.

**Step 8a branching formula and “bracketing”: FAILS.**
First failing step: 391–392. A dimension fraction is not the branching
probability of multiplication by a Wilson loop in an arbitrary physical
state. There is a direct gauge-invariant hand counterexample. With W the
holonomy of a simple closed loop, the unit Haar spin-network state
`psi_j=chi_j(W)` satisfies

    w_gamma psi_j = (chi_(j-1/2)(W)+chi_(j+1/2)(W))/2.

The two characters are orthogonal, each of norm one. After normalizing the
image, each branch has squared norm 1/2. For j=1, the printed fraction is
2/3; for j=2, it is 6/10. Both disagree with 1/2. Clebsch–Gordan gives the
allowed support, as in Construction A; it does not give that universal
norm fraction. Such dimension ratios require a specified isotropic average,
which the correlated Wilson-loop multiplication does not provide.

The second “vacuum-ratio” accounting is another guess, not an opposite
variational bound. Two estimates of opposite signs do not bracket the true
Delta. Neither accounting controls the normalization of `w_gamma psi_0`,
identifies it with the odd ground state, or gives the s-dependent data on
[1,s*]. The source's finite-torus s=1 densities supply none of those steps.
In particular their smallness cannot bound the integral over a boost of
about 262. The asserted monotone growth of the specific j=5/2 density in
line 239 is not established by EXP's monotonicity of sector traces.

The numerical operations behind the revised guides are consistent:

    (2/3)(0.0347)-0.00126 = 0.021873333...;
    0.0347(0.008)-0.00126 = -0.0009824;
    (6/10)(0.000021) = 0.0000126.

Using the supplied logarithms gives approximately 0.057 for the first
quantity times log(13.6), and at most about 0.000070 for the last times
log(262), before the indicated subtraction. This explains the *reported*
scales. It establishes no bound on Delta, no “at most a few hundredths”,
and no percentage of the area exponent. The revised spin-3/2 estimate is
larger than the spin-5/2 guide, but neither is a validated estimate of the
actual filter contribution. The recalled string tension 0.14 is not checked.

**Step 8a's environment correction: HOLDS with its precise object.**
Read H:106–119,149–158 and `gap-sep-opus.md:458–482`. The measured 0.267
is `e_(1/2)=E_nu[chi_(1/2)]/2`. DS bounds this coefficient in absolute value
by `r_(1/2)(5 beta)`; QS bounds it by
`E_nu[product_i r_(1/2)(beta rho_i)]<=r_(1/2)(5 beta)^4`.
Thus comparing the same coefficient with the stated one-link and four-link
upper bounds is legitimate. The number 0.267 is *not* a measurement of the
intermediate QS upper bound `E_nu[product_i r_(1/2)(beta rho_i)]` itself.
Step 7's contrary repair is superseded by Step 8a. A typical-value upper
bound for that intermediate quantity remains unsupplied.

**Strong-coupling sentence: HOLDS only as a flat-term comparison; FAILS as EXC.**
The existing Q:241 expansion is
`r_V^(2T)-r_(1/2)=beta^5/7680+O(beta^7)` and `r_(1/2)=beta/4+O(beta^3)`.
Hence `log(r_V^(2T)/r_(1/2))=beta^4/1920+O(beta^6)`.
The ratio of those two specified flat-plane weights is indeed
`exp[-A(beta^4/1920+O(beta^6))]`. No uniform expansion of both complete
partition functions is supplied, and a comparison of flat terms gives no
pointwise lower bound on Delta(s). It therefore proves neither EXC-W nor
that the actual filter carries that amount of area exponent, even at small
beta. The source itself disclaims a cluster-expansion proof.

## 10. Inherited filter, group tests and final claims

**Statement F1–F3: HOLDS as the stated inherited input and its placement.**
Q's Theorem 3.4, Corollary 3.7 and QC's kinetic-placement check are existing
work. On high blocks `C_hi<=M Pi_hi`; tensoring does not remove B_m or its
mixing of spins. The kinetic boost used here changes K and keeps B fixed.
It does not turn the full transfer into a Q_8, 2T, or U(1) transfer.
No already-completed filter theorem is re-proved in this check.

**F4: HOLDS AFTER CORRECTION of “first V-channel”.** Read it as the first
*additional* V-copy beyond the fundamental spin-1/2 carrier: spin 5/2 for
2T, spin 3/2 for Q_8. Literally both already have V at spin 1/2. The
statements that the high-block inequality supplies no low-block estimate,
no population estimate, and no whole-transfer comparison are correct.

**Step 7 group tests / Step 8a high-prime extension: HOLDS AFTER CORRECTION.**
For positive s, the EXP differentiation, monotonicity, covariance identity,
and Proposition 3.2's algebra work for any chosen centre-odd irreducible
blocks with positive convolution eigenvalues. The SU(2) high-prime set
`{3/2,5/2,...}` retains a spin-1/2 wrapping state, so its s=0 endpoint is
also valid. But “any set of blocks, any group” does not preserve that
endpoint. For Q_8, selecting its sole centre-odd irrep V removes every odd
edge at s=0. Then `P_- L(0)=0` and `p(0)=0`, so the finite log identity at
zero and Construction C's strict positivity fail. Retain s0>0, or assume
a nonzero retained odd subspace. The same issue occurs when every odd
block is selected in the other groups.
The group phase statements in the table are explicitly recalled expectations;
no proof of their limiting p, and no Villain-to-Wilson bridge, is supplied.
Only the conditional assertion “p bounded below as a grows excludes EXC”
is checked here. This does not refute the actual SU(2) filter hypothesis.

The note's closing statements resolve as follows. Their repeated formulations
in Step 8b and RESULT have the same verdicts, not additional evidence.

| Statement | Verdict | Exact surviving content or failure |
|---|---|---|
| EXP (a)–(d) | HOLDS | Positive sector traces, exact derivative and integral, monotonicity of unnormalized traces; Step 7 repairs s=0. |
| Lemma 3.1 | HOLDS AFTER CORRECTION | Keep half-integer membership in each high indicator. |
| 3.2(a), as a bare exponential estimate | HOLDS | p(1)<=exp(-c0 a); EXC-W gives the stated area exponent. |
| 3.2(a), as the original E17/FQ consumer | HOLDS AFTER CORRECTION | Match c0 to the existing S_ev rate, or supply a stronger lower bound. |
| 3.2(b) | HOLDS | Exact equivalence with the relative endpoint ratio; “carries” must mean this response route. |
| 3.2(c) | HOLDS | Its inequality holds; failure of uniform EXC follows on an unbounded-a family. |
| A and B | HOLDS | Simple-path support map and the existing normalized flat-term example, without a weight bound. |
| C trace assertion | HOLDS | The all-low compressed odd transfer is nonzero and has no larger odd trace. |
| C avoidance-cost interpretation | HOLDS AFTER CORRECTION | Relative change of odd fraction under truncation, not a one-slice avoidance probability. |
| 5.1 | HOLDS | Exact high-spin rescaling. |
| 5.2 | HOLDS AFTER CORRECTION | Keep the scalar z^n, sector ordering, and the fixed-volume scope; no joint-limit identification. |
| 5.3 | FAILS | Operator order is false; the spectral volume bound holds, without an optimality/no-go conclusion. |
| 5.4, Step 6 repair, Step 8a dichotomy | FAILS | No exhaustive dichotomy or necessary localization theorem is derived. |
| Step 8a norm fractions / size bounds | FAILS | Explicit loop-character counterexample; guesses do not bracket the response integral. |
| Step 8a environment correction | HOLDS | 0.267 denotes the measured environment coefficient, not the intermediate QS bound. |
| Strong-coupling full-transfer claim | FAILS | The scalar flat-weight expansion holds; EXC and EXC-W do not follow from it. |
| V-a | HOLDS AFTER CORRECTION | Exact response plus relative EXC criterion; retain the rate and route restrictions. |
| V-b | HOLDS AFTER CORRECTION | Nonzero high-free odd states; use the corrected meaning of “cost”. |
| V-c | FAILS | Entropic rigidity and exp(-0.58 A) are not controlled estimates. |
| V-d, including its Step 8a replacement | FAILS | Neither claimed magnitude bound nor percentage of tension is established. |
| V-e and the final negative conclusion | FAILS | Localization is not proved necessary; the filter is not excluded as a carrier of LS/E17. |

The check leaves EXP and the exact response formulation available, with the
repairs above. EXC, the consumer with its required rate, and localization
remain open. N1–N4 are proposals, not consequences. No mass gap, no new
scientific standing, and no obstruction to every filter-based route follows.

Not performed: simulations, numerical proof, reconstruction of previously
checked filter inequalities, a proof of the recalled phases or string tension,
a Balaban-paper import, registry/FINISH edits, commit, push, or outward post.
Only this local report was written. The pinned checkout was used as requested;
no branch or remote ref was changed.

RESULT: HOLDS — EXP and the exact conditional response algebra; HOLDS AFTER CORRECTION — Lemma 3.1, the E17 consumer rate, avoidance-cost interpretation, and the large-time reading; FAILS — Step 5.3's operator inequality and universal volume-loss claim, the localization necessity/dichotomy, the claimed dressing-size bounds, and the negative conclusion that the filter cannot carry LS/E17. EXC and E17 remain open; research check only, no status granted.
