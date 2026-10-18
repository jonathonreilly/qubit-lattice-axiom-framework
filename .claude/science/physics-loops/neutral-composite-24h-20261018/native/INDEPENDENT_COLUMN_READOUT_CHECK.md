# Original longitudinal readout from the fourth-order column interaction

The proposed coefficient, sign and factor of two check, conditional on the supplied fourth-order plaquette Hamiltonian coefficient. This report checks its source differentiation and operator interpretation; it does not independently rederive the entire native fourth-order loop enumeration. No physical source term is adopted and no repository files were changed.

## Source derivative and local denominator

Use H(s)=H+sC with C=sum_(column c,j) Z_(c,j)Z_(c,j+2). In an aligned column, flipping one spin at height j reverses each of its n1(j) nearest-neighbor bonds, costing2 n1(j)Jz. It also reverses n2(j) distance-two readout pairs, changing C by-2n2(j). Thus the single-spin cost is exactly

d_j(s)=2n1(j)Jz-2s n2(j).

For a same-height plaquette path whose intermediate state flips m distinct columns, the costs add to m d_j(s): there are no additional transverse diagonal terms in the unperturbed longitudinal Hamiltonian. Taking the supplied loop coefficient K_j=Jx²Jy²/(2d_j³),

partial_s K_j=6n2(j)K_j/d_j,
partial_s[-K_j P_square]=-6n2(j)K_j/d_j P_square.

The minus sign is tied to the PLUS source convention H+sC. Reversing the source convention would reverse the differentiation rule and must not be mixed with this formula.

## Open-boundary sum

For L>=5 the two endpoint heights have n1=1,n2=1; the two next-to-end heights have n1=2,n2=1; and the remaining L-4 heights have n1=2,n2=2. At s=0:

sum_j K_j=Jx²Jy²/Jz³ [2/16+(L-2)/128]
          =(L+14)Jx²Jy²/(128Jz³).

For the derivative, each endpoint contributes -3Jx²Jy²/(16Jz4); each next-to-end height contributes -3Jx²Jy²/(256Jz4); and each remaining interior contributes -3Jx²Jy²/(128Jz4). Therefore

C_eff,parity= -3(L+13)Jx²Jy²/(128Jz4) P_square.

Independent exact rational checks at L5,6,7,10 reproduce both sums. These counts are for the original open distance-two readout; periodic boundaries or short lengths require separate counts.

For a single plaquette parity comparison with Jx=Jy=lambda Jz, the + minus - difference is twice this coefficient:

<C>_+ - <C>_- = -3(L+13)lambda^4/64 + higher orders.

Scalar readout corrections are not included in this parity-dependent coefficient and cancel in such a comparison. For an arbitrary transverse array the result is a coefficient multiplying the SUM of plaquette parities. A two-state comparison equals twice the single-plaquette coefficient only when other relevant parity contributions cancel or the coefficient is otherwise isolated. Changing one column can change several plaquettes, so a generic '+ versus -' label is insufficient on its own.

## Canonical connection

The aligned unperturbed low projector is independent of s because C is diagonal and has the same value on all aligned configurations. For a smooth canonical isometry W(s), differentiation of H_eff=W†H(s)W gives the compressed observable W†CW plus a connection commutator with H_eff (the commutator sign depends on whether the connection is defined as W†partial_s W or its negative). The connection must not simply be discarded as a general identity.

Here H_eff through orders below four is scalar in the aligned band for L>=5: an off-diagonal full-column process needs at least L flips, and the supplied lower closed-loop terms are scalar. The canonical connection is analytic and starts at positive transverse order (in the usual polar convention its low-low block begins at second order). Therefore its commutator cannot modify the order-four parity-dependent observable coefficient. This establishes the operator differentiation argument to the claimed order, rather than only an eigenvalue derivative.

For the trace over an actual smoothly isolated band, the connection commutator has zero trace exactly. If a finite numerical comparison uses selected '+/-' subsets, specify how these are invariant or smoothly identified spectral subspaces; on a general transverse array P_square need not be an exact symmetry of the full H. The trace argument does not by itself justify an arbitrary basis-label subset.

## Physical meaning

At the retained order H_eff contains -K sum P_square and this readout term contains a scalar multiple of the same commuting plaquette operators. The displayed term alone is therefore elastic in that leading Hamiltonian: it gives different diagonal readout values, not an inelastic neutral pole. Higher column tunneling, other retained terms or different observables need separate treatment.

The source parameter is a differentiation device for an existing operator, not an added physical interaction or a derived detector coupling. The coefficient remains conditional on the supplied microscopic anisotropy, aligned low band and finite-order regime. No selected physical state, autonomous mode or cosmological identification follows.
