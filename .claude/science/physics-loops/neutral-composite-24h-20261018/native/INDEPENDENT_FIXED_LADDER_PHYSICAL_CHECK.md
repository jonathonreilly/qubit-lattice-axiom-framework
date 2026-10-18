# Focused check: every fixed occupation, microscopic energy-window ladder

Read `/tmp/neutral_fixed_ladder_root.md`, native `TWO_FEATURE_LADDER_PROOF.md`, and `LOW_ENERGY_SOURCE_BOUND.md`. This is a scoped mathematical extension check, not a formal audit or a replay of all earlier normal-form inputs.

## Result and required amendment

The proposed extension is consistent for every fixed finite M, conditional on the previously established coefficient, ground, and low-energy-source lemmas. One explicit amendment is necessary: replace the two-rung cutoff ell<L/16 by an M-dependent cutoff, for example ell<L/(16M), before invoking ground-orbit disjointness. Without that change, arbitrary fixed M strings can cover an entire column under the old cutoff. All limits keep M fixed; no uniformity in M is established.

## 1. Host normalization and mixed source

With B_b†=(1/sqrt2) sum_ij Phi_ij a_i†a_j† and rho=Phi†Phi, the stated generating function

    sum_m ||B_b†^m vacuum||² t^m/(m!)²
      = det(1-2t rho)^(-1/2)

has the correct factors. Its logarithm is sum_(k>=1) 2^(k-1) Tr(rho^k)t^k/k. For fixed m the k=1 term gives m! w^m. Every other coefficient contains a k>=2 trace and is bounded by C_m Tr(rho²) when w stays bounded. This is a finite-coefficient identity; no analytic generating-function radius uniform in the limit is needed.

Hard-core projection exactly reproduces the spin-host state, since repeated-site creations are deleted with the same coefficients. In the ordered pair tensor expansion, two sites from distinct pair copies coincide with probability O_m(1/V) by uniform one-site marginals. Cauchy-Schwarz over the finite number of pair matchings gives a lost squared norm O_m(1/V); bosonic factorial occupation factors are also bounded by a constant depending only on m. Thus the spin-host squared norm is m! w^m+O_m(1/(V delta)).

Complex holomorphic polarization of the norm polynomial gives

    <BH^m vacuum, F BH^(m-1) vacuum>
      =m! w^(m-1) Tr(Phi†Xi)+O_m(||rho||).

The factor m from differentiating B^m cancels the derivative's m in the leading norm term. Higher trace derivatives are bounded by C_m ||rho|| times bounded Hilbert-Schmidt norms. The hard-core mixed correction follows by Cauchy-Schwarz on the discarded bosonic states. The source's translation-uniform marginal is needed here, and is available for the fixed local-root Fourier source; an arbitrary concentrated Xi would not justify the same O(1/V) statement. Even the weaker O_m(V^-1/2) is sufficient on the declared scaling.

## 2. Full strings, projection, and contact residual

For a union containing 2S occupied sites, an ordered decomposition into m two-column finite intervals has at most C_m S^(2m) choices: each factor chooses two among at most 2m occupied columns and its two endpoints among at most 2S occupied sites. This deliberately overcounts and covers host factors too. Weighted Cauchy-Schwarz converts it into moments of total length S. Conditional ray moments of all fixed orders, together with fixed m, bound the term with j ray factors by C_m eta^j.

One ray factor raises the physical flip count above the all-host value by at least two. Therefore the host-only contribution is orthogonal to every term containing rays, both for the norm and for the mixed matrix element with F, which adds exactly two flips. Remaining mixed ray terms have at least one ray on each side and cost O_m(eta²). It follows that

    ||B^m vacuum||²=m!+O_m(eta²+1/(V delta)),

and the unnormalized mixed vertex is m!a+O_m(eta²+1/(V delta)+V^-1/2). Dividing by sqrt(m!(m-1)!) yields sqrt(m)a with a relative error tending to zero.

For independent feature COM translates, a union bound over the fixed number of pairs makes proximity within any fixed microscopic interaction radius have probability <=C_m E[S^r]/V for an appropriate fixed r. Include incident z neighbors, not only overlapping down sites. The same polynomial decomposition count bounds the bad-N projection and the K_(4m) intertwining defect in norm by C_m/sqrt(V). Away from this contact set, native bond flips and the wall-number filters act on a single feature, so the sum of independent K4 actions is exact. Output-predecessor counting adds only a fixed polynomial in S; a native inverse flip must touch the finite occupied/wall neighborhoods in this fixed wall sector.

These statements establish a quasimode at mE, not a bound m-feature molecule. The explicit breakup/contact channel already checked elsewhere remains compatible with this dilute, volume-normalized residual.

The fixed-order Dj argument also extends: vacuum-subtracted terms missing all down sites annihilate; at most C_j S candidate neighborhoods remain, with bounded support growth. Polynomial weighted counts and fixed total-length moments yield O_(j,m)(1) norms. Constants may grow rapidly with j and m, which is harmless only because both are fixed.

## 3. Ground-orbit map and physical source

Use ell<L/(16M) (or a comparably safe cutoff) for each string, and retain the fixed-order support enlargement. Then differences of two m-string configurations, and their fixed-order residual supports, cannot cover an entire column for sufficiently large L. Distinct background-orbit images are orthogonal. Stabilizer characters remain those of the ground because every factor is layer-even. The prior plane-orbit construction therefore supplies isometries T_m simultaneously for m<=M, with source cross matrices scalar on the ground space. Exponential ray tails make the new cutoff error superpolynomial. A transverse cutoff, if used in the earlier construction, can likewise be tightened by an M-dependent constant without changing the limit.

The original grade +4 source differs from its vacuum all-lowering extension only near preexisting defects. Fixed m, local row/column counts and total-length moments retain the O_m(V^-1/2) bound. Bare C preserves N and cannot connect N=4(m-1) to N=4m. Higher dressed coefficients contribute O_m(lambda²). Thus the proposed adjacent unprojected vertex sqrt(m) lambda a[1+o(1)] follows; it does not assume the physical source equals its vacuum extension on the full excited Hilbert space.

## 4. Actual windows and low-energy norm

The low-energy-source lemma extends to any fixed cutoff larger than the largest center near 8MJ, with a further fixed buffer when comparing the exact and normal-form projectors. Its N bound n_* and all constants then depend on M. The proof's creation/annihilation Schur counts, zero-grade bad-plaquette bound, and exact-tail estimates remain valid for this fixed n_*. No cutoff uniform in growing M follows.

For the unprojected quasimodes, bounded N and bounded normal-form energy norm give the same O_M(lambda) source norm via the lemma's F decomposition. For exact window vectors the buffered low-energy projector gives O_M(lambda), including the adjoint. Consequently two single-error terms control an adjacent projected matrix element by O_M(lambda²/delta); one must not use the global source norm on a double projection error.

Window halfwidth J lambda delta/4 and O_M(J lambda²) residual give O_M(lambda/delta) projection loss. The finite collection of windows is disjoint for sufficiently small lambda. Normalized projected vectors, together with the actual ground vector, are orthonormal. Since a is of order sqrt(delta) log(1/delta), the relative vertex error is bounded by C_M lambda/[delta^(3/2) log(1/delta)], which vanishes for the declared alpha<2/3. Other algebra/contact errors also vanish relative to a under V~lambda^-12.

## Scope of the conclusion

With the cutoff amendment, this constructs actual microscopic energy-window vectors with additive window centers and adjacent original-source vertices in the ratio sqrt(m), for every preassigned fixed M. It supplies neither a common invariant ladder subspace nor exact eigenstates. Most source weight can remain outside the chosen ladder. Nonadjacent compressed-source claims need their own grading/momentum analysis; definite absolute momentum cannot be assumed for an arbitrary ground state. No full CCR, finite-density limit, stable particles, autonomous oscillator dynamics, or cosmological identification is established.
