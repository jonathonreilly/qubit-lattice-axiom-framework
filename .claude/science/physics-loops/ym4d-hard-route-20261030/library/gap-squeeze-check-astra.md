# Repo search

The target-specific prior note is absent at `8647242a563efbb08c117562a9dc0cdc591161ad`.
The lead's `prior/repo-search-2026-11-08.md` reports a one-step positive
Wilson-loop correlation in the soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md`
(lines 106–149). That statement is not a squeeze comparison or a seed bound.
The primary source was read at `pr/10114` commit
`f76f6c649cff7dffbab664d8976e680e8f287fe9`, lines 106–170. Its convolution
eigenvalue is useful prior algebra, but its positive correlation supplies no
upper thermal bound. The digest reports the same blob on `pr/10133`.
The registry has no squeeze owner; FINISH row 966 explicitly owns this check of row 965. This check does
not attack the separately owned seed, LSI, or block-dynamics problems.

Research check by OpenAI Codex, configured model/effort of this session;
task dispatch names gpt-6-astra/xhigh. Not an audit; grants no status.
Source: `library/gap-squeeze-opus.md` at the pinned commit above.
Credit: Claude Opus 5.5 for that note; Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text, for the cited account.

## Checkpoint

Completed the six planned stages: prior-source and indexed reads; geometry
and boundary laws; exact inequalities; hand endpoints; GUIDE artifact
inspection; final statement verdicts. Source remains pinned at `8647242a5`.
No seed or LSI proof was attempted. No numeric job was run. Open obligations
are the reverse comparison, periodic block control, entropy comparison,
full-window endpoint bounds and large-beta spectral convergence. The next
decision is whether to repair the source's conclusions before using them
to close the squeeze route; this check recommends that repair.

The source stays unchanged. No numerical calculation can discharge a proof.

## Sources and scope

The outline and CA-I were each downloaded once at `31a47c543775`, into
`/tmp/sa-gap-squeeze-check-astra.3aYSms/`. The index README, matching chunk
rows and neighbours, and matching `obligations.md` rows were read first.
Outline 2195–2243 supplies the convolution coefficients and their positive
series. Outline 2313–2382 supplies the transfer trace and Schatten bound.
These are credited inputs, not new results of row 965. Outline 588–600 and
CA-I 2698–2714 expressly leave a physical gap additional.
The CA index's chart-shrinking and cube-holonomy hits were checked at
CA-I 80335–80363 and 102695–102725: different objects, not squeeze estimates.
The CA-II minimizer-squeeze title is only an index hit here; its source was
not downloaded or used. No relevant 4.12–4.19 statement is invoked.

The current-main workflow was read at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`.
Its check procedure is used for mathematical scrutiny only. The user's
specified output path, verdict vocabulary and no-status scope govern this file.
The prior digest is a locator, not proof or an exhaustive present-day search.

The source's Step 1 inputs were compared with `gap-lsivac-max.md` Step 1,
`gap-fc-max.md:487–532`, `gap-vargeom-opus.md` sections 2.1–3.7 and 4.5,
`gap-glue-max.md:220–243`, and the slab consumer in
`gap-shape-link-check-astra.md:168–230`. Its seed requires the same bare
Wilson measure, every required cutoff/coupling, a common strict margin
below 3/10, integer `a>=3`, `b>=24a`, and bounded physical side `b a_K`.
The even-`a>=30` condition belongs to the stronger HC/LSI route.
No squeezed estimate here supplies those uniform quantifiers.
The old ceilings are reused only with their recorded method restrictions
(`gap-status-1113.md:68,110–112`); this check does not repeat those prior
proofs or turn them into ceilings on arbitrary boundary comparisons.
Literature-domain warnings were read in `prior/gap-lit-hcvac.md:7–9`,
`prior/gap-lit-geom.md:57`, and `prior/gap-math-lit.md:41–42`.

## 1. Geometry and boundary laws

Line numbers below refer to `gap-squeeze-opus.md` at the pinned commit.

| Statement | Verdict | Check or required correction |
|---|---|---|
| 114–132, open boxes and schedule | HOLDS AFTER CORRECTION | Require every direction to become open on the first removal, and specify even `b`. The inequality `s_i(1) >= b-1` alone also permits `s_i(1)=b`. Extend the terminal schedule by `Q_(n+1)=Q_n` when defining its two-slice marginal. |
| 134–144, COUNT | HOLDS AFTER CORRECTION | For the stated first removal, `s_i(t)>=b+1-2t`, hence `n>=ceil((b-1)/2)` for a cube and `n>=ceil(b/2)` for a plaquette. For even `b` these are `b/2`. A symmetric closure needs `2n>=b`, stronger than the printed `b-1`. The bound inside an even period is valid. These are bounds for this removal speed, not arbitrary squeezing. |
| 150–160, free kernel | HOLDS | Haar product restriction is an isometry. Independent endpoint gauge changes are absorbed by the temporal gauge integral. Composition assigns each internal spatial action once. |
| 161–171, D and C | HOLDS AFTER CORRECTION | A fixed exterior defines an explicit local conditional density. Include **all** plaquettes touching retained links, including temporal end faces, to claim the DLR identity in the infinite or periodic parent. With frozen exterior links one cannot also impose the unrestricted vertex gauge projection of line 149: only transformations preserving that exterior remain symmetries. |
| 172–185, V projections and diamond | HOLDS | Use the physical invariant Hilbert space. Gauge covariance of the retained sigma-algebra and invariance of `nu` imply that conditional expectation preserves invariant functions. `A_n` fixes constants, and its adjoint closure is a positive Hilbert–Schmidt square. |
| 186–202, endpoint laws and computability | FAILS | The raw two-slice law of row 941 is the **unprojected**, simultaneously gauge-invariant law `J_0`. The trace chain is gauge-projected. Their raw two-slice laws differ; they agree on separately invariant tests. Also, a fixed exterior `tau` is explicit data, not an unknown vacuum. Finite-dimensional integration does not compute a Perron eigenvalue or an LSI constant. Step 5 computes the free plaquette bound and a **static** cube partition function; it does not compute D endpoints, the cube thermal sum, or either endpoint LSI. |
| 204–211, centre blindness | HOLDS AFTER CORRECTION | Applies to retained **gauge-invariant functions**, not every function of retained links. Move each centre-flip plane outside the open box by a gauge transformation. This proves the stated invariant-sector consequence when all three directions have been cut. |

The raw-law distinction follows directly from row 941 Step 1 (A1):
`T_0(x,w)=M(x) exp(beta<x,w>) M(w)` and `T=T_0 Pi_G`.
For invariant tests the two operators coincide. The physical trace identities
below use `T`; the bridge LSI of row 947 uses `J_0`. A marginal LSI gives no
reverse implication to the full `J_0` without an additional estimate.

## 2. Exact identities and the strength of their consequences

| Statement | Verdict | Check or required correction |
|---|---|---|
| 227–238, BND | HOLDS AFTER CORRECTION | Schatten Holder on the mean-zero invariant space proves the V inequality. The unitary from `L^2(nu)` to Haar space is `f -> Omega f`; division is its inverse. For F/D, the lens estimate holds for specified positive endpoint operators and an adjoint pair `Y,Y*`. It does not identify an arbitrary frozen-exterior closure with those operators or prove every mixed complex is below the target rectangular slab. |
| 240–259, SHELL | HOLDS | Nested conditional expectations give mutually orthogonal `D_k` summing to `I-Pi_c`. For positive trace-class `P^t`, `s_k=\|\|P^(t/2)D_k\|\|_HS^2`; summing gives `S`. This is a direct sum-of-squares verification. The cost `S_j(t)-S_(j+1)(t)` is exact at **fixed t**, in the physical invariant space. |
| 260–261, volume share | HOLDS AFTER CORRECTION | A model heuristic only. The recorded free scalar is not a gauge-link gas; its fraction `8/b^3` cannot verify the link fraction `12/(3b^3)`. |
| 262–265, FLUX | HOLDS AFTER CORRECTION | For an invariant centre-odd eigenfunction `v`, `Pi_1 v` is invariant and centre-even, hence zero. Thus `D_0 v=v` and the lower bound holds. Replace “every function” by “every invariant function.” The first shell may also contain centre-even winding states. |
| 267–277, LEAK | HOLDS AFTER CORRECTION | The operator telescoping identity holds. Triangle inequality on the full space gives the printed square roots with `1+S`; on the mean-zero space it gives the stronger `sqrt(S)<=sqrt(S_dia)+sum l_j`. Neither proves equality of this time-dependent cost with SHELL's fixed-time cost. “No better” is not a proved comparison. |
| 282–296, PR | HOLDS | Differentiate `log Tr T^a-a log lambda_0`. At fixed finite B the simple Perron level is analytic; equivalently Hellmann–Feynman identifies its derivative with one vacuum layer. At beta=0 both logarithms vanish. There are `6ab^3` plaquettes in the stated slab. This checks the identity without needing the author's convex-derivative interchange. |
| 297–304, window | HOLDS | For even `a>=4`, condition on the two end slices. The finite periodic law puts them on the diagonal; the infinite law uses the vacuum endpoint joint law. Both have the same interior Gibbs specification. |
| 305–314, oscillation bound | HOLDS AFTER CORRECTION | Taking a supremum and integrating gives a **sufficient** bound. `6*30*720^3*(23/10)=154529280000`; at `26/10` it is `174685593600`. The printed thresholds about `1.67e-12` and `1.48e-12` are consistent with `x_*=log(22/17)`. For `b=120` the coefficient is `715392000`, giving about `5.48e-11`. The local Gibbs specification has no exact finite-speed backward cone: within-slice couplings transmit dependence arbitrarily far. A cone/per-step influence estimate is an additional missing bound. |
| 315–323, HALF | HOLDS | Conditional averaging contracts oscillation. Mean zero gives `\|\|P^h g\|\|_2<=osc(P^h g)`, and reversibility gives `\|\|P^h g\|\|_2^2=<g,P^(2h)g>`. The last eigenfunction lower bound is valid, including zero overlap. |
| 324–335, spectral shift and doubled time | HOLDS AFTER CORRECTION | The displayed diagonal spectral identity holds. Its leading diagonal coefficient need not be nonzero when the **off-diagonal** matrix element in HALF is nonzero. The latter also vanishes for a centre-odd first state and a local plaquette. A doubled asymptotic exponent is conditional on a specified visible lowest band, nonzero relevant coefficients and controlled prefactors. The one-plaquette GUIDE is evidence only for that model. |
| 336–338, averaged form | HOLDS AFTER CORRECTION | The signed, coupling-integrated sum is exactly `X`. Absolute values, a supremum in coupling, or bounds on individual summands are stronger sufficient conditions, not equivalent statements. |

For the spectral distinction, take a two-state reversible positive transfer
matrix with eigenvectors `(1,1)/sqrt(2)`, `(1,-1)/sqrt(2)` and ratios `1,r`,
`0<r<1`. Multiplication by `s=diag(1,-1)` has off-diagonal matrix element one,
but both diagonal matrix elements vanish. Its thermal shift is zero while
its vacuum covariance is `r^a`. Thus the claimed implication between those
two coefficients is not spectral algebra.

The static lens inequality itself needs only
`0<=Y* T_L^a Y<=lambda_0(L)^a ||Y||^2 I`, followed by tracing against
`T_s^k`. This verifies the needed part of row 960 (L3) directly; no assertion
that every varying geometry has a rectangular comparator is used.

## 3. Block conditions and LSI

| Statement | Verdict | Check or required correction |
|---|---|---|
| 341–350, QF | HOLDS AFTER CORRECTION | Add `eps<1`. On the complement of the common range, `\|\|E_1+E_2\|\|<=1+eps`, as the displayed Cauchy–Schwarz calculation proves. This is a variance bound, not an entropy bound. |
| 351–356, finite-block supremum | HOLDS AFTER CORRECTION | Disintegrating over the exterior gives the essential supremum of the fibre norm of `E_1E_2-E_cap`. On a positive finite Wilson density, the common conditional range is the exterior sigma-algebra when the two blocks cover the interior. Continuous conditional kernels then permit replacing essential supremum by supremum. Without that finite positive-density setting, retain “essential.” |
| 357–364, top-level `r_1^w` | FAILS | MC is exact for past/future sigma-algebras of an **infinite stationary Markov chain**, on the specified physical test space. It is not an identity for overlapping spatial blocks of a periodic torus. “Up to the wrap” supplies neither a bound nor its constant. |
| 368–378, literature equivalence | FAILS as a supplied implication | No theorem with its hypotheses is applied here. The named results concern distinct spin spaces, boundary-uniform families and Glauber forms. An LSI for the single bridge law `J_0`, restricted to simultaneous invariance, is not thereby equivalent to complete analyticity. The local-parent LSI is a sufficient stronger input; marginalization is one way. The primary papers were not read in this check, so their general theorems are not re-certified. The repository's prior literature notes explicitly retain these domain/application gaps. |
| 380–401, comparison table | HOLDS AFTER CORRECTION | The identities deliver no new seed estimate. Keep this finding local to the displayed inequalities. Delete universal “needs twice the time,” “computable implies supremum,” and “top level equals the gap” conclusions. No entropy quasi-factorization theorem linking a squeezed endpoint to `(LSI-J-seed)` has been supplied. |

A hand counterexample to the periodic identification uses the two-state
kernel `K(s,t)=(1+r st)/2`, `0<r<1`. On a ring of length `L`, spins separated
by `w` have maximal correlation

`(r^w+r^(L-w))/(1+r^L)`.

Multiply the two kernels for the two arcs and sum `s,t=+/-1` to obtain this
formula. On the infinite chain the value is `r^w`. At `L=2w` the ring value
is `2r^w/(1+r^(2w))`, strictly larger. Thus MC needs a distinct periodic
comparison, even before its application to the actual gauge blocks.

The single-link ceiling in 550–561 **HOLDS AFTER CORRECTION** for the
specified certificate: a boundary-uniform full-function endpoint LSI has
constant at most 3, since an allowed cancelling-staple exterior gives Haar
measure on the unit `S^3`. For a coordinate `q_0`,
`Var(q_0)=1/4` and `E|grad q_0|^2=3/4`. Linearizing LSI bounds its constant
by this Rayleigh quotient, 3. No sharp sphere LSI theorem is needed.
This caps that certificate, not the true invariant LSI of `J_0`.
An explicit cancelling exterior sets three of the six staples to `I` and
three to `-I`: choose a distinct non-central-link edge on each incident
plaquette for the required sign, with all remaining edges equal to `I`.
These edges are distinct on the seed boxes. This realizes the asserted
zero staple sum without a numerical search.

At beta 2.3, `2 beta K_30` is about 4.30 on the slab and 3.73 at ratio 4.
Those comparisons with 3 hold. The printed minimum sizes do not:
`a=44` already gives `4.6(16.00+3 log 44)/42<3`, while `a=42` fails;
at ratio 4, `a=38` already gives `4.6(12.51+3 log 38)/36<3`, while 36
fails. Thus the smallest even choices using these constants are 44 and 38,
not 45 and 40. In particular 45 violates the even-`a` contract.
These numbers concern beta 2.3 only, not the whole window.

## 4. Fact tests

| Statement | Verdict | Check or required correction |
|---|---|---|
| 409–414, unbounded Gaussian oscillation | HOLDS AFTER CORRECTION | If the observable is a nonzero quadratic form on the **range** of the conditional-mean map, its boundary oscillation is infinite. `q!=0` and `L!=0` separately do not imply this. For a visible field-strength component of the free field the coupling supplies that range condition. It applies also to massive Gaussians: it is a supremum obstruction, not a diagnostic of masslessness. |
| 415–421, compact U(1) | HOLDS AFTER CORRECTION | Conditional on a uniform `Cov(s_0,s_a)>=c a^-8` on `b=ra`, HALF gives `6r^3 beta sqrt(c)` as a lower bound on the **upper-bound expression** in CONE. With the recalled free-field coefficient it is `82944/pi^2`, about 8400 at ratio 24. It is not a proved compact-U(1) bound, and no blow-up in `a` follows: the expression stays of constant order. |
| 422–429, scalar shell and block heuristics | HOLDS AFTER CORRECTION | SHELL is an identity. Bounded unit thermal traces, scale-invariant block angles and a particular recursion product are additional model hypotheses, not consequences of it. The finite scalar GUIDE tests some shell values; it does not test QF angles or establish the infinite-volume claims. |
| 431–438, frozen-group flux lower bound | HOLDS AFTER CORRECTION | The conditional lower bound `s_0>=7-o(1)` survives. The claim that the centre-even sector has a large gap is false; see the explicit flat-state argument below. |
| 439–448, frozen transitions/block test | HOLDS AFTER CORRECTION | The listed transition couplings and coexistence claims remain recalled GUIDE inputs. PR requires the integrated shift to account for the frozen degeneracy; it does not locate it solely at a transition. The periodic block claim again needs the missing wrap estimate. |
| 450–469, SMALL-BOX | HOLDS AFTER CORRECTION | A fixed finite open plaquette has a positive gap at every fixed finite beta, by positivity and compactness. That is not a uniform large-beta lower bound. Open growing boxes still have modes of order `1/b`; simple connectedness removes flat holonomies, not all low-momentum modes. The stated harmonic limit is a formal scaling calculation, not a spectral-convergence proof. |
| 471–481, K7 | HOLDS AFTER CORRECTION | If a local plaquette has order-one overlap with a near-degenerate state, `S_n(t)>=r_1^t\|\|Pi_n phi_1\|\|^2` is correct, so the faithful endpoint can itself be difficult. Smooth finite-volume weights ensure a simple top level, not a uniform order-one gap over couplings. Phase-jump and overlap estimates remain assumptions. A mixed-action PR must differentiate both couplings along a specified path; the single-beta formula is not unchanged. |
| 483–487, all tests pass / no endpoint carries difficulty | FAILS | K7 in the preceding paragraph puts order-one weight in the faithful endpoint. Several other tests are conditional heuristics, not checked model estimates. |

Here is a hand counterexample to the frozen even-gap assertion. At
`beta=infinity` for a finite subgroup of SU(2), the Wilson weight is one
on identity plaquettes and zero elsewhere. The transfer operator on
gauge-invariant functions, after division by its top eigenvalue, becomes
the identity on flat spatial gauge orbits. For Q8, take flat torus holonomy triples `(1,1,1)` and `(i,1,1)`.
Both exist as commuting triples. Their centre-flip orbits are distinct:
`((tr W_1)/2)^2` equals one on the first and zero on the second.
The sum of orbit indicators in each centre orbit is invariant and
centre-even. Hence the limiting transfer operator has **at least two**
independent even eigenvectors of eigenvalue one. The same construction
works in 2T, which contains Q8. Finite-dimensional matrix convergence
implies two even eigenvalues whose ratio tends to one as beta grows.
There is no large even-sector gap. The eight central triples still form
a regular centre-flip orbit, supplying the seven nontrivial centre
characters used in the surviving flux lower bound.

This does not weaken FLUX. It shows that the first cut can discard further
topological information besides its seven named flux contributions.

## 5. Endpoint formulas and hand arithmetic

**498–512, Bessel series and static plaquette: HOLDS AFTER CORRECTION.**
The positive series, `Z_pl=c_0`, mean `I_2/I_1`, and
`Var(x)=1-3(I_2/I_1)/beta-(I_2/I_1)^2` hold. The displayed decimals agree
at their stated precision and are rounded values.
Rounded series sums are not directed bounds. The tail claim needs a
summable majorant, not only “every term ... below 1e-7.” Here is one.

Write `z=beta/2`, `u_(nu,0)=z^nu/nu!` and
`u_(nu,k+1)=u_(nu,k) z^2/((k+1)(k+nu+1))`. All are rational at the two
couplings. If `B_(nu,K)=sum_(k=0)^K u_(nu,k)`, then

`B_(nu,K) < I_nu < B_(nu,K) + u_(nu,K+1)/(1-z^2/((K+2)(K+nu+2)))`.

This follows by bounding all subsequent successive ratios by the first
one. With `K=8`, rational addition and division give the following loose
enclosures; they deliberately leave room beyond rounding:

| beta | `A_(1/2)` | `A_1` | upper `A_(3/2)` | upper `A_2` |
|---|---|---|---|---|
| 23/10 | (0.479278, 0.479280) | (0.166470, 0.166473) | 0.045008 | 0.009929 |
| 26/10 | (0.520340, 0.520344) | (0.199472, 0.199476) | 0.060020 | 0.014804 |

For example, the first two terms for `I_1(23/10)` are exactly
`23/20` and `12167/16000`; the recurrence produces each remaining term
without a Bessel evaluator. The displayed enclosures are finite rational
inequalities with the explicit remainder above, not a numerical certificate.

Termwise comparison also gives `I_(nu+1)/I_nu <= z/(nu+1)` (the outline's
GL4). Starting at `A_2`, it bounds `A_(5/2)<0.003208` throughout these
two endpoints. The weighted integer-spin sum is below 1.68: its first
three terms are at most `1+3(0.199476)+5(0.014804)`, and the same ratio
bound makes the remaining sum below 0.0044. Therefore the tail in `N`
after `j=1` is below `7e-6` at 2.3 and `22e-6` at 2.6. The subsequent
`j>=5/2` tail is geometrically summable; using the coarser bound 7 for
the inner sum already bounds it by `8e-10`. This supplies the missing
hand tail argument.

**513–533, EP1: HOLDS AFTER CORRECTION.** Gauge fixing a spanning tree
leaves one holonomy; invariant functions are its class functions. Each
of the four link convolutions contributes `c_j/d_j`, so `T=MDM` and
`D chi_j=(c_j/d_j)^4 chi_j`. Clebsch–Gordan gives
`Tr T=c_0^5 N`. The trial vector `M1` has norm squared `c_0` and
Rayleigh quotient `c_0^5 R`. Thus `S(1)<=N/R-1` holds. For `k>=1`,
`sum r_i^k <= (sum r_i)^k` gives the power bound; `r_1<=S(1)` is immediate.

The narrow printed bound `0.03017` is rounded down: even the author's
GUIDE evaluation of this Rayleigh bound is `0.030171...`. That does not
refute `S(1)<=0.03017` by another argument; it invalidates this claimed
certification. From the rational enclosures just given, direct products yield

| beta | upper N | lower R | safe conclusion |
|---|---|---|---|
| 2.3 | 1.080317 | 1.048673 | `S(1)<0.03019` |
| 2.6 | 1.119853 | 1.079960 | `S(1)<0.03694` |

The last comparisons need only multiplication:
`0.03019*1.048673=0.03165943787 > 1.080317-1.048673`, and
`0.03694*1.079960=0.0398937224 > 1.119853-1.079960`.
The exponential series with its geometric remainder gives
`e^3.5<33.12` and `e^3.29<27`; multiplying by the two bounds gives
numbers below one. Hence the advertised **endpoint** gap lower bounds
3.50 and 3.29 survive. No machine computation is used to discharge these estimates.
The displayed values at just two couplings do not prove a uniform bound
over every beta in [2.3,2.6]. No monotonicity theorem for `S` is supplied.

**535–548, static cube: HOLDS.** Expanding each face weight and
integrating every edge pairs its two incident representations by Schur
orthogonality. All face representations agree; the residual factor is
`d_j^(F-E+V)=d_j^2`. Thus `Z_cube=sum d_j^2(c_j/d_j)^6`.
Differentiating gives the stated mean. Inserting `chi_1` on one face
gives exactly the three Clebsch–Gordan coefficients printed in line 542,
including the absent `c_j` contribution at `j=0`. These formulas and
the positive series yield the quoted rounded values 1.04868/1.07996,
0.49340/0.53884 and 0.53172/0.64606. The expressions 0.177/0.213 are
the first electric-loop contribution, **not a bound** on the cube seed.
The full cube thermal sum remains uncomputed, as the author states.

**453–463, harmonic endpoint argument: HOLDS AFTER CORRECTION.** In
line 456 replace `c_j/c_0` by `c_j/(d_j c_0)=A_j`; the former tends to
`d_j`, not one. After rescaling `q=sqrt(beta) theta`, the formal transfer
kernel is proportional to

`exp[-(3/8)(|q|^2+|q'|^2)+(1/4) q.q']`.

For this Gaussian kernel the one-quantum ratio has
`cosh(omega_tilde)=2(3/8)/(1/4)=3`. Radial states first excite two quanta,
giving `2 arccosh 3`. This verifies the **limiting oscillator calculation**,
not convergence of the SU(2) spectrum to it. That would require uniform
localization, a kernel limit with a controlled tail, and spectral convergence.

**563–568: HOLDS AFTER CORRECTION.** The power arithmetic is safe:
`0.03694^9<0.04^9=2.62144e-13<1.67e-12`.
But this thermal sum is not the boundary oscillation required by CONE.
“Gap above 3.3 ... as beta grows” is unsupported by the hand proof and
contradicted at GUIDE level by the author's beta=4 value 3.2412.
The fixed-finite-beta positive-gap fact survives; a uniform large-beta
bound and a full-window quantitative bound were not proved here.

## 6. GUIDE artifacts and every reported test

All three scripts and all three committed logs in `library/guide/lane965/`
were read in full. No numeric job was rerun. The checks below are of their
model, formulas, rounding and recorded arithmetic; decimal eigensolver and
determinant outputs have no independent numerical reproduction here.

For the scalar formulas a direct derivation is as follows. Whiten
the first-chaos coefficient space by `C^(1/2)`. The retained subspace has
Gram matrix `C_QQ`, and the compression of `A^t` has generalized matrix
`(CA^t)_QQ` relative to that Gram matrix. Diagonalizing this compression
and summing the geometric occupation series in each bosonic mode gives
`det(C_QQ)/det(C_QQ-(CA^t)_QQ)`. Subtract the vacuum one. Products of
orthogonal projections and `A` similarly give the singular-value formula
`det(I-a_n* a_n)^-1-1` for the diamond. These derivations validate the
objects computed by the scripts; they supply no interacting gauge estimate.

| Test / source lines | Verdict | What was checked |
|---|---|---|
| `endpoint.py`, 491–496, 527–544 | HOLDS AFTER CORRECTION | The code constructs the stated truncated character matrices with midpoint quadrature. Its N/R and cube formulas match the hand formulas. The docstring still describes the older, weaker `R=1` bound; the executed function uses R correctly. Entries at beta 2.45, 4, 8, 16, 32 are GUIDE approximations. Neither basis truncation nor quadrature has a certified error bound. |
| M1/M2 definitions, 572–580 | HOLDS AFTER CORRECTION | The scalar determinant and covariance formulas hold for `m>0`; G4 explicitly removes the zero mode when `m=0`. M2 is a finite matrix approximation, not “exact” for the infinite transfer operator. |
| G0, 583–584 and 605–610 | HOLDS AFTER CORRECTION | The full-box diagonalization and the retained Gram determinant describe the same trace. Positive shell values and the four BND comparisons are recorded. The claimed maximum relative discrepancy `2e-11` is wrong: the printed row `b=16,r=2,ma=6` has `abs(delta)/S = 1.5e-11/0.037363`, about `4.0e-10`. The two eigenvalue-logdet rechecks agree with those two rows, but do not prove that every warning in the main run was spurious. |
| G1, 585–588 and 611–617 | HOLDS AFTER CORRECTION | The 18 printed rows satisfy both declared thresholds: retained fraction below ten times `8/b^3` for `ma>=4`, and discarded fraction above 0.5. The minimum discarded share is 0.9785. Ratios and examples in the prose match the log to rounding. The schedule is `b,b-2,...,2`, which violates COUNT's first-step hypothesis. These are results for that explicitly different schedule. |
| G2, 589–590 and 618–622 | HOLDS AFTER CORRECTION | QR spans `C^(1/2)R^Q`; the code iterates `pi_j A` in the stated order. The four ratios 0.0296, 0.0235, 0.0084, 0.0073 pass the declared 0.5 threshold and each diamond value is below its recorded endpoint share. They do not prove that inequality for all P or all schedules. Here `n=b/2-1`, consistently with the relaxed first cut, not COUNT. |
| G3, 591–593 and 623–627 | HOLDS AFTER CORRECTION | The code computes `X=log(1+sum r_i^a)` and `L^2=sum r_i^a \|<psi_i,x psi_0>\|^2`. Consecutive reported X ratios are approximately `exp(-2E_1)`, and L ratios `exp(-E_1)`, as the fitted rates state. The declared criterion passes in the truncated model. “Exact here” must mean its spectral formula, not certified infinite-dimensional eigenvalues or a theorem on the full SU(2) seed. |
| G4, 594–597 and 628–631 | HOLDS | Wick's rule gives `Cov(phi_x^2(0),phi_x^2(a))=2(CA^a)_xx^2`, hence the computed V. Its logged values increase from 9.1341 to 28.510 between the declared sides 8 and 16; they pass the factor-two criterion. Sides 24 and 32 are additional runs outside that initial grid, not a new predeclared test. X is 13.493 down to 6.6131. This is a scalar with its zero mode removed, not a photon calculation. |
| G4', 632–636 | HOLDS AFTER CORRECTION | The six V/X divisions give the stated 0.654, 1.314, 2.271, 4.695, 7.296, 9.930. Even `phi^2` couples to two quanta, explaining the absence of an exponential square-root penalty relative to the one-particle trace. No separate pass/fail criterion for G4' was recorded; it is a descriptive GUIDE comparison. |
| Runtime/criteria chronology, 491–496, 598–603 | HOLDS AFTER CORRECTION | The main log records 7.7 seconds and 1.13 GB peak RSS. The committed scripts do not print lock receipts, memory-free shares, start timestamps or pre-run criterion timestamps. Those operational claims cannot be verified from these artifacts. `recheck_shells.py` lacks the stated RSS guard; the other scripts check RSS only between allocations. No conclusion here depends on these operational claims. |

The schedule correction changes a unit-reaching diamond from at least
`b` time steps under COUNT to `b-2` under the GUIDE schedule. Both remain
far longer than `a` at `b=24a`; the finite-step mismatch still matters when
claiming that a run tested a particular definition.

## 7. Final dispositions and the consumer

The source's final table (685–714) has the following dispositions, collecting
the line-by-line findings above. “After correction” retains only the exact
scope and premises stated in this check; it grants no scientific status.

| Final-table statement | Verdict |
|---|---|
| COUNT | HOLDS AFTER CORRECTION: even side, first cut, specified speed |
| F kernel / conditioned DLR | HOLDS AFTER CORRECTION: exterior and end plaquettes specified |
| Centre blindness | HOLDS AFTER CORRECTION: invariant tests |
| BND | HOLDS AFTER CORRECTION: correct unitary and actual lens operators |
| SHELL | HOLDS |
| FLUX | HOLDS AFTER CORRECTION: invariant-sector formulation |
| Volume-share reading | HOLDS AFTER CORRECTION: model heuristic only |
| LEAK | HOLDS AFTER CORRECTION: exact identity, no universal SHELL comparison |
| PR, window, oscillation estimate | HOLDS AFTER CORRECTION: bound is sufficient; no proved cone recurrence |
| HALF and diagonal spectral identity | HOLDS |
| Doubled time for the full SU(2) seed | FAILS as an established consequence; overlap/coefficient input missing |
| Signed integrated averaged cone | HOLDS |
| QF | HOLDS AFTER CORRECTION: eps below one, variance only |
| Finite-block essential supremum | HOLDS |
| Top-level periodic `r_1^w` | FAILS |
| Literature-to-J equivalence | FAILS as a supplied implication; exact application not verified |
| Gaussian infinite oscillation | HOLDS AFTER CORRECTION: observable visible in conditional mean |
| Compact-U(1)/massless-block conclusions | HOLDS AFTER CORRECTION: conditional model readings |
| Frozen first-cut lower bound | HOLDS AFTER CORRECTION; even-gap assertion FAILS |
| Open endpoint gapped at each finite beta | HOLDS; claimed quantitative full-window/large-beta proof FAILS |
| K7 | HOLDS AFTER CORRECTION: conditional overlap test, faithful endpoint can be difficult |
| Bessel series and static moments | HOLDS AFTER CORRECTION: rounded values versus directed bounds |
| EP1 formula and broad endpoint bounds | HOLDS AFTER CORRECTION: use 0.03019, 0.03694; no full-window inference |
| Cube static formula | HOLDS; cube thermal bound remains open |
| One-link certificate ceiling 3 | HOLDS AFTER CORRECTION: method scope and even-size arithmetic |
| G0–G4 | HOLDS AFTER CORRECTION on the stated finite GUIDE models; G0 relative-error claim corrected |
| Every averaged squeeze is unchanged / every computable endpoint harder | FAILS |
| Seed and `(LSI-J-seed)` remain open | HOLDS |

There are eight substantive defects, grouped by what they break:

1. Boundary and raw-law identifications do not specify one common object
   across the trace chain, fixed exterior and bridge LSI.
2. SHELL's exact fixed-time accounting is promoted to a universal comparison
   of time-dependent squeezes and other averaged methods.
3. The exact infinite-chain block norm is imported into a periodic spatial
   recursion without its wrap estimate; variance and entropy are conflated.
4. A conditional square-root lower bound is promoted to a full-seed rate
   obstruction, and the coupling supremum is called equivalent to its integral.
5. The frozen even-gap assertion is false by the flat-state construction.
6. Explicit finite integrals, static cube values and two endpoint couplings
   are promoted to uncomputed thermal/LSI and uniform-coupling conclusions.
7. The GUIDE schedule and relative-error claim differ from their stated
   hypotheses and arithmetic; the remaining GUIDE claims require their
   explicit finite-model and unreproduced-numerics limits.
8. The final recommendation excludes squeeze work more broadly than any
   checked estimate. In particular, a computable endpoint does not logically
   force a supremum over exterior data, and no such necessity theorem appears.

For lines 675–683 and the final RESULT, retain: **none of the displayed
estimates supplies a new seed bound**. Do not retain the request to stop all
squeeze lanes, the claimed equivalence of the pointwise-in-beta target to
the seed, or the assertion that EP1 settles every open-box obstruction.
The source itself leaves other averaged block estimates available.

The check used a sum-of-squares trace decomposition, Hellmann–Feynman
pressure differentiation, a two-state periodic counterexample, a finite-group
flat-state counterexample, and rational positive-series bounds. These are
mathematical checks of the relevant steps, not a second run of the author's
numerical method. Literature claims whose primary sources were not read remain
unverified; so do the operational timing/lock claims and a numerical rerun of
the matrix outputs. No Balaban result is imported, no outside message was
sent, and no source, registry, FINISH row, ledger or status was edited.

RESULT: HOLDS AFTER CORRECTION for COUNT on its stated schedule, BND, SHELL/FLUX, LEAK, PR/window, HALF, QF and the broad free-plaquette endpoint bounds; FAILS for the frozen centre-even-gap claim, the periodic-block identification and the claim that squeezing must leave every averaged crux unchanged or make every computable-endpoint route harder. The GUIDE arithmetic is restricted to its recorded models and corrected schedule/error claim, with no numerical rerun. No displayed estimate closes or weakens the seed or (LSI-J-seed); both remain OPEN, and this research check grants no status.
