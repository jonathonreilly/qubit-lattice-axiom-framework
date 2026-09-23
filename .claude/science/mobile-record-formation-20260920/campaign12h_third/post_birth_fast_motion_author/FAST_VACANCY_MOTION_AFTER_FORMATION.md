# Fast vacancy motion after a formation event

Status: personally derived conditional author result and exact graph control;
independent review pending. This is a finite six-site supplied-model transport
calculation, not a cubic field limit or a repeated-formation theorem.

## 1. Model and an actual formation output

Use the six-site oriented ring e=(e,e+1 mod 6), A={0,2,4},
background b=(1,0,1,0,1,0), and the supplied Gauss law
E_e-E_{e-1}+b_e-q_e=0. Each q is 0,+1,-1 and transport preserves q.
Integer-spin link shifts are normalized by sqrt(S(S+1)); their bounded
unit-rotor limit shifts integer E by one. Hopping has the same minus sign
as in the preceding formation model.

Start in q=b, E=0. Hop the plus record from 0 to 5 and apply the resolved
birth on edge 0 creating q_0=+1,q_1=-1. The resulting normalized P state is

    q*=(1,-1,1,0,1,1),  E*=(1,0,0,0,0,1).                 (1)

It has five records, total charge three and its only vacancy at B site 3.
This is precisely one nonzero output of -P j_0,+ T P, not an independently
postulated fast-sector initial state. On this ring the other outward hop
would occupy the birth edge and cannot contribute to the same mark. State
(1) is legal for all S>=1. Specifying its conditional post-event preparation
does not assert that a continuous-time event occurs at deterministic time zero.

Five records on six sites leave one vacancy. Every birth operator is therefore
zero throughout this number sector. Subsequent evolution here isolates motion;
it cannot test another birth. W counts empty A sites and is exactly zero or
one. Hopping changes W by one, so in the complete P/Q decomposition

    T = [[0,A^dagger],[A,0]],     W = [[0,0],[0,I]],
    H_epsilon = delta epsilon^-4 W + delta epsilon^-3 T.  (2)

At most two records can hop into a vacancy. Link amplitudes are at most one,
so ||T||<=2 and ||A||<=2, independent of S. No lossy-mode elimination or
assumption about decay is needed in this sector.

## 2. Controlled fast-time limit

Set laboratory time tau=epsilon^2 u/delta. After this time (2) becomes the
unitary generated in u by

    [[0,A^dagger/epsilon],[A/epsilon,I/epsilon^2]].         (3)

For an eigenvalue lambda of A^dagger A, 0<=lambda<=4, the two singular-value
blocks have eigenvalues

    e_-(lambda)=-2lambda/(1+sqrt(1+4epsilon^2 lambda)),
    e_+(lambda)=(1+sqrt(1+4epsilon^2 lambda))/(2epsilon^2).

Uniformly on this interval, |e_-+lambda|<=epsilon^2 lambda^2. The low-energy
spectral projection differs from bare P by O(epsilon), with the constant
bounded by ||A||; a P state has O(epsilon) amplitude in the high branch.
Spectral calculus therefore gives, uniformly for |u|<=U,

    ||exp(-i tau H_epsilon)P
        -P exp(i u A^dagger A)|| <= C_U epsilon.           (4)

For completeness the elementary projection bound follows directly by
normalizing (1, epsilon e_-/sqrt(lambda)) in a nonzero singular-value block;
its second component has absolute value <=epsilon sqrt(lambda). At lambda=0
the P component is already an exact zero-energy state. The low-branch phase
error is at most U epsilon^2 lambda^2, and the initial high-branch amplitude
and both endpoint rotations are O(epsilon). Thus (4) is also uniform in the
multiplicity or dimension of the singular-value decomposition. It extends
by the spectral theorem to the bounded rotor A.

The normalized, zero-extended spin shifts and their adjoints converge strongly
to the rotor shifts. Consequently A_S^dagger A_S converges strongly, with
uniform operator bounds, and its propagators converge strongly on compact
u intervals. Equation (4), followed by this bounded-operator limit, proves
trace-norm convergence from the normalizable state (1) for every joint
sequence epsilon->0, S->infinity. In particular it applies to

    epsilon^2 S(S+1)=delta/K

with fixed positive delta,K, the relation used in the pre-formation field
construction. This fast-time statement has a direct two-block proof; it does
not depend on the currently reviewed general dissipative fourth-order proof.
It is uniform on compact fast-time intervals, not on fixed nonzero laboratory
intervals as epsilon tends to zero.

## 3. Exact graph and field winding

At fixed Fourier coordinate theta conjugate to the integer flux E_0, there
are 30 charge words: the vacancy has six locations and the single minus
record has five. P has 15 words and Q has 15. A hop on edge 0 changes E_0 by
minus the oriented transported charge; other edges do not change E_0.
This determines every fiber matrix element, including its phase.

The two-hop operator on P is

    H2(theta)=-A(theta)^dagger A(theta)
             =-2I-(weighted adjacency of a 15-cycle).     (5)

Each word has exactly two distinct off-diagonal neighbors, each of magnitude
one. Traversing this 15-cycle once changes the integer flux by three. The
integer-exponent certificate in POST_BIRTH_FAST_RING_RESULTS.json lists all
15 charge words in order, the vacancy positions and the exact net flux.
It is an enumeration with integer arithmetic, not a floating spectral fit.
The spectrum at a fixed Fourier coordinate is consequently

    -2-2cos((2pi k+3theta)/15),  k=0,...,14,               (6)

up to reversing the cycle orientation. Equation (6) is checked numerically
at four angles, but the graph and holonomy establish the formula. Theta
fibers alone are not normalizable physical states.

Lifting the cycle back to integer flux unwraps it into an infinite path:
every complete circuit advances E_0 by three, so it never returns to the
same physical basis state. There are three disconnected winding components;
state (1) selects one. Within it, label successive P configurations by n in Z.
The operator is exactly -2I-(S_path+S_path^dagger). Its vacancy locations are
3,5,1,3,5,1,..., so the vacancy is at site 3 precisely when n=0 mod 3.

The initial delta state on that path evolves with probabilities J_n(2u)^2.
This follows by Fourier transforming the adjacency, whose dispersion is
2cos(k), and expanding exp(2iu cos(k)) in its Fourier coefficients. The
probability that the vacancy remains at the original B site is therefore

    p_3(u) = sum_{n=0 mod 3} J_n(2u)^2
           = [1+2 J_0(2sqrt(3)u)]/3.                     (7)

One can derive the second equality without an imported Bessel summation
identity. The characteristic function of n equals

    (1/2pi) integral exp(2iu[cos(k+alpha)-cos(k)]) dk
       = J_0(4u sin(alpha/2)).

Apply the three roots-of-unity filter alpha=0,2pi/3,4pi/3. The last integral
is the defining angular integral of J_0 after shifting k. This argument
uses a single normalizable electric-flux state and all of its winding paths.

At fast time u=1, p_3=0.08338269583779327; at u=1/2 it is
0.5862929500285945. These are probabilities that the vacancy is at its
original physical site, including returns with different charge words or
field windings. They are not no-hop or first-passage probabilities.
The laboratory interval for u=1 is epsilon^2/delta. Record motion after
this formation output is thus substantial on that short interval.

## 4. Controls, scope and next research decision

The standalone checker assembles the complete 30-state Fourier fibers without
importing another model builder. Exact integer graph checks establish the
15-cycle, flux three and vacancy period three. Numerical eigenspectra at four
angles agree with (6) to 4.5e-15. Fourier grids 64,128,256 at six fast times
agree with (7) to 3e-15. The numerical integrals are corroboration, not interval
certificates or the proof of the infinite path reduction. The first exploratory
source/results are preserved; its direct shell execution had no separate
saved timing receipt. The expanded graph checker has full timed streams and
a receipt. No scientific failure or threshold relaxation occurred in either
execution. Root read the complete scientific source and every result field.

This result identifies a concrete fast post-formation sector. It does not
exclude useful slow observables, averaging, dressed preparation, low-energy
wave packets, a simultaneous spatial scaling, or different supplied
Hamiltonians and instruments. It does not prove a thermodynamic transport
law, cubic field propagation after formation, fermion statistics, relativity,
a finite fuel mechanism, or a TOE derivation. The pre-event field theorem
remains a separate statement with its original hypotheses.

The next useful obligation is to choose and control the post-event matter/field
observables on the desired common time and spatial scales. An interaction
picture or band preparation may remove fast phases; that requires a new
proof with its gap, locality, preparation and scale assumptions explicit.
The field winding in this exact example makes that obligation substantive.
