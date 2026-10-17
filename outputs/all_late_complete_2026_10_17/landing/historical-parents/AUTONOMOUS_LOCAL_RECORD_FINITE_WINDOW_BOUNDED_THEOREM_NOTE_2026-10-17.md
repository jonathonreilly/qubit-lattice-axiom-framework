# A local coherent record for a static autonomous output device

Status: conditional mathematical note prepared for review. The component and synthesis checks listed in the proof packet are complete; publication integration review is recorded separately. This note confers no retained audit status. All results remain conditional on the supplied exact Hamiltonian, initialization and original source-calibration premises.

A single additional qubit can serve as a coherent record in the specified static real two-body device. The infinite device has an absolute, unnormalized record1 output-map error below .0045 for every nonnegative time. Separately, its complete unconditioned state approaches the specified output within asymptotic error .001061. A finite version with 15,000,000,000,240 physical qubits has record1-map error below .004501 on [0,2×10^15], and record1 probability above .991 on [10^15,2×10^15]. These are sufficient dimensionless mathematical bounds, not practical resource estimates or a permanent halt.

The three conclusions have different scopes:

| Device and time domain | Claim | Comparator |
|---|---|---|
| Infinite, every t>=0 | Record1 branch operator error <.0045 | Common subnormalized outgoing packet, literal old operation, blank other registers |
| Infinite, t tending to infinity | Complete state-map limsup error <.001061 | Normalized outgoing packet with record1 |
| Finite, 0<=t<=2T, T=10^15 | Record1 branch operator error <.004501 | Same infinite-space subnormalized packet |
| Same finite device, T<=t<=2T | Record1 probability >.991 for every input | Conditional consequence of the branch and reference-concentration bounds |

Every operator statement includes arbitrary passive references. Absolute branch accuracy does not imply small normalized error at arbitrarily early, very unlikely successful reads.

The finite result is a record-selected branch/error-and-success theorem with tolerance .004501. It is not the earlier unattached complete unconditioned finite-output theorem at tolerance .001515. Their different error metrics and tolerances do not establish a same-quality speed or size improvement. In particular the .001061 asymptotic complete-state bound is not asserted at the finite observation time T.

## 1. Supplied physical construction

The old system consists of two qubits with K=2I+Z1Z2 and literal target

    W=[(9+12i)I+(-16+12i)X1X2]/25.

There is one shared pair of source qubits A,B, not one copy per arm. With n=(I-Z)/2 and a=|0><1|, its internal Hamiltonian is

    B=K+DeltaA nA+DeltaB nB
      +h_src(nA+nB-aA* aB-aB* aA)+u_AB nA nB
      +gA nA(I+X1)+gB nB(I+X2).

Head occupations at positions c0,c1 of each original arm supply contacts VA=lambdaA(I+XA)+mu0 I and VB=lambdaB(I+XB)-nu I, with the positive-block realization in the original source. The exact terminating-decimal coefficients are:

| J | h_src | gA | gB |
|---:|---:|---:|---:|
| .030021107107032 | 3.999349697888060 | .996878563816670 | .599319315560298 |

| lambdaA | lambdaB | mu0 | nu |
|---:|---:|---:|---:|
| 3.801781381581202 | 2.575033765788497 | .321494607058201 | 1.459892813020969 |

| DeltaA | DeltaB | u_AB |
|---:|---:|---:|
| 2.192035527016003 | 2.186826508897014 | .544607276405587 |

Put k0=2 arctan(1/4.510351185997098), C0=cos k0, S0=sin k0. The nominal new-lead parameters are

    j=J(1-C0), tau=sqrt(j J S0), kappa=10^-8,
    .0027<j<.003.

The inherited original arm filter at positions 20/21 uses hopping -J S0/C0 and diagonal shift -J/C0. Its positive vacancy coefficient is beta_f=J[(1+S0)/C0-1]. Converter vacancies have gamma_c=tau-j; original junction vacancies have gamma_J=(sqrt(2)-1)J. The scalar after adding the record gate is

    c_att=2nu+2beta_f+4gamma_J+4gamma_c
                             +4(sqrt(2)-1)j.        (1)

This is a global scalar, present before the head reaches the gate. K is retained in B and need not commute with the source contacts. Only the common scalar is factored from actual evolution.

For definiteness the cubic-lattice embedding uses old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0). Arm0 is (n,1,1), 0<=n<=36, followed by (36,1,2),(36,1,3),(37,1,3),(38,1,3),(38,1,2),(38,1,1),(39,1,1),(40,1,1). Arm1 is (n,1,-1), 0<=n<=41, followed by (41,2,-1),(41,2,0),(41,2,1). Both have 45 vertices. The junction ports are out=(41,1,1) and in=(40,2,1), with hopping block -JU for U=2^-1/2[[1,1],[1,-1]]. Retain old-J port sites out_m=(41+m,1,1), in_m=(40,2+m,1), 0<=m<=40. Each converter joins its last old site to the first new site. The input new sites are (40,43+n,1), 0<=n<=20; the emitter is (40,64,1). The retained output cable is v_n=(82+n,1,1), 0<=n<=17.

The new local gate is specified first in local coordinates. Its record is R=(0,0,0). Arm0 is (1,0,0),(2,0,0),(2,1,0),(1,1,0),(1,2,0),...,(1,8,0). Arm1 is (-1,0,0),(-1,1,0),...,(-1,8,0),(-1,8,1),(0,8,1). Each has eleven heads. Add ports p=(0,8,0), o=(1,8,1) and the four signed square bonds -jU. On arm1 replace bonds y=2--3 and y=5--6 by phase cells of hopping -sqrt(2)j, each with positive occupations (2-sqrt(2))j at its two endpoints. At each square site add vacancy (sqrt(2)-1)j(I-n). Couple both terminals to the SAME record by j n_T(I+X_R). Apply the rigid map

    F(x,y,z)=(108-y,1+x,1+z).

The actual gate input is (100,1,1), its output is (100,2,2), and its record is (108,1,1). Join v17 to the input by -j. Continue the final output ray as o_n=(100,2+n,2), n>=0. The gate origin o_0 is counted once. New gate vertices lie at first coordinate 100 through 108; old retained heads lie at first coordinate at most 99. The ray extension meets the gate only at o_0. All installed bonds and contacts are nearest-neighbor; extra geometric adjacencies remain uninstalled under the selective-coupling premise.

Every real head hopping h uses Q(h)=|h|(n_x+n_y)+h(a_x* a_y+a_y* a_x), PSD on all two-qubit occupations. The emitter bond is instead j(n_e+n_end)-kappa(exchange), with positive onsite j n_e; this gives both one-head diagonals 2j without a kappa-dependent compensation. All source, contact, occupation and vacancy terms retain their supplied positive realizations. The new terminal contacts are PSD on the full head/record space, of norm 2j each; their shared record incident load is 4j. Original large source loads remain present; no all-site norm cap of 2 is claimed. The delivered seed has the emitter occupied, all other heads blank, source vacuum and record0, with arbitrary old/reference input.

The exact inventories and full-space block identities are in the [resource proof](../outputs/attached_record_2026_10_17/source_checks/bandcenter_resources/PROPOSAL.md), [local gate](../outputs/attached_record_2026_10_17/source_checks/autonomous_record_route/PROPOSAL.md) and [attachment](../outputs/attached_record_2026_10_17/source_checks/record_attached_kernel/PROPOSAL.md). Their checks are preserved alongside them. These supplied coefficients and states are not derived here from native framework physics.

## 2. Exact map and reference packet

Let V embed the full four-dimensional old input into the delivered seed, and P_1 project only the record onto computational value 1, retaining every other coordinate. Define A_1(t)=P_1 exp(-itH_att)V. Head number is conserved; the theorem concerns the seeded one-head sector with its full shared internal system.

Let I_q=[pi/2-h,pi/2+h], h=4e-6, w=exp(iq), E(q)=2j(1-cos q), and

    D_ref=E(q)-2j+(kappa^2/j)w,
    rho_att=-i w^40 rho_n(q),
    F(q)=i E'(q) kappa rho_att w^21/
                             [sqrt(2pi)jD_ref].

The fixed common converter phase is rho_n=zeta exp(172ik(q)), where cos k=C0+(1-C0)cos q and zeta is the original single calibration phase. The eighteen-edge cable and gate contribute -i w^40. Define the unnormalized outgoing packet ONLY on the free ray n>=1:

    beta_t(n)=(1/sqrt(2pi)) integral_Iq
                             F(q)exp(iqn-itE(q))dq. (2)

The output origin n=0 remains in the finite gate budget. Let J_out embed the head packet with all other heads blank, source vacuum and record1. The ideal successful map is

    T_1(t)=exp(-it c_att) J_out[beta_t tensor exp(-itK)W]. (3)

It is common to all old inputs and references. Its packet is not renormalized to fit a finite device. The exact scalar reference measure gives p0=integral_Iq|F|^2>1-1.1e-6, with p0<=1; hence ||beta_t||<=sqrt(p0). The norm tends to sqrt(p0) asymptotically, not p0.

## 3. Why the complete all-time branch estimate holds

Use the SAME physical energy union I=I_1 union I_3 for all inputs and record sectors, where I_b has center c_att+b+2j and halfwidth d=2j sin h. Within each old parity the source fiber is eight-dimensional, including the other old vacuum energy and all six excited-source directions. On each window one channel is open and seven are closed. Both record-X sectors are retained coherently.

The exact gate matrix h_x has diagonal 2j except terminal entries 2j+jx and phase endpoints 3j. Its off-diagonals are the literal installed bonds. With decaying root z=2j-j(s+s^-1), the one-output gate load is D_x^R(z)=z-h_x+js P_o. The PLUS selfenergy sign follows from the free surface resolvent -s/j. The checked local inverse is <26/j on the selected real band and <1/(56j) in every inherited closed channel |s|<1/60. These bounds include all 24 gate sites. The input-plane return at v0 is s^36 r_gate; paying the possible 1/|s| factor in closed reflection gives <3*60^-36<1e-63. No open-channel unitarity is imposed on closed coefficients.

Full ordered source/load Schur elimination then supplies the attached endpoint and emitter inverses. Their finite matching chain excludes hidden in-band finite modes and gives continuous resolvent boundaries through both cutoffs. Comparing the full four-input seed matrix measure with four genuine shifted free-emitter chains proves that ALL omitted spectral state has norm <.001057, including outside point or singular spectrum. This is actual attached mass, not a reference-tail substitution. See [endpoint](../outputs/attached_record_2026_10_17/source_checks/record_attached_emitter_bound/PROPOSAL.md) and [seed matrix mass](../outputs/attached_record_2026_10_17/source_checks/record_attached_seed_mass/PROPOSAL.md).

The remaining represented state must be synthesized from BOTH spectral lips. For any finite coordinate restriction Q, its rectangular density is

    Q dE_H(Lambda)V/dLambda
       =[Q R^down(Lambda)V-Q R^up(Lambda)V]/(2pi i). (4)

Reality relates the lower column to the conjugate upper column in fixed real bases, not to the adjoint of the same rectangular column. On the open output ray the retarded coefficient A_x gives F_x=iE'A_x/sqrt(2pi), so (4) produces outgoing exp(iqn)F_x PLUS incoming exp(-iqn)conjugate(F_x), at the actual output-window energy. Record0-to-record1 takes their sector half-difference. This proves the sign and normalization rather than identifying an outgoing resolvent coefficient with the entire state.

The [corrected outgoing proof](../outputs/attached_record_2026_10_17/source_checks/record_attached_outgoing_profile/PROPOSAL.md) gives coefficient error <2.5e-6 on the full old-input space, including prepared inputs on the other physical energy window. Their actual phases remain indexed by output-window energy; K is never commuted through interacting evolution. Real conjugation supplies the same incoming coefficient error. The incoming IDEAL carries conjugate W eigenvalues, so it is bounded as an unwanted contribution rather than inserted into (3). The [incoming reference proof](../outputs/attached_record_2026_10_17/source_checks/record_incoming_alltime/PROPOSAL.md) bounds its positive-ray norm by .00105 for every t>=0. Its contour retains the actual carrier 61q+172k(q), both vertical sides and the cutoff tail.

The finite upstream/source/gate coordinates and complete closed tails are also paid. For emitter inverse T_x and background recovery L_x their sector difference is exactly

    Delta F_core=[kappa^2 T_+ DeltaG T_-;
        -kappa DeltaL T_- -kappa^3 L_+ T_+ DeltaG T_-]. (5)

The direct kappa DeltaL term does not cancel merely because endpoint selfenergies nearly agree. The [sharp physical recovery proof](../outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_sharp/PROPOSAL.md) and its check use actual source/filter amplitudes, terminated-input feedback and finite-site aggregation to obtain, on both lips,

    ||T_x||<1/[.98 sqrt(delta^2+gamma^2)],
    ||DeltaG||<1e-47+1.21e7|delta|,
    ||DeltaL||<22001+5.3e9|delta|,
    ||L_x||<4e5, gamma=kappa^2/j.

In particular closed incoming powers on the finite input and cable are combined with their return factors before norms are taken. The closed coefficient at cable n=0 is not called negligible. Geometric downstream tails are included separately from the non-square-summable stationary open wave. Integrating (5) with the jump factor and sector half-difference costs <.00108 per physical window, hence <.00216 across both windows; parity sectors are orthogonal. This is the complete represented local/closed contribution, before charging the omitted state.

Fourier isometry, positive-ray restriction and triangle inequalities now give for every t>=0

    ||A_1(t)-T_1(t)||
      <.001057+.00216+.00105+2*(2.5e-6)
      =.004272<.0045.                              (6)

The omitted state is charged once. Incoming and outgoing errors on the same ray are not assumed orthogonal. All bounds are operator estimates before an old/reference input is chosen. The [complete composition](../outputs/attached_record_2026_10_17/source_checks/record_attached_alltime_composition/PROPOSAL.md) and [distinct synthesis check](../outputs/attached_record_2026_10_17/source_checks/record_attached_alltime_composition_check/REVIEW.md) spell out the actual two-lip synthesis, energy-dependent closed projections and every aggregation factor. Publication integration review is recorded separately.

## 4. Separate asymptotic complete-state result

This conclusion concerns the UNPROJECTED state, not only the successful branch. On each compact physical window the finite-coordinate spectral density is Hilbert-space-valued L1. The entire closed tail also has that property because its roots are uniformly below 1/60 and its recovered amplitudes are continuous. Approximating such a density in L1 by finite sums of constant Hilbert vectors on intervals proves that its time Fourier transform vanishes in norm. This controls infinite closed tails, not just individual site limits.

The actual incoming open coefficient is compact-band L2. For a smooth approximation its phase -qn-tE(q) has derivative bounded away from zero on n>=1, uniformly by n+vt for v>.0053. Integration by parts, summing squares and L2 approximation show that its positive-ray norm tends to zero. The same argument on n<=0 for the outgoing reference shows ||beta_t||^2 tends to p0.

Each record-X sector has outgoing coefficient error <2.5e-6 relative to its signed ideal. Combining the initialized sector weights in their orthogonal ranges preserves that error bound without deleting record0. Adding the omitted state yields

    limsup_(t->infinity)||exp(-itH_att)V-T_1(t)||
                                      <=.0010595.

For a_t=beta_t/||beta_t||, the limiting normalization cost is 1-sqrt(p0)<5.6e-7. Thus the COMPLETE state-map error against record1, blank other registers and a_t tensor exp(-itK)W has limsup <.001061. This implies asymptotic record1 probability at least 1-(.001061)^2 uniformly in input. It supplies no quantitative onset for this stronger complete-state conclusion. Persistent outside-band residuals remain charged; actual error is not claimed to tend to zero.

## 5. A finite observation window and exact resources

The separately [checked reference-concentration proof](../outputs/attached_record_2026_10_17/source_checks/record_reference_outgoing_onset/PROPOSAL.md) gives, for T=10^15 and every t>=T, normalized outgoing-reference norm on n<=0 below 2.8e-6. Its shallow contour uses h_c=kappa^2/(4j^2), an L2 horizontal estimate and both cutoff sides:

    left_norm <2.01 exp(-.0053 t h_c)
                      +.75/sqrt(.0053t-104).

The poles lie deeper than 2h_c, and the changed phase growth 104 is paid. This is a reference result, not an independently inferred actual runtime. Combining it with (6) is the actual branch argument.

Choose M=15×10^12 BEFORE delivery. Retain final-ray sites n=0,...,M-1 and all upstream/gate heads. Delete its sole outgoing exchange bond and add cap j n_(M-1). Compression preserves that deleted bond's diagonal exactly; the cap is static and is not an absorber or switch. The finite count is

    heads=M+235, head edges=M+236,
    physical qubits=M+240=15,000,000,000,240,
    positive blocks=M+275=15,000,000,000,275.

The four shared old/source qubits and the one record are included once. Passive references are not apparatus qubits. These are counts for the specified decomposition, not minima.

For completeness the weighted transfer argument keeps all head-diagonal internal dynamics exact. Set f=0 throughout the finite core/gate and f(n)=n on the final ray. Conjugating the compressed Hamiltonian by exp(f) changes only ray hoppings in its imaginary part; its block row/column norm is <=2j sinh(1). The cut endpoint has f=M-1. Gronwall bounds its evolved seed amplitude by exp[-(M-1)+2j sinh(1)t]. A single-cut Duhamel integral, whose reverse orientation acts on zero omitted seed amplitude, gives

    ||U_infinity(t)V-embed U_M(t)V||
       <1.2 exp[-M+4jT sinh(1)]<10^-6,
                                       0<=t<=2T.   (7)

Here j<.003 and sinh(1)<1.2 put the exponent below -6×10^11. This is a complete state-map difference including returns; it does not drop source loads or K. It is the output-ray specialization of the [weighted finite-transfer theorem](HOPPING_CONTROLLED_FINITE_OUTPUT_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-17.md).

Projection contracts (7). The [corrected finite application](../outputs/attached_record_2026_10_17/source_checks/record_finite_herald_transfer/PROPOSAL.md) and its [distinct check](../outputs/attached_record_2026_10_17/source_checks/record_finite_herald_transfer_check/REVIEW.md) therefore give finite successful-map error <.004501 on [0,2T], against exactly the same infinite-space packet (3). For T<=t<=2T,

    ||beta_t||^2>1-1.1e-6-(2.8e-6)^2,
    ||beta_t||>.9999994.

Every unit old/reference input then has successful norm >.9999994-.004501>.99549 and record1 probability >.991. The same lower probability holds for mixtures. For success probability p>0, the normalized successful vector differs from the normalized ideal by at most 2*.004501/sqrt(p); its unhalved pure-state trace-distance bound is at most 4*.004501/sqrt(p), capped at 2. Input-dependent normalization is not treated as a linear channel. The unnormalized successful CP maps have reference-assisted diamond distance <=2*.004501. Failure remains an actual outcome.

## 6. Corrections, evidence and remaining scope

The source packet preserves the routes that matter for assessing this proof. A proposed odd geometric arm offset was replaced by the two positive phase cells; it is not used as an established general no-go. The outgoing proof corrected a false strict zero-floor center inequality and added previously missing prepared-input rows on the other energy window. The coarse recovery proof corrected an unjustified claim that closed cable amplitude at n=0 was negligible; the sharp proof pays it explicitly. The finite application changed an insufficient exp(20)>2^20 arithmetic witness to exp(21)>2^21; the actual exponent and resource choice did not change. The inherited weighted-profile center erratum remains included. These corrections are disclosed rather than attributed to earlier checks that did not catch them.

The source files are preserved byte-exact. [SOURCES.json](../outputs/attached_record_2026_10_17/SOURCES.json) records original recovery paths, hashes, packet destinations, proof roles and repository dependencies. Packet links use `../outputs/attached_record_2026_10_17/source_checks/`. The [original endpoint note](REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md), SHA71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff; [nominal converter note](NOMINAL_BANDCENTER_CONVERTER_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md), SHAf8480df631730d3e4e9fadb07b73486a1e02aec650511f7eae859ae2dabbe311; and [published weighted-transfer note](HOPPING_CONTROLLED_FINITE_OUTPUT_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-17.md), SHA735ec540842018f17ecde72b43d102f52dd76f9df65682eaaeec64498628c429 remain explicit repository dependencies, not silently copied or newly recalibrated results. Component and synthesis checks are complete; publication integration review is recorded separately.

Checks are selective same-model, source-exposed analytical reconstructions with overlapping ancestry, not blind/model-diverse certification. The note's author wrote the sharp recovery and all-time composition and earlier resource checks; those arguments have distinct checks, not self-endorsement through this synthesis. The all-time check arrived during preparation and was read completely. The gate center-inverse evidence includes an exact symbolic calculation and a separate exact rational continuant reconstruction, preserved with their scripts/results. No new simulation, dynamics run, numerical sweep or solver was performed for this note. No audit status is granted, and ancestral calibration, supplied state and native identification are not independently recertified.

All coefficients, source vacuum, record0 state and computational readout remain supplied premises. The results establish no native Record/preparation derivation, practical fabrication precision, physical time units, arbitrary coefficient family, permanent finite storage, irreversible latch, reset or reuse. The finite theorem is an observation-window theorem. Early relative herald accuracy remains unproved, and no narrow early-time obstruction is promoted here to a universal negative claim. A different model, measurement protocol or physical supplier would require its own analysis.
