# Independent reconstruction before author-control access

Primary note: `DIMER_ROUTED_DIFFUSIVE_GAP_COMPARISON.md`, SHA-256
`1d9f7929c5600c6e097913ab2459f351857431c7f3035d4a80bc497f9d732124`.
The entire note was read. The prior complete-permutation Poincare proof, count
mixture preparation transfer and corrected moving-history estimate are reused
at the identities in `PRE_COMPARISON_SOURCES.json`. No author diffusive checker,
result or log, dynamic aggregate or finite-wavelength follow-up was opened.

Provisional finding: the constants and hypotheses reconstruct; no correction is
identified before comparison. This is a bounded scientific check, not an audit.

## 1. Physical path count

For even N, a one-dimensional displacement r has length min(r,N-r), with the
N/2 tie routed positively. Summing over the N displacements gives

    2 sum_{r=1}^{N/2-1} r + N/2 = N^2/4.

The tie choice is translation covariant. Summing over all N starts therefore
produces N^3/4 traversals, distributed equally over N undirected cyclic edges:
N^2/4 paths per edge. No path repeats an edge. Positively tied paths do not give
equal directed loads, but only the undirected count is claimed and used.

In a three-coordinate dimension-order route, a fixed i-edge fixes the target
coordinates before i and the source coordinates after i. For each of the other
two coordinates the other endpoint coordinate is free. Multiplying by N^2 gives
the exact undirected count N^4/4. This is consistent with summing all lengths:
there are N^6 ordered pairs, mean length 3N/4, and 3N^3 physical edges.

Selecting one lexicographically oriented black-endpoint route for each unordered
pair of dimers is literally a subset of this ordered family. Its load on every
physical edge is no larger. It is not necessary to assume equal loads in the
selected subset, reverse-route symmetry, a homogeneous matching or independence
of matching geometry from endpoints.

## 2. Contraction and actual channel multiplicity

Map physical vertices to their matched dimers. Each physical path becomes a
contracted walk; matching edges are consecutive repetitions. Deleting a closed
subwalk at a repeated vertex adds no edge: the surviving outgoing edge already
left its later occurrence. Thus chronological loop erasure preserves endpoints,
cannot lengthen the path and leaves only edges traversed by the original path.

For these particular routes, there is an additional harmless simplification:
they are geodesics in the physical torus. Every subpath of a geodesic is a
geodesic. If both endpoints of one dimer occur along it, their separation along
the route must therefore be one. Consequently, after consecutive contractions,
nonconsecutive loops cannot occur. The author's loop-erasure step remains valid
and does not weaken the estimate; our inventories accordingly find zero such
erasures even for irregular matchings. The proof does not depend on that extra
observation.

N is even and the physical torus is simple. A dimer has exactly one black and
one white endpoint. Between two distinct dimers, the only possible physical
edges are the two cross-parity connections. Hence each simple edge e of H_M has
at most two physical representatives. Every selected simple path using e can
be charged to at least one traversal of one of those representatives in its
original path. Summing these nonnegative incidences yields

    contracted_path_load(e) <= sum_{physical f representing e} subset_load(f)
                            <= 2 (N^4/4) = N^4/2.

Neither choosing a representative injectively nor omitting duplicate physical
generator channels is required. The original torus is connected, so its
contraction H_M is connected. The inherited physical routed process contains
each such channel and its symmetric transposition rate is k0/2 per channel.
The simple-graph form is a lower bound on that actual form, not a replacement
of the generator by a deduplicated one.

## 3. Endpoint words and forms

On a simple path x0,...,x_l, swap edges forward, then backward omitting the last
edge: (01),(12),...,(l-1,l),(l-2,l-1),...,(01). There are 2l-1 moves. The last
edge appears once and every earlier edge twice. The composition transposes the
endpoint keys and restores all intermediate keys. In the supplied model these
are legal exchanges of complete immutable pairs, by the already checked routed
construction. They preserve geometry throughout.

Since l<=3N/2, each word has length at most 3N-1. Its edge-use count across all
unordered endpoint pairs is at most twice the contracted path load, hence N^4.
For one endpoint word, telescope f along its successive configurations and use
Cauchy-Schwarz with its length. At each step the preceding key permutation is
a measure-preserving bijection of the uniform color-count sector. Therefore
the step's expected squared increment is exactly that for the corresponding
edge applied at a fresh uniform configuration. With

    D_all = (1/2) sum_{unordered endpoint pairs} E[(Delta f)^2],
    D_H   = (1/2) sum_{simple H edges} E[(Delta_e f)^2],

the factors 1/2 agree on both sides. The comparison is

    D_all <= (3N-1) N^4 D_H.

Using only the previously proved sufficient inequality Var<=2 D_all/K gives

    Var <= (2/K)(3N-1)N^4 D_H = 4N(3N-1)D_H.

Since D_S >= (k0/2) D_H,

    Var <= [8N(3N-1)/k0] D_S,
    gap(S) >= k0/[8N(3N-1)].

This establishes the displayed all-count-sector bound. Same-color exchanges
have zero increment and do not affect the argument. Singleton sectors have
zero variance. Uniformity in M follows from the physical congestion argument,
not from a finite inventory or an assumption about typical matchings. The
condition k0>|gamma| and the inherited rate normalization must remain in force.

## 4. Nonreversible preparation and law transfer

For a density f_t with respect to a uniform count-sector law, the forward
density generator is the stationary adjoint. Its symmetric form is still D_S:

    d/dt ||f_t-1||_2^2 = -2 D_S(f_t-1)
                       <= -2 g'_N ||f_t-1||_2^2.

This uses density, not square-root density. It does not require reversibility.
From any point mass, ||f_0-1||_2=sqrt(|Omega|-1); convexity extends the maximum
to any entrance law. Total variation is at most half the L2 norm. The number
of color configurations in a fixed count sector is bounded by 14^K, so

    TV <= (1/2)14^(K/2) exp(-g'_N t).

For the inherited range 0<epsilon<1/2, substitution of the new t'_prep makes
this at most epsilon. At epsilon_N=N^-4 the exact expression is

    k0 t'_prep = (6N^5-2N^4) log14
                 + 8N(3N-1)(4 log N-log2).

Thus the leading coefficient is 6 log14/k0 and the sufficient order is N^5.
This is a conservative total-variation schedule; it does not show that a real
mixing time is asymptotic to it, nor prove an optimal gap coefficient.

The earlier strong-Markov transfer and independent multinomial count mixture
need no new argument once the same uniform sector bound is available. At random
completion the arrangement may depend arbitrarily on the preceding history;
the sector estimate is uniform in that arrangement. The geometry/count
independence is still a required formation premise. Total variation contracts
under the common subsequent path kernel. The field residual squared is bounded
by C K, so epsilon_N=N^-4 contributes C K epsilon_N=C/(2N). The random time
to reach full packing is additional and is not bounded uniformly in volume.

For moving autonomous geometry, the already checked history conditioning makes
the color generator a succession of common-invariant interval semigroups and
boundary permutations. The new gap bound is uniform in every interval; boundary
permutations are L2 isometries. Multiplying contractions gives the same elapsed
time bound. No equilibrium or mixing assumption on geometry is introduced. The
reference geometry law is its law at the end of preparation, as in that checked
extension. This use remains conditional on its model hypotheses; fixed-geometry
Sections 1-3 do not need the moving result.

## 5. Independent finite controls and scope

`independent_check.py` imports no author checker. Its first execution completed
with exit zero and empty stderr. `INDEPENDENT_RESULTS.json` was read completely.

All 262,144 ordered physical paths at N=8 and all 1,000,000 at N=10 were counted
directly, including ties, wraparound and zero-length paths. Every physical edge
has exactly 1024 and 2500 paths, respectively. The total traversals are 1,572,864
and 7,500,000.

For each size, separately constructed winding, columnar and irregular matchings
check every unordered black-endpoint route: 32,640 per N=8 matching and 124,750
per N=10 matching. Every projected path has the intended endpoints and only
originally traversed edges. Every endpoint word was applied to distinguishable
keys and restores its intermediates. Multiplicities reach two in columnar and
irregular cases; treating H_M as if it had only one physical representative
would not match the inventory.

The maximal length-weighted word congestions are 5191, 9693 and 10167 at N=8,
and 15976, 30663 and 32539 at N=10, below the displayed conservative bounds
94208 and 290000. The irregular N=8 matching attains path length 12 and word
length 23, testing the stated worst length 3N-1. Every edgewise charging
inequality, not only its maximum, was checked.

Numerical one-marker-sector gaps of both the simple-edge lower comparison and
the physical-multiplicity symmetric graph lie above the derived conservative
bounds. These floating eigenvalues do not establish the all-sector theorem.
Two independent small multicolor sectors (six and 30 configurations) separately
check the exact Fraction-valued variance, complete form and endpoint-word
normalizations for nonlinear test functions. They are permutation controls,
not substitutions of an undersized torus for the stated geometry.

Exact integer coefficients and rational K epsilon_N were checked at five sizes;
the exponential TV substitution was evaluated numerically in logarithmic form.
All outputs distinguish exact integer/Fraction statements from floating checks.
No attempt failed and no counterexample within the stated hypotheses was found.
The proof concerns this finite torus geometry and supplied local color dynamics;
it does not import a sharp interchange theorem, a general-graph diffusive bound,
a quantum preparation or a volume-uniform filling-time statement.
