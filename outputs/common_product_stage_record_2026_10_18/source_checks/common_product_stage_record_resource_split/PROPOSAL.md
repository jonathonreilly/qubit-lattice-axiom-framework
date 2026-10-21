# Separate time budgets for the finite-output and flag-branch families

New bounded author refinement requiring a distinct check. ROOT proposed separating the inverse-time allowances from the inverse-square-root-time allowances instead of squaring their common maximum. The reconstruction below supports that prescription for both the finite-output source7286105f and the absolute flag-branch sourcee7b53eed. It retains every allocation, phase, finite cut and normalization condition. Neither frozen source is edited; their larger sufficient prescriptions remain valid historical results at their own check status.

The two refined prescriptions certify different contracts: the finite-output family has a complete normalized output guarantee on a final window; the flag family additionally has an absolute unnormalized record1-branch guarantee on[0,t_plus]. No normalized rare-success, permanent storage, native Record or practical-performance claim is added.

## 1. Fixed architecture and common definitions

Retain the actual finite positive staged network from7286105f: the four-cell core, two34-edge cables, two24-head writers sharing one R, two I emitters M=ell+1, and F output rays n=0,...,ell with positive terminal compensation j n_ell. Final target support is1<=n<=ell on the two F rays, excluding both physical writer origins. All other heads are vacant in the comparator. Programs are the supplied legal twelve-bit encoding, record input is|0>, and arbitrary encoded path/program/passive-reference input is preserved with ideal path action C_p and record output|1>.

The common physical scalar remains c_total=8b+2c_R, and the common outgoing Fourier sequence remains

    B_n(t)=(-i)/sqrt(2pi) integral
                       exp(i[n+ell+57]k-itE(k))g(k)dk.

No phase, graph, local positive block, cutoff shape or normalization convention is changed by splitting the budgets. Only ell and observation times are selected by a smaller sufficient formula.

For0<epsilon<=1, Lambda>0 use

    h=epsilon/10^5, eta^2=zeta=epsilon/10^5,
    D1=Lambda/2, D0=zeta D1, b=eta D0, j=b^2/D0,
    v_min=2j cos h, v_max=2j.

The normalized exact source profile uses the real C2 cutoff with plateau h/2, transition width h/4 and support through3h/4. Its phase-preserving amplitude is F=-i sqrt(2/pi)rho exp(ik)/[(2-rho^2)cot k-i rho^2], and g=chi F/sqrt(p_chi), with the positive actual p_chi=||chi F||_2^2.

For both policies below rho<=epsilon sqrt(h)/1024, so the complete cutoff/source estimates remain

    P<=3rho^2/h, p_chi>1/2, G0<=1,
    G1<=g1=80/rho, G2<=g2=1200/(h rho^3),
    B_minus<=bminus=82/rho.                    (1)

These include the changing cutoff costs. They are not fixed-wide-band constants.

## 2. Two source policies and valid local inverse constants

Policy F (finite output only): take exactly rho=epsilon sqrt(h)/1024 as in7286105f. One may keep its original B=10^31 writer inverse ceiling and all corresponding packet formulas. This is the default policy F comparison below. A separately valid fixed B=10 can also be substituted with every packet constant recomputed; no exponent below depends on choosing between these two fixed valid constants.

Policy A (absolute flagged branch): use the checked local B=10, with the conservative packet-formula constants a0=20, a1=w1=800, w2=56000, exactly as selected in e7b53eed. Compute q1,q2,T0,T1 from packet347719's core, feedback, external derivative and internal-map formulas at the actual h,eta,zeta BEFORE choosing rho. Then set

    rho=min{epsilon sqrt(h)/1024,
                   [epsilon/(4096(1+T0))]^2}.   (2)

No old values computed with B=10^31 are reused in this policy. The core c1,c2,m0,m1, feedback f1,f2,k0,k1,k2, connecting-map derivatives, s1,s2,q1,q2 and all endpoint/mediator/writer/cable sums must be evaluated with the stated chosen local constants, as explicitly prescribed in e7b53eed. T0 is an internal-map norm ceiling and has no dependence on rho or ell. Hence(2) is not circular.

For either policy, denote the resulting packet norm/first derivative ceilings for the strict internal map by T0,T1. The already derived source and product rules give the explicit sufficient coefficients

    H1bar=g1+q1,
    H2bar=g2+2q1 g1+q2,
    J0bar=T0, J1bar=T0 g1+T1,
    A_i=g2+(12j/v_min)g1+(4j/v_min+48j^2/v_min^2),
    A_o=H2bar+21H1bar+154.                      (3)

The complete scattering ceiling remains deltaS<epsilon/512 for both policies. Shrinking rho changes the source, not the stationary core/writer scattering matrix. Policy A also preserves the exact normalized-source estimate

    G0<=16sqrt(rho)<=epsilon/[256(1+T0)].        (4)

This uses the proved integrated resonance bound from e7b53eed, including p_chi>=1/2 and h>=rho^2/(2-rho^2). Both conditions still follow from the first term of the minimum in(2).

## 3. The split prescription

Define TWO positive coefficient maxima

    L=max{1,bminus,g1+1,H1bar+1,g1+7},
    Q=max{1,eta^-1,rho^-2,J1bar+J0bar,A_i+A_o}.

The symbol Q here is a scalar budget, not a positive hopping block or a scattering matrix. Select

    u0=10^12 max{1,(L/epsilon)^2,Q/epsilon},
    ell=ceil(100u0), M=ell+1,
    t0_time=u0/j,
    t_minus=3ell/(4j), t_plus=7ell/(8j).          (5)

All quantities on the right are explicit functions of epsilon,Lambda and the fixed valid local inverse choice, with no dependence on u0 or ell. The decisive inequalities are

    L/sqrt(u0)<=epsilon/10^6,
    Q/u0<=epsilon/10^12,
    sqrt(ell)>=10sqrt(u0), ell>=100u0.           (6)

Unlike the previous common-maximum square, this does not force the coefficient A_i+A_o, which enters as1/u0, to be paid through1/sqrt(u0). The old choice was sufficient; it was not a necessary lower bound.

Since u0>=10^12, every old strict geometric requirement remains true: early gaps are at least ell/2, t0_time v_min>2, t_plus v_max<2ell-2, and both late gaps t_minus v_min-ell and t_minus v_min-ell-57 exceed ell/4. The outgoing far-cut gap is at least ell/4. The relative window width is unchanged at1/6; t0_time<t_minus. No Hamiltonian switch occurs.

## 4. Every finite-output allocation with the changed denominator

The physical/reference comparison, exact packet and fixed-diagonal finite perturbation are unchanged in form. The reference contains the actual entire internal/F submatrix in its unoccupied head sector, including the shared record contacts. Only the two I contact origins differ from their standalone launcher continuations. Their full actual/reference difference has norm<=2j+sqrt(2)b, and the actual unitary retains its full norm. Thus the source's contact Taylor estimate, starting at degree M, still gives

    E_early<=(2+sqrt(2)/eta)/(5000u0)<=Q/u0.

The first inequality uses the same factorial estimate M>=100u0; the second uses Q>=1,eta^-1. It does not invoke a4j norm bound for the actual microscopic/writer Hamiltonian.

The complete twelve allowances now obey:

| Allowance | Split ceiling | Explicit accuracy ceiling |
|---|---|---|
| Actual/reference E_early | Q/u0 | epsilon/10^12 |
| Source residual2R0 | 2Q/u0 | 2epsilon/10^12 |
| Incoming launch2L0 | 2L/sqrt(u0) | 2epsilon/10^6 |
| Spectral tails4sqrt(P) | 4sqrt(3)epsilon/1024 | <epsilon/128 |
| Right early projection2d_right | 8L/sqrt(u0) | 8epsilon/10^6 |
| Early lead matching | 4L/sqrt(ell) | 4epsilon/10^7 |
| Early internal matching | 3Q/ell | 3epsilon/10^14 |
| Integrated finite boundary | 2Q/u0 | 2epsilon/10^12 |
| Late incoming2d_L | 6L/sqrt(ell) | 6epsilon/10^7 |
| Scattering2deltaS | epsilon/256 | epsilon/256 |
| Late internal2m_L | 56Q/ell | 56epsilon/10^14 |
| Final truncation4tau_F | 28L/sqrt(ell) | 28epsilon/10^7 |

Here is why every changed grouping is legitimate. The source residual uses rho^-2<=Q; the incoming launch uses bminus<=L; right-tail and early/late lead terms use g1+1,H1bar+1,g1+7<=L. Internal terms use J1bar+J0bar<=Q. The integrated twice-IBP boundary residual is<=2(A_i+A_o)/u0<=2Q/u0. In particular its G2 and Q(k) derivative costs are retained inside A_i+A_o rather than dropped from the maximum. The outgoing target excludes F origins n=0 and indices beyond ell, exactly as in the finite source; the term tau_F<=7(g1+7)/sqrt(ell) is unchanged by this time choice.

Each of these twelve positive ceilings is strictly below epsilon/32. Therefore their sum is below3epsilon/8. The same intermediate ceilings establish delta_launch<1, D_L=d_L+deltaS+m_L<1/2 and2tau_F<1 BEFORE any comparator normalization is used. The common positive normalization of B on1<=n<=ell exists throughout[t_minus,t_plus]. Consequently both policies obey

    sup_(t_minus<=t<=t_plus)
    ||exp(-itH_phys)E_seed
      -exp(-ic_total t)J_F(beta_F(t) tensor C_p tensor|1>_R)||
       <3epsilon/8.                            (7)

All actual outputs, coherent programs and arbitrary passive references are retained. No source/writer bound-state overlap is assumed zero: it remains paid by the complete initial vector match and unitary propagation. Actual finite F caps retain diagonal2j, so the hopping-only boundary identity is unchanged.

## 5. Policy A: entire finite-horizon flag branch survives the split

Use ONE target at all times, exactly as in e7b53eed:

    V_tar(t)xi=exp(-ic_total t)
        J_F[P_(1<=n<=ell)B(t) tensor C_p xi tensor|1>_R].

Its radial vector is unnormalized, ||V_tar(t)||<=1, and it is not redefined at t0_time. Let P1=|1><1|_R on the complete output space. For the exact infinite packet with I incidence and blank record, P1 annihilates its incoming component. The outgoing error is<=deltaS by full-integer Parseval, and its strict internal flagged vector is<=T0 G0/sqrt(2pi). This is the same full-fiber inequality, independent of time selection.

For t0_time<=t<=t_plus, the first eight finite allowances above sum to E_match<epsilon/4. Their full-vector comparison passes through P1 unchanged. At arbitrary transit times the omitted F-origin amplitude is bounded by G0/sqrt(2pi), not by a late phase gap. The far-F cut tail is at most3(g1+7)/sqrt(ell)<=3L/sqrt(ell). Therefore

    ||P1 exp(-itH_phys)E_seed-V_tar(t)||
       <=E_match+deltaS+(T0+1)G0/sqrt(2pi)
                                      +3L/sqrt(ell)
       <epsilon/4+epsilon/512+epsilon/256
                                      +3epsilon/10^7
       <epsilon/2.                            (8)

For0<=t<=t0_time, the reference remains recordblank and the actual contact error is at most Q/u0. The SAME target is an early outgoing tail with norm<=2(g1+1)/sqrt(ell)<=2L/sqrt(ell). Hence

    ||P1 exp(-itH_phys)E_seed-V_tar(t)||
       <=Q/u0+2L/sqrt(ell)<epsilon/32.          (9)

Thus the absolute branch bound<epsilon/2 holds on the entire closed horizon[0,t_plus] under the split prescription. The normalized final comparator(7) implies record1 probability and joint record1/F-support probability greater than1-(3epsilon/8)^2 on the final window. For subnormalized branch channels, the unhalved trace/diamond discrepancy is<epsilon by the same two-contraction estimate. None of these statements divide by a possibly small early success probability; no normalized rare-success guarantee is inferred.

Policy F alone has no asserted all-horizon branch guarantee: its original source ratio need not make(T0+1)G0 small enough. This difference in contracts is retained in the comparisons below.

## 6. Cap, counts and exact asymptotic comparison

Every local block and cap convention is unchanged. The listed incident sums remain below Lambda, including sharedR8j, source-adjacent5j, F-cap3j and core endpoint6b+6j. Qubit and block counts remain137+4ell and168+4ell. Both policies have exactly j=Lambda epsilon^2/(2*10^10), while gamma=rho j. Exact coefficient magnitudes are not fabrication tolerances or supply costs.

To justify asymptotic powers, fix the chosen valid B independently of epsilon, and take epsilon to zero at fixed Lambda. The local writer constants are fixed. The core dimensionless derivatives and mediator ceilings stay bounded; the feedback denominator tends to1 and stays uniformly positive. Every finite algebraic packet coefficient q1,q2,T0,T1 therefore stays bounded and has a finite limit. In fact T0 has a strictly positive finite limiting value: its endpoint-map contribution alone is>=2, and the explicit sums have no vanishing denominators. These assertions follow directly from the rational/square-root formulas in347719 with eta=sqrt(epsilon/10^5), zeta=epsilon/10^5, h=epsilon/10^5. They do not concern actual optimal norms.

Policy F has rho=Theta(epsilon^(3/2)). Thus g1,bminus=Theta(epsilon^(-3/2)), g2=Theta(epsilon^(-11/2)). It follows from their explicit maximum definitions that

    L=Theta(epsilon^(-3/2)), Q=Theta(epsilon^(-11/2)).

The lower bound for Q follows from A_i+A_o>=g2, and the other terms have no larger order. Hence(L/epsilon)^2 has order epsilon^-5, whereas Q/epsilon has order epsilon^(-13/2). The latter dominates asymptotically, giving

    policy F: u0,ell,size,jt_plus=Theta(epsilon^(-13/2)),
              t_plus=Theta(Lambda^-1 epsilon^(-17/2)),
              gamma=Theta(Lambda epsilon^(7/2)). (10)

Policy A uses(2). Since1+T0 tends to a positive finite constant, its second candidate ratio is Theta(epsilon^2), while the first is Theta(epsilon^(3/2)). The second is the minimum for all sufficiently small epsilon. Therefore rho=Theta(epsilon^2), g1,bminus=Theta(epsilon^-2), and g2=Theta(epsilon^-7). This yields

    L=Theta(epsilon^-2), Q=Theta(epsilon^-7),
    (L/epsilon)^2=Theta(epsilon^-6),
    Q/epsilon=Theta(epsilon^-8),
    policy A: u0,ell,size,jt_plus=Theta(epsilon^-8),
              t_plus=Theta(Lambda^-1 epsilon^-10),
              gamma=Theta(Lambda epsilon^4).    (11)

Ceilings in ell do not change any stated order. The crossover at which one maximum term dominates may be extremely small; these asymptotic statements are not evaluated operating points or practical-duration estimates.

For the same respective policy, metric, architecture, cap and relative window, comparison with the preserved common-maximum-square prescriptions is:

| Policy and guaranteed contract | Previous sufficient size/jt | Split size/jt | Previous sufficient physical time | Split physical time |
|---|---|---|---|---|
| F: normalized final-window output | Theta(epsilon^-13) | Theta(epsilon^(-13/2)) | Theta(Lambda^-1 epsilon^-15) | Theta(Lambda^-1 epsilon^(-17/2)) |
| A: absolute horizon branch plus eventual normalized output | Theta(epsilon^-16) | Theta(epsilon^-8) | Theta(Lambda^-1 epsilon^-18) | Theta(Lambda^-1 epsilon^-10) |

The previous policy-A orders are derived HERE from e7b53eed's actual K-square prescription: K=Theta(epsilon^-7), so K^2/epsilon^2=Theta(epsilon^-16). They were not previously claimed as checked numbers by that source. This table compares sufficient analytical families for each stated contract, not actual errors or speed on a fixed device, optimal exponents or lower bounds. Changing the valid fixed B can dramatically change prefactors but does not change these particular asymptotic powers. An epsilon-dependent B would require a fresh analysis.

## 7. Evidence, exposure and limits

New refinement depends on unchanged source identities:

- finite-output source common_product_stage_record_finite_seed/PROPOSAL.md,7286105ffd9b6b6d0caa97b121c5e79d37dfcf638128d63c6bbc144e9aa2a995;
- absolute-branch source common_product_stage_record_flag_branch/PROPOSAL.md,e7b53eeda3fc7df96986d3b55f68d9e5af4f1b6657ba068b6f33d03e18a37ee0.

Both were authored and fully read in the immediately preceding coherent tasks and their hashes refreshed unchanged here. Their new distinct checks are not presumed completed merely because this refinement was requested. Packet347719/check17029fa, stationaryc913/check61de4ee and writer sharpening22bca/checkd96ed6 retain the exact pins, full reads and scoped supports recorded in those sources. The B=10 substitution is applied only through its valid local inequalities and complete downstream recomputation. It does not change the physical writer or supply a finite theorem by itself.

ROOT suggested the L/Q separation and tentative exponents. This author reconstructed the complete table and both asymptotic maxima after that exposure; this is not an independent check. Required distinct checks are the classification of every term by its denominator, source-policy changes and normalization, all-horizon F-origin truncation, noncircular constants, same-metric comparison and asymptotic maxima. Component support does not independently certify this new family.

All results remain supplied-law statements. Record1 may occur internally during transit, its absolute erroneous amplitude is paid only for policy A, and finite returns after t_plus are uncontrolled. No irreversible latch, indefinite guarantee, permanent halt, native Record/readout/initialization mechanism, old literal processor replacement or coefficient-error tolerance is supplied.

Only common_product_stage_record_resource_split/PROPOSAL.md was created. No scientific executable, numerical solver/simulation, sweep, source/W/Git/publication/checkpoint/axiom/editable-prompt/model change or delegation occurred. No retained status or independent acceptance is assigned.
