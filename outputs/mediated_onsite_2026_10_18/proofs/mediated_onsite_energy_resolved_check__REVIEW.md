# Distinct check of the energy-resolved onsite interface

Verdict: conditional support for the full-row reconstruction, energy-resolved complete-certificate bound and stated fixed-supplier O(xi/lambda) scaling. No required mathematical correction found. Target: `mediated_onsite_energy_resolved/PROPOSAL.md`, SHA `7e1e1d1813f976a13c676d56373a073eab540acfe0c846d52805a48e1b04cdb0`. No numerical tolerance or operating point is certified by this review.

## Full physical elimination and arbitrary input

Accept equations (1)-(5) with the additional omega<1 gate. In physical coordinates the finite source/internal pencil after elimination of the unchanged background has off-diagonal blocks C_s* and C_s and internal block R_int^-1-gamma3^2 J_R G J_R*. The endpoint incidence duplicates s1 and s2 but not s0, so its norm is sqrt(2). The gate bounds the loaded internal inverse by r_L without requiring it to be Hermitian on a lip. Finite Schur associativity identifies its source complement with the inherited physical S; the new elimination is exact, not a low-energy approximation.

The resonant part of the full inverse factors as [I;-L C_s] S^-1 [I,-C_s* L]. The separate internal diagonal block is L. Both row and column factors have norm at most h=1+c r_L, even though L is not replaced by L*. Thus the full inverse ceiling h^2 u+r_L and the prepared-column ceiling h u are valid. The direct L term vanishes on the original source-only input, but must remain in the full inverse for onsite insertions on mediator interiors. The proposal makes this distinction correctly.

Accept the exact port row (6)-(7). Its sign follows by applying -gamma3 J_R* to the internal row of the full inverse. To check the order independently, put Y=gamma3 J_R* L C_s. From L=R_int+R_int gamma3^2 J_R G J_R* L one obtains Y=t3 J2+s_3R G Y, hence Y=(I-s_3R G)^-1 t3 J2. This is K_p on the LEFT. Only cell3 contributes to the unloaded right-end compression. Its right-to-left cofactor has the physical t3 convention in the loaded source; no adjoint substitution or sign reset is needed. The remaining arbitrary-internal-input row is exactly -gamma3 J_R* L[0,I].

Accept (8). Applying t3 before K_p uses the selected physical sqrt(Z2) kappa factor and the complementary tau factor on the full source-output rows. This yields D_w/R+e_w with e_w=tau B_c retained. Multiplication by the full right factor costs h. The direct internal row costs gamma3 r_L and is present in B_z. Neither this row nor the complementary constant is improperly given a resonant sqrt(lambda) suppression. All these estimates have the entire finite forcing domain, including wrong-window inputs.

The source row premises were checked against the loaded PP/PC/CP/CC block estimates: summing a full P row gives f(1+x)/R, while the C row gives fx(1+x)/R+B_c. The fixed physical congruence contracts and commutes with P/C projections. These are legitimate arbitrary-forcing row bounds, not prepared-column estimates relabeled as rows.

## Ordered Dyson identity and spectral integration

Accept (9)-(10). The perturbed inverse is (K_N^-1-D_N)^-1. The strict uniform gate gives K_d V=(I-K_N D_N)^-1 K_N V and hence h u/(1-theta). Using K_d-K_N=K_N D_N K_d gives the new-head difference. Applying the nominal physical port row on the left gives Z_N D_N K_d, exactly as stated. D_N need not commute with K_N, and its support can include every added source and internal vertex. No perturbed-row estimate has been assumed.

Accept the integral formulas and (11). Expanding (p/R+q)(A/R+B_c) gives pA/R^2+(pB_c+qA)/R+qB_c. Its exact finite-band integral is the stated I(p,q). The L2 triangle uses ||R^-2||_2<=sqrt(pi/(2lambda^3)), ||R^-1||_2<=sqrt(pi/lambda), and ||1||_2=sqrt(2rho), with correct powers and factors. This avoids differentiating any value envelope and preserves the calibration-dependent coefficients inside the bounds.

The local Stone factor 2/pi counts two lips and two windows; the local output includes all added heads plus the unchanged full finite background and closed tails recovered from port forcing. The traveling factor 4*461 sqrt(j/pi) counts both windows and both traveling coefficients, using the inherited exact physical flux conversion. Incoming comparison relies on the actual real matching at the same physical time, not a scalar conjugation assumption replacing the physical W-star structure. All comparisons precede halfline restriction, which is contractive. The result remains a full prepared-input operator bound with passive references.

Accept regularity only with the explicitly retained analytic matching premise. The new strict finite gate and the invertible loaded internal block supply local continuation on compact window neighborhoods and hence the same seed spectral identification. A norm envelope by itself would be insufficient; the proposal does not use it alone. No outside spectral type is excluded.

## Complete scope and scaling

Accept (12) and the witness increment. The original normalized first-cell trial X has norm one and support on the added region, so the new residual grows by at most xi. The full actual outside allowance therefore increases by at most sqrt(2)xi/rho. This replaces the nominal outside charge in its explicit retained-to-target composition; it is not added as a second omitted vector. The fixed packet, original mass, phase, old aging and all blank outputs remain. An already bond-perturbed tuple would require its OWN valid row and inverse constants before using this formula; the nominal constants do not automatically certify a joint error box. The proposal states that limitation.

Accept the conditional scaling in section 6. With fixed suppliers/background, eventual rho=sqrt(a lambda), and all named gaps including omega uniformly open, h,r_L,A_N,B_N and the full source constants stay bounded. The physical row gives A_z=O(sqrt(lambda)); the direct internal forcing leaves B_z=O(1), which is correctly retained. The new-head integral is O(xi/lambda)+O(xi log(1/lambda)); the background local integral is O(xi/sqrt(lambda))+O(xi log(1/lambda)). The largest ray term is xi*A_z*lambda^(-3/2)=O(xi/lambda); the unsuppressed direct-row term costs O(xi/sqrt(lambda)), not a worse power. Restricting xi/lambda to maintain theta uniformly below one therefore proves the claimed sufficient complete increment. The outside increment is only O(xi/sqrt(lambda)). This is not a necessary precision bound, protection mechanism, uniform fixed-xi unbounded-length theorem, or actual complete-output failure at larger errors.

No claim is rejected within its stated domain. No numerical usefulness, earlier onset, finite receiver theorem or native supplier conclusion has been established or checked here.

## Source identities and exposure

The target, full new residual source and its distinct review were read completely. The relevant physical Weyl/cofactor, Schur-order and full inverse passages of the unchanged loaded source were refreshed. Exact primary identities:

- Target: 7e1e1d1813f976a13c676d56373a073eab540acfe0c846d52805a48e1b04cdb0.
- mediated_recovery_residual_decay/PROPOSAL.md: f66b5636cca5cc6ef8e71b40746beb97b831527028738a6ccef7f17bca2b28ea; its check: 4f6784efb2f68f36b5598ac764cc3ae33ee7785048ad440acf16016305cadc5c.
- mediated_loaded_inverse_interface/PROPOSAL.md: 5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22; scoped check f6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3.
- Authored onsite predecessor: bba11422e5b425fa003ba4ba4890e2cdf70b717389d4b6ada4136ee19154dc50; ROOT check 972406c9ba8c40658ba3465f09a3110b270938a7b7df229472c1e5b2c18211c7 is cited by the target, not claimed as newly independently rechecked here.

The unchanged full background recovery83530c67, regularityf8153ddb and finite-Schur adapter594461 are reused only at their previously fully read physical scopes. I authored the onsite predecessor and several mediator/reference/complete ancestors and checked loaded/raw interfaces. This new proposal is ROOT-authored; the full loaded-internal inverse and arbitrary-input port row were independently reconstructed above, with substantial shared ancestry openly acknowledged. My own preceding work is not new independent evidence for itself.

No numerical program, root solve, integration run, dynamics, parameter sweep or model change occurred. Hashing was bookkeeping. Only this review was written; no target, W/Git/PR/checkpoint or editable prompt changed. Native blocks/occupations, exact background, preparation, phase knowledge and physical record identification remain supplied premises. No retained audit or delegation was performed.
