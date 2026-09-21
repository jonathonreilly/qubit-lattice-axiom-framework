# A diffusive comparison bound for record-color preparation

2026-09-21. Root conditional proof candidate; independent check pending.
This strengthens the earlier polynomial preparation estimate by using the
geometry of the torus instead of the worst possible connected graph. The
earlier note and its sealed check remain unchanged and valid. No sharp
interchange-process theorem is imported.

## 1. Statement and unchanged premises

Let N>=8 be even, K=N^3/2, and let M be any perfect nearest-neighbor matching
of the cubic torus. Let H_M be the simple graph obtained by contracting each
matched pair. Use the same immutable pair exchanges with k0>|gamma|. The
uniform measure in each color-count sector is invariant, and its symmetric
generator S_M has rate at least k0/2 on every edge of H_M.

The following stronger uniform Poincare bound holds:

    Var_mu(f) <= [8 N(3N-1)/k0] D_SM(f),
    gap(S_M) >= g'_N := k0/[8 N(3N-1)].                    (1)

Singleton count sectors have zero variance and satisfy the inequality
trivially. This is a lower bound on the symmetric spectral gap, not a
diagonalization of the nonreversible generator or a sharp gap assertion.
It is uniform over the matching and conserved color counts.

The sufficient post-completion waiting time can therefore be replaced by

    t'_prep(N,epsilon) = (8 N(3N-1)/k0)
                         [ (K/2) log 14 + log(1/(2epsilon)) ].       (2)

For epsilon_N=N^-4 this is O(N^5/k0), with leading coefficient
6 log(14)/k0. It remains a deliberately conservative sufficient time, not
a measured relaxation time or a lower bound. The random completion time is
still additional and has no volume-uniform upper bound here.

## 2. Physical torus paths and their congestion

For every ordered pair of physical vertices (x,y), use this deterministic
nearest-neighbor path. Move coordinates 1, then 2, then 3. In each cyclic
coordinate use the shortest displacement; for the tie N/2 choose the
positive direction. The path has length at most 3N/2 and is translation
covariant. Every coordinate segment visits any undirected edge at most
once.

Fix an undirected physical edge e in coordinate direction i. The total
number of these ordered reference paths using e is exactly

    N^4/4.                                                (3)

To count it, in one cyclic coordinate the sum of the shortest distances
over all target displacements from a fixed start is

    2 sum_(r=1)^(N/2-1) r + N/2 = N^2/4.

Summing over N starts gives N^3/4 total one-dimensional edge traversals.
Translation covariance makes every one of the N undirected cyclic edges
carry N^2/4 paths. For an edge in the three-dimensional coordinate-i
segment, the other two coordinates each leave one freely chosen endpoint
coordinate; their multiplicity is N^2. This proves (3), including the tie
convention. Count actual path use, not just endpoint distance.

For each unordered pair of matched dimers, take their black endpoints u,v,
choose a fixed lexicographic order and use the corresponding physical path
u to v above. This is a subset of the ordered all-vertex path family, so
its load on each physical edge is at most (3).

Project each path to H_M by replacing a physical vertex by its matched pair,
discard consecutive repetitions and erase loops chronologically. The result
is a simple path between the specified dimers, still of length at most
3N/2. Every remaining contracted edge was traversed by the original physical
path; loop erasure adds no new edge.

Any two distinct matched dimers have at most two nonmatching physical
nearest-neighbor edges between them. Each dimer has one black and one white
endpoint, and a nearest-neighbor edge connects opposite parity. The only
candidates are black(u)-white(v) and black(v)-white(u). Therefore the number
of these projected reference paths using a fixed simple edge of H_M is at
most

    2 (N^4/4) = N^4/2.                                   (4)

This count remains valid for arbitrarily irregular M. It does not require a
periodic matching, a mixing law on matchings, or a favorable typical geometry.

## 3. Endpoint transpositions and the Dirichlet constant

Let D_all be the complete-graph unit-rate transposition Dirichlet form and
D_H the unit-rate simple-edge transposition form on H_M, both with the
convention D=(1/2) sum_edges E_mu[(Delta_e f)^2]. The earlier independently
checked elementary permutation argument gives

    Var_mu(f) <= (2/K) D_all(f).                          (5)

It applies to every color-count sector by equal-size distinct-label fibers.

An endpoint transposition along a simple path of length ell is realized by
the forward edge word followed by its reverse with the last edge omitted.
It has length 2ell-1<=3N-1, each path edge occurs at most twice, and every
intermediate immutable key returns to its original position. From (4), the
total word-use count of any H_M edge over all unordered reference pairs is
at most N^4. Telescoping, Cauchy--Schwarz and invariance of the uniform sector
under each preceding swap then give

    D_all <= (3N-1) N^4 D_H,
    Var_mu(f) <= (2/K)(3N-1) N^4 D_H
               = 4N(3N-1) D_H.                           (6)

The actual symmetric form dominates (k0/2)D_H. Substitution into (6) gives
(1). All channel multiplicities can only improve this lower bound; no
deduplication of the physical generator is performed.

## 4. Preparation and moving geometry

The earlier density-energy identity now yields

    TV(law_t, uniform count sector)
       <= (1/2) sqrt(|Omega_counts|-1) exp(-g'_N t)
       <= (1/2) 14^(K/2) exp(-g'_N t).                    (7)

Equation (2) makes the last expression epsilon. The argument uses the
symmetric form of the adjoint density generator and does not assume
reversible routed dynamics.

At first completion, the stated formation construction gives multinomial
counts independently of the autonomous geometry. The same strong-Markov,
count-mixture and total-variation arguments as in the earlier preparation
note apply with (2). The mean-square transfer error is still bounded by
C K epsilon_N = C/(2N) for epsilon_N=N^-4.

If the moving-geometry extension is accepted, its proof also applies with
g'_N. Conditioned on a complete marked autonomous geometry history, every
between-jump color semigroup contracts at this common rate, and each
prescribed boundary color permutation is an L2 isometry. Multiplying these
contractions gives (7) in elapsed time even while geometry moves. No
geometric equilibrium or clock freezing is used for this conclusion.

The moving-geometry statement retains that extension as an explicit open
dependency until its separate check is complete. The fixed-geometry
comparison (1)-(7) does not depend on the moving-geometry proof.

## 5. Limits and finite checks

Finite controls should count the ordered physical path loads, project the
black-endpoint paths for winding, columnar and irregular matchings, verify
loop erasure and immutable endpoint words, and check the constants on
independent finite color sectors. The proof above supplies all-volume
uniformity; a finite graph inventory does not supply that inference.

No logarithmic Sobolev theorem, sharp color mixing time, empty-start filling
estimate, physical time calibration, quantum preparation or TOE result is
asserted. This is a better explicit preparation schedule for the same
supplied local classical dynamics and its conditional color-wave theorem.
