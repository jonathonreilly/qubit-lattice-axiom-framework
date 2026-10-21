<!-- Owning original: PR9758; source SHA256 03f9f5c6bb1473d38d61feb3bfa55e372785136daae4c98e6f23c1c549deecc0. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Ground-density independence and finite/infinite window comparison

Checked 2026-10-18. This is a separate extension to the conditional windowed-response check. Assume the first-half positive form bound, the exact local normal form, and the characterized B_m ground manifold. The argument is valid with the projector and scaling qualifications below.

## Isolated coefficient ground cluster

For N=0, each column is uniformly ordered. P=+1 on every elementary transverse plaquette implies column signs s_xy=a_x b_y, so plane flips act transitively on these product states. Fixed-support N-preserving terms cannot flip whole columns, so B_m acts diagonally there; all these states have exactly the same coefficient energy. The positive plaquette bound and L_z=K_m lambda^-4 give an order-one lower bound for other N=0 configurations, while nonzero allowed N already has an order-one wall gap. Thus the coefficient ground manifold has a volume-uniform positive gap under the assumed form proof.

The global remainder obeys ||R_40||=O(Jz V lambda^41)=O(Jz lambda^29). Standard isolated-cluster perturbation then makes the full microscopic LOW-ENERGY CLUSTER projector O(lambda^29) close to the rotated coefficient-ground projector. The exact true-ground projector need not have the same rank: tiny splittings may select a strict subset, in which case two-sided projector-norm closeness to the entire coefficient ground space is false.

Nevertheless every density supported on the exact true ground lies in that nearby cluster. A near-identity unitary intertwining the cluster projectors maps it to a density supported on P0 with trace-norm error O(lambda^29), independent of the large ground-space dimension. Correlations of the normalized global source, whose operator norm squared is O(V), incur an O(lambda^17) state-replacement error. This statement permits arbitrary mixtures and coherences of actual ground states.

## Localized plane-invariant responses

Each finite-order dressed local c_j remains invariant under every exact plane flip: its undressed version is invariant, the normal-form unitary respects the symmetry, and each Taylor coefficient inherits it. B_m evolution preserves that invariance. Conditional expectation onto a ball commutes with conjugation by a plane Pauli product because that unitary factors across the ball and its complement. Thus localized c_j(t) remains exactly plane invariant, rather than merely approximately invariant.

Choose R=L/10 with R-v_m T positive and proportional to L. Conditional expectation gives a uniform operator-norm localization error exponentially small in R-v_m T (up to harmless polynomial prefactors). The product c_j^loc(t)c_k has support whose total longitudinal extent is at most 2R+rho_m<L, even if j and k are widely separated. It therefore cannot connect any two distinct N=0 column configurations: they differ on at least one entire column. Every offdiagonal matrix element in that product basis vanishes exactly.

Plane invariance and transitivity make all its diagonal entries equal. Hence

    P0 c_j^loc(t)c_k P0 = a_jk(t) P0

as an operator identity. This is stronger than an entrywise smallness claim and avoids multiplying errors by the exponentially large ground-space dimension. Summing j,k and dividing by V costs only V. The resulting ground-density dependence is bounded by a polynomial factor times exp[-mu(R-v_m T)]. Means/connected subtractions are handled by the same localization or by stationarity in the coefficient ground space.

For T=c lambda^-4/Jz and L=evenceil(K_m lambda^-4), choose K_m larger than all geometric multiples of the finite-range LR velocity entering the several comparisons. No small-velocity assertion is required; a sufficiently large fixed K_m works. A single quoted inequality such as K_m>20v_m c should be adjusted if a later comparison uses L/40 rather than L/10. Stating 'sufficiently large for the displayed LR separations' avoids a spurious universal numerical constant.

## Infinite compact response

In the all-up product state, connected correlations of two operators with disjoint localized supports vanish. This gives summable LR tails for the coefficient connected correlation as a function of separation. The normalized zero-momentum finite-volume response is its relative-coordinate sum. Split that sum into separations well within L and its tail. Local finite/infinite dynamics agree up to exponentially small LR errors for the inner region; the tail is bounded by a polynomial in L,T times exp[-mu(L/c_geom-v_m T)]. Thus the full sum, and its normalized time window, have a superpolynomially small finite/infinite discrepancy with the chosen K_m.

The infinite all-up finite-excitation representation has a compact N=4 sector. This local-dynamics comparison is what permits replacing the finite full-N=4 response by that infinite compact response over the specified time window. Initial compact support alone was insufficient; the LR estimate supplies the missing step and suppresses finite winding/background changes on this time scale.

The source is truncated at fixed order before applying this finite-support argument; exact dressing tails are controlled by the separate O(lambda^29) source error. Likewise no infinite-volume global norm of the remainder is invoked: the microscopic comparison uses the chosen finite cube first.

## Result and boundary

Conditional on the form-gap proof, the supplied-all-up preparation can be removed from the finite-window comparison: every actual finite-volume microscopic ground density gives the same coefficient window response to the stated errors. The global Duhamel error O(lambda^13), source error O(lambda^29), state error O(lambda^17), and high-sector filter error O(lambda^8) remain dominated by O(lambda^8).

This is a joint weak-coupling, finite-volume scaling statement with L proportional to lambda^-4 and T proportional to lambda^-4. It is not an assertion about an arbitrary fixed-lambda thermodynamic ground state, a full-H outgoing pole, cosmological state selection, or an operational detector. The Hamiltonian, anisotropic regime, energy units, and choice of diagnostic remain supplied.

## Local extraction of the N=4 response

The proposed charge component

    c_(j,+4)=(1/2pi) integral exp(-i4theta)
       exp(i theta N)c_j exp(-i theta N) dtheta

satisfies [N,c_(j,+4)]=4c_(j,+4). Since N is a sum of commuting longitudinal bonds, its support enlarges only by the longitudinal neighbors of the original finite support. On the all-up N=0 vector it is exactly P4 c_j|vac>. Therefore the N=4 response is the correlation of local charge components <c_(+4)^dagger(t)c_(+4)>, with zero one-point expectation. This validates applying the local LR and finite/infinite comparison directly; no nonlocal spectral projector is inserted into an LR estimate. Apply this to the fixed-order truncated dressed local source, whose support is uniformly finite at fixed order.
