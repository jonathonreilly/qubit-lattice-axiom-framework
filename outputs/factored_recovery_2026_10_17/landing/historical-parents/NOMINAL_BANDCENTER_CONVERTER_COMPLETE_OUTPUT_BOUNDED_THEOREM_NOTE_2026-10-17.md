# Nominal converted autonomous output: a conditional complete-device bound

Status: conditional mathematical support, assembled from the full frozen arguments and selective checks linked below; prepared for separate integration review. No retained audit status is asserted.

For the exact supplied static Hamiltonian and delivered product seed defined here, set T=10^17. The infinite-output device approximates the specified complete output isometry with operator error <.001514 for every t>=T. One finite device with M=1500000000000000 new-output sites, fixed before delivery, has complete error <.001515 for every t in [10^17,2*10^17], after embedding into the infinite comparison space. These statements include arbitrary old inputs entangled with any passive reference, every source/emitter/clock output, the common physical scalar and the prescribed full old aging. Unhalved trace-distance ceilings are .003028 and .003030 respectively.

The conclusion is a mathematical implication for exact supplied data. It does not derive those data or the pure seed from native framework physics, establish physical time/energy units, prove coefficient-error robustness or claim permanent finite halting. The finite count remains enormous. The full [composition argument](../outputs/bandcenter_converter_2026_10_17/source_checks/converter_finite_composition/PROPOSAL.md) and its [integration check](../outputs/bandcenter_converter_2026_10_17/source_checks/converter_finite_composition_check/REVIEW.md) supply the final interface; the component proofs, not their status labels, are imported with their hypotheses.

## 1. Exact supplied physical construction

Let n=(I-Z)/2 and a=|0><1|. Use two old qubits 1,2 and one shared source pair A,B, at (0,0,0),(1,0,0),(0,1,0),(1,1,0), respectively. The source pair is not copied on the two clock arms. Define

    K=2I+Z1 Z2,
    B=K+DeltaA nA+DeltaB nB
       +h(nA+nB-aA* aB-aB* aA)+u_AB nA nB
       +gA nA(I+X1)+gB nB(I+X2),
    VA=lambdaA(I+XA)+mu0 I,  VB=lambdaB(I+XB)-nu I,
    W=[(9+12i)I+(-16+12i)X1X2]/25.

An asterisk denotes adjoint. The following terminating decimals are exact supplied values, not rounded fits introduced here:

| Parameter | Value | Parameter | Value |
|---|---:|---|---:|
| J | .030021107107032 | h | 3.999349697888060 |
| gA | .996878563816670 | gB | .599319315560298 |
| lambdaA | 3.801781381581202 | lambdaB | 2.575033765788497 |
| DeltaA | 2.192035527016003 | DeltaB | 2.186826508897014 |
| u_AB | .544607276405587 | mu0 | .321494607058201 |
| nu | 1.459892813020969 | q0 | 4.510351185997098 |

Set k0=2 atan(1/q0), C0=cos(k0), S0=sin(k0), and E0=2J(1-C0). With D=40, the first head arm consists of (n,1,1), 0<=n<=36, followed by

    (36,1,2),(36,1,3),(37,1,3),(38,1,3),
    (38,1,2),(38,1,1),(39,1,1),(40,1,1).

The second consists of (n,1,-1), 0<=n<=41, followed by (41,2,-1),(41,2,0),(41,2,1). Both have 45 vertices indexed 0,...,44. Their endpoints and the port origins out=(41,1,1), in=(40,2,1) form the four-edge junction square. Its hopping block from arm ends to ports is -JU with U=2^(-1/2)[[1,1],[1,-1]], in the canonical arm/port ordering. Every magnitude is J/sqrt(2); the canonical ordering fixes its one positive sign. Other arm hoppings are -J except the second-arm bond 20--21, which has hopping -t_filter, where t_filter=JS0/C0.

On each port retain old-J vertices m=0,...,40 at

    out_old(m)=(41+m,1,1), in_old(m)=(40,2+m,1).

Attach exactly two converter bonds from m=40 to new n=0, followed by new-j leads:

    j=J(1-C0), tau=sqrt(j J S0), gamma_c=tau-j>0,
    out_new(n)=(82+n,1,1),
    in_new(n)=(40,43+n,1), n=0,...,20,
    emitter=(40,64,1), kappa=10^-8.

New-output n runs over all nonnegative integers in the infinite device, or 0,...,M-1 in the finite device. Installed edges follow these paths; unused geometric nearest-neighbor adjacency does not install an interaction. All specified physical interactions are nearest-neighbor and at most two-local on this cubic embedding.

For clarity the positive block decomposition is part of the specification. Every ordinary hopping r uses Q(r)=|r|(nx+ny)+r(exchange), PSD with norm 2|r|. The seven displayed positive internal blocks summing to B occur once. At positions c0,c1 of each arm put

    lambdaA n_c0(I+XA), mu0 n_c0,
    lambdaB n_c1(I+XB), nu(I-n_c1).

These reproduce the head-conditioned VA,VB and scalar 2nu. Add J n_c0 at both entrances; beta_filter(I-n) at the two filter vertices, with beta_filter=J[(1+S0)/C0-1]; and gamma_J(I-n) at the four junction vertices, with gamma_J=(sqrt(2)-1)J. Each converter has Q(-tau) and gamma_c(I-n) on both its vertices. The full-space identity

    Q(-tau)+gamma_c[(I-nx)+(I-ny)]
      =2gamma_c I+j(nx+ny)-tau(exchange)

fixes its relative diagonals, not just its hopping. The emitter bond is the distinct structured PSD block j(ne+nend)-kappa(exchange), with additional j ne; both emitter and input endpoint have relative diagonal 2j. Its eigenvalues are 0,j-kappa,j+kappa,2j. Finally add j n_(M-1) at the finite-output cap. This cap exactly restores the removed ordinary bond's retained diagonal contribution, so H_M is the one-head compression of H_infinity, even for M=1. It adds no scalar.

The common scalar, with K still inside B, is

    c_total=2nu+2beta_filter+4gamma_J+4gamma_c.

All coefficients are static. The source incident-block norm loads remain 27.936224853155858 and 22.228906875353305; no all-site cap 2 is claimed. The full [resource construction](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_resources/PROPOSAL.md) and [check](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_resources_check/REVIEW.md) give the complete block inventory and load accounting. There are M+194 head qubits and head edges, M+198 physical qubits and M+223 positive blocks in that decomposition. At the selected M the physical count is 1500000000000198. Passive references are excluded, and the positive-block count is not claimed minimal.

## 2. Seed, spectral band and literal comparison target

The delivered seed has one occupied emitter, every other head qubit blank and sources in |00>, tensored with an arbitrary old input and passive reference. Let V_seed denote this embedding. Head number is conserved, so the analysis uses the invariant one-head space with the entire shared old/source fiber. The source registers are not constrained to remain vacuum during physical evolution.

Use the new comparison interval I=[pi/2-Delta,pi/2+Delta], Delta=4*10^-6, and

    E(q)=2j(1-cos q), cos k(q)=C0+(1-C0)cos q.

The branch k(q) is near k0. Energy margins show |E-E0|<2.4*10^-8, smaller than both original certified old-band edge margins 2.5*10^-8; hence |k-k0|<.96*10^-6 within the original k halfwidth 10^-6. The larger new-q cutoff does not enlarge that original source domain or change the Hamiltonian.

Define the exact scalar reference and its common phase by

    Dref(q)=E(q)-2j+(kappa²/j)exp(iq),
    rho_n(q)=-exp(80ik(q))rho_g(k(q)),
    Fref(q)=i kappa E'(q) exp(21iq)rho_n(q)
                         /[sqrt(2pi)j Dref(q)],
    p0=integral_I |Fref(q)|²dq, f=Fref/sqrt(p0).

The canonical fixed phase is rho_g(k)=-zeta exp(92ik), with zeta fixed by the canonical single reference calibration, not fitted to each old column. Thus the total packet phase is 21q+172k(q)+constant. Define the full lattice Fourier packet

    b_t(n)=(1/sqrt(2pi)) integral_I
                           f(q)exp(iqn-itE(q))dq, n in Z.

For t>=T its restriction to n>=0 has nonzero norm; beta_t is this restriction divided by its positive norm. It is an infinite-output comparison packet, not a finite-M renormalization. The target isometry Q_t places beta_t on output, blanks all other head/source registers, applies exp(-itK)W to the old input, and multiplies by exp(-it c_total), with identity on the passive reference.

K need not commute with the interacting source. Its factor in Q_t specifies target aging; it is never factored from the actual interacting evolution. The error is a fixed-phase vector/isometry norm, not merely a transition probability or a phase-optimized density comparison.

## 3. Imported proof chain and complete infinite bound

The packet incorporates the following complete arguments and their exact domains. The source hierarchy is substantive: source calibration and full finite-core regularity are premises; small open scattering error alone would not supply actual spectral mass or exclude dark in-band states.

1. [Nominal converter composition](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_converter_composition/PROPOSAL.md), with its [check](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_converter_composition_check/REVIEW.md), retains one open and seven closed directions in each selected parity/energy fiber, the full ordered generalized scattering relation and all source/buffer recovery. Closed feedback is bounded, not set to zero at band center.
2. [Endpoint/emitter construction](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_converter_endpoint/PROPOSAL.md), with its [check](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_converter_endpoint_check/REVIEW.md), supplies exact ordered Dirichlet deletion, the full eight-coordinate Schur inverse and local spectral-jump identity. The check's finite-matrix argument identifies the actual in-band seed density as |F_j(q)|²dq and excludes singular in-band mass under the stated complete-core premises. It does not discard out-of-band point mass.
3. The self-contained [free reference measure derivation/check](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_reference_measure_check/REVIEW.md) proves the equal-diagonal reference has total mass one and its hard-band tail formula. [Pointwise weighted-profile analysis](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_weighted_profile/PROPOSAL.md) and its [check](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_weighted_profile_check/REVIEW.md) connect that reference to actual mass by integrating a positive lower bound on actual density. Reference mass is not substituted for actual mass.
4. The final [wider-band proof](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_bandwidth_extension/PROPOSAL.md) and [check](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_bandwidth_check/REVIEW.md) re-establish changed-domain inverse margins. They give |F_j/Fref-omega_p|<1.8*10^-13+220|q-pi/2|, p0>1-1.1*10^-6, actual exterior mass <1.13*10^-6 and weighted coefficient norm <9.6*10^-7. Paying actual exterior amplitude, coefficient mismatch, positive normalization and possible within-parity error overlap yields initial operator error <.001510.
5. The corrected [narrow temporal argument](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_temporal_route/PROPOSAL.md) and [check](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_temporal_check/REVIEW.md) supply the complete-column contour mechanism and direct incoming-transform bridge. The [wide temporal proof](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_wide_temporal/PROPOSAL.md) and [check](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_wide_temporal_check/REVIEW.md) re-establish the complex reflection/return, projected deletion inverse, complete source-forcing and cutoff-side estimates on the actual wider domain.

In the last step the initial comparison is derived directly for the conjugate-incoming packet from the real seed's actual incoming coefficient conjugate(F_j). Arbitrary input coefficients are then extended linearly, not conjugated. The outgoing mismatch is paid once, contributing <2*10^-6 and giving static subtotal <.001512. All finite source/emitter/converter coordinates and entire closed tails remain in the localized column. The interacting strip depth is 10^-13; the distinct scalar contours are not an extension of that interacting domain.

Explicitly, with s_t=.0053t-64, the wide proof gives

    E_loc(t)<1.26*10^13 exp(-5.3*10^-16 t)+1.21*10^11/t,
    q_in(t)<.003 exp(-2*10^-6 s_t)+.75/sqrt(s_t),
    q_-(t)<1.5*10^6 exp[-s_t/(3.6*10^11)]+.75/sqrt(s_t),
    ||U_infinity(t)V_seed-Q_t||
        <.001512+E_loc(t)+q_in(t)+q_-(t)².               (1)

The last inequality requires s_t>=1 and q_-<1. Both cutoff sides and phase derivative 64 are included. Positive normalization of the ideal output restriction costs at most q_-²; it is not postselection of the physical state. At every t>=10^17 these envelopes decrease and yield

    error <.001512+1.21*10^-6+10^-9+4*10^-8+1.6*10^-15
          <.001514.                                   (2)

The specified infinite theorem is thus a complete all-old/reference bound. The underlying canonical source remains a conditional repository dependency: [the original endpoint note](REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md), SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff, associated by the root with PR9672 head e0835b2d048c9fa25bf8f1371993af628702e275. Its fixed-band calibration, real kernels and small complex disks are not recreated or broadened by this assembly.

## 4. Exact finite transfer and composition

The [output-only weight proof](../outputs/bandcenter_converter_2026_10_17/source_checks/output_lead_weight/PROPOSAL.md) and its [check](../outputs/bandcenter_converter_2026_10_17/source_checks/output_lead_weight_check/REVIEW.md) are self-contained for this step. Set the weight exponent f=0 on the entire core/input/buffers and first new-output vertex, and f(n)=n on the new-output ray. Only new-j output edges have nonzero weight gradient. In the finite one-head space, W_a=diag(exp(af)) commutes with every onsite internal block, and

    ||Im(W_a H_M W_a^-1)||<=2j sinh(a).

This keeps noncommuting K/source dynamics exactly; it is not a small bound on the whole Hamiltonian or a reduction of physical loads. Weighted norm growth bounds the last-site amplitude by exp[-a(M-1)+2j sinh(a)|t|]. Exact cap compression and single-cut Duhamel then give, for any integer M>=1, a>0 and real t,

    transfer <=min{2, exp[-a(M-1)]
                    [exp(2j sinh(a)|t|)-1]/[2sinh(a)]}. (3)

Only the retained-to-omitted edge acts on the decoupled finite state, so no extra factor two enters the forcing. At M=1 the actual weighted imaginary part is zero and (3) is valid, though loose. This bounds complete state maps and includes subsequent returns and all spectral components.

At a=1 and 0<=t<=2T, (3) is at most 1.2 exp[-M+4jT sinh1]. For the stated M and T, j<.003 and sinh1<1.2 imply exponent <-6*10^13, hence transfer <10^-6. Intersecting this horizon with (2) and taking the triangle inequality in the same infinite comparison space gives

    ||embed U_M(t)V_seed,M-Q_t||<.001514+10^-6=.001515,
    t in [10^17,2*10^17].                              (4)

No target tail is clipped to M sites. Arbitrary passive references preserve both operator bounds; their unhalved trace-distance counterparts are at most twice the errors. The finite theorem is restricted to this window, even though the infinite bound holds for all later times.

## 5. Comparisons with their actual status and tolerance

| Conditional certificate | Onset T | Output sites M | Infinite / finite error ceilings | Status of this particular choice |
|---|---:|---:|---:|---|
| Original nominal endpoint | 3*10^17 | 1.5*10^19 | .000320 / .001320 | Canonical PR9672 choice, root-reported published source |
| Original nominal endpoint, shorter output | 3*10^17 | 6*10^16 | .000320 / .001320 | Published in regular PR #9673 at b52801a596fefcda521a5df067f9b5dd3a158a13 |
| This nominal converted device | 10^17 | 1.5*10^15 | .001514 / .001515 | Selectively checked composition; this publication assembly awaits integration review |

All inequalities are strict and finite windows are [T,2T]. The [checked original shorter-output application](../outputs/bandcenter_converter_2026_10_17/source_checks/original_hopping_transfer/PROPOSAL.md) and its [check](../outputs/bandcenter_converter_2026_10_17/source_checks/original_hopping_transfer_check/REVIEW.md) reduce its displayed sufficient output count by 250 while retaining its onset and error; its supplied fixed-spectrum family also retains finite .001347. That family is not transferred to the converted device.

The converted row has a three-times earlier sufficient onset and forty-times fewer output sites than the checked shorter original choice, but larger errors, different coefficients and a different packet. This is not an equal-tolerance comparison, an optimum or evidence that the original architecture cannot reach the new horizon/size at the same error. No general architecture superiority or impossibility follows. Weighted propagation methods themselves are not claimed novel.

## 6. Premises, source preservation and limits

The exact correlations j=J(1-C0), tau²=jJS0 and the equal-diagonal emitter/lead relation are supplied Hamiltonian data, not derived fabrication tolerances. The original calibrated source, signs, selectively absent interactions, pure product preparation, unitary Hamiltonian dynamics, literal W and output identification remain named mathematical/physical premises. The native supplier and physical energy/time/Record identification gaps remain. No common-j drift, independent coefficient-error family, original fixed-spectrum robustness, new precision contract, capture, reset, reuse or all-future finite halt is established.

The companion [SOURCES.json](../outputs/bandcenter_converter_2026_10_17/SOURCES.json) inventories byte-exact existing source/check files and their dependency roles for the portable packet at `outputs/bandcenter_converter_2026_10_17/source_checks/`. The canonical original note stays a repository dependency and is not copied. Failed contact/search and Herglotz/Poisson routes are not used. The generic hopping lemma is not imported separately: the cited output-only proof contains its weighted-generator and single-cut argument in full. Original shorter-output files support comparison status only.

Review exposure is explicit. This note's author previously checked the physical resources and broader hopping argument and authored the output-only specialization; its separate checker authored the broader method. The original source, static, temporal and composition checks share ancestry and some reviewers. They are selective source-exposed analytical checks, not multiple blind recertifications. Root supplied the accepted component identities and requested this assembly. The present task read the complete finite composition/check, wide temporal argument/check, final wider-band argument/check, corrected narrow temporal argument/check, weighted-profile argument/check and reference-measure derivation, and reused the previously read resource/output proofs and construction passages. It is synthesis, not another independent audit of those proofs. A truncated combined source read was not treated as complete coverage; affected needed material was reread separately.

One preserved ancestor display requires the explicit [endpoint strictness erratum](../outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_weighted_profile/ENDPOINT_ERRATUM_REVIEW.md), SHA256 f307230fd3609e89e761d8dd6d240c55be870490e3d77cfcd6e02713389b36f1. Weighted-profile equation (4)'s displayed scalar comparison to 9x+delta_c is false as a strict inequality at x=0. Its earlier review did not flag this remaining source-text defect; the erratum records that omission rather than retroactively crediting the review. Write epsilon_closed(q)<Delta_c=10^-86 for actual closed feedback versus its fixed ceiling. The corrected chain is

    ||S_new+Z S_old||
      <=rho+rho/(1-rho)+6x+epsilon_closed(q)
      <rho+rho/(1-rho)+6x+Delta_c
      <=9x+Delta_c,  Z=exp(2iF k).

The last scalar comparison permits equality at x=0, while the preceding feedback comparison remains strict. The subsequent reflection/transmission floors and slopes retain positive rounding slack, so all downstream constants are unchanged. The final wider-band proof already states this distinction correctly. The historical source bytes remain unaltered; this note imports the corrected chain with the preserved erratum, and the separate publication review must assess its implications. The temporal packet correction likewise comes from the final corrected proof, not an earlier packet-switch assertion.

No new runner, numerical experiment, solver or parameter sweep was performed for this assembly. Hashing and source inventory are bookkeeping, not scientific verification. No W, Git, model, prompt or checkpoint was changed. The portable links specify the intended integration destination; copying, full integration review and publication remain separate root-owned steps.
