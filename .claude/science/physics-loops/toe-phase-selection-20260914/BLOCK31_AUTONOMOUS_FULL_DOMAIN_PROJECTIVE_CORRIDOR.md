# Block31: local activation of a full-domain projective corridor

Personal author derivation, 2026-09-15. Independent review pending. This
extends the supplied kernel construction in Block30. The mathematical target
is to derive the event order from one selected local generator while keeping
the Born weights, generator, seed and physical calibration explicitly supplied.

## 1. The program tag separates an input from an outcome

Keep Block30's smooth h and psi and carrier A=2I+rho. Encode a program as
B=8I+P, so its trace is17, while an outcome R has trace1. Define

 r(A)=psi(|tr A-5|^2),
 p(A)=psi(|tr A-17|^2+|det(A-8I)|^2),
 o(A)=psi(|tr A-1|^2+|det A|^2),
 k(A)=psi(|tr A-4|^2+|det A-4|^2).

Here k identifies the scalar marker2I on the benchmark, while o identifies
the benchmark rank-one outcomes. These functions are total smooth real
functions of all eight real matrix coordinates and similarity invariant.
They are all zero at the zero matrix. They are mathematical tag choices.

Replace the pair weights in Block30 by w_ij=r(A_i)p(A_j), and put
P_j=A_j-8I and x_ij=Re tr[(A_i-2I)P_j]. For arbitrary M2 input tuples set

 S=sum_(i!=j) w_ij, b=(S-1)^2, Z=S+b>=3/4,
 K_f(eta)=[b delta_(sum_i A_i)
   +sum_(i!=j) w_ij(f(x_ij)delta_(P_j)
                    +(1-f(x_ij))delta_(I-P_j))]/Z.        (1)

The full-domain probability, weak continuity, conjugation equivariance,
simultaneous GL2 similarity covariance and neighbor-permutation invariance
proofs are exactly finite-sum arguments as in Block30. Zero-valued neighbors
contribute neither tags nor a nonzero summand and may be ignored by (1).

With f_B=clip to[0,1], a carrier and program give the exact supplied Born
distribution on P and I-P. A single outcome gives delta_R. An outcome and
marker2I give delta_(R+2I). The program by itself no longer has an outcome's
trace; its formation activity can be distinguished locally.

## 2. A smooth rate function on the entire input domain

Let c=sum_i r(A_i), q=sum_i p(A_i), u=sum_i o(A_i), v=sum_i k(A_i), and

 D_measure=(c-1)^2+(q-1)^2+u^2+v^2,
 D_copy=c^2+q^2+(u-1)^2+v^2,
 D_retag=c^2+q^2+(u-1)^2+(v-1)^2,
 a=psi(D_measure)+psi(D_copy)+psi(D_retag),
 lambda(eta)=a/[a+(a-1)^2].                             (2)

The denominator is at least3/4. Hence lambda is smooth, lies in[0,1], and
has all the same matrix and lattice covariances. In the three intended
contexts the count vectors are (1,1,0,0), (0,0,1,0), (0,0,1,1); exactly one
psi term is1 and the others are0, so lambda=1. At an empty/zero-only context,
a program alone, or a marker alone, each psi term is0 and lambda=0. These
are direct substitutions; a sharp type predicate is unnecessary.

For a finite Record configuration x, define the pure-append generator

 (L F)(x)=sum_(blank z) lambda(eta_z(x))
       integral [F(x union{(z,A)})-F(x)] K_f(eta_z(x),dA). (3)

Only sites adjacent to a Record can have a positive rate. If n Records are
present, there are at most6n such blank sites, each of rate at most1. The
jump construction is nonexplosive. To see this without relying just on a
divergent sum of mean holding times, stop at the Mth Record. The stopped
count satisfies E N(t wedge tau_M)<=n_0 exp(6t) by its rate bound and Gronwall.
Consequently Pr(tau_M<=t)<=n_0 exp(6t)/M, which tends to0 as M increases.
This supplies a total finite-seed Markov process
without a separate caller scheduler. A selected dimensionless rate is not a
derived empirical clock.

The Born version is weakly continuous in its content kernel but need not be
weakly differentiable at sharp zero probabilities. Substituting Block30's
smooth f_S gives a weakly smooth content kernel as well as smooth rates,
with different probabilities. No regularity assumption selects Born here.

## 3. Finite guard seed and its literal geometry

Fix a positive finite measurement count L. Let T be the3L initially blank
axis sites (x,0,0), x=0,...,3L-1. Initial nonzero Records are

 a_0=(-1,0,0), content2I+rho_0;
 p_j=(3j,-1,0), content8I+P_j, j=0,...,L-1;
 k_j=(3j+2,1,0), content2I, j=0,...,L-1.

Let C consist of T and these1+2L seed sites. Put a permanent zero-valued
Record at every site of the external vertex boundary

 G={z outside C: z is a nearest neighbor of some c in C}. (4)

This is an explicitly supplied finite seed; the guard is part of its cost.
There are at most6|C| guard sites and |C|=1+5L. The bound is deliberately
coarse and requires no runner-derived asymptotic count. Every later nonzero
Record lies in C, and every neighbor outside C is already in G. Consequently
any remaining blank site outside C sees only zero Records or no Records and
has rate0. The guard blocks locations by their being already permanent
Records, not by an unrecorded geometric mask supplied to the generator.

Initially only e_0=(0,0,0) sees carrier plus program. Every later event e_j
sees only its program, every c_j=(3j+1,0,0) sees no nonzero Record, and every
next-carrier site a_(j+1)=(3j+2,0,0) sees only its marker. Their rates are0.
When e_j forms R_j, only c_j becomes active and copies it. When c_j forms,
only a_(j+1) becomes active and writes2I+R_j. That activates e_(j+1), if it
exists. Every other adjacent site is an old permanent Record or a zero guard.

Induction gives exactly one active blank site at each unfinished stage:

 e_0,c_0,a_1,e_1,c_1,a_2,...,e_(L-1),c_(L-1),a_L.        (5)

After3L writes there is no active blank site. This is an invariant of the
local generator on the stated seed sector, not a supplied event order.

## 4. Transcript law and duration

The unique active site's rate is exactly1 at every stage, independently of
the realized branch. Its holding times are independent rate-one exponential
variables, and the total completion time has the Erlang law with shape3L.
Thus E tau=3L and Var tau=3L in the selected dimensionless units. The marked
jump construction separates these waiting times from the outcome draws.

At the measurement steps, (1) gives

 Pr(R_0,...,R_(L-1))
   =tr(R_0 rho_0) product_(j>=1) tr(R_j R_(j-1))
   =tr[R_(L-1)...R_0 rho_0 R_0...R_(L-1)],             (6)

because R rho R=tr(rho R)R for rank-one projectors. Zero branches are not
normalized. All preceding Records, including zero guards, persist. With a
supplied countable corridor/guard seed the same single active sequence can
continue indefinitely; the sum of the rate-one waiting times diverges almost
surely, so this particular infinite-seed sector is also nonexplosive. No
arbitrary infinite-configuration process is claimed by this argument.

## 5. Relation to the current source and open suppliers

The existing Block36 active-cut note already constructs a selected local
continuous-time process and derives its order on a supplied corridor. Its
complete real Bloch/Gaussian/Haar codec and archive quotient differ from this
construction. It is prior machinery, not evidence that autonomous formation
has first been discovered here. This proposal instead gives a small direct
M2 kernel on the entire possibility domain, explicit similarity covariance,
and exact arbitrary finite one-qubit projective transcripts under supplied
trace weights. It makes no priority claim.

The improvement over Block30 is internal: a supplied external event list is
replaced by consequences of the displayed selected generator and guard seed.
The full extensional rule, rate convention, initial carrier, programs, scalar
markers, zero guards, projective event calibration and any composite entangled
history coupling remain inputs or open suppliers. No genesis from an empty
configuration occurs: its rate is0. No new axiom or primitive is requested.

The exact personal checker enumerates ALL blank sites adjacent to Records,
without receiving a target mask. Across32 five-measurement transcript branches
it checks187 complete frontier states, preserving all old Records, copy and
retag contents, and agreement with separately computed ordered matrix
products. This fixture has98 seed Records, of which87 are zero guards, and
adds15 Records per branch. Three nonunitary similarities and24 proper cubic
rotations are also executed, together with a zero-branch repeat fixture.
Actually omitting guards produces extra enabled sites; omitting program tag
separation changes the enabled frontier. The quarter-probability smooth
alternative is checked exactly. These finite author tests are not an
independent review or a numerical proof for arbitrary horizons.
