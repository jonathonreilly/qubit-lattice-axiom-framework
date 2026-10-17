# Selective check: actual slow-output outgoing coefficients

Disposition: conditional support; no mathematical correction required. The complete-input outgoing coefficient error <4.1e-5 in each record-X sector follows from the stated actual modified emitter/load premises and the inherited reference moment. This is not a complete state, all-time herald or finite-window theorem.

## Sources and exposure

Read the complete target `../slow_lead_outgoing_profile/PROPOSAL.md`, verified SHA256 `6f9ebabb3405b124e52582c313c342889c9146e0040306d0ec7b72e8e8371b17`. I did not author it. Root's proposed constants and intended scope were exposed. I authored the slow-gate load c1e1fe95ca3c9d390df0fad468c80c93d4c1c2aa1e3fee4c93c4326f44b0e61d, the operator recovery interface, slow recovery and earlier all-time synthesis. This is distinct-author checking of this outgoing composition, not blind checking or independent recertification of my own gate argument.

Read COMPLETE changed emitter source `../slow_lead_emitter/PROPOSAL.md`, SHA256 `53916c906eda8cd5a1c8c6228c54002f4f74fe7986bee301d3162124d40544c0`, and its distinct check `../slow_lead_emitter_check/REVIEW.md`, SHA256 `23c228886a96e29071beabf5e3ae1f6c9caee8544eee4e5b5ddc38f854fda707`. The target's opening statement that this check was pending describes its drafting time; the completed check now supports its emitter premise. No source amendment is needed for the mathematics.

Read COMPLETE scalar reference `../slow_lead_reference_packet/PROPOSAL.md`, verified SHA256 `e6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e`, and its root check `../slow_lead_reference_packet_check/REVIEW.md` (6fb89d66d0a79e5c66c6dabd00c030ddb603308485f60c857b95f0e791b1a5f5). Reread complete unchanged outgoing source `../record_attached_outgoing_profile/PROPOSAL.md` (52bd25106f95d06b1d06b741f1183a492d169e5a4c6e85aa40ebca88404d1788), using its unchanged upstream row and scalar reference rather than its old actual-device constants. Its prior distinct check44c697a5169b5cdb665e44c8b62787c2164f72537e082523e492ad535a29f026 and the inherited M2<1.9e-17 premise remain qualified ancestry. The slow-gate review8fb22bfddeeda9dd8abd1f3c90bafe4fd34916ec385d47aa017c99b08b221a65 was completely read in the immediately preceding coherent task and remains unchanged.

Original calibration, source inverses and reference moment are not rederived here. Applicable previously read instructions and review discipline are reused. No solver, dynamics, sweep, delegation, W/Git, publication, checkpoint, model or prompt change occurred; only this review is written.

## 1. Exact row, reference planes and denominator arithmetic

At v0, closed-channel elimination gives the selected outgoing coefficient b_P=d_src^-1 B_eff. The free eighteen-edge cable then multiplies by w^18. At the shared old gate port, solving the repeated interface return multiplies gate transmission by 1/(1-r_o r_L). The physical connector sends this amplitude to the DISTINCT first slow site through t_L. This reconstructs exactly

    L_phys=t_L w^18 (t_x/d_gate) d_src^-1 B_eff.

The gate is diagonal in B; closed-channel influence already enters through the ordered upstream B_eff and S_eff. No additional selected-output term or cable phase is missing. In particular the return already contains w^36 and cannot acquire a second such phase inside d_src.

The gate numerator comparison is <=34u, center included non-strictly. Inserting the unchanged upstream row gives total numerator deviation at most (34+181)u plus its positive calibration floor. The remaining denominator is d_src(1+R_new w^42), of modulus >.99365. Its deviation costs 1540u+r0+1540u*r0, with the negligible displayed closed correction retained. The slope before division is at most 215+1540+12+.07392 plus negligible allowances, below1767.075; division by .99365 keeps it below1780. The floor after division remains below1.8e-13, including the j-weighted row errors. Thus (A) follows without double-counting d_gate.

On complementary input columns the upstream scalar row has only its error E_L. Dividing its norm and the closed correction by the two margins leaves <2e-23. The entire selected row has norm <400/(.9937*.99999919) plus its tiny correction, hence <403. These are full row norms, not entrywise estimates.

## 2. Emitter Schur column and selected relative coefficient

The selected emitter-to-output column is -kappa times the ordered row [L_j+kappa^2 L_C Dcc^-1 G_Cj]/D_x. The complement correction has norm below (2e-23)*6*(2e-24)*kappa^2=24e-47*kappa^2 before multiplying by j. At fixed kappa its j-weighted relative allowance is far below1e-60. The signs match the negative emitter coupling and the negative upstream row; the reference A_ref therefore has the stated positive kappa numerator.

The changed actual emitter bound gives |D_x-Dref|<=kappa^2(8e-18+1.51e6u). Dividing by |Dref|>=gamma sin q and using j<.003 yields e_D<2.5e-20+4530.01u. Its maximum is <.018121, so the inverse margin .981879 is valid. Combining numerator and denominator comparisons gives slope (1780+4530.01)/.981879<6600, with the positive floor below2e-13. This verifies (B). No old 400u outgoing bound or old .9995 emitter margin is reused.

## 3. Physical transmission, Fourier normalization and phase

Differentiate the common energy: E'_k=(dq/dk)E'_q. The actual physical transmitted column is t_L A_tilde, so its k-normalized outgoing coefficient is i E'_k t_L A_tilde/sqrt(2pi). With J_k=dq/dk, exact flux normalization gives t_L J_k=t_f sqrt(J_k). This reconstructs the stated transformed coefficient and reference without a missing square root or velocity.

The reference before the connector has i times rho_att w^21. Since rho_att=-i w^40 rho_n, this supplies w^61 rho_n. The connector contributes exp[i(q+k)/2], and rho_n retains its fixed old-arm phase. The resulting scalar carrier is precisely61.5q+.5k+172k_old(q), referred to firstslowm0. It is neither61k nor an old-port coefficient relabeled as a slow-site coefficient.

Its squared norm is p_s, not p0: transformation multiplies the q measure by |t_f|^2. Because this multiplier is at most one, its u-squared moment remains below the inherited1.9e-17. The selected-column L2 error is bounded by 2e-13 sqrt(p_s)+6600 sqrt(1.9e-17)<2.88e-5. The source uses the safe sqrt(p_s)<=1, without normalizing the reference prematurely.

## 4. Complementary prepared inputs and complete aggregation

On each physical window the exact complementary prepared-input row retains BOTH terms shown in the source. With ||Dcc^-1||<6, ||G_jC||<2e-24, effective selected row<404 and |D_x|^-1<1/(326kappa^2), its amplitude is below

    kappa[1.2e-22+404*(12e-24)/326]<1.4e-30.

Multiplication by E'_q/sqrt(2pi)<.003 gives <4.2e-33, and multiplication by sqrt(8e-6) gives q-L2 norm <1.2e-35. The slow transformation cannot increase its integrated squared norm because its flux factor is contractive. Thus charging all finite window/record/parity combinations by <1e-34 is safe. These actual cross terms retain their output-window physical energy; the derivation does not commute K through an interacting source to assign them the input energy.

For the two selected old-energy columns within a parity, a Cauchy–Schwarz column bound costs sqrt2 even if their time-domain errors overlap. Since sqrt2*(2.88e-5)<4.074e-5, the4.1e-5 ceiling leaves ample room for the wrong-window terms. Orthogonal parity blocks combine by a maximum. Tensoring any passive reference leaves this operator bound unchanged.

Initial record0 weights the two conserved sectors by1/sqrt2. Projecting onto record1 forms their half-difference and hence preserves the common4.1e-5 error ceiling by triangle inequality. Before projection the record-X ranges are orthogonal and their squared errors average, also preserving that ceiling. This statement applies to outgoing coefficient maps; no analogous small norm for the entire incoming reference has been assumed.

## Scope

The checked result is a conditional actual outgoing coefficient comparison with the literal W eigenvalues, common scalar and common diagonal old aging. Actual two-lip synthesis must still include the conjugate incoming term, all finite/local components, closed tails and omitted seed amplitude. The reference incoming directional bound and outgoing onset are separate scalar facts; they are not proved by this coefficient estimate. No normalized early herald accuracy, finite success probability, permanent record, native preparation or retained audit status follows from this review.
