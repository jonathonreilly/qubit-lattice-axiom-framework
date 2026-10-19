# Mediator and background recovery with the actual source-time norm left explicit

Status: conditional author derivation requiring distinct checking. This extends the checked stationary mediated inverse to an explicit represented recovery bound for every new mediator head and the emitter-free finite background plus all closed slow tails. The actual represented three-source time norm is an INPUT, not a conclusion. No scalar pulse, normalized output, runtime or finite receiver theorem is imported.

## 1. Domain, exact maps and additional synthesis hypothesis

Use the corrected physical installation d2b7b435 and mass-tuned family of the checked loaded-inverse source5f909e1e/reviewf6303bb3. In particular remove the existing j n_p cap before installing the new path, extend shared B and c_att once, keep fixed positive supplied coefficients and disjoint paths, and impose all three strict gates eta<1, k_C>0 and zeta_m<1 on 0<rho<=min(d_bg,a/2), lambda<=1e-8. All symbols in that source retain their definitions:

    a=J_m-q, b=.185-(J_m+q),
    s_lambda=sqrt(1-3lambda/j), kappa=sqrt(3jlambda),
    theta3=(1-rho²/a²)^(-m)-1,
    b_mix=kappa(1+theta3)e_tilde tau,
    tau=gamma3²/b, Z2=1+v+w.

There are two physical windows centered at c_att+2j+1 and c_att+2j+3, both of halfwidth rho. On each, D=(E-c_att-2j)I-B has selected value delta and complementary gap at least .185. All assertions hold on both physical lips and uniformly in record/parity sectors. They extend by identity on passive references; the actual background need not commute with B or K.

Let V put the actual product head seed at s0 with its original old-input embedding. Define the physical source resolvent column

    U_s^±(E)=S^±(E)^(-1)V_s,

where V_s is the source-coordinate seed embedding and ||V_s||=1. This is the PHYSICAL inverse, including the mass congruence and fixed gauge of the loaded source. Let L^±(E) be the unchanged emitter-free background recovery map from forcing at p to all its 235 finite heads and all closed slow tails, with propagating stationary rays excluded. The checked full-forcing value bound is ||L^±||<=L0=14000. Its port row is G^±. This is independent of the source emitter coefficient: the background has no emitter.

For a time-domain assertion impose the actual assembled spectral matching/regularity hypothesis: on the two windows the coordinate-projected spectral measure of V is represented by the difference of these physical lower/upper boundary columns, with no missing atom or singular term in the retained windows, and the recovery expressions below are the actual coordinate columns. The finite and closed-tail columns must admit the displayed Bochner integrals in their physical Hilbert spaces. The finite bounds below provide integrable majorants once this identification holds; a stationary inverse estimate alone does not prove the absence of hidden in-band spectral mass. No bounded whole-space resolvent on continuous spectrum is assumed.

Let A_s(t) denote the norm of the ACTUAL represented three-source time map, namely the source projection of exp(-itH)E_H(I)V under that matching hypothesis. It includes both physical windows together. No small bound or decay is assigned to A_s(t) here.

## 2. Full prepared column ceilings, including wrong windows

Put R_delta=sqrt(delta²+lambda²) and define

    C_f=6/[s_lambda(1-zeta_m)],
    x=b_mix/k_C,
    U_P=C_f(1+x), U_C=C_f x(1+x).

The ordered block inverse in the checked source gives, for the FULL prepared column on each window and lip,

    ||P_s U_s|| <= U_P/R_delta,
    ||C_s U_s|| <= U_C/R_delta+1/k_C.                 (1)

Indeed selected forcing contributes at most C_f/R_delta and complementary forcing at most C_f x/R_delta to the first row. Their complementary responses contribute C_f x/R_delta and C_f x²/R_delta+1/k_C. Bounding the two input projections separately by one is conservative and requires no orthogonality of output images. Physical congruence factors have norm at most one and commute with these selected/complementary projections. They have been bounded above, not declared equal to one or removed from the exact column. Wrong-window complementary forcing and its O(1/k_C) term remain.

The physical third hopping obeys

    ||t3(D)P|| <= t_P:=sqrt(Z2) kappa(1+theta3),
    ||t3(D)C|| <= tau.

The sqrt(Z2) is essential: kappa is the mass-congruent center coefficient, not the physical hopping. Define

    D_* = t_P U_P+tau U_C,
    J0=2 asinh(rho/lambda),
    J1=2[sqrt(rho²+lambda²)-lambda].

Then for w=t3(D)(U_s)_2,

    ||w|| <= D_*/R_delta+tau/k_C,
    int ||w|| ddelta <= W0:=D_* J0+2rho tau/k_C.      (2)

Here and below the integrals are over [-rho,rho]. The exact elementary integrals are int R_delta^-1=J0 and int |delta|/R_delta=J1. There is no substitution of a selected scalar source column for the full prepared map.

## 3. Ordered loaded background and port recovery

Mediator elimination adds the port diagonal S_p=s3(D). With no independent background forcing, the original background equations give

    psi_p=G(S_p psi_p+w),
    psi_p=G_tilde w,
    psi_bg=L (I-S_p G)^(-1) w.                      (3)

The second equality uses G_tilde=(I-G S_p)^(-1)G. The last follows from S_p psi_p+w=(I-S_p G)^(-1)w. Its order is fixed: neither L nor G is commuted through S_p or t3. Since ||S_p G||<=eta, it follows that

    ||psi_bg|| <= L0/(1-eta) [D_*/R_delta+tau/k_C],
    ||psi_p|| <= B_tilde [D_*/R_delta+tau/k_C].       (4)

In particular set

    P0=B_tilde W0,
    P1=B_tilde[D_* J1+rho² tau/k_C].

These bound respectively int||psi_p|| and int|delta| ||psi_p||. They include port responses induced by all complementary columns; it would be incorrect to keep only t_P or assume the port is always selected.

For each physical window, Stone uses (column^-−column^+)/(2pi i). Applying the norm bound on both lips and then summing the TWO windows gives the conservative global factor 2/pi multiplying a single symmetric-window majorant. Thus the represented background and port time maps satisfy, for every real t,

    B_I(t) <= (2/pi) L0 W0/(1-eta),
    A_p(t) <= (2/pi) P0.                            (5)

No extra actual omitted spectral vector is included in (5). The port is already one of the background heads; A_p is used below only to bound its role as a mediator endpoint, not to add a new physical region to B_I.

## 4. Static internal recovery plus a genuinely weighted remainder

For mediator l its PHYSICAL internal row equation is

    psi_int,l=-gamma_l (D tensor I+A_l)^(-1)
                         (C_L psi_left+C_R psi_right). (6)

The sign is the negative endpoint coupling in its E−H equation. Here A_l is the positive adjacency, independent of E, with spectrum avoiding zero by a. Define R_l(D)=(D tensor I+A_l)^(-1). Use the identity

    R_l(D)=A_l^-1 tensor I+[R_l(D)-A_l^-1 tensor I]. (7)

Crucially the static first term is used on ALL internal fibers, not only P. It is the same physical map on both windows. This allows its Stone integral to act on the combined actual endpoint time maps and preserves any inter-window cancellation already present in A_s(t). A window-dependent P-only static term would not in general be controlled by A_s(t) alone.

On selected fibers the resolvent identity gives

    ||[R_l(delta)-A_l^-1]P|| <= |delta|/[a(a-rho)].

On complementary fibers use the actual gap and the triangle inequality:

    ||[R_l(D_C)-A_l^-1]C|| <= 1/b+1/a.              (8)

No small detuning is imposed on D_C. These are exact resolvent comparisons, not differentiated value inequalities or a replacement of the physical complementary root.

Let gamma_*=max_l gamma_l. Stack the three joint endpoint injections. Source coordinates s0,s1,s2 occur respectively once, twice, twice; p occurs once. Their joint norm is at most sqrt(2)||psi_s||+||psi_p||. The two internal endpoint injections within each mediator have orthogonal ranges, including at length n_l=1. Consequently the static part of the FULL internal time map has norm at most

    gamma_*/a [sqrt(2) A_s(t)+A_p(t)].              (9)

This bound aggregates all 10m−4 mediator heads without a spurious length-dependent per-site factor. The isolated mediator dressing/preparation theorem is not used.

For the remainder, the selected endpoint stack is bounded by sqrt(2)U_P/R_delta+||psi_p||, and the complementary stack by sqrt(2)(U_C/R_delta+1/k_C)+||psi_p||. We deliberately use the full port ceiling in both projections; this is conservative, not a claim of orthogonality or negligible closed return. Combining (8), the integrals J0,J1 and the two-window/two-lip factor gives the time-independent bound

    E_int=(2gamma_*/pi) {
       [sqrt(2)U_P J1+P1]/[a(a-rho)]
       +(1/a+1/b)[sqrt(2)(U_C J0+2rho/k_C)+P0] }.
                                                               (10)

Thus every represented mediator-internal coordinate satisfies jointly

    M_I(t) <= sqrt(2)gamma_*/a A_s(t)
                     +(2gamma_*/(pi a))P0+E_int.    (11)

The lower lip is its own actual rectangular recovery column. Formula (10) bounds the difference by separately bounding both columns; it does not replace an off-diagonal spectral density by entrywise imaginary part or by an adjoint of the same upper column.

## 5. Resulting apparatus interface and asymptotic scaling

Let N_I(t) be the sum of represented source, mediator-internal, finite-background and closed-tail amplitudes in the actual spatial decomposition; the propagating open output terms are excluded. Triangle inequality, sufficient even where the window-specific closed-tail descriptions differ, gives

    N_I(t) <= (1+sqrt(2)gamma_*/a) A_s(t)+E_rec,

    E_rec=(2/pi)L0 W0/(1-eta)
                         +(2gamma_*/(pi a))P0+E_int. (12)

It is also a bound on the norm of that combined nontraveling map. This is an interface to a separate actual source-time estimate, not an estimate of that source-time map by the old cubic pulse. It contains every new head and every background closed tail in the stated decomposition. No bound on the propagating outgoing or incoming errors, common output waveform, scalar normalization or readout success is supplied.

There is a useful asymptotic statement, with fixed supplied coefficients, fixed a>0 and fixed background g,h. For the checked eventual choice rho=sqrt(a lambda), all strict inverse margins are bounded away from zero for sufficiently large m. Then U_P=O(1), U_C=O(sqrt(lambda)), t_P=O(sqrt(lambda)), D_*=O(sqrt(lambda)), while

    J0=O(log(rho/lambda)), J1=O(rho).

Therefore

    W0,P0 = O(sqrt(lambda) log(rho/lambda)+rho),
    P1 = O(sqrt(lambda)rho+rho²),
    E_int = O(rho+sqrt(lambda) log(rho/lambda)),
    E_rec = O(sqrt(lambda) log(1/lambda)).             (13)

All constants can depend on the fixed supplier and background. The explicit formulas (2),(10),(12), not this notation, define the finite-m certificate. These estimates require neither a vanishing calibration floor nor a small full background inverse. The floor enters bounded constants, and the complementary source response is multiplied by t3 or integrated over a shrinking width. If g or the mediator gap varies with m, the statement (13) is not justified without rechecking every constant. A fixed rho would also not give this conclusion.

The coefficient of A_s(t) does NOT tend to one by increasing m at fixed supplier: gamma_*/a remains fixed. Nothing here proves A_s(t) tends to zero, or that its correct pulse equals the old nominal one. This is precisely the independent source-time obligation left open.

## 6. Outside state, phase and remaining obligations

The actual global outside vector is separate. The checked witness gives

    eps_out <= delta_p,m+sqrt(2 Z0 Z1/3)
                      lambda/[rho sqrt(1+u_m)],
    delta_p,m=sqrt(2[1-1/sqrt(1+u_m)]),
    u_m=u(1-r^(4m-2)).

It can be capped by one. In any eventual complete spatial comparison this actual outside vector is added ONCE, after composing represented components. It is not added separately to (5), (11) and A_s. Its fixed product-preparation allowance need not vanish as m grows. No in-band or outside spectral type is silently discarded.

Physical gauge/mass factors remain in U_s, (3) and (6); their upper bounds above use only contractions where justified. In particular the physical t_P includes sqrt(Z2), and a future output comparison still carries the seed-to-port (-1)^m, original c_att, old aging exp(-itK) and literal W. Scalar phase factors can be ignored only inside these norm estimates. There is no input-dependent refitting or assumption that the processor commutes with B.

Outstanding conditions are actual assembled in-window spectral regularity/matching if not independently established, a bound on the actual A_s(t), and actual traveling coefficient/common-waveform estimates with physical normalization and all wrong-window columns. A finite cut and resource inventory require a separate explicit geometric installation. This note proves none of these by reference to the old source. It does not assert a complete apparatus theorem, selected runtime, finite holding, permanent halt or native coefficient/preparation mechanism.

## 7. Source identities and exposure

Paths are relative to the renewal directory. This work refreshed the exact loaded-inverse/reconstruction and corrected-installation premises; the full-forcing background definition and value-bound scope were refreshed directly in the original recovery source. Unchanged mathematical ancestor checks are reused, not audited anew.

- `mediated_loaded_inverse_interface/PROPOSAL.md`: 5f909e1ea897e9aaef31dd362e42fc60d5ba0b5f595d28bd12f1d000d8552a22; own distinct check `mediated_loaded_inverse_interface_check/REVIEW.md`: f6303bb308a56b0db39cf66b673e40174be775e7a32a71f28a6e489beb3990c3.
- Corrected `mediated_critical_source_interface/PROPOSAL.md`: d2b7b435f6813847a0b293d5584a3aa5af844a02be09a95b768adc4ea4f963e3; correction recheck 2cea5e9a3cd59b63d09bf21c1ddb929fff2251f9044ed3bd7189b3df10062ff8.
- `prepared_core_recovery/PROPOSAL.md`: cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9; own dwell check 88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 and composition check 52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c.
- `mediated_product_seed_witness/PROPOSAL.md`: 57892f7690a5f634c44c2fe0752c5cfb682d3fbfbda1aa4c1ca4edd45bb0fdee; own check aac24f84f9373a5e59511195e717780d24ecffc41c1e4cb878bcf262a4085630.

Root suggested the static-resolvent splitting and possible coarse shrinking-width scaling; these were candidate routes, not premises. I previously checked the loaded inverse and witness, authored several derivative/recovery ancestors, and share substantial exposure with this lane. The present full recovery construction and constants are new author work requiring a distinct check. I have not read, derived or certified another agent's pending selected-source pulse for this task.

Only this proposal was written. No W, Git, PR, checkpoint, editable prompt or model changes, scientific runner, numerical inverse/evolution, sweep, operating point or delegation occurred. No claim of independent ancestral calibration or retained audit status is made.
