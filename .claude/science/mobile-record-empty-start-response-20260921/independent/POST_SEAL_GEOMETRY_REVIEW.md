# Post-seal review: geometry and the volume-uniform remainder

**Confirmed within the stated finite-model scope. No actionable mathematical
defect found.** The d-dimensional torus coefficient is correct for d>=1 and
side L>=6. The strict-positivity argument covers every positive symmetric
row-six W other than the all-ones matrix. The displayed support bound, Taylor
constant and uniform small-time sign follow with the given constants.

This was a narrow post-seal check. The complete working note was read for
premises; this report verifies its geometry reduction and population remainder,
plus the named graph checker/output. It is not a review of the complete PR,
the separate simulation claims, or the spectrum remainder. The original
independent report, code, results and seal remain unchanged.

## Exact sources reviewed

All three paths are relative to
`.claude/science/mobile-record-formation-20260920/campaign12h/`:

* `EMPTY_START_DERIVATION.md`:
  SHA-256 `4e34cda1cb85a8b7471c80f22bad5a56d64319b8bb3090fdcdcea0174091ec74`.
* `empty_start_geometry.py`:
  SHA-256 `182ce88938e4f7471b6801972bfbc8630b9dc79fd29918d36af3c33399727aec`.
* `EMPTY_START_GEOMETRY_RESULTS.json`:
  SHA-256 `52d18fa0fac5f62686421df89e021b17ac2114833e6b6a939a0166289bdf601c`.

The note and code were read completely. Hash guards before and after the
execution checks confirmed these identities.

## Geometry and strict positivity

For a fixed physical hop edge, spectator site and ordered pair of moving/fixed
contents, there is exactly one undirected two-record configuration edge.
This remains true when the contents are equal. Its conductance is uv/(u+v),
and its hazard difference is h_ab times the difference of the two common-
neighbor counts. Thus the general graph sum has the correct counting and no
missing factor of two.

For one endpoint of a torus edge, distance-two sites comprise 2d axial sites
with common-neighbor count one and 2d(d-1) diagonal sites with count two.
Their squared-count sum is 2d(4d-3). The part adjacent to the other endpoint
is one forward axial site plus 2(d-1) diagonal sites, giving
alpha=1+8(d-1)=8d-7. The remaining squared-count sum is
beta=8d^2-14d+7.

The two endpoint families are disjoint for L>=6: an overlap would produce an
odd closed walk of length five through the hop edge, impossible on these
tori. The distance-two coordinates also remain distinct at this minimum
size. Combining both endpoint families gives 2 alpha W/(1+W)+beta, since
the second class has conductance 1/2. There are d undirected edges per site,
which proves the displayed formula for D_2/V.

For d=3 and W=(3/2,1/2,1), the two menu sums are 3 and 7/5, so

`D_2/V = 3[34(7/5)+37(3)] = 2379/5`,

and division by 60 gives `793/100`. No rounding or imported constant occurs.

For the general positivity claim, symmetry and the row sum give AJ=JA=0 for
A=W-J, hence h=A^2. Its squared Frobenius norm is tr(A^4), positive for a
nonzero real symmetric A. Also alpha>0 and beta>0 for every integer d>=1,
and W/(1+W)>0. Thus the result is strict exactly when W is not all ones.
The sign of a centered content eigenvalue is irrelevant. Symmetry is a
load-bearing hypothesis of this proof.

Independent checks count length-two walks rather than intersecting neighbor
sets, reproducing the geometry in dimensions 1--4 at sides 6 and 7. Direct
birth-hazard sums over actual two-record configurations reproduce the energy
on a six-cycle and on the 6x6 torus with a matrix lacking axis symmetry.
The excluded five-cycle has the nonadjacent spectator count zero instead of
two; it is a concrete check that the side-length restriction matters.

## Support-by-support estimate

The norm argument is valid when a local jump difference is kept grouped as

`T_i f(s) = r_i(s)[f(s^i)-f(s)]`.

The phrase **"touching support S" should be understood as "whose updated
site or sites intersect S."** Making this phrase explicit would improve the
presentation, but no constant needs changing. An operator whose updated sites
miss S annihilates f, even if its rate inspects S. Counting all rate-support
intersections would be the wrong counting argument.

For a birth at x, the updated set is {x}, its rate depends on the closed
neighborhood of x, and each of its six channels is bounded by epsilon u^z.
Only x in S contributes. For a hop across {x,y}, the updated set is {x,y};
after cancelling the common factors in the strictly positive product w, its
heat-bath rate depends only on the closed neighborhoods of x and y. The rate
is at most kappa. At most z|S| undirected edges meet S. Hence

`sum_(active local operators) ||r_i||_infinity <= R_kappa |S|`.

Each such operator has norm at most 2||r_i||_infinity ||f||_infinity.
A birth adds at most z sites to a chosen support. A hop adds no more than
2(z+1) sites, since the union of its two closed neighborhoods has at most
that many vertices. Thus K=2(z+1) is safe; it is larger than necessary.

Expand L^j f as a sum of local-operator words, without replacing their
individual supports by their union. Every word has support of size at most
1+jK. If A_j is the sum of the norms of the resulting word terms, then

`A_(j+1) <= 2 R_kappa (1+jK) A_j`, with `A_0<=1`.

This proves exactly the displayed product bound for ||L^k f||. The argument
requires neither a bound on the inverse minimum weight nor derivatives of
the rate functions: heat-bath acceptance is at most one, and all dependence
is handled by support expansion.

Exact full-generator multiplication independently checked this inequality
through k=6 for every occupancy observable on a singleton, three-site path
and four-site star, with and without motion. All 96 rational norm comparisons
pass. These finite checks corroborate the proof; they are not a substitute
for the general local-operator induction.

## Remainder and the sign window

For each finite Markov generator, Taylor's integral remainder on f is

`integral_0^t (t-s)^5 exp(sL)L^6 f ds / 5!`.

Supremum-norm contraction bounds it by t^6||L^6 f||/720. Apply the estimate
to each n_x for both generators and average sites. The already-derived
population coefficients through degree four cancel after this averaging;
individual-site cancellation on an arbitrary irregular graph is unnecessary.
The fifth coefficient is the stated a. This gives exactly

`|rho_kappa(t)-rho_0(t)-a t^5| <= C t^6`

with the displayed C. For a>0 and 0<t<=a/(2C), the difference is at least
a t^5/2. Thus the claimed volume-uniform positive window follows for fixed
d>=1, fixed W not all ones, fixed positive kappa and epsilon, unit proposals,
and every torus side L>=6. Uniformity is over side length; it does not mean
uniformity in dimension, maximum degree, weight bounds, or rates.

The conservatism is substantial. For example, at d=3, W=(3/2,1/2,1),
epsilon=1/7 and kappa=2/3, the displayed constants give
R_kappa=3083/224, R_0=2187/224, K=14 and a=793/360150. The certified upper
time is approximately `2.13491716195e-17`. This does not invalidate the
uniform statement, and the note correctly does not use it to certify its
moderate-density behavior or a later-time sign.

## Execution and preservation evidence

`post_seal_check.py` executes the exact author runner, redirecting only its
attempted result-file write into this independent directory. Its reproduced
JSON is byte-for-byte identical to the reviewed result. Author files are
hash-checked unchanged. The same independent script performs the alternative
geometry counts, direct birth-hazard energy sums, both signs of a centered
rank-one matrix perturbation, and the 96 full-generator norm checks.

Evidence files are `POST_SEAL_PRIMARY_RUN.log`,
`POST_SEAL_PRIMARY_REPRODUCTION.json`, `POST_SEAL_CHECK_RESULTS.json` and
`POST_SEAL_CHECK_RUN.log`. `POST_SEAL_GEOMETRY_REVIEW_SEAL.json` pins those
outputs, the checker and this report, the three reviewed source identities,
and the unchanged original `SEAL.json`. No author file, earlier sealed file,
Git state or audit record was changed.
