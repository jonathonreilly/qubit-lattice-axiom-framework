# Repo search

The lead supplied `prior/repo-search-2026-11-08.md`; no
`prior/gap-blockcrit-check-astra.md` exists at the pinned commit. That older
digest concerns the UV construction, not row 836's block response criterion.
Its scalar covariance and one-step transfer hits do not supply this criterion.
Rows 836 and 841 assign the author text and this check respectively; the
registry has no competing `gap-blockcrit` assignment. No duplicate check was
found. The relevant earlier lane inputs are credited below, not reproved as
new results. I fetched main and PR 10114 and checked the digest's closest
hits: main's `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:79–94`
uses finite-Z_N variables; PR 10114's
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`
proves a one-step transfer witness. Neither is the continuous-group block
criterion here. A targeted main search for `Dobrushin|Shlosman|vertex.star|blockcrit`
in `docs/` and `research/` returned no hit. This supplements the lead's
five-ref search; no claim of repository-wide absence is made.
The fetched revisions were main `bb4ec020d5ada57c630dd89acc98a68397ade423`
and PR 10114 `f76f6c649cff7dffbab664d8976e680e8f287fe9`.

## Provenance and scope

Codex, configured for this dispatch as gpt-6-astra/xhigh; source commit
`ee98b52c7923f7803ac0d2b9a8b3b50fecf9a732`. This is a research check of
`library/gap-blockcrit-opus.md`, authored by Claude Opus 5.5, not an audit.
It grants no status. Line numbers below refer to that pinned author file.
Its SHA-256 is `5cb7b40b2a6a6815e58ec936a85b68cfb406348f004ba99089f6045da73f5201`.
Only this report is changed. Every mathematical check is by hand; no run
discharges a step. Numerical guides and novelty claims are outside the check.

The outline and CA-I were downloaded once, at `31a47c543775`, into the new
directory `/tmp/sa-gap-blockcrit-check-astra.JqruyT`. The SA index has no
Dobrushin, Shlosman, heat-bath, star-block or Villain hit in its outline
chunks, obligations or CA 4.12–4.19 index. This is a bounded search, not an
absence theorem. Chunk 01, neighbouring rows 567–635, and obligations
588–599 lead to outline lines 588–599: polynomial clustering alone does not
give a mass gap. That passage does not supply row 836's finite-block result.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text. No Balaban estimate is imported by this check.

## Checkpoint

Completed: every named statement in the dispatch, including the reduction
and obstruction statements. GFF's unrestricted family quantifier fails;
its covering-family repair is proved below. The core star and seed bounds
survive. No check remains in progress. Source revisions are fixed above;
the next decision is the lead's application of the listed corrections.
Imported statements were read at the ranges listed below; their full
earlier dependency checks are not repeated.

## 1. Lemma GF (lines 79–104): HOLDS AFTER CORRECTION

The disintegration at lines 93–94 is valid for arbitrary block observables,
not just invariant ones. The admissible forest and its section depend on
the block and event, not the exterior value. In (2.1) the same Haar variable
can therefore be used for both exteriors. For fixed eta, changing a free
coordinate changes only that coordinate of Phi, by an isometry. However,
line 95 must read

```math
\delta_c(h_\eta)\leq\delta_c(h),
```

not equality: the other coordinates range only over a section. This is all
the proof needs. For example, with a fixed link f and a free link c, take
`h(U)=Re(U_f) Re(U_c)` and eta with `Re((eta.1)_f)=0`. The left seminorm is
zero and the unrestricted one is one.

Each plaquette contains c at most once. Its staple is an isometric product
in each other link separately. Corollary V1 therefore gives the displayed
conditional discrepancies `x n(c,d)` and `x n(c,j)`. The comparison series
is nonnegative and converges under the row-sum hypothesis. Integrating its
bound over the common eta proves (GF); splitting the integrand and kernel
changes proves (2.3). No boundary gauge transformation has been smuggled
into either exterior.

Remark GF' (1)–(2): HOLDS. On each connected component the positive Perron
weight gives convergence when the spectral radius is below one (an isolated
zero row takes weight one). With F empty, the same comparison applies to
arbitrary link sets.

## 2. Lemma STAR (lines 172–174): HOLDS

At periods at least three the eight incident links are distinct. The corner
pairs number `8*6/2=24`. Each has two distinct far links; a far link fixes
its perpendicular displacement from the centre, hence its corner. This gives
48 events, each in one corner. For a fixed link, its two endpoints give
two containing stars; six perpendicular shifts at each endpoint give
twelve event stars. These centres stay distinct when a period is three.
The oriented holonomy identity in (iv) follows by multiplying its four links.

## 3. Theorem ST (lines 176–214): HOLDS

Here is a check of the response that does not count walks as in the source.
After fixing the event's adjacent spoke c, let `h` be the sum of responses
on the six perpendicular spokes and `t` the response at -c. Sum the seven
linear resolvent equations. The unit event forces exactly one of the six
spokes, with strength x; each of those six has four neighbours among them.
Therefore

```math
h=x+4xh+6xt,\qquad t=xh,
\qquad h+t=\frac{x(1+x)}{1-4x-6x^2}.
```

The row bound `6x<1` ensures this is the nonnegative convergent resolvent
in the claimed range. Counting events per block link gives

```math
\alpha_*=\frac{48}{8}(h+t)
 =\frac{6x(1+x)}{1-4x-6x^2}.
```

Its crossing is `12x^2+10x-1=0`, hence
`beta_*=(sqrt(37)-5)/3`. Since `sqrt(37)<7`, this is below `2/3`,
so both internal comparison arguments are in their convergence ranges.
The full eight-spoke conditional law has row sum `6x` and one-site
Poincare constant 3, by D1. Lemma W gives `c_*=3(1-6x)`. With `n=2`
and `kappa=2(1-alpha_*)`, R(c) gives precisely ST(ii).
ST(i) follows from R(b); ST(iii) follows from R(e) with step length 3/2.
The distance is the periodic midpoint distance, not a coordinate difference
across a cut. These conclusions include arbitrary fixed centre signs.

The displayed decimal examples can be replaced by exact hand arithmetic:

| beta | alpha_* | stated gap lower bound |
|---|---|---|
| 1/4 | 17/31 | 105/124 |
| 3/10 | 387/533 | 2409/5330 |
| 7/20 | 1827/1933 | 3021/38660 |

These fractions agree with the rounded values. They verify the coefficient
and normalization without a numerical run.

## 4. Lemma SYM and (2.4) (lines 108–124): HOLDS

Keep the embedding hypothesis: all local block/event incidences must be
the lattice incidences, with no identifications from a short period.
Translations make each incident sum independent of position. Including
every rotated shape makes it independent of link direction. This uses local
rooted configurations; it does not assert that a coordinate permutation is
a global automorphism of a rectangular torus. Stabilizer averaging makes
the coefficients well defined when the chosen forest itself is not fixed.

Double-counting `(block, internal link)` gives `|E|n=|A||B|`.
Counting `(block, event, internal link)` gives
`|E|s=|A||B|alpha`; thus `s=n alpha`. In particular, the count uses
the whole block's eight links, although each event fixes only one of them.
There is no factor of seven in the denominator. On stars of period three,
the explicit counts in Lemma STAR establish the needed incidences directly.

## 5. Lemma M* and Corollary SEED (lines 228–240)

**Lemma M*: HOLDS.** For `1<=t<=a-2`, every plaquette meeting the star
has all its links in the retained half of the long torus. The long-torus
conditional kernel is measurable with respect to the retained exterior.
Taking conditional expectations again gives the short-torus kernel.
No claim is made for stars centred at the two cut layers.

**Corollary SEED: HOLDS AFTER CORRECTION of the free-energy convention.**
The distance count and all its constants hold. This is the ordinary
untwisted Wilson transfer problem, as in the imported DOB/SH chain;
the translation argument does not establish this seed for arbitrary
inhomogeneous centre signs.

Put `j=floor(a/2)`. The offending stars have link positions
`{a-3/2,a-1,a-1/2,0,1/2}` on the time circle. The selected plaquette
links lie in `[j-1,j]`. For `a>=4` the two distances to the bordering
offending links are `j-3/2` and `a-3/2-j`. Their minimum is `j-3/2`.
For `a=3` use the trivial lower bound zero. Each response step changes
circular time by at most 3/2, giving exactly

```math
m_0=\max\{0,\lceil(2j-3)/3\rceil\}.
```

R(d), the multiplicity bound two, and `Delta(x_p)<=4` give the factor
`2*4=8` in (17*). The free-energy identity gives `12*8=96` in (18*),
and `|(2a)^3|=8a^3` gives 768. Source line 240 must specify
`F=log integral exp[-s sum_p(1-x_p)] dHaar` when writing
`F'=-6t|B| abar`. With the Z of line 21 instead,
`F'=6t|B|(1-abar)`. The added volume term cancels in Phi, so (18*)
and every seed conclusion are unchanged.

For completeness, the imported arithmetic is exact:
`exp(3/5000)-1 <= 3/4997 < 1/1650`. The corrected SH constants give
`s_1<32/809`, `K s_1<3552/4045<22/25` and
`log(1/(K s_1))>159/1250>1/8`; hence for `L>=64a` the gap exceeds
`1/(16a)>3/(50a)`. These are the bounds in `gap-vmf-lip.md:521–582`,
reused with the new comparison exponent. Existence follows from
`m_0>=(a-4)/3` and geometric decay beating `a^4`.

A new hand test, independent of the source's approximate size search:
take `beta=1/4`, `a=600`. Then `m_0=199`, `alpha=17/31<3/5` and
`(17/31)^4<1/10` (because `835210<923521`). Since `600<10^3`
and `199>=4*49`,

```math
\frac{768a^4\beta\alpha^{m_0}}{1-\alpha}
 <480\,(10^3)^4\,10^{-49}<10^{-34}<3/5000.
```

Thus the seed holds at a coupling beyond the former `2/9` range, and
`m(L^3;1/4)>=1/10000` for `L>=38400`, conditional on the imported
transfer/shape results. The source's “first holds near a=360” remark is
not a certified minimum and is not used.

## 6. Blocks, admissibility and Lemmas G/F (lines 43–77)

**Definitions and Lemma G (i)–(iv): HOLDS.** A vertex block contains
all links moved by a gauge transformation supported on Q. Consequently its
conditional density is invariant under that group, at each fixed exterior.
For an event j, neither endpoint is in Q. A plaquette through j that meets
the block therefore has a different vertex in Q and both links at that
vertex are in the block. Smooth positivity on the finite compact product
gives the Lipschitz assertion, and covariance under the full gauge action
gives preservation of invariant functions. These arguments do not use the
sign of any plaquette coupling.

**Lemma F: HOLDS.** Ignore isolated vertices outside `Q union O(Q)` in
describing the forest components; they carry no coordinate. Root each
component as specified. For an edge directed from a reached vertex s to
a new vertex t, solve `eta_t=U_e^{-1} eta_s`; with the opposite orientation
solve `eta_t=U_e eta_s`. Then `U=eta.U'` with every forest coordinate
of U' equal to one. Each new vertex is in Q, since an outer vertex can
only be the root. Thus the recursion gives precisely one eta in G'_F.
Successive Haar-preserving substitutions on tree edges, followed by left
and right translations on free edges, establish product Haar preservation.
Gauge invariance then gives (2.1), including its normalizing constant.

A tree joining two outer vertices would prescribe the holonomy of their
connecting path. Gauge transformations fixed at both endpoints cannot
change that holonomy to one for arbitrary U. This proves why the boundary
rule is necessary. Choosing a different admissible forest for each event
does not change the block law: every choice is another exact representation
of that same law. Convexly averaging the resulting inequalities is valid.

One scope sentence needs correction: lines 104 and 124 describe the
general construction as quotienting all of G_Q. It quotients G'_F.
A component rooted inside Q retains its root rotation. For the star
choice G'_F=G_Q, so this distinction does not affect ST.

**(BC-gen): HOLDS as a sufficient condition.** Its weights belong on the
event index j in `sum_j w_j K_je`, because (2.3) acts on the column vector
of coordinate seminorms. It automatically implies `n_e>=kappa>0` and
therefore coverage of every link. The finite walk formula (2.4) is defined
only where its nonnegative series converges. It is an upper-bound
certificate, not a formula for the optimal physical response.

## 7. Theorem R (lines 130–154)

**(a): HOLDS.** For each coordinate j, the `n_j` blocks containing j
erase that seminorm. Summing the other block estimates gives exactly
`M=|A|I-N+K`. Multiplication on the left by `w^T` gives its contraction.

**(b): HOLDS.** The finite product's chord diameter gives uniform
convergence of `P^t f` to its mean for centred Lipschitz f. For the
self-adjoint P, `||P^t f||_2^2=<f,P^(2t)f>` then excludes spectral mass
above the claimed contraction factor in absolute value. Density extends
the spectral bound to the centred L2 space. Finally
`|A|<f,(I-P)f>=sum_a mu(Var_(B_a) f)`. The prefactor depending on
`min w` is harmless: the exponential rate is unchanged.

**(c): HOLDS.** Integrating each conditional Poincare inequality gives
`c_* sum_a mu(Var_(B_a) f) <= sum_e n_e mu(|grad_e f|^2)`.
Apply (b) and the bound `n_e<=n_max`. This controls all smooth functions,
and hence the invariant subspace too.

**(d): HOLDS AFTER CORRECTION at line 152.** The first asserted
inequality for `u=Nw` does not follow from (BC-gen). Use w for that
inequality and u for the second:

```math
w^T\frac{M}{|A|}\leq(1-\kappa/|A|)w^T,
\qquad
u^TN^{-1}K=w^TK
 \leq u^T-\kappa w^T
 \leq(1-\kappa/n_{\max})u^T.
```

These are the two required convergent nonnegative series. They give

```math
(N-K)^{-1}=(I-N^{-1}K)^{-1}N^{-1}
 =|A|^{-1}\sum_{t\geq0}(M/|A|)^t.
```

The preceding telescoping proof and its factor two then hold unchanged.
An algebraic test exposes the erroneous weight substitution: take
`N=diag(1,2)`, `w=(1,1)`, `kappa=1/2`, `K_21=1/2` and all other
entries zero, with `|A|=3`. These satisfy the displayed coefficient
inequality. But `u=(1,2)` gives first coordinate 1 in `u^T M/3`,
where the asserted bound is 5/6. No such claim is needed for R(d).

**(e): HOLDS.** There is also a direct proof that avoids the density
tilt and works for bounded complex g. Telescope
`Cov(f,g)=sum_t mu(g(P^t f-P^(t+1) f))`. The block contribution is
zero when g is measurable off that block. Each remaining contribution
has absolute value at most `2||g||_infinity sum_(e in B_a) delta_e(P^t f)`.
The same inverse series as in (d), `N=nI`, bounds this by

```math
\frac{2\|g\|_\infty\Delta(f)}{1-\alpha}\alpha^{m_0}.
```

Each link is counted at most n times. Terms before m_0 vanish by the
step-support condition. This stronger bound implies the source's factor
six. For `alpha=0`, take `0^0=1`; if no chain exists the covariance is zero.

## 8. Theorem R' (lines 156–164): HOLDS

Compactness of the gauge group gives an optimizing transformation in d_w.
For invariant f, the Lipschitz constant for d_w equals
`max_e delta_e(f)/w_e`: telescoping coordinates proves one inequality,
and `d_w(U,U')<=w_j|U_j-U'_j|` for a one-link change proves the other.
After choosing an optimizing representative, a path changing coordinates
one at a time has total weighted chord length exactly d_w. The mixture of
block couplings and (QBC) therefore contract this Lipschitz constant by
`1-kappa/|A|`. Gauge covariance makes P preserve invariant functions.
Averaging Lipschitz approximants over the gauge group proves density in
the invariant L2 space. The spectral and conditional-energy steps of R
then apply there with the stated constants.

The comment after the proof concerns the symmetric families used here.
For those families, w=1 and the *row* sums of K also equal `n alpha`:
they are constant by symmetry and have the same total as the column sums.
The GF coupling then gives QBC with the same margin. For a general
weighted family, (BC-gen) controls column sums, whereas this coupling
test for QBC requires `sum_e w_e K_je<=(n_j-kappa)w_j`.
Do not extend the comment to an arbitrary family without that extra bound.

## 9. Proposition CEIL (lines 264–268): HOLDS AFTER CORRECTION

Take a nonempty block and only components meeting Q. A tree component
with k vertices in Q and one outer root has k edges, but its degree sum
over Q is `2k-deg_F(root)`, not always `2k-1`. Replace the equality
at line 268 by `<=2k-1`. A component rooted in Q has degree sum `2k-2`.
Summing still gives a total at most `2|Q|-1`, so some vertex has
forest degree at most one and at least seven free incident links.

The induced nonnegative matrix contains `x A_(Gamma_7)`. A positive
two-class eigenvector solves `lambda t=6s`, `lambda s=t+4s`;
thus `lambda=2+sqrt(10)`. Extending this vector by zero and using the
Rayleigh quotient proves the required lower bound for the symmetric
matrix C^F. The threshold is exactly

```math
4/(2+\sqrt{10})=(2/3)(\sqrt{10}-2).
```

This is a ceiling for this chosen majorant and GF's convergence test.
It is not a lower bound on the optimal block response, and it does not
exclude a different block estimate at order one. The source's wording
about the “method” must retain this restriction.

## 10. Proposition SL (line 283): HOLDS

Use all four direction families of slabs. Each link is resampled in
exactly one slab. A slab with V vertical links has `3V` bonds and `6V`
distinct horizontal event links (one at each end layer per bond).
Changing one event changes the fields at the two bond endpoints,
each by at most beta times its chord change. Thus `sum b=2x`.
The internal graph is six-regular, so summing the resolvent equations
gives `sum K=2x/(1-6x)`. Translation invariance within a layer makes
the incoming sum per internal link constant. It equals

```math
\alpha_{\rm slab}=6\frac{2x}{1-6x}.
```

Its being below one is exactly `18x<1`, or `beta<2/9`.
This is the coefficient furnished by GF with F empty. It says nothing
against sharper joint slab couplings. The slab factorization input is
`gap-arealaw-opus.md:186–211`, credited to its author Claude Opus 5.5.

## 11. Theorem U (lines 295–301): HOLDS, given Theorem V

There is a uniform conditional Poincare constant for each fixed block
shape at fixed beta. To see it directly, put
`l=min phi_beta>0`, `u=max phi_beta<infinity`, and let P be the maximum
number of plaquette factors meeting a block. The normalized block density
has maximum/minimum ratio at most `(u/l)^P`. Comparing its variance and
Dirichlet integral to product circle Haar, whose gap is one, gives
`c_*>=(l/u)^P>0`. This is uniform in both exterior and torus size.

The translated/rotated fixed shape also has bounded n_max independent of
M. A fixed positive margin on arbitrarily large tori would therefore give
`gamma_V>=kappa c_*/n_max>0`. This contradicts the *full limit* in the
imported Theorem V (`gap-tu-retry.md:66–101,333–345`), not merely a liminf.
For a size-independent local certificate, one positive margin repeats on
all sufficiently large tori, so its coefficient cannot be below one.
R' gives the same obstruction to any uniform QBC margin. It does not say
that an individual finite torus cannot have a margin tending to zero with M.

This checks the implication, not a fresh proof of Villain masslessness.
Credit the imported theorem to Codex gpt-6-astra and its recorded prior
check to Claude Opus 5.5. The Gaussian-limit discussion is not used.

## 12. Proposition GFF (lines 306–308): FAILS as quantified

The exit-kernel identity is right. The claim of a positive margin for
positive mass “for every block family” is false without a covering
hypothesis. On Z^d, take the family consisting of the single block `{0}`
and take any `m>0`. At a site z outside that block, `n_z=0` and the
left side of (BC-gen) is zero. For every positive weight w_z and every
positive kappa its right side is `-kappa w_z<0`. No positive global
margin exists. The first false conclusion is the third sentence of
line 306, not the Gaussian disintegration in line 307.

The following corrected statement holds. Use the finite-block Gaussian
specifications on Z^d, a covering family with finite incidence at each
site, and **w=1**. Its exact minimal response coefficients and unweighted
margin are

```math
K^a_{yx}=H_a(x,y),\qquad
\kappa_* =\inf_x\sum_{a:x\in B_a}\rho_a(x).
```

Indeed the conditional precision is `2d+m^2` on the diagonal and -1
on nearest-neighbour internal pairs. Its mean solves the killed-walk
Dirichlet equation. Translating one Gaussian by the change of its mean
couples the laws with coordinate cost `H_a(x,y)|Delta phi_y|`.
The coordinate test function phi_x proves that no smaller coefficient
can work. Summing exit probabilities gives the column identity in the
source. For m=0 a walk exits any finite block almost surely, so rho=0.
For m>0 its probability of being killed before its first move is
`m^2/(2d+m^2)>0`, uniformly in block and starting point. Coverage then
gives a strictly positive lower bound for kappa_*.

Thus the intended translation-family example is valid. The result concerns
conditional specifications, including when a massless full field itself
is unavailable in low dimensions. For arbitrary weights the displayed
column formula must instead retain `sum_y w_y H_a(x,y)`; the proof
does not assert that every choice of weights has the same margin.

## 13. Remaining assertions and limits

Section 6.5(a): HOLDS with CEIL's method restriction. Section 6.5(b):
HOLDS for the nonnegative walk certificate. The block part of an event
plaquette is a path between two outer vertices. Admissibility forbids
fixing that entire path. Thus each event has at least one free response
entry x, giving the claimed first-term lower bound. Where GF's series
diverges, this is a lower bound on that series, not a finite inverse or
a bound on an optimal block coupling.

The finite Gaussian-star arithmetic in 6.5(c) holds: the edge current
splits into antipodally even and odd parts with eigenvalues 8 and 6.
Its potentials are the four listed multiples of 1/48, with four zeros;
zero is a median, so minimizing over a common shift gives l1 cost 1/3.
The passage from this linear model to the optimal nonlinear SU(2) cost
is not proved in the source and is not used here. The claim about all
fixed small blocks remains an argument, not a consequence of the star
calculation. The correlation-length implication in 6.5(d) holds when xi
means the actual asymptotic exponential correlation length: R(e) gives
`1/xi>=log(1/alpha)/r` and hence the displayed lower bound on r.

The larger-block table, the row-832 estimates, the approximate first seed
size, the U(1)-Wilson extrapolation and the novelty comparisons were not
verified. They supply no premise here. In particular CEIL does not prove
that every possible block criterion fails at order one.

## Inputs reused and disposition

The primary input ranges read were:

- `gap-vmf-lip.md:57–80,192–313,438–594`: V/V1, DC,
  DOB and its seed arithmetic, by Codex gpt-6-astra.
- `gap-block-astra.md:513–532`: the refined discrepancy step and (B26),
  by Codex gpt-6-astra. The author's locator 497–512 is stale.
- `gap-mixed-opus.md:18–62`: forest disintegration and weighted spectral
  comparison, by Claude Opus 5.5.
- `gap-shape-exercise-astra.md:266–339`: D1, by Codex gpt-6-astra.
- `gap-seed-shape.md:1–17,87–111,116–125`: the corrected SH statement
  and constants, by Claude Fable 5.2, with its recorded lead corrections.
- `gap-arealaw-opus.md:186–211`: the slab factorization, by Claude Opus 5.5.
- `gap-tu-retry.md:55–101,333–347`: the Villain premise and full-limit
  conclusion, by Codex gpt-6-astra.

The comparison method is Dobrushin's; the block organization follows
Dobrushin and Shlosman, and the quotient path step follows Bubley and Dyer.
This report checks their finite arguments as written in the lane, without
a claim to have read their original papers. Tadeusz Balaban's results are
not needed for these strong-coupling statements. The transfer construction,
full SH proof and Villain masslessness proof remain reused inputs, not
fresh full-chain checks in this report.

The result delivers the proposed strong-coupling block certificate and
seed comparison after the stated corrections. It does not supply the
order-one coefficient, a continuum mass gap, a novelty finding or audit
status. The author file, registry and FINISH row remain untouched.

RESULT: ST, STAR, SYM, G, F, GF', M*, R(a–c,e), R', SL and U (given V) HOLD; GF, R(d), CEIL and the seed proof HOLD AFTER CORRECTION without changing the star threshold (sqrt(37)-5)/3 or the seed/gap bounds; GFF FAILS for arbitrary block families, while its unweighted covering-family version holds; order one remains open.
