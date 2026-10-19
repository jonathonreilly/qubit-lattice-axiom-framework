# Explicit decay of the actual mediated nontraveling component

Author derivation requiring a distinct check. For each fixed finite mediator length satisfying the existing strict loaded gates, the unchanged physical background derivative bounds give an explicit C_m/|t| bound for the represented source, all internal mediator heads, all finite background heads and all closed slow tails. It includes complementary prepared inputs. This is not a numerical onset or a finite-device permanence theorem. The constant is deliberately coarse and can be very large.

## Domain and fixed physical spaces

Retain corrected occupation-compensated installation d2b7, fixed mass tuning d01ed6, loaded inverse5f909, regularityf815 and recovery83530. In particular use the original capped background compression, shared B and c_att once, both physical windows I_e=c_att+2j+e+[-rho,rho], e=1,3, both boundary lips and all record/parity sectors. Require all their gates, including 0<rho<=min(d_bg,a/2), rho/g<=1/2, lambda>0, eta<1, k_C>0 and zeta<1. Here a=J_m-q, b=.185-(J_m+q)>0. No finite-cut real-axis resolvent is substituted for the infinite receiver's matching.

On each window the B projectors and the classification of open/closed channels are fixed. Embed its finite background plus closed-tail recovery space into the actual physical space before summing windows. This embedding is constant in E within that window. The propagating stationary ray is excluded; it is not square summable. Window-dependent closed/open decompositions need not be orthogonal to each other. All estimates below pay the two windows by triangle inequality.

Let S(E) be the PHYSICAL three-source Schur matrix in loaded equation(13), and V_s the fixed physical product-seed inclusion, norm one. Set U(E)=S(E)^(-1)V_s. This includes both prepared old energies on each window, not only the selected one. Physical mass factors and sign gauges remain in S and V_s; estimates that use their contraction norms do not redefine the preparation.

## Established background derivatives, not differentiated error envelopes

The emitter-free background has unchanged exact finite matching

 M(E)=E I-H_finite+j V_o Q_slow(E)V_o^T,
 R=M^-1, F=R V_p, G=V_p^T R V_p.

Its matrix is complex symmetric on a lip. Consequently

 G'=-F^T F-j F_o^T Q_slow' F_o,
 F_o=V_o^T F.                                               (1)

The transpose is literal, not an adjoint or positivity identity. The checked full-forcing bounds ||F||<=14000, ||F_o||<=3270 and ||Q_slow'||<1/(1.93g) give the usable ceiling

 G_1=196000000+16622/g,  ||G'||<=G_1.                       (2)

This is the unchanged background part of prepared inverse derivative25052, not its nominal three-source denominator derivative. The mediated source does not change that background matrix. It changes the forcing supplied to it.

The complete recovery L from port forcing to 235 finite heads and closed tails has established bounds

 L_0=14000,
 L_1=1.00068*(7.29e16+3.31e7/g)+30,
 ||L||<=L_0, ||L'||<=L_1.                                  (3)

Prepared core cce29994 sections5-6 derives (3) from F'=-RF-jRV_o Q_slow' F_o and the closed-tail lift derivative; prepared background IBP90d42 uses precisely this Hilbert-valued scope. Its slow closed-tail lift has norm<.00068 and derivative<.009 and acts on the actual output value<3270. Thus (3) covers the entire closed sequence, not merely each finite coordinate. These are full forcing-domain estimates, including wrong-window inputs. A later sharper L' can replace L_1 only with its own verified scope. We do not differentiate ||G-G0||<=a0+b0|delta|, and import no old source pulse or nominal Q derivative.

## Differentiating the exact mediated Schur matrix

Define uniform finite constants

 r_* = min(a-rho,b)>0,
 Gamma2=gamma1²+gamma2²+gamma3²,
 gamma_* = max_l gamma_l,
 G_b=1/j+e_rho,
 k=1/(1-eta),
 t_b=max(sqrt(Z2)*kappa*(1+theta3),tau),
 t_1=gamma3²/r_*²,
 s_1=gamma3²/r_*².

The exact internal resolvent R_l(D)=(D tensor I+A_l)^(-1) has ||R_l||<=1/r_* and R_l'=-R_l² on ALL internal fibers: selected distance>=a-rho and complementary distance>=b. Endpoint compression therefore gives ||s3'||,||t3'||<=gamma3²/r_*², without any center approximation or selected-only derivative. The full two-end self-energy derivative has norm<=gamma_l²/r_*². The sum of its source compressions costs at most Gamma2/r_*², including the last chain's source-end diagonal. No length-dependent sum over internal sites is needed.

Put S_p=s3(D), K=(I-S_p G)^(-1), and Gt=(I-G S_p)^(-1)G. Their exact ordered derivatives are

 K'=K(S_p' G+S_p G')K,
 Gt'=(I-G S_p)^(-1)G'(I-S_p G)^(-1)+Gt S_p' Gt.   (4)

Let sigma=max(nu rho,tau), as in the loaded source, and define

 K_1=k²(s_1 G_b+sigma G_1),
 Gt_0=k G_b,
 Gt_1=k² G_1+Gt_0² s_1.

These bound K', Gt and Gt'. They are valid on both lips; no actual factor commutes through a function of D.

The physical S consists of bare I_3 tensor D, the three compressed internal self-energies, and the source2 load -t3 Gt t3. Exact product differentiation gives

 ||S'||<= S_1 := 1+Gamma2/r_*²
                         +2 t_b t_1 Gt_0+t_b² Gt_1.       (5)

The two hopping-derivative terms are separately bounded, not equated. A fixed sign gauge or fixed mass congruence causes no derivative terms. We work directly in physical coordinates, so no energy-dependent normalization is introduced.

From the loaded full block inverse, put

 A=6*(1+b_mix/k_C)²/[sqrt(1-3lambda/j)*(1-zeta)],
 B_c=1/k_C, R_delta=sqrt(delta²+lambda²),
 u(delta)=A/R_delta+B_c.

Then ||S^-1||<=u(delta), including all complementary outputs and inputs. The physical congruence has norm<=1, which justifies this envelope. Differentiate the exact inverse identity, not this envelope:

 U'=-S^-1 S' S^-1 V_s,
 ||U||<=u(delta), ||U'||<=S_1 u(delta)².                   (6)

In particular the O(1/k_C) complementary inverse is retained. This route sacrifices prepared-column sharpness but avoids any missing noncommuting derivative or false selected-as-full substitution.

## Complete nontraveling recovery and its derivative

Let J2 select source coordinate2. The background recovery from an arbitrary physical source vector is the operator

 Bop(E)=L(E)K(E)t3(D)J2.                                  (7)

The port is already one of its finite background coordinates. With

 B_0=L_0 k t_b,
 B_1=L_1 k t_b+L_0 K_1 t_b+L_0 k t_1,

we have ||Bop||<=B_0 and ||Bop'||<=B_1. The order in (7) is the physical order; replacing it by Gt on the full background is not allowed.

Recover each mediator by -gamma_l R_l(D) applied to its two endpoint injections. Within each chain those injections have orthogonal ranges. Across the three chains the source endpoints s0,s1,s2 occur respectively once, twice, twice, and the port once. Thus the stacked endpoint map from a source vector and its recovered port has norm at most sqrt(2)+B_0, and its derivative norm at most B_1. This holds also at m=1.

Let Hrec(E) be the full recovery lift from source vectors to the direct collection of source, mediator-internal, finite-background and closed-tail outputs. Using triangle bounds (rather than asserting cross-window orthogonality), define

 H_0=1+B_0+(gamma_*/r_*)*(sqrt(2)+B_0),
 H_1=B_1+(gamma_*/r_*²)*(sqrt(2)+B_0)
                                      +(gamma_*/r_*)*B_1.  (8)

Exact differentiation of the mediator recovery and (7) proves ||Hrec||<=H_0 and ||Hrec'||<=H_1. All 10m-4 internal mediator heads are included jointly. The port is counted as a physical output only once, inside the background; its appearance in the endpoint estimate is only a bound for the mediator map. Both (8) and the source estimate are uniform on the two windows and lips.

The actual nontraveling boundary column is N_lip(E)=Hrec(E)U(E). Therefore

 ||N_lip||<=H_0 u(delta),
 ||N_lip'||<=H_1 u(delta)+H_0 S_1 u(delta)².                (9)

The spaces in (9) are fixed within each window, and the closed lift is differentiable in its Hilbert norm by (3). All maps are absolutely continuous there. No assertion of a bounded whole-space continuous-spectrum resolvent is made.

## Explicit hard-edge integration by parts

Set

 J_R=2 asinh(rho/lambda),
 J_R2=2 atan(rho/lambda)/lambda,
 I_u=A J_R+2rho B_c,
 I_u2=A² J_R2+2A B_c J_R+2rho B_c²,
 u_edge=A/sqrt(rho²+lambda²)+B_c.

These are exact integrals of the scalar envelopes u and u². In particular J_R2<=pi/lambda; no derivative is inferred by differentiating u. For each lip on a single window, the Bochner integration-by-parts estimate is

 ||integral exp(-itE)N_lip(E)dE||
 <=[2H_0 u_edge+H_1 I_u+H_0 S_1 I_u2]/|t|.

Neither hard endpoint vanishes. The two physical lips in Stone each have factor1/(2pi), and there are two windows. Hence define

 C_m=(2/pi)[2H_0 u_edge+H_1 I_u+H_0 S_1 I_u2].             (10)

For every t!=0, the ACTUAL represented nontraveling map satisfies

 ||N_I(t)||<=C_m/|t|.                                     (11)

Regularityf815 identifies the rectangular lower-minus-upper jump and excludes missing in-window singular seed mass. We bound its two columns separately; it is not replaced by entrywise imaginary part. All wrong-window prepared columns are included by (6), so no additional complementary error is added. Record-X/parity sectors combine by maximum with their original normalized weights. Passive references preserve the operator norm. Old-energy factors exp(-it(c_att+2j+e)) are retained in the exact integrals; unit modulus is used only in estimates. Nothing is refitted to input or time.

## Consequence and limitations

Equation(11) replaces the entire represented nontraveling allowance c_R[C_s exp(-lambda t/2)+S_s]+E_rec in complete6ed86, rather than adding a second recovery charge. One may take the minimum of that earlier bound and C_m/t, since both bound the same represented component. The actual outside vector remains charged ONCE globally and can contain atoms; (11) says nothing about its decay.

For clarity, retaining all other complete6ed86 hypotheses and notation gives the conditional replacement

 error(t)<=eps_out+C_m/t+2E_raw+J(t)/sqrt(Z0)
                              +1-sqrt((p-L(t)²)/Z0),

whenever t>0 and L(t)²<p. It has the same normalized physical target, phase, old aging and source blanks as that source. Let E_* = eps_out+2E_raw+1-sqrt(p/Z0). For any e>E_* set d_e=e-E_*. A sufficient explicit infinite-receiver onset is

 T=max{1/v_*, 3C_m/d_e,
       9B_ref²/(pi v_* Z0 d_e²),
       B_ref²/(pi v_* p),
       3B_ref²/(2pi v_* sqrt(Z0)*sqrt(p)*d_e)}.              (12)

The last three allowances are precisely the previously checked incoming and normalization estimates; the new local term is <=d_e/3. Formula(12) quantifies the formerly qualitative fixed-apparatus limit, without declaring the outside/reference allowances necessary lower error bounds. The energy-resolved raw refinement can be substituted only after its separate check and at the identical tuple; it is not needed here.

All constants are finite at fixed m, lambda,g and strict margins. They may diverge rapidly as lambda tends to zero or a gap/margin closes. This coarse full-source inverse squared and the large inherited L_1 may produce a severe onset. No supplier tuple was evaluated, no performance improvement claimed, and no uniform-in-length rate proved. A useful numerical onset would require substitution of exact supplied coefficients and a separately checked complete point. There is no new native interaction, preparation, coefficient-tolerance, capture, repeated-measurement or finite permanent-halt result. Finite receivers require their separate finite-window cut comparison.

## Sources, exposure and verification status

Exact refreshed source identities:

- mediated_loaded_inverse_interface/PROPOSAL.md: 5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22; checked f6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3.
- mediated_seed_regularity/PROPOSAL.md: f8153ddb6a86a58e04e9d69a1ef98d13feefe8f0171ba3cbb3e98cf35ae4522b; my check9d837417cc295e6d96fcaf1c8db5aad508d618f90cd57bcb9d560bb70640ea6d.
- mediated_apparatus_recovery/PROPOSAL.md: 83530c67a650ae309fa920c0d149388080bb47178fd2b9f2a4cba88512be6333; check6f1b07555cd71a9e4208041c5249e892cf4b7f41ea25c92ed47c5b22b974a79f.
- mediated_complete_output/PROPOSAL.md: 6ed86c33b624ffc8f672e0f2380194fb624c9678b6f477ccab6f5cb59eef57f7.
- prepared_core_recovery/PROPOSAL.md: cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9; checks88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 and52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c.
- three_site_prepared_inverse_derivative/PROPOSAL.md: 25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84; my check3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c. Only its background derivative derivation is reused.
- prepared_background_ibp/PROPOSAL.md: 90d42e3699496e7694ddda630672af778a506b795865118757ab1e57da4a9c5a. Only its fixed-space IBP machinery and unchanged background bounds are reused, not its nominal source column or point.

The relevant exact source formulas and full recovery/regularity/complete arguments were refreshed; unchanged ancestor hypotheses and checks are reused in their stated scope. I authored stationary/IBP ancestors and checked regularity/raw/derivative work. Root suggested a full-inverse derivative route while this derivation was in progress; it was not evidence of its validity. Equations(4)-(12) above are new author composition, not a distinct check of itself. A distinct reader must test the physical full-source derivative, endpoint multiplicities, Hilbert lift and two-window/two-lip constants before downstream use. No derivative premise is left as an assumed derivative of a value envelope: (1)-(3) are existing physical matching derivatives, while the new mediator and inverse derivatives were derived explicitly here. Sharpness is unresolved.

Only this proposal was written. No scientific numerical execution, dynamics, solver, parameter sweep, source edit, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Deterministic reading and hashing supplied source bookkeeping, not mathematical evidence.
