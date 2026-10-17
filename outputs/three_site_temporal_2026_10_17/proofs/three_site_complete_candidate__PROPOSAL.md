# Three-site product source: one conditional complete-output point

Status: **new author composition, requiring a distinct check**. The component interfaces have the scoped checks pinned below. They imply the proposed complete normalized-target vector-map ceiling

    ||embed exp(-it H_M)V - T_norm(t)|| < 0.0006,
    2e14 <= t <= 4e14,                                      (1)

at the single supplied choice

    lambda=1e-13, g=5e-8, h=4e-6,
    T=2e14, M=50,000,000,
    a1=lambda/sqrt(3), a2=lambda sqrt(8/3),
    kappa=sqrt(3j lambda),                                  (2)

with the ORIGINAL calibrated j, not a retuned value. The auxiliary proof cutoff is D=100lambda=1e-11. No parameter sweep, numerical dynamics or optimization was used. The proposed starting point closes with the explicit allocations in section 8, so no hardware/time change was needed during this composition.

This compares the complete unconditioned state, including every head, shared source, record and arbitrary passive reference, with a normalized common physical-halfline target. It does not postselect or normalize actual output. The time interval permits one chosen read; it does not give permanent storage, an intervening-measurement protocol, irreversible capture or reset/reuse. The new composition itself is not independently checked or retained-grade science.

## 1. Actual source, unchanged background and precise comparator

Keep the supplied original contact/filter calibration, shared B, two converters, input cap, eighteen-edge cable and 24-head record gate. Retain every original source/filter inverse and full matching premise and the selective installed-pair geometry. At the old input endpoint p=(40,63,1), use the three source heads

    s2=(40,64,1), s1=(40,65,1), s0=(40,66,1).

The head starts at s0; all other heads are blank, shared sources are in their supplied vacuum, and the computational record is 0. The old four-dimensional input and its passive reference are arbitrary. The checked source installation uses the six positive blocks

    j(n_s2+n_p)-kappa exchange_(s2,p),
    Q_a2(s1,s2), Q_a1(s0,s1),
    (j-a2)n_s2, (2j-a1-a2)n_s1, (2j-a1)n_s0,

where Q_a(x,y)=a(n_x+n_y-exchange_xy). Here kappa<3e-8<j and a1+a2<3e-13<2j. All six are full-qubit-space PSD, all source diagonals are 2j, and compressing off the three source heads leaves exactly j n_p. The emitter-free background and its full eight-coordinate kernel are therefore literally the same ones used in the checked recovery and outgoing-row proofs. No internal system is copied and no new vacancy scalar appears.

The slow output begins at r_m=(100,3+m,2), m>=0, beyond the distinct gate port o=(100,2,2). Its connector is Q_sqrt(jg), its internal bonds are Q_g, and its occupations are (j-sqrt(jg))n_o, (2j-sqrt(jg)-g)n_r0, and 2(j-g)n_rm for m>=1. The finite device retains r_0,...,r_(M-1) and adds the cap g n_r(M-1). This is the checked exact seeded compression, with no absorbing endpoint. The full blocks are positive and time independent. Retain exactly

    K=2I+Z1 Z2,
    W=[(9+12i)I+(-16+12i)X1 X2]/25,
    c_att=c_total+4(sqrt(2)-1)j,
    c_total=2nu+2beta+4gamma_J+4gamma_c.                     (3)

The coefficients in c_total are the unchanged source/filter/junction/converter vacancy coefficients. Actual H is not assumed to commute with K. The vacuum identity B iota=iota K, the ideal commutation of K and W, and the real sector bases retain their original meanings.

The two physical energy windows are I_b=c_att+b+2j+[-d,d], b=1,3, with d=2j sin h. Write delta=-2j cos q=-2g cos k, and keep the actual map

    k_old(q)=2asin(sqrt(j/J)sin(q/2)).

Use the physical halfline Weyl function m_j and the exact scalar determinant

    q3(delta)=(delta^2-lambda^2/3)(delta-kappa^2 m_j(delta+i0))
                                               -(8lambda^2/3)delta.

The subnormalized scalar coefficient, on the centered hard slow interval I_k, is precisely

    F3(q)=kappa a1 a2 (2j sin q) zeta
           exp[i61q+i172k_old(q)]/[sqrt(2pi)j q3(delta)],
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F_s(k)=t_f sqrt(g sin k/(j sin q)) F3(q(k)),
    p_s=integral_(I_k) |F_s(k)|^2 dk.                        (4)

The fixed phase zeta and complex q3 are not fitted or replaced by magnitudes. The first slow site is m=0. The phase 61.5q+.5k+172k_old is not a translation by 61 slow sites. Define the RAW physical-halfline packet

    beta_t(m)=(2pi)^(-1/2) integral_(I_k) F_s(k)
                 exp[ikm-it(2j-2g cos k)] dk, m>=0,
    r_phys(t)=||beta_t||,
    T_raw(t)=exp(-it c_att) J_out[beta_t tensor exp(-itK)W],
    T_norm(t)=T_raw(t)/r_phys(t).                            (5)

J_out supplies source vacuum, blank nonoutput heads and record 1. The passive reference is untouched. Section 7 proves r_phys>0. The normalized target stays on the common infinite comparison space when the finite actual state is embedded there. Its remote tail is not silently truncated.

## 2. Common envelopes, regularity and the one actual outside vector

All estimates below use the supplied fixed j enclosed by .0027<j<.003. At (2), elementary sine bounds give

    2.15e-8<d<2.4e-8, d/g<.48<.5,
    eta=lambda/j<3.71e-11,
    s=sqrt(1-3eta)>.9999999998,
    kappa^2<9e-16, kappa<3e-8.

The emitter-free full-fiber comparison remains

    ||G-G0||<a0+b0|delta|,
    a0=8e-18, b0=46000/.0053+290/g<5.81e9,
    G0=m_j(D_old), D_old=E-c_att-2j-B.

The checked ordered three-site inverse has condition

    Theta=(j a0+kappa^2 b0)/s+6kappa^2(a0+b0 d)<5.24e-6,
    c3=(1-Theta)s>.9999947.                                 (6)

The leading numerator is below .003*8e-18+9e-16*5.81e9; the complementary term is below 7.53e-13. These bounds do not import the former one-site emitter's kappa<=1e-8 premise. That restriction was not a restriction on the unchanged background.

Complete background matching and the strict full-source inverse margins on both physical lips give continuous seed boundary values on neighborhoods of the closed windows. All later Stone expressions rely on this regularity. Algebraic conditioning or the moment alone would not justify discarding in-window singular seed mass. Outside the windows every spectral type remains charged.

The exact ACTUAL installed seed moment is

    mu6=3lambda^6+(8/3)j lambda^5<8.00000001e-68.

It retains the port-reaching third-power term. No downstream dynamics or nonreflection assumption is used in this moment. For the common union I=I_1 union I_3 and full prepared embedding V,

    epsilon_sp=||E_H(I^c)V||
       <=sqrt(2mu6)/d^3<4.1e-11.                            (7)

The two old-energy images are not assumed orthogonal after omission. The sqrt(2) pays their input aggregation, and passive-reference tensoring preserves it. Inequality (7) is charged ONCE in the final complete-state comparison. It is not separately added to source, background or traveling contributions.

## 3. All three actual source heads

Use the checked local-source interface, whose error is for the represented state E_H(I)V. Its reference three-site polynomial norm is

    F(z)=exp(-z)sqrt[(1+z+z^2/3)^2+(z+z^2)^2/3+2z^4/9],
    z=lambda t.

Let E_vec be its three weighted scalar density-error norm. The checked explicit errors have C=6eta+9eta^2<2.227e-10 and q=1-3eta. Each of E0,E1,E2 is below 2.3e-10, including its finite-band and exterior rational tails, so E_vec<4e-10. This charges both intermediary sites; it is not a seed-return bound.

For clarity the full ordered-resolvent integral allowances used here are

    D_sel=kappa^2 a1 a2/[pi(1-Theta)] *
       [a0*pi/(2s^2 lambda^3)+b0/(s^2 lambda^2)
                           +(6/s)(2a0/lambda^2+2b0/lambda)],

    D_wrong=170 kappa^2 a1 a2/[pi(1-Theta)] *
       [(2a0/s)asinh(d/lambda)
        +(2b0/s)(sqrt(d^2+lambda^2)-lambda)+12a0d+6b0d^2].   (8)

They retain the full internal inverse, both lips, and the other prepared energy on each window. Since a1 a2=(2sqrt(2)/3)lambda^2<.944lambda^2, the leading term of D_sel is below

    (9e-16)*.944*(5.81e9)/[3.14(1-5.24e-6)s^2].

Including every other displayed term gives D_sel<1.574e-6. For D_wrong use asinh(d/lambda)<14 and sqrt(d^2+lambda^2)-lambda<d: its bracket is below 280 and its prefactor below 4.61e-40, giving D_wrong<1.4e-37. Neither complement is set to zero.

The reference truncation allowance is eta_ref<=sqrt(2mu6)/d^3<4.1e-11. This is a comparison-reference truncation cost inside the represented-source argument; it is distinct from the one actual outside vector in (7).

For z>=20 every component polynomial times exp(-z) in F decreases. At z=20 the polynomial square sum is below 344^2. The elementary Taylor witness sum_(n=0)^12 5^n/n!>148 gives exp(-20)<148^-4<2.1e-9. Consequently F(z)<7.3e-7 throughout [T,2T]. With sqrt(2)<1.415, the checked aggregate yields

    S_I(t)=||P_source exp(-itH)E_H(I)V||
      <=F(lambda t)+E_vec+eta_ref+sqrt(2)D_sel+2D_wrong
      <3e-6.                                                (9)

The record-X and parity sectors are genuinely orthogonal and contribute no extra multiplicity factor; selected errors from the two old-energy windows have already been aggregated without assuming their outputs orthogonal.

## 4. Represented finite background and every closed slow tail

The prepared-core proposal proves the full-forcing recovery norm L0<14000, covering all 235 background heads and complete closed slow tails. Its new discrete dwell identity and converter/cap step now have a distinct check, and its subsequent range/Stone aggregation has a separate check. At assignment the dwell check was pending. Both checks were subsequently read completely at the exact pins in section 10. The composition check's historical pending-dwell wording is preserved in its original file; the supplied dwell review resolves that dependency locally. This does not independently validate this new full-device composition.

On each physical window and lip, the actual background seed column is

    -kappa L(E) a1 a2 Q3(E)^(-1),
    ||Q3^(-1)||<=1/[c3(delta^2+lambda^2)^(3/2)].

Absolute integration, both lips and both windows, gives

    B_I(t)<=8sqrt(2) kappa L0/(3pi c3)<.000505.              (10)

Use sqrt(2)<1.415, pi>3.14, kappa<3e-8 and c3>.9999947 for the last strict bound. This covers wrong-window forcing and every internal output row. It excludes all three new source heads and the propagating output ray, so it does not duplicate (9) or the traveling terms. The output classification is retained separately on each physical window before their errors are added.

Equation (10) is an all-time represented-background upper bound. No eta_out is appended: (7) is the sole global actual omitted charge. No background derivative, D3 integral, Markov substitution of the actual Q3, or presumed cancellation is used here. The nondecaying .000505 allowance is a sufficient norm estimate, not a physical asymptotic residual or lower bound.

## 5. Raw outgoing AND incoming coefficient errors

The checked actual outgoing interface supplies the raw selected allowance

    E_sel<=2.1e-13 sqrt(p_s)
        +[304/(2j cos h)+.302/g]lambda/sqrt(3)
        +1.384 Theta sqrt(p_s)/(1-Theta).                  (11)

This uses the exact scalar second moment lambda^2/3 and the conservative bound on the theta-weighted integral. With sqrt(p_s)<=1, 304/(2j cos h)<56300, .302/g=6040000 and 1/sqrt(3)<.578,

    E_sel<2.1e-13+(6096300)(.578e-13)
                       +1.384*(5.24e-6)/(1-5.24e-6)
          <7.61e-6.

The wrong-window row remains

    B_wrong=170 kappa a1 a2[2e-23+461 Theta/(1-Theta)]
            <1.17e-34,
    E_wrong=.006 B_wrong sqrt(2h)<2.1e-39.

Thus the complete-input RAW outgoing coefficient allowance is

    E=sqrt(2)E_sel+E_wrong<1.08e-5.                        (12)

The actual real two-lip Stone identity identifies the outgoing term with F_actual and the incoming term with its entrywise conjugate, while preserving exp(-itE_b) on both. The ideal incoming factor is W* times the conjugate scalar coefficient; it is not W and is not folded into the outgoing target. Fixed real coordinate conjugation acts on the coefficient matrix, not on an unknown old/reference input. Wrong-window rows retain their actual energy until bounded.

That checked identification gives the SAME E for the incoming coefficient discrepancy. Since the two waves share a physical ray, their errors add by triangle inequality. The final comparison therefore pays

    2E<2.16e-5,                                           (13)

using raw E, not twice a spectrally normalized outgoing allowance. Ideal physical normalization is charged later exactly once.

## 6. Explicit physical phase and scalar time bound

Set xi=2g(k-pi/2), delta(xi)=2g sin(xi/(2g)), and choose D=1e-11. This D is only a proof cutoff; the actual hardware and hard packet cutoff remain (2) and h=4e-6. Since D<d, it lies inside the actual retained interval. Let

    phi(xi)=61.5q(delta(xi))+.5k(delta(xi))
                                      +172k_old(q(delta(xi))),
    phi0=phi(0), Phi=sup_(|xi|<=D)|phi(xi)-phi0|.

Here phi0 is the exact existing phase at the center, not a freely selected phase of the output target. The constant zeta and the full q3 phase remain in (4).

To bound Phi on the actual domain, retain the original calibration

    J=.030021107107032,
    k0=2atan(1/4.510351185997098), j=J(1-cos k0).

Thus .09<j/J<8/85. On |q-pi/2|<=h, the exact relation cos k_old=1-(j/J)(1-cos q) implies sin k_old>.4: setting y=(j/J)(1-cos q) gives .08999964<y<.1000004 and 2y-y^2>.16. Consequently

    |dk_old/dq|=(j/J)sin q/sin k_old<4/17<.24,
    |dq/dxi|<=1/(2j cos h), dk/dxi=1/(2g).

Every propagation and connector phase derivative is therefore paid:

    |dphi/dxi|<102.78/(2j cos h)+1/(4g)<5.02e6,
    Phi<5.02e-5.                                          (14)

In particular no source phase is silently optimized away, and no new j is chosen to center-match the source.

Use the checked scalar reference-time proof with its separately checked ROOT tail refinement. Its ingredients are

    v=D^3/(24g^2 lambda)=1/6000000,
    rho_t=3eta+3v(1+v)^2<5.002e-7,
    A=D^2/(4j^2)+5D^2/(4g^2)<5.01e-8,
    E_cent=(A+Phi+rho_t)/(1-rho_t)<5.076e-5.

All denominator margins are strict. Throughout t<=2T=4e14,

    t D^3/(24g^2)<=6.666667e-6<6.667e-6.                   (15)

The physical cutoff image satisfies

    delta_D=2g sin(D/(2g))>.999999998 D,

by sin z>=z-z^3/6 at z=1e-4. The exact finite-band scalar-tail refinement, the rational tail and the lattice alias allowance obey respectively

    U_sharp<=sqrt[16/(15pi(1-3eta))]*(lambda/delta_D)^(5/2)
             <5.84e-6,
    V_tail=sqrt[16/(15pi)]*(lambda/D)^(5/2)<5.83e-6,
    Z_alias=(8/3)sqrt[16/(15pi)]*(lambda/(2pi g))^(5/2)
             <1e-16.                                      (16)

For example the square-root constant is below .583 using pi>3.14. U_sharp and V_tail are different cutoff errors and are both retained. The alias term is required because the physical head coordinate is an integer; a continuum impulse is not silently substituted for a lattice state.

The scalar transmitted mass satisfies the checked bound

    1-p_s<=Xi<=mu6/d^6+lambda^2/(3g^2)<1.334e-12,
    1-sqrt(p_s)<7e-13.                                    (17)

Combining (14)--(17), including that exact normalization allowance once INSIDE the scalar packet comparison, gives the normalized reference-time error

    E_time(t)<=E_cent+tD^3/(24g^2)+U_sharp+V_tail
                                      +Z_alias+1-sqrt(p_s)
              <6.91e-5, T<=t<=2T.                         (18)

The sum of the first four displayed numerical ceilings is .000069097; the remaining terms are below .000000000000701. This bound is for the exact phase-sensitive packet (4), not for an unqualified Markov surrogate. The cubic impulse is used only inside the checked comparison, which explicitly pays dispersion, phase, source denominator, both tails and aliases. No actual interacting coefficient is analytically continued.

## 7. Incoming reference and ideal physical norm

The checked scalar estimate for the conjugate incoming partner gives its normalized physical-halfline norm at most E_time. Restoring the raw coefficient multiplies it by sqrt(p_s)<=1, while the carrier exp(-i2jt) is retained. Therefore

    J_raw(t)<6.91e-5.                                     (19)

For the outgoing negative-halfline fraction, the same proof supplies C_out<=H(lambda t)+E_time, where

    H(z)^2=exp(-2z)[(2lambda/(3g))z^4
                           +(2/3)z^4+(4/3)z^3+2z^2+2z+1].

Every monomial exp(-2z)z^n, n<=4, decreases for z>=20. The bracket at 20 is below 344^2, and exp(-20)<2.1e-9 as above, so H<7.3e-7. Hence

    C_out<7e-5.                                           (20)

The scalar proof excludes m<=0, conservatively containing the required complement m<0. It has not counted m=0 as an omitted physical output. Parseval and (17),(20) give

    r_phys(t)>=sqrt(p_s)sqrt(1-C_out^2)>0,
    1-r_phys(t)
       <=(1-sqrt(p_s))+sqrt(p_s)(1-sqrt(1-C_out^2))
       <7e-13+4.9e-9/(1+sqrt(1-4.9e-9))
       <2.46e-9.                                         (21)

This is the cost of normalizing the ideal PHYSICAL halfline target in (5). It is separate from the error used to prove the scalar time estimate; no algebraic equality identifies those two proof uses. The final traveling comparison uses raw E, so it does not also pay twice the outgoing spectral-normalization allowance. The actual physical state is never renormalized.

The scalar time proof grows with its upper time horizon. Equation (18) was bounded through 2T; it is not asserted uniformly for all later times.

## 8. Complete infinite comparison and finite transfer

The checked traveling synthesis, with all actual local ranges supplied, is

    ||exp(-itH_infinity)V-T_norm(t)||
      <=epsilon_sp+S_I(t)+B_I(t)+2E+J_raw(t)+1-r_phys(t).    (22)

This charges the raw outgoing and incoming coefficient errors separately, both old-energy windows, all three source heads, all remaining finite heads, every closed slow tail and one global actual outside vector. The common scalar, literal W, old aging and passive reference remain in the target. No record projection, channel trace or postselection was used to establish (22).

For the finite cut the existing weighted proof applies to this new source as well. Give weight zero to EVERY upstream site, including s0,s1,s2 and the first slow site, and weight m to r_m. All new source terms commute with the weight. Only the internal g receiver edges contribute to the weighted imaginary part; their bound remains 2g sinh(a). The connector also has zero weight increment. Exact compression and the single cut orientation in Duhamel consequently give

    ||embed exp(-itH_M)V-exp(-itH_infinity)V||
       <=min{2,1.2exp[-M+4gT sinh(1)]}, 0<=t<=2T.          (23)

No old source runtime, old finite-device error or whole-H norm is substituted into this argument. The changed source stays inside the zero-weight set and preserves the exact cap at the distant slow cut. Return paths and all internal directions are covered by the full unitary comparison.

At M=50,000,000 and sinh(1)<1.2,

    -M+4gT sinh(1)<-50,000,000+48,000,000=-2,000,000.

Thus (23) is below 1e-8 (already 1.2exp(-20)<1e-8). The infinite normalized target is unchanged by embedding the finite actual state. The exact complete allocations, uniform on [T,2T], are

| Complete-state contribution | Strict ceiling |
|---|---:|
| One actual omitted state, all spectral types | 0.000000000041 |
| Represented all-three-source amplitude | 0.000003 |
| Represented remaining finite/closed background | 0.000505 |
| Raw outgoing plus incoming coefficient errors | 0.0000216 |
| Raw scalar incoming partner | 0.0000691 |
| Ideal physical-halfline normalization | 0.00000000246 |
| Exact finite/infinite transfer | 0.00000001 |
| Sum | 0.000598712501 |

The sum is below .0006 with slack .000001287499. This proves the proposed conditional conclusion (1). The reference truncation eta_ref already appears inside the source line and is not an extra actual omitted vector. There is no uncharged physical target tail at the finite cut.

## 9. Resources, same-metric comparison and limits

The checked three-source installation adds two heads/edges and four unmerged positive blocks to the one-source inventory. At the proposed finite cut:

| Quantity | Exact count |
|---|---:|
| New receiver sites M | 50,000,000 |
| All head qubits M+238 | 50,000,238 |
| All physical qubits M+243 | 50,000,243 |
| Head edges M+239 | 50,000,239 |
| Unmerged positive local blocks 2M+281 | 100,000,281 |

The four old/shared-source qubits and one record are counted once. Passive references are not apparatus qubits. New source incident norm sums are 3j+a2 at s2, 2j+a1+a2 at s1 and 2j+a1 at s0. The previous load at p is unchanged. The receiver is slow, but the old source/contact/internal loads are not bounded by g. Exact correlated coefficients, positivity, diagonal compensations and selective nearest-neighbor installation remain supplied data.

The exact comparison surface supplied by root as PR9679 is `slow_lead_wide_publication/NOTE.md` at the pin below, with its separate publication review. Its certificate is for kappa=1e-8, g=5e-8, h=4e-6, onset 1e15, horizon 2e15, M=250,000,000 and complete normalized-target map ceiling .00191. This composition does not inherit that runtime or its one-source waveform. The candidate changes the source hardware and packet while preserving the same kind of complete-output metric:

| Conditional certificate | Onset T | Window | Receiver M | Complete ceiling |
|---|---:|---|---:|---:|
| Earlier one-source wide receiver | 1e15 | [1e15,2e15] | 250,000,000 | .00191 |
| Present three-source candidate | 2e14 | [2e14,4e14] | 50,000,000 | .0006 |

The candidate onset and new-site count are each smaller by the exact factor 5. Its sufficient ceiling is smaller, but this is not measured error ordering or a claim that the older device cannot work earlier. Each target uses its own exact transmitted waveform. Total-qubit ratio is (250000241)/(50000243), slightly below 5. No optimality, practical speed or physical-seconds identification is established by these Hamiltonian-unit bounds.

If (1) is distinctly supported, record 0 has norm below epsilon=.0006, so a single chosen computational-record read has failure effect below epsilon^2 I=3.6e-7 I and success probability above .99999964. The normalized successful vector is within epsilon+1-sqrt(1-epsilon^2)<.000601 of the ideal vector. The complete-channel and successful SUBNORMALIZED CP-map diamond distances are below 2epsilon=.0012, including passive references and after apparatus trace-out. Conditioned normalization is nonlinear, so no diamond bound for a normalized conditioned channel is claimed.

This is a finite-window receiver result, not autonomous irreversible storage or a stopping-time rule. Native preparation/readout identification, coefficient tolerance/supply, physical unit identification, original calibration and complete matching premises remain conditional. No omitted source subsystem, old-energy phase or hidden measurement is removed from the complete-state metric. No proposed capture, taper or later derivative improvement is imported.

## 10. Exact exposure, dependency status and verification limits

I authored the prepared-core recovery proposal and previously authored or reviewed several related interfaces. Root suggested this single parameter point and specified the component route; the desired conclusion was not taken as evidence. I read the complete source/local/outgoing/traveling/scalar-time/tail/installed-moment arguments and their listed checks, refreshed the loaded-inverse check and the full finite-cut proof/check, and read both new core checks completely. The original nominal phase-map and source/kernel premises were reused at their already inspected unchanged identities. The earlier certificate was read for its comparator, metric, finite cut, counts and published-claim scope; its old temporal theorem is only a comparison surface.

The two core reviews now jointly cover the new dwell/recovery and its downstream background integral. Their scopes remain separate, and the earlier pending wording is historical. This new aggregation, phase enclosure, proof-cutoff arithmetic and finite-point claim still require their own distinct check. All original calibration/scattering/inverse premises remain conditional; neither source hashes nor more checks eliminate those premises.

Exact primary sources and checks relative to this renewal directory:

| Source | SHA256 |
|---|---|
| three_site_actual_attachment/PROPOSAL.md | 4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006 |
| three_site_actual_attachment_check/REVIEW.md | ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d |
| three_site_loaded_inverse/PROPOSAL.md | 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 |
| three_site_loaded_inverse_check/REVIEW.md | 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2 |
| three_site_product_source/PROPOSAL.md | a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823 |
| three_site_product_source_check/REVIEW.md | c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b |
| three_site_local_escape/PROPOSAL.md | 0340895610d3a5ef709dd8a03c1bc5872c8f34cf00f21053c00adcc3d706468d |
| three_site_local_escape_check/REVIEW.md | e19767c8092fb856a3c24cb279f621deea38d69d65c41bef4a1aea44bad23074 |
| three_site_outgoing/PROPOSAL.md | af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac |
| three_site_outgoing_check/REVIEW.md | 721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02 |
| three_site_traveling_interface/PROPOSAL.md | 75b1ba68fae3f34e54c15df80b3a39a165240b1759f8fc84eb2b24677cc7f9e3 |
| three_site_traveling_interface_check/REVIEW.md | 9cb7655b688a61ce32b950f2d95024762023770380a6e5df8afaa1939744230a |
| three_site_reference_time/PROPOSAL.md | d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f |
| three_site_reference_tail/PROPOSAL.md | 92a14fa12ccb489bfe311278683b6aa12b67b6549449273ba181383f5f779fb1 |
| three_site_reference_time_check/REVIEW.md | 0439d990a12b51561257038b1ef14aeb88302adf12bb546de0f00571ac44a553 |
| prepared_core_recovery/PROPOSAL.md | cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9 |
| prepared_core_dwell_check/REVIEW.md | 88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 |
| prepared_core_composition_check/REVIEW.md | 52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c |
| slow_lead_resources/PROPOSAL.md | 84b76d1ec9b1e45811b74ecd2594a0622dfb01ef69d1acadf98931c0ed3f9967 |
| slow_lead_resources_check/REVIEW.md | dd944d8803da24fdfbccfd010e2fd865196aa08ac244605303093a605fef22fe |
| slow_lead_wide_publication/NOTE.md | feec1a7b2d48b758c86d5bdcde4ef0043a3b51ee09fb773024fbd7fd52d5bb38 |
| slow_lead_wide_publication_check/REVIEW.md | af131bc4fa01f5e349a20c547a34490cb95c1c7482a112351e3ebd577cafce76 |
| bandcenter_converter_composition/PROPOSAL.md | 1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78 |
| bandcenter_bandwidth_extension/PROPOSAL.md | d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2 |

The unchanged original canonical endpoint note remains SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`. The background full endpoint is `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3`, with its original qualified scope; the exact row and geometry ancestry are pinned by the outgoing and attachment sources above.

All numerical ceilings here are elementary enclosures of the stated formulas, not propagation data, fitted coefficients or an optimization result. No scientific program, numerical inverse, spectrum, quadrature, dynamics or sweep was executed. File/hash checks were metadata only. No prior source, W, Git, PR, checkpoint, editable prompt, axiom, model or publication state changed. This proposal is the sole new deliverable. The later weighted-reference candidate reported during drafting is not imported. A distinct check should especially test (14)'s actual phase derivative, both scalar cutoff tails and aliases, the raw 2E convention, reference versus actual omissions, the all-three-source term, and application of the exact cut after the source replacement.
