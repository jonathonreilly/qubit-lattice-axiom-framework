# Initial energy layer and band-resolved power in the full original cube

Personal root derivation, 2026-09-24. Conditional candidate; not independently
checked or published. The full-ensemble energy/rare-density candidate is an
explicit provisional dependency. Its independent PRE establishes the scalar
moment limits and uniform source/age estimates; its POST is still pending.
No physical reservoir, selected Hamiltonian, new axiom or audit verdict is
supplied here.

## 1. Fixed model and quantities

Keep the original compensated lambda=0 cube, canonical Hermitian N=4
zero-field input, and complete original resolved or coherent instrument.
Fix delta,K,kappa>0 and take the integer-spin sequence
epsilon^2 S(S+1)=delta/K. H_e is the physical Hermitian Hamiltonian,
L_i=sqrt(kappa) epsilon^-1 j_i, and the complete trace-one density is
rho_e=rho4,e+rho6,e+rho8,e, with H8=0. No field-only postbirth limit is used.

Use the exact no-event propagator V_N and first-birth decomposition

    v4,e(s)=V4,e(s) U4,e Omega,
    x_i,e(s,t)=V6,e(t-s) L_i v4,e(s),
    rho6,e(t)=sum_i integral_0^t |x_i,e(s,t)><x_i,e(s,t)| ds. (1)

Let Q1,e be the Hermitian first-high spectral projector in N=6, with
canonical isometry U1,e from its bare first-high coordinate space. Extend
those coordinates by zero to the fixed physical rotor space. Set

    n_e(t)=Tr[Q1,e rho6,e(t)],
    g_e(t)=Tr[H6,e Q1,e rho6,e(t)],
    M_e(t)=Tr[H_e rho_e(t)].                               (2)

The complete physical first-high rotor generator and actual source are

    Z=-i delta Pi1(FF*-F*F)Pi1-kappa Gamma1/2,
    Gamma1=2 P_bright,
    R_i=(j_i F^2/2-F j_i F)P4=-F_a j_i F_a P4.

For a coherent mark the two signs are added inside R_i, before forming its
outer product or propagating it. On the low N=4 physical rotor space,
sum_i R_i*R_i=72I for either complete original instrument. Write

    u4(t)=exp(-24 kappa t) exp(-it h4) Omega,
    S4(t)=||u4(t)||^2=exp(-48 kappa t),
    h_N=K D_N-delta Z_N*Z_N/2.

Here Z_N is the two-hop low-band map in the parent, distinct from Z above.
E_low(t) is the ordinary energy of the full common low rotor ensemble.

The full-ensemble candidate and its independent PRE give, uniformly on
each fixed positive compact physical-time interval,

    M_e(t) -> E_low(t)+delta Tr Sigma(t),
    epsilon^4 Tr[H_e^2 rho_e(t)] -> delta^2 Tr Sigma(t),
    epsilon^4 Var_(rho_e(t))(H_e) -> delta^2 Tr Sigma(t),    (3)

where

    Sigma(t)=kappa sum_i integral_0^infinity
      |exp(tau Z) R_i u4(t)><exp(tau Z) R_i u4(t)| d tau.  (4)

The scalar part of (3) is supported by the independent PRE. The trace-norm
rare-density extension in the sealed author candidate is still under POST
comparison. The results below can derive the needed density statement
directly from the same L2-in-age estimates; they do not assume convergence
of unbounded energy observables from ordinary state convergence.

## 2. The initial physical-time layer

For finite fast age tau>=0 define the positive trace-class operator

    Sigma_init(tau)=kappa sum_i integral_0^tau
      |exp(v Z) R_i Omega><exp(v Z) R_i Omega| dv.          (5)

For every fixed A<infinity the proposed limits, uniformly for tau in [0,A],
are

    epsilon^-4 U1,e* rho6,e(epsilon^2 tau) U1,e
                                      -> Sigma_init(tau) in trace norm,
    M_e(epsilon^2 tau) -> E_low(0)+delta Tr Sigma_init(tau),
    epsilon^4 Var_(rho_e(epsilon^2 tau))(H_e)
                                      -> delta^2 Tr Sigma_init(tau). (6)

The same limit as the last line holds for the scaled second moment.
This includes tau=0; it does not assert uniformity for unbounded tau.

To prove it, set s=epsilon^2 sigma in (1), 0<=sigma<=tau<=A. The parent
uniform birth-source estimate, in exact no-event block coordinates, is

    Pi1 J6,e^-1 L_i v4,e(s)
       =sqrt(kappa) epsilon R_i,S a4,e(s)+O(epsilon^3),    (7)

where a4,e(s) is the exact low N=4 coordinate. It converges strongly to
u4(s), uniformly on each bounded physical interval, and carries a common
fixed electric-weight bound. Consequently

    sup_(sigma<=A) ||R_i,S a4,e(epsilon^2 sigma)-R_i Omega|| ->0.

Remove the scalar first-high phase. Its exact fast generator A_e converges
strongly to Z with common bounded semigroups. On this compact age interval,
the propagated, canonical Hermitian first-high coordinate divided by
sqrt(kappa) epsilon converges uniformly to
exp[(tau-sigma)Z] R_i Omega. The Hermitian/no-event intertwiner mismatch
costs O(epsilon^3) times the uniformly bounded raw L_i source, and hence
O(epsilon^2) after that division. It does not alter the limit. The scalar
carrier phase cancels inside each rank-one density.

Since ds=epsilon^2 d sigma, (7) gives exactly the epsilon^4 density scale
in (6). Uniform convergence of the vector paths on the finite triangle
and the inequality

    || integral (|f><f|-|g><g|) ||_1
                  <= ||f-g||_L2 (||f||_L2+||g||_L2)       (8)

prove uniform trace-norm convergence. The time change v=tau-sigma yields
(5). This is a compact-time consequence; no finite-spin decay estimate
at infinite fast age has entered.

On the first-high Hermitian block,
H6,e=delta epsilon^-4[I+O(epsilon^2)] uniformly in spin. Thus this block's
ordinary mean tends to delta Tr Sigma_init and its scaled second moment
tends to delta^2 Tr Sigma_init.

The parent bounds hold uniformly on [0,T], including zero: the N=4 first
high amplitude is O(epsilon^3), the aggregate higher amplitude is
O(epsilon^4), and the low vector is uniformly electric-weighted. Hence
the N=4 mean tends uniformly in the shrinking interval to E_low(0), and
its scaled second moment is O(epsilon^2). Its initial canonical low mean
has that same limit. The leading N=6 low source and its energy-vector norm
are bounded; its low ordinary mean and second moment over an interval of
length epsilon^2 A are O(epsilon^2). The O(epsilon^2) low-coordinate source
remainder is controlled by self-adjointness and the O(epsilon^-2) norm of
the low Hamiltonian, exactly as in the parent proof. The second-high
source is at worst O(epsilon^3) after multiplication by L_i; its mean
and scaled second moment over that interval vanish. H8 remains zero.
The full mean in the shrinking interval is bounded, so its square times
epsilon^4 also vanishes. This proves every scalar assertion in (6).

The profile is monotone in the positive-operator order. Its trace derivative
is the genuine derivative of the limiting function,

    d/dtau [delta Tr Sigma_init(tau)]
       =kappa delta sum_i ||exp(tau Z) R_i Omega||^2.       (9)

It is positive at zero, with value 72 kappa delta. This does not by itself
assert convergence of pointwise derivatives of microscopic means.

The previously proved rotor source bound gives
||exp(tau Z)R_i Omega||^2 <= C(1+tau)^(-5/2). Therefore

    Sigma_init(tau) -> Sigma(0) in trace norm,
    ||Sigma(0)-Sigma_init(tau)||_1 <= C(1+tau)^(-3/2).     (10)

This order of limits is explicit: first epsilon->0 at fixed tau, then
tau->infinity. It connects the initial layer to the right-hand limit of
(3); it does not establish one uniform approximation for arbitrary
tau depending on epsilon.

## 3. Uniform energy bound needed for integrated accounting

The scalar proof in the independent full-ensemble PRE gives more than
positive-time convergence. Its age envelope, source remainders, low
weighted estimates and higher-band estimates imply

    sup_(0<=t<=T) |M_e(t)| <= C_T,
    sup_(0<=t<=T) |g_e(t)| <= C_T,
    sup_(0<=t<=T) n_e(t) <= C_T epsilon^4.                (11)

For clarity, the full age integral of the normalized first-high profile
is bounded uniformly even if its upper endpoint t/epsilon^2 is short.
Through tau*=epsilon^-1, its squared norm is bounded by the integrable
rotor envelope plus the epsilon^4(1+tau)^(3/2) error envelope. Beyond tau*
the exact bounded semigroup carries O(epsilon^(5/4)) amplitude through
at most T/epsilon^2 ages. The resulting integral is bounded, with the
old-age term O(epsilon^(1/2)). The normalized source/intertwiner error
has squared-age integral O(epsilon^2), and its cross term is controlled
by Cauchy-Schwarz. This proves the n_e bound and hence the g_e bound.
The low and other bands are bounded by the remaining parent estimates.
No uniform rate of convergence at t=0 is inferred from (11).

In particular (3), (11) and dominated convergence imply L1([0,T])
convergence of M_e to E_low+delta Tr Sigma, and of g_e to delta Tr Sigma.
Changing a function's value at t=0 does not affect that statement.

## 4. Net power as a distribution, including the initial impulse

At finite spin define the exact microscopic ensemble power

    P_e(t)=dM_e(t)/dt
      =sum_i Tr[H_e (L_i rho_e L_i* - {L_i*L_i,rho_e}/2)]. (12)

The Hamiltonian commutator contributes zero since H_e is time independent.
This is the system-energy drift of the supplied GKLS equation. It is not
an identified battery-work or bath-heat observable.

For every C1 test function phi on [0,T] vanishing near T, finite-spin
integration by parts is exact:

    integral_0^T phi P_e
       =-phi(0) M_e(0)-integral_0^T phi' M_e.             (13)

The canonical initial mean tends to E_low(0), whereas the positive-time
limit has right endpoint E_low(0)+delta Tr Sigma(0). Use (11) and dominated
convergence in (13) to obtain

    integral phi P_e -> phi(0) delta Tr Sigma(0)
                +integral phi(t) d/dt[E_low(t)+delta Tr Sigma(t)] dt. (14)

This is distributional convergence of the net power, with an initial
positive impulse of weight delta Tr Sigma(0). It is not convergence in
total variation, weak convergence of finite signed measures, pointwise
power convergence, or a claim that positive and negative powers have
bounded total variation. Such claims need additional estimates.

The derivative on the right exists for this canonical input. The weighted
Dyson argument preserves every fixed electric weight, and the Hamiltonian
has quadratic electric growth plus bounded finite shifts. Thus u4 is C1
in the weighted space needed for the rotor decay estimate. In (4), apply
the same integrable bounds to R_i u4 and R_i u4' and use Cauchy-Schwarz in
age. Differentiating the rank-one integral in trace norm is justified;
its derivative is the integral of the two cross terms. The common low
ensemble energy is C1 by the analogous weighted triangle integral and
finite-hop jump estimates. Alternatively, (13) already defines (14) with
the derivative interpreted distributionally, without assuming pointwise
smoothness of that limiting energy function.

The frozen-age Sylvester identity for (4) is

    Z Sigma+Sigma Z*=-kappa sum_i |R_i u4><R_i u4|,
    Tr[Gamma1 Sigma(t)]=72 S4(t),
    Tr[P_bright Sigma(t)]=36 S4(t).                       (15)

It follows by differentiating the bounded semigroup in its trace-class
integral and using its vanishing upper endpoint. In particular the impulse
weight in (14) is at least 36 delta. This fixes kappa>0 before all limits;
neither (10), (14), nor that lower bound is asserted uniform as kappa->0.
Equation (15) alone is a frozen-age balance, not (14); the latter required
the complete finite-spin energy identity and uniform integrability.

The same calculation for g_e, whose initial value is zero, gives

    integral phi g_e' -> phi(0) delta Tr Sigma(0)
                         +integral phi delta d(Tr Sigma)/dt.       (16)

Thus this entire initial energy impulse is carried by the first-high
N=6 band in the limit. Other bands account for the regular low energy.

## 5. Large opposing terms in the exact first-high energy equation

Define the exact band energy gain and loss terms

    Pplus_e(t)=kappa epsilon^-2 sum_i
       Tr[H6,e Q1,e j_i rho4,e(t) j_i*],
    Pminus_e(t)=kappa/(2epsilon^2)
       Tr[{H6,e Q1,e,Gamma6,e} rho6,e(t)].                (17)

The N=6 Hamiltonian commutes with its spectral band and the second birth
lands in terminal N=8. Consequently

    g_e'=Pplus_e-Pminus_e                                (18)

is exact. Pplus_e is nonnegative for sufficiently small epsilon, since
the first-high Hermitian band is positive. Pminus_e is a real loss term
including interband coherences; it is not assumed nonnegative for an
arbitrary density or identified as bath heat.

The complete evolved-input source estimate in Hermitian coordinates is

    U1,e* j_i v4,e(t)=epsilon^2 R_i,S a4,e(t)+O(epsilon^4).

Together with H6,e Q1,e=delta epsilon^-4 U1,e[I+O(epsilon^2)]U1,e*,
uniform strong source convergence, and sum_i R_i*R_i=72I, this gives

    epsilon^2 Pplus_e(t) -> 72 kappa delta S4(t),          (19)

uniformly on [0,T]. Finite-spin source coefficients are not set equal to
rotor constants before taking this limit.

Multiplying (18) by epsilon^2 and testing as in (13), the uniform bound
on g_e gives epsilon^2 g_e'->0 as a distribution. Hence

    epsilon^2 Pminus_e -> 72 kappa delta S4(t)             (20)

in the same distributional sense. This conclusion is weaker than a
pointwise limit of the loss term and does not claim such a limit.

For comparison, the positive diagonal fast-band carrier quantity

    D_e(t)=kappa delta epsilon^-6
       Tr[(U1,e* Gamma6,e U1,e)(U1,e* rho6,e U1,e)]         (21)

does have epsilon^2 D_e(t)->72 kappa delta S4(t) at fixed positive time,
using the trace-norm rare-density limit, bounded strong convergence of
the projected loss to Gamma1, and (15). It isolates the leading diagonal
carrier contribution. It is not substituted for the exact Pminus_e:
interband coherences and subleading physical band energies remain in
(17), with only the distributional comparison established above.

Thus a finite stored band energy coexists with first-high injection and
loss terms of order epsilon^-2. Their leading cancellation follows from
the exact finite-spin balance and the limiting rare density. This shows
why bounded total mean energy or ordinary state convergence alone cannot
replace a resource accounting for the original formation dynamics. It
does not turn either positive circulation term into a lower bound on
net external energy consumption, apparatus capacity, irreversible heat,
or preparation work.

## 6. Obligations and scope

The new checks owed are the shrinking-time source argument, uniform bound
at zero, distributional endpoint sign and coefficient, exact band-power
decomposition, and its singular-order normalization. The full-ensemble
age estimates and selected low-sector rotor construction remain named
provisional dependencies. An elementary injection/depletion control and
the actual rotor finite-fiber Green calculation can check normalizations;
neither proves the large-spin cube theorem or a physical bath model.

The original compensated Hamiltonian, joint scaling, canonical preparation,
instrument and clock remain supplied. There is no new physical selection
principle. No mixed-state Fisher conclusion follows from the divergent
variance. No statement about normalized N=6-start fixed-time variance,
growing graphs, joint small-kappa limits, unrestricted preparations or
TOE completion is made. The relevant scientific gain is a controlled
initial energy profile and integrated power balance for the same original
matter/field process, with the energetic rare population kept explicit.
