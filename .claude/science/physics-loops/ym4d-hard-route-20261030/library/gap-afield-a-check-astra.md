## Repo search

The target-specific prior digest is absent. I read the whole lead digest
`prior/repo-search-2026-11-08.md`. It concerns the November 8 existence
suppliers, not this November 16 scale-flow check. Its nearest named hit is
PR #10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`, under
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. I fetched that PR
and read those lines: they give a positive one-step plaquette correlation,
not a Casimir bound, scale-flow theorem or entropy derivative. I do not
rederive that result. Row 1031 has no "Repo prior work" line and explicitly
reports that its author did not search main or the other PRs (source
163–164). The older digest cannot certify absence of November 16 work.

The actual close predecessors are the lane's `gap-crux-restate.md:37–45,
170–219` (Lemma A, Theorem S, Lemma E', Corollary S3', the latter two credited
there to Codex GPT-6 Astra), `gap-compact-rigidity-max.md:131–243` (the
dyadic compactness/rigidity construction by Claude Fable 5.2), and
`gap-dichotomy.md:75–182` (definitions and repaired hypotheses). I use their
statements as named inputs, not as new results. Exact-name searches of
`open-registry.md` and `open-core.md` found no ownership match for this
check or its new real-scale statements. This is the requested check of
row 1031, not a new attack on the separately owned open (W) or (LIOU).

Written by OpenAI Codex (GPT-6; task label `gap-afield-a-check-astra`),
2026-11-16, against commit
`4e3d07e087c53357993e8d6a67cd3aa981c76d89`. Research check only; not an audit
and no status grant. No mass gap is claimed. No numerical or automated proof
step is used. This check does not cover the full Yang–Mills construction or
prove the open seed inequality. The exact backend suffix and effort are not
exposed to this session; the filename is not evidence of a runtime model ID.
Upstream theorem proofs remain named inputs. Literature metadata, recalled
NR-II(3), the specific-entropy identification and GUIDE comparison models
are not independently verified here.

### Checkpoint

All 1,057 lines of `gap-afield-a-max.md` have been read in bounded ranges.
The load-bearing predecessor statements above have been read. Own verdicts
were saved through section 8 before opening the Opus check. Its 364 lines
were then read in full. The comparison and final dispositions follow.
The source note is unchanged between Opus's `ee938bdf2` and this task's
`4e3d07e08` (the path-restricted git diff is empty). No source, registry,
FINISH row or status file was changed. No proof obligation remains for
this check; the underlying (W), BDD-Delta and LIOU remain open.

Download directory: `/tmp/sa-gap-afield-a-check-astra.6etIBY`; the outline
and CA-I were fetched once from `31a47c543775`.

## Own verdicts, recorded before reading Opus

All unqualified line numbers below refer to `gap-afield-a-max.md` at the
pinned commit. HOLDS means a research-level check of the stated implication,
with the named upstream results retained as inputs. It grants no status.

### 1. Finite comparisons and the real-scale limit

| Statement | Lines | Verdict and check |
|---|---|---|
| P1 | 485–486 | HOLDS. The inclusion of sequence spaces gives the monotonicity of the power norm; subtraction of the same bulk density preserves it. |
| P2 | 487–489 | HOLDS. Hölder gives log-convexity in the time; the bulk subtraction is affine. |
| P3 | 490–491 | HOLDS. Apply P1 to the four coordinates, starting from their minimum. |
| P4 | 492–495 | HOLDS. The right bound is P1; the left is the increasing-secant-slope inequality and nonnegativity of Delta. |
| EQC (i), (ii), integer form | 503–518 | HOLDS. At s=ceil(t/2), t-s>=t/3; the auxiliary box costs at most 16 C_1 M. Thus 48 C_1 M is valid. Changing one coordinate at a time and rounding each endpoint gives precisely the stated 4/N. |
| ASC | 520–526 | HOLDS. A finite net makes the diagonal subsequence uniformly Cauchy; continuity of the approximants is unnecessary. |
| FLOW (a) | 534–548 | HOLDS. EQC and ASC on an exhaustion give local uniform convergence. The units are positive integers, as in the predecessor definition, so N_i/u_j→infinity implies N_i→infinity. |
| FLOW (b) | 536–552 | HOLDS. The integer ratios and convex interpolation weights converge to their real counterparts. |
| FLOW (c), UNI | 538–541,553–573 | HOLDS. The shorter-time bound controls the number of low levels and suppresses the high-level tail. Every subsequential spectrum has the same Laplace sum; successive removal of its lowest exponent and its integer multiplicity determines all finite levels. This argument applies separately to every real B; no uncountable diagonal extraction is needed. |
| FLOW (d) | 542–544,574–578 | HOLDS. EQC controls the change of scale and the extra rounding uniformly on a compact box. |
| FLOW (e) | 545,579–582 | HOLDS. The diagonal selects j>=n and N/u_j>=n. Local bounds follow by evaluating on x=a/N, not by assuming them for an arbitrary diagonal. |
| EE and critical lower bound | 584–593 | HOLDS. The lowest spectral level is finite and nonpositive since E>=0 at all times. Criticality at side 2b and the other three side comparisons give log(1+1/5041)<=8D_E(b). |
| E0 | 595–604 | HOLDS. For fixed T_0, the upper estimate -c_n<=g_n(T)/T and lower estimate -c_n>=(g_n(T)-g_n(T_0))/T squeeze the limit as T→infinity. Rounded times converge and preserve the same squeeze. |
| OM^c (a) | 607,613–617 | HOLDS. Uniform diagonal bounds give local bounds and a common local Lipschitz constant. FLOW(e), spectral closure and E0 preserve the defining conditions. |
| OM^c (b) | 608–609,618–621 | HOLDS. Rescaling sends levels to lambda e_r(lambda B), preserves the bounds at every b, and has inverse phi_(1/lambda). |
| OM^c (c) | 610–612 | HOLDS. Evaluation and E0 give the two spectral functionals' continuity. |

### 2. Theorem CR^c

**HOLDS AFTER CORRECTION**, conditional on the stated engine and dyadic
existence theorem. The first correction is at line 689: with
`u_j=l_1/a_j` and physical `l in P`, write
`N=l/(2a_j)=(l/l_1)u_j/2`, not `l u_j/2`. Alternatively declare `l_1=1`
and use dimensionless physical sizes throughout this proof. No estimate
or theorem conclusion changes.

The five numbered clauses check as follows.

1. **(1) iff (2): HOLDS** given Theorem ZD-c in its repaired form.
2. **(2) implies (3^c): HOLDS** after the units correction. S3' supplies a
   uniform strict margin on *every* large integer cube. The rounded time
   ceil(N_i b/2) is at least half the rounded side ceil(N_i b). E0 then
   passes that margin to every blow-down, contradicting criticality.
3. **(3^c) implies (2): HOLDS.** The admissible dyadic sequence gives a
   locally bounded integer sequence by P3, at cost 16. If one real limiting
   cube had a seed, EQC and E0 transfer it to the nearest even lattice cube.
   Theorem S and S3' carry it to a larger dyadic cube, contrary to H2.
   This is a transfer to a fixed dyadic ratio, not an interchange of a
   limsup with an unbounded set of sizes.
4. **(3^c) iff (4^c): HOLDS.** Nonempty compact invariant sets contain a
   minimal set; a nested chain has nonempty intersection.
5. **(3^c) iff (5^c): HOLDS**, with the named compact-flow invariant-measure
   theorem as input. The empty space has no probability measure.

The last sentence, extending each member of Omega(D_0), **HOLDS**: apply
FLOW to its original admissible sequence. Its dyadic pointwise limit is
preserved by the further subsequence. The same even-cube argument proves
criticality at every real size. No assertion of uniqueness from dyadic
values alone is needed.

The decimal estimates at 704–707 can be replaced by this exact hand bound.
For 0<=x<2, the bound n!>=2^(n-1) for n>=1 gives
`exp(x)-1 <= x/(1-x/2)`. Hence
`c_S <= (64/5009)^2` and
`q_1=5041c_S <= (4544/5009)^2 < (10/11)^2 < 5/6`.
The last comparisons are `11·4544=49,984<50,090=10·5009` and `600<605`.
Also `(5/6)^4=625/1296<1/2`, so `q_1^32<1/256` and
`q_1^32/71<1/(256·71)<1/5041`. This proves exactly the margin used at
the factor-64 transfer; no floating-point evaluation is used.

### 3. VIR, KB, ENT and ENT-lat

**Proposition VIR (V1)–(V8): HOLDS.** The convention for an infinite level
is zero weight and zero contribution to the energy/entropy sums.

| Clause | Checked argument |
|---|---|
| V1 | For every derivative order, a polynomial times exp(-T e) is bounded by a constant times exp(-T_0 e/2) for e>=0 and T>=T_0. Negative levels are finite in number. Termwise differentiation on compact time intervals is justified; the first two derivatives have the asserted mean and variance. |
| V2 | The same tail estimate makes sum p_r abs(e_r) finite. Substitution of log p_r yields H=E+T<e>; H is finite. |
| V3 | Quotient differentiation gives -H/T². This is nonpositive since H is the entropy of a discrete probability law. |
| V4 | The two supporting-line inequalities at b/2 and 2b, and the three other side comparisons, give exactly -D(b)<=tau(b)<=16D(b/2)-2D(b). |
| V5 | For moving B_n the functions E_n(t,B_n) converge locally uniformly to E(t,B). Convex secants above and below the derivative squeeze it to E'(T,B). |
| V6 | The four-edge path from (b,b,b,b) to (lambda b)^4 yields the listed B_i, with oriented integrals also when lambda<1. |
| V7 | V5 gives joint continuity of the four partial derivatives. On the diagonal symmetry makes each derivative the same; dD(e^s)/ds=-4tau(e^s). |
| V8 | Spectral rescaling preserves the Gibbs weights and multiplies each energy by lambda. |

**KB: HOLDS.** On Omega^c the observable tau(1) is continuous and bounded;
V7–V8 give a bounded time integral. Fubini and invariance yield zero mean.
Existence of the measure is not needed for this implication; it is needed
when applying it to a nonempty compact invariant set.

**ENT (i), (ii), equivalence: HOLDS.** An invariant probability on a minimal
set has full support. A continuous one-sign tau with mean zero vanishes
there. V8 then gives vanishing at all b; V7 makes D constant on each orbit,
and orbit density makes that constant common to the minimal set. Otherwise
tau takes both signs. Thus strict positivity everywhere is impossible on
a nonempty Omega^c, and is vacuous on an empty one. The claimed equivalence
is precisely conditional on BDD-Delta and CR^c.

**ENT-lat implication: HOLDS.** At every limiting critical cube D>=d_min,
so the finite-lattice condition eventually applies. Convexity telescopes
backward k steps with each drop at least c/N. First pass to the local
uniform limit at fixed h, then send h down to zero: tau>=c. V7 would make
D negative along a sufficiently long forward scale orbit. This contradicts
E>=0. The lattice hypothesis is sufficient; no converse to it is proved.

### 4. CE-II and NR-II

**CE-II (i): HOLDS.** FIN makes every d(k) finite. Failure of an eventual
bound forces infinitely many strict records tending to infinity. At each
record, the upper limsup bounds on the finite preceding list hold
eventually, while approximation from below at the record holds infinitely
often. Their intersection supplies j_i. Discard finitely many initial
records so d(k_i)-1/i>0 when defining eta_i.

Final label after comparison with Opus: **HOLDS AFTER CORRECTION**,
because that finite-record deletion must be stated in the construction.

**CE-II (ii)(a), (b), (c): HOLDS.** P3 controls the larger scales and the
record condition controls the smaller dyadic scales. The four finite
comparisons are homogeneous under division by M_i, so EQC/ASC still apply.
At 1 the normalised value is exactly 1. For b<=1, compare up to 1 for the
lower bound b^4 and down to the preceding dyadic point for the upper bound
16. For b>=1, compare up from 1 for the bound b^4.

**CE-II converse and LIOU-II: HOLDS only with the written condition (i).**
The upper bound `M_i<=D^+(2^k_i l_1)+1/i` is essential. Under BDD-Delta it
contradicts M_i→infinity. An arbitrary moving-scale sequence with large
finite-j spikes need not obey this upper bound. Exact replacement for the
shorthand at 838, 891 and in the RESULT: "there is no record sequence
satisfying (i), with its normalised limit from (ii)."

**NR-II (1): HOLDS.** For alpha in [0,3], the power in the active coordinate
is alpha-3<=0, hence convex and scaled by at most lambda; the other terms
are linear. On the diagonal the value is b^alpha. The separate constant
1 also meets every clause. These are examples of the retained properties,
not realised FIN families for all alpha.

**NR-II (2), many vacua and lines: HOLDS** as unit-scale examples explicitly
*outside* FIN. In the first example, the log-sum differs from log m_i by
at most epsilon_i times the volume, uniformly on compact rescaled boxes.
For the lines example the binomial expansion supplies integer spectral
multiplicities and a simple largest eigenvalue; the bulk infimum is zero.
The displayed profile follows by dividing its four terms by N_i³.
For its record inequality one need not use the decimal at 889:
`log(1+1/e)>1/(e+1)>1/4` because e<3, so
`3log(1+1/e)-1/2>1/4>0`.

**NR-II (3): HOLDS AFTER CORRECTION of scope**, not as a proved example:
"A broken-continuous-symmetry model is recalled as a possible FIN example;
no such model or asymptotic is proved here." This clause cannot support
the claimed obstruction with FIN.

The broad inference at 892–899, 960–961 and the RESULT **FAILS as a proved
no-go claim, first failing inference at 892**. Its corrected form is:
"Properties (a)–(c) alone do not exclude these profiles. This
does not rule out further consequences of spectral integrality, FIN,
record realisability or the Wilson measure." NR-II's two realising families
violate FIN and are not the sequences in CE-II(i). "No soft proof on torus
data" claims a larger family than the argument treats.

### 5. T23 and one-side recurrence

**T23 (a)–(d): HOLDS.** An additive subgroup of R either has arbitrarily
small positive elements, making it dense, or has a least positive element
and is cyclic. A cyclic group containing log 2 and log 3 contradicts
unique prime factorisation. Continuity then extends two-map *group*
invariance to flow invariance, for closed sets, probability measures and
fixed points. The equalities `sigma_i C=C` matter; density of positive
powers alone is not the argument.

**T23 (e): HOLDS AFTER CORRECTION.** Replace 646–649 by:
"On Omega^c(16D_0), define (RIG-23) to exclude nonempty closed minimal
sets invariant under both phi_2 and phi_3. By (b) and CR^c this is (W).
No identification with a separately defined lattice sampling limit set
is asserted." For *observations* on the grid
`{2^i3^j:i,j in Z}^4`, the common EQC modulus uniquely extends a convergent
bounded family to real arguments. But the author has not defined which
base scales and criticality conditions its alternate lattice sampling
uses. In particular, positive powers with i,j>=0 are not dense locally.
This affects the phrasing of RIG-23, not CR^c.

**T23 (f): HOLDS AFTER CORRECTION.** The constants log m are correctly
realised by the finite-vacuum data; choose units and N_i so that
`N_i/u_i→infinity` as well as `epsilon_i N_i^4→0`. For the sum clause add
at 638: "both limits occur along a common subsequence (j_i,N_i), with
N_i/u_i→infinity for both families, and sup_b D_E'(b)<infinity."
The product spectrum is the pairwise sum of the two spectra, so
`1+S_(E+E')=(1+S_E)(1+S_E')` and D adds. Without the finite bound on D_E',
this calculation does not establish a critical element *with a finite
bound*. No counterexample to the bounded version is claimed.

The conclusion at 658–665 is **HOLDS AFTER CORRECTION of scope**:
"Two-map invariance alone adds nothing to flow invariance here; the
constant examples prevent it alone from excluding critical data. No
impossibility theorem for other rigidity arguments about this flow is
proved." Being part of a continuous flow does not, by itself, rule out
rigidity theorems with further hypotheses.

**The two by-products at 672–678: HOLDS** with the source's stated scope.
CR^c supplies real-size limits. P3 transfers upper bounds between
geometric size ladders with a fixed ratio cost. This does not remove S0
from CR^c or supply the account's trajectory/spacings.

**Z4 (a), (b): HOLDS.** For any shape translate y=tau^a E, recurrence and
monotonicity force Lambda(sigma_c y)=Lambda(y). All four intermediate
inequalities must then be equalities. Commutation permits each tau_i to
be last; applying this at tau_i^(-1)y covers negative exponents as well.

**Z4': HOLDS.** Strictness forces tau_i E=E. In each direction, constancy
along times 2^kT excludes negative lowest energy. Letting k→infinity
leaves the integer multiplicity of the zero level. The spectral sum at
every T is that same integer. Repeating in the other directions gives
one constant log m; criticality forces m>=2. Symmetry at 811 can be
replaced by repeating this argument, so the stated directionwise
spectral hypothesis suffices even if X was not explicitly symmetric.

**A4's necessity reading: HOLDS.** JOINT with strictness forces all
recurrent members to be constants. This is a necessary condition, not
a proof that no such functional can be constructed for the actual SU(2)
family. The photon comparison in 817–820 remains labelled GUIDE.

### 6. Lemma SURF and the variational wording

**SURF: HOLDS AFTER CORRECTION of the auxiliary tiling.** At 427 write
"k_i>=2 in every direction." The first incorrect auxiliary assertion is
437–442 if a direction has k_i=1: crossing that cell boundary then need
not enter another cell. In particular, if all k_i=1, nu=mu_N, and the
claimed mean-zero boundary plaquettes are ordinary plaquettes of mu_N.
The restriction is harmless: the proof only needs M_i=N n_i with n_i>=3.

With that restriction, a crossing plaquette has a single link in an
independent neighbouring cell. Integrate a gauge transformation at that
link's tail in the cell's torus. No other factor of this plaquette is in
that cell, so Haar averaging makes its trace zero. The number of internal
plaquettes per cell is `6N²(N-1)²`; subtract from `6N⁴` to get
`6(2N-1)N²`. Jensen gives the displayed lower bound on F(M)/|M|. For
every integer torus n, coordinatewise monotonicity gives
`F(n)/|n|>=F(Nn)/|Nn|` and the latter has the same lower bound. Taking
the infimum over n proves SURF. The last upper bound uses xbar_N<=1 and
beta>=0. No assumption about the sign of xbar_N is needed for this last
comparison; the first inequality and D>=0 already force its sign here.

**Relative-entropy identity at 447–450: HOLDS as a conditional identity**
with the specific-relative-entropy/pressure identity explicitly named
as input. It was only recalled in the source and is not rebuilt here.
Block-periodic versus translation-invariant versions may be matched by
averaging the finitely many translates; this does not change specific
entropy or energy density.

**A5's exact equivalence and precision: HOLDS AFTER CORRECTION.** For a
strict seed threshold delta, `D<delta` is equivalent to `N⁴h>Q-delta`,
where `Q=6beta(2N-1)N² xbar_N`. The weak inequality in 276 gives only
`D<=delta`; a uniform strict margin must be retained for a strict limsup
seed in this exact formulation. This is a correction to the asserted
rewriting, not a counterexample to a seed implication using additional
slack in the engine. Replace the "relative precision 1/N" at 413,465,1024 by
"absolute error of order N^(-4) per site; relative error of order N^(-3)
when the boundary term is of order N^(-1)." Without a lower bound on
beta xbar_N, use the absolute-error wording only. At 450 replace
"both terms are of order" by "the boundary term is at most of order
beta/N; the identity alone gives no matching asymptotic for h."

**Dynamic-control claim at 451–453: HOLDS AFTER CORRECTION of provenance.**
The inequality for Phi follows directly by using the 16-cell trial law
in the finite Jensen bound. It does not verify a Boue–Dupuis formula on
SU(2), an admissible product control, or its cost. Replace the dynamic
assertion by that finite variational inequality, and retain the control
interpretation as unproved.

### 7. Verdicts on ideas A1–A10

Here a route rejection is distinguished from refuting its needed SU(2)
inequality. These verdicts apply to the exact kills in 409–418 and their
restatements, not to every possible method in the named field.

| Idea | Verdict | First issue or exact supported rejection |
|---|---|---|
| A1, 227–234,409 | HOLDS AFTER CORRECTION | T23 supplies no extra obstruction from the two scalings on Omega^c. Use the precise real-flow definition of RIG-23 in section 5 above; the grid identification at 646 is not established as stated. No general no-rigidity theorem follows. |
| A2, 236–244,410 | HOLDS | ENT+ is equivalent to emptiness, hence to (W) given BDD-Delta. The lattice hypothesis is a sufficient strict drift, with no supplied mechanism. A claim that ENT-lat itself is equivalent to (W) would go beyond the proof. |
| A3, 246–254,411 | HOLDS AFTER CORRECTION | CE-II restates the failure of BDD-Delta through record sequences. NR-II defeats (a)–(c) alone; it does not refute every FIN-based argument. First overbroad inference: 892. |
| A4, 256–264,412 | HOLDS AFTER CORRECTION | Z4 gives the necessary recurrence condition. This rejects the proposed argument without an additional mechanism, not the existence of JOINT on this specific trajectory. |
| A5, 268–277,413 | HOLDS AFTER CORRECTION | The static inequality is a re-expression of a small-D seed, after the strict-margin and precision corrections above. The dynamic formula has not been verified. |
| A6, 279–286,414 | HOLDS AFTER CORRECTION | The literal concavity proposal can be excluded as described below. The asserted curvature ceiling and leading cos²t term at 414 are not a proved justification in this note. They must not be promoted from ARGUED. |
| A7, 290–298,415 | HOLDS AFTER CORRECTION | A qualitative rate c(L)>0 carries no growth bound for z^-(L) as L grows. Moreover, a Langevin Wasserstein rate has no automatic equality with the Euclidean transfer gap. The source supplies neither that comparison nor a useful L-dependent rate. Reject this supplied bridge, not all weak-Harris approaches. |
| A8, 300–311,416 | HOLDS AFTER CORRECTION | The naive conditional mark law fails the lattice FKG condition on frustrated backgrounds; conditioning on all U instead makes the Wilson observable fixed. The claim that this construction reads *only* Z_2 is false: its weights depend on the SO(3) field and beta. Sharing the centre with Q_8 or 2T alone is not a counterexample under matching premises. |
| A9, 313–320,417 | HOLDS AFTER CORRECTION | No required monotone comparison or quantitative carrier is supplied. Absence of FKG is not a theorem excluding every monotone coupling. Replace "would have to equal" by "must be no larger than" the lattice-spacing ratio, as the proposal actually states. The U(1) test is a selectivity test, not a refutation for SU(2). |
| A10, 322–330,418 | HOLDS AFTER CORRECTION | The needed covariance resolvent is that of the operator on field-dependent vector functions, including -L. A resolvent of the frozen matrix M(U) is a different object. No comparison is supplied. Delete "has no analogue here": off-diagonal, dependent disorder does not itself prove that universal negative assertion. |

For A6, one can test the desired conclusion without the uncomputed cube
coefficient. The definition of C2 in `gap-invent-selective-max.md:105–107`
is a common SU(2) corner insertion g on the sheet. Its partition function
is a smooth class function. For c²=-1, g_t and g_-t are conjugate, as are
g_(pi+t) and g_(pi-t). Thus `f(t)=log Z(g_t)` has f'(0)=f'(pi)=0.
A differentiable concave f on [0,pi] with these endpoint derivatives
must be constant. Yet the central endpoints are Z and Z_tw. In the
standard transfer representation (TM-c),
`Z-Z_tw=2 Tr(T^n P_-) > 0` for beta>0: the winding fundamental loop is a
nonzero odd gauge-invariant function; the electric convolution has
strictly positive character coefficients at beta>0, so T has a positive
quadratic form on that odd sector. The coefficient positivity follows by
expanding exp((beta/2)chi_(1/2)): tensor powers have nonnegative integer
multiplicities and every spin occurs in some tensor power. Multiplication
by the positive spatial weight does not introduce a kernel. This proves
nonconstancy given the named transfer representation. It is an exact
endpoint obstruction, not a numerical or leading-order proof. It says
nothing about alternative interpolation inequalities with error terms.
This uses existing transfer ingredients: `gap-transfer.md:127–157` and
the account's GL3/GL8, not a new positivity argument claimed as original.

For A8 the limited FKG obstruction is elementary. Fix a quotient
background with a frustrated cube, and write its plaquette constraints
as products of centre link signs equal to prescribed signs. All six
constraints around that cube are inconsistent when their product is -1;
each proper subset is consistent. Two such proper subsets can have all
six as their union and a consistent intersection. Their conditional
mark weights are positive, while the union has weight zero. This
violates the lattice condition `w(A union B)w(A intersection B)>=w(A)w(B)`.
Such quotient backgrounds exist: in an embedded U(1), choose the six
outward plaquette angles to be pi and five copies of -pi/5. Their sum is
zero, so they are a lattice curl on the cube; exactly one trace is
negative. The signs persist on an open neighbourhood. This argument
does not establish failure of FKG for every *unconditional* mark marginal
after averaging the quotient background, nor a no-go theorem for OSSS.

### 8. Coverage and source scope

Sections 0–2 (1–216) were read for provenance, definitions and prior-work
claims. Their historical logs and broad novelty searches were not
reproduced. The mathematical statements imported from the named earlier
notes remain conditional inputs; their whole dependency closures were
not checked. Section 4's literature catalogue was read as an explicitly
abstract-only/recalled catalogue. I did not verify its bibliographical
metadata, recent papers, or theorems not used above. It supplies no
additional proof here. F1–F8 are credited prior-route pointers, not new
numbered theorems checked by this report.

Sections 3 and 5 have the ten separate verdicts above; 5.2 has its own
proof check. Every named statement and numbered clause of 7.1–7.5 is
covered above. The numerical comparisons used by the new real-scale
proofs were replaced by written rational bounds where needed. Sections
6 and 8 are steering and summaries; their mathematical assertions must
carry the same corrections, especially the NR-II no-go wording and the
claimed universal rejection of entire A6–A10 method families. The open
question at 667–670 remains open; this check attempts no new research
on it. No mass gap or seed for SU(2) is obtained.

I first read `sa-index/README.md`, searched the chunk files and
`obligations.md` for the objects, and read the neighbouring scope rows
in chunk-01:65–72 and chunk-29:72–78. The corresponding outline source
passages read were 565–600 and 31858–31882. They distinguish scalar
non-Gaussianity from gauge-theory identification and explicitly keep
a mass gap separate from polynomial decay. They do not supply the
present seed or an invariant-set exclusion. This is a local scope check,
not a claim that a search proves absence from the entire account.

The `ca-4.12-4.19` README and targeted searches concern constrained
backgrounds and stage admission; none is an input to row 1031's proofs.
The complete numbered index likewise supplied no direct locator for
Casimir/thermal-entropy/scale-shift/uniform-recurrence statements. CA-I
was downloaded as requested but no CA-I proof is imported. Balaban's
papers were neither opened nor copied. Credit Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their text, for the account
and trajectory; credit Tadeusz Balaban for the underlying RG method.
No claimed result here is credited to them merely because it appears
downstream of their trajectory.

For the A6 replacement argument I additionally followed the GL3/GL8
index rows and their neighbours (`chunk-02.md:83–103`) to outline
2195–2231 and 2315–2335. They give strictly positive one-bond spectral
coefficients and the gauge-projected transfer construction. Credit these
ingredients to Sussman and Alpoge, with Claude and Codex as text authors,
and the existing `gap-transfer.md` port. The centre-twist trace identity
is the separately named TM-c input in `gap-crux-restate.md:35`.

Own verdicts through this section were saved before opening
`gap-afield-a-check-opus.md`. The comparison follows only after this save.

## Comparison with Claude Opus 5.5

Here **O** means lines of `gap-afield-a-check-opus.md`; **A** means lines
of `gap-afield-a-max.md`. Every difference in verdict or coverage found
in that check is listed below. Agreement is not a second proof path by
itself; the arguments above were formed before reading O.

1. **P4: Opus is right about the rendered statement.** O49,304,341–343
   identifies that A493 begins a Markdown sub-list. Its mathematical
   minus becomes a bullet. My first verdict judged the intended signed
   inequality and said HOLDS. Final verdict: **HOLDS AFTER CORRECTION**.
   Replace A493 by inline code or a display containing
   `Delta(t',B)-Delta(t,B) >= -((t'-t)/(t-s))Delta(s,B)` together with
   the unchanged upper bound. The proof at A494–495 already has the
   correct sign. This changes presentation, not EQC.

2. **CR^c units: this check is right; Opus missed the correction.**
   O93,113–114,134,312 accept `N=l u_j/2`. A683 reads the setting of
   `gap-dichotomy.md:92–98`, where l is a physical size and u_j=l_1/a_j.
   A689 therefore needs `N=l/(2a_j)`, or the explicit convention l_1=1.
   S0 does not make an arbitrary physical l times u_j an integer. The
   five equivalences survive with the correction in section 2.

3. **Displayed decimal verification: Opus's conclusion is right, its
   displayed arithmetic is not an exact hand certificate.** At O123,
   `64/5041=0.012696` is a rounded upper approximation, not equality.
   At O124, `5041·1.64·10^(-4)=0.8267` is also not equality: the product
   is 0.826724. The required strict inequalities nevertheless hold.
   Use section 2's exact factorial/geometric-series bound, which proves
   the seed transfer without these rounded assertions. At O230 the
   decimal logarithm is likewise unnecessary; section 4 gives a written
   positive lower bound for NR-II's derivative. No theorem fails here.

4. **T23(e): no mathematical disagreement, but the label needs its
   qualification.** O91,96–103,338–340 and this check agree that the
   implication on Omega^c holds and the other grid limit set is undefined.
   I use HOLDS AFTER CORRECTION for the whole labelled proposition,
   rather than HOLDS on the restricted interpretation. Opus's proposed
   grid repair is explicitly unproved and is not used here. Neither
   checker has verified that alternate lattice-sampling construction.

5. **T23(f): this check makes explicit a missing finite-bound hypothesis
   which Opus left implicit.** O92,105–110,310 prove the product spectral
   identity but do not justify finiteness of `sup_b D_E'(b)` in A639.
   A538–545 and the definition of BB impose only local boundedness;
   A589 requires a finite global critical bound. Thus the product
   calculation is right, but the conclusion needs the finite bound
   stated explicitly. Opus is right that pairing the two subsequences
   and reindexing the product family is harmless; this is the common
   indexing convention requested in section 5, not another obstruction.

6. **CE-II initial records: Opus is right about the final label.** O206,
   319,347–348 require deletion of the initial records for which
   d(k_i)<=1/i. My own argument already made that deletion but labelled
   (i) HOLDS. Final label is HOLDS AFTER CORRECTION, with exactly that
   sentence added at A842. There is no disagreement on (ii) or the
   converse. Both checks keep the upper-limsup clause in (i).

7. **NR-II: agreement on the failure and the narrower repair.** O212,
   233–241,322,330–337 and this check reject the broad PROVED no-go claim.
   Its first substantive overreach is A892; O emphasises A1057 and the
   title A857. The proved result only defeats properties (a)–(c). Also
   replace the title "exclude no growth rate" by "admit the displayed
   profiles": (c) itself excludes growth above b^4, and no profile for
   every alpha in (3,4) is supplied. NR-II(3) stays recalled and unchecked
   by both readers. Calling its role conditional is not a verification.

8. **SURF and its interpretations: agreement on the inequality; this
   check adds corrections to surrounding claims.** O247,262–275,344–346
   and section 6 agree on k_i>=2 and on the conditional entropy algebra.
   O249 correctly promotes the *finite Phi inequality* to HOLDS; my
   correction concerns the unverified control interpretation, not that
   inequality. O did not check A276's strict-margin quantifier or
   A413,465,1024's relative-precision claim. Their corrections in section
   6 are required by the displayed identity; Opus did not endorse or
   refute them.

9. **A1–A10 route scope: additional coverage, not an Opus endorsement.**
   O191 and O289–291 explicitly leave the argued readings and A6–A10
   outside its check. Its RESULT cannot be used to certify those kills.
   The ten verdicts in section 7 are this check's conclusions. In
   particular, the A6 endpoint obstruction is narrower than a ban on
   curvature methods; A8's common-centre argument is invalid; A9's
   no-coupling assertion and A10's "no analogue" exceed their evidence.
   For A1–A5, agreement on the underlying lemmas does not justify a
   universal no-go claim for the whole named field.

There is no remaining disagreement about EQC, ASC, FLOW, UNI, E0, OM^c,
VIR V1–V8, KB, ENT, ENT-lat, Z4, Z4', or NR-II(1)–(2). For the minor
z-bound remark A592–593 that O291 did not cover, the spectral tail gives
`S(b/2;b³)<=exp(64D(b/4)-z(b)/4)`; criticality yields
`z(b)<=256D(b/4)+4log5041`. This is the exact bound behind the decimal
version in the predecessor. No new dynamical estimate is contained in it.

## Final disposition

Theorem CR^c holds after the units correction, conditional on its named
inputs. VIR, KB, ENT and ENT-lat hold. CE-II holds after deleting finitely
many initial records and preserving condition (i) in every shorthand.
SURF holds after restricting the auxiliary tiling. T23 requires the grid
and finite-product-bound qualifications. P4 needs its rendered sign
repaired. NR-II's examples hold; its unrestricted no-go inference fails.
The ten ideas supply no proved SU(2) seed here, but the argued rejections
do not rule out entire method families.

No source text was repaired in place. Only this report was written.
No computational proof, numerical run, proof assistant, audit, status update,
commit or external post was used. The report remains local and unpushed
on `codex/gap-afield-a-check-astra-20261116`.

RESULT: Row 1031 checked line by line from the pinned text before reading Opus; the core implications HOLD or HOLD AFTER CORRECTION as listed, NR-II's broad no-go claim FAILS at line 892, and A1–A10 require the stated scope corrections; no mass gap, no seed, no status grant; (W), (BDD-Delta) and (LIOU) remain open.
