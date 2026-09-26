# Provisional independent proof review, before author-checker access

This review has read the complete proposed static-phase argument, the
identity-matched model note, and the specified external theorem. It has
not read or executed gauss_loop_polymer_check.py or its results. This is
therefore a pre-checker seal, not a claim of independence from the
proposed proof text itself.

The E/B small-fugacity theorem is supported by the reconstruction below.
No load-bearing mathematical gap has emerged. Two extensions deserve
explicit conventions: the numerical covariance prefactor for general
bounded observables must include their norms, and vacant-exterior boxes
must retain the Gauss constraints at every charge vertex incident to an
allowed edge. These qualifications do not alter the stated E/B bound
or the periodic limit.

## Imported theorem and read boundary

The version actually read is Daniel Ueltschi,
[arXiv:math-ph/0304003v3](https://arxiv.org/pdf/math-ph/0304003v3),
18 February 2005, Section 2 through the end of the proof on page 4.
Theorem 1 assumes a complex measure of finite total variation, a
symmetric pair factor with |1+zeta|<=1, and a nonnegative function a
satisfying the integral smallness condition and integrability with
weight exp(a). Its connected coefficient includes 1/m!. Equation (5)
bounds the absolute cluster sum marked by the number of incompatibilities
with any fixed root, by a(root).

These hypotheses and the root normalization were read in full, including
the proof; no correlation theorem from Section 3 is being imported.
The PDF version and byte identity are preserved in EXTERNAL_SOURCE.json.
The rest of this report reconstructs the model-specific application.

## Unique polymer representation

Take connected components separately within each species' occupied
unoriented charge-edge support, retaining every orientation. A component
is internally balanced because no incident edge of its species lies
outside that component. This decomposition is unique even when a
component branches. Decomposing into individual cycles instead would
not be unique and is not the proposed mapping.

Internal midpoint capacity is part of polymer validity. Between polymers,
incompatibility is exactly shared midpoint, or shared charge vertex
within the same species. The second rule is necessary for uniqueness;
it must not be imposed between different species. A compatible collection
reconstructs exactly one hard-capacity balanced configuration, so the
product activity is its original fugacity weight.

The independent checker exhibits a balanced ten-record component with
two different simple-cycle decompositions. It also exhibits two balanced
components with disjoint charge-vertex sets but a shared midpoint, which
must be forbidden, and a valid two-species pair sharing a charge vertex
with disjoint midpoints, which must be allowed. These target the two
distinct compatibility conditions.

## Counting and theorem hypotheses

For odd N>=7 the charge graph is simple of degree six, with unique
midpoint/axis representation of each unoriented edge. Its line graph has
degree ten. A deterministic depth-first traversal of a spanning tree
of a connected n-edge set, rooted at a specified edge, has length
2(n-1). Its visited vertices recover that edge set. This gives the
injection and the bound 10^(2n-2), without a missing spanning-tree
multiplicity. The signs add at most 2^n possibilities. Ignoring balance
and capacity is an overcount. Valid components have n>=4.

For each record of a fixed polymer, an incompatible polymer contains
either one of the eleven same-species edges incident to its two endpoints,
or one of the six typed axes/species at its midpoint. The exact union
has at most sixteen anchors here; seventeen is a valid conservative
bound. Each possible incompatibility is covered by at least one record
of the fixed polymer.

With enlarged activities |w|exp(n), a=n and q=200e^2 max|z_s|, the
anchored sum is at most q^4/[100(1-q)]. At z_star=1/(400e^2),
q=1/2 and this bound is 1/800. The incompatibility sum is thus bounded
by (17/800)n, strictly below a. The enlarged hard-core pair factor is
unchanged: it is -1 on incompatibility and zero otherwise.
Finite-volume polymer sets are finite, so both total-variation and
weighted integrability requirements hold. The theorem is not being
applied directly to an infinite translation-counting measure.

A new zero-mass root g_x is legitimate: the theorem's condition is
required for every point, including points of measure zero. Its own
condition is bounded by 6/800<1 with a(g_x)=1, and it contributes
nothing to any ordinary polymer's condition. The rooted equation (5)
then gives exactly

    sum_clusters |C| exp(M) R_x <= 1,

where M is total record size with occurrence multiplicity and R_x
counts polymer occurrences occupying x. No extra factorial or activity
of the ghost should be inserted. Repeated polymers in a connected
expansion are essential; they are not simultaneous physical records.

For a diagnostic, direct enumeration of connected graphs on up to five
repeated copies of one self-incompatible polymer gives coefficient
(-1)^(m-1)/m. The single root inserts m, and two source derivatives insert
m^2. They reproduce the Taylor series of w/(1+w)^2 for log(1+w exp(hx+hy)).
This checks precisely the normalization used in the proposed root bound.

## Two sources and the spatial estimate

A source for E_i(x) multiplies each activity by exp(h E_gamma,i(x)).
Because a compatible collection occupies x at most once, this is the
correct microscopic source. For two sources the derivative of a cluster
term is C times the product of the sums of these marks over occurrences,
whose absolute value is at most R_x R_y<=R_x M.

For differentiation it is enough to choose a complex neighborhood with
the sum of the two source moduli less than one, for example each below
1/4. The source deformation then costs less than exp(M); the remaining
exponential margin controls all derivative factors. The proof requires
a neighborhood of zero, not convergence for arbitrarily large sources.

Within a polymer, adjacent charge edges have midpoint distance at most
two. An incompatibility joins records at a common midpoint or records
incident to a common charge vertex. Therefore the record-occurrence
graph of a nonzero connected cluster is connected, and if it hits x,y,

    d_1(x,y)<=2(M-1)<=2M.

This holds for periodic distance and counts repeated record occurrences
as separate vertices when necessary. Consequently

    M exp(-M) <= (2/e) exp[-d_1(x,y)/4],

by maximizing M exp(-M/2). Multiplication by the rooted sum proves the
claimed component bound (2/e)exp[-d_1/4], for both E and B.

For general one-slot observables f,g, subtract their vacancy values and
put A_f=max_occupied |f(label)-f(vacancy)| and similarly A_g.
The precise general bound obtained is

    |Cov(f_x,g_y)| <= (2/e) A_f A_g exp[-d_1(x,y)/4].

The E/B components have A_f=A_g=1. Without normalization, the same
numerical prefactor cannot hold for all bounded observables: multiplying
a nonconstant site observable by an arbitrarily large finite scalar is
a direct counterexample. The primary phrase “same argument applies”
should be read with, or explicitly supplemented by, these norm factors.

## Periodic limit and vacant boundaries

An anchored cluster of total size M has record diameter at most 2M.
For M smaller than a fixed small multiple of N, it has a unique local
lift, with exactly the same activities and incompatibilities as on
the infinite lattice. Any inconsistent lift or noncontractible wrapping
requires M growing linearly in N.

The rooted estimate bounds tails after any finite number of local source
derivatives by a polynomial in M times exp(-M). For fixed finite-support
small sources, log Z(h)-log Z(0) uses only clusters intersecting that
support. A sum of its site roots supplies a volume-independent dominating
series. Thus the finite source generating functions converge, uniformly
in a neighborhood of zero, and their derivatives determine every finite
joint law. This is a precise version of the periodic thermodynamic
passage; it does not require finite-volume mixing.

For boxes with vacant exterior, use the ensemble of finite balanced edge
sets whose record midpoints are allowed inside the box, with the exterior
records fixed vacant and Gauss imposed also at adjacent charge vertices.
The polymer family is then a restriction of the infinite family; the same
tail/lift proof gives the same bulk local limit. If “vacant exterior”
instead allows unbalanced open edges by dropping exterior/boundary charge
constraints, that is a different specification requiring its own
boundary comparison. State this boundary convention explicitly.

For positive fugacities, noncontractible winding polymers have size at
least N. Their occurrence probability is at most their activity times a
partition-function ratio bounded by one. Summing with the anchored
exponential estimates gives a polynomial-volume factor times an
exponentially small factor in N. The finite winding covariance from
the previous sealed check is therefore compatible with the limit.

## Analytic Gauss and cubic consequence

The correlation bound gives an absolutely convergent Fourier transform
in a complex strip around the real momentum torus, including its
derivatives. The local Gauss constraint passes to the local limit and
gives S(k)s(k)=s(k)^T S(k)=0. At each centered-symbol zero k0, sin(k0+tv)
has derivative diag(cos(k0))v with invertible diagonal signs. Taking
t->0 along arbitrary v forces S(k0)=0.

Inversion symmetry makes S even; combined with covariance exchange
symmetry it is real symmetric on real k. Its first derivatives at zero
vanish. Full signed-cubic symmetry restricts the quadratic term to diagonal
a|k|^2+b k_i^2 and off-diagonal c k_i k_j. Transversality gives
b=c=-a, precisely a(|k|^2I-kk^T). Positive fugacities make the spectral
covariance positive semidefinite, hence a>=0. Cubic symmetry does not
assert full rotational invariance at higher orders.

The same rooted bounds hold uniformly for complex fugacities in the
stated polydisk and supply the uniform analyticity needed to pass the
quartic coefficients and the absence of degree five to the limit.
The leading coefficient on a fixed ray is therefore 8a0^4 epsilon^4
(or 8b0^4 epsilon^4), with O(epsilon^6). Strict positivity is justified
only for sufficiently small positive epsilon on a ray with the
corresponding species amplitude nonzero, as stated.

## Scope and provisional disposition

The result is for the full static grand ensemble, at positive real
fugacities in the sufficient domain. Complex fugacities are an analytic
tool, not probability laws. Winding sectors and count sectors are not
silently conditioned away. Nothing here implies ergodicity of the
physical loop generator or selection by irreversible formation.

For comparison, the equal mixture of the two fully occupied uniform
+A1 and -A1 states is stationary for the physical conservative moves,
is Gauss-free and has covariance one at every separation. It is not the
grand ensemble in the theorem. This directly prevents extending the
conclusion to arbitrary stationary Gauss-free laws. Births also do not
preserve the stated grand law. Outside the sufficient radius the
present majorant no longer supplies the theorem; that is not evidence
of either existence or absence of a high-density phase.

Provisional disposition: the load-bearing E/B proof is valid under its
stated finite-volume domain and the explicit infinite-volume construction
above. Clarify the observable norm factors and vacant-box convention for
the broader extension language. No missing theorem, sector-mixing
assumption or factorization hypothesis was needed for the periodic
E/B result.

The independent checker completed eleven groups. Its first run failed
because SymPy structural equality compared -(M-2)/2 with 1-M/2;
their simplified difference is zero. The exact first script and raw log
are preserved with a receipt, and the corrected run compares their
difference to zero. No scientific identity or constant was changed.
The external source and all provisional evidence are bound in
PRE_CHECKER_SEAL.json before primary checker/results access.
