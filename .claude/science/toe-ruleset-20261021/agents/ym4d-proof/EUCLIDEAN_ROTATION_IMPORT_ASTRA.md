# A conditional reflection-to-rotation bridge and its actual-model interfaces

Date: 2026-10-29. Claim type: bounded theorem / literature bridge.
Status: conditional support; full four-dimensional existence and the physical
continuum mass gap remain **OPEN**. This is an author construction with
finite exact diagnostics, awaiting independent review. It assigns no audit
status. The root owns the campaign, git, PR #10114 and shared summaries.

The useful result is a reusable spectral comparison and an explicit diagonal
Wilson factorization on reflection-symmetric free boxes. The proposed full
rotation import has two additional requirements that the lane has not
produced: diagonal positivity in its **same** limiting state, and an ordinary
random field with the specific global exponential estimate. Neither the
current scalar partial hierarchy nor local complex-source estimates supply
those requirements. An exact Gaussian counterexample below disproves the
general replacement of the exponential estimate by arbitrary Schwartz
moment bounds, even when source functionals are entire.

## 1. Frozen sources, scope and prior work

The primary candidate is [RPM1, TeX source](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310/RP%20O(d)%20trick%20(RP1)/RPM1.tex),
commit `1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310`, Git blob
`86d31273743ea0b3dc2b99090058ce3b930fba5a`. Its scientific body, source lines
702–2858, was read in full, including the appended contact and weight-three
counterexamples. The paired PDF has 30 pages, SHA-256
`1167b22c8a8fd957f66193a5d56c32c3683305d618a6dde5949b44731e8f6872`.
The 33-page [expanded outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310/RP%20O(d)%20trick%20(RP1)/RP1O1.pdf)
was read only for its introduction and final scalar application; it is not a
substitute for the full manuscript. That supplement identifies itself as a
conditional application retained from an older edition and omitted from the
current RPM1.

Both the [main README](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310/README.md)
(blob `24778ac2d5498b4cab2568447b58ae4e2b9c6612`) and the
[RP README](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/1b92bd0347e3b8763cd8ecc1f96dc3c2a92dd310/RP%20O(d)%20trick%20(RP1)/README.md)
(blob `1578fbcec3cd49a25c5163ab83c6eb33414250da`) were read. They explicitly
qualify correctness as tentative and describe substantial LLM authorship.
The RP README says its human-written manuscript has not yet been added.
The main README describes QED3 and YM3 work and an unpublished long YM4
argument. This note verifies no public YM4 existence or mass-gap claim and
makes no comparison of achievement with OpenAI. A theorem asserted in that
repository is not made established by its title, provenance or this read.

Primary literature inspected for the specific interfaces:

- [Sokal, 1982](https://www.numdam.org/article/AIHPA_1982__37_4_317_0.pdf),
  pp. 327–330 and 374–375: scalar infinite-volume construction, simultaneous
  mirror positivity and the proposed spectral route. The p. 329 Remark uses
  Griffiths inequalities to identify the limit across differently shaped
  boxes. This is precisely a producer that cannot be transferred to Wilson
  gauge fields by analogy. The later spectral discussion is a proposal, not
  the arbitrary-vector theorem proved in RPM1.
- [Jaffe–Jäkel–Martinez, arXiv:1302.5935v1](https://arxiv.org/abs/1302.5935v1),
  §VI, pp. 25–26: Proposition VI.1 and its Feynman–Kac comparison establish a
  spectrum condition in the specified scalar cylinder model. Its
  Hamiltonians, ground-state inputs and complex-field formula are not supplied
  for this Yang–Mills lane. It is primary precedent, not an imported YM bound.

RPM1 attributes parts of its method to Streater and Glaser and provides its
own proofs. Their original articles were not independently read in this
unit; no separate verification of those attributions is claimed. The
candidate manuscript is the actual source of the argument reconstructed
below. Research PDFs and complete extracted texts are confined to
`/tmp/euclidean_rotation_import_20261029/`; portable source pins and read
coverage are in the [source manifest](checks/euclidean_rotation_import_sources.json).

Methodology was read at root's fetched main revision
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`, including physics-loop,
review-loop, SCIENCE_WORKFLOW, premise classification and the negative-claim
gate. The minimal axioms and approved kinetic-isotropy source were inspected.
Kinetic-form isotropy is an approved structural premise; it does not supply
continuous rotations or the estimates below. The mathematical Wilson model
and the conditional probability laws here are explicit model data, not new
physical axioms or primitives.

A statement-based search at that revision for both word orders of diagonal
reflection positivity, RPM1 and spectral cones found no matching landed
bridge in the searched `docs/*.md` and lane notes. Unrelated single-particle
spectral-cone and Hodge-overlap hits do not prove this field-theoretic result.
The closest local material is [PROOF](PROOF.md), setting S4'/S4'', Decision 4,
L9a/L9a' and the open L9b; [OSLEAF55](OSLEAF55.md), D2–D8 and CLOSURE-sep;
[its review](CODEX_REVIEW_OSLEAF.md), findings F4–F9 and F12;
[the sphere review](CODEX_REVIEW_SPHERE2.md), its conditional Ward/tower
conclusions; [the actual source return](SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md),
(H1)–(H9) and its source-domain statements; and
[the expanded physical target](MASS_GAP_TARGET.md). Source hashes and exact
read limits are recorded rather than treating the older PROOF ledger as
current completion authority.

During this work the root integrated the separate coordinate-RP packet at
immutable commit `93a9d1a141849dfac1d8f1a585a17e43211ef271`.
[HRP](HRP.md), §§3–4 and 6, and the full [source review](REVIEW_HRP.md) were
read at that commit. They give the coordinate torus proof, exact full-chain
zero-source marginal and the ordinary/restricted-domain distinction without
requiring a new coordinate-RP derivation here. The source review's HOLD
concerns execution/certificate inspection and exact consumer wording; the
root reports later execution, whose certificates this unit has not reviewed.
Those are separate from this note's diagonal mechanism. Neither new file
supplies diagonal positivity or a global source estimate, and neither was
edited in this unit.

## 2. What the candidate theorem actually requires

Let F be a real random tempered distribution with values in a specified
finite-dimensional orthogonal O(d) representation. For every real Schwartz
test chi, one **fixed** C must satisfy

    E exp F(chi) <= exp[C (||chi||_1 + ||chi||_2^2)].          (R-exp)

The same law must be translation invariant and its characteristic functional
must be reflection positive across every coordinate plane and every plane
x_j +/- x_k=0. Planar tensor weights must have absolute value at most two.
RPM1 asserts O(d) covariance of all moments on pairwise disjoint supports.
It permits noncovariant contact terms; it does not assert invariance of the
whole probability measure or itself supply OS reconstruction, a Yang–Mills
identification, clustering or a mass gap.

The source proof was reconstructed through these load-bearing stages:

| Source lines | Mechanism and premise actually used |
|---|---|
| 2755–2858; 1360–1428 | R-exp gives finite Lp moments, dense cylinder polynomials and an ordinary ambient L2 law. Characteristic RP plus translations gives reflection invariance. The reflected quotient and dyadic translation argument give a contraction semigroup. |
| 1431–1540 | Evaluate one translated pairing in coordinate and diagonal OS spaces; compare their spectral measures using a family of Laplace transforms. This yields H>=|P| in the chosen plane. Section 5 below gives the argument without R-exp, under a separate common-law hypothesis. |
| 1543–1740 | Jointly holomorphic reflection kernels preserve positivity at conjugate parameters. All finite derivative Gram matrices are positive at the initial point; Taylor congruences propagate this to a common neighborhood, and closedness plus connectedness finishes the continuation. |
| 1802–1893 | Repeated reflection duplicates arbitrary slab sources. Each duplication doubles the L1 norm and the squared L2 norm; repeated square roots balance that growth. R-exp gives a bounded exponential insertion in the OS quotient, and Cauchy's estimate gives the linear field insertion. |
| 1895–2084 | Average planar mollified insertions, use L2 duality and holomorphic mean-value bounds, then identify their weak limits by smeared operator-norm convergence. The resulting planar insertion loses one inverse separation power, with transverse variables still smeared. Products use recovered bounded insertions, not products of unexplained weak limits. |
| 2086–2281 | Ordered kernel domains glue on real open overlaps. Narrow configurations admit an entire angular continuation: the scalar separation loss contributes N to the growth exponent, tensor weights contribute at most 2N. Thus only angular frequencies of magnitude <=3N remain. |
| 2284–2547 | Admissible support tuples make the mixed pairing and both squared norms narrow. Continued positivity gives 2 M_(a+b)<=M_(2a)+M_(2b). Rotating the **law** by pi/4 preserves the four mirror hypotheses and forces M_(2a) to be divisible by eight. This uses positivity of a leading diagonal coefficient, not a sign for every mixed coefficient. |
| 2549–2609; 1029–1245 | The even increments are nondecreasing multiples of eight. The bound M_(2n)<=6n forces them all to vanish. Analytic translation of separated groups removes the narrow-configuration restriction and projected coincidences. Compact truncation handles general disjoint Schwartz tests. |

This reconstruction found no concrete contradiction in those stages under
the printed strong premises. It is an author reading, not independent
verification of the full candidate theorem. Its decisive analytic step is
the slab insertion estimate in the **OS quotient norm**. An ordinary moment
bound alone gives no such operator estimate. Local source analyticity gives
neither the global replicated-source bound nor the specific one-power
localization loss. The source's finite Fourier-degree argument is sensitive
to that loss; its own weight-three counterexample sits at the failed
threshold M_N<=4N.

## 3. The actual observable and source dictionary

The present OS route uses the scalar clover energy of ROTDEF §2.2,

    e_a(x) = (4 a^4)^(-1) sum_(mu!=nu) sum_(p in clover_mu,nu(x)) s(U_p),
    s(U)=1-Re tr(U)/N,
    ehat_a(x)=Z(a)^(-1)[e_a(x)-E e_a(x)].                    (R-field)

It is an H(4) scalar with proposed continuum identification proportional to
tr F². It is **not** the Lie-algebra-valued curvature tensor F_mu,nu, which is
not itself gauge invariant, and not a constructed full family of
gauge-invariant local fields. The scalar's planar weight zero matches one
representation requirement; this does not establish the other premises.

OSLEAF D2–D7 define S_n only on the Schwartz functions flat on every
coincidence diagonal. Products are partial: f tensor f and e(f)^2 generally
do not lie in the domain. Its positive form is on ordered positive-time
tests. A Borel law on all ordinary smeared variables F(f), its characteristic
functional, the ordinary L2 norm, and its repeated-field moments therefore
cannot be read off that hierarchy. Even complete O(4) covariance of this
scalar hierarchy would leave the full observable scope in MASS_GAP_TARGET
unproved.

The source-radius mismatch is explicit. Write the uncentered smeared clover
as O_a(f)=sum_p c_p(f)s(U_p), where

    c_p(f)=(1/2) sum_(x a corner of p) f(x),
    |c_p(f)|<=2||f||_infinity.                              (R-coeff)

The actual source return uses exp[-u sum_p (1+epsilon_p)s(U_p)], with the
normalized kernels held at their real zero-source coupling. Inserting
exp[t O_a(f)] means epsilon_p=-t c_p(f)/u. A domain
|epsilon_p|<=lambda/u yields only
|t|<=lambda/(2||f||_infinity). Centering adds a deterministic factor;
normalization replaces c_p by c_p/Z(a). Neither changes a local-disc bound
into the all-real-source estimate R-exp. Original plaquette labels,
all-coarse-field integration, denominator and failure/sea terms still matter.

Also, the elementary bound 0<=e_a<=24 a^(-4) gives only a deterministic
Laplace bound with constant proportional to a^(-4)/Z(a). The number 24 is a
universal upper bound, not the sharp SU(3) maximum; the existing review
corrects the latter to 18. No cutoff-independent C in R-exp follows. The
review's torus variance lower bound, on its stated trajectory and in its
corrected coupling convention, is another obstruction to a uniform ordinary
unnormalized second moment. Its extra separated-covariance hypotheses are
not silently assumed here.

Two exact implications fail:

1. For a standard normal G, X=G²-1 has every moment and a Laplace transform
   analytic near zero, but E exp(tX)=exp(-t)/sqrt(1-2t) for t<1/2 and is
   infinite for t>=1/2. The random constant scalar distribution
   F(f)=X integral f is translation and reflection invariant and reflection
   positive. Local analyticity even with all mirror positivity does not
   imply R-exp. This example is rotationally invariant; it tests only that
   implication.
2. More decisively, let phi be the massive scalar Gaussian free field on R^4
   with m=1, and define the real scalar random tempered distribution
   F=D phi, D=sum_(j=0)^3 partial_j^4. Its Gaussian source functional is
   entire on every finite-dimensional source space and all moments obey
   continuous Schwartz bounds: E exp F(f)<=exp(||Df||_2²/2), hence the
   Gaussian moments are bounded by products of a fixed derivative seminorm
   times the usual (constant sqrt(n))^n factor. D preserves supports and commutes with
   translations and every signed coordinate permutation, including all
   required mirrors. Since D theta=theta D, Gaussian reflection positivity
   transfers from phi to F on every required half-space. For completeness,
   the free-field covariance reflection form is the nonnegative integral
   of |integral_(t>0) exp(-omega_p t) fhat(t,p) dt|²/(2 omega_p),
   omega_p=sqrt(|p|²+1); applying D to the test retains its half-space support.
   The Gaussian characteristic-functional form follows by expanding the
   exponential of that positive cross-covariance kernel.

   Yet F is not rotation covariant away from coincidences. Its covariance
   multiplier is Q(p)²/(p²+1), Q(p)=sum_j p_j^4. Rotate the first plane with
   cosine 3/5 and sine 4/5. At the complex zero p=(i,0,0,0) of p²+1,

       Q(Rp)²-Q(p)² = (337/625)²-1 = -277056/390625 != 0.

   Thus the difference multiplier is not a polynomial. A distribution
   supported only at the origin has polynomial Fourier transform; hence
   this rotational defect has nonzero support away from the origin and is
   detected by suitable disjoint smooth tests. Its covariance is unbounded
   on L2 (the axial multiplier is r^8/(r²+1)), so it does not satisfy R-exp.
   This is an exact counterexample to the **weakened abstract theorem** with
   arbitrary Schwartz bounds or mere source analyticity. It is not a
   Yang–Mills counterexample. Replacing D by the rotationally invariant
   Laplacian squared makes the tested defect exactly zero, a useful control.

## 4. Diagonal Wilson positivity: a proved local mechanism, precise boundaries

**Free-box factorization.** Let Lambda be a finite site set in Z^d invariant
under reflection theta in x_j+s x_k=0, s=+1 or -1, with all included bonds
and plaquettes reflected into included ones. Take the Wilson measure with
free boundaries and nonnegative, reflection-matched plaquette coefficients.
Then it is reflection positive on bounded functions of links whose endpoints
are in the closed positive half-space.

Proof. Put h(x)=x_j+s x_k. Each edge changes h by zero or one in absolute
value, so it cannot join a strictly positive vertex directly to a strictly
negative vertex. Shared plane links have both endpoints fixed by theta.
An elementary plaquette that visits both strict halves necessarily lies in
the j,k plane and has vertex heights {-1,0,0,1}. Its two height-zero
vertices are opposite and fixed pointwise. The positive two-edge path P
between them is reflected to the negative two-edge path Q with the same
endpoints. The loop holonomy is P Q^dagger, up to cyclic starting point or
orientation; its real trace is unchanged by those choices. Therefore

    Re tr(P Q^dagger)
      = (1/2) sum_ab [P_ab conjugate(Q_ab)+conjugate(P_ab) Q_ab].

Each crossing exponential expands absolutely into terms
c_alpha G_alpha Theta(G_alpha), c_alpha>=0, where
Theta(G)(U)=conjugate(G(theta U)). Noncrossing plaquettes contribute a
positive-half factor and its reflection; plane plaquettes contribute a
positive common weight. Conditional on the shared plane links, product Haar
integration turns the RP form into a sum of absolute squares. Integrating
the plane links preserves nonnegativity. No gauge fixing or field expansion
is involved, and the proof works for SU(N), N>=2. The finite enumerator
checks this actual geometry, not just a count of lattice symmetries.

**Clover support.** A clover at x has diagonal height radius at most 2a.
For a compact source supported at h(x)>delta>0, its clovers lie on the
closed positive side once 2a<=delta. The scalar clover map is covariant
under all signed permutations. Thus on the free-box measures above its
ordinary characteristic RP matrices, and its separated polynomial RP
forms, have exact positive representatives. Passing such matrices to one
common characteristic-functional limit preserves positivity. Passing
polynomial forms instead requires convergence of the actual products on
their domains. Neither limit is supplied by the finite geometry.

**Actual blocking.** For the centered odd L blocks in PROOF S4', let
r=(L-1)/2 in fine units. The minimum diagonal height inside a block centered
at c is h(c)-(L-1). A strictly positive coarse center has h(c)>=L, so its
entire block stays at height >=1. Every actual order-averaged contour for a
coarse link stays inside its two endpoint blocks. Coarse links whose two
centers are strictly positive therefore have positive fine footprints.
Boundary-center blocks fail that assertion: at c=0 the contour point
y=(-r,r,0,0) has h(y)=-(L-1) for h=x_0-x_1 and occurs in the prescribed
path family for a tangential coarse link. The valid pullback algebra must
exclude these footprints or impose a buffer. The all-orders average and
the odd branch rule provide the stated signed-permutation covariance, but
covariance alone supplies no locality or positivity.

For the normalized product soft kernel K(V,U)=product_c k_c(V_c;Mbar_c(U)),
all V integrations give one for fixed U. Fine-observable expectations in
the integrated joint measure consequently equal their Wilson expectations
exactly. A stronger useful restricted statement is also valid: if f(V)
depends only on coarse links with wholly positive fine footprints, its
reflected partner uses disjoint coarse variables; integrating those
variables yields (Tf)(U) Theta(Tf)(U). The other normalized link kernels
integrate to one. Reflection covariance and fine-measure RP then give
coarse RP on that restricted algebra. Shared plane variables or crossing
footprints require a separate factorization; this argument does not include
them. Conditioning on an arbitrary fixed V gives the distinct density
exp(-S(U))K(V,U)/Z(V). Covariance relates V to theta V and is not invariance
at fixed V. The source-history return is explicitly at fixed V; its positive
real integrals do not by themselves prove the needed reflection inequalities.

**Periodic regulator limitation.** The actual lane uses a standard
hypercubic torus, not the preceding free box. The swap theta(t,x)=(x,t)
has a nonseparating diagonal fixed set on that torus. On the side-four
two-dimensional section, all 12 nonfixed sites are connected after deleting
the four diagonal sites. The wrapping plaquette

    (3,0) -> (0,0) -> (0,1) -> (3,1) -> (3,0)

visits both sign regions t-x>0 and t-x<0 in the displayed representatives,
has only one fixed vertex, and is not reflection-fixed as a loop. Thus the
two-fixed-vertex proof cannot simply be applied to all periodic plaquettes.
The same local section embeds in the actual four-dimensional geometry.

This is a failure of that proof transfer, not a theorem that every Wilson
torus diagonal-RP inequality fails. To show why symmetry is insufficient,
the separate massive scalar Gaussian measure on the periodic 4x4 square,
with covariance (1-Delta_lat)^(-1), has the reflected covariance matrix for
positive sites (1,0),(3,1)

    [[2/45, 5/63], [5/63, 8/315]],   determinant=-19/3675.

Direct rational inversion and an independent discrete Fourier sum agree.
It is translation invariant, square symmetric and coordinate RP, yet this
diagonal form is not positive. No gauge-model verdict follows from this
control. A same-state thermodynamic or boundary comparison is an actual
missing producer; changing to free boxes or a diagonal torus requires it.
Sokal's scalar construction supplies its own such comparison, as discussed
in section 1. Naive rotational averaging supplies no replacement: a rotated
state need not be RP for the fixed test plane.

## 5. A bounded-observable spectral comparison that does not use R-exp

**Conditional spectral-cone lemma.** Suppose one ordinary probability law
has a local observable net on R^d. Geometric translations and coordinate
and diagonal reflections act covariantly on that net, preserve the law,
and satisfy the usual reflection–translation relations. Assume translations
act strongly continuously on its L2 space, and RP holds on the closed
positive-half L2 subspaces. Suppose bounded observables
with compact positive supports have dense images in each relevant OS
quotient. Then the coordinate time generator H and each tangential
translation generator P_j satisfy

    H>=|P_j|.                                               (R-cone)

The assumptions include existence of the ordinary common law and dense
local subspaces. They do not follow from the collision-flat hierarchy.
For an actual random tempered field, bounded local cylinder functions plus
continuity of the law give a natural domain to check these assumptions;
polynomial density and R-exp are unnecessary for this lemma.

Proof, adapted directly from RPM1's spectral comparison. Quotient norms
obey ||[A]||<=||A||_L2. Reflection and translation give
||[U_t A]||²=<[A],[U_(2t) A]>. Iterating Cauchy–Schwarz and using the
ordinary L2 bound proves contraction and preservation of null vectors.
Strong continuity yields commuting H>=0 and P, with
V(t,x)=exp(-tH+ixP). Construct the second quotient at t+x=0.

Translate a bounded compact-support A forward until its support lies in
t>|x|. Both A and J_Delta J_0 A then lie on the positive diagonal side.
The same expectation has two spectral representations, with rho a finite
positive measure and sigma a finite complex measure:

    E[(J_0 A) U_(t,x) A]
       = integral exp(-omega t+i p x) d rho
       = integral exp[-Omega(t+x)+i P(t-x)] d sigma.         (R-two)

Here rho is the coordinate spectral measure of [A]. Sigma is the diagonal
cross-spectral measure of [J_Delta J_0 A] and [A]; its total variation is
bounded by the product of their norms. Time in the diagonal space is
parameterized by v=t+x and tangent translation by u=t-x, so no unmentioned
Euclidean normalization factor enters.

Integrate R-two on v,u>0 against h(v) conjugate(h(u)). Fubini is valid
because h is integrable and the spectral measures are finite. It gives

    integral |Lh((omega-i p)/2)|² d rho
       <= ||sigma|| sup_(r>=0)|Lh(r)| sup_(r real)|Lh(i r)|. (R-Lap)

Take h(s)=s^(i gamma) exp(-epsilon s), epsilon>0. Its transform is a
nonzero constant times (1+z/epsilon)^(-1-i gamma). Cancel that constant.
On the real and imaginary axes the right side grows at most
exp(pi |gamma|/2). A positive rho-mass where
|arg(epsilon+(omega-i p)/2)|>pi/4 would make the left side grow strictly
faster for one sign of gamma. Localize to a bounded positive-mass subset
with a fixed angular margin to make this comparison rigorous. Consequently
|p|<=omega+2epsilon on the spectral support. Sending epsilon to zero
gives |p|<=omega. The preliminary forward translation multiplies rho by
exp(-2b omega)>0, so it does not change spectral null sets. Density of the
original compact observables makes the prohibited spectral projection zero
on the whole coordinate quotient. Repeat for each j. This proves R-cone.

In d=4 these coordinate conclusions alone give H>=max_j|P_j|, not the
full Euclidean norm of momentum. Continuous rotational covariance is the
additional target. Even the full relativistic cone would allow zero mass.
Neither this lemma nor RPM1 implies the common positive physical threshold
required by MASS_GAP_TARGET's dense-family reflected-correlation criterion.

## 6. What can be reused next, and what is still missing

| Proposed use | Exact producer still required |
|---|---|
| Reuse the diagonal Wilson square factorization | Match its boundary geometry to the actual periodic sequence or prove a same-state boundary/exhaustion comparison. Centered free-box positivity is established here only for those finite measures. |
| Reuse R-cone for bounded local observables | One common translation-invariant ordinary law with all coordinate/diagonal RP forms, strong continuity and the specified dense local domains. The spectral-measure comparison itself needs no global exponential bound. |
| Apply RPM1 to the physical clover scalar | A real random tempered field on all Schwartz tests, the exact R-exp with cutoff-independent constant on the same limiting state, and all mirror RP. The collision-flat OS hierarchy and fixed source discs do not establish these. |
| Use a uniformly bounded scalar variant | A field linear in its test source with a genuine deterministic bound gives E exp F(chi)<=exp(M||chi||_1), so R-exp follows. Merely taking bounded exponentials of unbounded smeared fields is nonlinear in chi and does not meet this field hypothesis. Rescaling/clipping e_a changes the observable and still requires nontriviality, locality, common-law convergence and matching to physical tr F². |
| Stay on the collision-flat hierarchy | Derive a different analytic-positive kernel theorem with quantitative OS-quotient insertion bounds compatible with that partial domain. Arbitrary Schwartz bounds are insufficient by the derivative-Gaussian counterexample. No such upgraded theorem is asserted here. |
| Finish the full Yang–Mills target | Supply the complete gauge-invariant observable family, same-trajectory regularity/covariance/positivity, nontrivial Yang–Mills identification and the independent uniform infrared estimate. A one-scalar rotation result closes none of those automatically. |

The sphere route remains a separate approach. Its reviewed Ward identities
and positive conditional-mean towers do not identify the torus law with a
law satisfying RPM1; all-product matching, contact control and seam
transparency remain explicitly open there. Nothing in this unit repairs or
withdraws the sphere source files.

The next concrete decision is whether a same-state diagonal-RP producer can
be established on the existing periodic continuum sequence. If yes, the
spectral comparison can be applied without first solving R-exp. If not,
the free-box mechanism remains available only with an explicit regulator
comparison. The full rotation import should not be used downstream until
its stronger random-field and insertion hypotheses are actually produced.

## 7. Diagnostics, failures and independent-check boundary

[Pre-stated criteria](checks/euclidean_rotation_import_criteria.md) preceded
the script execution. The torus and derivative-Gaussian discriminators were
added before those calculations, after the full source proof was read;
that sequencing is disclosed. The [runner](checks/euclidean_rotation_import_exact.py)
checks 45,000 four-dimensional plaquette/plane pairs, including 1,350
straddlers, the noncommuting SU(2) path identity, actual centered-block and
clover support radii, periodic diagonal topology, an exact Gaussian torus
Gram witness and the noncontact Gaussian derivative defect. Wrong path
orientation and negative crossing coefficient controls distinguish the
Wilson factorization. Rotationally invariant derivative data give zero
defect. These are discriminating finite/exact checks, not numerical proof
of the candidate source theorem or of continuum Yang–Mills.

The first execution succeeded and is retained as
[attempt 01](checks/euclidean_rotation_import_attempt01.receipt.json).
The second execution adds an independent Fourier calculation of the Gaussian
torus covariance, agreeing with direct matrix inversion; it is bound by
[attempt 02](checks/euclidean_rotation_import_attempt02.receipt.json).
Those two runs printed the analytic negative-coefficient witness but did
not evaluate its Gram matrix. Author inspection caught that execution
coverage gap. [Attempt 03](checks/euclidean_rotation_import_attempt03.receipt.json)
executes the exact matrix at coefficient -log(2)/2 and checks that the
quadratic form on (1,-1) is -3. The old source versions and output receipts
are preserved, and the criterion was not relaxed. Block computations
enumerate the full block envelopes and the crossing member's endpoint;
whole-contour confinement is the geometric proof in section 4, not a claim
that the script enumerates every path ordering.
The source-download attempt using Python's certificate store failed with an
SSL certificate verification error; the non-escalated curl retrieval
succeeded. Both download records are preserved in the source manifest.
There was no failed mathematical run silently replaced. This author's
alternative calculations are not a fresh reviewer; independent review of
the final frozen unit remains pending.

## 8. No-Go Discipline Gate: a partial narrowing, not a global exclusion

**N1 — actual routes.** Direct RPM1 import, a bounded-observable spectral
comparison, a genuinely bounded scalar family, and a theorem on the partial
hierarchy are distinct approaches examined above. The first remains
unmatched, the second is proved conditionally, and the latter two have
unproved physical/domain producers. These are not five routes ruled out.
No N1 packet PASS or exhaustive no-go is claimed. The disposition is
**partial-narrowing**; the exact counterexamples disprove only the stated
logical weakenings. The root may preserve this reusable unit without
advertising a global route exclusion.

**N2 — conditions and dependence.** Let P denote the common ordinary law,
G its global R-exp, and D all mirror RP in that law. R-exp is a condition on
P, not an independent probability-construction proof. The characteristic
RP limit requires P; the conditional cone uses P and D but not G. P+D does
not imply G (the Gaussian-square example), while P+G need not imply D:
the stationary scalar Gaussian covariance exp(-|x-y|²) has a bounded
Fourier density, hence R-exp, but its reflected two-time covariance at
times 1,2 has determinant exp(-20)-exp(-18)<0. Small smooth supported
approximations of those point tests retain the negative determinant.
No further pairwise independence
claim or independent-wall count is made. Existence of the physical law is
stronger than having one finite-cutoff law. Full local-field identification
and mass-gap obligations are consumers, not duplicate analytic conditions.

**N3 — hidden-condition scan.** The probability law, strong continuity,
dense compact local domains, nonnegative Wilson coefficient, reflection-
matched free boundary, support buffer, normalized product kernels and
source convention are explicit. The scalar free field is a mathematical
counterexample model, not a supplied Yang–Mills state. The approved
kinetic-isotropy primitive is classified in section 1 and supplies none of
these downstream dynamical estimates. No result is inferred from a
background, registered status or unspecified canonical choice.

**N4 — exact residual matching.** OSLEAF's partial-product exclusion is
used only against an ordinary probability-law import. Its variance finding
is qualified by its actual trajectory and hypotheses. The periodic
plaquette witness attacks the free-box proof transfer; the Gaussian torus
witness attacks a symmetry-only inference; the derivative-Gaussian model
attacks replacing R-exp by Schwartz bounds/entire source analyticity.
None is evidence against all Euclidean-invariance or Yang–Mills routes.

**N5 — resolution limits.** Per-element nonabelian path factors, per-site
clover buffers, per-mode rational covariance defects, per-block footprints
and finite-lattice topology are checked in the retained output's resolution
certificate. Infinite-volume existence, physical spectra, uniform Ward
estimates and all-background source induction are not executed or proved
by those checks. The negative coefficient witness concerns a crossing
matrix kernel, not a complete gauge-invariant Wilson measure at beta<0.

**N6 — partial closure.** Reframing the existing target as one scalar
partial hierarchy is already explicit in OSLEAF; it does not create its
missing ordinary law. A bounded transformed field or different regulator
is a valid research choice if its physical identification is proved. No new
axiom is claimed necessary; the missing items are mathematical producers.

**N7 — strongest counter-route.** A reviewer can reasonably demand a
direct diagonal-RP limit theorem for the periodic clover hierarchy with
boundary errors controlled in the same source norms. That could supply
R-cone or support a tailored insertion theorem without an ordinary
unrenormalized composite law. The free-box square decomposition and the
actual strict-block support calculation make this a concrete live route;
RPM1's slab argument identifies the operator estimate to target. The
counterexamples above do not rule it out. Consequently a global no-go
would be unjustified.

**N8 — prior route comparison.** PROOF L9b already leaves universality and
observable-family matching open; OSLEAF's reviewed collision-flat
formulation partially avoids contact divergences, and the sphere route
attempts all-order covariance by Ward estimates. Those mechanisms have
not been shown closed by the present witnesses and remain live. The
statement-based main search and the actual-source reads in section 1 are
the search boundary; no claim of exhaustive repository or literature
coverage is made.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
artifact_role: literature_bridge
conditional_surface_status: common-law spectral-cone implication; free-box Wilson diagonal RP
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Reusable reflected spectral comparison and exact Wilson geometry; global source/probability and same-state limit producers remain unconstructed."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_four_dimensional_existence: OPEN
physical_continuum_mass_gap: OPEN
```
