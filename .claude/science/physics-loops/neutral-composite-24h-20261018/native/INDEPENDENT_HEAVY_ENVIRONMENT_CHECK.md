# Native heavy-defect environment and loop fluctuation check

Focused independent algebraic check of the proposed fixed-transverse-size weak-lambda route. Native longitudinal period is four, lambda>0, and transverse periods are large enough to avoid duplicated edge/plaquette conventions. Background spins s_(x,y) denote aligned physical Z columns. This report does not identify a gravitational coupling.

## 1. N2 first-order graph and its signs

A single flipped spin at one z layer relative to an aligned-column background carries two longitudinal walls. An XX bond from the defect column i to an unflipped neighbor j moves the defect with Hamiltonian matrix element -Jlambda. For YY the two input spins are -s_i and s_j, giving Hamiltonian matrix element -Jlambda s_i s_j. After removing Jlambda, the hopping entries are therefore -1 on x links and -s_i s_j on y links, as proposed.

Other transverse flips cannot remain in the singleton N2 sector unless they move this defect in the same layer. The z-plane parity pattern fixes that layer. The length-three interval is the same singleton configuration described relative to the opposite majority-column background and must not be counted as an independent duplicate. A half-column interval of length two cannot move or change its occupied column with one transverse two-spin insertion while remaining N2. Its first-order block is zero. Thus the singleton branch reaching coefficient energy -4 lies below those static first-order blocks for lambda>0.

## 2. Exact minimum and background selection

Let eta_ij be the link sign, so hopping is -eta_ij. On the degree-four periodic graph,

    <psi,(Hhop+4)psi>=sum_edges |psi_i-eta_ij psi_j|².

This proves min spectrum >=-4. Equality requires psi_j=eta_ij psi_i on every edge. Connectedness then makes all magnitudes equal and makes every cycle flux +1; a zero amplitude cannot evade the condition because it would propagate to all sites.

The elementary plaquette flux is exactly product_(four corners) s=P_p. x Wilson loops are trivially +1. A y Wilson loop telescopes product_y s_(x,y)s_(x,y+1)=+1. Thus all elementary P_p=+1 are necessary and sufficient for equality. Flat patterns have s_(x,y)=a_x b_y, and the normalized ground wave is psi_(x,y)=b_y/sqrt(N), up to a common phase. This satisfies every signed link equation directly.

For fixed R there are finitely many backgrounds; all nonflat blocks have a strictly higher minimum than -4. Hence the first-order N2 ground selection favors flat backgrounds. No R-uniform gap to nonflat backgrounds is asserted. Subsequent terms can select states inside the degenerate flat-background first-order manifold, and the actual heavy ground includes dressing. This is not a statement that the bare heavy background must remain classical at every order.

## 3. Vacuum plaquette fluctuation

For Kvac=-5E-4P, the X-polarized trial state has energy -10N. Since <P><=N, any ground satisfies <E>>=1.2N. In a translation/rotation invariant ground, each of the 2N equivalent edges therefore has expectation at least 0.6.

The symmetry condition should remain explicit. In the usual finite selected positive block, Perron-Frobenius uniqueness and the lattice symmetries give it. A general mixture can also be symmetrized without changing the ground energy. Extending the statement to every unsymmetrized ground requires the previously proved ground-response/symmetry equivalence, rather than the variational inequality alone.

Choose a plaquette P_p and one of its boundary-crossing edge operators E_e=X_iX_j, with exactly one endpoint on the plaquette. They anticommute and both square to I. Therefore, in any state,

    <P_p>²+<E_e>²<=1.

Under the uniform-edge bound this gives |<P_p>|<=0.8 and Var(P_p)>=0.36. In the positive selected block the plaquette flip has positive expectation, but positivity is not needed for the variance bound.

To infer an inelastic excitation from that variance, one must exclude merely rotating within a degenerate ground space. Here P_p preserves the selected row/column symmetry block, whose ground is unique, so its centered action has squared norm at least 0.36 entirely in positive-energy states of that block. If using arbitrary global ground mixtures, retain the established equivalence of their neutral responses. Without that extra fact, nonzero variance alone would not exclude an elastic degenerate-ground contribution.

## 4. Native loop and the mismatch of environments

The product of link phases around a native four-hop transverse square is P_p. Therefore the conditional closed transport path acts on the quantum background by that existing plaquette operator. Its nontrivial action on the vacuum neutral state follows from the fluctuation bound above. This is an exact channel in the native transport algebra, not an appended interaction or a universal source coupling. It does not by itself determine the full coherent sum of paths, an excitation probability, or a scattering rate.

For sufficiently large transverse periods, flipping two adjacent columns toggles four plaquette signs, so

    Pflat E Pflat=0,
    Pflat Kvac Pflat=-4N Pflat.

The actual vacuum coefficient ground energy is <=-10N. Hence its state cannot be a flat-background state. This comparison is decisive about the differing background preferences; it is not a computation of the higher-order heavy-sector energy, whose coefficient operator may differ from Kvac after projection/dressing.

## Conclusion

The signed-link graph, flux criterion, half-column first-order immobility, and flat-background heavy selection check out at fixed size. The vacuum variance argument supplies a concrete neutral excitation channel for the plaquette transport loop, with the stated ground-state symmetry qualification. The prepared vacuum environment and the dressed heavy ground must not be identified. The result demonstrates native backreaction structure, not gravitational universality, a measured detector bridge, or an R-uniform adiabatic heavy-particle theory.
