# Quantitative halfline concentration of the three-site scalar comparator

Status: new conditional analytic derivation, requiring a distinct check. This concerns precisely the normalized scalar outgoing coefficient of `three_site_outgoing/PROPOSAL.md`, not escape from the installed source/core. No operating point is selected. Root suggested testing a cubic impulse comparison; the comparison below includes its lattice alias, dispersion, cutoff and physical phase errors.

## Packet and domain

Retain the full domain and physical root/phase definitions of the outgoing source, including lambda/j<=1/16, d/g<=1/2 and its exact positive transmitted mass p. The source conditioning Theta<1 is needed for its actual outgoing comparison, but not for the scalar estimates here. Set

    C=sqrt(8 lambda^5/(3pi)), theta=k-pi/2, x=2g theta,
    delta(x)=2g sin(x/(2g)),
    phi(x)=61.5 q(delta(x))+.5 k(delta(x))+172 k_old(q(delta(x))),
    phi0=phi(0), eta=lambda/j.

The constant phase zeta is retained. The exact subnormalized coefficient on the physical selected interval is

    F(k)=zeta exp(i phi(x)) sqrt(2g) C
                 sqrt(sin q sin k) |t_f| / q3(delta(x)),             (1)

and zero elsewhere in a full 2pi Fourier cell. Thus integral |F|^2 dk=p. This is exactly F_s3, not a newly fitted packet; the phase of q3 is still present. The physical output starts at m=0. Define

    a_m(t)=(2pi)^(-1/2) integral F(k)/sqrt(p)
                            exp(ikm-it delta(k)) dk.                (2)

The common carrier exp[-it(c_att+2j)] and old factor exp(-itK)W multiply (2) as in the source; they do not affect the following scalar norms. No time-dependent phase choice is made.

Choose any auxiliary cutoff 0<D<=d. This is a proof parameter, not hardware. Put

    delta_D=2g sin(D/(2g)), v=D^3/(24g^2 lambda),
    r=3eta+3v(1+v)^2,
    A=D^2/(4j^2)+5D^2/(4g^2),
    Phi=max_{|x|<=D}|phi(x)-phi0|,
    Ecent=(A+Phi+r)/(1-r),                         assume r<1.

Phi is the supremum of the displayed exact, continuously unwrapped physical phase on this compact interval. It is an explicit scalar function of the supplied source dispersion, not an adjustable phase. If an elementary numerical ceiling is desired it suffices to use D times the supremum of the derivative of that same phase. No derivative of the resonant q3 is included in Phi.

Let mu6=3lambda^6+(8/3)jlambda^5 and define

    U=sqrt(min{1,lambda^2/(3delta_D^2),mu6/delta_D^6}),
    V=sqrt(16/(15pi)) (lambda/D)^(5/2),
    Z=(8/3)sqrt(16/(15pi)) (lambda/(2pi g))^(5/2),
    E(t)=Ecent+|t|D^3/(24g^2)+U+V+Z+1-sqrt(p).                  (3)

All quantities are finite for positive parameters and D. One may bound 1-sqrt(p) using Xi in the outgoing source when Xi<1. Keeping exact p is always valid. These estimates are sufficient and deliberately conservative; large E gives no useful conclusion.

## Exact amplitude comparison

On |x|<=D, |x-delta(x)|<=D^3/(24g^2). The checked finite-band determinant estimate gives

    |q3(delta)-(delta+i lambda)^3|<=3eta |delta+i lambda|^3.

Since |delta|<=|x|, expanding the difference of cubes shows

    |q3(delta)-(x+i lambda)^3|/|x+i lambda|^3<=r.

The chosen cube bound 3v(1+v)^2 is conservative. Hence division by q3 costs at most 1/(1-r); it never replaces the physical denominator by its modulus. Also 0<=sqrt(sin q sin k)|t_f|<=1. The inequalities 1-sin q<=delta^2/(4j^2), 1-sin k<=delta^2/(4g^2), and 1-|t_f|<=|r_L|^2<=delta^2/g^2 imply its distance from one is at most A. Combining these estimates and |exp(i(phi-phi0))-1|<=Phi gives central L2 error at most Ecent relative to

    F_M(k)=zeta exp(i phi0) sqrt(2g) C/(x+i lambda)^3.           (4)

The full real-x Markov density C^2/(x^2+lambda^2)^3 has mass one, so central integration introduces no further constant. Replacing exp(-it delta) by exp(-it x) in (4) costs at most |t|D^3/(24g^2).

The actual raw packet outside |x|<=D has norm at most U: the exact change of variables gives the scalar finite-band density, flux is contractive, and outside this interval |delta|>=delta_D. The exact scalar second and sixth moments yield U. The full real-x comparison outside |x|<=D has norm at most V, by integrating C^2/x^6 over both tails. This pays the reference cutoff as well as the actual cutoff; neither is discarded.

## Lattice periodization and the exponential bound

A continuum Fourier impulse is not itself a lattice state. To connect it rigorously, periodize the function in (4), including exp(-it x), with x-period 4pi g. On the central Fourier cell the L2 norm of all noncentral translates is at most Z, uniformly in t. Indeed translate ell>=1 lies at |x|>=(4ell-2)pi g; each translated norm is bounded by the full two-sided tail estimate at this threshold. Triangle inequality and

    sum_{ell>=1}(2ell-1)^(-5/2)<=1+integral_1^infinity(2s-1)^(-5/2)ds=4/3

prove the displayed Z. The integrable amplitude tails justify termwise Fourier integration. Thus the periodized comparator's Fourier coefficients are exactly the continuum samples, with no assumption of continuous position or omitted alias terms.

For s=t-m/(2g), residue evaluation gives these coefficients as

    b_m(t)=zeta exp(i phi0) exp(i pi m/2)
             i C sqrt(pi)/(2sqrt(g)) s^2 exp(-lambda s) 1_{s>=0}. (5)

The third-order lower pole and the convention exp(-ixs) fix both support and phase. Formula (5) is a comparison, not the exact physical propagator. Combining the preceding central and tail estimates and then paying the exact normalization cost ||F/sqrt(p)-F||=1-sqrt(p) gives

    ||a(t)-b(t)||_{ell2(Z)}<=E(t).                             (6)

In particular (6) does not incorrectly assume that the sampled comparator has norm one; its possible norm discrepancy is already covered by the periodization comparison.

For t>=2/lambda, s^4 exp(-2lambda s) decreases for s>=t. Sum-integral comparison for m<=0 in (5), with z=lambda t, yields

    ||1_{m<=0}b(t)||^2 <= H(z)^2,
    H(z)^2=exp(-2z)[(2lambda/(3g))z^4
                         +(2/3)z^4+(4/3)z^3+2z^2+2z+1].       (7)

Indeed the exact sum is (2lambda^5/(3g)) sum_{n>=0}
(t+n/(2g))^4 exp[-2lambda(t+n/(2g))]. Its first summand plus 2g times the integral gives (7). Consequently

    ||1_{m<=0}a(t)||<=min{1,H(lambda t)+E(t)}=:epsilon_left(t). (8)

The stronger excluded set m<=0 is used deliberately; the actual physical complement m<0 is contained in it. Since a(t) has exact full-line norm one,

    ||1_{m>=0}a(t)||>=sqrt(1-epsilon_left(t)^2).               (9)

If epsilon_left<1, normalizing this physical restriction costs at most
1-sqrt(1-epsilon_left^2) in norm. This is a scalar reference statement only. It supplies quantitative finite-time halfline normalization and can be made uniform on a finite interval by taking the supremum of the right-hand side of (8). The dispersion term grows with |t|, so this particular comparison is not a uniform all-late-time bound or a permanent-halt statement.

## Incoming partner and its precise limitation

For the conjugate-coefficient scalar partner define

    a_in,m(t)=(2pi)^(-1/2) integral conjugate(F(k))/sqrt(p)
                                      exp(-ikm-it delta(k)) dk.

Apply exactly the same central/tail/alias proof to the conjugate rational amplitude. Its pole is now upper, and its continuum sample is supported on t+m/(2g)<=0. Therefore for t>0 and m>=0 its comparison vanishes identically, giving

    ||1_{m>=0}a_in(t)||<=min{1,E(t)}.                         (10)

This is a bound for the explicitly defined scalar conjugate partner, with the conjugated physical phase retained. It becomes an incoming reference bound in a physical Stone decomposition only where that decomposition actually identifies its incoming coefficient with this partner. An arbitrary loaded operator-valued incoming row is not proved to have that coefficient here. In particular (10) cannot replace an actual source/core or incoming-row derivation. The outgoing halfline conclusion (8) requires no such identification.

## Exposure, pins and open checks

I authored the scalar source and separately checked the outgoing synthesis; this new time derivation is author work, not an independent check. Root supplied the suggestion to exploit the cubic impulse and mentioned a heuristic parameter regime; no such numerical operating point is assumed or evaluated here. Required exact sources are:

- `three_site_outgoing/PROPOSAL.md`: af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac.
- Its distinct synthesis review `three_site_outgoing_check/REVIEW.md`: 721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02 (my prior check; shared exposure disclosed).
- `three_site_product_source/PROPOSAL.md`: a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823; distinct scalar review c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b.

The actual physical phase and converter ancestry are precisely those of the outgoing source, whose emitter-free row is not rederived here. The proof does not use an installed source escape assertion, prepared omitted-state estimate, or actual outgoing error as a scalar normalization premise. A distinct check should test particularly the residue normalization, periodization tail, source/slow Jacobian, cutoff mapping and distinction between the conjugate reference and actual incoming rows. No scientific run, sweep, numerical optimization, Git/canonical/PR/checkpoint/prompt/model edit or delegation occurred. Supplied coefficients, correlations, preparation and native physical identification remain premises of any later device composition.
