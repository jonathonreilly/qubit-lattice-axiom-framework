# Resonant cutoff Fourier tails on complete half-lines

New bounded author derivation requiring distinct review. For the actual normalized quintic-cutoff source spectrum, this note gives whole-half-line norm bounds with algebraic cost rho h^-2 times gap^-3/2, plus an exponentially small term in the adverse incoming sign case. These estimates concern lead fields, not a complete finite-device theorem. The emitter, internal maps, full-vector initial match, finite budgets and output normalization are separate obligations.

The proof uses the exact real-axis pole representation, the actual cutoff's W^{3,1} regularity and explicit phase inequalities. It does not analytically continue a merely C2 cutoff, infer spatial tails from survival alone, or assume an unproved complex-domain network inverse.

## 1. Source, coefficient and phase conventions

Let 0<rho<=1/2, rho^2<=h<=10^-3 and p=||chi F||_2^2>=1/2. Use exactly

    g(k)=chi(k)F(k)/sqrt(p),
    F(k)=-i sqrt(2/pi)rho exp(ik)
                        /[(2-rho^2)cot k-i rho^2],
    e(k)=E(k)/j=2(1-cos k).                              (1)

The cutoff is1 on |k-pi/2|<=h/2, zero beyond3h/4, and on each width-h/4 transition is 1-10s^3+15s^4-6s^5. It is real, C2 and W^{3,1}, with no distributional atoms through derivative order three. Positive normalization sqrt(p) and every complex source phase are retained. Set

    x=tan(k-pi/2), k(x)=pi/2+atan x,
    A=2-rho^2, b=rho^2/A>0.

The exact identities, including signs, are

    F(k(x))=i sqrt(2/pi)rho exp(ik(x))/[A(x+ib)],
    1/(x+ib)=-i integral_0^infinity exp(ixv-bv)dv,
    conjugate(F(k(x)))=-i sqrt(2/pi)rho exp(-ik(x))/[A(x-ib)],
    1/(x-ib)= i integral_0^infinity exp(-ixv-bv)dv.      (2)

Thus F adds +vx to the real phase, whereas conjugate(F) adds -vx. This distinction cannot be dropped when estimating incoming fields.

Let M(k) be an operator from the arbitrary supplied logical/reference input fiber to a finite port/record fiber, with uniform derivatives ||M^(s)||<=M_s, s=0,...,3. References are tensored by identity; no norm constant depends on their dimension. The scalar case is M=1, with (M0,M1,M2,M3)=(1,0,0,0). All statements below apply in operator norm to the synthesized sequence.

For both signs of exp(ik), define nonnegative four-entry coefficient ceilings using (u star v)_s=sum_l binomial(s,l)u_l v_(s-l):

    C=(1,1,2,5) star (1,1,3,10)
                   star (M0,M1,M2+M1,M3+3M2+3M1),
    D0=2C0,
    D1=20C0+2C1,
    D2=300C0+40C1+2C2,
    D3=4000C0+900C1+60C2+2C3.                            (3)

These D_s are numerical amplitude bounds, not physical mediator energies. If a(x)=chi(k(x))exp(+-ik(x))k'(x)M(k(x)), then

    ||a^(s)||_1<=D_s/h^2, s=0,1,2,3.                  (4)

For completeness, k'>=.999, |k''|<=.002, |k'''|<=3 and |k''''|<=.1 on this support. The cutoff x-derivative L1 bounds are (2h,20,300/h,4000/h^2). In k coordinates the derivative sup bounds are8/h,100/h^2,3840/h^3, with total transition width h/2. Its third L1 bound is therefore1920/h^2 before the harmless atan chain/Jacobian factors. Applying Leibniz gives respectively 2h C0;20C0+2h C1;300C0/h+40C1+2h C2;4000C0/h^2+900C1/h+60C2+2h C3. Since h<=1, (3),(4) follow. Compact support and continuous first two derivatives justify all three integrations by parts below. Arbitrary C2 cutoffs without this weak third derivative are not included.

## 2. Two explicit integration constants

For positive a and nonnegative B2,B3,B4, define

    P(D;a,B)=D3/a^3+6B2 D2/a^4
       +(4B3/a^4+15B2^2/a^5)D1
       +(B4/a^4+10B2 B3/a^5+15B2^3/a^6)D0,

    Q(D;a,B)=D3/(2a^2)+2B2 D2/a^3
       +(4B3/(3a^3)+15B2^2/(4a^4))D1
       +(B4/(3a^3)+10B2 B3/(4a^4)+3B2^3/a^5)D0.       (5)

They are explicit arithmetic expressions. If a real phase has |phase'|>=a N and derivatives of orders2,3,4 bounded by B2 N,B3 N,B4 N, three integrations by parts bound its integral against a(x) by P/(h^2 N^3). The seven absolute coefficient terms are a'''/p^3,6a''p'/p^4,4a'p''/p^4,15a'(p')^2/p^5,a p'''/p^4,10a p'p''/p^5,15a(p')^3/p^6, where p=phase'. Their signs do not matter for this norm estimate.

If instead |phase'|>=a N+v and the higher derivatives have those same bounds independent of v, integrating that estimate over v>=0 gives Q/(h^2 N^2). This follows term by term from integral_0^infinity(a N+v)^(-m)dv=(a N)^(1-m)/(m-1). It is valid for either sign of phase' as long as adding the auxiliary term increases its absolute value. All integrals are Bochner integrals of finite-dimensional operators, or their tensor products with passive identities.

In the pole synthesis the common prefactor, including the Fourier 1/sqrt(2pi), is rho/(pi A sqrt(p))<=rho. Thus (5) is directly usable without an omitted Fourier or normalization factor. Fubini before integration by parts is justified for each b>0 by the finite bound ||a||_1/b. The uniform small-rho result is obtained afterward, not by assuming uniform absolute integrability of that original representation.

## 3. Adverse sign: F with an incoming phase

For dimensionless u>=1, define the complete n>=0 sequence

    Z_n(u)=(2pi)^(-1/2) integral
                        exp(-ink-iu e(k))M(k)g(k)dk.    (6)

Take a0=.23 and (B2,B3,B4)=(4,32,128), and let P0=P(D;a0,B). Then

    ||Z(u)||_(ell2(n>=0))
       <=rho P0/(h^2 u^(3/2))
                           +2M0 sqrt(h)/rho exp(-b u/2). (7)

Here is the complete low/high proof. In (2), split the auxiliary integral into 0<=v<=u/2 and v>=u/2. On the low range put N=n+u. The x-phase derivative equals [-n-2u sin k]k'+v. Since sin k>.99 and k'>=.999, it is at most -.999n-1.478u, hence negative with magnitude greater than a0 N. In k coordinates the original first derivative is bounded by2N and all derivatives of orders2 through4 by2N. The atan chain gives bounds4N,32N,128N on its higher x derivatives; the added vx has none. Applying P0 and integrating the low v range of length u/2, dropping exp(-bv)<=1, yields

    ||Z_n,low||<=rho u P0/[2h^2(n+u)^3].               (8)

Summing the squared ceilings uses

    sum_(n>=0)(n+u)^(-6)<=u^-6+u^-5/5
                                      <=6/(5u^5).

The resulting low-frequency sequence norm is below the first term in (7). This pays n=0 as well as the whole infinite half-line; it is not a pointwise-to-norm guess.

For the high range work in the ORIGINAL k variable before estimating any individual n. At each v the factor exp(iv tan(k-pi/2)-iu e(k)) has modulus1. Full-integer Fourier Parseval and ||chi||_2<=sqrt(2h) give sequence norm at most M0 sqrt(2h) for the coefficient chi exp(ik)M, independently of u,v. Minkowski and projection onto n>=0 are contractions, so the high part is at most

    [sqrt(2/pi)rho/(A sqrt(p))] M0 sqrt(2h)
                                integral_(u/2)^infinity exp(-bv)dv
       <=2M0 sqrt(h)/rho exp(-b u/2).                   (9)

The cancellation A b=rho^2 is used exactly. This proves (7). The high part is paid as a coherent vector norm; no independent probabilities are added. Equation (7) need not be useful before rho^2 u is large. It is a sufficient envelope, not a statement that this exponential is the exact tail.

## 4. Favorable incoming sign: the actual conjugate term

Define

    Zbar_n(u)=(2pi)^(-1/2) integral
                     exp(-ink-iu e(k))M(k)conjugate(g(k))dk.

The cutoff is real, so conjugate(g)=chi conjugate(F)/sqrt(p). The auxiliary phase is now [-nk-ue(k)]-vx. Its derivative has negative magnitude at least a0(n+u)+v for every v>=0. The same higher derivative ceilings apply. Let Q0=Q(D;a0,(4,32,128)). Integrating v with (5) gives

    ||Zbar_n(u)||<=rho Q0/[h^2(n+u)^2],
    ||Zbar(u)||_(ell2(n>=0))<=2rho Q0/(h^2 u^(3/2)).    (10)

The sum bound is sum_(n>=0)(n+u)^(-4)<=u^-4+u^-3/3<=4/(3u^3). No high-frequency exponential remainder is needed because the signs remain favorable throughout the auxiliary integral. The actual standalone incoming term I_t conjugate(g) has precisely this sign for u=jt. It must not be replaced by (6) merely because |F|=|conjugate(F)|.

## 5. Favorable outgoing half-line with biased momentum

Let k_a=k or q(k)=acos(cos k+r/2), 0<=r<=10^-3, and take R,L,u>=0. The outgoing sequence starting at physical radius R is

    Y_n=(2pi)^(-1/2) integral exp(i[(n+R)k_a(k)+Lk-u e(k)])
                                             M(k)g(k)dk,
    n>=0.                                               (11)

Require a proved gap and a bounded phase ratio:

    Qgap=.99R+L-2u>=1,
    R+L+u<=Cgap Qgap, Cgap>=1.                          (12)

Set a0=.23 and B=(4Cgap,32Cgap,128Cgap), and Qout=Q(D;a0,B). Then

    ||Y_n||<=rho Qout/[h^2(n+Qgap)^2],
    ||Y||_(ell2(n>=0))<=2rho Qout/(h^2 Qgap^(3/2)).      (13)

To verify the phase hypotheses, the packet gives .99<=q'<=100/99, |q''|<.003 and |q'''|<3. A fourth derivative follows directly from cos q=cos k+r/2:

    sin q q''''=-cos k+cos q(q')^4+6sin q(q')^2q''
                              -3cos q(q'')^2-4cos q q'q'''.

Using sin q>.99, |cos q|<=.0015 and |cos k|<=.001 bounds |q''''|<.04; the loose bound10 suffices. In k coordinates the first derivative is at least .99n+Qgap. Its absolute upper bound is 2Cgap(n+Qgap); orders2,3,4 are bounded by respectively2Cgap,3Cgap,10Cgap times n+Qgap. Atan chain differentiation therefore supplies (5) with the B in (13), while its first derivative is at least .98(n+Qgap). The +vx contribution from F strengthens this positive derivative. Integrate v, then sum the fourth-power sequence as in (10). This establishes the whole-half-line operator bound, including n=0.

Examples of valid domains, not new finite theorems: for ell>=1000, L=ell+57, the early outgoing half-line R=0 and 0<=u<=ell/100 satisfy (12) with Cgap=2 and Qgap>=.98ell. The far-positive half-line R=ell+1 and 0<=u<=7ell/8 satisfies it with Cgap=16 and Qgap>=.24ell. Thus (13) covers these two actual types of packet tails with explicit constant choices. The outgoing negative-radius tail at late times is a different sign/geometry and is not covered automatically by these examples.

For the actual ordinary outgoing packet coefficient take

    M_a=P_a J^-1/2 exp(-57ik) S(k) sqrt(sin k)V_0.

This is exactly the demodulated map of cf080. It includes both record-dependent velocity conversions; its derivative ceilings through order three are supplied by outgoing-pole proposal b262, which is a provisional dependency pending its separate check. This note does not duplicate or independently validate those full network inverse calculations. If separate record bounds are used, their orthogonal sum costs at most sqrt(2) times a common ceiling, or the conservative factor2. Port/path/reference dimensions do not supply extra factors.

For the ideal inelastic scalar profile use M=sqrt(q'), including its Jacobian, rather than M=1. The explicit derivative ceilings (2,1,10,100) suffice: differentiating sqrt(q') three times uses q'',q''',q'''' and the real lower bound q'>=.99 just proved. For example its second derivative is q'''/(2sqrt(q'))-(q'')^2/(4(q')^(3/2)); its third is q''''/(2sqrt(q'))-3q''q'''/(4(q')^(3/2))+3(q'')^3/(8(q')^(5/2)). No variable change in the half-line estimate drops this amplitude. Parseval in (9) is only applied to the k-Fourier incoming sequence; it is not an assertion that q-Fourier coefficients have the k measure.

## 6. Exact interfaces and limits of substitution

For scalar M=1, (7) is a candidate replacement for an incoming right-projection tail whose exact phase is -nk-iu e(k), and (10) bounds the normalized cutoff's conjugate physical incoming term. Equation (13) is a replacement for explicitly verified positive outgoing gaps satisfying (12). Translations or reversed source coordinates must be checked against these exact signs and offsets before application. Noninteger R is harmless analytically, but the physical examples use integer radii.

All norms retain the entire n>=0 sequence, all specified ports/record sectors, and arbitrary passive references. They are not probabilities and are not normalized success branches. The comparison fields themselves need not have norm one after half-line restriction. The normalized g remains the actual source-derived envelope, not a separately supplied packet. Spectral omission outside chi, emitter survival, and the difference between a true seeded state and its packet representation remain separate costs.

The new algebraic terms can be smaller than a rho^-1/sqrt(u) estimate in a suitable joint regime, but they include explicit h^-2 and large derivative constants. The adverse-sign term also requires controlling rho^-1 sqrt(h) exp[-rho^2 u/(2(2-rho^2))]. No universal improvement at every time, no complete finite family, and no runtime exponent is claimed. Incoming finite boundary integrals are another interface and are being treated separately; none is imported here.

## 7. Sources, exposure and required check

Paths are under N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- common_product_outgoing_pole_tail/PROPOSAL.md: b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80. Authored, fully read and frozen immediately before this task; its third network derivatives remain provisional here. The present scalar/abstract coefficient lemmas have complete proofs above and do not require that matrix substitution.
- common_product_biased_record_packet/PROPOSAL.md: cf080f0dae5bf71021fe91533fc97355ceaaadb5db6f3d3145e3a911c8f3ffcf, fully reread/hash verified in that preceding task. Its real q bounds, exact ordinary amplitudes and common phase are reused at their checked scope; prior distinct check315a618f389598fe8443a8ed3cdf8c39180b65ba223c4de2a359be4e218ea916 was fully read in the earlier preparation task.
- common_product_biased_record_finite_seed/PROPOSAL.md:532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123, fully reread/hash verified in the preceding task. Only its actual cutoff and examples of tail geometry inform the interfaces; no frozen budget is edited or declared improved.
- common_product_endpoint_launch/PROPOSAL.md:fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4 and common_product_launch_derivative_bounds/PROPOSAL.md:378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8. Complete exact source arguments were read in the preceding geometric task and reused unchanged. The critical sign identities are reconstructed in (2).

ROOT suggested the low/high auxiliary-frequency split and favorable-sign half-line route. This author reconstructed signs, norm measures, cutoff derivatives, phase conditions and sums above. This is source/design-exposed same-model author work, not independent checking. Required distinct checks include (7)'s high-v Parseval normalization, all sign choices, the weak derivative integrations, coefficient-to-sequence bounds, biased Jacobian and the actual network third-derivative dependency before any finite transfer.

Only this file was created. No scientific executable, simulation/sweep, delegation, source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. No physical preparation/readout/capture mechanism, old processor theorem, native realization or permanent halt is inferred.
