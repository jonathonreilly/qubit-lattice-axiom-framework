# Same-offset nominal scalar packet: shifted-carrier halfline bounds

Status: new conditional author derivation requiring distinct checking. This gives explicit scalar functional bounds with the actual same-Delta hard-band coefficient. It selects no hardware/time point and supplies no actual complete-device performance. The shifted quadratic dispersion term is retained; the bandcenter time theorem is not transferred.

## Physical coefficient and restricted domain

Retain the calibrated j,J, original energy map and physical domain of the checked common-mode actual interface: 0<lambda<=1e-8, .0027<j<.003, 0<g<=1e-6, 0<h<=4e-6, d=2j sin h, d/g<=1/2. Fix a supplied |Delta|<d. Only the NOMINAL source at that Delta is treated: a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa^2=3jlambda; residual errors are zero. Its exact determinant is

    q_Delta(delta)=[(delta-Delta)^2-lambda^2/3]
       [delta-Delta-3jlambda m_j(delta+i0)]
                  -(8lambda^2/3)(delta-Delta).

The physical load is m_j(delta). Put beta=3(lambda+|Delta|)/j<1. The checked scalar theorem supplies no hidden mass and |q_Delta|>=(1-beta)[(delta-Delta)^2+lambda^2]^(3/2) on the physical j band.

Let

    kD=acos(-Delta/(2g)), v=2g sin(kD), x=v(k-kD),
    delta(k)=-2g cos k,
    y(x)=delta(k)-Delta= v sin(x/v)+Delta[cos(x/v)-1],
    q(k)=pi/2+asin(delta(k)/(2j)),
    k_old(q)=2asin(sqrt(j/J)sin(q/2)),
    phi(k)=61.5q(k)+.5k+172k_old(q(k)), phiD=phi(kD),
    C=sqrt(8lambda^5/(3pi)).

All physical roots are those of the original calibrated band. On |delta(k)|<=d, 0<k<pi, the EXACT raw coefficient is

    F(k)=zeta exp(i phi(k)) C sqrt(2g sin k)
                           sqrt(sin q(k)) |t_f(k)|/q_Delta(delta(k)),
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2).

It vanishes outside that hard band. This is the checked transmitted coefficient with the nominal shifted determinant; the phase of t_f is already included in phi and is not multiplied in again. Its norm squared is p in (0,1]. Preserve the first slow coordinate m=0, distinct from the gate port. Use the length-2pi Fourier cell k in [kD-pi,kD+pi]; the physical hard band lies in it.

Choose an auxiliary proof cutoff 0<D<=g/4 with |Delta|+2D<d. This changes no physical band. Such a D exists whenever |Delta|<d. Define

    etaD=|Delta|D/(2v^2)+D^2/(6v^2), alphaD=1-etaD,
    omegaD=|Delta|D/v^2+D^2/(2v^2),
    mD=(1-beta)alphaD^3,
    bD=alphaD D,
    mu6=3lambda^6+(8/3)jlambda^5.

Since |Delta|/g<1/2, v>=sqrt(15)g/2. With D<=g/4, etaD<=7/360<.02 and omegaD<=1/24<.042. Thus alphaD,mD,bD are strictly positive. On |x|<=D, |y-x|<=etaD |x| and |delta|<=|Delta|+(1+etaD)D<d. All phase and background reference-plane formulas therefore stay on the original calibrated domain, without extending actual device analyticity.

## Explicit error functional

A valid physical phase derivative ceiling on the central interval is

    P=1/(2v)+(1+omegaD)*102.78/(2j cos h).

It uses the already checked k_old'(q)<.24 on the original band. Define the following nonnegative terms:

    J2=Delta^2+2|Delta|(1+etaD)lambda/sqrt(3)
                                  +(1+etaD)^2 lambda^2,
    Nerr=|Delta|lambda/(sqrt(3)v^2)+lambda^2/(2v^2)
             +sqrt(1+omegaD)*(1/(4j^2)+1/g^2)*J2,
    Qerr=beta(1+etaD)^3
          +3(1+etaD)^2[|Delta|lambda/(2sqrt(3)v^2)
                                            +lambda^2/(6v^2)],
    Ecentral=(Nerr+P lambda/sqrt(3)+Qerr)/mD,
    Edisp(t)=|t|[|Delta|lambda^2/(2v^2)
                         +sqrt(16lambda^5 D/(3pi))/(6v^2)],
    U=min{1,lambda/(sqrt(3)bD),sqrt(mu6)/bD^3,
               sqrt(16/(15pi))/(1-beta)*(lambda/bD)^(5/2)},
    V=sqrt(16/(15pi))*(lambda/D)^(5/2),
    Z=(8/3)*sqrt(16/(3pi))*(lambda/(pi v))^(5/2),
    E(t)=Ecentral+Edisp(t)+U+V+Z+1-sqrt(p).             (1)

These conservative bounds need not be small. Exact p may be used without any additional estimate. A useful optional certified lower bound is obtained from

    1-p <= mu6/(d-|Delta|)^6
                         +(Delta^2+lambda^2/3)/g^2,    (2)

capped above by one. It uses the nominal scalar shifted sixth moment for band exclusion and the checked real scalar-interface reflection bound |r|^2<=delta^2/g^2 on the retained physical band. A nonpositive resulting lower bound does not mean p=0; the exact nonempty-band mass is positive.

Define normalized physical sequences on all integers by

    a_m(t)=1/sqrt(2pi) integral F(k)/sqrt(p)
                              exp[ikm-it(2j+delta(k))] dk,
    a_in,m(t)=1/sqrt(2pi) integral conjugate(F(k))/sqrt(p)
                              exp[-ikm-it(2j+delta(k))] dk.

They each have full lattice norm one. For every real t, the outgoing cubic comparison is

    b_m(t)=zeta exp(i phiD) exp(i kD m) exp[-it(2j+Delta)]
          *i C sqrt(pi/(2v)) [t-m/v]^2
            exp[-lambda(t-m/v)] 1_{t-m/v>=0},

and satisfies

    ||a(t)-b(t)||_ell2 <= E(t).                         (3)

The comparator need not have lattice norm one. For z=lambda t and t>=2/lambda, put

    H_v(z)^2=exp(-2z)[(4lambda/(3v))z^4
                     +(2/3)z^4+(4/3)z^3+2z^2+2z+1].

Then explicit halfline functionals are

    C_out(t)=min{1,H_v(lambda t)+E(t)},
    ||1_{m<=0}a(t)||<=C_out(t),
    ||1_{m>=0}a(t)||>=sqrt(1-C_out(t)^2),              (4)

and, for t>0,

    J_in(t)=min{1,E(t)},
    ||1_{m>=0}a_in(t)||<=J_in(t).                     (5)

The actual outgoing complement is m<0; (4) conservatively also includes m=0. The incoming bound also includes m=0. Taking suprema gives a finite-interval bound; the growing dispersion term prevents an all-late-time conclusion from this estimate.

## Weighted central comparison proof

Write R_x=sqrt(x^2+lambda^2). Taylor inequalities on real x give

    |y-x|<=|Delta|x^2/(2v^2)+|x|^3/(6v^2).

Thus alphaD|x|<=|y|<=(1+etaD)|x|, and the checked physical scalar margin yields |q_Delta|>=mD R_x^3. No smallness condition on D^2/(v lambda) is needed. Factoring the cubic difference gives

    |q_Delta(delta)/(x+i lambda)^3-1|
       <=beta(1+etaD)^3
           +3(1+etaD)^2[|Delta||x|/(2v^2)+x^2/(6v^2)].

Only the shifted scalar theorem is used; this is not an actual operator strip or resonance claim.

The physical velocity is vphys=2g sin k=v cos(x/v)-Delta sin(x/v). Hence

    |vphys/v-1|<=|Delta||x|/v^2+x^2/(2v^2)<=omegaD.

Relative to the constant-velocity cubic coefficient sqrt(v)C/(x+i lambda)^3, the real numerator is N=sqrt(vphys/v)sqrt(sin q)|t_f|. The checked reflection estimate implies 1-|t_f|<=delta^2/g^2, while 1-sqrt(sin q)<=delta^2/(4j^2). Therefore

    |N-1|<=|Delta||x|/v^2+x^2/(2v^2)
                 +sqrt(1+omegaD)delta^2[1/(4j^2)+1/g^2].

Here sqrt(vphys/v) is not silently replaced by one, and the physical phase and denominator remain exact. The phase derivative satisfies |dphi/dx|<=P because dq/dx=(vphys/v)/(2j sin q), dk/dx=1/v and k_old'<.24.

The normalized cubic density C^2/R_x^6 has moments int x^2 rho=lambda^2/3 and int x^4 rho=lambda^4. Since |delta|<=|Delta|+(1+etaD)|x|, Minkowski gives ||delta^2||_L2(rho,central)<=J2. The weighted numerator, phase and denominator differences consequently have L2 ceilings Nerr, P lambda/sqrt(3) and Qerr. Dividing by the lower ratio mD proves Ecentral. In particular the phase is a fixed physical phase, not a fitted per-time shift.

After comparing central coefficients, compare the linear time factor to the exact one. The quadratic displacement uses the finite fourth moment; the cubic displacement uses only

    integral_-D^D x^6 rho(x) dx <=2D C^2.

This gives Edisp(t) in (1). The full cubic sixth moment diverges and is not used. The common carrier exp[-it(2j+Delta)] remains on both sides.

## Tails, periodization and integer sampling

On the physical k band delta is strictly increasing. Outside |x|<=D, |delta-Delta|>=bD; thus scalar centered second/sixth moments give the first moment-based U ceilings. Also the nominal density is bounded by C^2/[(1-beta)^2(y^2+lambda^2)^3]. Integrating its two tails gives the last U ceiling. Transmission can only reduce those raw masses. The full rational tail outside |x|<=D has norm <=V.

Periodize the full linear-time cubic coefficient in x with period 2pi v, corresponding to a 2pi k cell centered at kD. The central cell has |x|<=pi v. For nonzero alias index n, |x+2pi v n|>=(2|n|-1)pi v. Each alias L2 norm is bounded by C sqrt(2pi v)/[(2|n|-1)^3(pi v)^3]. The both-sign sum obeys 2sum_(n>=1)(2n-1)^-3<=8/3 (a simple integral bound even gives 5/2). This yields exactly Z in (1). Time factors have unit modulus, so this bound is uniform in t. It deliberately uses a conservative full-cell supremum and does not import the previous centered alias constant.

Fourier coefficients of this periodization equal the full-line integral. Closing the lower pole at -i lambda gives the displayed b_m: the factor is i C sqrt(pi/(2v)), the delay is t-m/v, and the carrier is exp(i kD m)exp[-it(2j+Delta)]. Combining central, dispersion, physical/rational tails and aliases proves the raw version of (3). Normalizing the exact physical coefficient costs exactly 1-sqrt(p), proving (3).

For outgoing m<=0 and t>=2/lambda, s^4 exp(-2lambda s) is decreasing for s>=t. Since |b_m|^2=(4lambda^5/(3v))(t-m/v)^4 exp[-2lambda(t-m/v)], the sum-integral estimate with spacing 1/v gives H_v^2. No assumption that the sampled comparator has norm one is involved.

For the incoming comparison, conjugate the fixed coefficient and its phase but retain physical exp(-itE). Its cubic pole is upper and its Fourier sample is supported on t+m/v<=0. It therefore vanishes for t>0,m>=0. The same central errors, tails and aliases prove (5). No arbitrary input/reference vector is conjugated. In a later actual traveling use this is the scalar partner of W*, not W and not time-reversed actual evolution.

## Raw physical normalization interface and open obligations

Let beta_Delta,0 and alpha_Delta,0 be the raw physical packets. The above bounds imply

    ||alpha_Delta,0(t)||_(m>=0)<=sqrt(p) J_in(t),
    r(t)=||beta_Delta,0(t)||_(m>=0)
                              >=sqrt(p)*sqrt(1-C_out(t)^2).

When the latter lower bound is positive the physical normalized outgoing target is well defined; more generally exact r>0 suffices. One may use

    1-r(t)<=1-sqrt(p)+C_out(t)^2.

This is the single target-normalization cost in the checked actual traveling synthesis. The normalization within the scalar comparison is used to estimate these functions; it is not a second actual-state normalization or a new actual omitted mass. That synthesis still separately pays its two actual coefficient discrepancies, two same-Delta residual packet replacements, represented source/background and one actual outside state.

This proposal gives no numerical operating point, no smallness assertion for the full parameter domain and no all-late-time estimate. Large Delta relative to lambda is allowed in the derivation but affects physical reflection, phase, load margin and curvature explicitly. Near |Delta|=d the admissible proof cutoff shrinks and the tail bound can deteriorate. Actual-source analyticity, actual escape rates, finite output performance, unknown-offset zero-target robustness, permanent storage and native suppliers are not established.

## Exact sources and exposure

- `three_site_common_mode_source/PROPOSAL.md`: `5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb`.
- `three_site_common_mode_source_check/REVIEW.md`: `af2e768b78e337f1f11d982ea83fdb1d6270f6b646ccb0895b79fd6613d44ffb`.
- `three_site_common_mode_actual_interface/PROPOSAL.md`: `9225b6ea6533dea56db4f8b7157deac5c6f52e5927b554052c59299622a13957`.
- `three_site_common_mode_traveling/PROPOSAL.md`: `0abafe7b46fe6c93df110df8bc1e7a9dbc3a4eca30d38dbdea619337ca75940d`.
- `three_site_common_mode_traveling_check/REVIEW.md`: `4ac2571d63c5c6b4e7d7ea4e490a224b1e3d9d0a34b7ca4d82bce7fcc5038bdd`.
- `three_site_weighted_reference_time/PROPOSAL.md`: `d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36`.
- `three_site_weighted_reference_time_check/REVIEW.md`: `809c0e0b452b4d913d5750f3aa184473c4d4b20132de7a73b919e8d0be5415ac`.
- `three_site_outgoing/PROPOSAL.md`: `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac`.
- `three_site_outgoing_check/REVIEW.md`: `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02`.
- `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.

I authored the centered weighted reference and related traveling/attachment ancestors and checked the common-mode scalar, actual and traveling sources. Root suggested the shifted-carrier route, not its validity. The centered weighted source was refreshed in full; unchanged coefficient/mapping and scalar premises are reused at their exact checked scope. The changed velocity, quadratic curvature, denominator margin, alias period and sampling residue are derived here, not claimed to inherit an independent check. This proposal requires a distinct check before scientific composition. No numerical integration, dynamics, spectrum, sweep, scientific runner, Git/PR/checkpoint/prompt/model change or delegation occurred. Only this proposal was written.
