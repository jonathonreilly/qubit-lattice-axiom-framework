# Finite cyclic approximation of gauge record instruments

Date: 2026-09-22. Status: personal conditional theorem candidate;
independent proof check pending. The result concerns a supplied finite graph,
finite time, bounded flux shifts and record instruments. It is not a continuum
limit, a ground-state phase theorem or a native framework derivation.

## 1. Models and output being compared

Use the classical permanent-record model of
CLASSICAL_PERMANENT_RECORDS_WITH_QUANTUM_GAUGE_MEMORY.md, now with an integer
electric field E_l on every link. U_l|e_l>=|e_l+1> is the bilateral unitary
shift. Gauss law is the integer equation D E=Q(c). Hops and neutral pair
births preserve it by the same incidence calculation. A loop shift has
z_l in {0,+1,-1}, Dz=0. The graph is fixed and finite.

The regulator replaces each link by Z_(2S+1), represented by -S,...,S,
and each shift by cyclic addition. Embed this basis into the integer one
with I_S. Initial record contents are fixed; the initial field, possibly
entangled with an arbitrary inert reference, has support |E_l|<=M0<=S
on every link and satisfies the integer Gauss equation. A mixed initial
record configuration follows by conditioning and convexity.

Between occupation events, in each classical record block c let

    H_c = A_c(E) + sum_alpha (v_(c,alpha) U^(z_alpha)
                              + conjugate(v_(c,alpha)) U^(-z_alpha)), (1)

where A_c is any real diagonal function and z_alpha is a unit-step closed
cycle. The coefficients v are bounded uniformly in c. This finite sum is
a bounded perturbation of the self-adjoint diagonal operator A_c. In the
cyclic model use exactly the same A_c on representative electric values
and the cyclic loop shifts. In particular one may keep quadratic electric
energy exactly on those representatives. Define

    J_l = sum_(alpha:z_alpha,l!=0) sup_c |v_(c,alpha)|.                (2)

No cosine approximation to E^2 is used in this theorem, so it does not
inherit a positive Euclidean-transfer construction or an N^-2 dispersion
term from one. The existing September 14 closed-Hamiltonian cyclic/rotor
note addresses that different, more structured comparison.

An unmarked occupation event a is a specified allowed vacancy/record swap
or neutral pair birth on an edge. Its intensity r_a(o) depends only on the
current occupation pattern and is bounded by rbar_a. The event's internal
charge/readout instrument is the earlier unitary shift, or the Wilson birth
instrument K_(b,eta)=(I+bW^eta)/(2 sqrt(2)), including its charge transport.
It can copy all newly made record contents into a history register. The
unmarked occupation process is identical in both models and independent
of the field and existing contents, as proved in that note.

For event a and link l let s_(a,l) be a uniform bound on the largest partial
electric displacement in its shift words. A unitary record hop or ordinary
birth has s=1 on its edge and zero elsewhere. A Wilson-reading birth has

    s_(a,l) = 1_(l is the birth edge) + |z_l|,                         (3)

at most two. Using the maximal partial displacement, rather than only the
net displacement, prevents a wrap-and-return word being ignored. All event
instruments in this note are built from these specified words. Assume S is
at least their largest s. Other instruments require their own growth and
boundary checks and are not silently included.

The compared output includes the final quantum field, final record contents,
and, if desired, the entire marked record trajectory including event times.
Tracing away any part of that output can only improve the bound. This
mathematical output extension does not claim that the native record axioms
provide or make readable every trajectory label and time.

## 2. Explicit finite-time error

For every lambda>0 define

    k_l(lambda)=sum_a rbar_a (exp(lambda s_(a,l))-1),
    a_l(lambda)=2 J_l sinh(lambda)+k_l(lambda),
    C_l(lambda)=4 J_l
                +2 sum_(a:s_(a,l)>0) rbar_a exp(lambda(s_(a,l)-1)),
    F(a,T)=integral_0^T exp(a t) dt
          =(exp(aT)-1)/a for a>0, and T for a=0.

The claimed bound is

    (1/2)|| output_infinite - I_S output_cyclic I_S^dagger ||_1
       <= min(1, B_S(T,lambda)),

    B_S(T,lambda)=sum_l exp[-lambda(S-M0)] C_l(lambda) F(a_l(lambda),T).
                                                                         (4)

I_S acts only on final field factors. The bound is uniform over the stated
initial support and arbitrary reference systems, hence also controls the
corresponding restricted-input channel distance. Classical total-variation
distance for any selected record outputs is at most the same right side.
Optimizing lambda is permitted; no asserted optimum or volume-uniform
estimate is needed. With fixed lambda, graph and rates, the upper bound
decays exponentially in S at each fixed T.

For unit-shift events only, let R_l=sum_(a:s_(a,l)=1) rbar_a. Then

    k_l=R_l(exp(lambda)-1),    C_l=4J_l+2R_l.

The weaker replacement F(a,T)<=T exp(aT) is sometimes convenient. The
rates are upper bounds, so counting mutually exclusive directed events
separately remains valid but may be wasteful.

## 3. Proof, including the output history

Write M_l=exp(lambda |E_l|), in either field space. For a loop in (1),
the ratio of adjacent weights is in [exp(-lambda),exp(lambda)], including
a cyclic endpoint transition whose absolute-value ratio is one. The
anti-Hermitian part of the conjugated Hamiltonian M_l H_c M_l^(-1) has
norm at most 2J_l sinh(lambda). Diagonal A_c commutes with M_l. Consequently

    || M_l exp(-i H_c t) psi ||
       <= exp(2J_l t sinh(lambda)) ||M_l psi||.                         (5)

The same estimate holds for classical-record-controlled Hamiltonians on
purifications. One can first prove it with finite diagonal cutoffs; the
diagonal interaction picture and bounded shift perturbation give the
infinite-space statement on the weighted domain. No bound on ||A_c|| is
required.

Dilate each normalized event instrument to an isometry B_a with fresh
orthogonal output labels. For a unitary shift its weighted growth is
immediate. For the Wilson event, summing the two b values cancels the
cross terms in sum K^dagger M_l^2 K. The remaining terms are a convex
combination of M_l^2 conjugated by the identity and the two loop shifts;
including the charge shift and uniformly selected q only adds the shifts
already counted in (3). Thus in both models

    || M_l B_a psi || <= exp(lambda s_(a,l)) ||M_l psi||.               (6)

The labels and inert reference are acted on by the identity in (5)-(6).
The instruments need not have field-independent individual b probabilities.

Condition on the entire **unmarked occupation** path h. Its probability
law is common to both models, even though the conditional readout-bit laws
can differ. Let N_l(t)=sum_(events a before t) s_(a,l). Applying (5)-(6)
to the finite-model prefix purification gives

    ||M_l psi_(S,h)(t)||
       <= exp[lambda M0+2J_l t sinh(lambda)+lambda N_l(t)].             (7)

Between events, the Hamiltonian embedding discrepancy is supported at a
cyclic endpoint. A shift and its adjoint each have discrepancy norm at
most twice their coefficient. Summing the affected endpoints gives

    ||(H_infinite I_S-I_S H_cyclic) psi||
       <=4 sum_l J_l ||1_(|E_l|=S) psi||.                             (8)

The diagonal part cancels exactly. The bound permits overcounting a loop
at every affected link. At an event, B_infinite I_S and I_S B_cyclic are
isometries, have difference norm at most two, and agree on all inputs
whose relevant link values are at least s steps from a wrap. Therefore

    ||(B_(a,infinite) I_S-I_S B_(a,cyclic)) psi||
       <=2 sum_(l:s_(a,l)>0)
           ||1_(|E_l|>=S-s_(a,l)+1) psi||.                            (9)

The union-of-boundaries projector and the triangle inequality justify the
sum; no assumption of independent link amplitudes is made. This argument
uses identical record/environment label conventions in the two dilations.

Telescope the two dilated evolutions using a finite-model prefix and an
infinite-model suffix. All suffix isometries/unitaries have norm one.
Duhamel's formula handles the intervals between events. Equations (7)-(9)
then bound the difference of output purifications by a sum of time
integrals and event contributions. A boundary layer of depth s costs at
most exp[-lambda(S-s+1)] times the norm in (7); for Hamiltonian endpoints
the cost is exp(-lambda S).

For the finite-state nonexplosive occupation process, the counting
exponential has the elementary estimate

    E exp(lambda N_l(t)) <= exp(k_l(lambda) t).                        (10)

Indeed its conditional drift is exp(lambda N_l) times
sum_a r_a(o)(exp(lambda s_(a,l))-1), bounded by k_l times itself; apply
Gronwall. For event terms use the predictable compensator with the
**pre-event** N_l(t-), bounding r_a by rbar_a. Together these yield
exactly the integral and coefficient in (4). No post-event displacement
factor is omitted: its required boundary depth is the separate
exp(lambda(s-1)) in C_l.

For normalized pure states, half trace distance is at most their vector
distance. Partial trace is contractive. Average these inequalities over
the common path law h, retaining h as an orthogonal classical output if
wanted. This proves (4) for pure inputs with a reference; purifying a
mixed input proves the general case. Adding the record-mark copies only
enlarges the dilation and does not change the estimates. Importantly, the
proof never identifies the field-sensitive fully marked path probabilities
with one another; only the unmarked occupation law is shared.

## 4. What is and is not controlled

The integer dynamics preserves integer Gauss law. The finite dynamics
preserves modular Gauss law. Embedded cyclic configurations produced by
wraps can violate integer Gauss law; they are included in the state error
in (4), not discarded or called physical integer states. Thus the
probability assigned to that violation is also at most (4) for an initially
physical state, as a consequence of trace-distance control.

The full record formation statistics for occupation are already identical
at every cutoff; (4) additionally controls field-sensitive contents and
quantum output. A fixed finite S is not asserted exact for infinite time.
There is no exchange here of infinite volume, long time and increasing
cutoff, and no assertion that the model's field is a physical photon.
Locality, covariance, record ontology, energy supply, fresh apparatus,
physical Born readout and continuum selection remain separate dependencies.

The weighted-norm/finite-time truncation method has established precedents:
Tong et al., arXiv:2110.06942v2, and the repository's September 14 positive
finite-cyclic gauge-history note. Etienney, Robin and Rouchon,
arXiv:2501.09607v2, Section 2, also give a general contractive Duhamel
residual estimate for Lindblad truncation. Those are context for the method;
the history-instrument estimate (4) and the specific event bounds above
are proved directly for the displayed model. No claim of a literature-wide
novel theorem is made. A direct bounded-shift posteriori residual estimate
may be sharper for a particular computed trajectory.
