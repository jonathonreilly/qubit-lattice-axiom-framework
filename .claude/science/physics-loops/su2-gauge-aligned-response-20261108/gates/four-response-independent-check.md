# Independent check of the two fourth-response consequences

2026-11-09. Research gate, not landing review, an audit verdict, or retained
status. Both frozen consequences have research signal **advance** within their
stated domains. No material mathematical correction is required by this check.

## Findings and disposition

| Severity | Finding |
|---|---|
| Critical / high | None found in either frozen argument or the necessary supplier steps checked below. |
| Medium | None found. In particular, no shrinking-threshold prefactor, missing cumulant pairing, cube boundary term, or volume factor was found. |
| Scope boundary, already explicit | The compact result is a nonspatial fourth-cumulant bound for the stated root-fixed-gauge-invariant source class. The spatial and summability results concern the fixed quotient cube. They do not combine into a full compact spatial bound. |

The broader globally conjugation-invariant-only source class is not covered by
the compact source-moment argument. The draft's forest-edge example correctly
refutes that moment step, while making no claim to refute the target cumulant.
This is a checked scope distinction, not a new no-go result.

The complete new arguments were read: `full-compact-fourth-scaling.md`, lines
1–252, and `chart-fourth-connected-bound.md`, lines 1–258. The specific checks
below used the original supplier text, not earlier gate conclusions.

## Frozen sources and review provenance

Source root:
`/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics`.
Pack: `.claude/science/physics-loops/su2-gauge-aligned-response-20261108`.
Source checkout HEAD: `55fd670ff8995427b24617b2273bd3f78b7559d9`.
Coordinator's main pin, matching the locally available `origin/main`:
`1e0d3b58dcda7f83152b0bb51729260247454d65`.
The new drafts were untracked files, so their byte hashes, not HEAD alone,
identify the checked source. No fetch or other Git/network mutation was made.

All filenames in the following table are under `parts/`, except the explicitly
identified main note.

| Source | SHA-256 |
|---|---|
| full-compact-fourth-scaling.md | 549757b9574e7d50b8626ac0421889152cd2fae284f3d8589fe01309c3f86094 |
| chart-fourth-connected-bound.md | 848015af72eda20f25644b960ba52f5a438ad85c20a756cecadd510d7ee26aa4 |
| rough-component-bound.md | 1a4c40385f1fc492033f261f8ed938bed23f32475eb9a116347fd7361f9e9c44 |
| local-relative-coercivity.md | 6b7c3a0eba818566fad0cb34f13998a3cf98de632761d7942ca527c51c80cb37 |
| nonlinear-chart-response.md | 5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1 |
| flat-two-step-bound.md | 0f028f694bb686cf4272d8620329f1f2e8535d8af9a2d028bbde6965cab3f03a |
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |
| compact-energy-coercivity.md | 7e8e798759239aadfc8c137125bf23f6d1de2cac18b714ddca70ea294cbaa4aa |
| local-conditional-tail.md | cf47acdfe0deea09fe49f7b08d90d45a3aac0df3251062ba4f67f566e639072d |
| docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md | 94986863c312a5880569cdf8d663c191a3d802a51542e2b671bcfdbc615e913c |

All listed part files except `local-conditional-tail.md` were read in full.
For that file, sections 1–3 and the necessary portion of section 4 were read;
the actual conditional and compact Haar/radial estimates are the inputs here.
The main note was read through sections 1–3. No conclusion about its remaining
appendices or the historical draft dependency chain is supplied by this gate.

Root AGENTS.md and SCIENCE_WORKFLOW.md were read, as were the applicable
physics-claim-reviewer procedure, proof-search governance, review-loop's
focused mathematical/independence contract and scientific lenses. The checked
procedure files match the pinned main revision. The destination worktree's
AGENTS.md and SCIENCE_WORKFLOW.md match the source worktree. Their hashes are,
respectively, `7def904fdd52d811e7aba87a0d3d859bfb017cccd59703125f4a53f2805aaab2`
and `1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca`.
The dated search inventories were consulted for method/scope context only;
no external clustering theorem or inventory verdict is a proof premise.

The reviewer was separate from the two draft authors and preserved the
inherited supervising model and effort; no model override was requested or
used. The exact runtime identifier is not exposed by the tool interface, and
no cross-provider independence is claimed. Independence here consists of
reconstructing the estimates, boundary identities and cancellations from the
specified law and source formulas, including the alternative connectivity
argument and algebraic controls below. No numerical job, runner, formal
verification, source edit or status mutation was performed. Only this report
was written; no editable prompt file changed.

## 1. Compact law and threshold uniformity

The forest change of variables was checked directly: recursively multiplying
fresh tree-link Haar variables gives product Haar site variables; conditioned
on those variables, each remaining original link undergoes fixed left/right
multiplication. Thus `dU=da dh`. Common-endpoint path covariance preserves each
kernel numerator and each input-dependent radial normalizer separately. The
root-fixed orbit remains independent Haar under the actual posterior. This
checks the law needed in `full-compact-fourth-scaling.md`, lines 14–20 and
43–52, without assuming independence of the interacting quotient coordinates.

For the relative supplier, the flat leading Hessian really has a uniform gap:
zero energy forces `d0 a0=0`, `a1=Q0 a0`, and `Q1 Q0 a0=0`. At nonzero Bloch
momentum a closed fine form is a gradient, and actual contour telescoping
forces its terminal value to vanish. The fine tree slice then kills the
gradient. At zero momentum the only additional harmonic form is multiplied
by `L^2` by `Q1 Q0`, so it also vanishes. Continuity of the finite fiber matrix
on the compact momentum torus gives a positive minimum. Principal
restriction preserves that gap for arbitrary interior sets.

I also checked the independent compact lower-bound mechanism used by the
relative supplier: the inequality `d(V,T)^2 <= 4 gamma + 3 average d(P,T)^2`
retains the mean deficit and holds at a zero mean; finite lifted path fillings
retain winding displacement through the explicit terminal straight path.
Bounded template incidence gives the global compact chord-square bound. In
the relative perturbation, each factor is globally Lipschitz in the small
background. The small-q Taylor remainder is `O(epsilon sum d(q,I)^2)`, and
outside a *fixed* q cap its uniform `O(epsilon)` bound is divided only by that
fixed cap radius squared. The summed linear proxy vanishes by stationarity.
This is why the relative lower-bound constant does not depend on the later
roughness threshold. The cap upper bound is also chosen once after fixing
`epsilon_*`.

For the new threshold argument (lines 54–102), set the exterior allowance and
rough threshold both equal to `t`. Then choosing
`C_* exp[-alpha(h+1)] <= 1/4` fixes the same h for every `0<t<=t0`.
For an entire rough component S, its exterior reader cells are good because
they are adjacent in the fixed component graph; no outside independence is
used. The supplier's stationary reference is within `t/4` on S.

The denominator integrates over `d(q_e,I)<=b/sqrt(u)`, with b independent of
t. It must not integrate over `bt/sqrt(u)`. On this cap every selected mean
has norm at least `1/2`, uniformly down to `t=0`. If n is the number of actual
retained coordinates and k the number of whole selected kernels, the cap
mass and radial factors give `u^{-3n/2} u^{3k/2}`. After extracting the rough
charge, the unrestricted numerator Haar integral gives exactly the same
power. Conditionally constant normalizers may be bounded on both sides and
remain included; there is no unmatched intermediate-layer power of u.

Hence the component bound is `C0^|S| exp[-a u t^2 |S|]` with fixed C0,a and
fixed animal degree Delta. In the variable `z=u t^2`, the animal series is
geometric when `z >= log(2 Delta^2 C0)/a`. Below that crossover, a single
fixed `K >= 2 Delta^2 C0` makes `K exp(-a z)>=1`. This verifies the claimed
pointwise `min(1,K exp[-a u t^2])` bound, including `t << u^{-1/2}`. Whole-torus
components use the stationary reference I and require no exterior collar.

Integrating this bound over `0<t<=t0`, and using the fixed `t0` tail above it,
gives `E X^p <= C_p u^{-p/2}` for every fixed p>0. The latter contribution is
controlled by the finite supremum of `u^{p/2} exp[-a u t0^2]`. The finite-set
union bound introduces only the number of owner cells, not total volume.
These are moments in the actual compact posterior quotient.

## 2. Compact sources, scores, cumulants and tilts

At the identity, simultaneous conjugation acts as the adjoint rotation in
each coordinate tangent space. Setting every tangent component but one to
zero shows that each component of an invariant differential is zero. Along
product shortest geodesics, the covariant Hessian bound therefore gives
`|f(a)-f(I)| <= (pi^2 H_f/8) sum d(a_e,I)^2`, also at an antipode by choosing
any minimizing geodesic. This independently checks the global, rather than
chart-only, Taylor step at lines 118–139. The compact moments imply
`||f-f(I)||_4=O(u^-1)` and likewise for g.

For the last kernel, the derivative at terminal identity has no scalar
identity contribution: `A_c=kappa u <v_c,M_c-I>`. Telescoping its actual
finite unitary words bounds this by a fixed sum of input chord distances,
so `||A_c||_4=O(|v_c| sqrt(u))`. This uses the actual intermediate-link
posterior, without inserting a Wilson action at that layer.

The partition formula for four cumulant arguments has absolute coefficient
sum `1+7+12+6=26`. Applying Holder inside each block with exponent equal to
its size, followed by monotonicity up to L4, gives the product of the four
L4 norms for every partition. Constant shifts of f and g do not change the
cumulant. The resulting power is
`u^-1 * u^-1 * u^(1/2) * u^(1/2) = u^-1`, as asserted at lines 157–170.

As an independent algebraic scaling control, for `x=Z/sqrt(u)` and a standard
one-dimensional Gaussian Z, the centered formula gives
`kappa4(x^2,x^2,ux,ux)=8/u`: its unscaled value is
`(15-2*3+1)-2=8`. This is a Wick-moment consistency check, not an example of
the actual SU(2) law or a substitute for its proof. It confirms that the
power counting does not secretly require a stronger cancellation.

The source-class caveat was checked on the exact forest disintegration:
for a fine tree edge, `U_e=h(x)^*h(y)` is Haar under the full posterior for
every u, including when one endpoint is the fixed root. Thus `F=w(U_e)` is
smooth and globally conjugation invariant but its distance from 1 has a
nonvanishing moment. For non-H-invariant sources the generating orbit factor
is the integral of `exp(sF+tG)`, whose mixed logarithmic derivative is the
conditional orbit covariance. The draft retains this distinction correctly.

On a bounded rectangle of real source tilts, the density ratio is at most
`B=exp[s0 osc(F)+t0_source osc(G)]`; this follows by comparing the maximum
and minimum of the exponent, including its denominator. Each L4 bound gains
at most `B^(1/4)`, so the cumulant estimate gains at most B. No complex tilt
or nonidentity terminal neighborhood is obtained this way.

## 3. The fixed-cube supplier, including its boundary domain

The chart argument uses the actual negative logarithm
`S=u Phi + sum h(kappa u r) - sum log j`, with `h(z)=log Z(z)-z`.
The signs follow by expanding the normalized kernel exactly. On the fixed
small cube, all means stay away from zero; the local factor and incidence
bounds control the Hessian perturbation by `u C delta + O(1)`. Combined with
the checked flat gap, this gives `Hess S >= m0 I`, `m0=u g_*/2`, and finite
spatial Hessian range. Normalizers and coordinate Haar densities are present.

I reconstructed the covariance identity with the cube boundary explicitly.
For the scalar weighted Neumann operator `L=-Delta+grad S dot grad`, a
Neumann solution v has zero normal derivative on each face. Its gradient
therefore has zero normal component; the normal derivative of every
tangential component is zero by tangential differentiation of that Neumann
condition. Consequently the vector operator is `L I + Hess S` with normal
Dirichlet and tangential Neumann conditions, not all-component Neumann.
Its quadratic form is the sum of gradient squares and the Hessian form.
The scalar Bochner integration has zero face curvature contribution on the
box; edges do not supply an additional codimension-one boundary integral.
Closing these forms yields the scalar gap at least m0 and
`Cov(f,g)=<T^-1 grad f,grad g>` for the stated C1 functions.

The diagonal spatial weight acts on vector coordinate labels, not on the
point in the cube. It commutes with the differential part and preserves
those mixed face conditions. Only the finite-range Hessian is conjugated.
Its row/column bound gives a perturbation smaller than `m0/2` for a fixed
small alpha, and hence the stated exponentially weighted inverse bound.
The same scalar gap proof applies to `S-t h dot a`: its Hessian and domain
are unchanged for every real t. Thus the input covariance and tilted gap
used by the new draft have compatible domains.

For the coordinate moments, the law and cube are invariant under each
simultaneous color pi rotation around a coordinate axis. Every coordinate
component is flipped by one such rotation, so its mean is zero; full
continuous rotation invariance of the cube is unnecessary. Integrating
`d^2/dt^2 log E exp(t h dot a) <= |h|^2/m0` twice gives the stated Gaussian
tail and finite local moments. Conjugation invariance of a source at zero
still forces its differential to vanish, because the source is a restriction
of the invariant original function. Taylor's formula on the convex cube then
gives centered source size `u^-1` and gradient size `u^-1/2`. The actual score
has centered size `u^1/2` and gradient size u. These checks establish precisely
the scales used at lines 128–136 of the chart draft.

## 4. Every cut, connecting geometry and the weighted sum

I obtained the cut identities from the centered moment-cumulant polynomial.
Across a `1|3` cut, the raw fourth moment is the covariance of the singleton
with the triple product, and every subtracted pairing contains a crossing
pair. Across a `2|2` cut, the covariance of the two products already subtracts
the within-side pairing; the two other pairings cross the cut. Thus the
expressions at lines 151–165 contain every term with the correct sign. A law
which is a product of the two pair-marginals makes the `2|2` expression vanish
exactly, even when each within-pair covariance is large. Singleton cuts alone
would not establish that cancellation.

For a product of k<=3 centered insertions, the gradient product rule and
Holder exponents 2k give
`||grad product X_i||_2 <= C sqrt(u) product w_i`.
No union diameter appears in this norm. The covariance bound across each cut
therefore costs `u^-1 * sqrt(u) * sqrt(u)=1`, leaving
`product w_i=u^-1`. Pairing terms have the same scaling by using one crossing
covariance and an ordinary L2 bound for the other pair. Moments of order six
for the insertions, hence at most twelve for the underlying coordinates,
suffice. No unassumed third or fourth source derivative is used.

As a separate check of the tree step, take one representative in each support
and let b be the smallest distance threshold making their four-label graph
connected. Just below b there is a nonempty cut whose representative crossing
distances are all at least b. At threshold b a spanning tree has at most
three edges of length b, so `tau<=3b`. Actual support points can shorten a
representative distance by at most `2D`. Thus some cut has separation at
least `tau/3-2D`, proving the exponent `alpha/3` independently of the draft's
choice of a largest minimum-spanning-tree edge. This also covers repeated
representatives, overlapping supports and periodic shortest distances.

A connected graph meeting all four supports gives, independently,
`d(x_F,x_G)<=tau+2D` and
`d(x_F,x_c), d(x_F,x_d)<=tau+D+R`. Adding yields the draft's factor 1/3 in
the lower bound for tau. After multiplying by `exp(nu tau)`, the remaining
rate is `eta=alpha/3-nu>0`. The two terminal-anchor sums are bounded by
the square of `4 sum_r (2r+1)^4 exp(-eta r/3)`, uniformly in periodic volume.
The geometric majorant can be extended to diagonal link labels without
using a same-link response identity. This verifies the weighted summability
claim and `b_nu=eta/3` at lines 199–227.

## 5. Response identity and final boundary

For distinct independent terminal links, the logarithmic density has separate
first derivatives A_c and A_d and no mixed derivative of either score.
Taking the coefficient with one copy each of the two sources and the two
terminal variations in its logarithmic generating integral therefore gives
exactly the fourth cumulant, with a positive sign. A repeated-link variation
would also differentiate its score and contribute a third cumulant. The
fixed chart introduces no moving-domain derivative. These checks agree with
both drafts' response formulas.

For a coarse normalization independent of the varied terminal coordinates,
the terminal derivatives annihilate its source-dependent logarithm. For an
exterior conditional denominator that depends on those coordinates, its
complete response must instead be subtracted. Neither frozen draft asserts
that its posterior estimate supplies that second law's bound. Their statements
therefore preserve the main note's normalization and total-covariance boundary.

This gate supports the threshold-uniform compact local moments and stated
nonspatial O(u^-1) cumulant, and the fixed-cube O(u^-1) connected tree and
weighted-sum estimates. Full compact spatial response, normalized rough-field
gluing, non-H-invariant orbit contributions, nonidentity terminal backgrounds,
terminal-integrated denominator control and further blocking remain outside
these conclusions. Reopen the affected check if a listed source hash, source
class, reader ownership, domain, covariance boundary condition or normalization
convention changes.
