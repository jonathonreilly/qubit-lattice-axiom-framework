<!-- Original PR9802 source SHA256 e2acd4702f31bc724984aef54b95cca219d9df553b69ace458b3408029eca588. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Vacuum-mixing-induced heavy vertex: focused check

PASS for a finite-volume prepared-channel coefficient in the explicitly matched vacuum-channel basis and local flat-orbit gauge. It is not a diagonalization of the complete heavy/environment Hamiltonian. One subleading common-background assertion requires qualification, as explained below.

## Leading channel algebra

Let c=(gamma_L/Delta4)lambda^(L-4), with Delta4=L/16. Use normalized flat and edge-syndrome orbit states |0>,|e>. The first vacuum cluster rotation has

 |g>=|0>+c sum_e |e>+higher orders,
 |b_e>=|e>-c|0>+higher orders.

The sign is correct because both the winding matrix element and the vacuum excitation denominator are negative. Orthogonalization terms between excited states begin at higher powers of c and do not affect the proposed leading coefficient at fixed finite R.

For the operator-valued heavy channel blocks,

 <b_e|H|g> = H_e0+c(H_ee-H_00)+higher orders.

The leading diagonal heavy terms are Jlambda T_e and Jlambda T_0. Thus, with V_e=T_e-T_0,

    <b_e|H|g> = J(gamma_L/Delta4)lambda^(L-3)V_e
                +O_(R,L)(Jlambda^(L-2)).

This is earlier than the direct complementary assisted hop at order lambda^(L-1). Background-diagonal heavy corrections at order lambda^2 give only c lambda^2=lambda^(L-2). Corrections to the vacuum mixing coefficient are higher relative powers. The minimum spin-count bound excludes any independent background-changing heavy term earlier than lambda^(L-1). Hence no earlier direct term cancels this leading rotated coefficient.

The common vacuum winding piece -Jgamma_L lambda^L I cancels c JDelta4 lambda^4 I. However the full heavy H_e0 should not be equated to that scalar operator at order L: winding processes whose support meets the occupied heavy column can have local defect corrections at that same order, and assisted hops also have higher corrections. These terms are later than lambda^(L-3) and do not invalidate the leading result. State the cancellation for the common background contribution, not as an exact exhaustion of all order-L heavy terms.

## Physical-plane characters and the anchor gauge

A singleton in row y_i contributes an extra minus sign to its physical Y-normal-plane character. Fix a physical heavy sector obtained by creating the singleton at reference row y0 from the positive vacuum. Its background logical row characters must consequently shift at y_i and y0 when the particle moves. The proposed

    W_i=Z_(x_anchor,y_i) Z_(x_anchor,y0)

implements exactly those two shifts. It changes no x-normal-plane character, since both Z factors are in the same x column; when y_i=y0 the product is identity. It also preserves column parity. The longitudinal plane parity pattern of the single spin insertion is held fixed.

On a flat background s_xy=a_x b_y, adjacent-y transport contains s_i s_j=b_(y_i)b_(y_j). The W_j W_i factor is the same quantity, canceling it in the orbit matrix element. The x hopping is already sign-free and W is unchanged along x. Hence the flat channel becomes the ordinary T0 hopping with no additional normalization. Applying an edge-column flip away from the anchor column commutes with W_i for every i; the same calculation yields the signed-flux channel T_e. Normalized positive-character orbit states map with unit amplitude.

The restriction “edge support away from the anchor column” is substantive. Edges touching it require the corresponding transformed phase convention and cannot simply be included in the same local formula unchanged. An anchor gauge suffices for each specified local coefficient; a global translation-covariant sum or momentum matrix element must track this gauge consistently. The fixed physical heavy plane sector should be stated as above; one cannot keep the background all-positive at every particle row without the W_i identification.

## What the rotation does and does not prove

This rotation diagonalizes the vacuum/background channels to the needed order, thereby defining a prepared ground/excited-background basis for the heavy problem. It does not eliminate heavy/environment transitions. In fact the heavy kinetic scale Jlambda is much larger than the neutral background separation Jlambda^4. A Schrieffer–Wolff elimination of the complete heavy off-diagonal block using only that neutral denominator is not justified here. Degenerate or on-shell heavy-channel scattering requires a separate calculation.

The connected coefficient is basis dependent, but becomes a well-defined matrix element once the canonical microscopic reduction, anchor identification, vacuum-channel rotation, preparation and readout are all specified together. Under a simultaneous effective-frame transformation the physical prepared matrix element is unchanged. A change of channel gauge can redistribute the local entries of V_e; it cannot remove the nontrivial plaquette flux of T_e relative to T0. Nonzero V_e does not by itself ensure a nonzero chosen on-shell or momentum-resolved amplitude.

A useful consistency check is the leading finite-time propagator. The same basis rotation gives excited-background amplitude c[exp(-i tau T_e)-exp(-i tau T0)], whose Dyson representation is the time integral of the vertex c(T_e-T0). A return at one site first detects the flux difference at four hops, reproducing the previously checked c tau^4 return signal. There is therefore no contradiction between the lambda^(L-3) Hamiltonian coefficient and the lambda^(L-4) dimensionless-time return amplitude at physical time tau/(Jlambda).

The claim is valid at fixed finite R,L with an analytic matched construction to sufficient order. Bare-spin preparation, growing-volume uniformity, relaxed-heavy ground response, an emission rate, exact scattering, universal coupling and empirical identification remain unproved. Subject to these qualifications, no leading-order algebraic or physical-plane-sector obstruction was found.

## Agreed scope confirmation

Root explicitly accepted the common-winding-only cancellation and restricted the new claim to the local finite-feature vertex away from the anchor, with matched physical plane characters. No global sum over edge channels, translation-invariant scalar/Yukawa projection, or zero-momentum pole coupling is inferred from this local V_e. Such a projection needs complete anchor-string and symmetry-sector accounting; naive orientation sums are not gauge-independent evidence. The exact leading propagator identity is

    -i c integral_0^tau exp[-i(tau-s)T_e] V_e exp[-is T0] ds
       = c[exp(-i tau T_e)-exp(-i tau T0)],

with the stated sign. This corroborates the previously checked local return protocol without diagonalizing the full heavy problem. Final disposition: PASS for this narrowed, explicitly matched local coefficient and propagator identity.
