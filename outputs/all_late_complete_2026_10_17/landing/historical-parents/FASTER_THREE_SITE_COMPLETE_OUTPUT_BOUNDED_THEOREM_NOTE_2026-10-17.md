# Faster nominal three-site source: a complete finite-window output certificate

Claim type: bounded_theorem. Status: conditional publication draft prepared for review. The component derivative and integration-by-parts results have completed distinct checks. The new operating-point composition has completed a distinct source-exposed check; final publication integration remains pending. No retained audit status is conferred.

Under the original supplied physical/calibration, matching and preparation premises, the proposed certificate is a complete unconditioned output-map error **<.00086 for every chosen read time in [2×10^13,4×10^13]**, using **5,000,243 physical qubits**. It uses the nominal three-site product source with

    lambda=10^-12, g=5×10^-8, h=4×10^-6,
    T=2×10^13, M=5,000,000,
    a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa²=3jlambda.

The calibrated j is unchanged, with .0027<j<.003. The [scientific parent, published through PR9681](THREE_SITE_PRODUCT_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md), contains a larger-receiver nominal certificate at lambda=10^-13, T=2×10^14, M=50,000,000 and ceiling .0006. Relative to that point, this certificate has a tenfold earlier interval scale and tenfold fewer receiver sites, with a weaker complete-error ceiling. It does not make that comparison to PR9681's separate one-million-site compact receiver. These are sufficient certificates for changed source coefficients and waveforms, not measured error or a lower bound on the old device's operating time.

The technical branch parent is PR9684. Its common-offset and source-tolerance conclusions are not premises of this nominal Delta=0 result. The [spectral parent](CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md) and the PR9681 temporal parent provide the unchanged physical and spectral interfaces.

## Construction and exact target

Retain the original contact/filter source, shared B, converters, capped input, eighteen-edge cable and 24-head record gate. At port p=(40,63,1), put s2=(40,64,1), s1=(40,65,1), s0=(40,66,1), with the single head initially at s0, source vacuum and record0. The six nominal positive blocks are

    j(n_s2+n_p)-kappa exchange_(s2,p),
    Q_a2(s1,s2), Q_a1(s0,s1),
    (j-a2)n_s2, (2j-a1-a2)n_s1, (2j-a1)n_s0,
    Q_a(x,y)=a(n_x+n_y-exchange_xy).

Here kappa<9.487×10^-8<j. All blocks are positive on the full physical qubit space, give source diagonals 2j and add no vacancy scalar. Removing the three source heads leaves j n_p, the exact emitter-free background load. Shared B appears once, and B iota=iota K on the prepared source vacuum. No full [H,K]=0 identity is assumed. This is the compensated six-block nominal family; the later seven-block reexpression is not used.

The slow receiver begins at r_m=(100,3+m,2), m>=0, beyond distinct gate port o=(100,2,2). Its connector is Q_sqrt(jg), internal bonds Q_g, and occupations are (j-sqrt(jg))n_o, (2j-sqrt(jg)-g)n_r0 and 2(j-g)n_rm for m>=1. Keeping M sites and adding g n_r(M-1) is exact seeded-sector principal compression, not an absorber.

Retain literally

    K=2I+Z1Z2,
    W=[(9+12i)I+(-16+12i)X1X2]/25,
    c_att=2nu+2beta+4gamma_J+4gamma_c+4(sqrt(2)-1)j.

On the two physical windows c_att+b+2j+[-d,d], b=1,3, d=2j sin h, use delta=-2j cos q=-2g cos k and k_old(q)=2asin(sqrt(j/J)sin(q/2)), with the original calibrated J. The exact reference coefficient is

    q3(delta)=(delta²-lambda²/3)(delta-kappa²m_j(delta+i0))
                                                -(8lambda²/3)delta,
    F3(q)=kappa a1a2(2j sin q) zeta exp[i61q+i172k_old(q)]
                                            /[sqrt(2pi)j q3(delta)],
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F_s(k)=t_f sqrt(g sin k/(j sin q)) F3(q(k)).

It is zero off the selected hard band. The physical Weyl function m_j, fixed zeta, complex denominator, flux and Jacobian are retained. In particular the phase is 61.5q+.5k+172k_old plus the denominator phase, not a fitted phase. Put

    beta_t(m)=1/sqrt(2pi) int F_s(k)
                         exp[ikm-it(2j-2g cos k)]dk, m>=0,
    r(t)=||beta_t||,
    Tnorm(t)=exp(-it c_att) Jout[(beta_t/r(t)) tensor exp(-itK)W].

Jout supplies record1, source vacuum and the other blank registers. This is one common apparatus vector for all old inputs and arbitrary passive references. The bound below establishes r(t)>0. The finite actual evolution is embedded in the same infinite comparison space; the comparator tail is not silently cut off or renormalized a second time. No actual output is postselected to obtain the complete bound.

## Why the changed source still admits full matching

The exact ordered three-source denominator is

    Q=(D²-a1²)(D-kappa²G)-a2²D, D=E-c_att-2j-B.

The emitter-free background retains ||G-m_j(D)||<a0+b0|delta|, where a0=8×10^-18 and b0=46000/.0053+290/g<5.81×10^9. For s=sqrt(1-3lambda/j), its full-fiber Neumann margin is

    Theta=(j a0+kappa²b0)/s+6kappa²(a0+b0d)<5.24×10^-5,
    c3=(1-Theta)s>.9999475.

Thus ||Q^-1||<=1/[c3(delta²+lambda²)^(3/2)] on both physical lips, with selected and complementary forcing retained in the actual noncommuting order. This uses the three-site inverse; the old one-site emitter's kappa<=10^-8 restriction is not a premise. Root continuation and invertible physical matching supply in-window seed regularity, not merely a small matrix norm. Every outside spectral type is paid separately.

The installed product seed has exact sixth central moment

    mu6=3lambda^6+(8/3)jlambda^5<8.00000001×10^-63.

The second term is the third-hop arrival at the old port. It yields one full-input outside-window allowance sqrt(2mu6)/d³<1.3×10^-8, including passive references and without assuming orthogonal omitted output ranges. This actual omitted state is charged once globally. The separate scalar reference truncation inside the local comparison is not another actual outside vector.

The unchanged local-source interface retains all three source coordinates, both lips and wrong-window inputs. Recalculation gives E_vec<4×10^-9, selected integral D_sel<1.574×10^-5 and complementary D_wrong<1.4×10^-34. At lambda t>=20 the cubic three-coordinate norm is <7.3×10^-7. Including scalar truncation gives represented source amplitude <.0000231. The [distinct point check](../outputs/faster_three_site_2026_10_17/proofs/three_site_faster_nominal_check__REVIEW.md) reconstructs this composition. The [new point proof](../outputs/faster_three_site_2026_10_17/proofs/three_site_faster_nominal__PROPOSAL.md) contains the complete integral formulas and elementary enclosures; no previous point's numerical mass or error is simply inherited.

## Structural derivative improvement for the actual background

The unchanged prepared recovery L contains all remaining finite heads and every closed slow tail, excluding the three source heads and the propagating ray. Its full forcing value bound is L0<14000. Absolute integration alone gives B_absolute<.0016 here and a complete baseline <.00185.

The [prepared inverse derivative](../outputs/faster_three_site_2026_10_17/proofs/three_site_prepared_inverse_derivative__PROPOSAL.md) controls

    D3=a1a2 sup_(window,lip,sector)
                         int ||(Q^-1 V_seed)'|| dE.

It retains full prepared selected and wrong-window columns. Its actual emitter-free derivative comes from the physical finite equations and closed roots, with a sufficient discrepancy derivative Z_g=2×10^8+17000/g. It is not obtained by differentiating a small real-axis value bound. The [distinct derivative check](../outputs/faster_three_site_2026_10_17/proofs/three_site_prepared_inverse_derivative_check__REVIEW.md) fixes this scope.

The [cubic cancellation refinement](../outputs/faster_three_site_2026_10_17/proofs/three_site_cubic_derivative_cancellation__PROPOSAL.md) uses the exact identity

    q0(delta)=(delta+i lambda)^3
           -kappa²(delta²-lambda²/3)[m_j(delta+i0)+i/j].

Differentiating this identity preserves the coherent cubic cancellation and gives |q0'|<3.00002(delta²+lambda²) on the selected band. The physical Weyl correction and its derivative are paid, not replaced by a Markov load. Its [distinct check](../outputs/faster_three_site_2026_10_17/proofs/three_site_cubic_derivative_cancellation_check__REVIEW.md) supports substitution into the ordered Neumann derivative while retaining all complementary terms. At this point the full integrated bound is D3<4.46×10^12.

Use the older checked FULL forcing recovery derivative

    M_g=1.00068(7.29×10^16+3.31×10^7/g)+30<7.37×10^16.

No selected-only direct derivative or newly proposed full L' bound is imported. The [background IBP proof](../outputs/faster_three_site_2026_10_17/proofs/prepared_background_ibp__PROPOSAL.md), with its [distinct check](../outputs/faster_three_site_2026_10_17/proofs/prepared_background_ibp_check__REVIEW.md), integrates the exact column -kappa L a1a2 Q^-1 by parts in the fixed physical output Hilbert space. Each window's fixed closed projector may differ, but the recovered vectors are embedded into the same space before triangle summation. Geometric closed tails and their derivatives are square summable. Both lips, both windows and both hard endpoints give

    B_IBP(t)<=2kappa/(pi|t|) *
      [2c_a lambda²L0/(c3(d²+lambda²)^(3/2))
                                  +2c_a M_g/c3+L0D3],
    c_a=2sqrt(2)/3.

The bracket terms are <2700, <1.392×10^17 and <6.244×10^16. Hence B_IBP(t)<.000610 T/t for t>=T. The complete synthesis may use min(B_absolute,B_IBP). At this point the recovery-derivative term dominates the IBP bracket. This is a better sufficient bound on the same represented background, not a measured amplitude or an all-time finite-storage theorem.

## Traveling wave, physical normalization and complete budget

The inherited actual outgoing row gives raw E_sel<7.61×10^-5, with complementary error <10^-34, and 2E_raw<.000216. The real rectangular Stone identity supplies the incoming coefficient by fixed conjugation, keeping physical exp(-itE); its ideal old multiplier is W*, while outgoing has W. They share a physical halfline, so both raw discrepancies are paid by triangle. Record/parity orthogonality does not produce an extra multiplicity factor.

The checked resonance-weighted scalar time comparison is evaluated with the proof cutoff D=g/4, without changing the hardware or literal F_s. Its phase cost uses the second moment lambda²/3, its numerator/displacement cost uses the fourth moment lambda^4, and its dispersion cost uses a truncated sixth moment. Both hard-cutoff tails and integer-lattice aliases remain. Recomputed through 2T it gives E_w<3.1×10^-6. The exact transmitted scalar mass satisfies 1-p<1.334×10^-10; the stronger outgoing excluded set m<=0 has norm <3.9×10^-6. Thus r(t)>0 and 1-r(t)<10^-10. The incoming raw packet has norm <3.1×10^-6. Only one physical-halfline normalization is charged in the complete comparison.

| Complete contribution | Strict ceiling on [T,2T] |
|---|---:|
| One actual outside-window state | .000000013 |
| All three represented source heads | .0000231 |
| Remaining finite background and closed tails | .000610 |
| Raw outgoing and incoming coefficient errors | .000216 |
| Raw scalar incoming packet | .0000031 |
| Physical target normalization | .0000000001 |
| Finite/infinite evolution comparison | .0000000001 |
| Sum | .0008522132 |
| Stated ceiling | .00086 |

For the cut, put weight zero on every upstream/source/gate site and r0, and weight m on r_m. Only receiver g edges change weight; all shared internal terms and the connector have zero increment. Exact cap compression and one-cut Duhamel give

    finite transfer <1.2 exp[-M+4gT sinh(1)], 0<=t<=2T.

Here 4gT=4,000,000 and sinh(1)<1.176, so the exponent is <-296,000 and transfer <10^-10. This includes returns and all internal channels. The cap is not absorbing and later recurrence is not excluded.

Under these conditional premises, the checked theorem is therefore

    ||J_M exp(-it H_M)V_M-Tnorm(t)||<.00086,
                         every t in [2×10^13,4×10^13].

The operator domain includes arbitrary old/reference input; its range is the complete apparatus, not a reduced record or selected output. Record1 failure effect is then <7.396×10^-7 I, success >.9999992604, and normalized successful-vector distance <.000861. Complete-channel and successful subnormalized CP-map diamond errors are <.00172. Normalized conditioning is nonlinear and is not assigned a diamond-channel distance.

## Resources and interpretation

The exact nominal inventory is M+238 heads, M+243 physical qubits, M+239 head edges and 2M+281 unmerged positive blocks. This point has 5,000,238 heads, 5,000,243 physical qubits, 5,000,239 edges and 10,000,281 positive blocks. Shared source/old/record qubits are counted once, and passive references are excluded. Original incident loads remain; they are not all bounded by the small receiver hopping g.

Increasing lambda tenfold and decreasing T tenfold preserves lambda*T=20, but not every budget. The inverse and traveling errors grow mainly as lambda, the actual moment tail as lambda^(5/2), and the absolute background as sqrt(lambda). Weighted phase and dispersion costs depend on lambda/g. The checked derivative/cancellation and IBP machinery make the complete budget useful without assuming those errors invariant. No parameter sweep or optimum is claimed.

Exact correlated coefficients, the supplied product preparation, original filter/source calibration, selective positive local interactions, native Hamiltonian/Record interpretation and physical time units remain premises. This note does not import source-offset tolerance, arbitrary hardware robustness, a native program cell or a coefficient supplier. The guarantee is one chosen read in a finite interval, not repeated monitoring, permanent halt, irreversible memory, reset/reuse or all-late-time finite output.

## Evidence, exposure and review gates

The packet links above use the repository path `outputs/faster_three_site_2026_10_17/proofs/<folder>__<filename>`. Root owns the manifest, inherited dependency closure, exact repository copies and graph validation. The new point assembles whole cited proofs at their stated scopes; source hashes alone do not validate a theorem.

I authored the new point and the prepared inverse derivative, as well as scalar/source/time ancestors, and checked other interfaces. The cubic cancellation and background IBP have separately authored, source-exposed checks. This note is synthesis by an exposed author, not independent recertification of my own premises or blind/model-diverse review. The distinct point review reconstructed the complete sum and found no load-bearing correction. Its two prose qualifications concern the absolute baseline and its scaling; the present note explicitly labels both as absolute. Final publication integration remains pending. No scientific runner, quadrature, dynamics, sweep, new performance point, W/Git/PR/checkpoint/prompt/model change or delegation occurred while drafting this note. Only this note was created.

Exact primary revisions:

- `three_site_prepared_inverse_derivative/PROPOSAL.md`: `25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84`.
- `three_site_prepared_inverse_derivative_check/REVIEW.md`: `3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c`.
- `three_site_cubic_derivative_cancellation/PROPOSAL.md`: `d57ca3702567780319131cdcadd824588364b93d77575e26b56e00565fd292ac`.
- `three_site_cubic_derivative_cancellation_check/REVIEW.md`: `c65696bec16ece9a1080fd24100fb8d7130821f76136f35810d3d148c155d5d4`.
- `prepared_background_ibp/PROPOSAL.md`: `90d42e3699496e7694ddda630672af778a506b795865118757ab1e57da4a9c5a`.
- `prepared_background_ibp_check/REVIEW.md`: `5c4c1e2b8930be39195181681c563cd0c150611ad07a201316f3096e5a55ea12`.
- `three_site_faster_nominal/PROPOSAL.md`: `48cdce93fd998d94334182866a37d29bf69b674f58d84dd653e9cea5590f1263`.

- `three_site_faster_nominal_check/REVIEW.md`: `f28828c93e59f281ae2a8d813ba3d6a88b4088bbbb855fcc265a6e88e0dee433`.
