# Repo search

Provenance: Codex, gpt-6-astra, xhigh; FINISH row 896; source checkout
`bb841b67d05fd9924f68a0c1bb347875b7585f49`; 2026-11-13. Research-text check,
not an audit. This file grants no status. Author checked: Claude Fable 5.2
max, `library/gap-glue-max.md`, all 354 lines. Below, **A** means that file;
other unqualified paths are relative to this lane.
Author-file SHA-256:
`32304a1784cb14c4b441afc47fea5fa93a6fc4e933b0766ebb8ac9a91075e68e`.

`library/prior/gap-glue-check-astra.md` does not exist. This was checked before
any other source read. This output file was created in the first tool call.
The November 8 repository digest was read in full. It covers other targets;
its conditional RG and covariance results supply no glue seed. FINISH row
896 has no separate "Repo prior work" entry. Target-specific searches of
`open-registry.md`, `open-core.md`, and `l17c.md` returned no glue/thermal-sum
assignment. Row 895 owns the author text; row 896 explicitly requests this
check. No new proof lane or reassignment is made.

The requested five refs were searched using bounded `git grep -n -i -E`
commands over `*.md` and `*.tex` in `/Users/jonreilly/Projects/Physics`:

| Ref | Revision read |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

The completed narrow global expression was
`GLUE-FP|gap-glue|zero.flux gap|centre-even|maximal correlation|Casimir free energy|gap.times.count|Lemma FIB`
(head 40; six hits, all on pr/10134). There were no hits for the target's
names. Earlier broad expressions containing `Casimir`, a bare numerical
constant, or `BETA._C` were swamped by unrelated representation/normalization
notes. Those capped searches establish no absence. A method search used
`thermal sum|Feynman.Hellmann|ground.state transform|direct.integral|centre.blind|center.blind`;
its global list was capped. A bounded follow-up in the soft YM4D route and
`research/ym4d/` located the transfer construction below. Unrelated Casimir,
ordinary integral, and gravity Feynman-Hellmann matches are not suppliers.

| Relevant hit, actual source read | Exact statement and closeness |
|---|---|
| pr/10134, hard-route `library/convex-maximal-correlation.md`; local current file read whole; pr/10134 `parts/upper-chain.md:1376` | If `S_xx >= A_x`, `S_yy >= A_y`, and `norm(A_x^-1/2 S_xy A_y^-1/2) <= r < 1`, then `abs(Cov(F,G)) <= r norm(F)_2 norm(G)_2` for centered functions. A conditional convex-law bound, not the Wilson even-sector gap or Lemma MC's exact Markov identity. Credit Gebelein, Bakry–Emery, Prekopa and Brascamp–Lieb as the source does. No convexity input is manufactured here. |
| pr/10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CONSTRUCTION_ASTRA.md:125–215` | The ground-state transform is reversible for `psi_0^2 dU`; minorization gives `lambda/lambda_0 <= 1-exp(-2 beta n_s)` and `m=-a^-1 log(1-exp(-2 beta n_s))>0`. Exact finite-volume construction, explicitly not a volume-uniform gap. This already supplies the transform and an extensive comparison bound used in A's bridge discussion. |
| Local `library/gap-seed-shape.md:44–110` | `g(t;B^h) <= h/(b-t) g(t;B)` for `h>=b>t>=3`; spectral time monotonicity and the SH recursion. These are the actual inputs of G5 and UP, reused below. |
| Local `library/gap-es1-opus.md:30–64` | Twisted trace representation, sector positivity, permutation symmetry and the crossing identity `Z_0(a;A')=(1/4) sum_z Z_z(2a;A)`. G4 is a specialization of this existing crossing method, not a new structural input. |

The SA-index README, chunk-02 rows 85–106, chunk-06 rows 58–72, and the
matching obligation entries were read before source lines. At the supplied
SA revision `31a47c543775`, outline 2195–2257 proves the positive convolution
coefficients `c_l=2 exp(-beta) I_(2l+1)(beta)/beta>0`; 2313–2338 constructs the
positive trace-class transfer and `Z_s=Tr L^s`; 6836–6869 defines first-passage
data and the exact change of lattice units. These are credited to Sussman
and Alpoge, with Claude and Codex as authors of their text. They supply the
finite transfer and the scaling dictionary, not GLUE-FP. The index explicitly
keeps the physical mass gap separate from a scalar block gap. No Balaban
estimate is needed by the checked algebra; none is imported from memory.

# Statement checks

Research-text check only; no scientific or audit status is granted. No computational run discharges a claim.

Verdicts cover the written statement and distinguish it from its subsequent
interpretation. HOLDS means an implication from the specified class inputs,
not a proof that the first-passage Wilson theory satisfies an open input.

## 1. G1 — HOLDS

A:110–114. Each even excited ratio lies in `[0,r_1]`, with `r_1<1`.
For `0<t_0<a`, termwise domination gives
`sum_i r_i^a <= r_1^(a-t_0) sum_i r_i^t_0`; retaining the first term gives
the lower bound. Including odd sectors gives `S_ev(t_0)<=S(t_0)`.
The diagonal terms of the product of the two nonnegative sums give
`S_ev(t+t')<=S_ev(t)S_ev(t')`. All sums converge for positive integer times.
For an empty excited even sector, take the sums and `r_1` to be zero.

The phrase "gap and count" describes a sufficient estimate, not an
equivalence with a prescribed shorter-time count. A small sum at time `a`
alone does not bound a shorter-time sum uniformly.

## 2. G2 — HOLDS; fixed-threshold equivalence needs correction

Write `x_t=S_ev(t)`. Then
`D_ev(a,s)=log(1+x_a)+log(1+x_s)-log(1+x_(a+s))`.
Since `0<=x_(a+s)<=x_s`, both displayed bounds follow. Also
`Z(a+s)<=lambda_0^a Z(s)`, so
`Z_0(a)Z(s)/Z(a+s)>=1+x_a`. No parity information is lost in this last
inequality because the numerator still contains `Z_0(a)`.

For `s=a`, `D_ev<=log(1+sigma)` suffices for GLUE at level `sigma`;
GLUE implies only `D_ev<=2 log(1+sigma)`. Thus A:8.1's "all PROVED
equivalences" is false at the same numerical level. Exact equivalence is
`lim_(s->infinity) D_ev(a,s)=log(1+x_a)`, or the spectral identity itself.
The vacuum is simple and the trace is summable, so dominated convergence
justifies this limit. The two inequalities in G2 remain correct as printed.

## 3. G3 — HOLDS

Use the gauge quotient, or the invariant subspace of the slice space.
Multiplication by the normalized positive vacuum is a unitary map from
`L^2(nu)` to the transfer Hilbert space. It carries the invariant constant to
the vacuum and intertwines the centre actions. Thus `P^s P_0` has spectrum
`1,r_1^s,r_2^s,...` on the even subspace and zero on its orthogonal
complement. Subtracting the projection onto constants gives
`||P^s P_0-Pi_1||_HS^2=sum_(i>=1)r_i^(2s)`.
Its kernel is `pbar_s-1`. Averaging over the group gives the quotient
transition density relative to the pushforward of `nu`; stabilizers require
no division by orbit size. Integrating its squared deviation proves both
chi-square formulas. This is the stationary ground-state chain, not a finite
time-ring marginal.

The mixing identity is exact. It does not identify every even function as
local, nor turn a single finite-box statement into a bulk mass gap.

## 4. G4 — HOLDS AFTER CORRECTION of its interpretation

The crossing identity and the displayed bound hold. Relabel time as direction
2. Summing the old `k_2` gives `2P'_+`; summing `k_3,k_4` gives the four
magnetic twists. The original factor `1/8` therefore becomes `1/4`.
Dividing by the untwisted vacuum factors yields exactly

`1+S_ev=exp(Cas) A_cross`, where `A_cross=(1/4)sum_m sigma_m`.

Sector positivity and the untwisted even vacuum give `A_cross>=1/4`.
Consequently GLUE at level `sigma` implies only
`Cas<=log 4+log(1+sigma)`, as G4's own display correctly states.

**D1: the subsequent thermodynamic reading drops a necessary factor.**
The sentences claiming `Cas<=about log 1.1`, "no Casimir energy", and
separately small even/twisted traces do not follow. Smallness bounds the
product, not each factor. A's own proposed deconfined profile
`sigma_0~4`, `sigma_m~0` for nonzero `m`, `Cas~0`, has `S_ev~0` but a
`C'_1`-even excited trace near 3. A small glue sum therefore does not force
that trace to be small. The permitted exact reading is the product formula
and the bound with `log 4`. The pressure estimates and 8.1–8.2 must retain
this distinction. No stronger Casimir conclusion is proved by G4.

## 5. Proposition SEP — HOLDS AFTER CORRECTION of scope and witnesses

(a) HOLDS. Tensor-product traces, vacuum normalization and sector projections
factor exactly as written. The neutral factor has trivial centre action.
Its partition function multiplies both sides of a crossed-torus identity
by the same number, so the crossing identity is preserved as well.

(b) HOLDS with A:8.0(3)'s substitution. Reuse the compact Gaussian model of
`gap-seed-shape.md:223–244`, not an unproved assertion about Coulomb U(1).
Its explicit trace has a neutral excitation of energy `1/(2R^2 b^3)`.
Taking this symmetric model with trivial twists already gives `Q_0=0`
and a large even sum on `b>=24a`: choose `R=1`, so its one excitation
contributes at least `exp(-1/48)>=47/48>1/10`. A product can preserve any pre-existing
flux ratio while making its even sum arbitrarily large. This proves the
non-implication within the abstract class; it says nothing specific about
pure Wilson SU(2) along its first-passage trajectory.

(c) The proposed Z2 witness is valid on a fixed box, but A gives only an
ARGUED phase assertion. The missing finite-box justification already exists:
`gap-es1-opus.md:157–168`, Lemma Z2-c. It bounds every within-sector excited
sum by `d_chi[2(1+u)^E u^4]^a`, `u=exp(-2 beta)`, while each sector top
lies between `1-[(1+u)^E-1]` and `(1+u)^E` in the same normalization.
There is one flat vector per electric sector. For fixed `a,b`, letting
`u->0` therefore gives `S_ev->0` and each `q_i->4/8=1/2`. Finite dimension
makes these limits immediate from those bounds. Choose a sufficiently
large finite beta to get `S_ev<1/10` and `Q_0>1/20`. This reuses the existing
proof and supplies the other non-implication without a phase diagram.

Thus **neither one-box numerical half implies the other in the stated
class**. Do not upgrade this to a proof about every size at one fixed beta,
a continuum trajectory, or the specific SU(2) action. The mixed-action K7
paragraph is explicitly GUIDE, not a second rigorous witness. The Q8/2T
substitutes are false as blanket frozen-model witnesses; see section 14.

## 6. Remark UNTW — HOLDS AFTER CORRECTION

The positive eigenvalues, with multiplicities, are fixed by the power sums.
For example the finite measure `sum_i lambda_i delta_(lambda_i)` on a compact
interval has these as its moments. Its moments determine the measure by
polynomial approximation. Zero-eigenvalue multiplicity is invisible, and
should be excluded from the sentence.

The same untwisted family admits a trivial-centre extension: set all flips
to the identity and all magnetic-twist transfers equal to the untwisted
one. Then `S_ev=S`. Consequently a bound based **only on the untwisted
partition numbers and the stated abstract class axioms**, valid for every
such extension, also bounds the full sum. This proves the claimed
information limitation in that precise sense. It applies to the cited
untwisted D-shape proof.

**D2: it is not an impossibility theorem for one-box proofs.** A bound using
the known centre action, sector correlations, or the Wilson action's
additional structure does not satisfy that information-only premise.
G1/G3 themselves give such one-box formulations. Nor does failure of the
present enlarging argument prove that every possible enlarging theorem
needs flux. Replace "as a proof: only if volume-uniform" and "every
one-box proof proves both halves or nothing" by the restricted statement
about the existing untwisted-trace method. The need for additional inputs
in the listed consumers remains a fact about those consumers.

## 7. Lemma CS — HOLDS; its exclusion of other methods FAILS

For integer `3<=x<=x'`, trace-norm monotonicity gives
`log Z(x,y,c,d)/x >= log Z(x',y,c,d)/x'`. Divide by `y` and let
`y->infinity`, using the top eigenvalue in that direction. This gives
`e(x,c,d)/x>=e(x',c,d)/x'`. Hence
`Cas=ab[e(a,b,b)/a-e(b,b,b)/b]>=0`. Together with G4:
`1/4<=A_cross<=1+S_ev` and `0<=Cas<=log4+log(1+S_ev)`.
This is the earlier Lemma K sign, correctly reused.

D1 also affects A:203: its reverse inequality needs `log4+log1.1` in the
numerator. More fundamentally, listing several inequalities of one sign
proves no statement about **every** exact inequality of the class. The
claim that a reverse estimate can come only from a smaller seed or a
contraction is not established. CS supplies a sign, not a classification
of proofs or a prohibition of trial-vector arguments.

## 8. Lemma LOC — HOLDS for the stated support condition; its converse and method ceiling do not follow

If the omitted plane is the reference flip plane, the conclusion is
immediate. Otherwise the central gauge transformation on the strip between
the two planes changes signs on precisely those planes. On the support of
`f` it agrees with `C_i`. Gauge invariance proves `f(C_i U)=f(U)`.
Applying this separately in every direction proves evenness for supports
with the required cuts in all directions.

**D3: inclusion is not equality of sectors or of optimization problems.**
A:235 labels the converse ARGUED, but 8.1, 8.2 and RESULT use it as proved.
No density/separation proof is supplied for finite-beta SU(2). In the
comparison class it is false: the existing Q8/2T flat-holonomy witness
(`gap-crux-exercise2-check-astra.md:227–255`, reused in section 14) supplies
distinct even flat states on which all contractible local holonomies are
identical. A local mass gap need not remove global even states from a trace.
The zero-flux gap bounds local decay; equality with the lightest locally
accessible energy needs an additional cyclicity/overlap argument.

The numerical constants of the **unchanged** single-link or star method
remain unchanged. LOC does not prove that all local criteria, all choices
of gauge-invariant test functions, or every even-sector method have the
same optimal constants. In particular 0.3609 is a proved sufficient range,
not a demonstrated universal ceiling. The old 1/3 and approximately 0.775
obstructions concern their specified worst-case influence constructions.
Keep those scopes instead of claiming that local evenness rules out any
improvement. The conditional law inside a block can still depend on its
exterior; centre-blindness is an invariance, not independence of that data.

## 9. Proposition FIB — HOLDS AFTER CORRECTION; the exhaustive dichotomy FAILS

Commutation with every exterior multiplier makes a bounded operator
fibrewise. For a self-adjoint fibre operator, integrate its
Rayleigh inequality: a common lower bound on the complement of its kernel
holds globally if and only if it holds for almost every fibre. The global
bound is the essential infimum of these fibre bounds. For the norm, apply
the same argument to `A* A`, giving the essential supremum. Conversely, an
exterior set of positive measure with a violating fibre test can be
localized by its indicator; a countable dense family of fibre tests makes
the choice measurable. This proves the asserted essential extrema without
replacing an average by an infimum without justification.

**D4: regularity and the quantifier over tests are missing in the extension.**
An arbitrary bounded self-adjoint operator in the statement need not have
continuous fibres merely because the Wilson density is continuous. Fibres
are only defined almost everywhere. For example, on a torus with a
nonempty exterior take `A=I`, and change its representative fibre at one
exterior configuration to `(1/2)I`. This is the same global operator;
its essential bottom is 1, while the infimum of that representative is
1/2. Thus "ALL exteriors" needs a specified continuous version and a
continuous quadratic-form inequality. For finite heat-bath combinations
such versions can be supplied using the strictly positive continuous Wilson
densities. Test the inequality first on a dense continuous family and
extend by full support. The bare hypotheses on A do not supply this.
A heat-bath sweep is also generally not self-adjoint; use its norm or a
self-adjoint gap operator as appropriate.

The lemma concerns an operator inequality for **all** fibre-dependent
vectors. An averaged scalar estimate, a weighted estimate with a bad-set
term, or an estimate only for exterior-independent tests is a different
hypothesis. FIB does not convert these to worst-case bounds. Therefore
"every averaged condition is either the worst case or the claim itself"
is not proved by FIB and MC. They identify two particular formulations,
not every possible local-to-global method.

## 10. Lemma MC — HOLDS

For a stationary reversible Markov chain, conditioning the past and future
functions onto their boundary slices gives the displayed identity
`E(FG)=<fhat,P^w ghat>`. Conditional expectation is an L2 contraction.
On centered even functions, positivity and compactness give
`||P^w||=r_1^w`. An even first eigenfunction at each endpoint attains the
bound. For path functions, "even" means invariance under the same centre
action on the entire path; equivariance then makes their conditional
expectations even. This proves the exact maximal-correlation statement.

It is already a spectral-gap reformulation if the input demands a uniform
bound on this very maximal correlation. The broader exclusion of other
annealed criteria is D4, not a consequence of MC.

## 11. Lemma UP — HOLDS as an upper bound; "only with factor 1728" FAILS

The printed two enlargements cost `4^3` and `3^3`, so the displayed
`G_0(2t)<=1728 G_0(t)` is valid for integer `t>=3`.
It is not a necessary loss. The very same inputs give the stronger bound

`G_0(2t)=g(2t;(4t)^3)<=g(t;(4t)^3)<=4^3 g(t;(2t)^3)=64 G_0(t)`.

Here time monotonicity is used first, then E' enlarges each side from `2t`
to `4t` at time `t`. Thus neither a factor 1728 per doubling nor an optimal
power-law loss was proved. A bounded count at one fixed physical size does
propagate to any fixed finite number of doublings, with a finite constant
uniform in the cutoff. A uniform count at arbitrarily many doublings is
not supplied by this estimate. State that precise limitation instead of
saying COUNT never follows from a count at the first-passage scale.

## 12. Lemma G5 and its constants — HOLDS

Set `t=a/2>=3`. G1 gives `S_ev(a;b^3)<=exp(-m_ev t) S(t;b^3)`.
E' applies in each direction since `b>=a=2t>t`; it gives
`g(t;b^3)<=(b/t)^3 g(t;(2t)^3)`.
Using `S=exp(g)-1<=exp(g)` proves the displayed bound. At `b=24a`,
`(2b/a)^3=48^3=2304*48=110592`. If `G_0(a/2)<=G` and
`m_ev a>=2[110592 G+log(1/sigma)]`, the exponent is at most `log sigma`.
This is a correct sufficient condition, with exactly the printed constant.
Use `0<sigma<1` and preserve the integer/even-size requirements.

It is not the "weakest sufficient pair": the proof deliberately drops the
minus one in `exp(g)-1` and uses a full-sector count and a crude enlargement.
Nor does this pair alone certify Proposition W's additional half-time bound
`S_ev(a/2)<=1`. That is a separate hypothesis, or requires a further
application at half the time with its own gap/count estimates.
Theorem ZD-c (`gap-phys-seed.md:311–336`) already contains the full-sector
gap/count split and explicitly distinguishes its zero-flux component. G5
is a conditional even-sector specialization, not new progress on Z0 or
COUNT. The identification of its gap with the full local-observable gap is
subject to D3.

## 13. Proposition TR — HOLDS as a conditional comparison; its converse FAILS

On a complete multiplicity-preserving family of positive even branches,
`-E'/E<=C` integrates to `E(beta_1)>=exp(-C Delta beta) E(beta_0)`.
Exponentiation and summation give exactly the claimed comparison. The
vacuum branch is omitted throughout. At real times at least one, trace
class ensures summability of the ratios. A crossing between excited
branches does not affect the sum. Analyticity locally follows from the
analytic compact transfer family; for using this proof globally one must
follow the branches, with multiplicity, across the interval as stated.
The positive one-link coefficients in SA 2195–2257 ensure injectivity on
the physical invariant space for positive coupling, not on discarded
non-invariant gauge directions.

Corollary TR1 HOLDS AFTER CORRECTION of its formulation. It proves a
**fixed-bare-coupling seed**, conditional on one C uniform in the boxes
used. Enlarge C to be nonnegative if necessary, and let
`M=exp(C Delta beta)`. From the supplied strong-coupling seed
and SH, choose integer times n on the corrected shape `(n,(4n)^3)` with
`g_n=g(n;(4n)^3;beta_0)->0`. Set `a_1=ceil(Mn)`, `b=24a_1`. E' gives
`g(n;b^3;beta_0)<=[8(M+1)]^3 g_n`; TR and time monotonicity give

`S_ev(a_1;b^3;beta_1)<=exp([8(M+1)]^3 g_n)-1`.

Choose n so this is below sigma. To include W's separate half-time
condition, take `a_1=2 ceil(Mn)` and replace the enlargement constant by
`[16(M+1)]^3`; make the bound at half time at most sigma. This supplies
both requested numbers. No new independent count hypothesis is needed,
but the initial full seed and its enlargement theorem are still inputs.
Do not call this GLUE-FP without the cutoff comparison.

**D5: analyticity and nonclosure of the lowest gap do not imply the
all-level logarithmic-derivative bound.** A concrete counterexample to that
inference is an entire diagonal trace-class family with vacuum eigenvalue
1 and, for n=2,3,...,

`lambda_n(s)=exp(-n^4)[(s-2)^2+exp(-n^2)]`, `1<=s<=3`.

Every eigenvalue is positive, the vacuum is simple, and all excited energies
are uniformly bounded away from zero. At `s_n=2+exp(-n^2/2)`, however,

`E_n(s_n)=n^4+n^2-log2`,
`-E_n'(s_n)/E_n(s_n)=exp(n^2/2)/(n^4+n^2-log2)->infinity`.

Thus even a single such infinite-dimensional finite-volume family need not
admit one finite C for all levels. If a pointwise positive Markov kernel is
desired, use the bounded real trigonometric basis on a circle, take constant
vacuum, and these coefficients on its other basis vectors. The uniformly
summable kernel tail is at most `4 sum_(n>=2) exp(-4n)<1/2`, since
`n^4>=4n`, so the kernel is strictly positive.
This is a counterexample to the general analytic inference, not a claim
that the Wilson family violates BETA. Wilson needs a separate all-level
estimate. Likewise absence of a critical point is not equivalent to a
uniform derivative bound; it gives no control of rapid level variation.

The thermal differential inequality
`d_s X<=-C a d_a X`, `X=log(1+S_ev)`, follows when the indicated differentiated
sums are justified, term by term from `E'>=-CE`. It is weaker than a bound
on every branch; its converse is not proved. Its identification with a
continuum pressure/interaction-measure inequality is not supplied.

For first passage the relevant sufficient size control is
`sup_K a_K exp(integral C(s) ds)<infinity`, together with the initial-size
and count constants used above. Matching a leading asymptotic rate alone
is neither the written full condition nor sufficient to control subleading
factors. A:288's "only if C is the exact asymptotic rate" is too strong as
a necessity claim and too weak as a sufficiency claim. TR alone proves no
cutoff-uniform seed.

## 14. Fact-test verdicts

**D6: frozen nonabelian finite groups were assigned the wrong even-state
count. This failure was already covered elsewhere; no new attack is made.**
Use `gap-crux-exercise2-check-astra.md:227–266`, whose explicit witness and
bounds were read. For Q8 and 2T the flat commuting triples `(1,1,1)` and
`(i,1,1)` are inequivalent even after conjugation and central flips.
Centrality of the first holonomy distinguishes them. Their orbit indicators
are orthogonal even flat vectors. The source proves, at each fixed box,

`||T-P_flat||<=eta=(1+(|G|-1)z)^E-1+z`, `z=exp(-beta d_G)`,
`S_ev(t;B)>=((1-eta)/(1+eta))^t>=1/2`

when `beta>=(1/d_G) log(16E(|G|-1)t)`, with `d_Q8=1`, `d_2T=1/2`.
It uses no numerical enumeration. At the frozen limit the even flat space
has dimension at least two. This directly defeats the blanket frozen
PASS and the assumption of only eight low states in the full count.
The source carefully does **not** prove failure at every box at one fixed
finite beta, or locate a phase transition. Those limits remain distinct.

| Test asserted in A | Verdict and exact surviving scope |
|---|---|
| Frozen Q8 and 2T pass static GLUE, have a large enough even gap, and need only `G~log8` | **FAILS.** The prior witness above gives a non-small even trace at every specified box for sufficiently large finite beta. At strictly frozen coupling it retains even vacuum multiplicity. A local bulk gap does not remove these states. No conclusion at beta 2.3–2.6 follows from this fixed-box estimate alone. |
| Z2 passes static GLUE while flux fails | **HOLDS AFTER CORRECTION** to the fixed-box, sufficiently-large-beta statement of section 5(c). This is proved by the existing Z2-c estimates. A volume-uniform phase claim needs further control. |
| U(1) Coulomb fails GLUE/Z0 and passes COUNT with the printed photon scale | **FAILS as an established test from the cited inputs.** The photon/free-Maxwell calculation is GUIDE. Row 786 proves a periodic Villain **Langevin** gap tends to zero and nonsummability of a bounded plaquette score; it explicitly distinguishes the transfer bridge (`gap-tu-retry.md:231–255`). It does not evaluate `S_ev` on every candidate one-box seed, prove its COUNT bound, or give `m_ev~2pi/b`. The same note leaves the Wilson-cosine extension open. These model distinctions cannot be removed by saying "photon". |
| Villain U(1) defeats the stated fixed-shape block coefficient at beta at least `2^14` | **HOLDS as an implication from the cited Theorem V and block theorem.** Theorem U (`gap-blockcrit-opus.md:294–311`) explicitly makes this deduction: a uniform coefficient margin would yield a positive uniform Langevin gap. It refutes that coefficient formulation, not every possible even-sector criterion. The massless Gaussian coefficient example also holds in its stated Gaussian setting. |
| Q8/2T/Z2 pass all gauge-invariant block criteria in their deconfined phases | **FAILS as a proved statement.** No admissible block family or positive uniform margin is supplied. A local gap alone does not prove the specific worst-case criterion. The finite-group topological states further forbid identifying that local statement with the whole even trace. |
| U(1), Z2, Q8 and 2T fail volume-uniform BETA on paths through the listed transitions | **HOLDS AFTER CORRECTION to a conditional test.** If an even level has a uniform positive starting energy and tends to zero at a later coupling along growing boxes, TR rules out one uniform finite C. A supplies neither that finite-volume level statement nor a proof of its transition locations/orders for these models. The numbers 1.01, 0.4407, 1.15 and 2.15 remain GUIDE. No finite-box failure of BETA follows simply from the word "transition". |
| K7's mixed action supplies a soft neutral state, with small flux and failed GLUE/BETA | **FAILS as a proved witness here.** The cited `gap-brainstorm2-max.md:453–478` explicitly recalls the mixed-action phase diagram. It proves neither the critical endpoint nor a small one-box flux weight there. A path in two coupling parameters must also be specified before applying the one-parameter transport inequality. Conditional on an even level closing, the same Gronwall obstruction applies. |
| SU(2) thermal windows, masses, pressure values and relative size thresholds | **HOLDS AFTER CORRECTION** as heuristic orientation only, as most individual entries already say GUIDE. They are not exact fact-test verdicts. The final declarations that all four combinations occur in SU(2)/the listed models are not established by those numbers. SEP proves only the two non-implications in its abstract class. |
| Electric-model `C=1.14` on `[0.36,3]`, A:8.0(8) | **FAILS as a proof.** Sampling finitely many spins and couplings gives no uniform derivative bound on every branch. A calls the run GUIDE but then says "So BETA holds". Retain only the guide observation. The ratio-of-sums argument transfers a true all-spin bound if one is first proved. |

The prior AN1 result is reused, not enlarged: the same-block repeated
schedule forces `mu_ext(r^m)<=k^m` for every m, hence `r<=k` almost
everywhere (`gap-annealed-check-astra.md:64–86`). It proves that **that**
annealed hypothesis is worst-case. It does not repair D4's universal claim.

## 15. The even D-shape — HOLDS in the stated Wilson normalization

Let the coupling variable be s. At a finite torus, differentiating the
positive sum of the eight twisted partition functions gives
`d_s log Z_0(a)=6ab^3(u_ev,a(s)-1)`, with the twisted signs retained.
The top untwisted eigenvalue is simple and isolated. On a fixed spatial
box, the infinite-time pressure is `e(s)=log lambda_0(s)` and
`e'(s)=6b^3(u_inf(s)-1)`. One may either use the simple-eigenvalue derivative
or integrate the finite-time convex pressures and take their limit; the
latter uses their bounded slopes and gives the identity almost everywhere.
At s=0, Haar normalization gives `Z_0(a)=lambda_0=1`. Subtraction and
integration therefore give exactly

`log(1+S_ev(a;b^3;beta))=6ab^3 int_0^beta [u_ev,a(s)-u_inf(s)] ds`.

This is a signed integrated identity. It is not an absolute bound or a
pointwise estimate on the plaquette difference. The probability mixture
is justified here by positive Wilson twisted weights; sector-trace
positivity alone in an arbitrary abstract model would not supply such a
configuration-space mixture. No small value of the integral is proved.

## 16. Hamiltonian virial identity — HOLDS; the extensive-defect conclusion remains unproved

For `H(lambda)=K/lambda+lambda N`, follow differentiable normalized
excited and vacuum eigenvectors, with common operator/form domains.
Put `G=E_n-E_0`, and let Delta denote the difference of their expectations.
Feynman–Hellmann gives `G'=-Delta K/lambda^2+Delta N`, while
`G=Delta K/lambda+lambda Delta N`. Eliminating Delta K gives

`lambda G'=2lambda Delta N-G`, and `(lambda G)'=2lambda Delta N`.

Thus the asserted monotonicity is equivalent to `Delta N>=0` along that
branch. At a degeneracy use the differentiable eigenbranches or the
one-sided eigenvalue derivatives; no arbitrary eigenvector derivative is
allowed. This identity concerns the Hamiltonian family written here, not
an exact identification of the finite-step isotropic Wilson transfer with
that Hamiltonian.

For clarity, the exact best additive constant in the proposed form bound
can be checked without a tangent-line shortcut. Write `mu=lambda^2`,
`psi(mu)=inf spec(K+mu N)`, and take `kappa>1`. Then

`K<=kappa lambda(H-E_0)+C I`

holds exactly when

`C>=C_min=kappa psi(mu)-(kappa-1)psi(kappa mu/(kappa-1))`.

This follows by taking the bottom of
`(kappa-1)K+kappa mu N`. It also shows what must be subtracted to call the
constant a tangent concavity defect. If psi is differentiable and
`K_0=psi(mu)-mu psi'(mu)` is the vacuum kinetic expectation, then with
`mu'=kappa mu/(kappa-1)`,

`C_min-K_0=(kappa-1)[psi(mu)+(mu'-mu)psi'(mu)-psi(mu')]>=0`.

This is the actual tangent defect. Extensivity of this residual in the
specific model is an extra estimate; A:8.0(4) correctly demotes it to
ARGUED. Neither concavity nor the identity bounds it by the level gap.
The asymptotic-freedom sign discussion is GUIDE and supplies no BETA bound.

## Disposition and coverage

Checked line by line by Codex (gpt-6-astra, xhigh). The first failed
inference among G1–G4 is A:131, the interpretation following G4, not its
crossing identity. The original report's final conclusion FAILS as written:
G3 proves quotient mixing; LOC proves only an inclusion; neither establishes
that this finite-box trace is exactly the bulk mass gap. The frozen Q8/2T
PASS is contradicted by existing repository work.

| Author lines | Statement | Verdict |
|---|---|---|
| 110–114 | G1 | HOLDS |
| 116–120 | G2's inequalities | HOLDS; the same-threshold equivalence at 313 fails |
| 122–125 | G3 | HOLDS |
| 127–137 | G4 and its reading | HOLDS AFTER CORRECTION |
| 141–151 | SEP | HOLDS AFTER CORRECTION; two finite-box non-implications |
| 153–157 | UNTW | HOLDS AFTER CORRECTION; partition-data-only scope |
| 198–203 | CS | HOLDS for the inequalities; method exclusion FAILS |
| 230–237 | LOC | HOLDS for local-to-even inclusion; asserted converse and universal ceiling FAILS as deductions |
| 239–243 | FIB | HOLDS AFTER CORRECTION; exhaustive averaged-method dichotomy FAILS |
| 222–224 | MC | HOLDS |
| 251–255 | UP | HOLDS for the bound; necessary factor 1728 FAILS |
| 188–196 | G5, including 110592 | HOLDS as a sufficient implication |
| 270–288 | TR and TR1 | TR HOLDS; TR1 HOLDS AFTER CORRECTION; all-level converse FAILS |
| 205–210 | Even D-shape | HOLDS |
| 291–293, 303 | Virial and monotonicity identities | HOLDS; claimed extensivity remains unproved |
| 135–137, 169–184, 194, 249, 282–288, 307 | Fact tests | Individual verdicts in section 14; frozen Q8/2T PASS FAILS |

No source note, queue, registry, ledger or status file was edited. Only this
report was written. No numerical run, machine enumeration, Lean proof,
external posting, commit or push was performed. The inherited strong-coupling
and shape theorems remain named inputs; their entire proofs were not
rechecked. Balaban's papers and the complete-account volumes were not needed
for these class-level checks and were not newly read. Source scope claims
here use the specified outline passages, not an assertion of a full-account
absence theorem.

RESULT: Row 896 complete — gap-glue-max.md FAILS as written, while its elementary spectral, mixing, gap/count (110592), D-shape and virial identities survive; SEP, UNTW, G4, FIB and TR1 need the stated corrections, and the frozen Q8/2T PASS contradicts prior work. No order-one or first-passage glue seed is proved; GLUE-FP, Z0, COUNT at the required size, and volume-uniform BETA remain open.
