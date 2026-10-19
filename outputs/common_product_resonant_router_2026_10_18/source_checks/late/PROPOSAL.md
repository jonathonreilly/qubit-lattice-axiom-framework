# Late negative-gap tails with the physical channel measure

New bounded author derivation requiring distinct review. This extends the normalized cutoff half-line estimates to phases with a negative spatial slope and a positive source translation. It treats the physical late incoming field and the ideal inelastic output's nonpositive-radius tail, including radius zero. The high auxiliary-frequency term is bounded in the correct channel momentum measure. No complete finite budget, new runtime exponent or normalized success-branch claim follows here.

## 1. Actual spectrum and the exact negative-gap sequence

Use the real quintic cutoff and source amplitude of frozen halfline43c0:

    g=chi F/sqrt(p_chi), p_chi=||chi F||_2^2>=1/2,
    F(k)=-i sqrt(2/pi)rho exp(ik)
                           /[(2-rho^2)cot k-i rho^2],
    0<rho<=1/2, rho^2<=h<=10^-3,
    e(k)=2(1-cos k), |k-pi/2|<=h.

The cutoff equals1 on |k-pi/2|<=h/2, is zero beyond3h/4 and uses 1-10s^3+15s^4-6s^5 on each width-h/4 transition. It is C2 and W^{3,1}; all source phases and positive normalization are retained. Let k_a(k)=k or q(k)=acos(cos k+r/2), with fixed 0<=r<=10^-3. For n>=0 define

    Z_n=(2pi)^(-1/2) integral
        exp(i[-n k_a(k)+Lk-u e(k)]) M(k)g(k)dk.          (1)

Here L,u>=0, and M maps the supplied logical/reference fiber to the full desired output fiber. Assume real derivative ceilings ||M^(s)||<=M_s for s=0,...,3. The input may be arbitrarily entangled with passive references; all estimates are operator bounds, independent of that reference dimension.

Require the explicit gap conditions

    Q=1.98u-L>=1,
    L+u<=Cgap Q, Cgap>=1.                              (2)

These are hypotheses to verify for a proposed physical tail. A positive late time alone does not supply them.

## 2. Explicit coefficient constant

For nonnegative four-entry vectors define

    (a star b)_s=sum_(l=0)^s binomial(s,l)a_l b_(s-l).

Put

    C=(1,1,2,5) star (1,1,3,10)
                    star (M0,M1,M2+M1,M3+3M2+3M1),
    D0=2C0,
    D1=20C0+2C1,
    D2=300C0+40C1+2C2,
    D3=4000C0+900C1+60C2+2C3.                            (3)

These D_s are numerical amplitude constants, unrelated to mediator energy labels. Set a_*=.23 and B2=4Cgap, B3=32Cgap, B4=128Cgap, and define

    P_late=D3/a_*^3+6B2 D2/a_*^4
       +(4B3/a_*^4+15B2^2/a_*^5)D1
       +(B4/a_*^4+10B2 B3/a_*^5+15B2^3/a_*^6)D0.       (4)

The resulting whole-half-line estimate is

    ||Z||_(ell2(n>=0))
      <=rho P_late/(h^2 Q^(3/2))
                    +4M0 sqrt(h)/rho exp[-rho^2 Q/(2(2-rho^2))]. (5)

All constants in (5) are explicit. The exponential prefactor is deliberately loose. The algebraic term depends on actual coefficient derivatives, not just their norms.

## 3. Pole representation and low-frequency phase proof

Set x=tan(k-pi/2), k(x)=pi/2+atan x, A=2-rho^2 and b=rho^2/A. The exact identities are

    F(k(x))=i sqrt(2/pi)rho exp(ik(x))/[A(x+ib)],
    1/(x+ib)=-i integral_0^infinity exp(ixv-bv)dv.        (6)

Thus the real auxiliary phase is phi_n(x)+vx, where phi_n=-n k_a(k(x))+Lk(x)-u e(k(x)). The amplitude after changing variable is

    a(x)=chi(k(x))exp(ik(x))k'(x)M(k(x)).

Its weak derivative L1 norms are at most D_s/h^2. To check the regularity explicitly, |x|<.001 on the cutoff support, k'>=.999, |k''|<=.002, |k'''|<=3 and |k''''|<=.1. The cutoff's x-derivative L1 bounds are (2h,20,300/h,4000/h^2). In k coordinates the derivative sup bounds are8/h,100/h^2,3840/h^3 and the total transition width is h/2; the third derivative is piecewise integrable, with no atoms because the cutoff and its first two derivatives match continuously at every join. Chain differentiation and Leibniz give (3). No analyticity of this cutoff is assumed.

The real channel bounds are .99<=k_a'<=100/99, |k_a''|<.003, |k_a'''|<3 and |k_a''''|<=10. The elastic case satisfies these directly. For q, the first three are the checked packet bounds. The fourth follows by differentiating cos q=cos k+r/2:

    sin q q''''=-cos k+cos q(q')^4+6sin q(q')^2q''
                            -3cos q(q'')^2-4cos q q'q'''.

Using sin q>.99, |cos q|<=.0015, |cos k|<=.001 and the preceding three derivative bounds actually gives |q''''|<.04. The ceiling10 is sufficient here.

Split the auxiliary integral into 0<=v<=Q/2 and v>=Q/2. In k coordinates the phase derivative on the low range obeys

    -n k_a'+L-2u sin k<=-.99n-Q,

because sin k>.99. After the x change and addition of v,

    (phi_n+vx)'<=-.999(.99n+Q)+Q/2
                      <=-.98901n-.499Q<=-a_*(n+Q).     (7)

In particular the derivative stays negative; the positive auxiliary frequency cannot cancel it on this range. Set N=n+Q. The original k-phase first derivative in absolute value is at most2n+L+2u<=2Cgap N. Its derivatives of orders2,3,4 have ceilings2Cgap N,3Cgap N,10Cgap N. The atan chain gives the higher x derivative bounds B2 N,B3 N,B4 N. The auxiliary vx contributes no higher derivatives.

Three real integrations by parts now give, uniformly on the low range,

    ||integral exp(i(phi_n+vx))a(x)dx||
                                    <=P_late/(h^2 N^3). (8)

For verification, the absolute integrand coefficients after three integrations are a'''/p^3,6a''p'/p^4,4a'p''/p^4,15a'(p')^2/p^5,a p'''/p^4,10a p'p''/p^5,15a(p')^3/p^6, with p=(phi_n+vx)'. Inserting (7) and the higher ceilings yields exactly (4). Compact W^{3,1} support and vanishing boundary traces justify the integrations, including the joins of the quintic.

The complete pole/Fourier prefactor is rho/(pi A sqrt(p_chi))<=rho. Drop exp(-bv)<=1 only after (8) and integrate over length Q/2. Thus

    ||Z_n,low||<=rho Q P_late/[2h^2(n+Q)^3].            (9)

Finally sum_(n>=0)(n+Q)^(-6)<=Q^-6+Q^-5/5<=6/(5Q^5). Taking the square root in (9) bounds the whole low part by the first term in (5). Radius zero is included in this sum.

## 4. High-frequency channel Parseval and its Jacobian

For v>=Q/2 work in the original k variable, and set p=k_a(k), with derivative d_a(k)=k_a'(k)>=.99. The full-integer n-Fourier sequence at this fixed v has p-spectrum

    chi(k(p))exp(ik(p))M(k(p))
       exp(i[Lk(p)-u e(k(p))+v tan(k(p)-pi/2)]) / d_a(k(p)). (10)

This is zero outside the transformed cutoff support. The divisor is d_a, not sqrt(d_a), because it comes from dk=dp/d_a in the Fourier integral. Its squared norm in dp is, for any unit input vector xi,

    integral |chi(k)|^2 ||M(k)xi||^2 / d_a(k) dk
                                    <=2h M0^2/.99.     (11)

All displayed phase factors have unit modulus. Fourier Parseval therefore bounds the complete integer sequence norm by M0 sqrt(2h/.99). Projection onto n>=0 contracts it. Minkowski over v and integral_(Q/2)^infinity exp(-bv)dv=b^-1 exp(-bQ/2) give

    ||Z_high|| <=[sqrt(2/pi)rho/(A sqrt(p_chi))]
                     M0 sqrt(2h/.99) b^-1 exp(-bQ/2)
                   <=4M0 sqrt(h)/rho exp(-bQ/2).        (12)

Here A b=rho^2 and p_chi>=1/2 are used. The scalar numerical prefactor is in fact below2, so4 is conservative. For each rho>0 the original double integral is absolutely integrable against the compact coefficient, justifying Fubini; Parseval and Minkowski subsequently provide the uniform stated bound. This proves (5). No assumption that the q Fourier transform has the unweighted k norm is used.

## 5. Exact late physical interfaces

For the actual incoming field in cf080, the phase is -nk+ell k-u e(k), n>=0, and the coefficient is the constant injection V_0. Take M=V_0 with ceilings (1,0,0,0), L=ell and u=jt in[3ell/4,7ell/8]. Then

    Q>=.485ell,
    L+u<=1.875ell<=16Q.

Thus (5) bounds the entire physical late incoming field, with record0, both I ports and arbitrary coherent program/path/reference input. It does not project onto only one successful port or discard its origin.

For the ideal inelastic scalar sequence of cf080,

    B_m(t)=(-i)/sqrt(2pi) integral
        exp(i[m q(k)+(ell+57)k-u e(k)])sqrt(q'(k))g(k)dk.

The nonpositive-radius tail is indexed EXACTLY by m=-n, n=0,1,... . Consequently it has phase (1) with k_a=q, L=ell+57 and M=-i sqrt(q'). The -i is a fixed part of the comparator phase, not an adjustable normalization. For ell>=1000 and the same late window,

    Q>=.485ell-57>=.428ell>=1,
    L+u<=1.875ell+57<=1.932ell<16Q.                    (13)

Take Cgap=16 in both examples. The ceilings (M0,M1,M2,M3)=(2,1,10,100) are valid for -i sqrt(q'): q'>=.99, |q''|<.003, |q'''|<3 and |q''''|<.04 imply them by direct differentiation. In particular

    (sqrt(q'))''=q'''/(2sqrt(q'))-(q'')^2/(4(q')^(3/2)),
    (sqrt(q'))'''=q''''/(2sqrt(q'))
       -3q''q'''/(4(q')^(3/2))+3(q'')^3/(8(q')^(5/2)).

Keeping sqrt(q') in M and then dividing by q' in (10) is correct: its squared contribution in (11) cancels that denominator. It must not be omitted first and counted again later. The general larger coefficient bound (12) remains valid without exploiting this cancellation.

Both the physical incoming n=0 coordinate and the ideal nonpositive m=0 coordinate are included, for their respective distinct estimates. This is important when the retained target begins at F radius1. The physical complete packet counts each origin once through its incoming-plus-outgoing sum; the present separate estimates do not change that coordinate convention.

The actual common factor exp(-ict) multiplies the physical field and comparator unchanged; it has unit modulus in these inequalities. A supplied exact uniform head penalty would likewise keep its common phase. No extra record phase is inserted: the relation E(k)=E_0(q)+kappa already fixes the threshold convention. All passive references and output port/record fibers are retained.

## 6. Scope, evidence and next obligations

Equation (5) supplies a late incoming norm and an ideal nonpositive output tail norm under explicit checked gaps. These estimates can replace those particular lead bounds only after this new argument is checked and the finite composition's exact signs and coordinate identifications are matched. They do not control strict internal maps, source residuals, early matching, integrated boundary errors, positive output tails or final positive normalization by themselves. No global finite resource exponent or improved twelve-budget family is asserted.

An arbitrary matrix M with the stated real third derivatives is covered abstractly. For a full outgoing network matrix that premise would require the separate b262 third-derivative argument; the two concrete applications above use only a constant injection or the explicit scalar sqrt(q') and do not depend on that provisional matrix extension. The prior outgoing and half-line proposals remain frozen.

Exact sources under N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934:

- common_product_resonant_halfline_tails/PROPOSAL.md:43c0cc0560ccd6b9ce33345796f511fba63c5fa7360f9225e8d9b30ec1bf33b1. Authored and fully read immediately before this task; distinct check pending. Its coefficient convention and pole route are reconstructed above for the changed sign/offset rather than treated as a late-tail theorem.
- common_product_outgoing_pole_tail/PROPOSAL.md:b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80. Fully read/frozen in the preceding task; real matrix derivative transfer remains a separate provisional interface. Both preceding hashes were verified unchanged in the half-line task.
- common_product_biased_record_packet/PROPOSAL.md:cf080f0dae5bf71021fe91533fc97355ceaaadb5db6f3d3145e3a911c8f3ffcf, with prior fully read distinct check315a618f389598fe8443a8ed3cdf8c39180b65ba223c4de2a359be4e218ea916. Its complete exact phase/measure arguments were fully reread and hash refreshed in the outgoing-pole task and reused unchanged here.
- common_product_biased_record_finite_seed/PROPOSAL.md:532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123. Fully reread/hash verified in that task; only its actual late window and target coordinate convention are used, with no edits to its budgets.
- common_product_endpoint_launch/PROPOSAL.md:fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4. Its exact normalized source premises retain their earlier complete reads and checked scope; the critical pole identity is displayed anew in (6).

ROOT suggested the late-gap extension and the channel-measure high-frequency bound. The author reconstructed its negative derivative, phase constants, weak-derivative integration, half-line sum, Parseval Jacobian and concrete coordinate enumeration above. This is source/design-exposed same-model author derivation, not independent checking. A distinct check remains required, especially of (10)--(13) and the sign in (7).

Only this proposal was created. No scientific executable, simulation/sweep, delegation, source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. No physical readout, preparation mechanism, native coefficient supply, old literal processor transfer, normalized rare-branch guarantee or permanent halt is claimed.
