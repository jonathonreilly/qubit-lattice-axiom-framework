# Independent lapse-rescaling derivation, frozen before new author-source exposure

Scope: focused independent mathematics supporting root's continued authorship. This is not a formal audit, full solution construction, empirical test, or action/initial-state selection. I read the inherited complete M17 note and used its already checked physical action and static scalar equation. The task disclosed the idea of a positive rescaling to remove lapse second derivatives; it supplied no new rescaling formula. I have not read root's `lapse_derivative_probe` working derivation, scripts, or M18 sources. The inherited sources and prior independent reviews are identified in `INHERITED_EXPOSURE_v1.json`.

The result is affirmative, with an essential sign threshold and a cost. The substitution is z=f^lambda w, where f is any positive dimensionless constant normalization of the lapse and lambda=a/(1-3a)>0. It removes the lapse Laplacian exactly, leaving a first-gradient square with a destabilizing sign. A finite positive-Green norm bound follows only after imposing a constant threshold that controls both the complete boundary and the entire region where the potential sign is usable. Lapse contrast and first-derivative control replace the removed second-lapse-derivative input. Spatial curvature and all physical action/domain suppliers remain.

## Inherited equation and hypotheses

Take the complete M17 candidate, all fields static, and the physical metric

    ds^2 = -N(X)^2 dt^2 + h_ij(X) dX^i dX^j,
    L_N = Delta_h + grad_h ln N . grad_h,
    lambda = a/(1-3a), 1/4<a<1/3.

Thus lambda>1 for the candidate, although the following conjugacy algebra works for any positive lambda. With the exact M17 normalization Z=Q(1-3a)/[a(1+s)], its radial equation is

    L_N z = -(lambda/2) R4 z + S_z,
    S_z = {Q z [4k |grad x|^2/(9D)+k |grad y|^2/(3D)]
             +(1/2) partial_z V_J}/Z.

All gradients and curvatures here are physical. Staticity and the complete supplied potential imply S_z>=0 when z>=1. They do not imply that sign for every positive z. There is no setting x=y=0 in the comparison and no identification of Q with measured Newton G. This derivation only uses the sign, not an assumed scalar mass or a particular field history.

Assume a bounded smooth domain with every boundary component controlled, positive lapse bounded away from zero, uniformly positive spatial metric, and enough smoothness for the inherited classical equations and weak elliptic comparison; the C3 metric/lapse and C2 finite scalar hypotheses of M17 suffice. A horizon, an unbounded domain without additional conditions, or an uncontrolled inner boundary is excluded. The analysis below is not a proof of a weaker-regularity extension.

## Exact conjugacy and uniqueness within lapse-only rescalings

Use the static curvature identity

    R4 = R3 - 2 Delta_h N/N.

Let n=ln f, with f=N/N_* and N_* a positive spatial constant. Then Delta N/N=Delta n+|grad n|^2. For the general substitution z=f^p w,

    f^(-p) [L_N z-lambda (Delta N/N) z]
      = Delta w+(2p+1) grad n . grad w
        +(p-lambda)(Delta n) w
        +[p(p+1)-lambda]|grad n|^2 w.

Therefore p=lambda is the required power, and

    L_tilde w = -C_raw w + f^(-lambda) S_z,                 (A)
    L_tilde = Delta_h+(2lambda+1) grad_h ln f . grad_h
            = [f^(2lambda+1) sqrt(h)]^(-1)
              partial_i[f^(2lambda+1) sqrt(h) h^ij partial_j],
    C_raw = (lambda/2) R3 + lambda^2 |grad_h ln f|^2.       (B)

There is no lapse second derivative in either coefficient of this equation. The gradient-square coefficient is positive in C_raw: it cannot be discarded as an additional favorable source. The opposite power p=-lambda leaves a -2lambda Delta n coefficient and does not achieve the target.

More generally, for z=G(N)w the coefficient of Delta N after division by G is G'/G-lambda/N. Cancellation for arbitrary smooth positive N requires G'=lambda G/N and hence G=constant times N^lambda. This is uniqueness among rescalings depending only on the pointwise lapse; it is not a theorem excluding other changes of variables or separately supplied elliptic solutions.

## Threshold and positive-Green comparison

Define m=inf_Omega f>0 and m_boundary=inf_boundary f>0. Suppose z<=zB on the complete boundary, zB>=1. A safe constant transformed threshold is

    b = max[zB m_boundary^(-lambda), m^(-lambda)].         (C)

The first term guarantees w<=b on every boundary component. The second guarantees that w>b implies z=f^lambda w>1 throughout the domain, where S_z is known nonnegative. Neither condition can generally be omitted. A larger finite b is also valid. If the actual nonconstant boundary upper function is known, its transformed supremum may replace the first term; no boundary values are selected here.

Let

    c = (C_raw)_+ >=0,
    -L_tilde P=c, P|boundary=0,
    eta=sup_Omega P.

One may instead use the looser c=lambda (R3)_+/2+lambda^2|grad ln f|^2. Because the Dirichlet inverse G=(-L_tilde)^(-1) is positive on this regular bounded domain, P=Gc>=0. For v=(w-b)_+, weak Kato comparison applied to (A) gives

    -L_tilde v <= c(v+b), v|boundary=0,
    v <= G(cv)+bP.

The positive operator T:g->G(cg) has L-infinity norm ||T||=||T1||=eta: positivity supplies the upper bound and the constant function 1 attains it. Finite fields on compact closure have finite V=sup v. Hence V<=eta(V+b). If eta<1,

    w(X) <= b[1+P(X)/(1-eta)] <= b/(1-eta),
    z(X) <= f(X)^lambda b[1+P(X)/(1-eta)],                 (D)
    sup z <= (sup f)^lambda b/(1-eta).

If eta>=1 this argument is inconclusive, rather than an exclusion or failure of the candidate. No claim of existence, uniqueness, dynamics, or a field-gradient/force bound follows. The positive inverse used here is that of -L_tilde, not an asserted positive inverse of an unchecked operator with a zeroth-order negative potential.

A useful normalization is f=N/Nmin>=1. Taking b=zB is then immediately valid, and

    z(X) <= zB (N(X)/Nmin)^lambda [1+P(X)/(1-eta)],
    sup z <= zB (Nmax/Nmin)^lambda/(1-eta).                (E)

The sharper (C) in this normalization is max[zB/(inf_boundary f)^lambda,1]. A variable threshold zB f^(-lambda) would require differentiating it in Kato comparison and reintroduce the lapse Laplacian; treating that variable threshold as a constant is invalid.

## Constant clock normalization and derivative suppliers

Under N->gamma N with constant gamma>0, log gradients and L_tilde are unchanged: the weight acquires a cancelling overall factor gamma^(2lambda+1). Thus c,P,eta are unchanged. If f itself is multiplied by gamma, w and b scale by gamma^(-lambda), so the physical product f^lambda b and bound (D) are unchanged. The choice f=N/Nmin makes this invariance explicit. No absolute clock normalization is needed.

The transformation does not remove spatial-curvature input R3 or lapse first derivatives. It can be ill conditioned when lambda, lapse contrast, metric distortion, or eta/(1-eta) is large. It is not uniformly sharper than M17. For example a static Schwarzschild annulus has R4=R3=Delta N=0 but grad N nonzero; M17's curvature source vanishes, while the transformed source includes lambda^2|grad ln N|^2>0. This is a geometric comparison, not a claim that Schwarzschild with positive Hv supplies a full candidate solution.

In spherical areal coordinates h=dr^2/B+r^2 dOmega^2, on a regular ball,

    R3=-2B'/r+2(1-B)/r^2,
    L_tilde w=B w''+[2B/r+(2lambda+1)B f'/f+B'/2]w',
    C_raw=lambda[-B'/r+(1-B)/r^2]+lambda^2 B(f'/f)^2.

Regularity and P(L)=0 give

    P(r)=integral_r^L ds/[f(s)^(2lambda+1)s^2 sqrt(B(s))]
          integral_0^s dt f(t)^(2lambda+1)t^2 c(t)/sqrt(B(t)).

For c<=cmax, B>=Bmin>0 and lapse contrast rho=Nmax/Nmin, this implies the sufficient envelope

    eta<=rho^(2lambda+1) cmax L^2/(6Bmin).

The lapse second derivative has disappeared; B' and lapse first derivative remain. In M17's conditional outward clock/range map, g=tau'=2/(f sqrt(B)) gives B=4/(f^2g^2) and B'/B=-2(f'/f+g'/g). Thus this route uses f' and g'=tau'', but not f''. This is an exact supplier-order statement under the same static clock, vacuum radial propagation, complete boundary, and calibrated areal-radius assumptions. Finite noisy values do not themselves supply these derivative bounds. No actual measurements or carrier conventions were used.

## Failure witnesses and exact checks

1. Wrong power: p=-lambda leaves -2lambda Delta ln N. Wrong gradient sign: after the correct power the remaining term is +lambda^2|grad ln N|^2 on the left before writing (A), hence the destabilizing C_raw in (A).

2. An unnormalized threshold w>1 does not imply z>1. At lambda=2, constant f=exp(-1/4), z=exp(-1/4) gives w=exp(1/4)>1 while z<1. With nu=64a and x=y=0, the inherited potential-derivative bracket is 12a+nu[4(ln z)^2+2ln z]=-4a<0. The correct sign floor f^(-lambda)=exp(1/2) deactivates this point. This is an exact failure of the sign-dropping step, not a constructed full metric/matter solution.

3. Boundary-only rescaled thresholds also fail. On [-1,1], f=1+x^2 has boundary f=2 and interior minimum 1. With lambda=2 and zB=1 the transformed boundary ceiling is 1/4. At the center the same z=exp(-1/4)>1/4 activates the truncated field but still has the negative source above. The global sign floor 1 in (C) is necessary for this argument. Local scalar ODE jets can have this value; no global scalar or matter solution is asserted by this witness.

4. A positive gradient source cannot be dropped from the comparison merely because it came from a rescaling. On [0,ln 2], take f=exp(x), lambda=2 and

       w=(15 exp(-x)-8 exp(-4x))/7.

   It solves w''+5w'+4w=0, with both boundary values 1. At x=ln(4/3), w=279/224>1. Dropping the 4w potential would falsely produce a unit maximum bound. This is an exact linear comparison fixture with S_z=0, not a complete positive-Hv candidate solution.

   Its positive Green solution is

       P=128 ln(2)/155 [1-exp(-5x)]-4x/5,
       eta=128 ln(2)/155-(4/25)[1+ln(160 ln(2)/31)],

   with 0<eta<1. The general proof yields the admitted pointwise bound; a separately evaluated 101-point diagnostic checks it for this fixture. The grid is not the proof.

5. Complete boundary matters independently: w=1+x is harmonic on [0,1] and exceeds 1 when only its left boundary is reported. The unreported right boundary equals 2. This elementary comparison witness does not assert a full candidate solution.

`independent_controls_v1.py` imports only SymPy/mpmath, not root sources. It verifies the complete conjugacy, drift and gradient coefficients, constant-clock identities, sign witnesses, exact Green fixture, spherical divergence identity, and sup-bound algebra. The saved result is 37 passed, 0 failed. No failed execution was hidden or repaired; the rejected shortcuts above are deliberate mathematical counterexamples. There was no new root-source exposure before this freeze.

The useful result is a conditional necessary ceiling with one lower derivative order in the lapse supplier. It neither derives the action, supplies a physical metric or boundary, chooses a scalar state, nor closes the measured-gravity bridge.
