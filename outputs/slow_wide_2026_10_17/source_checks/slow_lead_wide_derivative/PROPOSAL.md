# Wider receiver band: full inverse and direct forced derivative

Status: authored conditional analytical derivation, requiring a distinct check. On the wider positive-g domain below, the actual235-head emitter-free background satisfies

    ||R||<1.17e13,  ||R V_o||<6.5e6,
    ||R F||<6.47e17,
    sup ||L'(E)||<1.00068*(6.47e17+3.31e7/g)+3600.     (1)

Here F=R V_endpoint is the complete finite endpoint-forced column, and L additionally recovers every slow closed tail. The full inverse ceiling happens to retain the earlier relaxed number, but its changed gate portion is recomputed below. The narrow derivative ceiling is not transferred. No runtime, spectral mass, error target or receiver length is selected.

## Domain, exposure and source contract

Keep the exact supplied original source, calibration, converters, input cap,18-edge cable and24-head record gate, with

    .0027<j<.003, 0<g<=1e-6, 0<h<=4e-6,
    d=2j sin h, d/g<=.5.

The emitter is removed, retaining its input-endpoint diagonal. No kappa or H=d/gamma condition is needed for this background result. Work on each of the two physical old-energy windows, both parities and record-X sectors, and the full eight-coordinate forcing fiber. The slow connector remains sqrt(jg), every compensation occupation and diagonal remains the specified physical one, and the common scalar c_att is unchanged. K is retained inside the source; it is not commuted through any matching matrix.

I previously checked the narrow full-inverse, direct-action and synthesis arguments and authored some recovery and uniform-interface ancestors. I did not author the wider gate or endpoint sources. Root requested this changed-domain derivation and exposed the changed constants. This is author work with that exposure, not independent checking of itself or its ancestors. I read the complete wider-gate source/check and wider-endpoint source/check; initial truncated combined output was completed by bounded follow-up reads. The unchanged narrow sharp/direct arguments and my corresponding checks were already read completely in the immediately preceding coherent tasks. Original source/filter inverse and calibration premises remain conditional. The wider endpoint is contextual corroboration of regularity, not an imported emitter/mass bound in this proof.

No numerical inverse, scientific runner, sweep, solver, delegation, Git/W/PR, checkpoint, publication, model or editable-prompt change occurred. This proposal is the sole deliverable.

## 1. Unloaded arbitrary-forcing interfaces remain valid

Before the downstream gate load is imposed, none of the following objects depends on g. Their original q band is still u=|q-pi/2|<=4e-6. Consequently the full arbitrary-forcing proofs in the pinned sharp source remain applicable to these UNLOADED objects:

* O comprises90 original arm heads and82 old-buffer heads. The old kernel has full norm<5.2e9 and its two physical boundary columns together have norm<4e4. The latter uses original two-open-port recovery800 and explicit closed Q_old^40 decay, not selected-only forcing.
* Both converter updates retain D=J-j+J S0 Qn-JQ, ordered inverse bound142, and full172-head loaded kernel ||Gc||<3e10.
* G2 retains22 new input sites0,...,21 and18 output sites0,...,17, hence212 heads. The full eight-coordinate input deletion block Z=G2(21,21) satisfies ||Z^-1||<24. Its column is<130000, split into old-coordinate norm<120001 and new-coordinate norm<3220.
* After deleting input21 and its exterior, G_D acts on211 heads. Its full norm is<1.15e13. At a=v17 its column and transpose row have norm<C_a=220000 and ||G_D(a,a)||<401.
* The input-terminated source at v0 retains |S^D_PP|=1, ||S^D_CP||<2, ||S^D||<2e8 and ||Qn,C||<1/60. These are full generalized-source bounds, not closed-channel flux unitarity.

All these interfaces include arbitrary forcing at every retained finite head, not only the eventual endpoint column. Their proofs use complex transpose symmetry in fixed real coordinates; they do not assume normal boundary matrices. Changing only the subsequent slow boundary condition does not change them. The decomposition and improved disjoint lift used below are also exact for these same auxiliary objects.

## 2. Recompute the actual wide gate feedback

Let Rg be the24-head gate inverse with its actual slow ray eliminated and no artificial incoming selfenergy. The checked wider gate supplies

    ||Rg||<33/j,  j||Rg e_p||<6.28,
    |r_gate,P|<.129,
    ||Rg,C||<1/(56j).

The forced6.28 bound also includes the slow CLOSED tails; restricting it to finite gate coordinates is contractive. The raw closed reflection is not assumed bounded by3. Its root-dependent bound, for an old closed root s, is

    |r_gate,C| <=(1+1/(56|s|))/(1-|s|/56).

At last cable site a=v17 the physical update is

    Dg=-jQn-j^2 Gg,  Gg=e_p^T Rg e_p,
    ||Dg||<34j<.102.                                (2)

The signs compare E-H_up+jQn with E-H_up-j^2Gg. Set An=[j(Qn-Qn^-1)]^-1, Cg=I+AnDg and rho=-AnDg Cg^-1. Direct scalar algebra gives rho=Qn^2 r_gate. Thus the selected reflection at a is still<.129. On C,

    |rho_C| <=(|s|^2+|s|/56)/(1-|s|/56)<3,

uniformly for both signed roots, |s|<1/60. This bound is taken AFTER the one-edge round trip; it does not discard an inverse closed root. The regular input-loaded gate and its closed gap give existence of Cg^-1; exactly Cg^-1=I+rho, so ||Cg^-1||<4.

The free boundary kernel at a is An+Qn^17 S^D An Qn^17. Retaining the matrix order gives

    I+G_D(a,a)Dg=(I-Qn^17 S^D Qn^17 rho) Cg.         (3)

The PP, PC, CP and CC feedback block ceilings are respectively

    .129,  (2e8)*3*60^-17,
    2*.129*60^-17,  (2e8)*3*60^-34.

Their sum is<.1291. Hence the first inverse is<1/.8709<1.15 and

    ||(I+G_D(a,a)Dg)^-1||<4.6.                     (4)

Transpose symmetry gives the same norm for the reversed product. At v0 the return is Qn^36 r_gate, consistent with the actual18-edge reference plane. This full-fiber estimate includes closed forcing and does not multiply the whole2e8 scattering norm by the selected reflection.

Woodbury now gives the actual gate-eliminated upstream inverse Ru:

    ||Ru||<1.15e13+.102*4.6*(220000)^2<1.16e13,
    ||Ru(:,a)||<4.6*220000=1012000,
    ||Ru(a,a)||<4.6*401<1845.                       (5)

Restore all24 gate coordinates. With the physical off-diagonal j in E-H, the exact blocks are

    R_UU=Ru,
    R_UG=-Ru(:,a)j e_p^T Rg,
    R_GU=-Rg e_p j Ru(a,:),
    R_GG=Rg+Rg e_p j Ru(a,a)j e_p^T Rg.

Thus both cross norms are<1012000*6.28<6.4e6, and

    ||R_GG||<33/.0027+6.28^2*1845<86000.

Adding block norms proves ||R||<1.17e13 on all235*8 coordinates. For output port o, reciprocity gives j||Rg(p,o)||<6.28. The upper part of R V_o is<6.4e6 and its lower part<86000, hence

    ||R V_o||<6.5e6.                               (6)

No whole-internal multiplicity factor is omitted: each displayed bound is already an operator norm on the full fiber. Lower-lip conjugation preserves all estimates.

## 3. Actual wide recovery components

The wider-gate proof redoes source feedback with denominator>.8709, selected outgoing amplitude<460, closed outgoing amplitude<1280, selected incoming amplitude<59.34 and closed incoming amplitude<1280e-63. It derives the following complete actual endpoint-forcing components:

    original arms/buffers before return <240001,
    finite input before return <4670,
    total noncable upstream attachment correction <59341,
    cable <9000,
    gate plus complete closed tails <3270.

The cable bound explicitly pays its closed outgoing amplitude near v0; only at v17 is that amplitude suppressed by60^-17. These are full forcing-domain norms. Their sum<4e5 proves ||F||<4e5 and ||V_o^T F||<3270; no old2060 allowance survives.

Partition finite coordinates into O (172 old heads), N (21 retained input and18 cable heads), and G (24 gate heads), and let U=O union N. Restricting the attachment correction to each subrange gives

    ||F_O||<240001+59341<300000,
    ||F_input||<4670+59341<65000,
    ||F_N||<sqrt(65000^2+9000^2)<66000,
    ||F_U||<240001+4670+59341+9000<320000,
    ||F_G||<3270.                                  (7)

Paying the same total correction in both restrictions is conservative. The square sum for N uses orthogonal coordinate ranges, valid for an operator on arbitrary forcing input.

## 4. Direct inverse action on this actual F

Extend F_U by zero at input deletion site b=21, obtaining f on the212-head auxiliary space. This f need not solve auxiliary dynamics; the exact kernel identities act on arbitrary forcing. The two disjoint boundary supports give

    G2=diag(0,Dn)+J Gc J^T, J=[I;L_n],
    ||L_n||^2<=9*max(22,18)=198,
    ||L_n||<14.1, ||J||<14.2, ||Dn||<8800.

The transpose factor has the same Euclidean operator norm; it is not replaced by an adjoint. From(7),

    ||J^T f||<300000+14.1*66000=1230600,
    ||G2 f||<8800*66000+14.2*(3e10)*1230600
               <5.243e17.                         (8)

The deletion row acts on the actual partition as

    ||G2(b,:)f||<120001*300000+3220*66000
                 =36212820000<3.63e10.

Full Dirichlet deletion therefore gives

    ||G_D F_U||<5.243e17+130000*24*(3.63e10)
                    <6.38e17.                     (9)

Now apply the exact gate-load Woodbury action, in its ordered form from(2)–(4). Its final row obeys ||G_D(a,:)F_U||<220000*320000. Consequently

    ||Ru F_U||<6.38e17
       +220000*.102*4.6*220000*320000
                    <6.46e17.                    (10)

Restoring the gate action uses the full blocks just proved, not a new selected scalar approximation:

    ||(RF)_U||<6.46e17+(6.4e6)*3270,
    ||(RF)_G||<(6.4e6)*320000+86000*3270.

Their sum is<6.47e17, proving the direct-action part of(1). This is a bound on R acting on its actual endpoint-forced column, not a replacement for the full arbitrary-forcing inverse norm.

## 5. Differentiate the assembled equation, including all closed tails

After restoring every finite coordinate, the exact matching equation is

    M(E)F(E)=V_endpoint, R=M^-1,
    M(E)=E I-H_finite+j V_o Q_slow(E)V_o^T.

Physical coefficients and inclusions are energy independent. The eliminated slow surface has coefficient j because the connector square is jg. Thus

    F'=-RF-j R V_o Q_slow' V_o^T F.                 (11)

Every buffer/cable power and feedback derivative represented inside R is accounted for by this assembled identity. No value bound is merely asserted to bound a derivative.

On the wider domain sin k>=sqrt(15/16)>.968. Therefore the open root derivative is

    |v'|=1/(2g sin k)<1/(1.93g).

The closed-root derivatives are smaller by the fixed gap, so the same ceiling holds on the full fiber. The old1/(1.99g) ceiling is not used. Equations(6),(7),(10) yield

    ||F'||<6.47e17+(6.5e6)*[j/(1.93g)]*3270
             <6.47e17+3.31e7/g.                    (12)

For a closed slow root, the physical tail lift has entries sqrt(j/g)v^(m+1), m>=0, and |v'|=|v|^2/[g(1-|v|^2)]. The unchanged gap>.162 and g<=1e-6 imply |v|<=2g/.162. Summing the full geometric square series gives lift norm<.00068 and derivative norm<.009 uniformly on this wider domain. The seven closed channels combine by maximum, with fixed B projectors on each window. Differentiating the tail times the actual output value and using the safe ||F||<4e5 gives

    ||L'||<1.00068||F'||+.009*(4e5),

which proves(1). The open stationary ray is excluded because it is not square summable; every finite and closed coordinate remains. Local analytic root branches and the full finite inverse ensure ordinary differentiability through the closed real-window endpoints for each positive g. No uniform complex strip or value at g=0 is asserted. The envelope explicitly diverges as1/g; the domain requires h to shrink when g does.

## Scope and next check

This derives a uniform positive-g background derivative envelope on d/g<=.5. It does not attach the emitter, infer seed mass, identify the full traveling coefficient, integrate a complete-state error curve, choose a read time or finite receiver, or claim useful performance. The independently checked wider endpoint/emitter source remains a separate spectral interface. A temporal composition must still use its actual full-input mass/denominator constants and independently checked wider reference/coefficient estimates, paying both windows/lips and one omitted state. Exact finite compression by itself is not a performance theorem.

A distinct check should reconstruct the full feedback factor4.6 with rho=Qn^2 r_gate, the changed output column6.5e6, actual component bounds(7), all ordered deletion/load actions, the wider root derivative1/(1.93g), and the complete closed-tail product rule. The earlier narrow checks do not certify these new changed-domain calculations. No original source recalibration or retained audit status is claimed.

## Exact source identities

- Wider gate `slow_lead_wider_receiver_band/PROPOSAL.md`: `5b667173cd9ee3d8faa285e5856e8a89e8a83ae87f09207664cc5115e247ee57`; check `9c32a1c901300c32cb6d0630cfef19e9aa33b9438274b6ab8dc561ccc2a38b0d`.
- Wider endpoint, read for context, `slow_lead_wide_endpoint/PROPOSAL.md`: `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3`; check `c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5`.
- Unloaded physical columns and exact assembled derivative, `slow_lead_forced_derivative_sharp/PROPOSAL.md`: `662b64aa1d7714746abaa585f8e1af17ece308771b5c9de25f88fde03bb787c0`; my check `41f8ad9e18d7c1910f8a2c9b7cc70a2cb6b5a89ecbad47d52fd555b694718d4d`.
- Exact direct-action decomposition, `slow_lead_direct_forcing_refinement/PROPOSAL.md`: `f9fdcaa59e3b2d58805d295cb2dd63d4c7c763917ee8099b90afb2ec3c0db909`; my check `ea62892ef0105008e9aaebf80d53bb5a6f143b86425d8d3c6ec1c417f76e1e47`.
- Closed-tail derivative interface, `slow_lead_complete_onset_frontier/PROPOSAL.md`: `c590e093e7a4ca6abc1e147414f5ee5b08e725fa1a881b266fae7271b56e0d46`; check `5f8b8a3b4aea4008c07d9d8e59b53a7c58bf4cb0deead4d7da66be84a2c4a32b`.

Unchanged original/kernel, gate-center, converter and unloaded recovery ancestry is explicitly pinned in those complete sources; canonical original source SHA256 is `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`. Source identities are bookkeeping, not proof.
