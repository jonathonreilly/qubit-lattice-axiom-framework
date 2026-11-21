# Repo search

Writer: OpenAI Codex, GPT-6; row 1041 dispatch specifies gpt-6-astra/xhigh.
The runtime does not separately expose the precise subtype or effort.
Date: 2026-11-16.
Source checkout: `1a4ecc662f6554c62e77738a837953878a5875f2`.
Source SHA-256: `4197a3ced7e6f9f65ffb2e937e22e345f2a7367cc039276f3847f41233591a5b`.
Research check only; no audit status and no mass gap claimed.
Not covered: row 1040, GUIDE computations, typical-pin probability bounds,
whole-boundary tilings, or a new route. No numerical proof or Lean run.

The target-specific prior digest is absent. The lead's supplied search covers
main and PRs 10114, 10133, 10134 and 10141; no target-specific hit list is
attached. The older November 8 digest covers different RG targets. I checked
its boundary-admission near match in PR 10141's `out-pi.md`, main's
noncompact Maxwell score identity, and the same-lane FLOW, GR, MASS and
frame consumers. The first two concern different operators; the lane
sources supply the exact inputs and conventions. The lattice Uhlenbeck
statement controls a potential, not this frame. The SA account already
proves the axial product bound used by LAD/LIP-TREE; it is credited below.
No separate registry owner or completed duplicate of this check was found.

All requested checks are complete. The exact source ranges, corrections,
unresolved consumer obligations and final verdict are recorded below.

Downloads (each fetched once) are in
`/tmp/sa-gap-collapse-frame-check-astra.fMvhCV/`.
Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, receive credit for every input taken from their account.

## First hand tests

Line references below mean `gap-collapse-frame.md` at the pinned checkout.
These tests precede the detailed verdicts. No numerical run is used.

**Transported cube (L95–118).** Move the vectors to 000. Then
`u_0=u_1=u_2=a`, so the directly moved holonomy is conjugate to `h`:
`h(e)=exp(e A a) h exp(-e A a)`, where `A=lambda_000-lambda_110`.
Thus `t(h(e))=t(h)` exactly and `H_c=0`. GR leaves only the defect on
`l_2`; hence `Q=lambda_110^2 beta^2 Var(D_l2 n . Im(omega_l2 R_2))`.
Its variance is positive when the vector is nonzero: conditional on the
vertical links, the corresponding top link has strictly positive density
on SU(2), and its scalar product with a fixed nonzero vector is nonconstant.
This also proves the upper bound `4 beta^2 lambda_110^2 |s x a|^2`.

**NOLIP constant (L210–218).** Normalize Haar measure on `U_eps`.
Four sets each of measure greater than `3/4` have nonempty intersection,
since the sum of their complement measures is less than one. At that
intersection, telescoping the path twice gives
`|n-Ad(g)n| <= 2k(d+2eps)`, for `g=i,j,k`. The three squared left sides
sum to `8|n|^2=8`. Therefore
`d >= sqrt(8/3)/(2k)-2eps = sqrt(2/3)/k-2eps`.
The measure and covariance domain qualifications are recorded below.

**An explicit non-stationary TUNE pin (L355–372).** Use the allowed cube
strengths `beta=1`, `b_0=2`, and pin `omega_a=omega_b=omega_2=1`,
`omega_1=i`. Thus `h=i`, `t=0`, `s=i`. Put `A=2+kappa(0)`.
The interior partition function has `|d log G(cos(phi))/d phi|<=1`:
varying this one lower link differentiates only one side plaquette,
whose action derivative has magnitude at most beta. At `phi=pi/2`
this gives `|kappa(0)|<=1`, so `A>=1`; the pin is non-stationary.
Choose `u_0=j`, `w=k`, `cos(alpha)=4/5`, `sin(alpha)=3/5`, and
`n_100=4j/5+3k/5`, `n_010=4j/5-3k/5`.
For `lambda_110=lambda_000=lambda_010=0`, `lambda_100=1`, direct
quaternion multiplication gives `t'(0)=0`, `t''(0)=6/5`.
Consequently `H_c=-6A/5 <= -6/5`.
Only `X_a` enters the variance; `|D_a n|^2=2/5`, so
`Var(X_a)<=2/5` and `Q<=-4/5<0`.
The displayed all-theta condition also holds:
`tan(alpha/2) 2 beta^2=2/3 < (4/5) A`.
This tests a descent by acceleration, not a positive stiffness estimate.

## Source and overlap record

The November 8 digest concerns older RG obligations, not this check. Its
boundary-admission near match is PR 10141, `research/ym4d/library/out-pi.md`,
now L352–381, read through `git show` at
`a2f6a430e251aa47bc3eb4f67a1dca2a88530116`. It concerns a compressed classical
Hessian and leaves boundary admission additional. It supplies no frame-cost
identity here. Main's
`docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md`
L120–145, read at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`, concerns a
specified noncompact Maxwell law. Its score identity is a method analogue,
not a result for this compact pinned cell.

The closest actual inputs are Claude's `gap-boundary-q.md` GR, CUBE-Z,
CUBE, TP and MASS; its two earlier checks; `gap-short-step-max.md`
L217–231 (FLOW); `gap-aligned-frame.md` L200–242; `gap-sym-reg.md`
L34–43 and L334–374; and `gap-pinned-cell-gauge-max.md` L440–501.
These already contain the boundary convention, the extension freedom and
N1–N3. They are reused, not claimed as results of row 1038 or this check.
`open-registry.md` has no match for this check, boundary-q, NOLIP or
LIP-TREE. Row 1038 owns the source; row 1040 is the separate concurrent
check and was not opened. No duplicate target requiring a stop was found.

I read the relevant SA-index rows and neighbours before using the source:
chunk-07 (axial/comb and Landau gauges), chunk-02 (GL3), the corresponding
obligations, and CA-4.12-4.19 chunk-01 (monotone paths and axial gauge).
The outline's L7178–7202 defines these gauges; it does not give O2.
Its L2197–2243 proves the positive, factorially decaying Wilson character
coefficients used by CUBE-Z, with `u_d=exp(beta)c_l`, `d=2l+1`.
CA-I L43690–43865 proves the product-of-conjugated-plaquettes estimate
and finite-box axial bound in detail. **LAD and the geometric part of
LIP-TREE are already this method**, with coordinate order reversed.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, and Balaban for the axial-gauge method. This check verifies
the use and the SU(2) constant; it makes no novelty claim for that step.
Index hits at outline L11032–11048, L11460–11470 and L12795–12820 were
also read: they concern local Green estimates, flat row lifts and
covariant derivatives of potentials, not the present thermal Hessian.

Row 1039's reading record was read. `lattice-uhlenbeck.md` L7–23 states a
box-wide potential estimate under total curvature smallness. It does not
supply a covariant unit frame or O2. Its proof is not rechecked here.
The recalled Balaban/Uhlenbeck bibliography in source Step 2 is not
verified against the original papers in this check and supplies no premise.
No Balaban text was copied. The SA search is targeted, not a claim that
all 166711 lines contain no differently formulated result.

## 1. TG, LAD and LIP-TREE — HOLDS with the stated domain

TG L155–166 is exact. Gauge covariance follows from
`P_x -> g_x P_x g_o^-1`, provided the root axis is itself measurable and
covariant on its domain. Conjugating a vector by `h=t+s` gives
`|(1-Ad(h))a|^2=4(|s|^2-(s.a)^2)` for unit `a`.
This proves the exact defect formula, including central holonomies.
The tree-gauge pin curve is `H_l(e)=e^(-e lambda_y a) H_l e^(e lambda_y a)`;
its logarithm rotates by angle `-2e lambda_y`. There is no differentiation
of the axis rule when defining this boundary move.

LAD L170–175 is the cited finite product identity and norm inequality.
For the reversed-coordinate comb, a direction-2 edge needs `x_1`
plaquette swaps. A direction-3 edge needs `x_1+x_2`. Direction-1 edges
are tree edges. The swap plaquettes are two unit-width strips, with at
most `S_1+S_2` members, within that distance of the edge. Thus the source
lines L183–188 give `r=S_1+S_2` and `C_r=2 sqrt(2)` correctly:
`|U-1|^2=2(1-t)<=2(1-t^2)=2|s(U)|^2` when `t>=0`.

The domain qualification is essential. A root plaquette axis is undefined
when that plaquette is central. At a pure-gauge pin no equivariant unit
axis exists. Therefore L186/L230 mean the punctured domain where the
chosen root axis exists, with defect tending uniformly to zero on
approach to pure gauge. They do not define a frame on the pure-gauge orbit.
The radius `S_1+S_2` bounds the curvature stencil, not all reads of `n_x`:
its tree path can also traverse the whole third coordinate. This is not
uniform LOC or the same local rule at every site. The whole-boundary
construction and shared-face compatibility are not supplied by LIP-TREE.

## 2. NOLIP — HOLDS for equivariant local rules

The hand test above checks the coefficient exactly. For a reversed edge,
`|Ad(u^-1)m-m|<=2|u^-1-1|=2|u-1|`, so path orientation changes nothing.
For each plaquette, four-link telescoping gives `|s(U_p)|<4eps`.
A bound by at most R such terms would therefore give `d<=4CR eps`,
contradicting the positive limiting lower bound for fixed k, C and R.
Separated radius-r read sets on a face of adequate length give
`k<=2r+2`, as claimed. Translation invariance of the rule is not needed.

Write the domain premise explicitly at L197–200:
“Each local evaluation map is equivariant under simultaneous conjugation
of its read links, on its conjugation-invariant domain; O is measurable.”
A frame defined on a gauge-invariant domain has this usual meaning.
If covariance is instead asserted only when two *global pins in O* are
related by a gauge transformation, L213 is not justified: `rho_g` is a
partial conjugation, not a gauge transformation of all links. With that
weaker reading the proof needs the premise above. No regularity or
continuity is needed once local equivariance is specified.

This theorem excludes dense near-trivial families, not every open set
approaching the trivial pin. The thin-set remark L220–224 is plausible
locally for a fixed finite face: away from central plaquettes the axis
map has derivative bounded by a constant times `1/m`; perturbations of
size `c m^2` around a common-axis Abelian pin give defects `O(m)`.
This does not establish any lower bound on the density of that union,
or a typical-pin statement. No stronger exclusion is retained.

## 3. CUBE-H, the transported test and ONE

**CUBE-H L79–91: HOLDS.** Let `r=theta_2-theta_1` and expand
`Re(e^(e r u_0) e^(e theta_1 u_1) h e^(-e theta_2 u_2))`.
The first derivative is `-s.v`. The quadratic scalar part is `-t|v|^2`.
The ordered cross products are
`-theta_1^2 u_0 x d_1 + theta_2^2 u_0 x d_2
 + theta_1 theta_2 d_1 x d_2`, with coefficient `-2s` in `t''`.
Applying `F_t=-(b_0+kappa)` and `F_tt=-kappa'` gives L81.
This checks the order and signs independently of any finite difference.
The absent `n_110` and `lambda_000` are correct.

**Transported test L95–118: HOLDS.** The exact conclusions and strict
variance test were given above. Continuity of the covariance matrix at
the trivial pin, where it is scalar, gives the stated leading coefficient
`4(beta xbar-kappa)`. Its positivity follows from the nonconstant side
staple variance, not the GUIDE value. In L104–110, restore a factor
`lambda_110^2` in each displayed direct/force contribution, or explicitly
state `lambda_110=1`. This omission does not affect their cancellation.

**ONE L120–134: HOLDS AFTER CORRECTION of its headline and summaries.**
For a constant boundary lambda, the boundary does not move. The extension
is a product of fixed left rotations on the vertical links, so Haar
integration gives `Q=E[Psi^2]`, `E[Psi]=0`. Conditional on the vertical
links, the four side staples have full support SU(2)^4. A sum of four
linear scalar functions of those separately variable coordinates is constant
only if all four defect vectors vanish. This proves

`Q(d1)>0 if Dn is nonzero on a pinned edge;`
`Q(d lambda)<=0 for all lambda iff Dn=0 on all four pinned edges,`
`and in that exceptional case Q is identically zero.`

The phrase “never negative semidefinite” at L120 is false without that
exception. More seriously, this exception is realized by **every
noncentral cube pin** with the transported common holonomy axis. It is a
pin-measurable covariant rule on a full-measure domain, with collapsing
(in fact zero) defect. Thus the universal cube failures at L348–350,
L409–410 and L479 must retain the exception. Nonstationarity does not
remove it. O2 on the cube has this zero-gain solution.

## 4. LEAD — HOLDS AFTER CORRECTION of the remainder specification

L255–268 has the correct coefficients and signs. The statement is for a
**fixed finite cell, fixed strengths and fixed tree**. It supplies no
constant uniform in the cell size or coupling. Here is a precise
existence bound for the omitted remainder; it uses no computation.

Use Euclidean norm `r=||eta||_2<=r_0<=1` and put
`Phi(eta)=F_c((exp eta_l)_l)`. Global colour symmetry gives
`D Phi(0)=0` and the block Hessian `Hh_0(l,l') I_3`.
Let `mathcal C(eta)` be the full covariance matrix of the pinned forces
in tree-gauge coordinates. On the closed radius-r_0 ball define

`M_3 = sup ||D^3 Phi||`,
`L_C = sup ||D mathcal C||`, and `B_C=||mathcal C(0)||`.

These numbers are finite. The action is smooth on a finite product of
compact groups, its derivatives on this compact chart are bounded, and
`Z>=exp(-sum_p |beta_p w_p|)>0` for normalized Haar measure.
Differentiating the finite integral therefore gives the required smooth
functions and finite suprema. This is the order of choice: fix the cell
and strengths, fix r_0, then take these three constants.

Write `p_l=eta_l-(a.eta_l)a` and `Lambda=max_l |lambda_head(l)|`.
Along the returned pin curve,
`eta'_l=-2 lambda_l a x eta_l`,
`eta''_l=-4 lambda_l^2 p_l`.
Taylor bounds on the gradient and Hessian give

`|H_c-[Hh_0(eta',eta')+Hh_0(eta,eta'')]|`
` <= 6 M_3 Lambda^2 r^3`.

The quadratic part equals
`-2 sum Hh_0(l,l') (lambda_l-lambda_l')^2 p_l.p_l'`.
For the variance, set `d_l=lambda_l(a-Ad(exp eta_l)a)` and
`d^0_l=2 lambda_l a x eta_l`. The rotation Taylor formula, with its
integral remainder, gives
`||d||,||d^0||<=2 Lambda r` and `||d-d^0||<=2 Lambda r^2`.
Consequently

`|d^T mathcal C(eta)d-(d^0)^T mathcal C(0)d^0|`
` <= (4 L_C+8 B_C) Lambda^2 r^3`.

Thus L256 and L257 hold with these respective constants, and L258 holds
with `6 M_3+4 L_C+8 B_C`; replace Lambda by `||lambda||_2` if desired.
Symmetrizing the two lambda-squared terms gives exactly L258. In GR,
`c_l=-2 lambda_l^2 p_l+O(lambda_l^2 |eta_l|^2)` and
`E N_l=sum_l' Hh_0(l,l') eta_l'+O(r^2)`, which gives L259's force term.
The direct term has matrix K_0 and yields the other term at L259.

Corrected wording for L255–261:
“For each fixed finite cell and strength profile, the three expansions
hold uniformly over unit a with the remainder constants just defined.
They are expansions in the distance r of the tree-gauge pin from 1.
The displayed quadratic terms involve the transverse defects. No
size-uniform stiffness constant, or cubic remainder solely in ||Dn||,
is asserted.”

## 5. BOTH and ORB

**BOTH L274–287: HOLDS AFTER CORRECTION of the axis-link choice.**
Choose the axis-defining link `l_0` distinct from both `l_1` and `l'`,
and not entering z. Otherwise the proof's assignment
`eta_l'=rho u'` perpendicular to a conflicts with `a=axis(H_l0)`.
A face comb can be extended to a tree of the connected pinned graph
without changing any tree path between face vertices. This is the
required interpretation when applying the face example in the whole cell.

At pin 1 the boundary-only staple terms have zero imaginary part.
The single interior staple gives
`C_0(l_1,l_1)=(beta^2/3) E(1-t_p^2)>0` by colour symmetry and full support.
LEAD therefore gives the positive example in (i). For the indicated pair
of parallel edges, the shared boundary plaquette contributes
`K_0(l_1,l')=-beta/2`. Cauchy–Schwarz in one colour coordinate gives
`|C_0(l_1,l')|<=beta^2/3`, so `Hh_0(l_1,l')` is nonzero for
`0<beta<3/2`, exactly the advertised strict threshold.
With `h=|Hh_0(l_1,l')|` and `c=C_0(l_1,l_1)`, choose
`M>max(1,2c/h)`, then choose rho positive small enough that the bounded
cubic remainder is less than half the strict quadratic margin.
This proves the negative Q and H_c example. Reversing u' gives positive
H_c. Smoothness where `H_l0` is noncentral makes each sign persist on
an open set. These are witnesses for this frame and one lambda, not a
decision on all lambdas simultaneously.

**ORB L289–298: HOLDS.** The distinguished holonomy rotates about its
own axis and is unchanged. Tree links are unchanged, so P_x and a are
constant along the whole orbit. The per-edge rotations commute and
form a group. Thus phi'' really is the same H_c evaluated at the moved
pin. A bounded C^2 function on the real line with phi''<=0 is constant:
its derivative is nonincreasing, and any nonzero derivative would force
unbounded change on one half-line. The same argument applies to >=0.
If phi is nonconstant, phi'' takes both signs. Continuity of this axis
rule off its central exceptional set gives open pin neighbourhoods.
The closure of the commuting rotation group is a compact torus; a
maximum of F_c on its orbit has nonpositive second derivatives in all
the generated directions. No measure assertion follows for that set.

The theorem is orbitwise and specific to TREE with its invariant axis
choice. BOTH supplies both signs arbitrarily near 1 for `beta<3/2`.
Neither theorem excludes a positive-measure set where the entire
restricted gradient form is nonpositive.

## 6. WEAK — HOLDS

L300–304 uses precisely the corrected MASS hypothesis
`|beta_p w_p|<=b`, and absolute coefficients in its finer bound.
Each plaquette has at most four pinned edges and each four-dimensional
edge meets at most six plaquettes. Hence MASS gives coefficients
`4*6=24` and `2*6=12`. TG gives `|Dn_l|<=2|s(H_l)|`, so they become
96 and 24. Grouping terms by the head site proves exactly L301.
This is a finite-cell absolute upper bound, with delta tending to zero
as all fundamental holonomies tend to 1, even if the axis has no limit.
It gives neither a sign nor a necessary condition for O2. Its dependence
on the scalar potential lambda must be retained.

## 7. ONE+ — HOLDS AFTER CORRECTION; consumer exclusion FAILS

The new pinned-end convention is admissible for **general FLOW**.
An incoming free link can be written in left coordinates as
`b_l(U)=-lambda_y Ad(U_l)n_y`. This smoothly generates right translations,
with zero Haar divergence. Outgoing free links use fixed left rotations.
The same gauge return cancels them exactly. For constant boundary lambda
one indeed has `H_c=0`, `Q=Var(Psi)`.

The strict variance argument at L312–317 holds under explicit conditions:
a plaquette contains l as its only pinned edge and contains a private free
edge (no other plaquette with a pinned edge contains that free edge).
Its strength is nonzero. Conditioning on the other free links then leaves
`beta_p w_p Dn_l . Im(A U^+-1 B)` plus a constant. This is nonconstant
when `Dn_l!=0`. If zero strengths are allowed, strict positivity is
false without the nonzero-strength condition: all strengths zero give
Q=0 for every frame.

The printed size `S_mu>=4` does not by itself supply the two all-deep
plaquettes used for the null-set conclusion L315. In a face of a
side-4 box, a site at distance at least 2 from every other face has all
three tangential coordinates equal to 2. There are no edges whose two
ends both lie in this one-point interior. Thus the described deep-link
witness is absent. A safe corrected version assumes the private-edge
property explicitly. For the stated distance-2 construction,
`S_mu>=5` suffices: take two face plaquettes based at tangential
coordinates (2,2,2), in two different planes. All their vertices have
coordinates 2 or 3. Their opposite interior edges at normal coordinate
1 are private when the normal side is at least 4.
If defects vanish on these two plaquettes, their holonomies fix the
same unit vector. Their noncentral axes must therefore be parallel.
Fixing all pins except one exclusive edge of each plaquette leaves
two independent Haar holonomies. Parallel axes have measure zero.
This proves the corrected almost-everywhere obstruction for this
specified extension and geometric patch.

It is **not** the old site-frame class. At an interior site incident to
several incoming free links, the required vectors `Ad(U_l)n_head(l)`
need not agree. One site vector cannot represent all these right
rotations. General FLOW allows them; row 1034's `V_theta=theta n_tail`
does not automatically do so.

The first unsupported consumer inference is L318–319, and L327 repeats
it as “of no use to the consumer.” Showing one extension has a positive
variance at B=0 does not exclude another extension. The zero extension
at B=0 has Q=0. Even within the displayed cube example, subtracting
`lambda_110` changes the free-link extension while keeping the boundary
rotation, and removes the entire variance for TREE.

Corrected text:
“ONE+ obstructs the pinned-end extension with constants admitted, under
its private-edge and positive-strength hypotheses. It does not refute
existential O2 over other allowed extensions, or O2 restricted to lambda
supported on L. It gives no reason to replace O2 by O2-min as an
equivalent condition.”

Indeed FLOW proves only `H_c<=Q`. Equality requires constant Psi. The
existence argument for an optimizing general flow in the original FLOW
source is explicitly ARGUED, and does not give a local site frame.
O2-min is a necessary extension-free condition; its sufficiency for
the consumer is not proved here.

## 8. TUNE and the covariant/U(1) controls

**TUNE L351–387: HOLDS, with its printed non-covariance and zero-mode
exceptions.** Put `A=b_0+kappa`, `c=cos(alpha)`, `v_s=sin(alpha)`.
The assigned vectors give
`d_1=(c-1)u_0+sign(A)v_s w`,
`d_2=(c-1)u_0-sign(A)v_s w`.
Both are perpendicular to s, so the kappa-prime contribution is zero.
The cross-product bracket in CUBE-H becomes
`-sign(A)v_s [theta_1^2+theta_2^2-2(1-c)theta_1 theta_2] s/|s|`.
The norm term is exactly the first bracket at L360.
Using `2|theta_1 theta_2|<=theta_1^2+theta_2^2` gives L362.
For `lambda_110=0`, GR contains only `theta_1 X_a+theta_2 X_b`.
Each random scalar is bounded in magnitude by `2 beta sin(alpha/2)`;
thus the stated variance bound `8 beta^2 sin^2(alpha/2) sum theta_i^2`
is valid, including all cross covariances. Factoring `4 sin(alpha/2)`
gives L363 and exactly the strict condition L365.

There is a measurable angle choice. For example, with
`D=2|t||A|+2 beta^2>0`, set
`q=min(1/4, |A||s|/(4D))` and `alpha=2 arctan q`.
Then `q D<=|A||s|/4` and `cos(alpha)>=15/17`, so L365 holds.
Choose u_0 by projecting the first fixed coordinate axis not parallel
to s and normalizing. This is measurable, though not covariant.
The explicit pin test above supplies a completely evaluated example.

The decrease is **by acceleration**: `F_c'(0)=0` along these curves,
while `F_c''(0)<0`. The acceleration has a component along the gradient
of F_c at a non-stationary pin. Thus “descent direction” should read
“a locally descending pin curve through a non-stationary pin.” It is
not a negative intrinsic Hessian on a stationary quotient, a uniform
classical stiffness constant, or a gain across scales. The extension's
zero curl means `d(d lambda)=0` for the scalar cochain; it does not mean
the colour-valued rotation `(d lambda)n` has zero covariant curl.
The nonzero pair `(theta_1,theta_2)` is necessary for strict negativity;
the remaining corner gauge direction has H_c=Q=0.

**Covariant cube L389–395 and compact U(1): HOLDS as structural controls.**
At a noncentral cube pin, its stabilizer fixes only the holonomy-axis
line. After transport to 000 each covariant vector is therefore
`sigma_z s/|s|`, with one sign per site. The cross products in CUBE-H
vanish and

`H_c = F_c,phi phi [theta_1(sigma_100-sigma_000)
                   -theta_2(sigma_010-sigma_000)]^2`,
`F_c,phi phi=(b_0+kappa)cos(phi)-kappa' sin^2(phi)`.

Compact U(1) has the same chain-rule structure with its own free energy;
the two theories' free energies are not asserted equal. With a common
site sign, Dn=0 and GR gives Psi=Q=H_c=0. With different site signs the
displayed response need not vanish. “Zero gain” is the absence of a
selective non-Abelian mechanism in these identities, not an assertion
that every signed-frame response equals zero. TUNE cannot be covariant
on this one-plaquette pin: it requires u_0 perpendicular to the very
axis its stabilizer forces a covariant vector to follow.

## 9. The two ARGUED meanings — FAILS as stated

**The threshold `S^3` (L332–342): first failing estimate L336–337.**
WEAK controls `delta sum_sites lambda^2`, not
`delta sum_edges (d lambda)^2`. The cited count `f^2 S^5` is a count
for link angles theta. A scalar potential for a slowly varying gradient
with `theta=O(f S)` has size `lambda=O(f S^2)`. On a three-dimensional
face, its squared norm is then of order `f^2 S^7`.
This is a hand-checkable scaling countertest. Let
`lambda(x)=f S^2 product_(j=1)^3 min(x_j/S,1-x_j/S)` on the lower face,
and zero elsewhere on the boundary. It vanishes on that face's edges,
so this definition agrees there. On its middle half, lambda is bounded
below by a fixed multiple of `f S^2`, on order `S^3` sites. Everywhere
it is at most a fixed multiple of `f S^2`, and a nearest-neighbour
difference is at most a fixed multiple of `f S`. Thus
`sum lambda^2` has order `f^2 S^7` while
`sum_pinned_edges (d lambda)^2` has at most order `f^2 S^5`.
These are the boundary links counted in the source's scaling argument.
The ratio has the missing factor `S^2`. This lambda is supported on L.

Comparing that **gradient-error estimate** with `b f^2 S^4` would require
`delta` of order at most `b/S^3` by this argument, not `b/S`.
Even if one separately supplied `delta<=C b |s(H)|^2` and the heuristic
`|s(H)|^2` of order `S^2/b`, this arithmetic would give `S^5` rather
than `S^3`. This is a diagnostic of the claimed deduction, not a new
threshold theorem. The displayed WEAK bound is actually linear in
`|s(H)|` near zero; LEAD has fixed-cell constants and gives no uniform
replacement by `C b |s(H)|^2` as S and b vary.

There are two further missing premises. The cited row 1011 L480–484
contains only an ARGUED single-plaquette size estimate, not a theorem
for cell-size Wilson holonomies, their maxima or rare cells. Also the
comb's fundamental loops in LIP-TREE bound strips of area at most
`S_1+S_2`, not area S^2. A chosen different loop family needs its own
geometry and measure estimate. No “only when” statement follows from
an upper bound on the defect; holonomy parallel to a can have zero
defect without small class angle.

Corrected text:
“WEAK gives a finite-cell gradient-error bound. Applying it to a
scale-invariant response requires a scalar-potential norm estimate,
control of mixed terms and constants, and typical-pin/rare-cell bounds.
Neither an S^3 threshold nor failure at typical order-one pins is
established here. N1 alone is insufficient; N2 and N3 remain additional.”
For example, vanishing on gradient squares alone does not bound mixed
terms: the quadratic form `2xy` vanishes on the y-axis but is not
bounded above by `C x^2`. A full curl estimate needs that issue settled.

**No exact curl mechanism in the collapsing-defect class (L479): FAILS.**
The first invalid extension argument is L318–319; L327 draws the route
conclusion from it. ONE/ONE+ concern specified extensions. BOTH concerns
one TREE rule and one lambda; ORB compares points of a particular orbit.
None excludes one frame and a positive-measure set of pins on which all
required gradient directions have nonpositive cost, with a different
admissible extension. The covariant transported cube gives an explicit
zero-cost exception. The 4D lambda-on-L problem is expressly open at
L325–327 and L397–406. A theorem declaring the whole class closed cannot
follow while that case remains undecided.

Replace L477 and the route sentence in L479 by:
“O2-min is a necessary extension-free test, not a proved replacement for
O2. The transported cube has H_c=0 and an extension with Q=0. For TREE
in the 4D cell, the proved examples give both signs, with BOTH's coupling
and link-choice hypotheses. The displayed extensions do not supply a
selective curl mechanism. Existence of such a mechanism in the general
collapsing-defect class, or for all lambda supported on L on a
positive-measure pin set, remains open. No gain at order-one coupling
has been established by this file.”

## Final verdict record and limits

| Source statement | Verdict | Precise scope or repair |
|---|---|---|
| TG; LAD; LIP-TREE | HOLDS | Root axis supplied on its domain; face comb; curvature radius, not uniform read range |
| NOLIP | HOLDS | Equivariant local evaluation maps on their invariant domains; density strictly greater than 3/4 |
| CUBE-H; transported cube | HOLDS | Restore lambda_110 squared in the isolated direct/force terms |
| ONE | HOLDS AFTER CORRECTION | Positive unless Dn=0; the zero-form exception is realized covariantly on the cube |
| LEAD | HOLDS AFTER CORRECTION | Fixed-cell remainder constants specified in section 4; no uniform stiffness constant |
| BOTH; ORB | HOLDS AFTER CORRECTION / HOLDS | BOTH needs a distinct axis-defining link and 0<beta<3/2 for its explicit pair; ORB is orbitwise |
| WEAK | HOLDS | Absolute strengths; bound on lambda, not d lambda |
| ONE+ | HOLDS AFTER CORRECTION | Private free edge, nonzero coefficient, adequate deep patch; one new FLOW extension only |
| TUNE; covariant/U(1) controls | HOLDS | Non-covariant descending curves; gauge zero modes retained; structural Abelian control |
| S^3 threshold; closure of route (ii) | FAILS | First failures L336–337 and L318–319; corrected meanings above |

Checked by hand: every requested mathematical statement and its load-bearing
source convention. Not checked: the author's GUIDE runs or their logs,
original Balaban/Uhlenbeck papers, a global thin-set frame construction,
whole-boundary/tiling compatibility, a covariant TUNE in larger cells,
or any typical-pin probability estimate. No new attack, numerical run,
Lean certificate, audit, ledger edit, source repair, or external post was
performed. The mathematical arguments are finite quaternion algebra,
finite-dimensional differentiation, Haar invariance and elementary bounds;
no conclusion depends on a machine evaluation. The open consumer questions
remain open. Only this report is changed in the checkout.

RESULT: Row 1041 research check of row 1038 at 1a4ecc662: the finite-cell frame identities, NOLIP constant, corrected LEAD expansion, WEAK and non-covariant cube TUNE survive; ONE/ONE+ require their zero-form, strength, geometry and extension restrictions. The S^3 threshold and the claimed closure of route (ii) for collapsing-defect frames FAIL as stated. Existential 4D O2 remains open; no audit status or mass gap is claimed.
