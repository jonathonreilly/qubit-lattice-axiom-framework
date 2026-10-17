# Fixed dimensionless slow-lead scaling: conditional quantitative corollary

Status: authored corollary, requiring distinct checking. Its composition dependency remains pending distinct review at SHA256 `8cd26edcb7941d8254494480455d17c137652ec779e37e78901de5a04e71ac9e`. This standalone artifact supplies sufficient common envelopes, not monotonicity of the exact spectral masses.

## Domain, evidence and exposure

Fix the supplied original apparatus and .0027<j<.003. An admissible base triple satisfies

    0<kappa0<=10^-8, 0<g0<=10^-6, 0<h0<=4e-6,
    gamma0=kappa0^2/j, d0=2j sin h0,
    H=d0/gamma0>=100, L=g0/gamma0>=100, H/L<=.024.

Take T0>0 and sigma0=gamma0 T0 with L sigma0>=1. Keep the exact same-center occupation/connector relations, emitter diagonal, original source calibration, shared K/W, physical scalar c_att and supplied seed. The varying h is a spectral proof cutoff, not hardware.

The load-bearing uniform endpoint source is `../slow_lead_uniform_endpoint/PROPOSAL.md` c8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887, with root check f3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0. The scalar source is `../slow_lead_uniform_reference/PROPOSAL.md`5f2026dc3f63a757f13cf58bc468f05de10cfca9f04fda9c6615b816c9b94907, with distinct check338e554834f994741982842c555589db5e62dba9ad121233989ce60068f26c93. Complete arguments/checks were read in the preceding coherent tasks. The actual all-time and finite composition is `../slow_lead_uniform_composition/PROPOSAL.md` at the pending-check revision pinned above. All original physical/inverse/calibration ancestry remains conditional; no fresh recalibration is asserted.

I authored these uniform sources and composition. Root exposed this exact one-parameter route. This is author derivation, not an independent check. The temporary corollary addition to the composition was removed, restoring that file byte-exactly to its pinned revision before this separate deliverable was completed. No W/Git, PR/publication, checkpoint, prompt, model or further-agent changes occurred. No scientific execution or parameter sweep occurred.

## Scaling and common certificate

Root exposed the following candidate after the general formulas were drafted. Use the admissible base data just defined. For0<a<=1 set

    kappa(a)=a kappa0, g(a)=a^2 g0,
    h(a)=asin(a^2 sin h0), T(a)=a^-2 T0.

Then gamma(a)=a^2 gamma0 and d(a)=a^2 d0 EXACTLY. Hence H,L and sigma0=gamma(a)T(a) are fixed, the domain remains satisfied, and g(a)T(a)=g0T0. The exact cutoff condition below therefore uses the same M for every a. This is longer waiting at smaller kappa, not faster operation or a proof of reduced coefficient precision.

Here is one explicit uniform certificate; it avoids assuming that the exact transmitted mass p_s is invariant. Set

    pbar=1-.68/H-.043H/L^2>0,
    C1=41000/.0053,
    eta_bar(a)=1.05/pi *[2j*(8e-18)*atan(H)
                  +(a^2 kappa0^2 C1+244 kappa0^2/g0)*log(1+H^2)],
    epsilon_sp_bar(a)=sqrt(min{1,.68/H+2eta_bar(a)}).

The composition mass formula and the uniform reference tail imply epsilon_sp<=epsilon_sp_bar(a). This bound does not increase as a decreases; the calibration floor and the kappa0^2/g0 term survive.

The explicit BASE moment ceilings are

    U2=4kappa0^2 h0/[pi(2j-gamma0)^2]*(h0/sin h0)^2,
    UD2=16kappa0^2 j^2 h0/[pi(2j-gamma0)^2].

These bound the unnormalized u-squared and energy-squared reference moments. Since asin(a^2 sin h0)<=a^2 h0, 2j-gamma(a)>=2j-gamma0 and h/sin h decreases with decreasing h, the corresponding moment upper bounds at a are at most a^4 U2 and a^4 UD2. Thus a safe outgoing certificate is

    Eout_bar(a)=sqrt(2)*[2e-13+400a^2 sqrt(U2)
                                      +(1.01/g0)sqrt(UD2)]
                  +8.4e-25 a^2 kappa0 sqrt(2h0).

It also does not increase as a decreases. The raw incoming certificate2.7/sqrt(L)+sqrt(.68/H) is constant. The composition local formulas have Ecore=E_floor+a^2 E_variable and Bcore=a B_linear+a^3 B_cubic with nonnegative fixed coefficients: this follows by writing IG(a)=a^-2[2a_G atan(H)/gamma0]+b_G log(1+H^2) and IL(a)=2a_L asinh(H)+a^2[2b_L gamma0(sqrt(1+H^2)-1)]. Hence epsilon_local(a) is nonincreasing as a decreases, with its explicit emitter floor retained.

For completeness, all local coefficients can be written explicitly. Set c=1/1.03, L0=4e5, a_G=10^-45, b_G=1.27e7, a_L=4121, b_L=5.5e9 and

    Gf=2a_G atan(H)/gamma0, Gv=b_G log(1+H^2),
    Lf=2a_L asinh(H), Lv=2b_L gamma0(sqrt(1+H^2)-1),
    E_floor=kappa0^2 Gf/(2pi c^2),
    E_variable=kappa0^2 Gv/(2pi c^2),
    B_linear=kappa0 Lf/(2pi c)+kappa0^3 L0 Gf/(2pi c^2),
    B_cubic=kappa0 Lv/(2pi c)+kappa0^3 L0 Gv/(2pi c^2),
    Elocal_bar(a)=2sqrt[(E_floor+a^2 E_variable)^2
                                      +(a B_linear+a^3 B_cubic)^2].

The factor2 adds the two physical windows; the full inverse c=1/1.03, direct DeltaL term and both spectral lips are retained. These are nonnegative fixed coefficients, so their monotonic envelope claim is immediate. E_floor=j*a_G*atan(H)/(pi c^2) survives at small a. This is a certificate floor, not a claimed nonzero actual error.

## Common finite horizon and sufficient tolerances

For a common success lower certificate set

    Cbar=min{1,2.1exp(-.4975 sigma0)
                              +.8/[H sqrt(pbar sigma0)]},
    Rbar=sqrt(pbar)*sqrt(1-Cbar^2).

Because p_s>=pbar, the actual outgoing norm on every t in[T(a),2T(a)] is at least Rbar. Choose any integer M>=1. Exact cap transfer on the absolute horizon[0,2T(a)] is at most

    Dcut=min{2,1.2 exp[-M+4g0 T0 sinh1]},

independent of a. To allocate epsilon_tr>0 it suffices to take

    M>=max{1,ceil(4g0 T0 sinh1+log(1.2/epsilon_tr))}.

Define the complete branch certificate

    Iin_bar=2.7/sqrt(L)+sqrt(.68/H),
    Einfinity_bar(a)=epsilon_sp_bar(a)+Elocal_bar(a)
                                      +Iin_bar+2Eout_bar(a),
    EM_bar(a)=Einfinity_bar(a)+Dcut.

Every term is a valid upper envelope for the corresponding actual-composition term. The outside mass is charged once, and the two outgoing-coefficient allowances separately cover the incoming error and outgoing error; the reference incoming term itself is Iin_bar. All prepared inputs, wrong-window rows and passive references retain the scope of the pending composition. EM_bar(a)<=EM_bar(1) for0<a<=1 without any monotonicity claim about exact p0 or p_s.

For desired single-read probability p_* and normalized successful-vector error e_*, the explicit sufficient BASE conditions are

    Rbar>EM_bar(1),
    (Rbar-EM_bar(1))^2>=p_*,
    2EM_bar(1)/Rbar<=e_*.

If these hold, the same inequalities certify every member0<a<=1 at every ONE chosen read time in[T0/a^2,2T0/a^2], with the SAME M. The subnormalized successful CP-map diamond error is at most2EM_bar(1). The comparator is the actual parameter-dependent infinite-space reference packet with literal old aging and W; conditioning does not define a new linear channel. A weaker complete finite normalized-vector error is <=min{2,sqrt(2(1-Rbar+EM_bar(1)))}. No sharper qualitative asymptotic rate is imported.

This implication does not claim that a previously accepted base estimate using sharper exact masses automatically meets these more conservative common inequalities. No p_*,e_*,T0 or M is selected here. The physical inventory is M+241 qubits and2M+277 unmerged positive blocks, independent of a, under the exact cap construction and shared-register convention.

## Interpretation and surviving obligations

This is a conditional time/length scaling corollary of the present formulas, subject to their pending distinct check and exact-supply premises. The reference waveform changes with the parameters and is always the corresponding physical comparator. No statement at a=0, fixed physical read time, finite infinite-time storage, manufacturing tolerance or optimized resource scaling follows.


The composition also gives a separate qualitative infinite complete-state envelope epsilon_sp_bar(a)+Eout_bar(a)+1-sqrt(pbar). It has no quantitative onset from this corollary and is not used to replace the finite branch conditions. A nonincreasing sufficient envelope need not describe monotone actual errors or exact success probabilities.

Decreasing a makes waiting time grow as a^-2 and changes supplied hardware coefficients: the slow hopping scales as a^2 and the slow connector sqrt(jg) as a, while onsite compensations must track them exactly. The original shared diagonal correlations and source calibration are still assumed. This proves no achievable manufacturing precision, fixed-error tolerance under independent coefficient perturbations, energy/time-unit conversion or native preparation. At a=0 the emitter is decoupled and the reference normalization/time parametrization cannot be substituted. The corollary claims only the explicit conditional same-length implication for strictly positive a.
