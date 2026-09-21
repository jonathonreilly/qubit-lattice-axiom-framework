# Additional selection tests for the cubic symbol classification

2026-09-21. Provisional addendum to
`CUBIC_ENTROPY_PRINCIPAL_SYMBOL_CLASSIFICATION.md`, using exactly its uniform
fifteen-state product, full 48-element polar/axial action and five-parameter
symbol. These are added conditional implications, not new microscopic laws
or a derivation of a physical gauge principle.

## Generalized time reversal does not further select the curl member

Let Theta flip each A label to its opposite and leave B and vacancy labels
unchanged. On the tangent coordinates it is T=diag(-I_3,I_11). Every symbol
in the five-dimensional family obeys T A(q) T=-A(q), since each is off-diagonal
between E and the even moments. Thus this particular reversible parity rule
allows all five couplings.

For the supplied whole-record context generators this is more than a
principal-symbol identity. Their pair tensors satisfy S_i(Theta a,Theta d)
=-S_i(a,d). Therefore h_i(Theta eta)=-h_i(eta) and

    c_i(Theta eta)=kappa+max(-h_i(eta),0)=c_i(eta^edge).

The uniform product has equal weight before and after an edge exchange.
The pointwise telescoping identity makes the adjoint diagonal agree as well.
Consequently Theta L Theta=L* in that stationary product. A fixed fine-count
sector need not be invariant under Theta unless its opposite A counts agree.
This is a conditional generalized reversibility, not microscopic quantum
time reversal. Imposing it does not remove the scalar or tensor couplings.

## Conserving the two raw vector divergences does select the curl member

For the linear conservation system d_t u=-i A(q)u, suppose the subspace
q.E=q.B=0 must remain invariant for every q, while the scalar and tensor
moments remain otherwise arbitrary. The B equation automatically conserves
q.B because q^T[q]_cross=0. The E equation requires, independently,

    a1 |q|^2 = a2 |q|^2 = 0,
    u q^T D_alpha q = 0 for both alpha,
    v q^T Q_ij q = 0 for all i<j.

For all q these conditions give a1=a2=u=v=0. Conversely that choice preserves
both constraints. Thus **if** two raw-vector Gauss constraints hold and are
preserved for arbitrary remaining moments, the Maxwell-shaped symbol is
selected within this family, with m still free. This supplies a precise
conditional selection route.

The context exchange process in the classification does not in general
preserve those microscopic raw-vector constraints. Independent births can
also generate longitudinal noise. The constrained loop model and the local
curl readout are different constructions. This implication cannot silently
identify them with the unconstrained context generator.

## Curl observables give a weaker, useful closure condition

Alternatively define derivative observables at q!=0,

    E_curl=i[q]_cross B,     B_curl=-i[q]_cross E.

They satisfy their divergence identities kinematically. Their evolution is

    d_t E_curl=-i m[q]_cross B_curl,
    d_t B_curl=+i m[q]_cross E_curl-[q]_cross K_other(q) z,

where z comprises the two scalars, two diagonal tensors, three off-diagonal
tensors and the triple moment. Since [q]_cross q=0, both scalar couplings
drop out identically. The tensor columns do not vanish for every q. Hence
the curl observables close for arbitrary full-field perturbations iff
u=v=0; a1,a2 can be nonzero. This accommodates an independent longitudinal
sound sector alongside the transverse waves. It is weaker than closure of
the full six raw vector observables.

Kinematic closure does not fix the equal-time state. For a bounded raw
spectral covariance, these derivative observables still have covariance
of order |q|^2 near zero. The critical-correlation/quantum-state obligation
from the earlier local-curl analysis therefore remains.

## Conserved higher moments need a justified treatment

All fifteen species counts are conserved by pure whole-record exchanges.
The scalar and tensor coordinates are linear combinations of those counts.
At zero wave number their fluctuations are therefore exact conserved modes,
not a sector with an already supplied positive relaxation gap. An argument
that eliminates them needs a specified scaling and estimate, or a justified
additional process. This does not rule out emergent decoupling; it prevents
using unproved fast relaxation as the selection premise.

The attached exact symbolic checks reconstruct the cross-product source
terms, reversal identity and explicit q choices that force the stated
coefficients. No additional continuum-limit theorem is asserted.
