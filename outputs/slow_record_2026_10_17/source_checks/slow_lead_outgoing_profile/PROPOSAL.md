# Actual slow-lead outgoing profile

Status: root-authored conditional derivation requiring a distinct check. New emitter source53916c906eda8cd5a1c8c6228c54002f4f74fe7986bee301d3162124d40544c0 was fully read but its check is pending. Gate sourcec1e1fe95ca3c9d390df0fad468c80c93d4c1c2aa1e3fee4c93c4326f44b0e61d and distinct review8fb22bfddeeda9dd8abd1f3c90bafe4fd34916ec385d47aa017c99b08b221a65 were fully read. Reuse the full unchanged upstream row in record_attached_outgoing_profile/PROPOSAL.md52bd25106f95d06b1d06b741f1183a492d169e5a4c6e85aa40ebca88404d1788 and its prior check44c697a5169b5cdb665e44c8b62787c2164f72537e082523e492ad535a29f026. Its actual old-device bounds are NOT imported. The new scalar comparison is slow_lead_reference_packet/PROPOSAL.md e6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e with root check6fb89d66d0a79e5c66c6dabd00c030ddb603308485f60c857b95f0e791b1a5f5. Source exposure includes root's interface and previous outgoing derivation. No scientific execution, simulation or model/prompt edit occurs here.

## Exact output row and source feedback

Use the same physical old input/output reference planes as the new gate proof. Record-X sector is x=+1,-1. Let r_L,t_L be the interface reflection and PHYSICAL transmission from old port o to distinct firstslowm0. Let t_x,r_o,x be the original equal-j gate entries and d_gate,x=1-r_o,x r_L. Let d_src,x=1-S_eff,x r_x be the ACTUAL modified source feedback denominator, with r_x=w^36 R_left,x. The gate does not mix B channels. The exact selected slow output row for full endpoint forcing is

 L_phys,x=t_L L_tilde,x,
 L_tilde,x=w^18 [t_x/d_gate,x] d_src,x^-1 B_eff,x.

All matrices retain order; the shown scalar factors occur only on the selected row. Closed source backreaction is inside B_eff and S_eff. There is no extra cable phase inside either denominator.

The checked new gate gives |d_gate|>.99999919, |t_x|<=1, and

 |t_x/d_gate-x rho_R|<=33u+33u|r_L|/|d_gate|<34u

away fromu0, with the corresponding non-strict zero bound at center. Here rho_R=-i w^22 and u=|q-pi/2|<=4e-6. The new endpoint gives |d_src|>.9937 and |1-d_src|<=1540u(1+8e-47). Its unchanged upstream forcing is

 PB_e=-(t_new/j)w^21(1+R_new w^42)^-1 P+E_L,
 ||E_L||<1e-23, ||B_eff-PB_e||<2e-48,
 |R_new|<1e-20+12u=r0,
 |t_new-rho_n omega|<1.76e-13+1e-20+181u,
 |t_new|<=1.

omega is the literal W eigenvalue, not a fitted phase. Define rho_att=w^18 rho_R rho_n=-i w^40 rho_n, the old attached phase BEFORE the new connector. Combining the numerator comparison (34+181)u and positive floor with the new source/input denominator gives

 j||L_tilde,x+(x rho_att omega/j)w^21 P||
       <1.8e-13+1780u.                            (A)

Indeed the common denominator has modulus>.9937(1-r0)>.99365. Its difference from1 is at most1540u(1+8e-47)+r0+1540u(1+8e-47)r0. The unrounded slope including the numerator is below1767.075, and division by.99365 is below1780. The tiny E_L and B_eff corrections are paid within the positive floor. The gate numerator comparison above already includes d_gate; it is not counted twice.

Also ||L_tilde,C||<2e-23 and ||L_tilde,j||<403. The former follows from the unchanged E_L complementary row and B_eff correction divided by BOTH margins; the latter follows from ||PB_e||<400 plus its correction and both denominators. These are full complementary-row norms, not deleted inputs.

## Actual emitter and transmitted reference

Let D_x,Dcc_x,G_x be the NEW emitter objects. Its selected outgoing coefficient before t_L is

 A_tilde,x=-kappa[L_tilde,j+kappa² L_tilde,C Dcc^-1 G_Cj]/D_x.

Use ||Dcc^-1||<6 and ||G_Cj||<2e-24 from the new emitter proposal. The added numerator is explicitly less than24e-47 kappa² before multiplying byj, and can be paid by1e-60 in the relative comparison. Put

 A_ref=kappa rho_att w^21/(j Dref), Dref=delta+(kappa²/j)w.

The actual denominator comparison is

 |D_x-Dref|/|Dref|<=j(8e-18+1.51e6u)/sin q
                    <2.5e-20+4530.01u=e_D(u).

Its maximum is below.018121, so the inverse margin is>.981879. Combining(A), |omega|1 and the complementary numerator yields

 |A_tilde,x/A_ref-x omega|
   <[1.8e-13+1780u+e_D(u)+1e-60]/[1-e_D(u)]
   <2e-13+6600u.                                 (B)

The slope6310.01/.981879 is below6600; the positive floor has slack. These are new bounds; the old400u estimate does not survive unchanged.

Let k be slow momentum and J_k=dq/dk=g sin k/(j sin q). The ACTUAL physical coefficient at firstslow is A_phys=t_L A_tilde. Its Fourier coefficient is i E'_k A_phys/sqrt(2pi). Since E'_k=J_k E'_q and t_L J_k=t_f sqrt(J_k), it equals

 F_actual,x(k)=t_f sqrt(J_k) [i E'_q A_tilde,x(q)/sqrt(2pi)].

The scalar slow reference is exactly F_s(k)=t_f sqrt(J_k) [i E'_q A_ref(q)/sqrt(2pi)], the sourcee6a9706d coefficient. It has phase61.5q+.5k+172k_old(q) and mass p_s, notp0. Thus(B) compares actualF to x omega F_s without dividing by a possibly omitted physical velocity or replacing t_L by unit transmission.

Because |t_f|<=1, its weighted moment obeys

 integral u(q(k))² |F_s(k)|² dk
       <=integral u(q)² |F_ref,att(q)|² dq<1.9e-17.

The selected-column coefficient L2 error is therefore

 ||F_actual,x-x omega F_s||_2
       <2e-13+6600 sqrt(1.9e-17)<2.88e-5.         (C)

This is a subnormalized reference; division bysqrt(p_s) is reserved for an explicitly normalized target later. For the two old-energy columns in each parity, use the safe sqrt2 aggregation unless sharper orthogonality is proved. Orthogonal parities combine by maximum. This gives complete-input outgoing coefficient error<4.1e-5 in EACH record-X sector, before record recombination.

## Other prepared input on each physical window

Retain the whole union of two physical windows. On the window with open channelj, complementary PREPARED columns have

 A_tilde,C=-kappa[L_C Dcc^-1
 +(L_j+kappa² L_C Dcc^-1 G_Cj) D_x^-1 kappa² G_jC Dcc^-1].

Using the bounds above, effectiveL_j<404 and ImD_x>326kappa² gives

 ||A_tilde,C||<kappa[12e-23+404*12e-24/326]<1.4e-30.

Before the slow transformation its q coefficient is<4.2e-33, using E'_q/sqrt(2pi)<.003. Its qL2 norm on length8e-6 is<1.2e-35. Transmission/change of variable multiplies its squared integral by|t_f|²<=1, so the corresponding slowkL2 bound is no larger. Both windows and finite parity/record aggregation contribute<1e-34, inside4.1e-5 slack. These cross terms evolve with ACTUAL output-window energyc_att+b_j+E(q), not the input energy. No K commutation is assumed.

The initial record0 gives sector weights1/sqrt2; final record1 gives the half-difference. Each sector's coefficient bound supplies the same4.1e-5 allowance for the projected outgoing comparison. For an unprojected comparison, orthogonal record-X ranges preserve that allowance as well. Literal W, common c_att and exp(-itK) remain in the ideal diagonal target, and every actual cross term is charged by its Fourier norm.

This proposal only compares outgoing coefficients. Actual Stone synthesis must include the conjugate incoming coefficient, finite/core outputs, all closed tails and omitted seed mass. The new reference incoming halfline and onset are separate checked scalar estimates. No all-time or finite success theorem, repeated-measurement protocol, permanent halt, capture or native preparation is asserted here.
