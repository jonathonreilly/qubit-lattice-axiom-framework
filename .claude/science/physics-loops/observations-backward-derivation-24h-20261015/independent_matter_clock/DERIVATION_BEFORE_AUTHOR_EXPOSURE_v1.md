# Independent matter-clock derivation before author exposure

Only MATTER_CLOCK_NEUTRAL_CONTRACT_v1.json was read for this matter-clock
unit. No author matter-clock note, code, conclusions or results were opened.
Earlier Einstein-time scalar-history work is known context, including its
uncoupled dust-era family; the independence claim here concerns this new
matter-clock derivation and implementation. The action is varied directly
below. This proof and its decisive fixtures are frozen before coding.

## Action equations and clock conversion

With an arbitrary homogeneous lapse n, a comoving dust rest-mass constant
rho_* and Einstein scale factor a, the reduced action per comoving volume is

    L=-3 M^2 a adot^2/n + a^3 phidot^2/(2n)
      -n a^3 V(phi)-n rho_* A(phi).

The lapse, scale-factor and scalar variations, followed by n=1, imply

    3M^2 H^2=v^2/2+V+r,
    -2M^2 Hdot=v^2+r,
    vdot+3Hv+V_phi+(A_phi/A)r=0,
    rdot+3Hr=(A_phi/A) v r,

where r=A rho and rho=rho_* a^-3. The scalar variation differentiates the
particle term A itself, not an independently held Einstein energy density r.

Use primes for matter time tau, with dt_E/dtau=1/A, and define

    x=phi'/M, b=M A_phi/A, u=h-bx,
    s=r/(M^2 A^2), z=V/(M^2 A^2).

No function A(tau) is supplied. Its evolution follows from the coupling:

    A'/A=bx, H_E=A u, v_E=M A x.
    Hdot_E=A^2(u'+bxu), vdot_E=M A^2(x'+bx^2).

The Raychaudhuri equation and dust exchange become

    s=-2(u'+bxu)-x^2
     =2b x'+Q(tau,x),                                    (1)
    s'=(2bx-3h)s,                                         (2)

    Q=(2b^2-1)x^2+2(b'-bh)x-2h'.
    z=3u^2-x^2/2-s.                                      (3)

For F=(V_phi+(A_phi/A)r)/(M A^2), scalar evolution gives
F=-x'-3hx+2bx^2. Since bare rho'=-3u rho, the stipulated response obeys

    F'+2bxF=kappa x-3bu s.

Thus the second independent compatibility equation is

    E_m=x''+(3h-2bx)x'+(3h'+kappa)x
        +(6bh-2b')x^2-4b^2x^3-3bu s=0.                  (4)

The physical meaning of kappa is exactly the fixed-bare-density derivative
in the contract divided by A^2. It is not presumed to be a measured pole.
At fixed r rather than fixed rho the same force derivative would differ
by b^2 s after this division.

## Necessity, sufficiency and regularity

A convenient sufficient regularity for the direct two-equation form is
h,b in C2, kappa continuous, and candidate x in C2. Require on a connected
open interval x nonzero and s from (1) strictly positive. Let (2) and (4)
hold. Choose A_0>0 and phi_0, and integrate A'/A=bx and phi'=M x.
Choose a positive normalization for a_J with a_J'/a_J=h, set a_E=a_J/A,
r=M^2 A^2 s, rho=r/A, and V=M^2 A^2 z.

Equation (2) gives rho'/rho=-3u, hence rho a_E^3 is a positive constant.
Friedmann and Raychaudhuri hold by construction. The scalar equation is
not lost when differentiated: differentiating (3), before any mass
condition, gives

    x[x'+bx^2+3ux+V_phi/(M A^2)+b s]
       =-s'+(2bx-3h)s.

It vanishes by (2), and division by x is allowed. Equation (4) then makes
the independently reconstructed fixed-rho curvature equal the supplied
kappa, again because x is nonzero. A(phi),V(phi) exist on the monotonic
sampled field interval; the scalar identity supplies the required second
derivative of V. An affine addition to V is not an available integration
constant: Friedmann and the original scalar equation already fix it.

This proves necessity and sufficiency for the direct form on that chart.
The positive A map defines an increasing Einstein time; no continuation
through x=0, s=0 or an interval endpoint, and no off-chart action extension,
is inferred.

## First-order elimination on a narrower chart

After substituting (1), write

    E_m=x''+C x'+R,
    C=3h-2bx-6b^2u,
    R=(3h'+kappa)x+(6bh-2b')x^2-4b^2x^3-3bu Q.

The dust equation is

    E_d=2b x''+(4b'+4bh-2x)x'+Q_tau-(2bx-3h)Q.

Here Q_tau is a partial derivative holding x fixed. Their exact combination
is

    E_d-2b E_m=-2 Delta x'+2N,
    Delta=c4 x-2b'-bh(6b^2-1), c4=6b^4-2b^2+1,
    N=[Q_tau+(3h-2bx+6b^2u)Q
       -2b((3h'+kappa)x+(6bh-2b')x^2-4b^2x^3)]/2.         (5)

The slope c4=6(b^2-1/6)^2+5/6 is strictly positive for real b.
N is cubic; my hand expansion is

    N=n3 x^3+n2 x^2+n1 x+n0,
    n3=b(1-b^2)(6b^2+1),
    n2=2b(1-3b^2)b'+(12b^4-4b^2-3/2)h,
    n1=b''+2(1+3b^2)h b'+2b(3b^2-1)h'
       -3b(1+2b^2)h^2-b kappa,
    n0=-h''-3h(1+2b^2)h'.

On Delta nonzero the flow is x'=N/Delta. Substitution into E_m, with
partials at fixed x, yields the polynomial filter

    P=Delta^2 N_tau-Delta N Delta_tau
      +Delta N N_x-N^2 Delta_x+C N Delta^2+R Delta^3=0.     (6)

For classical use of this algebraic filter, h,b in C3 and kappa in C1
are sufficient: N contains h'',b'',kappa and N_tau contains
h''',b''',kappa'. These stronger input requirements must not be concealed.
The flow plus P=0, x nonzero and s>0 is equivalent to the direct form on
Delta nonzero. The flow is locally Lipschitz in x there; a value x(tau_0)
determines at most one compatible full chart history.

The polynomial has degree at most six. The hand-derived x^6 coefficient is

    -b^2(6b^4-2b^2+1)(6b^2-1)(12b^2-7).                 (7)

This will be independently checked by expansion and high-x balance.
The degree can fall at b=0, b^2=1/6 or b^2=7/12. If b is identically zero
near the time, the degree is at most four. Merely b(tau_0)=0 with b' nonzero
does not imply the fourth-degree restriction; the fifth-degree coefficient
at such a point is -b'. The leading coefficient alone cannot classify
the exceptional lower-degree cases.

If P is a nonzero polynomial at one time, at most six x histories can
stay on the regular flow chart throughout the connected interval. An
instantaneous root does not itself establish a history. This bound does
not include the continuous A_0 normalization freedom or unconstrained
extensions of the reconstructed action.

Delta=0 is not a physical exclusion. It is only loss of the particular
first-order elimination. At such a point compatibility still requires
N=0; P vanishes there whenever N=0 but does not define a flow. The direct
form (1)-(4) remains the appropriate test. The exact fixture below proves
that positive-density, monotonic physical histories can live on Delta=0
throughout their interval.

## Normalization

For fixed x,h,b,kappa and fixed a_J normalization,

    A -> lambda A, V -> lambda^2 V, r -> lambda^2 r,
    rho -> lambda rho, a_E -> a_E/lambda,
    dt_E -> dt_E/lambda, rho_* -> rho_*/lambda^2

preserves all registered input functions and direct compatibility.
These are reconstructed actions/normalizations, not a claim that an
already fixed action has a scaling symmetry with unchanged matter data.
The canonical field origin and Einstein time origin are also conventional.
A generic field rescaling is not allowed once M and the canonical kinetic
normalization are fixed.

If positive rho_* and a_J normalization are independently supplied,
A_0^2=M^2 s_0 a_J0^3/rho_* fixes the positive A_0. Equivalently a registered
physical dust density rho_J=rho/A^3 fixes A^2=M^2 s/rho_J. Merely assigning
a scale-factor normalization is not such a density measurement.

## Frozen exact fixtures and rejection controls

All constants below use stipulated numerical reference units, not derived
physical scales. Derivatives and positivity are checked only on the stated
domains. These are synthetic constructions.

1. Nonzero-coupling regular flow fixture: M=1, Einstein t>0,
   H_E=2/t, phi=ln t, A=t^4, rho=3t^-6,
   r=3t^-2 and V=17/(2t^2). Then tau=t^5/5 and

       h=6/(5tau), b=4, x=1/(5tau),
       s=3/(25tau^2), kappa=82/(25tau^2).

   Direct differentiation at fixed rho gives 34/t^2+48/t^2 for the
   two Einstein curvature pieces. Holding r fixed instead would omit
   the second term. The Delta value is to be computed exactly. Test
   action equations, both direct equations, flow, polynomial and
   reconstruction, plus a wrong-curvature perturbation.

2. A regular physical history on the singular elimination chart:
   H_E=12/(17t), phi=(4/17)ln t, A=t^(2/17),
   r=(392/289)t^-2, V=(32/289)t^-2.
   With tau=(17/19)t^(19/17),

       h=14/(19tau), b=1/2, x=4/(19tau),
       s=392/(361tau^2), kappa=2410/(361tau^2).

   It has x>0, s>0, Delta=N=0 identically. Check the original scalar,
   Friedmann, dust and curvature equations; do not evaluate N/Delta.

3. A varying-coupling forward fixture, convenient in Einstein parameter
   t in (0,1): M=1, phi=t, H_E=1/t, a_E=t,
   rho=t^-3, A=2t-t^3, r=2/t^2-1, V=1/t^2+1/2.
   Then tau=t^2-t^4/4 is increasing, and d/dtau=A^-1 d/dt gives

       x=1/[t(2-t^2)],
       b=(2-3t^2)/[t(2-t^2)],
       h=4(1-t^2)/[t^2(2-t^2)^2],
       s=1/[t^4(2-t^2)],
       kappa=6(1-t^2)/[t^6(2-t^2)^2].

   Check direct equations as rational t identities. At t=1/2 check
   every input jet needed by P, nonzero Delta, exact flow and filter.
   This exercises b',b'',b''' and kappa' rather than constant-b cases
   alone. The neighborhood flow-domain assertion depends on the
   computed nonzero Delta at that point.

4. Continuous shape ambiguity in addition to A_0: with b=0,
   h=2/(3tau), kappa=2/tau^2, any x=c/tau with
   0<c^2<4/3 has s=(4/3-c^2)/tau^2,
   A=A_0, phi=M c ln tau and
   V=M^2 A_0^2 c^2/(2tau^2). The direct and flow equations hold and
   P is identically zero. Distinct absolute c change the kinetic/dust
   fractions; they are not just field translations.

Independent executable controls will also test off-constraint action
variation signs, the eliminated equation identity, the exact leading
coefficient at general symbolic b, several specialized degrees, the
fixed-rho versus fixed-r distinction, normalization scaling, and that a
linear or constant potential addition violates the retained equations.
Any incorrect hand formula or actual operational failure will be preserved.
