# Focused finite-order normal-form form-gap check

Disposition: PASS with the explicit local decomposition below, in the stated finite-order, nonwrapping, symmetry-preserving setting. The inequality concerns B_m, not the exact microscopic Hamiltonian. It is not a positive gap above a unique vacuum across the entire N=0 sector.

## Individually N-preserving terms

At each order decompose D_j into Hermitian finite-support terms, then apply the commuting-N time-average separately to each term. Since D_j already commutes with N, their sum is unchanged. The filter enlarges support only by incident longitudinal neighbors and preserves Hermiticity. Average each filtered term under the finitely many physical plane-flip actions meeting its support. These actions commute with N, preserve the full coefficient, do not enlarge support, and do not increase its norm. Thus one may take each term t to commute with N and respect plane flips. All relevant diameter, overlap and norm constants are finite at fixed m.

Enlarge its support to a bounded column-convex box B, including vertical bonds incident to all potentially changed spins and vertical paths to a chosen anchor slice z0. Let Q_B project onto at least one broken vertical bond in B. A computational-basis matrix element of t preserves total N and changes spins only inside its support. If its input has no walls in B, any nonempty changed set in an affected column would create a vertical wall on the boundary of that finite set. It cannot remove a wall outside B, because bonds outside the incident neighborhood are unchanged. It therefore cannot preserve N. Whole-column flips are excluded by longitudinal period larger than the support diameter. Thus t is diagonal on Q_B=0 and has no matrix elements connecting that subspace to its complement. Hermiticity gives both directions.

Define f_t to be the diagonal value of t on locally aligned column configurations, evaluated using the column signs at z0. It is a bounded diagonal operator on the transverse bounding rectangle, with ||f_t||<=||t||. On Q_B=0 it agrees with t. Therefore

 r_t=t-f_t=Q_B r_t Q_B,
 |<psi,r_t psi>|<=2||t||<psi,Q_B psi>.

Since Q_B<=sum of the broken-bond projectors in B, summing translates gives a volume-independent C_m N bound. Multiplication by the perturbative coefficient lambda^j and summation j=1,...,m gives C_m lambda N for small positive lambda. This resolves the concern that a projected term could move a wall outside its original support: B includes every vertical bond whose value the term can change.

## Wall-free diagonal functions and plaquette comparison

The physical X-plane and Y-plane flips act on the sampled signs as s_xy -> a_x b_y s_xy. Accordingly f_t is invariant under these row/column actions. On any finite simply connected transverse rectangle, all elementary plaquettes P=+1 imply s_xy=a_x b_y. Thus f_t equals its all-up value whenever that rectangle has no bad plaquette. Pointwise,

 |f_t-f_t(allup)| <= 2||t|| sum_(plaquettes in rectangle) (1-P)/2.

Intermediate columns outside the original support are harmless: adding them merely enlarges the comparison rectangle by a fixed amount. This argument needs no explicit Walsh decomposition, although the even row/column Walsh monomials give the same conclusion. It also avoids periodic topological constraints by using proper local rectangles.

For a precise leading-coefficient identification, group translated terms by their anchor z slice before applying the wall-free substitution. The sum of their f_t is the same transverse functional that the order-j coefficient evaluates on an arbitrary globally aligned column-sign pattern, per longitudinal slice. This removes a possible density/divergence ambiguity in assigning individual plaquettes. One can then substitute the actual signs of each slice into this functional identity. Differences from the original terms remain in the r_t already bounded by N.

For j<4 the functional is constant: diagonal return words have fewer than four transverse edges, and no sign-dependent cycle can occur. At fourth order, the only sign-dependent return graph is a same-slice elementary square. Repeated edges are constant on aligned columns; distinct longitudinal layers must each have even edge-degree and cannot form another four-edge cycle. The local-gauge square coefficient is -P/128, as in DIRECT_LOCAL_TENSION_PROOF.md. Consequently the fourth-order wall-free excess is exactly

 (lambda^4/64) sum_(x,y,z) B_xyz,  B_xyz=(1-P_xyz)/2.

For j>=5 the local comparison above bounds the absolute wall-free excess by C_m lambda^5 sum B_xyz. The same fixed-order constant absorbs overlap multiplicities and the finite sum over j. For sufficiently small lambda this can be absorbed into half the positive fourth-order potential.

Combining both decompositions therefore gives the stronger convenient form

 B_m-Evac >= (2-C_m lambda) N + (lambda^4/128) sum B_xyz,

after increasing C_m and reducing the fixed-m lambda threshold if necessary. A version counting only plaquettes away from walls is also valid. Plaquettes near walls cause no obstruction: the anchor-slice construction retains the positive comparison potential everywhere and pays the difference in the wall-supported remainder. All-up scalar values are subtracted termwise, whose sum is exactly Evac; no uncancelled volume constant is introduced.

## Meaning of the separation

This proves a lower form bound uniformly on sufficiently large periodic tori, with all local boxes nonwrapping, for each fixed m. Constants and the small-lambda threshold may depend strongly on m. It does not justify summing all orders or claiming the same inequality for the microscopic remainder.

There remain many N=0 configurations. Some have positive plaquette energies of order lambda^4; row/column-gauge configurations remain degenerate at this local finite-order level. Thus the inequality is not a global gap of order one above a unique all-up state. The needed statement is separation of specified N sectors. In the even relative z-plane-parity sector, a compact N=2 configuration would be one flipped column interval and is forbidden. The first allowed finite excitation has N=4. Sectors N>=6 have energy at least 12-O_m(lambda), separating them from [7,9] for small lambda.

A finite-support dressed-source coefficient cannot connect the all-up state to a different N=0 state: that would require a whole-column flip. This must be used together with the sector bound when filtering the response; the bound alone would not remove other N=0 states. The exact untruncated dressed source is treated by the separate source-tail estimate. No assertion of an isolated positive line or microscopic pole follows from the present gap check.

Scope read: /private/tmp/neutral_normalform_gap_root.md (first half), native/INDEPENDENT_LOCAL_NORMALFORM.md and native/DIRECT_LOCAL_TENSION_PROOF.md. No repository changes or formal audit. The finite-time correlation/filter estimates in the second half were not independently re-proved in this report.

## Addendum: growing finite-box ground band

The proposed growing-box ground-band conclusion follows from the same stronger inequality. Take even periodic transverse sizes and longitudinal size Lz asymptotic to lambda^-4, all much larger than the fixed support range. In N=0, every column is constant along z, so sum_xyz B_xyz=Lz times the number of bad transverse plaquettes. Any nonzero such number is at least one (additional torus constraints can only improve this lower bound). Its energy is therefore at least lambda^4 Lz/128, bounded below by a positive constant as lambda tends to zero. In N>0 the wall term provides a positive constant lower bound as well. Hence B_m has a volume-uniform positive gap above its exact ground eigenspace along this prescribed growing-box family.

The zero-energy configurations are precisely N=0 and every transverse plaquette +. On the periodic square grid these are s_xy=a_x b_y, with one simultaneous sign redundancy, yielding 2^(Lx+Ly-1) computational-basis configurations. Each is an exact eigenvector of the fixed-order local B_m: no proper-support term can connect different aligned configurations, and plane symmetries equate their energies to all-up. Their span is the full ground eigenspace by the positive form bound. This conclusion uses the positive comparison potential, not merely the weaker bound proportional to N.

For m=40 and volume V=O(lambda^-12), the interaction-norm remainder gives global operator norm ||R||<=C V lambda^41=O(lambda^29). Weyl separation and the spectral-subspace perturbation bound for an isolated cluster apply with constants independent of the cluster's very large dimension. The actual transformed Hamiltonian thus has an isolated lowest band of the same dimension, lying within O(lambda^29) of Evac, with spectral projection differing from that of B_m by O(lambda^29). Any actual ground vector is at norm-distance O(lambda^29) from this entire unperturbed ground subspace (and, after normalization, from some vector in it). Conjugating back gives the corresponding U_m†-dressed statement. Splittings within the narrow band are allowed; this does not pick the all-up vector.

This is a valid finite-box ground-band result along L~lambda^-4. It is not a thermodynamic ground-state gap or proof that arbitrary ground-band superpositions have the same C response. The latter requires the separately proposed symmetry/locality and normalization argument, including error bounds after multiplication by the observable norms.
