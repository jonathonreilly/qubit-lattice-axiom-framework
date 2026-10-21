<!-- Original SHA256 37df775aa35e15bd4bd631f2d8ce44956e8235528f10827ba5298d32989077a0 -->
**Provenance boundary:** Complete original source follows. Historical review labels and execution narratives are provenance, not fresh verification or current audit authority. Mathematical arguments retain their explicit hypotheses.

# Independent proof/check: actual-Z3 nodal persistence for every finite excitation number

2026-10-18. Root proposed the coordinate-antisymmetry mechanism. This is a separate analytical reconstruction and fresh exact computational implementation, performed without reading root's new `infinite_two_root_check.py` or its results. Shared task/model context and exposure to the proposed mechanism are explicit. No audit, historical novelty or physical phase-selection claim is made. No repository publication source was edited.

**Finding:** the proposed n=2 construction is correct, and its extension to every fixed finite n is correct with the normalization and domain specified below. The actual full homogeneous positive Heisenberg generator exactly intertwines with the free ordered-coordinate operator on these closed subspaces. The proof removes periodic geometry and the one/two-only restriction for this prepared persistence interface. It does not remove correlated preparation, selected Hamiltonian/background, Record formation/readout or generic finite-density restrictions.

## 1. Actual physical generator and ordered comparison

Use precisely the polarized-vacuum representation and physical operator from the checked `INFINITE_LATTICE_PROBE.md`:

    H=2j sum_{nearest-neighbour bonds}(I-SWAP), j>0.

The n-excitation physical Hilbert space is K_n=l2(X_n), where X_n is the set of unordered n-element subsets S of Z3. On it H_n=2j L_config. Its degree is

    deg(S)=6n-2 a(S),

where a(S) counts nearest-neighbour pairs contained in S. Each occupied site has six incident edges; an occupied–occupied edge contributes two to that count but no possible move. The graph Laplacian has one off-diagonal -1 for each allowed move. As previously checked, H_n is bounded self-adjoint positive and ||H_n||<=24jn. The vacuum block is0.

The comparison Hilbert space is the ordered l2((Z3)^n), with

    F_n=2j sum_(i=1)^n L_Z3^(i), ||F_n||<=24jn.          (1)

This ordered tensor product is an encoding coordinate space, not additional physical particles or qubits. Its diagonal is12jn and each ordered nearest-neighbour hop has amplitude-2j. The physical diagonal is2j[6n-2a(S)], so the difference on collision-free configurations is -4j a(S). This factor and sign are load-bearing.

## 2. Closed code and all relevant symmetries

Let h=l2(Z), and let h_odd={u:u(-x)=-u(x)}. Reorder the ordered coordinates unitarily as

    l2((Z3)^n) = l2(Z_x^n) tensor l2(Z_y^n) tensor l2(Z_z^n).

Inside that space take the concrete closed tensor subspace

    C_n=(wedge^n h_odd) tensor (wedge^n h)
                                      tensor (Sym^n h). (2)

Here wedge and symmetric powers are their standard normalized subspaces of h^tensor n, not unnormalized exterior symbols. Equivalently C_n is the common range of bounded orthogonal antisymmetrizers in x and y, the symmetrizer in z, and the product of individual x-odd projections. The x antisymmetrizer commutes with that product, so the definition is consistent and closed. Define C_0=C.

A simultaneous permutation of the n complete particle coordinates has sign(sigma) from x, sign(sigma) from y and1 from z. Their product is1. Every f in C_n is therefore a physically symmetric ordered amplitude. This does not assert antisymmetric statistics for the physical qubit excitations.

The x and y antisymmetries respectively imply

    f=0 whenever x_i=x_k or y_i=y_k, i!=k.              (3)

For l2 on a discrete lattice these statements hold pointwise: coordinate evaluations are continuous, and the equal-coordinate swap leaves an argument unchanged while reversing its amplitude. Individual x oddness also gives

    f=0 whenever any x_i=0.                            (4)

Every collision has repeated x and y. Every nearest-neighbour pair shares x or y: an x-direction edge has equal y, a y-direction edge has equal x, and a z-direction edge has both. Hence (3) kills every collision and every configuration with a nearest-neighbour occupied pair.

Each one-dimensional Laplacian commutes with reflection. The sum of its n coordinate copies commutes with all permutations in that coordinate. Therefore F_n commutes with all the projections defining (2), and C_n is reducing for F_n. In particular F_n f and exp(-itF_n)f satisfy (3)–(4) whenever f does. Merely having these zeros at time0 would not suffice; this exact reducing-space statement supplies their persistence.

## 3. Normalized physical embedding and exact intertwining

For f in C_n and an unordered set S={r_1,...,r_n}, define

    (B_n f)(S)=sqrt(n!) f(r_1,...,r_n).                 (5)

Physical exchange symmetry makes this independent of enumeration. Because f vanishes on all collisions, each unordered configuration has exactly n! ordered representatives and

    ||f||^2 = n! sum_(S in X_n)|f(r_1,...,r_n)|^2
             = ||B_n f||^2.

Thus B_n is an isometry with closed range. The factor is sqrt(n!), not n!,1/sqrt(n!), or1. At n=2 it is sqrt2 as proposed. B_0 sends1 to the polarized vacuum.

For a collision-free ordered tuple representing S, the off-diagonal free moves to collision-free tuples correspond one-to-one to actual occupied-to-empty moves. Terms whose destination has a collision vanish because f does. Comparing diagonals gives pointwise

    (H_n B_n f)(S)
      =sqrt(n!) (F_n f)(r_1,...,r_n)
                          -4j a(S)(B_n f)(S).          (6)

The second term is zero because f vanishes wherever a(S)>0. The first term is B_n F_n f because C_n is reducing, so F_n f is again collision-free and physically symmetric. Consequently

    H_n B_n = B_n (F_n restricted to C_n).              (7)

Every operator at fixed n is bounded, and the coordinate calculation is valid throughout l2. Equivalently it can first be verified on finite-support code vectors and then extended by boundedness. The code has dense finite-support vectors: truncate all coordinates in reflection-symmetric finite boxes, which commutes with the symmetry projections, and approximate there.

Equation (7) includes the outputs on adjacent configurations, where both sides vanish by preserved coordinate symmetry. It is not an agreement only on an arbitrarily deleted set of sites or on the initial support. It follows that ran B_n is reducing for the physical self-adjoint H_n and

    exp(-itH_n) B_n = B_n exp(-it F_n|C_n)               (8)

for every real t. No physical collision projection or additional penalty is imposed during evolution.

## 4. Plane purity, full outputs and passive references

Equation (4) implies that no physical configuration in ran B_n has an occupied site on x=0. Every finite product of local projectors onto q on that plane acts identically on ran B_n. Equation (8) preserves that fact at all times.

For an arbitrary encoded density operator, including arbitrary entanglement with a passive reference, extend B_n and (8) by identity on the reference. Every finite plane-site reduced state is exactly the pure product q, and hence factors from the rest and the reference. This is full physical output equality; no mirror packet, excitation, coordinate sector or apparatus is discarded. It supplies the same operational meaning of infinite-plane purity as the previously checked one-excitation result.

If these initial q rays are additionally supplied as law-admissible Records, (8) proves their persistence in the encoded sector. It does not derive that initial physical identification, formation or admissibility.

## 5. Nonzero and genuinely moving codes for every finite n

There are arbitrarily many orthonormal odd x vectors. One explicit choice is

    u_k=(delta_k-delta_(-k))/sqrt2, k=1,...,n.

Choose y vectors delta_0,...,delta_(n-1), and z vector delta_0^tensor n. Their normalized x and y Slater determinants, tensored with the symmetric z product, define a unit vector f_n in C_n. It has finite spatial support.

Its ordered support has 2^n(n!)^2 points, with coefficient magnitude1/(2^(n/2)n!). Under (5), physical support has2^n n! unordered configurations, with coefficient magnitude1/sqrt(2^n n!). These counts also verify the embedding normalization directly for this family.

The free z part of F_n sends a nonzero component to tuples with one z coordinate equal+1 or-1 and all others0. The x/y terms preserve every z=0 and cannot cancel those components. Thus F_n f_n is not proportional to f_n, and the physical encoded state has genuine nonstationary motion for every n>=1. The effective restricted dynamics remains free in the ordered-coordinate description; this does not derive interacting matter or generic many-particle protection.

## 6. Direct sums, domain and infinite-particle-number superpositions

Let C=direct sum_(n>=0) C_n and B=direct sum B_n. B is an isometry into the existing polarized-vacuum physical Hilbert space. Define

    F=direct sum F_n|C_n,
    D(F)={f:sum_n ||F_n f_n||^2<infinity}.               (9)

The same blockwise-resolvent argument used for H makes F positive self-adjoint. Equation (7) implies B maps D(F) into D(H), HB=BF there, and conversely Bf in D(H) exactly when f in D(F). Sectorwise unitary identities sum to

    exp(-itH)B=B exp(-itF)                              (10)

for every f in C, whether or not f lies in D(F). Plane projectors are bounded and act identically on every sector, hence on the full direct-sum code and its passive-reference extension.

Every fixed-n encoded state has finite energy and second energy moment, bounded by24jn and its square. An arbitrary superposition over unbounded n need not have finite energy; (9) states the actual operator domain. A sufficient condition for D(F) is sum n^2||f_n||^2<infinity, but that sufficient condition need not equal the exact domain. No arbitrary thermal representation, finite-density state or infinite occupied configuration is claimed.

The actual model is the positive vacuum-zero bond sum. An unshifted infinite Heisenberg sum has divergent vacuum energy and is not assigned a finite global scalar or absolute phase by this construction.

## 7. Fresh exact controls and limits of independence

`infinite_many_independent_check.py` was authored here before inspecting root's new two-particle implementation. It constructs ordered integer Slater-product seed amplitudes and separately applies:

1. the free ordered generator, with diagonal12n and coefficient-2 on each one-coordinate hop;
2. the actual unordered spin-exchange generator, with one occupied-to-empty move per physical bond and coefficient2(I-SWAP).

It checks full equality of the resulting ordered/unordered amplitudes, all coordinate symmetries, individual x oddness, absence of adjacent/colliding configurations, plane purity and factorial normalization through H^2 for n=1,2,3. It also verifies nonzero z motion. No periodic box or boundary truncation is used: all neighbours of every supported physical configuration are generated on actual Z3.

Saved exact support sizes:

| n | Ordered seed norm squared | Physical integer seed norm squared | Physical supports at powers0,1,2 |
|---|---:|---:|---|
|1|2|2|2,12,38|
|2|16|8|8,64,296|
|3|288|48|48,480,2640|

All identities were satisfied. The saved file `infinite_many_independent_result.json` records the outputs. These are distinct implementation controls with mechanism exposure and common research context; they do not prove the all-n or all-time claims without sections1–6. No generic robustness or native preparation test was performed.

## 8. Scope and next decision

The mechanism succeeds because two coordinate antisymmetries make the physical amplitude symmetric while imposing stronger zeros than hard-core exclusion. One antisymmetry alone would give an antisymmetric physical amplitude unless another factor compensates it. Symmetry without both necessary zero structures need not kill adjacent-pair terms. The retained generic two-excitation parity and adjacent-singlet counterexamples remain valid for those other preparations.

The result can replace finite periodic geometry and fixed low excitation count for this **specially correlated finite-excitation persistence code**. It does not make arbitrary initial excitations load into that code. It uses no new Hamiltonian terms and requires no protection gap, but a gap/robustness theorem against perturbations is not established. The main open supplier is a preparation or loading map producing these coordinate-correlated inputs under a selected native law. No theorem establishes arbitrary density, formation, empirical readout, an operational universal gate or complete TOE closure.

## Source and evidence identities

- `INFINITE_LATTICE_PROBE.md` SHA256 `d85f00866d575e03486ed876f0694b28e7f723f6d228ab3e2cf7854f2ddef1b0`.
- `INFINITE_CHECK.md` SHA256 `3518afc688da1f9003fb509f027bfe4b1e8b007008dc5eb1c27dd89536e0d91a`.
- `infinite_many_independent_check.py` SHA256 `c848fff9ae0f24fa27c21d02b0951c27fefe31e5a59b8a59b92b02c8fcfea986`.
- `infinite_many_independent_result.json` SHA256 `2d8b121da80714f1b4461fb9c2bb930dbb1407e72d40b9dffb020f23984faf6e`.
