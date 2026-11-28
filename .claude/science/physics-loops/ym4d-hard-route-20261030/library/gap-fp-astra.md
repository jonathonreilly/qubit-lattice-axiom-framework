# Repo search

The lead's `prior/repo-search-2026-11-08.md` was read in full. It is a
November 8 search, not a prior check of row 712. Its closest hit is
`pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`.
I fetched that PR and read those lines at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`. They concern a positive
one-step loop correlation and a convolution inequality, not the present
discard tests, torus covariance, twist comparison, or sphere lemma.
That result is prior Codex work and is not rederived here.
The digest's Gaussian covariance hit is a different law; its source check
is recorded below. The requested task-specific prior file is absent.
Targeted searches of `open-registry.md` found no owner of this check or
these mass-gap statements. This check does not take over any proof lane.

## Status and provenance

- Writer/checker: OpenAI Codex; dispatched as `gpt-6-astra`, max effort,
  in FINISH row 726. Model provenance here records that supplied dispatch.
- Frozen research source: `661c239dc535359263c7e929a3ab715c356e9286`.
  Rules read on fetched main: `1f20846b8057f6346ebab6c0dbebdabbd9e472a4`.
- Target: `library/gap-crux-fp.md`, row 712. Unless another file is named,
  source line numbers below refer to that file at the frozen revision.
- Research check only. No audit, status grant, or mass gap at a coupling
  of order one. No computer-assisted proof or numerical run is used.
- Scope: P1, P2; T1–T3 and their Corollary; COV, REG; Identity L, TW;
  Lemma P. This does not check the other first-principles assertions,
  Proposition V or its literature input, the Brownian-motion proposal,
  the general `(vMF-Lip)` claim, or the continuum construction.
- Complete: nine statements HOLD; T3 and its Corollary HOLD AFTER
  CORRECTION. The earlier Claude check was opened only after all eleven
  verdicts were appended. Section 12 records the comparison and differences.
- Credit: the source checked is Claude Fable 5.2's row-712 text.
  Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
  their text, supply the outline/account context. Tadeusz Balaban supplies
  the cited ultraviolet research background; none of his paper theorems
  is an input to the elementary checks below.
- Checkpoint: the assigned check and comparison are complete. Source
  revisions are fixed above. No numerical program was run. Applying
  the proposed source wording is for the lead; this output changes no
  source, registry, FINISH row, or scientific status.

## 1. P1 — HOLDS (source lines 28, 55)

Write `r = lambda_1/lambda_0`, `m = -log r`, and take `0 < t < 1`.
The nonnegative spectral sum contains `r^n`. Thus
`r^n <= S(n;B) < t`, and taking logarithms gives
`n m > log(1/t)`. No converse follows. The correlation length here is
`1/m(B)` of this same finite box. The spatial factor two applies to
`B=(2n)^3`, not to an arbitrary rectangular box.

Here is a hand bound for the decimal in line 55. The exponential series gives
`e < 1957/720 + 1/4410 < 87/32`: the tail starting at term 7 has
successive ratios at most `1/8`. Also
`e^(2/5) <= 1 + 2/5 + (2/25)/(1-2/15) = 97/65 < 3/2`.
Direct integer products give `(87/32)^3 < 201/10` and
`(87/32)^4 < 547/10`. Hence
`e^(37/5) < (201*547/100)*(3/2) = 329841/200 < 1650`.
Therefore `log 1650 > 37/5 = 7.4`, and `2 log 1650 > 14.8`.
This verifies the two lower bounds without floating-point evaluation.
The closing sentence asserts only this necessary size condition; it cannot
exclude a different finite criterion or compare gaps of different boxes.

## 2. P2 — HOLDS (source lines 57–59), given (TM-c)

Use the actual twist of `gap-crux-restate.md:35`: replace `1-x_p` by
`1+x_p` on the stack. Replacing beta by minus beta would introduce an
extra constant and would invalidate this calculation.

The centre involution preserves nonnegative functions and commutes with T.
Its action on the positive, simple top eigenfunction must therefore be +1.
In each other eigenspace diagonalize the involution. If `S_odd` is the sum
of `r_i^n` over its minus eigenspaces, the exact formula is

`1 - Z^tw/Z = 2 S_odd/(1+S)`, with `0 <= S_odd <= S`.

This gives every inequality in P2. Strict positivity of the twisted
partition integral also gives `Z^tw/Z > 0`. At `S < 1/1650`, the sharper
upper bound is `2/1651 < 1/825`; multiplying `1/825` by 100 gives
`4/33 < 13/100`, which verifies the stated 0.13 percent bound.
This is a finite-torus twist estimate, not an infinite-volume confinement
or mass-gap theorem. The factor 2 counts minus parity, not three planes.

## 3. Proposition T1 — HOLDS (source lines 272–274)

Fix the exact model class, coupling, seed threshold, and hypothesis H.
A proved implication `H(M) => Seed(M)` has the contrapositive
`not Seed(M) => not H(M)`. A model with both H and a false seed refutes
that implication; a model satisfying both does not. Merely extending the
proof to another group supplies neither H nor failure of its seed.
No physical assumption or numerical constant enters this statement.

## 4. Proposition T2 — HOLDS (source line 276)

The first example suffices. Here is its group-independent constant check,
using `gap-mid-max.md:258–304` and the row-709 note at line 10.
For densities proportional to `exp(h+tau g)`,

`TV(rho_1,rho_0) <= (1/2) integral_0^1 E_tau|g-E_tau g| d tau
                   <= osc(g)/4`.

The last step follows from `Var(g) <= osc(g)^2/4` and Cauchy–Schwarz.
For a Wilson plaquette with `x_p in [-1,1]`, changing one other link gives
`osc(g) <= 4 beta`. The six incident plaquettes have three distinct other
links each. On sides at least three they give 18 neighbours and no repeated
pair. Thus `C(l,k) <= beta`, `alpha <= 18 beta`. This reasoning also
applies to U(1) and Z_2, without a quaternion representation.

The two row-709 additions to DC are valid. In one update cycle let R be
the total removed comparison mass, including descendants, and M the
initial mass. Every initial unit is removed, so `R >= M`. New mass is
at most `alpha R`, hence the end mass is at most
`M-(1-alpha)R <= alpha M`. Between cycles each averaging operator cannot
increase oscillation. The level-m mass budget is at most
`alpha^m Delta(f)`, giving the sum
`Delta(f) alpha^d/(1-alpha)` for discrepancies at distance d.
This proves the finite comparison estimate used here and in TW below.

For one plaquette, `Delta(x_p) <= 4*2 = 8`. The cut comparison in
Lemma M preserves its local specification away from the cut. With time
positions measured on the circle, its distance is at least
`floor(a/2)-1`. Differentiating `2F(a,B)-F(2a,B)` gives the factor
`12 a |B|`, since each four-dimensional torus has `6 a |B|` plaquettes.
Thus the constants are `96=12*8` and `768=96*8` when `B=(2a)^3`.
For fixed `alpha<1`, this polynomial times `alpha^(floor(a/2)-1)` tends
to zero. The spectral trace inequality gives `S <= exp(Phi_B)-1`.
In particular `Phi_B <= 3/5000` suffices: `exp(3/5000)-1 <= 3/4997
< 1/1650`. No numerical experiment is involved.

For a general log weight psi with oscillation omega, the same argument
has `osc(g) <= 2 omega`, hence `alpha <= 9 omega`. For the mixed weight
with nonnegative parameters, `omega <= 2 beta_F + 4 beta_A/3`.
Consequently the explicit sufficient condition is
`18 beta_F + 12 beta_A < 1`. It includes, for example,
`beta_F=beta_A=1/100`, whose upper bound is `3/10`.
Scaling both parameters from zero supplies the same cut-integral argument.
This addresses the K7 *weight family*, not its proposed transition point.

The positive-transfer hypotheses for each model remain inputs; this does
not attempt the separately owned general-weight transfer port.
The cluster-expansion example is an additional cited route, not needed
for this refutation of the worded test; its full expansion is not rechecked
here. Nothing above asserts a seed for a comparison model in its massless
or coexistence regime.

## 5. Proposition T3 — HOLDS AFTER CORRECTION (lines 278–283)

The implication in line 278 HOLDS in the fixed model class. Its applications
need the following range wording. The first overreach is line 280,
“ends below beta_U”; a first failure does not by itself exclude later
couplings. The same issue occurs in lines 281 and 283. These are claims
about the stated logical criterion, not counterexamples to Yang–Mills.

**Corrected text.** Let C be the class on which `H=>Seed` is proved,
and require `M'(beta) in C`. Fix a comparison map `beta -> M'(beta)` for which
`H(M(beta)) => H(M'(beta))`. This tool cannot establish its hypothesis
at any beta in the set where the comparison seed fails. If that failure
set contains an entire upper interval, that interval is excluded. A
restriction of the weight to a subgroup alone does not prove the required
implication for a hypothesis that also reads Haar measure or representation
multiplicities. State and verify that implication for the actual tool.

- **Maximal-torus application — HOLDS AFTER CORRECTION.** The restrictions
  of the Wilson weights agree. The conclusion is exclusion on the supplied
  U(1) failure set, conditional on transfer of H. The numerical boundary
  near 1.01 remains GUIDE; it is not supplied by T1 or T3.
- **Centre application — HOLDS AFTER CORRECTION.** The same statement
  applies to Z_2. Neither the first failure nor the number 0.44 alone
  supplies a whole excluded upper interval. The latter remains GUIDE.
- **Oscillation application — HOLDS AFTER CORRECTION in scope; the
  arithmetic HOLDS.** Treat the proposed endpoint as the exact rational
  pair `(37/25,9/10)` only for the arithmetic. Completing the square gives

  `psi(x) = (6/5)(x+37/60)^2 - 2269/3000`.

  Its minimum is at `-37/60`, its maximum is `psi(1)=119/50`, and
  `osc(psi)=9409/3000`. The Wilson weight has the same oscillation at
  `beta=9409/6000`, which rounds to 1.57. Moreover
  `max_[−1,1]|psi'(x)| = 97/25 = 3.88`.
  Thus all rounded numbers in line 282 are correct. If H reads only this
  oscillation and the common lattice incidences, its truth transfers at
  the matched value. Exclusion of *all larger* Wilson couplings also needs
  monotonicity of that criterion, or comparison failures at every matched
  value. Failure at the K7 endpoint is still GUIDE, not proved here.
- **Dimension/N application — HOLDS AFTER CORRECTION.** Apply the same
  pointwise test at actual supplied seed-failure parameters, after checking
  transfer of H. A transition and blindness by themselves do not prove
  a one-sided interval bound. The quoted transitions remain GUIDE.

The hand calculation proves properties of the displayed quadratic only.
It does not verify the physical location or nature of a transition.

## 6. Corollary to T3 — HOLDS AFTER CORRECTION (lines 285–287)

The first unjustified clause is line 285: having a numerical hypothesis
computed from a weight and incidences does not make a tool sound. Soundness
is its proved implication, as line 272 correctly requires. Nor do the
quoted GUIDE transition values constitute rigorous range bounds.

**Corrected text.** For an already proved criterion `H => Seed`, compare
its actual numerical inputs with those of a model having a proved seed
failure. Equality of those inputs, or an explicit implication between
hypotheses, excludes that matched case. A monotone smallness criterion
can extend this exclusion to larger input values. Without these premises,
0.44, approximately 1, and approximately 1.6 are conditional GUIDE
benchmarks, not discard thresholds. A tool stopping below these benchmarks
has not thereby been refuted by these comparisons.

In particular the verified crude gauge criterion stops at `beta=1/18`,
from `18 beta<1`. The layer criterion below stops at `1/6`, from
`6 beta<1`. The source's generic range “0.1 to 0.33” is not a proved
range for all the named methods and is not used. The valid Corollary
asserts no soundness or failure of an unnamed criterion.

## 7. Lemma COV — HOLDS (lines 321–338)

Work on the full `L^2(X,du)` with the gauge-averaged operator `T_P`,
whose kernel is `A_T`; the extra orthogonal sector has eigenvalue zero.
This makes arbitrary, possibly non-invariant layer insertions legitimate.
It does not replace the physical transfer spectrum by the unprojected one.

**Insertion and trace lines 327–331.** Integrating the temporal links in
one layer gives the bounded measurable kernel `A_T^A`. Fubini applies
because all factors are bounded on probability spaces. Its absolute value
is at most `A_T`. For arbitrary f,g this gives
`|<f,T_A g>| <= <|f|,T_P |g|> <= lambda_0 ||f|| ||g||`.
Thus `||T_A/lambda_0|| <= 1`; the same holds for B. Each kernel is in L2.
Grouping the cyclic integral into two integral operators and applying
A0(e), `gap-transfer.md:61,67`, proves all three traces in line 329,
including merely measurable A,B. No extra continuity hypothesis is needed.

**Spectral lines 332–337.** Write normalized insertions as Abar,Bbar,
`T_P/lambda_0=P+R`, `a=d-1`, `b=D-d-1`, and
`alpha=<Omega,Abar Omega>`, `gamma=<Omega,Bbar Omega>`.
Then `b>=a>=1` and the four terms in line 334 are exactly the expansion
of `Tr[Abar(P+R^a)Bbar(P+R^b)]`. The single-R terms have bounds `r^a`
and `r^b`. For the double-R term, the two valid bounds are
`r^a S(b)` and `sqrt(S(2a) S(2b))`.
If `b>=D/2`, the former is at most sigma. Otherwise even D and `d<=D/2`
force `a=b=D/2-1`; then the latter is `S(D-2)<=sigma`, also at D=4.
Consequently

`N_AB=alpha gamma+E_AB`, `|E_AB|<=2r^a+sigma`,
`N_A=alpha+E_A`, `N_B=gamma+E_B`, `|E_A|,|E_B|<=sigma`,
`N_1=1+delta`, `0<=delta=S(D)<=sigma`.

Here and below `|alpha|,|gamma|<=1`; this also handles complex observables.

**Independent normalization check.** Use the actual bound `|<B>|<=1`
instead of expanding a product of two error estimates:

`Cov(A,B) = [E_AB-alpha E_B+(alpha delta-E_A)<B>]/(1+delta)`.

It follows that `|Cov(A,B)| <= (2r^a+3sigma+delta)/(1+delta)
<= 2r^a+4sigma`. This is stronger than line 325.
For the source's own accounting, its numerator bound is
`2(1+sigma)r^a + 4sigma + 2sigma^2`, and
`2sigma^2<=sigma` for `sigma<=1/2`. Hence its constants 2 and 5 are
valid. The denominator is at least one. No step of the stated lemma fails.

### Independent hand example for COV

This uses a direct wall count, not the source's random-matrix experiment
or its trace expansion. Take spins `s=+1,-1` and transfer matrix
`T=(1/8)[[5,3],[3,5]]`. Its eigenvalues, from the sum and difference
vectors, are 1 and 1/4. Set `D=4`, `A=s_0`, `B=s_2`, so `d=2`,
`a=b=1`, and `sigma=(1/4)^2=1/16`.

On a four-spin ring the number of domain walls is 0, 2 or 4.
There are respectively 2, 12 and 2 configurations. After removing the
common factor `8^(-4)`, their total weight is

`2*5^4 + 12*5^2*3^2 + 2*3^4 = 1250+2700+162 = 4112`.

Global spin reversal makes both means zero. Among the twelve two-wall
configurations, four have `s_0 s_2=+1` and eight have `s_0 s_2=-1`:
both walls must lie on the same two-edge arc for the plus sign.
The other two wall classes have plus sign. Thus the covariance is

`[1250+(4-8)*225+162]/4112 = 512/4112 = 32/257`.

COV gives `2*(17/16)*(1/4)+5/16 = 27/32`, and
`32/257 < 27/32` since `1024 < 6939`.
This also tests the exceptional `D=4, a=b` branch by an independent
finite count. It is an exact toy-model check, not evidence for a Wilson gap.

## 8. Lemma REG — HOLDS (lines 319, 342–350), given its inputs

The general-weight transfer construction remains the named `(TM-gen)`
input. This verdict does not establish that input or Proposition V.
For the cube sequence in the proof, Theorem S alone supplies the stronger
thermal bound; the all-cube extension S3' is not needed.

**The seed constant.** The three spatial doublings give exponent
`4^3=64`. For `0<=x<=1/640`,
`(1+x)^64-1 <= 64x exp(64x) <= 71x`.
A hand justification of the last constant is
`exp(1/10) <= 11/10 + (1/200)/(1-1/10) = 199/180 < 71/64`.
Squaring gives `71^2=5041`. Induction on
`s_(k+1)<=5041 s_k^2` yields
`s_k<=q^(2^k)/5041`; all iterates stay below `1/5041<1/640`.
The largest excited ratio obeys
`r_k^(2^k n)<=s_k`, hence `r_k<=q^(1/n)`.
These are precisely the dyadic inputs in source line 345.

**Every counting constant.** Translation invariance gives six choices of
the first plaquette orientation. For each one, at most `6*3^4=486`
second plaquettes have base-point distance at most one; each covariance
has absolute value at most one by the variance bound. At distance j>=2,
there are at most `(2j+1)^4-(2j-1)^4=64j^3+16j<=72j^3` base points,
including the possible truncation at half a torus period. Each has six
orientations. COV gives `2(1+sigma)<=2+2/5041<2.001`, and
`6*72*2.001=864.432<865`. Its residual contributes at most
`5sigma*6D_k^4=30D_k^4 sigma` for each first orientation. Thus every
factor in line 347 is correct, including the outer factor six.

For an explicit finite constant put `rho=q^(1/n)` and `c=-log q`,
assuming `0<q<1`. The geometric series and three differentiations give

`H(rho):=sum_(j>=2) j^3 rho^(j-1)
        =(1+4rho+rho^2)/(1-rho)^4-1`.

Since `exp(cy)>=(cy)^4/24`, with `y=2^k`,
`D_k^4 sigma_k <= 16n^4 y^4 exp(-cy)/5041
                 <= 384n^4/(5041 c^4)`.
One admissible value is therefore

`C(n,q)=6[486+865 H(rho)+11520n^4/(5041 c^4)]`.

If q=0, every such thermal sum is zero; the near-plaquette bound alone
gives `C(n,0)=6*486=2916`. A negative q is incompatible with the premise.
The geometric-series differentiation is justified on every compact
subinterval of `[0,1)` by uniform convergence, or by finite sums and their
vanishing tails. This is a written bound, not a numerical maximization.

**Passage to the limiting pressure.** The finite pressures are convex,
converge pointwise to f, have `|f_k'|<=6`, and satisfy `0<=f_k''<=C`.
At x choose a convergent subsequence of derivatives with limit g.
Passing the lower tangent and upper quadratic inequalities to the limit
gives, for every y in I,

`g(y-x) <= f(y)-f(x) <= g(y-x)+(C/2)(y-x)^2`.

The two one-sided difference quotients both tend to g. Thus f is
differentiable at x. Adding the upper quadratic inequalities at x<y
gives `0<=f'(y)-f'(x)<=C(y-x)`. This completes C^(1,1), with the
quantifiers uniform over beta in I as claimed. No assumption about
absence of a transition was used in proving this implication.

## 9. Identity L — HOLDS (lines 371–384)

The direct layer integral in `gap-transfer.md:119,128–136` is the input.
For a product centre flip c, Haar invariance and `c^2=1` give
`(T_P C)(u,v)=A_T(u,c v)`. This proves the twisted cyclic integral
without assuming a temporal gauge or removing a holonomy.
Every spatial plaquette has an even number of flipped links, so
`V(c v)=V(v)`. Thus its last-layer ratio is exactly
`A_T(u,c v)/A_T(u,v)=I(u,c v)/I(u,v)`.
The denominator is strictly positive. Dividing the two finite integrals
gives the asserted expectation under the ordinary torus law.

A flip changes the signs of the layer bonds crossing the chosen plane.
It is therefore the antiperiodic sign seam of this background spin model;
no ferromagnetic assumption is needed. Applying the finite group identity
`Pi_flux=(1/8) sum_(k in Z_2^3) C^k` yields
`U=(1/8) sum_(k!=0) E[1-I(u,c^k v)/I(u,v)]`, as in line 384.
Here `Pi_flux` is the zero-flux projection, not the vacuum projection used
in COV. Individual layer ratios may exceed one; the identity does not
assert a pointwise sign for their deficit.

## 10. Proposition TW — HOLDS (lines 386–402)

Take `0<beta<1/6` and `alpha=6beta`. The finite comparison estimate DC
was checked in Section 4 above, including both row-709 additions.

1. **Influence, line 392 — HOLDS.** At a site, the six incident spin bonds
   have six distinct neighbours when every side is at least three.
   Changing one neighbour changes a unit quaternion coefficient by norm
   at most two. Hence the log-density increment has oscillation at most
   `4 beta |J_b|<=4 beta`. The total-variation interpolation bound proved
   above gives `C(x,y)<=beta`, uniformly in all backgrounds and all
   `J_b in [-1,1]`. Row sum: `alpha<=6 beta`.
2. **Interpolation, line 393 — HOLDS.** Explicitly keep the constant
   `exp(-beta |E(B)|)` fixed along the path:
   `I_theta=exp(-beta |E|) integral exp(beta sum_b J_b^theta y_b) dh`.
   This is the twist convention, not multiplication of the full action
   `1-y_b` by J. It gives exactly
   `d log I_theta/dtheta=-2 beta sum_(b in Sigma_0) <y_b>_Jtheta`.
3. **Half-box flip, lines 394–396 — HOLDS.** Multiplication by -1 on H
   reverses precisely the two seams Sigma_0 and Sigma_1. The coupling
   `1-2theta` becomes `1-2(1-theta)` and the other seam becomes -1.
   Thus the transformed law is `K^(1-theta)` and y_b changes sign.
   Integration in theta gives exactly one half of the difference between
   the J and K expectations, with the sign in line 396 correct.
4. **Distance and oscillation, line 398 — HOLDS.** The changed
   conditionals are confined to coordinates `j_1-1,j_1`, whereas y_b
   reads coordinates `b_nu-1,0`. Periodic distance gives
   `d>=min(j_1-1,b_nu-1-j_1)=floor(b_nu/2)-1`.
   Its two coordinate oscillations are at most two, so `Delta(y_b)<=4`.
   DC therefore gives `4 alpha^d/(1-alpha)`. The case `b_nu=3` has d=0
   and is included, not discarded.
5. **One twist, line 399 — HOLDS.** Multiply the derivative factor
   `2 beta`, the pairing factor `1/2`, the comparison factor 4, and
   the seam size `|B|/b_nu`. The result is exactly
   `4 beta (|B|/b_nu) alpha^(floor(b_nu/2)-1)/(1-alpha)`.
6. **Several twists and U, line 400 — HOLDS.** Telescope layer ratios
   through successive flipped backgrounds. Uniformity makes logarithmic
   bounds additive. If their sum is M_k, Identity L gives
   `exp(-M_k)<=Z[k]/Z<=exp(M_k)`. Spectral positivity and parity give
   `0<Z[k]/Z<=1`, hence `1-Z[k]/Z<=-log(Z[k]/Z)<=M_k`.
   Among the eight binary triples each coordinate equals one four times;
   the total number of flips is `3*4=12`. Consequently
   `(12/8)*4 beta=6 beta`, proving line 390 with no time-length factor.

**Example, line 402 — HOLDS by integer arithmetic.** At `beta=1/12`,
`alpha=1/2`, `b=2a`, the expression in line 390 becomes
`(1/2)*4a^2*2^(-(a-1))*2=8a^2/2^a`.
For a=25 this is `5000/33554432`. It is less than `3/20000` because
`100000000<100663296`, and `3/20000<1/4950` because `14850<20000`.
The last denominator is `3*1650`. This verifies the flux threshold for
all time extents at least three. It supplies no bound on the even-sector
thermal sum and therefore proves no full seed above the DOB range.

## 11. Lemma P — HOLDS (lines 425, 431–433)

The inherited convention is `|e|=1`, and phi has chord-Lipschitz constant
at most one. Reflect across the hyperplane perpendicular to e. When
`e.F=0`, this reflection preserves both Haar measure on S3 and the tilted
law. Thus `E_F h_e=0` and

`Cov_F(phi,h_e)=(1/2) E_F[(phi(h)-phi(Rh))h_e]`.

The chord length is exactly `2|h_e|`. This proves the first bound,
`|Cov_F(phi,h_e)|<=E_F h_e^2`, with no factor lost.

An independent route to the second bound avoids differentiating the
normalizer. For `F!=0`, put `t=h.F/|F|`, `kappa=|F|`, and `R_0=|t|`.
The law of R_0 is tilted from its untilted law by `cosh(kappa R_0)`.
Both `R_0^2` and `cosh(kappa R_0)` are increasing. Their covariance is
one half of the expectation of the product of their differences for two
independent copies, and is nonnegative. Therefore
`E_F t^2 >= E_0 t^2=1/4`. Rotations fixing F make the three orthogonal
second moments equal, so
`E_F h_e^2=(1-E_F t^2)/3<=1/4`.
For F=0, use rotational invariance directly; no division by |F| is needed.

The source's stronger intermediate monotonicity claim also checks:
`d E_kappa(t^2)/d kappa=Cov_kappa(t^2,t)` equals
`(1/(2 Z_kappa^2)) integral (t-t')^2 (t+t') sinh(kappa(t+t')) dnu(t)dnu(t')`,
where nu is the even untilted coordinate law. The integrand is nonnegative.
Finally phi(h)=h_e attains the first bound, and F=0 attains 1/4.
Thus this constant cannot be reduced uniformly. No conclusion about
nonorthogonal e, `(vMF-Lip)`, or the proposed transport ranges follows.

## Pre-comparison boundary

All eleven named statements have now received verdicts on disk.
P1, P2, T1, T2, COV, REG, Identity L, TW and P hold on their named inputs.
T3's pointwise theorem holds; its range applications and its Corollary
need the corrected text above. No claimed physical transition value was
promoted from GUIDE. At this boundary the earlier Claude check had not
been opened. Its subsequent reading and comparison are recorded next.

## 12. Comparison with the earlier Claude check

Only after Sections 1–11 were on disk did I read all 186 lines of
`gap-crux-fp-check.md` (Claude Opus 5.5, row 716). The pre-comparison
report has SHA-256
`0283b4c983d15ed41f7b196a798980ce47c2894f00b92a99f23815a05f8262da`.
An unchanged copy is `/tmp/gap-fp-astra-726/independent-verdicts.md`.
This records the reading order; the hash is not mathematical evidence.

**All eleven verdict labels agree.** In particular the full-space layer
trace, the exceptional COV distance, REG's count, TW's sign flip and its
periodic distance, and Lemma P's sign agree. No result was changed to
match a majority. The remaining comparisons are these:

1. **T3's class hypothesis: Claude is right to make it explicit.**
   Row 716 line 52 requires the comparison model to belong to the tool's
   class. My pre-comparison text inherited this from the fixed setting.
   The corrected statement must explicitly say `M'(beta) in C`, where
   `H=>Seed` has been proved for every model in C. That clause is included
   in the final corrected text above. This is an accepted clarification,
   not a disagreement about the contrapositive.
2. **T3's range applications: the pointwise restriction in this report
   is the justified conclusion.** Row 716 lines 55–58 accepts the uses,
   retaining GUIDE labels and noting monotonicity for K7. That caveat
   should also govern the “ends below” language in source lines 280,
   281 and 283. There is one direct logical disagreement: row 716 line 57
   offers “a K7 point with larger oscillation where the seed fails” as
   an alternative to monotonicity for an upper range limit. One further
   failed point excludes its matched input only. Without monotonicity,
   H may be true between two failed comparison inputs. To exclude an
   interval one needs failure at every matched input in it, or a proved
   implication from each accepted hypothesis to some failing comparison.
   The corrected pointwise formulation in Section 5 is right; neither
   check establishes any proposed physical transition boundary.
3. **An extra P1 decimal in the Claude report is not a strict bound.**
   Row 716 line 128 says the 1/5041 threshold gives a length “above 17.1”.
   P1 gives the exact lower bound `2 log 5041=4 log 71`, which is
   *less* than 17.1. For a hand verification,
   `e>163/60>19/7` and `exp(11/40)>4201/3200`, so
   `exp(171/40)>(19/7)^4*(4201/3200)>71`; the last comparison is
   `547478521>545507200`. Thus `4 log 71<171/10`.
   Conversely the bounds used in Section 1 and
   `exp(1/4)<=113/88` give
   `exp(17/4)<(547/10)*(113/88)=61811/880<71`.
   A safe decimal lower bound is therefore 17.0, or use the exact logarithm.
   This report is right on that arithmetic. Source P1's weaker 14.8 bound
   remains true; this does not change any verdict on an assigned statement.
4. **Arithmetic agreement is not three independent checks.** Row 716
   line 118 evaluates the same TW bound in three rearrangements. The
   value and the comparison with 1/4950 are right, as Section 10 verifies
   exactly. I do not count those rearrangements as three independent
   derivations of the bound. The alternative normalization in Section 7,
   the direct domain-wall count, and the untilted-law argument in Section 11
   supply different calculation paths here. Provider difference alone is
   not the mathematical reason for independence.

The Corollary corrections in row 716 line 62 agree with Section 6:
“if sound” is necessary, and the reported generic stopping range is GUIDE.
The extra claims checked in row 716 (Remark 2.A, Proposition V, Corollary C,
P3 and P4) remain outside this assignment. Apart from the displayed P1
arithmetic, this report neither endorses nor disputes those extra verdicts.
There is no other disagreement within the assigned scope.

## 13. Source boundary, reuse, and disposition

The lead's November 8 digest searched main and PRs 10114, 10133, 10134 and
10141. I reused that search rather than repeat its unrelated inventory.
At the fetched main revision, the exact-name search for this check,
COV, TW and vMF-Lip returned only unrelated substring matches.
The digest's main hit at
`docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145`
was read. It is a determinant-weighted, noncompact Dirichlet Maxwell law
and a covariance lower bound, not this torus upper bound.
The additional prior hit named by `gap-transfer.md:6` was also read:
PR 10114's `MASS_GAP_CONSTRUCTION_ASTRA.md:86–215`, at the PR revision
recorded above. It already constructs the Wilson transfer operator and
its finite-volume gap. Those are reused inputs, not new results here.

The full-read SA-index README was read, then the relevant chunk rows
and their neighbours: chunk-02 lines 85–104, chunk-01 lines 65–72,
and obligations lines 22–28. Searches covered the transfer operator,
GL3/GL8, mass/spectral gap, Dobrushin, von Mises, antiperiodic seams,
thermal sums, and first-order transitions. The outline passages actually
read were SA 588–599, 2195–2243 and 2313–2335, at `31a47c543775`.
Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, already provide the positive one-bond coefficients and transfer trace
construction there. The index calls GL3/GL8 proved in detail; the original
lines contain their derivations. They are credited and reused, not rebuilt.
Their polynomial-decay example also explicitly separates clustering from
a positive spectral gap. None of these passages is a check of row 712.

CA-I was fetched once as requested. The 4.12–4.19 index README concerns
background/stage hypotheses, not these transfer estimates. Searches in
CA-I for Dobrushin, von Mises, antiperiodic, thermal sum, first-order
transition, Perron and Jentzsch returned no hits. This is a bounded search
record, not a claim of exhaustive mathematical absence. No CA-I theorem
or Balaban paper theorem is imported into the checks. Tadeusz Balaban's
ultraviolet work remains credited as background, and his PDFs/OCR were
not needed or opened. The listed general-weight transfer input retains
its separate owner; no general-weight port was attempted.

**Disposition.** Nine named statements HOLD on their stated inputs.
T3 and its Corollary HOLD AFTER CORRECTION of the comparison scope.
No assigned estimate FAILS. All source files, FINISH and the registries
are unchanged. The proposed wording is in this report only. No scripts
were run to prove, test numerically, or discharge a mathematical statement;
Python was used only for checkpoint, source, staging, and credential checks.
The mathematical checks are the written arguments above. This remains
research text and grants no status.
