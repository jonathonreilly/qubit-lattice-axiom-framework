# Complete output with a wider relative slow-receiver band

**Type:** bounded_theorem
**Status:** conditional mathematical support; unaudited.

Runner: [control_output_family_2026_10_17.py](../scripts/control_output_family_2026_10_17.py).

Publication evidence boundary: the analytical argument and its named supporting proofs remain controlling. The shared runner supplies finite algebra, matrix, flux and budget corroborations only; it does not prove the continuum/contour estimates, certify all parameter families, or establish physical realization. Statements below about no new computation describe the original authoring stage; its exact source is preserved in `outputs/control_family_landing_2026_10_17/originals/WIDE_SLOW_OUTPUT_COMPLETE_STATE_BOUNDED_THEOREM_NOTE_2026-10-17.md`. Historical author reviews are provenance, not independent landing authority.

Claim type: bounded_theorem. Actual current-surface status: conditional-support. The changed-domain components, their complete temporal composition and the final sharpened synthesis have distinct selective checks. This publication note is new authoring and still requires its own integration review; it grants no retained audit status. Exact source/calibration, coefficient correlations, seed and physical-identification premises remain conditional.

For the single supplied device with kappa=10^-8, h=4×10^-6, slow hopping g=5×10^-8 and M=250,000,000 new receiver sites, the complete unconditioned vector map has error **<.00191 at every chosen read time t∈[10^15,2×10^15]** against its specified normalized output target. The comparison retains the head, shared source, record and any passive reference. The target is normalized on a common infinite comparison space and the finite actual state is embedded there; its tail is not silently truncated.

| Certificate | Slow hopping g | New receiver sites | Single-read interval | Complete normalized-target error |
|---|---:|---:|---|---:|
| Prior PR9678 primary point | 10^-6 | 5,000,000,000 | [10^15,2×10^15] | <.00191 |
| Present wider-band point | 5×10^-8 | 250,000,000 | [10^15,2×10^15] | <.00191 |

The new-site ratio is exactly 20. The receiver hopping, connector and compensation occupations change, so these are different supplied Hamiltonians. Each target uses its own transmitted spatial waveform. The common comparison is the complete normalized-target metric, certified ceiling and read window. No measured-error ordering, optimality or practical speed is established. The original source and contact loads do not all shrink with g. Times use the supplied Hamiltonian convention; no independent physical-seconds identification is made.

The [complete-onset parent](SLOW_OUTPUT_COMPLETE_STATE_ONSET_BOUNDED_THEOREM_NOTE_2026-10-17.md), SHA256 `49f53a9ab571c7784158d64a4b206e43e570b6c4252f294ec854015d99ba7027`, is recorded as regular PR9678 at head `39af77cb9563f678d9f7ce93494c39f544968d75`. Its [uniform-family ancestor](UNIFORM_SLOW_OUTPUT_RESOURCE_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md) and [original exact-source note](REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md) retain the named mathematical and supplied-device premises. Their earlier numerical performance does not automatically extend to the enlarged relative receiver band. The `outputs/slow_wide_2026_10_17/SOURCES.json` maps every changed source/check and the two preserved historical revisions, then resolves the unchanged ancestry through existing packets without recopying it. Mathematical imports follow actual interfaces, not Git ancestry.

## Fixed device and complete comparator

Keep the original supplied j with .0027<j<.003, original hopping J, exact correlated old/source calibration, two converters, capped input, emitter, eighteen-edge cable and 24-head record gate. The shared old/source internal system is counted once. The selective installed-pair contract remains: incidental geometric neighbors are not silently added as interactions.

The retained old gate port is o=(100,2,2); the distinct first slow site is r_0=(100,3,2), with r_m=(100,3+m,2). Write n=(I-Z)/2 and use the positive exchange block

    Q(-b)=b(n_x+n_y-a_x* a_y-a_y* a_x), b>=0.

The connector is Q(-sqrt(jg)), internal slow bonds are Q(-g), and the occupations are

    (j-sqrt(jg))n_o,
    (2j-sqrt(jg)-g)n_r0,
    2(j-g)n_rm, m>=1.

They remain positive and preserve diagonal 2j in the one-head sector. Keep r_0,...,r_(M-1) and the cap g n_r(M-1) in the finite apparatus. With every original coefficient retained, this is the exact compression H_M=P H_infinity P in that seeded sector. It introduces no absorbing endpoint. The occupations add no vacancy scalar; retain

    c_att=c_total+4(sqrt(2)-1)j,
    K=2I+Z1Z2,
    W=[(9+12i)I+(-16+12i)X1X2]/25.

Here c_total is the unchanged original source/filter/converter vacancy sum. No scalar is removed or fitted to an input. K remains inside the actual interacting source and is not assumed to commute with its contacts.

Let V prepare an occupied emitter, blank other heads, source vacuum and computational record 0 from arbitrary four-dimensional old input. Tensor this preparation with the identity on any passive reference. Define U(t)=exp(-itH_infinity)V. At the fixed point put

    gamma=kappa²/j, d=2j sin h, H=d/gamma, L=g/gamma.

H in these scalar formulas is a dimensionless ratio. The enclosures are d/g<.48<.5, 580000<H<720000, L>1350000 and gamma T>100/3 for T=10^15. The old q band stays q∈pi/2+[-h,h]; its width has not increased. The relative slow band is wider because delta=-2j cos q=-2g cos k and g has decreased.

With k_old(q)=2asin(sqrt(j/J)sin(q/2)), E'_q=2j sin q and the one fixed supplied phase zeta, retain exactly

    Dref(q)=-2j cos q+gamma exp(iq),
    Fref(q)=kappa E'_q zeta exp[i61q+i172k_old(q)]
                                      /[sqrt(2pi)jDref(q)],
    tf(q)=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    Fs(k)=tf(q)sqrt(dq/dk)Fref(q),
    dq/dk=g sin k/(j sin q),  E_s(k)=2j-2g cos k.

The phase is 61.5q+.5k+172k_old(q), with m=0 at the first slow site. It is not a translation by 61 slow sites. The physical connector transmission and the flux-normalized tf are distinguished by this actual Jacobian.

Let beta_t(m), m>=0, be the Fourier integral of Fs(k)exp[ikm-itE_s(k)]/sqrt(2pi) over the original centered hard slow band. Define ps=∫|Fs|²=p0-R_ref, including reflected mass R_ref, and r(t)=||beta_t||. The complete target is

    Traw(t)=exp(-it c_att)Jout[beta_t tensor exp(-itK)W],
    Tnorm(t)=Traw(t)/r(t), when r(t)>0.               (1)

Jout includes source vacuum, record 1 and blank other head sites. Tnorm is an ideal isometry on every old/reference input. The actual state is neither normalized nor postselected in the complete comparison.

## The changed-domain interfaces

The new local and spectral proofs cover 0<kappa<=10^-8, 0<g<=10^-6, 0<h<=4×10^-6, d/g<=.5 and, where required for the sharper emitter/reference estimates, H>=100. These imply L>=2H>=200. They are not extensions of narrow numerical constants by assertion. Both record-X sectors and every prepared input use the same physical union

    I=I_1 union I_3,
    I_b=c_att+b+2j+[-d,d], b=1,3.                   (2)

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band/PROPOSAL.md` controls the physical interface reflection by |r_L|<.128 and |r_L|<=.261|delta|/g. The naive whole-inverse Neumann test can fail on this interval. The exact rank-one update instead uses the small actual output diagonal of the old gate inverse: its denominator exceeds .999923. It gives gate inverse <33/j, full forced gate/closed-tail recovery <6.28 and selected source-facing reflection <.129. Closed reflection is bounded only after its necessary root powers are paid.

The source feedback margin is newly bounded by .8709. Recomputing every recovery range yields absolute recovery L0=4×10^5 for all 235 nonemitter finite heads and every complete closed slow tail. The stationary propagating ray is excluded from this square-summable recovery map and is treated separately. The earlier finer attachment and gate constants do not transfer.

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint/PROPOSAL.md` preserves ordered full-input source feedback and derives

    ||G-Gref||<a+b(g)|delta|,
    a=8×10^-18, b(g)=46000/.0053+290/g,
    Gref=-Q/j, ||G||<550.

Here Q is the diagonal old-root matrix in the fixed B basis; P selects the open channel on the given window and C its seven-coordinate complement. The nonzero a floor comes from the original supplied calibration. It is not removed by a phase convention. All complementary blocks remain: ||G_PC||,||G_CP||<10^-23 and the complementary emitter inverse is <6. The selected Schur denominator has positive imaginary part >189kappa²; under H>=100 its modulus is >.9955sqrt(delta²+gamma²). The full eight-coordinate inverse is <1.01/sqrt(delta²+gamma²). Wrong-window prepared inputs retain their real complementary response.

The complete finite matching inverses and local root branches supply seed absolute continuity on both closed windows, including their endpoints. No absence of outside atoms or singular spectrum is asserted. The genuine comparison uses a j chain for every B eigenvalue. Before prepared compression, the full8 difference obeys

    ||Tactual-Tref||
      <1.021kappa²(a+b(g)|delta|)/(delta²+gamma²).

Its integrated per-window allowance is

    eta=(1.021kappa²/pi)
         [2a atan(H)/gamma+b(g)log(1+H²)]<5.3×10^-6 (3)

at the fixed point. This full resolvent allowance remains necessary below even after the prepared-mass improvement.

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_outgoing/PROPOSAL.md` compares the complete endpoint-forcing row with the literal reference, paying the changed gate and source denominators. The physical conversion is E'_k t_L=E'_q tf sqrt(dq/dk), with no lost sqrt(j/g) factor. It preserves wrong-window prepared columns and their actual output-window phases before factorizing the ideal old aging. A convenient moment relaxation is

    A=2j-gamma,
    Q2=4kappa²h/(pi A²)*(h/sin h)²,
    E2=16kappa²j²h/(pi A²),
    theta=j a+kappa²b(g),
    Esel=[(2.1×10^-13+10^-60+theta)sqrt(ps)
                      +304sqrt(Q2)+(.302/g)sqrt(E2)]/.9955,
    Eout=sqrt(2)Esel+1.7×10^-24 kappa sqrt(2h).

At this point Eout<.000197. The moments are unnormalized; no division by sqrt(ps) occurs here. The sqrt(2) safely combines selected input columns within a parity; orthogonal parity and record sectors add no further multiplicity. Real-band conjugation, Fourier isometry and halfline restriction give this same allowance for actual incoming. Outgoing and incoming share the physical ray, so their two errors must both be charged.

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_derivative/PROPOSAL.md` redoes the finite gate load and direct inverse action on the actual recovered forcing. With R=M(E)^-1 and F=R V_endpoint, it proves ||R||<1.17×10^13, ||R V_o||<6.5×10^6 and ||RF||<6.47×10^17. Differentiating the assembled equation

    M(E)=E I-H_finite+j V_o Q_slow(E)V_o^T,
    F'=-RF-j R V_o Q_slow' V_o^T F

includes all propagation and feedback derivatives. The wider root derivative is <1/(1.93g), not the narrow 1/(1.99g). Including every closed-tail lift and its derivative gives

    D1(g)=1.00068(6.47×10^17+3.31×10^7/g)+3600,
    sup ||L'(E)||<D1(g)<6.49×10^17                  (4)

at g=5×10^-8. The last evaluation is for this fixed point. These are ordinary real-window derivatives at positive g; no uniform actual-source complex strip or g=0 limit is inferred.

## Sharper prepared mass, with its restricted use

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_seed_mass/PROPOSAL.md` improves only the one global omitted-state allowance. It retains the exact source phase instead of integrating the dominant slow reflection solely by its pointwise norm.

On a selected channel the exact leading return at the source plane is -w^80 r_L, w=exp(iq). Ordered source feedback and the complex transpose identity produce

    g_eff(delta)+w/j=C0 r_L(delta)+E(delta),
    |C0|=2/j,
    |E(delta)|<=a_E+b_E|delta|+76delta²/g²,
    a_E=4×10^-11, b_E=120000/.0053.                 (5)

C0 can have any fixed complex phase. The product uses the square of the complex selected row, not its absolute square. The larger a_E allowance pays the structured source comparison; it does not change the underlying calibration. The original tighter a+b(g)|delta| envelope is retained for the quadratic resolvent remainder.

For Delta_g=g_eff+w/j, T0=1/Dref and Tx=1/(delta-kappa²g_eff), exact scalar algebra gives

    Tx-T0=kappa² Delta_g T0²+kappa⁴ Delta_g² T0² Tx.

Only the explicit leading C0 r_L term is paired. The identities r_L(-delta)=conjugate(r_L(delta)) and Dref(-delta)=-conjugate(Dref(delta)) make the symmetric integral of T0²r_L real. They do not make the actual selfenergy odd or the C0-weighted integral real. Bounding its imaginary part by |C0|∫|Re(T0²r_L)| pays <.523/L. Every unpaired remainder remains charged.

Writing H=d/gamma, the selected diagonal deficit is bounded by eta_diag=.523/L+eta_E+eta_2, where

    eta_E=(1.0003kappa²/pi)
        [2a_E atan(H)/gamma+b_E log(1+H²)
                          +(152/g²)(d-gamma atan(H))],
    eta_2=(1.006kappa⁴/pi)
        [2a²/gamma²+4a b(g)/gamma+2b(g)² asinh(H)].

The genuine reference mass is p0; its exact expression uses A=2j-gamma, alpha=gamma/A and y=tan h:

    p0=4kappa²/[pi A²(1-alpha²)]
                         [atan(y/alpha)/alpha-h].

On each window the prepared density is positive. Its wrong-window diagonal can be discarded for a lower bound, but its off-diagonal cannot. Both full Schur cross entries give the additional two-window allowance

    eta_cross=28×10^-23 kappa² asinh(H)/pi.

The two selected deficits multiply orthogonal prepared projections, hence cost eta_diag I rather than 2eta_diag I. This is a Loewner lower bound with the cross matrix paid explicitly, not an assertion that actual error ranges are orthogonal. It yields the full four-input statement

    M_seed(I)>=(p0-eta_diag-eta_cross)I,
    0<=M_seed(R outside I)
          <=min{1,1-p0+eta_diag+eta_cross}I.         (6)

At the fixed point, 1-p0<1.1×10^-6 and eta_diag+eta_cross<4.58×10^-7. Thus outside prepared mass is <1.558×10^-6 I and the omitted seed embedding has norm <.00125, since .00125²=1.5625×10^-6. Exact total seed normalization charges every outside spectral type. Parity and record-X aggregation preserve this operator bound, including passive references and all later output coordinates.

Equation (6) replaces only the coarse .00344 omitted-state amplitude. It does not replace eta in (3), the represented full8 emitter comparison, the outgoing coefficient or the background's full resolvent substitution.

## Centered recovery for the represented background

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_centered_background/PROPOSAL.md` reduces the represented finite/closed contribution while keeping the same actual recovery L and derivative D1. First replace Tactual by the complete Tref in -kappa L Tactual Vseed. Across both windows and lips, this still costs 2kappa L0 eta. The new density-only result cannot pay this full resolvent error.

Only after that replacement does the diagonal reference reduce the prepared input to one selected channel and one complementary vacuum channel on each window. For the selected scalar, compare Tref to Tlor_±=1/(delta±i gamma) on the real band. This costs

    Bscalar=(2kappa L0/pi)(gamma/j)log(1+H²).

Separately on each lip and window subtract its own center: L(delta)=L(0)+DeltaL(delta), with ||DeltaL||<=D1|delta|. With r_delta=sqrt(delta²+gamma²), the derivative of DeltaL Tlor is bounded by D1/r_delta+D1|delta|/r_delta². Real-energy integration by parts pays both endpoints and gives

    Bvary(t)=(2kappa D1/(pi t))
        [2d/sqrt(d²+gamma²)+2asinh(H)+log(1+H²)].    (7)

No equality of centers across lips, windows or record sectors is assumed. The resonant denominator derivative now multiplies a function vanishing at delta=0, removing the former L0/gamma cost while retaining the independently proved D1 obligation.

For the constant part, the full-line rational Fourier integrals at t>0 are -2pi i exp(-gamma t) on the upper lip and zero on the lower. Each lip's removed pair of oscillatory tails costs <=4/(dt), including its endpoints. This extends only an explicit rational comparator, not actual L or the physical energy band. Together,

    Bcenter(t)=2kappa L0 exp(-gamma t)+8kappa L0/(pi d t).

The other prepared reference channel has norm <=6 and derivative <=37, so keeping its real resolvent and both endpoints costs

    Bwrong(t)=(2kappa/(pi t))[12L0+12dD1+74dL0].

All finite nonemitter coordinates, complete closed tails, physical window phases and arbitrary prepared superpositions are retained. The full bound is

    B_I(t)<=2kappa L0 eta+Bscalar+Bvary(t)
                                  +Bcenter(t)+Bwrong(t). (8)

At t>=T=10^15 the five respective allowances are <4.24×10^-8, <1.1×10^-12, <.000249, <4.9×10^-10 and <1.3×10^-12. Thus B_I(t)<.000250. This replaces the coarse .000607 background allowance and consumes no omitted-state budget.

## Complete finite certificate

The unchanged-in-scope but newly evaluated wide `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_complete/PROPOSAL.md` retains the full represented emitter estimate

    E_I(t)<=exp(-gamma t)+2gamma/j+(1-p0)+2eta
           <.000011781, t>=T.                      (9)

It compares the full8 emitter inverse before prepared restriction and charges both windows. The one global omitted state covers its unrepresented part. The paired-mass bound is not substituted into (9).

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_reference/PROPOSAL.md` recomputes the exact transmitted mass and contours on d/g<=.5. It gives R_ref<.047H/L² and ps>1-.68/H-.047H/L²>.993. For sigma=gamma t and gt>=1,

    Jref(t)=min{sqrt(ps),1.7sqrt(ps)exp(-1.93gt)
                                      +.72/(H sqrt(sigma))},
    Cout(sigma)=min{1,2.1exp(-.4825sigma)
                                      +.8/(H sqrt(ps sigma))},
    r(t)>=sqrt(ps)*sqrt(1-Cout(sigma)²).

The conjugate incoming contour pays m=0 and both hard-cutoff sides. The outgoing contour is shallower; neither continues actual source coefficients. At the fixed point these give Jref<2.2×10^-7 and 1-r(t)<6.2×10^-7 for all t>=T. The latter includes reflected loss, not just negative-site concentration. Actual incoming additionally costs Eout and outgoing separately costs Eout.

With epsilon_sp<.00125 from (6), the complete raw comparison is therefore

    ||U(t)-Traw(t)||
       <=epsilon_sp+E_I(t)+B_I(t)+2Eout+Jref(t).     (10)

It follows from the physical rectangular-column Stone jump, retaining both lips, both physical windows, wrong-window phases and orthogonal record-X sectors. It charges the omitted state once. Normalizing the ideal comparator costs 1-r(t), with no conditioning of the actual state.

The unchanged general-g compression theorem applies with the actual new connector, occupations and finite cap. Weight zero on every upstream site and first slow site, then f(r_m)=m. Only internal g edges contribute; the connector has zero weight increment. Writing U_M(t)=exp(-itH_M)V, single-cut Duhamel yields

    ||embed U_M(t)-U(t)||
      <=min{2,1.2exp[-M+4gT sinh1]}, 0<=t<=2T.      (11)

With M=250,000,000, T=10^15 and sinh1<1.2, the exponent is <-10,000,000, hence transfer is <10^-6. Returns, all internal directions and both record sectors remain covered through the absolute horizon 2T. The cap is not absorbing; the infinite normalized target remains unchanged.

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_sharp/PROPOSAL.md` and its `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_sharp_check/REVIEW.md` establish the compatible sum:

| Complete-error contribution | Uniform ceiling on [T,2T] |
|---|---:|
| One global omitted state | .00125 |
| Represented full8 emitter | .000011781 |
| Represented finite/closed background | .000250 |
| Two actual coefficient comparisons | .000394 |
| Scalar incoming reference | .00000022 |
| Ideal transmitted-reference normalization | .00000062 |
| Exact full-state finite transfer | .000001 |
| Sum | .001907621 |

Thus

    ||embed exp(-itH_M)V-Tnorm(t)||<.00191
                         for every t∈[10^15,2×10^15]. (12)

The displayed sum has slack .000002379 below .00191. These are analytical sufficient ceilings, not observed propagation errors. The sharper synthesis changes exactly the omitted-state and represented-background allowances of the earlier .00446 certificate for this same wide device. The earlier certificate remains valid history; no parameter changed between those two certificates.

## Resources, single-read consequences and limits

The exact inventory is M+236 heads, M+241 total physical qubits, M+237 head edges and 2M+277 unmerged positive local blocks:

| Quantity | Present finite device |
|---|---:|
| Head qubits | 250,000,236 |
| Total physical qubits | 250,000,241 |
| Head edges | 250,000,237 |
| Unmerged positive blocks | 500,000,277 |

The four original old/source qubits and one record are counted once; passive references are excluded. Against PR9678's primary point, new sites decrease exactly 20-fold, while the total-qubit ratio (5,000,000,000+241)/(250,000,000+241) is slightly less than 20. Its separately earlier point at T=3×10^14 with 1.5×10^9 new sites and ceiling .00331 has a different interval; the present theorem does not dominate that time/resource tradeoff.

Let P0 and P1 be computational record projections. Since the normalized ideal target has record 1, (12) gives failure effect <(.00191)²I=3.6481×10^-6 I, hence single-read success >.9999963519 for every old/reference input. Projection gives an actual successful contraction within epsilon=.00191 of the ideal isometry. Its norm is at least sqrt(1-epsilon²), so normalizing its successful vector costs at most

    epsilon+1-sqrt(1-epsilon²)<.001912.

The complete-channel and successful subnormalized-CP-map diamond errors are <2epsilon=.00382, also after discarding apparatus. This includes the old/reference channel compared with the literal exp(-itK)W operation. A normalized conditioned channel is generally nonlinear; no diamond estimate for that normalization is asserted. The common scalar remains in vector comparisons and cancels only at channel level.

The theorem covers one chosen read in the finite window. It supplies no intervening-measurement or first-success rule, permanent storage, irreversible capture, autonomous reset/reuse or practical speed. No source/contact norm load, outside spectrum, physical scalar, passive reference or output subsystem has been removed to obtain the bound. No new coefficient-tolerance or optimal-resource theorem is claimed.

Exact correlated coefficient/calibration supply, original source/filter/converter inverse premises, initial seed preparation, selective installed pairs and native Hamiltonian/time/energy/Record-readout identification remain named conditions. Registered framework primitives are not classified as missing imports; they do not themselves provide these additional device-specific dynamics, preparation or readout identifications.

## Source history and review coverage

The proposed packet maps nine complete argument/check pairs for byte-preserving installation:

| Argument | Distinct selective check | Scope |
|---|---|---|
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band_check/REVIEW.md` | Local scattering, actual feedback and complete recovery |
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint_check/REVIEW.md` | Full resolvent, complements, local regularity and coarse matrix mass |
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_reference/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_reference_check/REVIEW.md` | Exact transmitted mass and paid hard-band contours |
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_outgoing/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_outgoing_check/REVIEW.md` | Complete prepared input, flux/Jacobian and wrong-window outputs |
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_derivative/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_derivative_check/REVIEW.md` | Full finite inverse, direct forcing and all closed-tail derivatives |
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_complete/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_complete_check/REVIEW.md` | Full temporal/finite interface and valid .00446 history |
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_seed_mass/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_seed_mass_check/REVIEW.md` | Scoped omitted-state improvement |
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_centered_background/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_centered_background_check/REVIEW.md` | Scoped represented finite/closed improvement |
| `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_sharp/PROPOSAL.md` | `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_sharp_check/REVIEW.md` | Compatible substitutions, complete bound and same-quality comparison |

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band/PROPOSAL_v1.md` is preserved. Its checker found that the displayed strict <38u comparison fails at the included center u=0; final <=38u repairs that statement without changing downstream constants. The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint/PROPOSAL_v1.md` is also preserved; its changes only record completion of the gate check. Historical pending-review wording remains unchanged in original source bodies and is qualified by the actual final paired reviews.

The publication drafter read all nine current arguments and checks completely and inspected both complete revision diffs. The necessary prior complete-onset, uniform-recovery and general-g compression/resource arguments were read in the preceding coherent task and reused at verified unchanged identities. The manuscript adds no self-issued independent approval. Component authors/checkers share the selected model, ancestors and exposure to routes/constants, with roles disclosed in their reports; the checks are neither blind nor model-diverse original recalibrations.

Only this research-directory NOTE.md and SOURCES.json are delivered. Hashes, exact mappings and virtual note-link checks establish identity and proposed layout, not physics. No scientific runner, inverse experiment, quadrature, simulation, sweep, additional candidate, Git/W/PR/checkpoint action, editable prompt or axiom change was performed. Actual copying, canonical link/graph validation, distinct publication integration review and publication remain root-owned later actions. No unrelated fermion or other concurrent lane is incorporated.
