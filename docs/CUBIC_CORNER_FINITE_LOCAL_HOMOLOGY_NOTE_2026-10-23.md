# Exact finite local homology for supplied cubic and corner complexes

**Type:** bounded_theorem
**Status:** conditional finite geometry certificate; no physical or audit status assigned
**Primary runner:** `scripts/cubic_corner_finite_local_homology_2026_10_23.py`
**Scope:** exact GF(2) subspace equalities for the finite complexes and box sizes below. An arbitrary-size one-collar theorem is not claimed.

## Supplied complexes and support

All chains and cochains have coefficients in GF(2). Let D be the six signed
coordinate unit vectors. The inner site box is B_r={0,...,r-1}^3; the outer
site box is U_r={-1,...,r}^3. Here “one collar” means precisely this finite
outer box. The inner edge set I contains edges with both endpoint sites in
B_r. Every calculation below uses all outer edges and all outer cells.

The cubic complex has one vertex per site, nearest-neighbor edges, and
coordinate unit-square faces. The supplied corner complex has vertices
(v,{d,e}) for d,e in D with d dot e=0 (12 vertices per site). Onsite edges
join {d,e} to {d,f} when e dot f=0. An intersite link joins (v,{d,e}) to
(v+d,{-d,e}). Onsite faces are the six squares obtained by fixing d and
cycling the four perpendicular directions, and the eight triangles formed
by choosing one signed direction on each axis. For each lattice edge there
are four tube rectangles between its four intersite links. For each cubic
plaquette there is the four-link face following its four successive corner
vertices. Only cells whose vertices lie on outer sites are kept. The author
builder includes each tube rectangle twice; duplicate GF(2) rows do not
change a span. This is a chosen finite cell complex, not a derived physical
lattice or Hilbert space.

## Exact finite claims

Let C_I be the subspace of outer edge vectors supported in I. Let d1 map
edges to their two endpoints and d2 map faces to their edge boundaries.
For cubic r=1,2,3,4,5 and corner r=1,2,3,4 the runner establishes

    ker(d1) intersect C_I = im(d2) intersect C_I,
    ker(d2^T) intersect C_I = im(d1^T) intersect C_I.

Thus every inner-supported cycle is the boundary of a chain of outer faces,
and every inner-supported cochain closed on every outer face is the
coboundary of some potential on outer vertices. This exhausts each finite
vector space; it is not sampling individual cycles. The potential statement
is **inside the finite outer graph**. Extending a potential by zero outside
U_r may introduce values on crossing edges; no infinite-lattice compact
support conclusion is inferred here.

The exact dimensions (cycle space = filled subspace; closed cochains =
coboundaries) are:

| Complex | r | cycles / filled | closed / coboundaries |
|---|---:|---:|---:|
| cubic | 1 | 0 | 0 |
| cubic | 2 | 5 | 0 |
| cubic | 3 | 28 | 1 |
| cubic | 4 | 81 | 8 |
| cubic | 5 | 176 | 27 |
| corner | 1 | 13 | 0 |
| corner | 2 | 145 | 24 |
| corner | 3 | 541 | 144 |
| corner | 4 | 1345 | 432 |

Separately, for the periodic cubic and corner complexes at L=3 and4, the
runner checks connectivity and computes dim H_1=3. Coordinates are reduced
modulo L. Builders explicitly reject L<3; only L=3,4 are certified here.
This is geometry alone: it does not fix a stabilizer code's logical count,
frustration-freeness, ground-state degeneracy or excitation statistics.

## Why the finite calculation is a certificate

The primary explicitly checks valid edge endpoints, face-edge incidence,
and d1*d2=0. Therefore boundaries are cycles and coboundaries are closed;
these inclusions are prerequisites for concluding equality from dimensions.
For any subspace S of edge vectors, restriction to outside I has kernel
S intersect C_I, so

    dim(S intersect C_I) = dim S - rank(restriction_outside on S).

The runner applies this identity to face-boundary and vertex-coboundary
spans using exact integer-bitset Gaussian elimination over GF(2). Inner
cycle dimension is |E_I|-|V_I|+components, with components obtained by
union-find. Isolated vertices omitted from V_I contribute equally to the
vertex and component counts and hence do not affect the cycle dimension.
Closed supported cochain dimension is |I|-rank(face rows restricted to I).
On each connected torus the homology dimension is |E|-(|V|-1)-rank(d2).
No floating-point tolerance enters these rank equalities.

The negative control removes all faces from the cubic r=2 outer complex
and detects a positive unfilled-cycle defect using the same analysis code.
A malformed one-edge face is rejected because its vertex boundary is
nonzero. Both builders reject the formerly unsupported L=2 torus input.
A failing check returns nonzero; optimized Python is rejected so structural
checks cannot disappear. The historical finite predicates and arithmetic
are preserved, with explicit validation added.

## General-size route and deferred obligations

The original C6 argument proposes tube sliding, filling the resulting cubic
cycle, and filling the remaining onsite cycles on the cuboctahedral sphere.
Its cochain argument integrates along paths from an exterior base point.
Those are useful proposed extensions. This canonical finite unit does not
certify all sizes: an explicit support-controlled cubic contraction, every
boundary move, path independence, connected-exterior gauge choice and
zero-extension across outer boundary edges must be established together
before claiming the infinite-lattice one-collar potential theorem.

No Pauli code theorem, logical count, general-L frustration-freeness,
Hamiltonian stability, physical fermion, photon exclusion or new primitive
is supplied. The original broader code and negative claims remain deferred.
The exact original C6 NOTE, primary, library, review and logs are recoverable
at commit `e294c1dc745dad0c95b4c8688efc6f3f0be03613` under
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C6/`.
Historical review using a separate cell builder is preserved as evidence,
not represented as a new independent review of this extraction.
