# Actual seed matrix mass from physical-energy windows

Status: root-authored conditional interface; requires a distinct check. No attached-device constants or spectral regularity are established here. This addresses actual omitted state amplitude for all old inputs, rather than a scalar return expectation.

Let H be bounded self-adjoint on the complete apparatus space and V:O -> Hphys an isometry, dim(O)=4. Its actual positive operator-valued seed measure is M(B)=V* E_H(B)V, with M(R)=I. Define F(z)=V*(z-H)^(-1)V. Fix disjoint closed physical-energy windows I_r around each distinct old energy plus the same kinetic emitter energy. For literal K=2I+Z1Z2, the old eigenvalues are 1 and 3, with orthogonal projections P_1,P_3 summing to I. No commutation of H with K is assumed.

Assume the actual seed measure is absolutely continuous on I=union I_r, with no singular mass including endpoints, and density D(E)=-(F(E+i0)-F(E+i0)*)/(2 pi i). Let reference nonnegative scalar densities f_r(E) on I_r have integrals p_r in [0,1], and assume the full FOUR-BY-FOUR density comparison

  integral_(I_r) ||D(E)-f_r(E)P_r||_op dE <= eta_r.

This assumption controls off-diagonal logical entries as well as other energy channels; separate diagonal expectation estimates do not suffice. Set p_min=min_r p_r and eta=sum_r eta_r. Then

  0 <= M(R\I) <= (1-p_min+eta) I,
  ||E_H(R\I)V|| <= min(1,sqrt(1-p_min+eta)).

Proof: integration gives ||M(I)-sum_r p_r P_r||<=eta. Therefore M(I)>=sum_r p_r P_r-eta I>=(p_min-eta)I. Subtract from the exact total mass I. The omitted embedding has squared norm ||V*E_H(R\I)V||. Every external spectral type is automatically included. Actual omitted initial components remain this small under unitary evolution, real record projection, and passive reference tensoring. This supplies the amplitude epsilon_sp used in the all-time interface; the mass itself must not be substituted for it. If local singular seed mass is present, either pay its operator norm separately or include it in an explicitly controlled measure comparison; boundary resolvent values alone cannot discard it.

A sufficient pointwise route is a comparison F_ref(E) with density f_r(E)P_r on each physical window. The imaginary-part map is operator-norm contractive, so eta_r <= pi^(-1) integral_(I_r)||F(E+i0)-F_ref(E)|| dE. For an invertible matrix Schur denominator D_e and reference D_ref, the EXACT identity is

  D_e^(-1)-D_ref^(-1)=D_e^(-1)(D_ref-D_e)D_ref^(-1).

If both inverse norms are bounded by C/sqrt(delta^2+gamma^2) and C_ref/sqrt(delta^2+gamma^2), and ||D_ref-D_e||<=kappa^2(a+b|delta|), then on a symmetric window delta in[-d,d],

 eta_r <= kappa^2 C C_ref/pi * [2a arctan(d/gamma)/gamma + b log(1+d^2/gamma^2)].

This is an upper bound on the integrated resolvent difference, not an identification of its density with a scalar Lorentzian. In particular a full reference diagonal resolvent for K+Ee generally has nonzero densities from the other old-energy channel on I_r if it is coupled to its own continuum. One must choose an actual reference with the stipulated density or add those reference tails explicitly to eta_r; silently dropping them invalidates the displayed sufficient route. Equivalently use a full positive reference matrix measure M_ref with M_ref(R)=I, REQUIRE its restriction to I to be absolutely continuous with density D_ref (including no endpoint singular mass), and assume ||M_ref(R\I)||<=tau and integral_I||D-D_ref||<=eta. The identical proof then yields omitted amplitude<=min(1,sqrt(tau+eta)); this formulation avoids artificial channel truncation.

Record sectors: if H decomposes into conserved X_R sectors H_s, and V delivers record0, apply the full-matrix theorem to each sector embedding V_s separately. For each fixed common input, the omitted full state has squared norm equal to the average of the two sector squared norms, before any projection onto record1. Taking a supremum gives an upper bound by the average of sector squared OPERATOR norms, not generally an equality of those operator norms. Consequently epsilon_sp <= sqrt((tau_++eta_++tau_-+eta_-)/2), capped at1. Recombining record1 is a contraction and cannot increase it. No assumption that the sector errors cancel is made. An alternative direct full-record spectral measure comparison gives the same type of result.

This theorem only uses full operator-valued measures on common PHYSICAL energy windows. It does not permit factoring old aging through a noncommuting H, replacing the full matrix inverse by one diagonal element, or using the local stationary record gate to infer these hypotheses. It is intended as the explicit missing normalization interface for the attached construction. Main next obligation: establish both sector inverse margins, actual local regularity and comparison density for the full emitter seed; an exact formula alone is not a bound.

Sources/exposure: author root has read the scalar-return proposal/check, complete all-time herald proposal/check, PR9674 converter proof packet and exact matrix Schur identities. This is an author derivation, not independent checking. No numerical/scientific execution or external source is used. No Git science branch, prompts, axioms or audit status changed.

Correction after distinct review: the first version omitted local absolute continuity of the reference in the alternative matrix-measure formulation. A reference atom inside I and actual atom outside I would defeat its density-only comparison. The reference hypothesis is now explicit; alternatively its local singular mass must be charged. The scalar-density formulation was unaffected. PROPOSAL_v1.md preserves the exposed original.
