## Repo search

The target-specific prior digest is absent at `8acc094fd6e12393c12f360417070c5ab0d6ef20`.
The lead's `prior/repo-search-2026-11-08.md` concerns earlier UV and history targets;
it is not a search for the November 15 pinned-cell statements. Its snapshot hits
must not be counted as independent proofs. Targeted source checks are recorded below.

The target's own search (514–525) found soft-kernel stiffness and Balaban
background-field vocabulary, not the pinned-cell response. I fetched main
and PR heads and checked these named hits:

| Source checked | Closeness to this target |
|---|---|
| PR #10114, `f76f6c649`, `FINITE_COUPLING_KERNEL_ASTRA.md:1–45,310–330` | Stiffness is the parameter of a normalized one-group kernel. It is not the boundary free-energy Hessian. |
| Same ref, `UNIFORM_ONE_LOOP_COUPLING_ASTRA.md:175–205` | A fixed soft-kernel stiffness ratio and Gaussian normalization; different object. |
| Same ref, `BARE_DETERMINANT_COUPLING_ASTRA.md:277–300`; `RTARGET.md:1126–1144` | Background jets and a Balaban reading assignment, not an all-pin bound. |
| PR #10133, `89faef229`, `BFT4W55.md:283–306`; `MATCHA_LOG.md:31–47` | CEN1 is a contour-centering cancellation; “pinned-cell jets” concern ancestral soft-kernel laws. Neither is CEN or B'. |
| Main `8b11ae2bb9`, PR #10134 `1e70c7211`, PR #10141 `a2f6a430e` | Targeted searches found no supplier in the inspected YM4D paths. Broad #10134 matches were unrelated process/history and other-model notes, not evidence about this target. |

The PR paths above are under
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
Queries used `pinned.cell`, `Lemma CEN`, `Proposition SEAG`,
`pin.uniform.curl`, `Schr.dinger.functional`, plus the named hits' stiffness
and background-field terms. These are bounded searches, not an absence
theorem. The earlier November 8 digest was read, including its cautions about
identical snapshots and different measures. No exact target owner was found
by those labels in `open-registry.md` or `open-core.md`. This task checks row
1011; it does not reopen the separately owned BH result or typical-frame work.

Written by OpenAI Codex (GPT-6; the runtime does not expose a more specific model
identifier or effort). The filename follows the assigned task name. Research check
of row 1011 at the pinned commit above; not an audit and no status grant.
No mass gap is claimed. No numerical or computer-assisted proof is used.

Scope: line-by-line mathematical check of `gap-pinned-cell-gauge-max.md`, especially
W1(i)-(vii), with the later Theorem BH kept separate. This does not check the full
OpenAI O(4)/O(3) papers, the Sussman–Alpoge construction, or any proposed repair's
mixing theorem. Historical run claims will not be treated as proof.

Order disclosure: the FINISH rows were read to locate the sources. Their embedded
summary of the Claude check was therefore visible. The Claude check file itself
was opened only after the first-pass verdicts were written. This is not a
verdict-blind experiment.

Downloads and PDF page extraction are confined to the newly created directory
`/tmp/sa-gap-pinned-cell-gauge-check-astra.i4qhl3`. No mathematical computation
was run. The branch is `check/gap-pinned-cell-gauge-astra-8acc094fd`;
the output is local and uncommitted, with no push authorized by this task.

## First-pass finding, before reading the Claude check file

**W1(v), Lemma CEN: FAILS at line 266.** Take any noncentral quaternion
`h`, and set `h_1=h_4=h`, `h_2=h_3=1`. For every choice of the four links,

```math
(hU_1)U_2U_3^{-1}(hU_4)^{-1}=hU_ph^{-1}.
```

Its real trace equals that of `U_p`. This satisfies the exact hypothesis at
lines 265–266 but violates the conclusion. For example, take `h=i`.
The first invalid proof step is line 270, “The other links are the same.”
The two links leaving the base site are not interchangeable with the other
two under the fixed positive-link, left-multiplier convention.

The exact single-plaquette classification is instead

```math
h_2,h_3\in Z(G),\qquad h_4^{-1}h_1=h_3h_2^{-1}.
```

Here `h_4` is arbitrary. To derive it, vary `U_1` as in the source to remove
the trace. Setting `U_3=U_4=1` forces `h_2` central. Setting `U_2=U_3=1`
and varying `U_4` then forces `h_3` central. The all-identity configuration gives the displayed
relation. Substitution proves sufficiency. This leaves a base-site gauge
conjugation as well as central multipliers.

**Corollary CEN2: FAILS at lines 279–281.** The same example works in every
nonabelian compact group with the stated faithful representation. The trace
separation argument at lines 285–287 is valid; its continuation into CEN is
not. The allowed multipliers need not form an abelian group: the subgroup
`(h,1,1,h)` is a copy of `G`. Infinitesimally, choose `B_1=B_4=i` and
`B'_1=B'_4=j`, all other entries zero. Their linkwise bracket has entries
`2k` on links 1 and 4. It is nonzero, although the corresponding action
derivatives vanish because these are gauge motions. A nonzero Lie bracket
does not by itself supply the useful current signal required by the 2D proof.

The counterexample is not restricted to an isolated plaquette. In a positively
oriented cube, multiply every outgoing link at its minimal corner by `h`.
There is no incoming link at that corner. This is a configuration-independent
left multiplication implementing a gauge transformation, and preserves all
plaquette traces. Thus the unqualified claims at lines 272, 282–283, 536–537,
550–551 and 576–578 cannot stand. A theorem modulo gauge transformations, or
with additional interior/periodicity hypotheses, would be a different statement.

This does **not** undo Proposition B': its zero-curl, positive-response
counterexample uses no CEN input. The broad symmetry classification fails;
the specific all-pin classical-curl bound remains separately testable.

## Remaining first-pass verdicts

Line numbers in this section refer to `gap-pinned-cell-gauge-max.md` at the
pinned commit. All appearances of `a` in the scalar-field specializations
require an imaginary **unit** quaternion. For general `a`, multiply the
quadratic formulas by `|a|^2`.

The three prescribed initial tests all hold. (a) The strengths in B' belong
to the expressly defined `[0,b]` class (142, 236–238). (b) At the base corner,
the two outgoing rotations conjugate the plaquette; its trace is constant.
(c) The sign in FR's decomposition is correct: adding
`lambda_head D_l n` to the gauge direction of `-lambda n` gives
`(lambda_head-lambda_tail)n_tail` exactly. Test (b) also exposes CEN's failure.

| W1 statement | Verdict | Exact scope |
|---|---|---|
| (i) Proposition A(i) | HOLDS | Lines 160–164 and 174–176, including the order and signs of all four insertions. |
| A(ii)–(iii), also read | HOLDS AFTER CORRECTION | Formulas hold at 165–178. At 171 call `N_l` the **negative** left gradient of the action, since `D_B A=-sum B_l dot N_l`. |
| (ii) Proposition W | HOLDS | Lines 186–198 for SU(2), with B zero on boundary links. The general-group sentence at 200 must refer to Haar integration by parts, not the quaternion-specific dot/cross formula. |
| (iii-a) Proposition B | HOLDS | Lines 223–232, with the fixed-tail convention and the supremum over all pins. |
| (iii-b) Proposition B' | HOLDS | Lines 236–251 for the stated variable-strength class. The later homogeneous result is credited below. |
| (iv) Proposition SEAG | HOLDS AFTER CORRECTION | The sum at 300 holds. Specify the far-corner averaging site and define a local plaquette average in 302; homogeneous strengths alone do not make all plaquette means equal in a pinned finite box. |
| (v) Lemma CEN / CEN2 | FAILS | First failing assertions: 266 / 279–281. Explicit counterexample and proof failure above. |
| (vi) Lemma EMB | HOLDS | Lines 322–332 as an identity of conditional laws, up to a pin-dependent normalization. OpenAI's p. 13 was read directly and visually checked. |
| (vii) Lemma FR | HOLDS AFTER CORRECTION | Inequality 465–473 holds on the subcomplex where omega is specified. Its interpretation at 479 is only a local common-axis test, not a characterization of abelian pins. |

### (i) Ordered expansion and free-energy derivative

Write `P=U_1 U_2 U_3^{-1} U_4^{-1}`. Moving each exponential to the
left produces precisely the four factors in line 163, with the inverse-link
insertions following their inverse links. Direct multiplication gives

```math
E'(0)=\delta,\qquad
E''(0)=\sum_i a_i^2+2\sum_{i<j}a_i a_j
       =-|\delta|^2+\sum_{i<j}[a_i,a_j].
```

Taking the real part of `E P` gives line 164. On a finite product of compact
groups, the integrand and its derivatives are bounded; differentiation under
the integral is justified. Fixed left translations of the interior variables
give line 166 for every extension, at every epsilon. Differentiating its
logarithm gives `-E A''-Var(A')`, proving both extension independence and 168.
Collecting its first derivative by link proves 169–172 with the sign correction.

### (ii) Mixed identity and commutator

In the two-parameter path, an inverse link has the order
`U^{-1} exp(-e B') exp(-d B)`. Thus all eight insertions in 187 are in the
right order. Pairing every B insertion with every B' insertion gives scalar
part `-delta(B) dot delta(B')` and imaginary part `kappa(B,B')/2`.
The integral in 196 is independent of `d`, even if B' moves the pin.
Its mixed derivative is therefore zero, giving 190 without any omitted
normalization or mean term. The same-link pairs have signs `+,+,-,-`;
their sum is `delta([B,B'])`, giving the minus sign in 193. This is an
identity, not a positive lower bound from its bracket term.

### (iii) Covariance and the exact zero-curl counterexample

The equality `(exp(eps B)omega)^g=exp(eps Ad_g B)omega^g` proves B by
two derivatives. The map on pins is bijective. At each site SU(2)'s adjoint
action sends a fixed unit `a` to any chosen `n_x`; the orbit statement follows.

For B', only boundary plaquettes have nonzero strength. They involve no
integration variables, so `F=-b sum_boundary w_p t_p` exactly. At the identity
pin its Hessian is `b sum w_p |B_1+B_2-B_3-B_4|^2`. Gauge covariance permits
every field `theta_l n_tail(l)` when taking the pin supremum. For a boundary
plaquette with `z=x+mu`, set `lambda=1_z` on the whole box. Its gradient has
zero curl everywhere, whereas the chosen plaquette has twisted curl
`n_x-n_z`. Choose unequal unit vectors. All summands in the identity-pin
Hessian are nonnegative, and this one is positive. This defeats every finite
K in 237. Independent signs at the three distinct tails remove all mixed
terms, proving 243. No homogeneous-strength or large-b argument is needed.

Lines 253–261 do not prove their scale-growth claim. Keep it labelled ARGUED.
Moreover 257–258 mix two normalizations: a ratio to `b f^2 S^4` scales as S,
whereas the coefficient relative to the unweighted `f^2 S^4` scales as bS.
For the full set of boundary fields there is already **no finite constant**,
because it contains the exact gradients. Any growth discussion must explicitly
restrict to a different, nonzero-curl family.

### (iv) SEAG, all four corners

Here all 24 plaquettes touching z are interior plaquettes of weight one.
For each of the six coordinate planes there are four corners. With the
transported axes of A, the nonzero insertions are:

| Position of z | Nonzero insertions | Gauge average |
|---|---|---|
| x | `a_1=-a`, `a_4=Ad(P)a` | The entire varied plaquette is conjugate to P; its direct term is zero pointwise. |
| x+mu | `a_1=a`, `a_2=-Ad(U_1)a` | Average the gauge at z. P is fixed and the transported second axis has zero average. |
| x+nu | `a_3=Ad(U_1 U_2 U_3^{-1})a`, `a_4=-Ad(P)a` | Average at z. The first listed axis has zero average; P and the other axis stay fixed. |
| x+mu+nu | `a_2=Ad(U_1)a`, `a_3=-Ad(U_1 U_2 U_3^{-1})a` | Average at **x+mu**, not z. Only the first axis rotates; P and the second axis stay fixed. |

The selected averaging sites are unpinned under 296. In each nonbase case,
the two squared lengths contribute 2; the scalar cross term and commutator
average to zero. Thus each contributes `2 beta_p w_p E[t_p]`. There are
six base cases and eighteen others. Since B vanishes on boundary links,
A(ii) gives `H=0` and the variance equality in 300.

Replace 302 by: **“For homogeneous strength b this equals
`36 b tbar_z`, where `tbar_z` is the mean of `E[t_p]` over the eighteen
nonbase plaquettes touching z. If these expectations agree, it is
`36 b E[t_p]`.”** A translation- and coordinate-permutation-invariant periodic law has that agreement;
a general pinned finite box need not. The example concerns this exact
gradient field only. It does not prove the broad assertions about every
fixed-colour field at 313–316, nor uniqueness of a possible cancellation tool.

### (vi) Exact sheet law

All variable links are the direction-1 links listed at 323. The (0,1)
plaquettes have zero strength. On each remaining variable plaquette,
inverting its quaternion product and taking the real part gives
`Re(q_(y+k) u_k(1,1,y)^{-1} q_y^{-1})`, exactly as at 331.
Boundary-tangent bonds have half allocation; the remaining plaquettes
contribute only a constant depending on the pin. The q pins and upper-face
links can be prescribed independently. This reproduces every signed,
right-twisted local law on OpenAI's p. 13. It does not transfer that paper's
mixing theorem to bulk gauge fields or to two-sided background twists.
Credit: OpenAI for the local class; Durhuus and Fröhlich for the layer idea,
as identified by the source. Their original paper was not read here.

### (vii) Frame inequality and its limit

Telescoping around an oriented plaquette transports each `D_l n` to its
base by an orthogonal adjoint map. The triangle inequality gives 465.
For a unit quaternion `cos(phi)+u sin(phi)`, its adjoint is rotation by
`2 phi`, giving the exact left side `2|s_p cross n_x|`. Squaring and using
Cauchy–Schwarz gives `|s_p cross n_x|^2 <= sum_{l in p}|D_l n|^2`.
Every unoriented link is in at most six plaquettes in four dimensions.
Summing and then minimizing independently at each base gives 468.

Replace the setup by: **“Let omega be specified on every edge of a cubical
subcomplex. Sum only over its plaquettes and edges. For a boundary pin,
use the boundary subcomplex.”** Replace the gloss at 479 by:
**“NA=0 exactly when the nonzero plaquette vectors based at each site
are collinear. This local condition does not imply a globally compatible
covariantly constant frame or a pin gauge-equivalent to one maximal torus.”**
Zero plaquette vectors impose no axis condition. The quantitative statements
480–484 remain ARGUED; FR supplies no probability estimate or cancellation
bound. The sign identity 475–477 holds, but does not alone prove that an
action Hessian contains a positive term of the asserted size.

## Comparison with Claude Opus 5.5, row 1014

The complete `gap-pinned-cell-gauge-check-opus.md` was read **after** the
first-pass verdicts above. The following are the disagreements and substantive
qualifications; line numbers in this table refer to that Claude check.

| Lines | Claude's conclusion | Resolution |
|---|---|---|
| 315–319, 487 | CEN holds; h1 and h4 are central “likewise”. | **Claude is wrong at 317.** The explicit `(h,1,1,h)` example above satisfies the hypothesis. Isolating another variable cannot separate the adjacent product `h4^{-1}h1`. |
| 333–335, 488 | CEN2 holds for every faithful compact-group representation. | **Claude is wrong at 333–334.** Trace separation is right; the claimed cyclic continuation is false. The same noncentral gauge example survives in a faithful representation. |
| 494–496, 534 | No WRONG; 4.7 stands including the exact-symmetry assertion. | **Wrong for the symmetry assertion.** B' still proves failure of the specified all-pin classical-curl bound. Keep that conclusion and remove CEN/CEN2 as its support. The latest request requires all statement verdicts, so the independent algebraic checks were completed despite this failure. |
| 171–172, 209 | `N_l` is the derivative of A; no defect. | **Sign correction required.** With the printed `X=-sum B dot N`, N is its negative left gradient. The covariance formula is unaffected. |
| 198–199 | The same-link term has zero expectation; “the term is a covariance, not a mean.” | The zero expectation is right. The displayed same-link contribution to W is **a mean**, `-E X([B,B'])/2=0`. No covariance of this current appears there. Do not infer a nonzero integrated gain from this sentence. |
| 248–253, 485 | The bS scaling orders are consistent as written. | **Normalization needs correction.** A ratio of `b f^2 S^5` to `b f^2 S^4` is of order S. The coefficient relative to an unweighted curl energy is of order bS. No finite constant exists on the full class containing exact gradients. |
| 284–286, 486 | A homogeneous interior gives common `E[t_p]` at all eighteen plaquettes. | **An extra hypothesis is inserted at 285.** Homogeneous couplings do not provide the required symmetry of a pinned finite box. Use `tbar_z`, or assume equality of those expectations. |
| 437–439 | SEAG's direct term is strictly positive at every pin and every strength field. | **False at 438.** At `beta_p=0` for all p, both sides of SEAG are zero. Its identity is valid, but universal strict positivity is not. B' still supplies a positive counterexample to the proposed uniform bound. |

We agree on A(i), W's mixed coefficient, B, B' on its stated class, EMB,
the FR inequality, FR's local-axis restriction, and SEAG's corrected
far-corner averaging site. We also agree that SEAG does not rule out an
optimal extension at the trivial pin. The frame-domain clarification above
is additional, not a disagreement about the telescoping inequality.
Claude's two-sided corner-product observation at 339–342 is compatible
with the counterexample: all four corner products there equal 1. Its
qualification **“up to gauge”** is essential. It does not prove the original
left-multiplier statement, which failed to remove even base-site gauge motions.

The homogeneous-strength reservation at Claude lines 101–109 and 500–504
was justified for row 1011 alone. It is now superseded by row 1016's BH,
not by a repair of the zero-interior-coupling proof. See the next section.

### The two corrections to row 1009

The original lines 387–390 and 402–418 of
`prior/gap-o4-pinned-cell-read-opus.md` were read directly.

1. **HOLDS AFTER CORRECTION:** replace row 1011 lines 414–415 by:
   “The proposed SF inequality does not follow merely by dropping the
   variance. The direct term contains transported colours and commutators;
   it has no universal bound by the ordinary curl energy for arbitrary
   fixed-colour extensions. The optimal-extension inequality at the trivial
   pin remains open.” B' gives a positive obstruction in the specified
   all-pin class. SEAG explains the cancellation for its interior-gradient
   example; it does not assert strict positivity at all strengths.
2. **HOLDS AFTER CORRECTION:** replace lines 416–418 by:
   “For a fixed box, field and bounded strengths, compactness gives a finite
   pin supremum. It does not give a bound proportional to the classical
   curl energy. B' refutes that latter bound on C_b.” This agrees with the
   substance of Claude's narrowing at 455–466. The literal observation that
   an already uniform upper bound survives a supremum is not false.

## Later result: Theorem BH belongs to row 1016

Read directly: `gap-global-reform-max.md:693–791`, including AV, AV2 and
BH's full argument. **BH's positive lower bound HOLDS.** It is Claude
Fable 5.2's later result, not new work by this check. It does not use CEN.

The key identity is integration by parts on the boundary Haar variables:

```math
\mathbb E_{\rm free}H(B)
=\mathbb E_{\rm free}\bigl(\mathbb E_\omega X(B)\bigr)^2.
```

For the boundary plaquette and indicator gradient in BH, its score psi
is pin-measurable. Thus Cauchy–Schwarz and the free Haar integration by
parts give the lower bound from `E[X psi]` and `E[psi^2]`. The two distinct
site averages in 745–750 give, exactly,

```math
\mathbb E[X\psi]=2\mathbb E[t_p],\qquad
\mathbb E[\psi^2]=\frac23\mathbb E[1-t_p^2],\qquad
\sup_\omega H(B)\ge
\frac{6(\mathbb E[t_p])^2}{\mathbb E[1-t_p^2]}.
```

The denominator is positive at finite b: the density is strictly positive
on the entire finite product group and the plaquette trace is not identically
±1. The corner-link conditioning argument in 752–759 gives at least one
boundary plaquette with positive mean for each b>0. It requires d>=3 to
make every plaquette at that chosen link a boundary plaquette. Therefore
BH refutes a homogeneous-strength all-pin curl bound with its exact-gradient
test, at each finite box and b>0. This closes the reservation in row 1014.

Its fixed-box growth statement is **HOLDS AFTER CORRECTION** to the last
estimate: use the exact constant `2 log(3 pi^3/8)` in place of `4.92` at
764, and apply 766 only once `2^(d-2)e(b)<1`. Squaring the lower bound
`E t_p >= 1-2^(d-2)e(b)` requires that restriction. The displayed small-ball
measure estimate and convexity give `e(b)=O_c(log(b)/b)`, so this restriction
holds eventually and the stated fixed-box lower growth `b/log b` follows.
No computation is needed. No size-uniform bS growth follows. BH2's separate
WN-dependent general-field extension was not checked here.

## Remaining lines and numbered conclusions

The entire 622-line target was read. This table accounts for the portions
outside the detailed W1 checks, without promoting its labelled readings into
theorems.

| Target lines | Disposition |
|---|---|
| 1–100 | Provenance, plan and earlier-reading summaries. Historical timings and searches are not proof and were not independently reconstructed. |
| 102–125 | M1–M3 agree with the directly read O(4) p. 13. M4–M8's full 2D proof is outside this check; they are credited source inputs. |
| 131–154 | Cell action, Haar gauge covariance and conditional independence hold. Signed strengths need not be a **closed** centre-flux cocycle. |
| 180–182 | HOLDS for compact U(1): adjoint transports on its Lie algebra are trivial and every commutator is zero. |
| 200–208 | The SU(2) identity is not literally a quaternion formula for every group. The shell coefficient holds with the error correction below; the claimed bracket-power interpretation at 207 is not proved. |
| 210–215 | Dependence on transported colours is correct. “Cannot be repaired inside C_b” must mean the exact bound refuted by B', not every possible choice of twist or observable. |
| 272–292 | CEN/CEN2-dependent assertions fail. A closed central link field has coboundary 1 and flips no plaquette signs. A general central link field changes signs by its coboundary; these two cases must not be conflated. The separate cohomology commentary does not repair CEN. |
| 334–342 | The embedded law and its flat-face change of variables hold. General bulk mixing or D2's quantitative conclusion is not supplied by the embedding. |
| 344–362 | HOPF is explicitly an unrebuilt smooth-topology input; no new certification here. AR's commuting ring variables have no Lie-bracket signal. This does not prove that no other effective-action gain is possible. |
| 364–375 | HOLDS AFTER CORRECTION: B' refutes the stated ordinary-curl normalization. Remove the false symmetry classification and any blanket exclusion of every class-supremum construction. |
| 377–411 | GUIDE results were not rerun or used. Prior-work claims are credited, with the search limits above. |
| 413–418 | The two corrected wordings are given above. |
| 420–436 | The U(1) algebra holds. The assertion that CEN holds for Q8 and 2T is false by the same base-site example, using any noncentral element of either group. The Lie-derivative method indeed does not apply to finite groups. D2, SHEET, G8, PT and NP are not rechecked as separate theorems. No mixing implication is proved in this table. |
| 438–458 | B' refutes the proposed induction normalization. The log coefficient and a bracket identity alone are not a gain theorem. CEN cannot rule out all symmetry repairs. |
| 475–501 | The frame sign identity holds. The proposed N1–N3 are open; no proof establishes that every repair must use first-passage data or remain above the band. |
| 503–512 | HOLDS for the mixed derivative identity: disjoint plaquette supports remove the direct mixed term, leaving minus the covariance. Calling this a sufficient mixing criterion needs a quantitative norm and theorem. The claimed absence of any sum rule does not follow from CEN. |
| 514–538 | Search limitations retained. The plain-language assertion at 536–537 excluding every noncentral operation fails by base-site gauge transformations. These transformations leave gauge-invariant observables unchanged and do not provide a mixing proof. |
| 559–620 | No mass-gap advance is shown. Proposed work items and registry dispositions are not theorems. G1 may be excluded only with the exact B'/BH ordinary-curl normalization; G2's probability and cancellation obligations remain open. No registry is edited. |
| 622 | Must carry the corrected CEN/CEN2 verdict, SEAG/FR restrictions, and separate BH provenance. It cannot report all listed claims as proved. |

**Section 3.4: HOLDS AFTER CORRECTION.** With mesh `h=2 pi/N`, `M>=4h`,
and `K>=M`, the appropriate four-dimensional assertion is

```math
N^{-4}\sum_{k\in h\mathbb Z^4\, :\, M\le |k|\le K}|k|^{-4}
=\frac{1}{8\pi^2}\log(K/M)+O(h/M).
```

The error is **additive**, not the asserted uniform relative error at 204.
For the hand estimate, compare each grid value with the integral over its
cube. The radial gradient has size `4 r^{-5}`; summing cube errors is bounded
by a constant times `h integral_M^infinity r^{-2} dr`. The cubes intersecting
the two shell boundaries contribute at most `C h/M+C h/K`. Adjusting the
lower radius by the cube diameter changes only the constant. The spherical
integral is `2 pi^2 log(K/M)`. Division by `(2 pi)^4` gives the coefficient.
Arbitrarily thin shells between successive lattice radii have zero sum and
a positive integral, disproving a uniform relative error claim. This is only
shell arithmetic. It does not construct the nonlinear gauge-wave family in
207. Scale invariance in 4D means rescaling the field strength as `S^{-2}`;
the action of a field strength held fixed instead grows as `S^4`.

Verdicts on the **five numbered statements of 9.2**, as requested:

1. **HOLDS AFTER CORRECTION** (541–543): keep the finite-volume identities;
   state the shell normalization, additive error and regime above.
2. **HOLDS AFTER CORRECTION** (544–548): B' proves failure of the exact
   all-pin ordinary-curl bound. Delete “only link symmetries are central”;
   keep size growth labelled ARGUED and distinguish its normalization.
3. **FAILS**, first failing claim at 549–551 that SU(2) has “no twist”
   because every symmetric multiplier is central. The CEN counterexample
   gives noncentral gauge twists. No useful nonzero current signal follows.
4. **HOLDS** (552–553): the conditional-law embedding, with its stated
   credit and absence of a bulk conclusion.
5. **FAILS** as a deduction from FR, first unsupported exclusivity at 555.
   FR's inequality holds, but a defect-free frame need not be small-field:
   take arbitrary links in one maximal torus and its constant unit axis.
   Then `D_l n=0` even with large plaquette angles. FR proves neither a
   typical-field theorem nor that all alternative repairs fail in the band.

## Sussman–Alpoge source record and exclusions

Credit Ethan Sussman and Levent Alpoge, **with Claude and Codex as the
authors of their text**. Their outline and CA-I were each fetched once at
`31a47c543775`, into the scratch directory named above. No other Sussman–Alpoge
version is silently substituted.

The full index README was read. The chunk files and `obligations.md` were
searched for the pinned class, stiffness, seagull, central/link symmetries,
Schwinger–Dyson/Ward identities, holonomies and frames. Matching rows and
neighbours were read before these source passages:

| Index and source | Relation to this check |
|---|---|
| Chunk 02, rows around 2094–2117; outline 2094–2117 | Their “link symmetry” is **spatial link reflection**, not multiplication of group-valued links. This hit does not prove CEN. |
| Chunk 10, rows 11299–11361; outline 11313–11352, PX114–PX118 | Their plaquette insertion expansion and curvature remainder already contain the method behind A. Credit this prior method; the result concerns constrained/small-curvature forms, not B's pin supremum. |
| Chunk 12, rows 13016–13080; outline 13048–13065, PH8 | A compact gauge Ward identity at a stationary point. The vanished first derivative is explicit; it is not a claim that every gauge tangent is Hessian-null at every pin. |
| CA-full index rows 46–53; CA-I 15469–15530, `4.5:lem-ward-identities` | The account labels the nonlinear-gauge Ward lemma PROVED and derives the current correction. This supports the distinction between the gauge orbit curve and an exponential left-link tangent curve at a noncritical background. No rederivation of its operator-localization machinery was attempted. |

The prescribed `ca-4.12-4.19/` index was also searched for these target
terms; it yielded no matching supplier. The relevant account hit is in
4.5, outside that subindex. These bounded searches do not assert that the
entire account lacks every possible related result.

OpenAI's O(4) PDF at `4eaee87548250b2682affda7d05d947c05554bae`, pages
13–14, was fetched once, extracted locally, and page 13 visually inspected.
Its fixed right twists, signed strengths, half boundary allocation and
equations (3.4)–(3.8) were used only for the stated class/identity comparison.
The rest of that proof and the O(3) continuum theorem were not checked.
Balaban's original papers were not read or imported; their cited role is
attributed through the account, not certified here.

No numerical job, automated proof, audit, ledger update, source repair,
external post or mass-gap claim was made. Only this requested output file
was written. The core surviving conclusion is the failure of the exact
all-pin ordinary-curl bound, proved by B' and extended to homogeneous
strengths by the later BH. The symmetry classification in CEN/CEN2 fails.

RESULT: Row 1011 requires correction: CEN and CEN2 FAIL at 266 and 279–281; A, W, B and B' retain their stated finite-volume content, SEAG and FR hold with the corrections above, EMB holds, and row 1016's BH preserves the homogeneous-strength obstruction; no mass gap or scientific status is granted.
