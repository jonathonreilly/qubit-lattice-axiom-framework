## Repo search

The task-specific prior note is absent. The lead's November 8 digest records
searches of main and PRs 10114, 10133, 10134 and 10141 for thirteen earlier
UV/RG targets. It contains no target-specific prior result for this face
model. I read the digest in full and checked its nearest hits:

| Prior hit checked | Closeness to B1 |
|---|---|
| Main `research/ym4d/library/out-mu.md`, L8–32, 69–82, 180–190 | Axial representatives and regular-window minimizers. Different measure and domain; no flat-plane Gibbs limit. |
| Main `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md`, L120–145 | A determinant-weighted noncompact Dirichlet Maxwell covariance bound. Not the anisotropic face Gaussian law. |
| PR 10114 `.../ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`, L106–149 | A positive one-step plaquette witness, not long-distance decay or a chiral decomposition. |
| B1's REM/F3 and O(n) reading files | Direct antecedents for removable pin twists and the proposed annulus port; credited and reused below. |

The main snapshot read was `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`;
PR 10114 was `f76f6c649cff7dffbab664d8976e680e8f287fe9`, matching the digest.
The digest reports the corresponding soft-route source identical on PR
10133; that is a recorded lineage statement, not a fresh second check.
The registry search found no competing entry under the face-model or Pin(2)
names. This is the assigned B1 check of row 1053, not another attack on
row 1051's isotropic annulus work. No novelty or exhaustive absence is claimed.

Author: OpenAI Codex, assigned GPT-6 Astra / xhigh by row 1061. The exact runtime
model and effort are not exposed to this session, so the assignment is recorded
as such. Source pin: `1b75bdfbaf4fdd983b195df0af18ea271d1abbbc`.
Research check, not an audit; no scientific standing or mass gap is claimed.
Coverage: B1 only. Excluded: a proof of FACE-TW, FACE-SG, BR-L', the 2D input
theorems, and the four-dimensional gap. No numerical proof or Lean run.

The six planned stages are complete: prior sources; face identities;
capacity and iteration; EVEN/Gaussian/one-loop comparisons; Orland; vector
verdicts. The final checkpoint at the end records the open obligations.

Only the report is edited. Downloads are in newly created directories under
`/tmp`, beginning with `/tmp/sa-gap-wall-vectors-check-astra.KPy8Iw`.
The two requested Sussman–Alpoge files were fetched once at `31a47c543775`.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors
of their text; Claude Fable 5.2 for row 1053. Source details follow.

## 1. Exact face identities (source §§6.1–6.3)

### FACE-LIM — HOLDS

Read line by line: source L228–232. First failing step: none, on a finite
product of rectangles with free boundary and fixed finite mixed/transverse
couplings. This says nothing about periodic longitudinal holonomies.

Here is the missing normalization written explicitly. After comb-tree gauge
fixing, put `H_k = V_{k+1} V_k^{-1}` in each remaining row. Successive left
translations show that the change from the `V_k` to the `H_k` preserves
product Haar measure. Each longitudinal plaquette contributes one independent
factor `exp(beta_L Re H_k)`. Let `nu_b(dH)` be its normalized law. Outside any
neighbourhood of 1, `Re H <= 1-delta`; a smaller neighbourhood has positive
Haar measure and `Re H >= 1-delta/2`. Their exponential ratio proves
`nu_b -> delta_1`. There are finitely many plaquettes, so their product also
converges. Multiplication reconstructs every `V_k -> 1`.

Write the remaining positive continuous weight as `h`. The expectation is
`integral F h / integral h` against this product law and transverse Haar
measure. Both integrals converge; the limiting denominator is positive.
This proves the normalized limit, not just concentration of the action.
Mixed plaquettes become the displayed nearest-neighbour quaternion products.
The residual transformations satisfy `g(u,x)=g(u',x)` along every longitudinal
edge, hence are precisely the constant-in-u transformations `g_x`.

### ANCH — HOLDS

Read line by line: L236–237. First failing step: none. Multiplying
`Phi=s_0+i s.sigma` by `Phi'^{-1}` gives scalar part
`s_0 s'_0+s.s'`. Normalized Haar on SU(2) is uniform measure on the unit
3-sphere. With `beta_T=0`, the action and reference measure both factor over
transverse links. This proves the finite-volume product identity.

### ANCH-W — HOLDS AFTER CORRECTION

Read L239–245. The mixed rectangular-loop identity holds. Fix distinct
transverse path edges `l_1,...,l_T` and the same two longitudinal endpoints
in every sheet. Independent global left rotations of each O(4) sheet imply
`E[Phi_l(0) Phi_l(R)^{-1}]=G(R) I`. Integrate the innermost pair of matrices
in the rectangular holonomy, then the next pair. This gives `G(R)^T` even
though the matrices do not commute.

Correction to L239: **“A transverse loop containing an edge exactly once
has expectation zero; in particular every nondegenerate simple transverse
loop does.”** A backtracking closed walk has holonomy 1, so the unqualified
statement about every transverse loop is false. Haar invariance of a sheet
at one site gives `E Phi_l(u)=0`, which proves the corrected assertion.

The cited spin bound gives `|E W(R,T)| <= A^T exp(-mRT)`. Thus the asymptotic
area rate is at least `m` as `R -> infinity`; it does not give the bound
`exp(-mRT)` for every finite rectangle. Full local-observable clustering
still needs the separate mixing input. The posted 2D results and the
Peierls/plane-rotator imports are not proved or certified by this check.

### RIG — HOLDS AFTER CORRECTION (scope)

Read line by line: L249–259. The SU(2), two-transverse-dimensional statement
holds, for `beta_M >= 0` and finite positive partition functions. On-site
terms must be invariant under independent transverse site transformations
at each fixed `u`. The printed extension to **every compact Lie group** needs
a specified representation, generator norm and degree-dependent constant;
its numerical coefficient is not established as written.

For one incident link and one longitudinal bond, averaging the two twists
changes its action by `-beta_M w_0(1-cos(delta/2))`, bounded below by
`-beta_M delta^2/8`. There are at most four incident transverse links. Thus
`(S_++S_-)/2 >= S-beta_M D/2`. Separate Haar changes of the interior
variables give the two twisted-boundary integrals. Cauchy–Schwarz gives
`Z_+ Z_- >= (integral exp((S_++S_-)/2))^2 >= exp(-beta_M D) Z^2`.
All factors and signs agree. No constant depends on `beta_T` or transverse
volume. For transverse degree `d_x`, the same proof gives
`exp(-beta_M d_x D/4)` in place of `exp(-beta_M D)`.

## 2. Capacity and iteration (source §§6.4–6.5)

### FACE-MW — HOLDS AFTER CORRECTION (domain and interpretation)

The three numerical constants **24, 12 pi^2 and 48 pi^2 hold**. Read L263–267
line by line. Specify integer radii `1 <= r < R`, `log(R/r) >= 1`, the
nearest-neighbour square lattice, the SU(2) normalization of §6, and
`||f||_infinity = sup_z |f(z)|` with Euclidean norm for vectors. The model
must have the finite positive densities used in the proof. Hard constraints
need a separate invariant-support version; no such generalization is used.
The rotation/capacity method is credited to Dobrushin and Shlosman,
McBryan and Spencer, and Pfister, as in the source note; no theorem from
those papers is used in place of the written estimate.

Let `L=log(R/r)` and let the profile be constant `t` inside `B_r`, zero on
and outside the shell `R`, and `t log(R/k)/L` on shell `k`. Exactly `8k+4`
nearest-neighbour edges join square shells `k` and `k+1`: four sides, each
with `2k+1` outward edges. Corners contribute two different outward edges.
The profile jump is `t log(1+1/k)/L`, whose absolute value is at most
`|t|/(kL)`. Therefore

```math
D \le \frac{t^2}{L^2}\sum_{k=r}^{R-1}\frac{8k+4}{k^2}
\le \frac{12t^2}{L^2}\sum_{k=r}^{R-1}\frac1k
\le \frac{12t^2(1+L)}{L^2}
\le \frac{24t^2}{L}.
```

The penultimate inequality follows by separating `1/r <= 1` and comparing
the rest to the integral of `1/x` from `r` to `R`. No numerical estimate
enters. Applying RIG to the annulus gives
`p(gz)p(g^{-1}z) >= exp(-epsilon)p(z)^2`, with
`epsilon=24 beta_M t^2/L`. Interior weights and reference measure are
invariant under constant `g`.

Put `q=(p o g+p o g^{-1})/2`. Then `q >= exp(-epsilon/2)p` and
`integral p=integral q=1`. Consequently
`integral |p-q|=2 integral(p-q)_+ <= 2(1-exp(-epsilon/2)) <= epsilon`.
For any bounded scalar component, the change of expectation is at most
`epsilon ||f||_infinity`. At `t=pi`, choose the axis perpendicular to the
component. Both adjoint rotations reverse that component. Division by two
gives `12 pi^2 beta_M ||f||_infinity/L`. For a centre-odd observable,
`t=2pi` makes both transformations equal to minus the identity on `f`;
the same division gives `48 pi^2 beta_M ||f||_infinity/L`.

Correction to L267: **“The face admits a gauge-fixed spin description with
residual group G. Charged expectations relative to a pin obey FACE-MW.
Original gauge-invariant observables still restrict to G-invariant
functions. A charged two-point function can represent an observable with
specified longitudinal parallel transport.”** Freezing plaquettes does not
make arbitrary gauge-variant quantities physical; FACE-LIM itself retains
the gauge-invariant restriction. This correction does not change the bound.

### ITER — HOLDS AFTER CORRECTION (one missing reversal)

Read L271–279 line by line. The hypothesis remains OPEN. This check proves
only the displayed implication, with fixed finite inner support and positive
finite-volume kernels. It does not prove FACE-TW or exponential decay.

First incomplete line: L276, **“Averaging over g: K_j >= (1-eps_j) Kbar_j.”**
Direct averaging of the preceding inequality gives the opposite comparison.
The stated stronger conclusion nevertheless follows from the all-`g`,
all-pin hypothesis. Replace that passage by:

**“Write `c=1-eps_j`. Simultaneous rotation of both boundary layers leaves
`W` unchanged, and the interior partition function is invariant. FACE-TW
therefore gives `k_y(gz) >= c k_y(z)` for every `g,z`. Apply this inequality
at `g^{-1}z`, then average over `g`. This gives `k_y(z) >= c kbar_y(z)`.
Hence `R_y=(k_y-c kbar_y)/eps_j` is a probability density.”**

If `eps_j=0`, the kernel is already invariant and its action on the
zero-average subspace is zero; no division is needed. For `0<eps_j<1`,
the printed decomposition follows exactly, without a factor loss.

To check the other delicate line, let `F_j(z)` be the expectation of `f`
inside shell `j` with boundary `z`. A constant change of every interior
variable gives `F_j(gz)=E_z[f(g configuration)]`. Haar-averaging this identity
uses the pointwise orbit-average assumption on `f` and gives zero. The
nearest-neighbour Markov property yields `F_{j+1}=K_j F_j`. The invariant
part annihilates `F_j`; the residual probability kernel contracts its sup
norm by at most `eps_j`. Conditioning on the outermost shell covers any
exterior pin. Induction proves the claimed product.

For an explicit faster-than-power conclusion, fix `A>0`. Eventually
`eps_j <= 2^{-A}`. The finitely many earlier factors form a constant, so
`product eps_j <= C_A 2^{-AJ} <= C'_A N_J^{-A}`. This is a hand proof of
the required conclusion; for `C>0`, `exp(-(1+o(1))J log J)` also follows
by comparing `sum log(j+c)` with its integral. Neither conclusion implies
a positive spectral gap in the singlet sector.

## 3. EVEN and the Gaussian checks

### EVEN — HOLDS; its physical consequence needs qualification

Read L289–294. First failing step in the lemma: none. Write
`t=diag(exp(i theta),exp(-i theta))` and `j=i sigma_2`. Direct matrix
multiplication gives `j t j^{-1}=t^{-1}`. The constant allowed gauge
transformation by `j` therefore inverts **all** torus links simultaneously.
Restriction of an SU(2)-gauge-invariant function is invariant under this map.
The same statement holds for Pin(2)-gauge-invariant functions, since `j`
belongs to Pin(2). It does not assert invariance under independent inversions
of single links.

Correction to the consequence: **“If an effective abelian description is
identified with the torus restriction and respects this Weyl transformation,
its restricted observables are even under simultaneous sign reversal of the
abelian field.”** EVEN alone proves neither abelian dominance nor that every
observable of a putative massless branch is such a restriction.

For the Gaussian comparison, let centred jointly Gaussian variables `X,Y`
have common variance `v` and covariance `c`. Their characteristic function
gives `Cov(cos X,cos Y)=exp(-v)(cosh c-1)=exp(-v)c^2/2+O(c^4)`.
Thus a four-dimensional curvature covariance of order `|x|^{-4}` yields
an even-observable covariance of order `|x|^{-8}`, for components/directions
with a nonzero leading coefficient. This is a Gaussian statement only.
Finite-beta Pin(2) includes nonflat component configurations; calling them
rare supplies no estimate preserving this power law. No Pin(2) massless
phase is proved here or by EVEN.

### §6.6, first bullet: Gaussian face — HOLDS AFTER CORRECTION

Read L283. The quadratic form and its two eigenvalues hold, with lattice
momenta replaced by their difference symbols for an exact lattice formula.
Specify `beta_M>0`, `beta_T>0`, an infinite symmetric transverse lattice,
and the longitudinal large-distance limit. For transverse momentum `q`,
let `P_L(q)` project onto gradients and `P_T=I-P_L`. The covariance is

```math
C(p,q)=\frac{P_L(q)}{\beta_M\widehat p^2}
       +\frac{P_T(q)}{\beta_M\widehat p^2+\beta_T\widehat q^2}.
```

For the curl observable `B`, the first summand vanishes and the second gains
`widehat q^2`. Its low-momentum radial integral is, up to smooth ultraviolet
terms and with `a=beta_M p^2`,

```math
\frac1{2\pi}\int_0^\Lambda\frac{q^3\,dq}{a+\beta_Tq^2}
=\frac{\Lambda^2}{4\pi\beta_T}
 -\frac{a}{4\pi\beta_T^2}
  \log\frac{a+\beta_T\Lambda^2}{a}.
```

Its nonanalytic part is a nonzero multiple of `p^2 log(p^2)` and has the
stated `|u|^{-4}` tail. One can check the power without distributions by
writing `(beta_M p^2+beta_T q^2)^{-1}` as its heat integral: the Gaussian
`p` integral contributes `s^{-1} exp(-|u|^2/(4 beta_M s))`, and the `q^2`
weighted transverse integral contributes `s^{-2}`. The remaining integral
of `s^{-3} exp(-c |u|^2/s)` scales as `|u|^{-4}`.

For a single link direction, symmetry gives the Brillouin-zone average
`(P_L)_{ii}=1/2`. The two-dimensional Green-function difference is
`(2 pi)^{-1} log|u|+O(1)`. Hence the variance of the link-angle difference
has logarithmic coefficient `1/(2 pi beta_M)` and its exponential has power
`1/(4 pi beta_M)`, as printed. The curl contribution has no logarithmic
infrared divergence when `beta_T>0`.

Two omitted limits matter. At `beta_T=0`, both polarizations are massless:
the charged exponent is `1/(2 pi beta_M)`, not `1/(4 pi beta_M)`, and the
unsmeared noncompact curl field has an infrared divergence. For a fixed
finite transverse graph, every nonzero curl mode is massive in `u`; the
continuum `q` integral and its tail do not apply. The charged logarithmic
coefficient is then determined by the edge diagonal of the projector onto
the zero-curl modes. Finally, this Gaussian calculation does **not** prove
a power law or failure of FACE-TW for the compact U(1) model. Those
statements require a compact-model input.

### §6.6, third bullet: dimensional scaling — HOLDS AFTER CORRECTION

The displayed factors are correct **classical engineering factors**, not an
exact blocking flow. A plaquette of type `mu,nu` has quadratic weight
proportional to `beta_{mu nu} a_mu^2 a_nu^2`; the site density is
`a_long^{-2} a_perp^{-d_perp}`. Matching these coefficients yields
`beta_L proportional a_perp^{d_perp}/a_long^2`,
`beta_M proportional a_perp^{d_perp-2}`, and
`beta_T proportional a_long^2 a_perp^{d_perp-4}`.
Thus changing the transverse unit by `b` gives the three printed powers.
Replace **“blocking ... sends them to”** by **“classical rescaling assigns
these engineering factors; actual blocking also renormalizes couplings and
generates other interactions.”** Marginality in `d_perp=2` and the factor
`b` in `d_perp=3` hold at this level. The assertion about the final flow
steps being in the strong-coupling band is not proved by dimensional
counting.

## 4. One-loop normalization and the scale-matching step

### §6.6, second bullet — HOLDS AFTER CORRECTION

The SU(2) leading exponential coefficients hold in the stated convention.
They are perturbative comparisons, not correlation-length theorems. Use
`beta=4/g^2` and action `g^{-2} tr(dPhi^dagger dPhi)` for the chiral field.
Since `tr(dPhi^dagger dPhi)=2|ds|^2`, its O(4) stiffness is `beta`.
The conventional one-loop stiffness coefficient is `(4-2)/(2pi)=1/pi`.
Thus `d(g^{-2})/d log(mu)=1/(4pi)`. This agrees with Orland's
`exp(-2pi/g_0^2)` mass exponential after `g^2=2g_0^2`; his action is
`(2g_0^2)^{-1} tr(dPhi^dagger dPhi)` (2006, (4.2), (6.3) and the paragraph
after it; 2007, (1.1), (1.6)).

The four-dimensional coefficient `11/(12pi^2)` for `g^{-2}` gives
`d beta/d log(mu)=11/(3pi^2)`. It matches the Sussman–Alpoge convention
`x_0=beta`, `c_0/log L=11N^2/(12pi^2)` at `N=2`
(SA 6844–6854, 6871). This comparison does not certify their one-loop
calculation or their nonperturbative running assumptions.

For the printed general-N normalization, Orland's (1.6) has leading
exponential `exp(-4pi/(N g_0^2))`. The same conversion gives
`exp(-8pi/(N g^2))`, hence the formal inverse-coupling coefficient
`N/(8pi)`. Converting the outline's beta coefficient by `beta=2N/g^2`
gives `11N/(24pi^2)` in four dimensions. These are source-normalization
checks, not a new derivation of either perturbation expansion.

Integrating these leading beta functions to a fixed order-one coupling gives
the formal running scales `log ell_4=(3pi^2/11) beta+lower-order terms` and
`log ell_2=pi beta+lower-order terms`, each measured in its **own matched
ultraviolet units**. Identifying these scales with actual correlation lengths
is an additional step, especially in four dimensions. The ratio of the two
inverse-coupling coefficients is `3pi/11`, as printed. No decimal evaluation is
needed. Replace the equalities for the scales by leading-exponential
statements, retaining unknown prefactors and subleading logarithms. This
checks the normalization and algebra, not the loop expansion's error bounds.

### §4.2's formula used to exclude R — FAILS as an unconditional argument

First unsupported line: L183, **“The sheets then have two-dimensional
coupling g(a_perp) at the scale a_perp.”** This is a matching assumption,
not a consequence of the preceding classical anisotropic coefficients.
The anchor in ANCH instead has bare sheet stiffness `beta_M` at longitudinal
lattice spacing `a_long`; its correlation length in longitudinal lattice
units depends on `beta_M`, not on an independently chosen `xi`.

The missing step is visible even within the printed leading-exponential
approximation. From the tree coefficients and the actual anchor's bare
stiffness, one obtains

```math
\xi_{2,\mathrm{lat}}\asymp e^{\pi\beta},\qquad
\beta_T\xi_{2,\mathrm{lat}}^2
 \asymp \frac{\beta}{\xi^2}e^{2\pi\beta}.
```

It does not equal `beta exp(2pi beta)` without further matching. At this
purely algebraic level, choosing `xi^2=(beta/epsilon) exp(2pi beta)` makes
the first defining quantity of R equal to `epsilon` and gives
`beta_L=beta^2 exp(2pi beta)/epsilon`, satisfying its second inequality for
`beta>=1`. This is **not** a continuum construction or a counterexample to
physical isotropy. It shows that the displayed tree equations alone do not
exclude R. Large anisotropy makes the missing logarithmic matching more,
not less, important.

Correct conditional text: **“Suppose the anisotropic model can be matched
at the transverse scale to an O(4) sheet with renormalized coupling
`g_M(a_perp)=g_4(a_perp)`, and suppose the transverse coefficient there is
`4/(g_4(a_perp)^2 xi^2)`. To leading exponential accuracy the sheet length
is `xi exp(4pi/g_M(a_perp)^2)` in longitudinal units. Under these additional
assumptions their product grows like
`(4/g_4(a_perp)^2) exp(8pi/g_4(a_perp)^2)` as `g_4 -> 0`.”**

No matched anisotropic running, error estimate, or Lorentz-invariant
trajectory with these properties is supplied. The formula supports a
conditional warning; it does not prove that every trajectory must leave R.

## 5. S0, the dimension argument, and the five vector verdicts

These verdicts judge the assertions in row 1053. A FAILS below can reject
its **negative argument**; it does not turn the proposed vector into a
successful route. The author labels these route assessments ARGUED, not
PROVED. The failures below identify unsupported inferences in those
arguments; they do not attribute a stronger proof claim to the author.

### §4.1 S0 / V1 — HOLDS, for the submitted route

A positive clustering lower bound uniform in `beta_L in [beta,infinity]`
implies the desired reference-coupling isotropic clustering simply by
setting `beta_L=beta`. Thus BR-L contains the reference-scale objective.
FACE-SG is also an additional singlet input, not supplied by a charged
estimate. No mechanism proving either is given. V1 therefore supplies no
completed route to the target.

Keep the scope: BR-L alone is not the all-cutoff, all-state T_JW-lat of
row 1052 L485. The stated scale transport and identification are still
needed. Nor does endpoint containment refute the possibility of proving a
useful comparison theorem. BR-L' is a conditional bridge whose proof might
be useful; it is unproved here, not a logical contradiction.

### §4.1 dimension count — FAILS as an exclusion

First unsupported line: L175, **“A flux twist ... needs its colour axis to
be covariantly constant on a three-dimensional set.”** No quantified class
of flux deformations or necessity proof is given. The construction described
there propagates an axis along longitudinal planes and a transverse path;
it therefore requires mixed-plaquette compatibility on that chosen side.
This explains that construction's problem. It does not exclude a different
deformation using frames on a two-dimensional set. Discrete central twists
need no colour axis at all, so even the word “flux” must be restricted to
the intended continuous noncentral twist.

The `k=2` logarithmic capacity calculation is valid. The cited ordered
`k=3` spin model obstructs a uniform disorder estimate for that particular
layer device, conditional on its ordering theorem. Neither proves the
necessity of `k=3` for every flux method.

Replacement for L175–177 and the corresponding B3 sentence: **“This
construction supplies rigid gauge-frame twists on two-dimensional planes.
For the continuous noncentral flux construction considered here, extending
the chosen frame along a transverse path requires compatibility not imposed
by the face model. No two-dimensional framed flux construction was found;
none is excluded by the dimension count.”** The stronger exclusion in
L301 and the summary L343 must be removed as well.

### §4.2 S0 / V2 — FAILS on the stated renaming argument

The first failure is the scale matching at L183, detailed in §4 above.
The parametric region itself is not proved, and there is no constructed
Lorentz-invariant continuum trajectory inside it. Thus V2 is an uncompleted
proposal. Calling it an established renaming of the band goes beyond this
argument. Use the conditional text above, and leave the trajectory question
open. The known anisotropic literature does not fill this gap.

### §4.3 S0 / V3 — HOLDS AFTER CORRECTION

The submitted text gives no uniform bulk estimate. Calling that estimate
exactly **“the one-box estimate”** at L187 is not a demonstrated equivalence:
its constrained specification and domain differ. Charged decay on a defect
does not supply bulk clustering. The U(1) perimeter observation is a
perturbative or cited comparator here, not a proof of the bulk assertion.

There is also a specific error in the proposed limit at L142. With the
skeleton anchored at `s Z^4`, the fine plaquette at the origin in the (0,1)
plane stays frozen for every integer `s`. Its normalized trace is always 1.
At finite-coupling unconstrained Wilson specification the conditional link
densities are strictly positive with respect to Haar. The corresponding
plaquette has normalized trace less than 1 almost surely, so its expectation is less
than 1. Uniqueness of a Wilson Gibbs state cannot identify a limit that
retains this pinned plaquette with that state.

Correction: **“Move the observation region to cell interiors whose distance
from the frozen skeleton tends to infinity. If translated states have a
uniform local-observable clustering bound, their weak limits inherit it.
Every fixed local specification is eventually the unconstrained Wilson
specification, so those limits are Wilson Gibbs states. Uniqueness, if
proved, identifies the limit. The uniform bulk estimate and uniqueness
remain unproved; no weaker sufficient input has been established.”**

This is the valid scoped reason to reject V3 as a delivered reduction.
It is not an impossibility theorem for constrained approximations.

### §4.4 S0 / V4 — FAILS on the stated renaming argument

First unsupported line: L191, **“the irrelevant directions contract under
blocking, so the projective family is one orbit of the scale group.”**
Neither contraction nor uniqueness of a limit classifies all compatible
refinement families or reconstructs their finite-scale measures. No theorem
with those hypotheses and that conclusion is stated or proved. In
particular, the cited account cannot be used for this classification:
SA 6871 explicitly limits its uniqueness claim to fixed tori and named
comparison premises; SA 32172–32176 repeats the restriction.

Replacement: **“A freely chosen clustered coarse measure has not been shown
to admit an exact asymptotically free refinement with the required continuum
identification. If the family is required to be a given Yang–Mills RG orbit,
putting its coarse member in a cluster-expansion domain is an additional
infrared-entry condition. Allowing another regularization leaves a
construction and identification problem; no equivalence to EXIT or Theorem
CR is proved here.”** V4 has not delivered a route, but the general
renaming verdict is not established.

### §4.5 / V5 — HOLDS AFTER CORRECTION

Pin(2) is a valid **GUIDE-grade candidate test**, with the even-observable
Gaussian diagnosis in §3. It is not an established gapless comparison model
at finite coupling. Replace L294/B3's assertion that K6 “stays in force on
the authority of Pin(2)” by: **“Pin(2) motivates a provisional control: a
mechanism using only noncommutativity and the existence of a Lie algebra
should explain how it distinguishes this candidate abelian infrared model.
For the proposed commutator mechanism, the Lie algebra of Pin(2) supplies no
noncommuting infinitesimal rotations.”** Even a proved gapless Pin(2) model
would require a gap argument to distinguish it somehow; it would not prove
that every possible argument must use this particular commutator identity.

## 6. Orland: paper-level check of step 7

### Attribution — HOLDS AFTER CORRECTION

Open copies were downloaded once each, into separate new directories. PDF
page numbers below count the title page. The 2007 and 2008 papers were read
through their bodies and conclusions. The 2006 body, §§1–8, was read;
its S-matrix/form-factor appendix was not checked or imported. The relevant
2007 action and regime, and the 2008 chiral Hamiltonian and perturbations,
were also inspected on rendered PDF pages. `pdftotext` was unavailable;
PyMuPDF text extraction and page rendering supplied the reads. This was
source inspection, not a computer-assisted proof.

- [Peter Orland, 2006, hep-th/0607013v6](https://arxiv.org/pdf/hep-th/0607013v6),
  PDF pp. 7–10, (3.2)–(3.5), (4.2): setting `g'_0=0` gives a sum of chiral
  Hamiltonians, with a residual Gauss constraint on physical states. This is
  a **2+1-dimensional** antecedent, not the exact four-dimensional classical
  measure of FACE-LIM. PDF pp. 4 and 16–19 explicitly retain weak-anisotropy
  assumptions, discuss crossover, and leave the gauge-theory mass gap open.
  Scratch: `/tmp/sa-gap-wall-orland.t2G6BL`.
- [Peter Orland, 2007, 0704.0940v2](https://arxiv.org/pdf/0704.0940v2),
  PDF pp. 3–5, (1.1)–(1.6): the same 2+1-dimensional setting requires
  `(g'_0)^2 << g_0^{-1} exp(-4pi/(N g_0^2))`. The leading low-lying singlet
  mass is near `2m_1`; PDF pp. 7–9 obtain corrections with a nonrelativistic
  two-body approximation, S-matrix matching and WKB, while omitting other
  corrections. PDF pp. 9–10 propose, rather than establish, an anisotropic
  RG connection to the isotropic theory. This is not a uniform spectral-gap
  theorem or a four-dimensional proof of BR-L'.
  Scratch: `/tmp/sa-gap-wall-orland.41XG9A`.
- [Peter Orland, 2008, 0801.0389v2](https://arxiv.org/pdf/0801.0389v2),
  PDF pp. 1–6, (1.1), (2.2), (2.9), (2.12)–(2.13), (3.1)–(3.5): this is
  the relevant **3+1-dimensional** ancestor. `H=H_0+H'+H''`; `H_0` is a sum
  of chiral models on transverse links, `H'` is a longitudinal Coulomb
  interaction, and `H''` is the transverse plaquette term. The limit
  `g'_0=0`, `g''_0=infinity` removes both interactions, retaining residual
  Gauss invariance. The paper takes continuous time and then a longitudinal
  continuum approximation; it does not prove the finite free-box Wilson
  weak limit or all-beta O(4) mixing used here. PDF pp. 6–8 impose (4.1)
  and leave extension to small `g''_0` unresolved. On p. 2, Orland credits
  earlier work by H. and E. Verlinde and by I. Ya. Aref'eva for the chiral
  limit; references also credit the transverse-lattice work of Bardeen,
  Pearson and Rabinovici. “The anchor is his” must not imply sole priority.
  Scratch: `/tmp/sa-gap-wall-orland.DYMOST`.

Replace step 7's conclusion by: **“The decoupled-chiral structure and weak
interlayer perturbation are established antecedents of this proposal in
Orland's anisotropic Hamiltonian work, particularly his 2008 four-dimensional
paper, which credits earlier transverse-lattice and rescaling work. FACE-LIM
and ANCH give the finite classical-lattice identity checked here. The exact
region R, an all-coupling anchor gap, and a controlled isotropic bridge are
not theorems supplied by those papers. The 2007 glueball calculation is a
2+1-dimensional perturbative analogy, not a proof of four-dimensional
BR-L'.”**

This also corrects the claim that V2's **specific region** is already
Orland's. The resemblance is structural; equality of regimes with the
normalizations and `xi_2^2` bounds in row 1053 has not been demonstrated.

## 7. Source record and disposition

All citations to `L...` above refer to `gap-wall-vectors-max.md` at the source
pin. Its SHA-256 is
`eabc47225a2545f16f77231402826e2468c08d0ac61e138e9b2f378e6ae6a238`.
Its complete 387 lines were read, with the B1 source ranges:
`gap-global-reform-max.md` L491–530 and L1033–1043;
`gap-invent-selective-max.md` L52–63;
`prior/gap-2don-proofs-read-opus.md` L113–176.
The last file is a reading record, not a checked proof of the OpenAI text.
The check does not promote its imported 2D theorems.

The Sussman–Alpoge outline index, neighbouring rows and obligations supplied
the scope checks: chunk 06, rows for SA 6844–6879; chunk 29, rows for
SA 31871–31882, 32120–32198 and 32293–32319; and chunk 01's gauge and
normalization rows. Source reads were SA 275–323, 6836–6854, 6868–6873,
31871–31882, 32165–32176 and 32291–32324. In particular their text says
“does not assert uniqueness of the infinite-volume limit” (SA 6871).
Their scalar polynomial-clustering example separates reconstruction from
a spectral gap (SA 31871–31882). Neither result is new here.

The exact-object index search (`FACE-LIM`, `FACE-MW`, `FACE-TW`,
`principal.chiral`, `Pin(2)`, `Mermin`, `Orland`, `flat.plane`) found no
matches in the 30 outline chunk files, obligations, or the CA-I 4.12–4.19
index. This is a search result, not an absence theorem about the whole
account. A broader search for chiral models and anisotropic/flux twists
also located SA 5051–5062 and 7071–7075, read after chunk 04 L128–133 and
chunk 07 L18–22. The former is an independent-Gaussian example about
anisotropic marginal terms. The latter credits Balaban's earlier chiral
block averages. Neither is the face-model reduction or a flux-frame
exclusion. CA-I was fetched as requested but no CA-I passage was needed as a
proof premise; its stage-admission index concerns different objects.
No Balaban paper, the parallel row 1062 check, or a historical automation
protocol was read or executed.

The finite algebra, weak-convergence argument, capacity bound and kernel
iteration above are written mathematical checks. No numerical experiment,
interval certificate, enumeration, Lean run or general test suite was used.
Perturbative and Gaussian comparisons retain their declared scope. No
source, registry, FINISH row, audit file or ledger was changed.

Final checkpoint: B1 is covered at the requested item level. FACE-LIM,
ANCH and EVEN hold; ANCH-W, RIG, FACE-MW and ITER hold with the stated
scope/proof corrections. The Gaussian checks need their limit and coupling
conditions. The one-loop constants match, but V2's scale identification is
unproved. V1 remains incomplete at BR-L and FACE-SG. V2/V4 are not proved
renamings; V3 requires a corrected limit and an unsupplied uniform bulk
estimate. No exclusion of two-dimensional framed flux twists was proved.
Pin(2) remains GUIDE. Orland supplies ancestry, not the missing bridge.
The next decision belongs to the lead: correct these claims before using
B3; B1 supplies no proof of FACE-TW or authorization to start B2.

Delivery: the report is local and uncommitted on
`check/gap-wall-vectors-astra-1061`; HEAD remains the requested source pin.
No remote write was made.

RESULT: B1 completed as a research check: FACE-LIM, ANCH and EVEN HOLDS; ANCH-W, RIG, FACE-MW (24, 12 pi^2, 48 pi^2), ITER, scoped Gaussian/engineering checks, Orland attribution and V3/V5 verdicts HOLDS AFTER CORRECTION; V1's endpoint-containment verdict HOLDS; the flux-dimension exclusion, unconditional V2 scale-matching argument, and V2/V4 renaming verdicts FAILS at the lines identified; FACE-TW, FACE-SG, BR-L' and the mass gap remain open, with no status granted.
