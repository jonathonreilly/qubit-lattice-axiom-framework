# Physical port columns and a forced background derivative

Status: new conditional analytical derivation requiring a distinct check. On the uniform slow-output real-band domain the complete235-head background inverse obeys ||R||<1.17e13 and its actual slow-output-port column obeys ||R V_o||<5e6. Differentiating the EXACT assembled forcing equation, rather than differentiating an unstructured inverse bound or scattering amplitude separately, gives

    sup ||L'(E)||
      <1.00068 [4.68e18+1.56e7/g]+3600.                (1)

At fixed g=1e-6 this is<4.7e18. This does not establish the previously illustrative1e17 certificate. No new actual-device runtime, mass or incoming decay theorem is asserted. The improvement over the coarse proposal is mathematical norm accounting, not a numerical search.

## Domain, sources and exposure

Keep the supplied source, two original converters, input cap, eighteen cable sites and24 gate heads, .0027<j<.003, 0<g<=1e-6, 0<h<=4e-6 and d/g<=.024 with d=2j sin h. Work on both physical windows, in each parity and each record-X sector, with the entire eight-dimensional internal fiber. Remove the emitter and eliminate the actual slow ray. All finite coordinates remain orthonormal physical coordinates. Literal shared K, scalar c_att and the real fixed source matrices are retained; no old-system phase is commuted through matching. The bound is independent of kappa because the emitter is removed.

The preceding coarse inverse proposal603919c0 is frozen and under separate check. Its exact load-update identities are restated here, with new physical-column estimates. I authored that proposal, checked several earlier components and authored attachment/resource work. Root requested the direct derivative and exposed the usefulness of physical port columns, then specifically suggested the original-port and blockwise gate refinements after I had found the two later port improvements. This is disclosed source-exposed author derivation, not independent checking. No desired derivative constant is assumed.

Complete sharp recovery, fixed recovery, converter composition/endpoint, bandwidth extension and onset arguments were refreshed in the preceding coherent task. This task additionally refreshed the complete corrected coarse recovery and uniform composition, with necessary original-port and gate premises. Exact identities appear below. Original M16/filter/kernel and calibration premises remain conditional; no original source recalibration, dynamics execution, sweep, W/Git/publication, prompt/model change or delegation occurred. The sole deliverable is this proposal.

## 1. Original172-head port columns before changing either tail

Let O contain90 original arm heads and82 old-buffer heads, the latter organized into41 two-port slices m=0,...,40. Let B be the two old sites at m=40. Start with both old-J tails outgoing. The original predeletion kernel supplies every physical block<3e7 and therefore

    ||G_old,OO||<5.2e9.                               (2)

The physical selected-incoming recovery on the90 original heads is<800 for a unit TWO-port open incoming vector. This is the actual original-J response from sharp recovery section1, before either converter or input cap: the filtered arm has per-site amplitude<106, its45-site norm<800, and the unfiltered arm obeys the same ceiling. Their direct sum and the real Hadamard transformation preserve the operator norm. It is not the later K_U bound for the changed apparatus.

Set Q=Q_old, A=[J(Q-Q^-1)]^-1 and S_old=T A^-1, with the two-port interpretation throughout. Their inherited bounds are

    ||A||<=40, ||A_C||<=50/9, ||A^-1||<20,
    ||Q_C||<=1/7, ||S_old||<1.0001, ||T||<41.

For forcing at B the incoming coefficient at the original port origins is A Q^40. Consequently the OPEN part of G_old(original90,B) has norm<800*40=32000. On the82 buffer coordinates the two-port slice kernel is

    G_old(m,40)=A Q^(40-m)+Q^m T Q^40.

For selected forcing each slice has norm<40+41=81; its stacked norm is<sqrt(41)*81<567. Thus

    ||G_old(O,B)P_twoports||<33000.                    (3)

For closed forcing the direct buffer term has stacked norm at most

    (50/9)/sqrt(1-1/49)<6.

The image term is bounded by sqrt(41)*41*7^-40. For the90 original heads, use the exact exterior column identity

    G_old(original90,B)=G_old(original90,ports0)Q^40.

The complete predeletion block bound gives ||G_old(original90,ports0)||<sqrt(180)*3e7<4.1e8. Thus its CLOSED restriction is<4.1e8*7^-40. These latter two terms are together<1. They retain all14 complementary directions across the two ports; no closed column is declared zero. Hence safely

    ||G_old(O,B)C_twoports||<8,
    ||G_old(O,B)||<4e4.                               (4)

Transpose symmetry in the fixed real basis gives the same bound for the row. All powers were combined BEFORE taking norms. No formal growing closed coefficient appears in(3)–(4).

## 2. Both converter loads and the whole finite lifted inverse

The physical diagonal update at each old m=40 boundary after eliminating its new-j tail is

    D=J-j+J S0 Qn-JQ, ||D||<.1.

Let C=I+AD and r=-AD C^-1, the exact old-boundary converter reflection. Closed denominator>5.99J>.1797 and ||A^-1||<20 give ||C^-1||<112. The open denominator>.024-.029h gives a smaller bound<3. All channels have ||r||<1/5; the open reflection is<4.88e-6. At B,

    G_old(B,B)=A+Q^40 S_old A Q^40,
    I+G_old(B,B)D=[I-Q^40 S_old Q^40 r] C.             (5)

This ordered factorization uses only commutation of the diagonal channel matrices A,D,Q; it does not commute S_old. The first inverse is<1.26 from ||S_old||<1.0001. Thus ||(I+G_old(B,B)D)^-1||<142. Woodbury and(2),(4) give the FULL arbitrary-forcing172-head loaded inverse

    ||Gc||<5.2e9+(4e4)^2*.1*142
            =2.792e10<3e10.                           (6)

Next retain22 input new sites0,...,21 and18 output new sites0,...,17, total40 new sites and212 finite heads. Before any input deletion, both new rays still have outgoing boundary conditions. Their free Dirichlet blocks are

    Dn(m,n)=An[Qn^|m-n|-Qn^(m+n+2)], ||Dn(m,n)||<400.

The exact lift from old boundary to each new site is (tau_c/j)Qn^(m+1), with norm<3. Let L_n denote the full40-site lift from O, supported on its two boundary coordinates. Even without exploiting the disjoint input/output support,

    ||L_n||<=3sqrt(40),
    ||[I;L_n]||^2=1+||L_n||^2<=361.

The full compressed kernel is exactly

    G2=diag(0,Dn)+[I;L_n] Gc [I,L_n^T].

This is a transpose factorization, not an adjoint factorization, but the two outer norms agree. The40-site Dirichlet norm is<40*400=16000. Therefore

    ||G2||<16000+361*(3e10)<1.1e13.                   (7)

This avoids multiplying a maximum block by212 after the lift. It includes arbitrary forcing at every retained old or new head and all internal coordinates.

## 3. Physical deletion column at input b=21

Let Phi denote recovery of the172 old heads from incoming NEW-port coefficients. The checked physical response bounds are ||Phi P_twoports||<600 and ||Phi||<3e10. The selected estimate includes actual scalar-filter amplitudes and converter velocity factors; the full estimate includes all closed incidence and canceled buffer powers, as in corrected coarse recovery section2. At b=21,

    G2(O,b)=Phi_in An Qn^21.

Since ||An P||<200, ||An C||<6.18 and ||Qn,C||<1/60,

    ||G2(O,b)||<600*200+(3e10)*6.18*60^-21<120001.

On any of the40 new sites the exact two-port kernel has norm<200+260=460, using ||Tn||<260. Stacking them costs<sqrt(40)*460<3220. Thus the FULL physical input-deletion column and its transpose row obey

    ||G2(:,b)||=||G2(b,:)||<130000=:C_b.               (8)

The complete8-by8 deletion block Z=G2(b,b) has ||Z^-1||<24 on the whole wider interval. For the retained211 heads, the ordered Dirichlet formula and(7)–(8) give

    G_D=G2(ret,ret)-G2(ret,b)Z^-1G2(b,ret),
    ||G_D||<1.1e13+24*(130000)^2<1.15e13.             (9)

This is exact deletion beyond the input endpoint20, with its diagonal2j. It introduces neither an emitter resonance nor an incoming-boundary approximation.

## 4. Physical last-cable column and actual gate feedback

Let a=v17 and U denote the193 upstream noncable heads. The exact source-to-ray kernel gives

    G_D(U,a)=K_U An Qn^17.

Here ||K_U P||<1000, ||K_U||<2e18, ||S^D_CP||<2, |S^D_PP|=1 and ||S^D||<2e8 are the unloaded, input-terminated source bounds, independent of g. Consequently

    ||G_D(U,a)||<1000*200+(2e18)*6.18*60^-17<200001.

For cable sites n=0,...,17,

    G_D(n,a)=An Qn^(17-n)+Qn^n S^D An Qn^17.

The free term is<200. In the image term, PP is<200, CP is<400*60^-n, PC is<(2e8)*6.18*60^-17, and CC has the additional60^-n. Hence every cable block is<801, and the stack is<5*801=4005. The COMPLETE last-cable column and row therefore obey

    ||G_D(:,a)||<220000=:C_a.                         (10)

At a itself both closed sides carry60^-17, so the sharper diagonal bound is

    ||G_D(a,a)||<401.                                 (11)

Let Rg be the complete24-head gate inverse with only its actual slow ray eliminated. Uniform gate bounds give ||Rg||<38/j and j||Rg e_p||<5.064, with all eight B fibers retained. Define Gg=e_p^T Rg e_p. Replacing the free j ray at a by the actual gate changes the upstream matching matrix by

    Dg=-jQn-j^2 Gg, ||Dg||<39j<.117.

For Cg=I+AnDg, the scalar-channel reflection rho=-AnDg Cg^-1 is at a, not p. Thus rho=Qn^2 r_gate; its return at v0 is Qn^36 r_gate. The checked margins imply |rho_P|<.0062, ||rho_C||<3 and Cg^-1=I+rho, so ||Cg^-1||<4. The exact factorization is

    I+G_D(a,a)Dg=[I-Qn^17 S^D Qn^17 rho] Cg.

Its four P/C feedback blocks have norm ceilings .0062, (2e8)*3*60^-17, 2*.0062*60^-17 and(2e8)*3*60^-34. Their sum is<.0063, so the entire inverse is<4.1. Transpose symmetry gives the same ceiling for the reversed product. This is full-fiber feedback, not a selected-only inverse assertion.

Let Ru be the loaded upstream inverse after eliminating the gate. Equations(9)–(11) now give

    ||Ru||<1.15e13+.117*4.1*C_a^2<1.16e13,
    ||Ru(:,a)||<4.1*C_a=902000,
    ||Ru(a,a)||<4.1*401<1645.                         (12)

Only the actual small port column is squared in the update. No whole inverse norm is squared.

## 5. Restore all gate coordinates without triangular overcounting

The full235-head inverse consists of blocks

    R_UU=Ru,
    R_UG=-Ru(:,a) j e_p^T Rg,
    R_GU=-Rg e_p j Ru(a,:),
    R_GG=Rg+Rg e_p j Ru(a,a) j e_p^T Rg.              (13)

The signs are those of the positive off-diagonal j in E-H; norm bounds do not remove the actual signs from the identity. Since j||Rg e_p||<5.064, (12) implies

    ||R_UG||=||R_GU||<902000*5.064<5e6,
    ||R_GG||<38/j+(5.064)^2*1645<60000.

Adding block norms safely yields

    ||R||<1.16e13+2*(5e6)+60000<1.17e13.             (14)

For the actual slow-output port o inside the gate, reciprocity gives j|Rg(p,o)|<=j||Rg e_p||<5.064. The upper part of R V_o is<902000*5.064, while its lower part is<38/j+(5.064)^2*1645<60000. Therefore

    ||R V_o||<5e6.                                   (15)

All these maps have full internal domains. Closed fibers are not removed, and there is no extra factor eight. They hold on either spectral lip by fixed real conjugation.

## 6. Differentiate the actual forced equation

Write the assembled finite matching matrix as

    M(E)=E I-H_finite+j V_o Q_slow(E)V_o^T,
    F(E)=M(E)^-1 V_endpoint.

The physical finite matrix and both coordinate inclusions are energy independent. All input-cap, cable, converter and gate coordinates have already been restored; Qn^n and original-buffer powers are descriptions of its inverse, not additional energy-dependent entries of M. Consequently exact differentiation gives

    F'=-R F-j R V_o Q_slow' V_o^T F.                  (16)

This equation accounts for the derivatives of EVERY earlier propagation factor and feedback denominator. It does not infer any derivative from a value bound, and it does not drop Q-power derivatives by pretending their coefficients are constant. Rather, it differentiates the equivalent assembled linear equations before choosing a norm bound. Differentiating the factored recovery instead would reproduce(16) after product-rule cancellations.

For the open slow root v, |v'|=1/(2g sin k)<1/(1.99g); fixed-gap closed roots have smaller derivatives. These are fixed-B spectral functions, so the projectors do not differentiate. Existing actual full recovery gives ||F||<4e5, and the actual gate-plus-closed-tail forcing estimate gives ||V_o^T F||<2060. Using(14),(15) in(16),

    ||F'||<(1.17e13)*(4e5)
                +(5e6)*[j/(1.99g)]*2060
           <4.68e18+1.56e7/g.                        (17)

The large1/g factor multiplies only the actual output-port column and value, not the whole inverse and complete recovery norm. For every fixed positive triple the roots and matching inverses continue locally across the real compact window; therefore F' exists in the ordinary finite-dimensional sense. No uniform complex-strip width is claimed.

The remaining complete slow CLOSED-tail lift has norm multiplier<.00068 and derivative norm<.009, as established in the checked onset interface by differentiating v^(m+1) and summing its full geometric square series. Combining finite and closed-tail ranges by a safe triangle estimate gives(1). On g=1e-6,

    1.00068*(4.68e18+1.56e13)+3600<4.7e18.

The estimate applies to both physical windows, all prepared and complementary forcing directions, both parities and record sectors, and arbitrary passive references. The propagating stationary ray is not square summable and is not included in L; its actual incoming/outgoing Fourier terms remain separate in temporal composition.

## Scope, losses and next check

This proposal supplies a much smaller explicit derivative than the coarse603919c0 route. It remains above1e17 and makes no assertion that the illustrative complete error or time in the onset frontier follows. Any temporal use must insert this actual ceiling into that checked real-energy integration-by-parts expression, retaining both hard-cutoff endpoints, both lips, both physical windows, the one omitted state and the actual incoming bound. A separately authored incoming refinement has been mentioned by root but was not read or imported here.

The main remaining loss is the general original-source kernel norm and full lifted response acting on F in the first term of(16). A sharper direct action estimate for R F could improve it without changing the apparatus. The estimate is a sufficient upper bound, not a resource or precision lower bound; failure to reach a preferred ceiling is not a no-go.

Distinct checking should focus on the ORIGINAL open port recovery800 used in(3), the closed Q_old^40 column identity, the transpose lift in(7), physical selected deletion/cable columns(8),(10), actual one-edge gate reference-plane shift, and the assembled derivative identity(16). No hash inventory is a substitute for those checks. The coarse frozen proposal is not edited or treated as independently certified by this new note.

## Exact identities

- `slow_lead_background_derivative/PROPOSAL.md`: `603919c05d1ade774f478474b0d09ee781bf298918d3ebc19b37e7eac6c22020`.
- `record_attached_recovery_sharp/PROPOSAL.md`: `07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11`.
- `record_attached_recovery_sharp_check/REVIEW.md`: `cbd5dfd29fbe67ad36c3ffc97a896f55ea30b8a5af367930c48a080589523430`.
- `record_attached_recovery_bound/PROPOSAL.md`: `395bad394b141cf6495b6c2505bc9c9be560f9e388867461b4f594388e05f1fe`.
- `slow_lead_recovery/PROPOSAL.md`: `f0f39510b65133d8399720c53ce2822bfe60a378ab2e50e1773a3dc8d0fe880f`.
- `slow_lead_recovery_check/REVIEW.md`: `488d0a9e8871f77f40d44803ee9bfe7fda25388c66b367944eea3376f51f5195`.
- `bandcenter_converter_composition/PROPOSAL.md`: `1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78`.
- `bandcenter_converter_endpoint/PROPOSAL.md`: `22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a`.
- `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.
- `slow_lead_gate_load/PROPOSAL.md`: `c1e1fe95ca3c9d390df0fad468c80c93d4c1c2aa1e3fee4c93c4326f44b0e61d`.
- `slow_lead_gate_load_check/REVIEW.md`: `8fb22bfddeeda9dd8abd1f3c90bafe4fd34916ec385d47aa017c99b08b221a65`.
- `slow_lead_uniform_endpoint/PROPOSAL.md`: `c8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887`.
- `slow_lead_uniform_endpoint_check/REVIEW.md`: `f3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0`.
- `slow_lead_uniform_composition/PROPOSAL.md`: `8cd26edcb7941d8254494480455d17c137652ec779e37e78901de5a04e71ac9e`.
- `slow_lead_uniform_composition_check/REVIEW.md`: `b873ac37d8a327f27491f36e80dfe5e8aeef7eb0d7b405bba6b70a6ffb9e71a7`.
- `slow_lead_complete_onset_frontier/PROPOSAL.md`: `c590e093e7a4ca6abc1e147414f5ee5b08e725fa1a881b266fae7271b56e0d46`.
- `slow_lead_complete_onset_frontier_check/REVIEW.md`: `5f8b8a3b4aea4008c07d9d8e59b53a7c58bf4cb0deead4d7da66be84a2c4a32b`.
- Original source note: `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`; original source/filter/kernel passages refreshed in the preceding coherent task. No blanket re-audit of the note is claimed.
