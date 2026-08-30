# Preflight Witnesses

No Block19 target runner, target cache, or target mutation has executed. The
committed initial packet was attacked independently before execution. These
corrected analytical witnesses must be rederived by independent
implementations after the support-correction commit.

## Why the initial target was revised

The initial full family explicitly allowed every positive bounded
proper-cubic orbit-invariant hazard h(r). That makes full-family one-ray
selection impossible by definition and turns a generic controlled dilation
into an encoding of a chosen classical generator. The broad family is now an
outer structural control only.

The terminal-bearing family is the finite relation-factor Hamiltonian in
GOAL.md: one shared coefficient for a blank neighbor, one for a neighbor with
the candidate label, and one for any other recorded label. It contains no
profile lookup table.

## Exact star-unitary witness

On a fixed profile r, the relation-factor coefficients are

~~~
c_f(r)=g a^(m_f(r)) b^(n(r)-m_f(r)),
h(r)=sum_f c_f(r)^2.
~~~

The Hermitian interaction couples |bottom,0> only to the bright state

~~~
|chi_r>=h(r)^(-1/2) sum_f c_f(r)|f,f>.
~~~

The seven-dimensional star block has eigenvalues +sqrt(h), -sqrt(h), and five
zero modes. Its exact
exponential gives the sine/cosine channel in GOAL.md. The induced
fresh-vacuum Kraus completeness reduces exactly to

~~~
cos^2(sqrt(delta h))
  + sin^2(sqrt(delta h)) sum_f c_f^2/h
=1.
~~~

This witnesses exact unitarity and CP/TP. It does not authorize the runner to
insert the expected block as an oracle; the spectrum and channel must be
derived from the displayed Hamiltonian.

The target lock is exact only on a recorded target paired with the stipulated
vacuum ancilla. The Hamiltonian can reverse |f,f> to |bottom,0> on a
nonvacuum ancilla. Neighbor QND means every neighbor label projector commutes
with the Hamiltonian. Coherent profile marginals can still dephase after
discarding the target or ancilla.

## Weak-generator witness

For z=sqrt(delta h) with 0<=z<=1,

~~~
0 <= z^2-sin^2(z) <= z^4/3.
~~~

The upper bound follows from sin(z)>=z-z^3/6. Therefore the exact collision
probability has first-order coefficient h with a uniform O(delta^2)
profile remainder. The target label probability conditional on a write is
exactly c_f^2/h at every allowed finite delta.

The fresh-vacuum expectation of the Hermitian interaction vanishes. The
second-order expansion in sqrt(delta) therefore gives Lindblad jump operators

~~~
J_f=g |f><bottom| D_f,
~~~

and diagonal intensities q_f=c_f^2. A mutation that prints q_f without
recovering it from the sine expansion and Kraus coefficients must fail.

## Core classification witness

Let beta=b^2 and kappa=(a/b)^2. Then

~~~
q_f=g^2 beta^n kappa^(m_f).
~~~

A one-record profile has one same-label intensity and five other-label
intensities, with ratio kappa. The supplied kernel demands ratio two, so it
forces kappa=2. Conversely this value gives p_f=2^(m_f)/Z on all profiles.

The complete positive-real family matching the supplied kernel is therefore

~~~
q_f^(beta)=g^2 beta^n 2^(m_f),
h_beta=g^2 beta^n Z,       beta>0.
~~~

The overall g^2 is a clock-unit scale. Beta is not: changing beta multiplies
a profile with n records by beta^n. This is a one-dimensional
dimensionless freedom derived inside a fixed coefficient-sharing grammar.

The beta=1 matching-only member gives h=g^2 Z. It is a useful realization
identity, but its apparent uniqueness is conditional on equating the
other-recorded and blank gains.

## Same-Z discriminator witness

Use two separated blank targets:

- target x_2 has two same-label recorded neighbors, so n=2 and Z=9;
- target x_3 has three distinct-label recorded neighbors, so n=3 and Z=9.

Their rate ratio is beta. With the same g and all other premises:

~~~
beta=1: P(x_3 first | x_2 or x_3)=1/2,
beta=2: P(x_3 first | x_2 or x_3)=2/3.
~~~

The equal Z isolates the occupancy gain. For the local-infinite event, include
both targets and all blank target neighbors in the observation region.
Conditioning on exterior graphical history yields one common predictable
survival factor for the two named target densities; it cancels in the ratio.
Other competitors are not assumed to have constant rates.

The old n=0/n=6 fixture gives

~~~
P(x_6 first)=2 beta^6/(1+2 beta^6)
~~~

for one of each neighboring label. It is a hostile mutation if a checker
blindly reuses 1/2 and 2/3 on that fixture.

## Finite-step order witness

Normalize g^2=1/6. For two adjacent initially blank sites with all other
neighbors blank, define

~~~
r_0(delta)=sin^2(sqrt(delta)),
r_(1,beta)(delta)=sin^2(sqrt(7 beta delta/6)).
~~~

If x is visited before y,

~~~
P(y writes)=r_0+r_0[r_(1,beta)-r_0].
~~~

If y is visited before x, P(y writes)=r_0. The exact difference is

~~~
Delta_beta=r_0[r_(1,beta)-r_0].
~~~

Its leading terms are +delta^2/6 for beta=1 and
-5 delta^2/12 for beta=1/2. Finite scan order can therefore change an
O(delta^2) probability and can even reverse its sign. This must vanish from
the first-order generator; it is a regulator control, not a physical
selection statistic.

## Finite-volume convergence witness

On a finite torus, every local diagonal channel is a Markov contraction and
has

~~~
T_(x,delta)=I+delta L_x+R_(x,delta),
||R_(x,delta)||<=2 delta^2 h_max^2/3,
||L_x||<=2 h_max.
~~~

Expanding an ordered sweep and bounding all cross products gives the explicit
finite-volume remainder in GOAL.md. Its O(delta^2) constant depends on
L^3 but is uniform over every sweep permutation. Telescoping contractions at
delta=t/N give the same exp(t sum_x L_x) for arbitrary varying order
sequences. No volume-uniform or simultaneous-unitary result follows.

## Finite and local-infinite witness

For beta in \{1,2\} and alpha=6g^2, the profile extrema are anticipated to be

~~~
alpha <= h_beta <= 736 alpha.
~~~

The maximum occurs for beta=2 with six identical recorded neighbors:

~~~
h=(alpha/6) 2^6 (2^6+5)=736 alpha.
~~~

A common rate-736 alpha proposal field and an acceptance key realize both
hazards. Exponential keys with rates 2^(m_f) realize the conditional marks.
Each backward proposal query branches to at most the target and six
neighbors, giving the factorial-tail parameter 7*736 alpha T. The runner must
rederive the bounds, measurable local construction, covariance, formation,
and permanence rather than citing them as labels.

## Outer structural control

The simultaneous proper-cubic action on slots and labels has a held-out desk
census of 5,075 profile orbits. An arbitrary positive orbit-controlled h
therefore has 5,074 dimensionless coordinates modulo scale, while count-only
H(0),...,H(6) has six. This is expected to confirm that broad symmetry and
QND alone do not classify a coupling, but it is not evidence for the
pair-factor terminal.

The primary and independent implementations must derive the census
independently; the number may be checked only after the derivation.

## Strict carrier and provenance scope

The orthogonal seven-state pointer makes the label controls readable. It is
an auxiliary enlarged carrier, not a strict-M_2 construction and not a
derived encoder from the six nonorthogonal rho_f contents. Blocks09 and 10 do
not supply the six-mark law used here. Block02 is only a writer precedent.
Block11's noncommuting-readout boundary remains intact.

Fresh ancillas, vacuum preparation, discarding, mesh cadence, and weak
scaling are supplied. The campaign does not derive an autonomous bath,
physical time, or an action.

## Principal risks

1. Reverse-engineering the supplied factor of two may be called a prediction.
2. The exact sine/cosine collision may be conflated with an engineered
   linear-in-delta Kraus map.
3. Fresh-vacuum channel lock may be overstated as a Hamiltonian identity for
   arbitrary ancilla input.
4. Pointer-projector QND may be overstated as complete-state preservation.
5. A finite scan order may be called a clock.
6. The beta freedom may be confused with global g^2 rescaling.
7. The broad 5,075-coordinate outer family may be used to make the core
   result look stronger than it is.
8. One-site arity or the seven-state carrier may be reported as selected.
9. A local-infinite classical process may be reported as a global quantum
   collision unitary.
10. A bounded family result may be promoted to gravity, axiom, or TOE closure.

## Hard falsifiers

- any profile lookup coefficient in the core pair-factor Hamiltonian;
- missing Hermitian conjugate, wrong star norm, or failed exact CP/TP;
- target lock tested outside but described beyond the fresh-vacuum sector;
- neighbor-label projectors that fail to commute with H;
- an exact total jump probability printed as delta h instead of
  sin^2(sqrt(delta h));
- failure to recover the first-order q_f from the exact collision;
- a conditional mark ratio other than two on the one-record profile;
- beta=1 and beta=2 compared with different carriers, baths, schedules,
  event arities, initial laws, or weak scalings;
- quotienting beta as if it were a global time scale;
- failure of the same-Z local Record-order witness;
- first-order scan-order dependence;
- a simultaneous overlapping unitary asserted without construction;
- slot-only or label-only cubic rotations;
- arbitrary orbit controls used as the core terminal witness;
- no local-infinite generator construction or an invalid global next-event
  chain on infinitely blank Z^3;
- a strict-M_2, autonomous-bath, compound-event, gravity, axiom, audit,
  obligation, or TOE upgrade.
