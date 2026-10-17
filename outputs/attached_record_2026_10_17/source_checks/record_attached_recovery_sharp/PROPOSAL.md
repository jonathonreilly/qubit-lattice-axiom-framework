# Physical selected-input recovery and an attached finite-core envelope

Status: new authored conditional derivation, awaiting independent checking. On the fixed real band u=|q-pi/2|<=4e-6, the actual input-terminated source has selected incoming recovery

    ||K_U P||<1000,   ||S^D P||<3,                 (1)

where U contains all 193 noncable upstream heads. With the eighteen cable heads added, the attached background endpoint-forcing columns satisfy

    ||Delta L_up||<3e-24+2.8e7 u,
    ||L_up,x||<3e5,  x=+,-.                       (2)

The checked local gate plus downstream closed-tail recovery still gives each-sector norm <11000 and difference <22000. Thus the complete finite-core background column admits L0=4e5 and

    ||Delta L||<22001+5.3e9 |delta|,
    delta=E(q)-2j.                                (3)

The finite-core estimate also safely overbounds the separately charged downstream closed tails; it excludes the stationary propagating output ray. These are full-eight-coordinate forcing norms and both-lip bounds. They are not a scalar measure or a runtime theorem. A conditional integral consequence is given in section 6; actual omitted seed amplitude and spectral synthesis remain separate obligations.

## Sources and exposure

I authored the preceding coarse recovery derivation, not its attachment or gate sources. Root requested sharper physical recovery after seeing its unusable upstream slope. This is source-exposed author work, not independent verification. The coarse first draft remains `../record_attached_recovery_bound/PROPOSAL_v1.md` SHA256 `46785c5a9a9dbdec43d8457dd7c2361eb834431918d4bbdc81fcd4b5fca2ea98`. Root identified that its absolute cable closed amplitude need not be negligible at n=0. At root's explicit request I corrected that line to the safe <1.6e8 cable norm, preserving the first draft; corrected coarse source SHA256 is `395bad394b141cf6495b6c2505bc9c9be560f9e388867461b4f594388e05f1fe`. Its final coarse ceilings were unchanged. This new artifact does not silently repair or supersede an independently checked sharp result.

Read canonical original-note source/filter/finite-kernel passages completely at unchanged SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`, especially lines 145–319, in `correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`. The original calibration and M16 inverse premises remain conditional, not rerun.

Necessary complete readings reused unchanged:

- Two-converter composition `../bandcenter_converter_composition/PROPOSAL.md`, `1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78`.
- Endpoint/Dirichlet source `../bandcenter_converter_endpoint/PROPOSAL.md`, `22e7b4a9363a0c010ebce59f3235891708fd40eb5a5fa18f91b1a8878fe99c5a`.
- Wider band `../bandcenter_bandwidth_extension/PROPOSAL.md`, `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.
- Attachment `../record_attached_kernel/PROPOSAL.md`, `fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457`, and my check `7df395639ea91083d9321fd05f91ffbae94eb3ae87256beb09f7f4474fa2b005`.
- Gate inverse `../record_gate_center_inverse/PROPOSAL.md`, `3fb72f1629c0136531a41424683279a1b42f3a54bda4785359a367c018756c82`, and distinct check `cebb4153f1f1f75001614110ad7597fcf5b835ddad2ab15e0d57c1e089f0f67f`.
- Attached endpoint `../record_attached_emitter_bound/PROPOSAL.md`, `2b2161aabb84d533ac884d4199a72d6c4ff6745cd00599a20abe547b9c9caea9`; its now available distinct check `../record_attached_emitter_bound_check/REVIEW.md`, `30bb3f38752c5d6fc2b036042315c7ccb82f2f932805e04476e9a886822b6fa3`, was read completely.

The abstract operator interface is my `../record_core_operator_difference/PROPOSAL.md`, `69aa54015825bd6e240b1da5f856cb062157e2686d5403698592315fa4d529ac`. No scientific execution, solver, sweep, delegation, Git/W/publication/model/prompt/checkpoint change occurred. Only source inspection, hashes, this proposal and the explicitly requested narrow coarse correction were performed.

## 1. Physical source and filter amplitudes

First use a unit OPEN incoming amplitude on an original old-J arm. For the bare contact pair the matching right-hand side has norm E'_old<2J<.062. The inherited ||M16^-1||<166 therefore bounds the pair of terminal/contact amplitudes by 11. Elsewhere the bare wave is its unit incoming and unit reflected open components plus its decaying closed component, whose coefficient norm is <=16. Thus a safe per-site norm bound is 18. No source interaction is assumed to commute with K.

On the filtered arm, the scalar reference problem has the exact bare open reflection, of modulus one, as its terminating load. The filter has |a|<=5e-6 and |b|<=1. Multiple reflection gives the wave incident on its left port magnitude <=1/(1-|a|); the two waves there give site magnitude <=2/(1-|a|). At its right port unit incidence and a unit-modulus total reflection give magnitude <=2. Consequently the TWO filter-site scalar vector has norm <3. This replaces the loose inverse-only bound 1500 by a physical standing-wave bound; it does not use a small full closed-channel inverse without proof.

The canonical filter argument separately supplies

    ||x_P-x_P0||<1e8*7^-37,
    ||x_C||<5000*7^-18.

Together these imply the actual full two-site vector ||x||<5. This conclusion retains all seven closed coordinates and the original nonzero calibration; no exact W calibration is required to use unit reflection for a terminated self-adjoint bare arm.

The Dyson correction at an ordinary site n>=2 is G_g(n,{F,F+1}) V x. Each single filter-column block is bounded by ||A_old||+||T_g||<=246; concatenating two columns costs sqrt(2), giving <350. For the first two source sites the exact cross Green column is M16^-1 E_1 Q_old^(m-1), m>=1: this follows by solving the free recurrence and the same two-site boundary system. Its two-filter-column norm is at most 166 sqrt(2)<235, so the same 350 ceiling is safe there. Since ||V||<1/20, every site's correction is <87.5. The bare bound 18 yields per-site norm <106. Summing the 45 head sites on one arm gives <sqrt(45)*106<800. The unfiltered arm satisfies the same ceiling. Their direct sum and the real Hadamard lead transformation preserve this bound for a two-port open incoming vector of norm one. Shared internal source coordinates have not been duplicated.

For unit OPEN incoming new-port vector, the actual two-converter feedback gives old incoming open norm <chi/(1-rho_converter)<.5, and old incoming closed norm <1.2e-76. Use <800 on the former and the existing conservative <2e10 finite recovery on the latter. The actual finite old buffers have combined norm <40, including their closed returns. Therefore the full original finite arms plus both 41-site old buffers obey the convenient bound

    ||Phi_old P_twoports||<600.                    (4)

For arbitrary, possibly closed incoming new-port data keep the previously derived coarse ceiling ||Phi_old||<3e10. Its large complementary part will only multiply an explicitly small closed coefficient. Phi_old includes the 90 arm sites and 82 old-port sites, with all their internal coordinates.

## 2. Closing the input for one selected incident output wave

Let S_n be the full two-new-port generalized source matrix, ||S_n||<1.3. Its two-open-port block is unitary with reflection |R|<=r0=1e-20+12u<4.81e-5. The input cap after ell=20 imposes incoming coefficient

    alpha_in=-Q^42 beta_in.

Prescribe alpha_out=P f, ||f||=1, and no incoming closed output. Eliminate the input closed coefficient first. Its feedback inverse is bounded by 1/(1-1.3*60^-42)<2. Its correction to open scattering is less than 4*60^-42. The selected input denominator is at least 1-r0-4*60^-42. The transmission numerator has modulus at most 1+4*60^-42. Therefore

    |alpha_in,P|<1.0001,
    ||alpha_open,bothports||<1.5,
    ||alpha_in,C||<4*60^-42.                       (5)

The last inequality follows also directly from beta=S_n alpha and the preceding bounds. Thus (4) bounds old finite recovery by <901. On input sites n=0,...,20 use Q^-n alpha_in+Q^n beta_in. Its closed incoming part is -Q^(42-n) beta_in,C, so no growing-root norm is taken in isolation. Since ||beta||<1.3*(1.5+4*60^-42)<2, every input site has norm <4.1; their orthogonal sum costs sqrt(21)<5. Combining with 901 proves ||K_U P||<1000 for all 193 upstream noncable heads.

The same beta bound gives ||S^D_CP||<2 for the one-output terminated source. Its selected reflection modulus is exactly one by flux conservation and regularity. Hence

    ||S^D P||<sqrt(1+2^2)<3.                       (6)

Keep ||S^D||<2e8 for the complementary columns. This distinction is essential: the full generalized bound is not the physical size of a selected incident wave.

## 3. Full endpoint forcing and finite input recovery

For the emitter-free input endpoint forcing define the exact bracket

    B_br=I-Q Z^-1 Q(A+X),
    alpha=A Q^20 B_br.                             (7)

Then the finite original arms/buffers respond as Phi_old,in alpha, and the outgoing output coefficient is B_e=S_n,ba alpha. This follows either by Dirichlet deletion or by comparing T_ba Q^20 B_br with S_n,ba=T_ba A^-1. No factor is reordered past T_ba.

Replace X by its checked block-diagonal approximation X0; ||X-X0||<1e-32. The bracket perturbation is bounded by [24+24^2*201]||X-X0||<1.2e-25 (deliberately loose). On P the reference coefficient in (7) is exactly

    alpha_0,P=-w^21/[j(1+R w^42)] P,

so its norm is <400. On C its bracket is I-Q_C^2 and ||A_C||<6.18. Thus, for the FULL eight-coordinate forcing domain,

    ||P alpha||<400,
    ||C alpha||<7*60^-20+200*1.2e-25<3e-23,
    ||B_e||<1.3*(400+3e-23)<521.                  (8)

The original selected-row bound ||P B_e||<400 remains available. In particular (8) improves a whole forcing column, not just its selected input column.

Equation (4) now gives finite arms/buffers norm <240001. For input sites 0<=n<=20 the exact field, including its value at the forced endpoint, is Q^-n alpha+Q^n beta, beta=S_n,aa alpha. This is the left side of the Green kernel source solution; only the derivative/bond equation jumps at the source. For its incoming closed part retain the structure

    Q_C^-n alpha_C=A_C Q_C^(20-n) C B_br.

Since ||C B_br||<2, this norm is <13, even at n=20. The open incoming part is <400 and ||beta||<521. Thus every input site has norm <934 and their sum has norm <4670. This avoids the erroneous amplification of the unstructured tiny alpha_C bound by Q_C^-20.

## 4. Attached return, cable and sector difference

Use the checked same-plane return equations b_x=S^D a_x+B_e f and a_x=R_x b_x. Write rho=33u and ||R_x,C||<e_C=1e-63. The checked selected denominator >.99986 and ||P B_e||<400 still imply ||P b_x||<401. Combining (6), (8) with the closed inverse <2 improves the complementary response to

    ||C b_x||<2(2*rho*401+521)<1100,
    ||P a_x||<=401rho,   ||C a_x||<1100 e_C.       (9)

For U, the exact sector difference is K_U(a_+-a_-). Keep the coarse complementary norm ||K_U||<2e18, but apply (1) on its selected column. Consequently

    ||Delta L_U||<1000*802rho+(2e18)*2200e_C
                 <2.6466e7 u+5e-42.               (10)

The cable field is psi_x(n)=Q^n b_x+Q^-n a_x, n=0,...,17. Since Delta b=S^D Delta a, equations (6),(9) give ||Delta b||<3*802rho+(2e8)*2200e_C. The open incoming difference is <=802rho. For the incoming closed term the literal load formula gives, for every retained n,

    |s|^(36-n)|r_gate,x|<3*60^(-(36-n))<=3*60^-19.

Multiplying by the actual closed outgoing coefficient <1100 and paying both sectors and sqrt(18)<5 bounds this incoming closed difference by 33000*60^-19<1e-29. The entire cable difference is therefore <16040rho+1e-28<5.3e5u+1e-28. Adding (10) proves the first inequality (2) with slack.

For absolute recovery the cable closed outgoing coefficient is NOT negligible at n=0: use its <1100 bound explicitly. Every cable site has norm less than 401+1100+401rho+3300*60^-19<1502. Its total is <7510. For U the attachment adds at most 1000*401rho+(2e18)*1100e_C<54 to the unperturbed recovery of section 3. Summing all these finite coordinates gives

    ||L_up,x||<240001+4670+54+7510<3e5.

At n=17, unlike at n=0, the outgoing closed term is suppressed by 60^-17. Thus ||psi_x(v17)||<402 still holds. The checked gate recovery factor <26, and closed-tail geometric factor sqrt(1+1/3599), give each-sector gate-plus-closed-tail norm <11000 and difference <22000. Orthogonality of upstream and gate coordinate ranges yields the sharper square-sum if desired; summing their ceilings already gives (3) and L0=4e5. Since |delta|>=.0053u, 2.8e7u<=5.3e9|delta|.

## 5. Both lips and complete old/reference scope

All fixed matrices and coordinate embeddings are real; the record-X basis can be chosen real. The lower resolvent column is conjugate, in the corresponding domain/range conjugations, to the upper column. Every norm and sector-difference bound above therefore applies to both lips. This does not replace the rectangular-column spectral jump by an ordinary imaginary part. Actual synthesis still uses (F_down-F_up)/(2pi i), and requires its own absolute continuity and remainder statement.

The endpoint forcing domain is the full eight-dimensional fiber in each parity throughout. The selected P labels the channel open at that energy, not a deletion of other input directions. Passive-reference tensoring preserves the operator norms. K remains in B and the contact matrices; no old aging has been commuted through source recovery. The common c_att shift remains owed in a physical target. The two different old-energy windows within a parity must be integrated with their possible error overlap retained. Orthogonal parity sectors may be combined by a maximum.

## 6. Conditional finite-core spectral-integral consequence

This section only inserts the new real-band envelopes into the existing abstract interface. It assumes its actual spectral-jump regularity and an independently bounded omitted seed amplitude; neither is proved here.

For kappa=1e-8 let gamma=kappa^2/j and d=2j sin(4e-6)<2.4e-8. The checked selected emitter denominator is >.99 sqrt(delta^2+gamma^2). Its full block inverse is bounded by the usual Schur factorization,

    ||T_x|| <=(1+2406 kappa^2)^2/
                    [.99 sqrt(delta^2+gamma^2)]+6
             <1/[.98 sqrt(delta^2+gamma^2)].        (11)

For the last inequality use sqrt(delta^2+gamma^2)<2.5e-8; the complementary +6 term is then harmless. This retains all emitter directions. The checked full endpoint sector difference is <=1e-47+64000u, so use a_G=1e-47 and b_G=1.21e7 in energy coordinates. Equations (3) provide a_L=22001, b_L=5.3e9, L0=4e5 and c=.98 for the abstract integral bound.

Here d/gamma<720000, asinh(d/gamma)<15 and log(1+(d/gamma)^2)<28. Thus

    I_L < 2*22001*15+2*(5.3e9)*(2.4e-8)<660285,
    I_G < pi*1e-47/gamma+(1.21e7)*28<3.39e8.

The pi term is negligible since gamma>1e-16/.003. With pi>3.14, the abstract background contribution obeys

    kappa I_L/(2pi c)+kappa^3 L0 I_G/(2pi c^2)
       <.00108,

and its emitter contribution kappa^2 I_G/(2pi c^2)<6e-9. Their square sum is still <.00108 with the numerical slack above. This is per selected energy window. Summing the two windows in one parity gives <.00216 for the represented in-band finite-core record-1 map, plus the actual omitted seed amplitude (epsilon_++epsilon_-)/2. No orthogonality of those two error maps is assumed. The same bound holds under arbitrary passive references and combines across orthogonal parities by a maximum.

This is an all-time ABSOLUTE local-core bound conditional on spectral synthesis and omitted amplitude. It does not establish correct downstream W, eventual success, normalized relative herald error, readout at arbitrary time, native preparation or permanent storage. The constant gate term remains in the one-resonant-inverse recovery integral. Independent checking should focus on the physical filter-site bound, full forcing alpha structure, selected terminated-source recovery, growing-root cancellation on finite input/cable sites, and all numerical aggregation factors before using this candidate envelope.
