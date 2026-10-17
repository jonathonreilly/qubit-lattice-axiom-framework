# Complementary new-port incidence: physical old finite recovery derivative

Status: new conditional author derivation requiring distinct checking. For the unchanged two-converter background on |q-pi/2|<=4e-6, both physical old-energy windows and both lips, this argument gives

    ||Phi_old C_new||<6.5,
    ||(Phi_old C_new)'||<1e23.                         (1)

The output is the complete172-head old finite region, including both40-step buffers and their endpoints, with all internal coordinates. The input is arbitrary complementary incidence on either NEW port. The large derivative is acceptable only when later multiplied by a proved small cap coefficient. A separately conditional cap application below gives a forced-old derivative <1.9e14 using the still-unchecked scattering-derivative proposal909fef. Nothing here bounds the downstream cable/gate or complete Lprime, nor selects an operating point.

## 1. Fixed planes, exact propagation and source conventions

Use the inherited fixed real B projectors P,C on both old and new ports, identified channel by channel at each window. Old-port origins are m=0, the converter planes are m=40, and new-port origins are their first sites. The selected roots have unit modulus; old closed roots have |a|<=1/7. Let L=Q_old^40. Generalized old scattering is b=S_o a with S_o=T A^-1, inverse on the RIGHT. These are physical amplitudes, not closed flux-normalized vectors.

For a fixed new-port incident vector x=C_new x, ||x||<=1, the exact converter/source equations are

    a=R_o L² b+L U x, b=S_o a,
    F=(I-R_o L²S_o)^-1,
    a=F L U C_new x.                                  (2)

The outer OLD incoming coefficient is obtained without taking a growing-root norm:

    u_outer=L^-1 a=U C_new x+R_o L b.                  (3)

The identity uses the physical diagonal commutation of L,R_o,U, never commutation with S_o or F. Equation(3) cancels exactly forty powers before estimating the coefficient. The old response at those outer planes is

    Phi_old C_new x=Psi_B u_P+H_C v_C,
    u_P=P u_outer, v_C=C u_outer.                      (4)

Here Psi_B is the full finite old response to selected outer incidence and H_C=G_old(O,B)A_old^-1 C is the response to complementary OLD outer incidence. O contains all172 finite old head positions and B the two outer sites. Its exact kernel construction includes the boundary values; the auxiliary incoming-minus-outgoing completion is outside O. Thus(4) includes both selected cross-output and complementary recovery, without assigning infinite growing waves a Hilbert norm.

## 2. Checked finite old derivatives and converter ingredients

The checked direct-core/converter arguments supply

    ||Psi_B||<30, ||Psi_B'||<1e12,
    ||H_C||<160, ||H_C'||<2e24,
    ||S_o||<1.000001, ||S_o'||<4e22.                   (5)

H_C' and S_o' use the actual canonical old-k analytic disks of radius1e-12 and finite matching/Green bounds, followed by |dk/dE|<40. They do not follow from the much smaller real values in(5). No new analytic converter neighborhood is assumed. These are physical E derivatives at fixed hardware and fixed input vectors.

For completeness the real converter derivatives needed here are reconstructed. On a closed channel

    H=epsilon-J-j+Ja+(tau²/j)w,
    U_C=-tau(1-w²)/H,
    R_c=-(J-j-Ja+J S0 w)/H.

The exact checked bounds |H|>.1797, |H'|<1.157, |w|<1/60, |w'|<.104, tau<.007 give

    ||U_C||<.04,
    ||U_C'||<=.007[2(.104)/[60(.1797)]
                         +(1+1/3600)1.157/.1797²]<1.

The existing quotient calculation gives ||R_c||<.2, ||R_c'||<3. On selected channels |r_o|<4.88e-6 and |r_o'|<230. These derivative bounds come from the actual interface quotient, not small reflection values. All signed closed roots are retained.

Since 7^40>1e32, fixed-projector differentiation gives

    ||L_C||<1e-32,
    ||L_C'||<=40*5*7^-39<1.4e-29,
    ||L||=1, ||L'||<1600.

Also ||R_o L²||<4.881e-6 and ||F||<1.000005. Differentiate the exact factor in(2):

    F'=F[R_o' L²S_o+R_o(L²)'S_o+R_oL²S_o']F.

Using ||(L²)'||<3200 and(5),

    ||R_o' L²S_o+R_o(L²)'S_o+R_oL²S_o'||
        <230*1.000001+.2*3200*1.000001
                                    +4.881e-6*4e22<1.953e17,
    ||F'||<1.954e17.                                (6)

This repeats the necessary elementary full-feedback derivative calculation rather than importing the unchecked selected scattering conclusion of909fef. Its old S_o' premise is already distinctly checked.

## 3. Full complementary incidence and induced selected coefficients

The driving origin coefficient J_in=L U C_new obeys

    ||J_in||<4e-34,
    ||J_in'||<1.4e-29*.04+1e-32<5.7e-31.

From(2),(6), with x fixed,

    ||a||<4.1e-34,
    ||a'||<1.954e17*4e-34+1.000005*5.7e-31<8.1e-17,
    ||b||<4.1e-34,
    ||b'||<4e22*4.1e-34+1.000001*8.1e-17<1.7e-11. (7)

The strict b value follows also directly from
1.000001*1.000005*4e-34<4.1e-34; it does not multiply the rounded a bound and claim unchanged slack. The huge source derivative in b' is multiplied by an actual40-step closed input factor. It is retained rather than called negligible by inspection.

Because U is channel diagonal, P U C_new=0. Equation(3) therefore gives the induced selected coefficient u_P=r_o L_P b_P. Its derivative includes all three factors, so

    ||u_P||<4.88e-6*4.1e-34<2.1e-39,
    ||u_P'||<230*4.1e-34
               +4.88e-6[1600*4.1e-34+1.7e-11]<8.4e-17. (8)

These selected outputs are present; they are not excluded because the incident vector was complementary. Their estimates cover mixing through the full S_o.

The closed outer coefficient is

    v_C=U_C x+R_c L_C b_C,
    v_C'=U_C' x+R_c' L_C b_C+R_c L_C' b_C+R_c L_C b_C'.

Consequently

    ||v_C||<.040001,
    ||v_C'||<1+3*1e-32*4.1e-34
                     +.2*1.4e-29*4.1e-34+.2*1e-32*1.7e-11
               <1.000001.                          (9)

The direct U_C incidence at the outer old plane is NOT damped by Q_old^40. Only its source-reflected return is. Accordingly the large H_C' term below must be paid against .040001, not against an invented tiny origin amplitude. This distinction is essential to the physical plane convention.

## 4. Complete old finite product derivative

Differentiate(4) at fixed real P,C and fixed x:

    (Phi_old C_new)'x
        =Psi_B' u_P+Psi_B u_P'+H_C' v_C+H_C v_C'.

All four terms are controlled by(5),(8),(9). Thus

    ||Phi_old C_new||<30*2.1e-39+160*.040001<6.5,
    ||(Phi_old C_new)'||
      <1e12*2.1e-39+30*8.4e-17
                         +2e24*.040001+160*1.000001<1e23.

The dominant term is the genuine finite old complementary Green derivative applied to direct outer incidence. Its Cauchy bound is deliberately coarse. There is no claim of intrinsic small derivative, complete source escape or useful runtime from(1) by itself.

All coefficients are maps on the full complementary two-new-port fiber. The input-input restriction needed by the cap is a contraction. Both physical windows have their own fixed P,C and the same ceilings; lower-lip conjugation in the fixed real basis gives the identical estimates. Conserved record/parity direct sums use maximum norm and passive-reference tensoring preserves these bounds. No channel-count factor or scalarization of the mixed old source is used.

## 5. Optional cap application: explicitly pending909fef review

The exact input cap factorization itself has completed distinct review. Its further numerical scattering-derivative proposal
`input_cap_scattering_derivative/PROPOSAL.md`, SHA909fef0047e8380d00e1807cf9d88b74b0ff6704600414c0192ab296cb96069b, is STILL PROVISIONAL here. Conditional on its claimed ceilings,

    ||alpha||<371, ||alpha'||<2e7,
    ||C alpha||<1.72e-35, ||C alpha'||<8.6e-31,

and the checked selected bound ||(Phi_old P)'||<5.1e11, the endpoint-forced OLD finite map obeys

    (Phi_old alpha)'=(Phi_old P)'Palpha+Phi_old P Palpha'
                  +(Phi_old C)'Calpha+Phi_old C Calpha'.

Use the existing checked conservative ||Phi_old P||<600, not an unproved new value. Then the full operator derivative is

    <(5.1e11)*371+600*(2e7)+(1e23)*(1.72e-35)+6.5*(8.6e-31)
    <1.9e14.                                       (10)

Equation(10) is doubly conditional on distinct checking of the present new complementary derivation and completion of the909fef check. It covers only the172-head OLD finite response. It does not cover the21 retained new-input sites, cable, gate, closed output tails or their later feedback. No complete Lprime or background-IBP substitution is made. The finite input sites should use their exact canceled power products, not Q_C^-n times a rounded tiny coefficient.

## Exposure and remaining scope

I authored the prepared converter derivative and recent909fef proposal, and checked the root cap factorization. Their origins and distinct-check scopes are explicit. The complete prepared converter source/check and two-converter composition were read in the immediately preceding task; their identities and physical-plane/finite H_C premises are reused here. The new argument derives complementary incidence separately instead of extending a selected-input theorem by notation. This is author work, not a self-check or independent recertification of the original calibration.

The original canonical finite analytic-disk and physical matching premises remain supplied and conditional. No numerical inverse, scientific execution, dynamics, quadrature, sweep, new operating point, W/Git/PR/publication/checkpoint/prompt/model change or delegation occurred. Only this proposal was created. Downstream attached-response derivatives remain separate obligations.

- `prepared_converter_direct_derivative/PROPOSAL.md`: `a444e105c88fcfad8fcae59b7f72d9dd9247e2b83ada73edeb7b97a849b33653`.
- `prepared_converter_direct_derivative_check/REVIEW.md`: `283494e3a50b12b77bf9d4be184452b49b582627fac20c802087e00e4d69e11d`.
- `prepared_core_direct_derivative/PROPOSAL.md`: `cfca9422163b4f4694a2efddbbff6779bd3c354bbd505e90af4d16189d1e40be`.
- `prepared_core_direct_derivative_check/REVIEW.md`: `75563597ec6edd1b688bfd81b51b4dc5b1adab7033d9f78a860f759cf5e70729`.
- `record_attached_recovery_sharp/PROPOSAL.md`: `07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11`.
- `bandcenter_converter_composition/PROPOSAL.md`: `1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78`.
- `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.
- `input_cap_factored_forcing/PROPOSAL.md`: `95755c3a08b6434a7ec7f86897a80f975c7575be747d1a9f09cdf34c9cce4376`.
- `input_cap_factored_forcing_check/REVIEW.md`: `85ad12b8df4b15a4abeeded5b28e84d1413f9ab848122ca0e45e0e09eece66d3`.
- `input_cap_scattering_derivative/PROPOSAL.md`: `909fef0047e8380d00e1807cf9d88b74b0ff6704600414c0192ab296cb96069b`.

Canonical original endpoint source SHA256: `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`; no new calibration or whole-note review.
