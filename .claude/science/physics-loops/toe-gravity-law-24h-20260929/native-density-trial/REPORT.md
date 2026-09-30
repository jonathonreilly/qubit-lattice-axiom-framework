# A finite-time pair pulse and uniform low-density variational bounds

Provisional root derivation, independent check pending. The goal is to improve
the explicit mobile native model's dilute variational control, not to assume
Bose condensation, a gravity phase, or an actual record instrument. The same
single physical qubit per site and supplied Hamiltonian/Born interpretation
remain hypotheses. This is internal discovery, not a formal source proposal.

## Inputs and exact target

Use each finite cubic torus L>=5 and the mobile positive Hamiltonian
H0=H+V3+Wtau in native-stability-route/REPORT.md, with mu,tau>0 and volumeV.
Its complete pair/SOS construction has root's selective independent check in
independent-native-stability-check/REPORT.md. In particular H0>=0,
H0 Omega=0, and H0 Q_E1(x)†Omega=0 only before Wtau is added; for the mobile
model the UNIFORM sum Q†Omega, Q†=sum_x Q_E1(x)†, remains a zero vector.
This uniform property, not compact zero modes of the mobile model, is the
load-bearing two-particle input. Its norm squared isV by the unique-center
E overlap. A future use of the separate coercivity bound inherits that proof's
independent-check status; the variational result below does not depend on it.

For Hnu=H0-nu N with nu>0, construct a legal full-carrier state with uniform
volume-independent energy bound of order-nu²V. Do not replace the actual
interacting carrier by independent bosonic pairs.

## A local bounded generator with exact selection rules

Let K=sum_x K_x and

    K_x=i[Q_E1(x)†-Q_E1(x)],   psi(t)=exp(-it K)Omega.

Each K_x is Hermitian and supported on the four physical sites x±e1,x±e2.
Its norm is at most2sqrt(2)<3 by the triangle bound. Each physical site belongs
to exactly four translated K supports. The exact local norm is sqrt(2), but
the estimate3 is sufficient and avoids using an optimized constant.
K Omega=iQ†Omega, with norm squaredV and particle number2. Thus H0 kills
both Omega and K Omega. This is an actual finite-volume unitary state, on the
full hard-core Hilbert space, not a truncation of its power series.
The pulse selects one cubic E channel as a variational state; the Hamiltonian
itself retains its original cubic symmetry. No new basis or axiom is selected.

Every operator H0 can be grouped as sum_x h_x, where h_x contains its onsite
mu n_x, original E/T attraction centered atx, the153 center-x triple terms,
and all15 positive pair-gradient squares based atx. This h_x need not be
positive. Its support lies in {x}, the6 unit neighbors and18 pair-graph
neighbors, so at most25 sites. Using ||Q_A||<=2 gives

    ||h_x|| <= h_* =182 mu+240 tau.

Here onsite plus attraction cost1+16+12=29 timesmu, triples153mu, and each of
15 pair differences has norm at most4, hence squared norm16 and total240tau.
All estimates use the actual monomials and do not scale with total volume.

## Uniform fourth-commutator bound

For an operator O initially supported on s sites, only at most4s terms K_x
can have a nonzero commutator. A nonzero nested step adds at most3 sites and
costs at most2*3 in norm. Therefore, by expanding the full nested commutator
and counting only connected sequences,

    ||ad_K^r O|| <=24^r product_(j=0..r-1)(s+3j) ||O||.

Periodic identifications can reduce the count, not increase it. This bound
uses no Lieb-Robinson theorem or thermodynamic limit. It is valid uniformly
for every finite stated torus. Consequently

    ||ad_K^4 H0|| <= C_H V,
    C_H=24^4*25*28*31*34*(182mu+240tau),
    ||ad_K^4 N|| <= C_N V,
    C_N=24^4*1*4*7*10.

Define A=C_H/24 and B=C_N/24. These deliberately loose positive constants
are finite and independent of volume. There is no requirement that K commute
with H0 or that overlapping pair creators behave as bosons.

## Exact Taylor remainder on the full unitary trajectory

Because H0 kills Omega and K Omega, the energy expectation and its first
three derivatives vanish at t=0. The fourth derivative at any t is the
expectation of ad_K^4 H0 in psi(t), up to i^4=1. Integral Taylor remainder
and the previous norm bound give

    0 <= <H0>_t/V <= A t^4.                              (1)

The mean number has value and first derivative zero and

    d²<N>_t/dt² at0 =2<K Omega,N K Omega>=4V.

The number phase R=exp(i pi N/2) sends K to-K and fixes Omega and N, so
<N>_t=<N>_(-t); in particular the third derivative at zero vanishes.
The same global remainder bound yields

    |<N>_t/V-2t²| <= B t^4.                             (2)

Equations(1),(2) are uniform inequalities for the exact state, not merely
asymptotic coefficients or an expansion valid only while totalVt² is small.
Unitarity preserves the norm of every fourth commutator, even at largeV.

## Variational energy and density bounds

Choose the actual pulse duration by

    t²=nu/(A+nu B).

Then (1),(2) give the finite-volume bound

    E0(Hnu)/V <= -nu²/(A+nu B).                         (3)

No truncation error remains in this inequality. Also H0>=0 implies
E0>=-nu<N> in every ground state. Combining with (3) gives

    rho_ground >= nu/(A+nu B)>0.                        (4)

This is an honest, very small quantitative lower bound. It uses a full
interacting quantum trial rather than finite separated wave packets. It does
not identify the order parameter or show a differentiable equation of state.
At fixed finiteV, the exact two-particle zero states additionally allow the
usual boundE0<=-2nu; the uniform bound(3) is useful at fixed positive density
and large volume, and is compatible with that finite-size fact.

Conditionally, if the independently established mobile-model coercivity is
H0>=c N(N-2)/V with a volume-independent c>0, then every ground state also has

    rho_ground <= min(1,nu/c+2/V),
    E0/V >= -(nu+2c/V)²/(4c).

The first uses E0<=0 and <N²>>=<N>²; the second minimizes the same quadratic.
Together with (3),(4), thermodynamic accumulation points at fixed positive nu
have density between constant multiples ofnu asnu decreases tozero, and
energy density between negative constant multiples ofnu². This is a bounded
onset statement, not proof of condensation, linear Goldstone propagation,
rotational emergence, two tensor modes, or compatibility with gravitational
constraints. The coercivity step must remain conditional until checked.

## Review boundary and next action

This note is an original root derivation. It uses the separately reconstructed
native pair identities but no author implementation. Obtain an independent
check of the uniform commutator count, exact early derivatives, variational
minimizer and density inequalities before downstream reuse. The actual law
still needs a physical source/action, a record instrument and any gravitational
identification; those are not supplied by an equation-of-state bound.
