# Microscopic birth energy beyond one star

Personal root reconstruction, 2026-09-24. Provisional conditional theorem in
the supplied compensated model; independent comparison pending. The original
resolved or coherent formation instrument is retained. The initial state is
explicitly prepared in the canonical dressed low band. No field-only output,
energy filtering, new axiom, physical selector or TOE result is assumed.

## 1. Fixed graph and uniform perturbation premises

Take a fixed finite bipartite graph, hard-core matter states0,+1,-1, normalized
integer-spin link shifts, and the original Gauss constraint with background
one on each A vertex. Every edge below is oriented A to B. Let

    W=sum_(a in A)(1-n_a),    P=1_(W=0),    Pi_k=1_(W=k),
    F=sum_a F_a,             T=-(F+F*),
    h_epsilon=W+epsilon T+epsilon² C_S,
    H_epsilon=delta epsilon^-4 h_epsilon,
    L_j=sqrt(kappa)/epsilon j.

Here j is the original actual edge mark, either resolved by its sign or the
stipulated coherent sum of those signs. Let C=S(S+1). The supplied compensation
and its electric family preserve W and obey, on P,

    P C_S P=M+Q_S,
    M=P F*F P,
    Q_S=D_lambda/C,
    D_lambda=(1-lambda)D+lambda E2,      0<=lambda<=1.        (1)

D is the active matter-dependent electric energy and E2=sum_e E_e². This is
the already supplied family, not a selection of one member. At fixed graph,
||T||, ||C_S|| and ||j|| are uniformly bounded in S and lambda. Normalized
spin shifts have norm at most one, E²/C<=1, and |E|/C<=1/2 for integer S>=1;
the finite number of local terms supplies the bounds. C_S can have nonzero
blocks above P; only W preservation and (1) are used in this proof.

For sufficiently small epsilon, uniformly in S and lambda, the Riesz band of
h_epsilon descending from W=0 remains separated from W>=1. For example choose
epsilon so ||epsilon T+epsilon²C_S||<1/4. The contour |z|=1/2 then has a
uniform resolvent Neumann expansion. Let P_epsilon be that spectral projector
and U_epsilon its canonical direct rotation from P, with U_0=I and positive
P-to-P polar convention. Its convergent Taylor expansion has uniform operator
norm bounds, independent of the growing Hilbert dimension. U preserves total
matter number because the full h and P do.

Explicitly, U=[P_epsilon P+(I-P_epsilon)(I-P)]
[I-(P_epsilon-P)²]^(-1/2), with the branch continuous from I. The uniform
resolvent bound and analytic inverse square root justify the uniform Taylor
remainders used below; unitarity is for real epsilon.

The physical initial state is U_epsilon psi for a normalized psi in P. It
need not be an H eigenvector. This preparation is supplied and differs from
the bare psi. At changed lambda it uses that lambda's canonical band; it is
not silently identified with the single fixed star preparation used in the
earlier electric robustness result.

## 2. The first high-band part of an actual jump

Put A=Pi1 T P=-F P and Z=Pi2 T Pi1 T P=F²P. The uniform direct-rotation
expansion gives

    U_epsilon P=P+epsilon F P
      +epsilon²[Z/2-M/2]+O(epsilon³).                       (2)

The order-two terms shown lie in Pi2 and P. There is no order-two Pi1 term:
C_S has no off-diagonal W blocks and two T moves have even W parity. The
Pi2 denominator is two; it must not be replaced by one.

Let jbar=U_epsilon* j U_epsilon, and define B_j=PjF P. Since j lowers W by
one and annihilates P, equations (2) and the adjoint rotation give

    P jbar P=epsilon B_j+O(epsilon³),
    Pi1 jbar P=epsilon² R_j+O(epsilon^4),
    R_j=jZ/2+A B_j.                                        (3)

The other first allowed orders are Pi2 jbar P=O(epsilon³), Pi3 at order four,
and so on. These are actual microscopic output amplitudes in the rotated
energy decomposition, not a declaration that the born state stays in P.

There is a useful exact local simplification. For a mark centered at a,

    R_j=-F_a j F_a P=-F_a B_j.                              (4)

To prove it, F_a²=0, different F_c commute, and F_c commutes with j for c!=a.
Shared B targets do not spoil this: two attempted hard-core creations on the
same B site vanish in either order. Different link shifts commute. In jF²P,
only terms containing F_a survive, since otherwise a is still occupied and j
annihilates it. The two orderings give
jF²P/2=sum_(c!=a)F_c jF_a P. Subtracting F B_j leaves precisely (4).
This proof works at finite spin, with the actual shift coefficients and blocked
boundary moves, and on the whole P space. It does not require a dilute B state.

The sign and denominator in (3) are consequential: the high component left
after rotating the actual birth is not simply the dressed image of B_j psi.
The other centers' apparent first contributions cancel; the same-center
three-step path remains.

## 3. Full microscopic moments and power

Write hbar=U_epsilon* h_epsilon U_epsilon. Its P/Q off-diagonal blocks vanish
exactly. J=(-1)^W gives h(-epsilon)=J h(epsilon)J and the same covariance of
the canonical rotation. Therefore

    P hbar P=epsilon² Q_S+epsilon^4 H4_S+O(epsilon^6),

with bounded H4_S and uniform remainders. The first high diagonal block is
Pi1+O(epsilon²); its couplings to Pi2 start at order epsilon. Selection rules
in (3) and parity make the unscaled gain and loss expansions even in epsilon.

For a normalized psi in P, put

    b_j=||B_j psi||²,
    r_j=||R_j psi||²,
    q_j=<B_j psi,Q_S B_j psi>.

For a mark with b_j>=b_*>0 the actual normalized conditional output obeys

    <H>_j = delta epsilon^-2 (q_j+r_j)/b_j + O(delta),
    Var_j(H) = delta² epsilon^-6 r_j/b_j
                +O(delta² epsilon^-4).                    (5)

Constants may depend on the fixed graph and b_*, but not on S, lambda or psi.
The denominator is ||j U_epsilon psi||²=epsilon² b_j+O(epsilon^4).
For the mean, the unscaled numerator is
epsilon^4(q_j+r_j)+O(epsilon^6). For the second moment it is
epsilon^4 r_j+O(epsilon^6): the first high band has W²=1, while the low-band
contribution starts two orders later. Subtracting the squared mean changes
only the O(delta² epsilon^-4) term. These facts prove (5).

For fixed-field finite-support inputs, Q_S B_j psi tends to zero, so r_j/b_j
is the leading rescaled mean coefficient as well. If flux grows with S, the
q_j term can be of order one and must remain. No normalized formula is asserted
for a leading blocked mark b_j=0 or a sequence with b_j tending to zero.

Define the dimensionless effective dissipator adjoint

    D_B*(Q)=sum_j B_j* Q B_j-{Gamma_B,Q}/2,
    Gamma_B=sum_j B_j*B_j.

The full instantaneous microscopic energy derivative, compressed to the dressed
initial band, has the stronger operator-norm expansion

    P U_epsilon* L_micro*(H_epsilon) U_epsilon P
      = kappa delta epsilon^-2
          [D_B*(Q_S)+sum_j R_j*R_j]+O(kappa delta).          (6)

The Hamiltonian part is identically zero on H_epsilon. The unscaled jump gain
is epsilon^4[B_j*Q_S B_j+R_j*R_j]+O(epsilon^6). The low compression of jbar*jbar
is epsilon² B_j*B_j+O(epsilon^4), so the energy loss is
epsilon^4{B_j*B_j,Q_S}/2+O(epsilon^6). Multiplying their difference by the
physical prefactor kappa delta epsilon^-6 yields (6). Odd order-five terms
vanish by parity; retaining them would unnecessarily weaken the uniform
remainder. This argument does not assume psi is a low-energy eigenstate.

Under the joint scaling epsilon²C=delta/K, equation (6) reads

    d<H>/dt at0 = kappa K <D_B*(D_lambda)>
                 +kappa K C sum_j r_j +O(kappa delta).     (7)

Thus energy moved within the slow matter/field sector and energy put into fast
microscopic states are separate contributions. The first contribution alone
need not have the sign of the full microscopic derivative. Equations (5)-(7)
come from the full generator and a uniform spectral expansion, not from a
trace-norm limit of density matrices.

## 4. Geometry controls and a degree-two exception

For a rotor basis word with all A charges+1 and every B empty, let d_a be a
center's degree. At one resolved edge from that center,

    b_+=b_-=d_a-1,
    r_+=2(d_a-1)(d_a-2),
    r_-=(d_a-1)(d_a-2).                                    (8)

For r_+, each unordered pair of remaining destinations admits two identical
transport histories, giving squared amplitude four. For r_-, the final
negative charge distinguishes the two ordered destinations. For a coherent
edge mark the plus and minus R outputs have different final negative-charge
locations, so their norms add; b is2(d_a-1). Hence both stipulated instruments
give

    sum_j r_j=sum_a 3d_a(d_a-1)(d_a-2).                     (9)

The three-leaf star gives18, reproducing its previously exact microscopic
power coefficient. The cube gives72. A degree-two ring gives zero, because
after the transport and birth no third empty neighbor remains for F_a in (4).
This exact exception excludes a universal application of the star's divergent
mean-energy coefficient. It does not say that the ring's full energy or
higher moment is zero: higher-order high-band contributions can remain.
The six-site cycle still cannot form a second pair.

## 5. Actual cube input, including high flux

Use the cube with A={0,3,5,6}, the original local operators, all A charges+1,
B empty, and circulation n on square0-1-3-2-0. All edges are oriented A to B,
so the nonzero fields are E01=n,E31=-n,E32=n,E02=-n. The initial word is
Omega_n. At finite spin require |n|<=S, and prepare U_epsilon Omega_n.

Set u=n²/C and v=n/C. At each of the two affected A centers the incident
fields are a permutation of(n,-n,0). Define a=1-u-v and b=1-u+v. The squared
plus outward weights are(b,a,1), and squared plus birth weights(a,b,1).
The other two A centers have zero incident fields. Direct summation of (4)
over the actual finite-spin marks gives, for either instrument,

    sum_j r_j=72-72u+36u²+12u/C.                           (10)

At an affected center the sum is6(a²+b²+ab)=18(1-u)²+6v²; each unaffected
center contributes18. For the particular resolved(01,+) mark,

    b_j=a(1+a),     r_j=4a²,
    r_j/b_j=4a/(1+a) when a>0.                             (11)

At n=S this mark is blocked at leading order; the normalized expansion (5)
does not apply there. The all-mark result (6) has no such division and remains
uniform up to the spin boundary.

For this same nonblocked resolved mark, its two B output weights are a² and a.
Their conditional slow electric means are

    <D>_B=2n²/(1+a),
    <E2>_B=4n²+2+2n(2a+1)/(1+a).

Consequently, for n/S->x with |x|<1 and fixed lambda, (5) gives

    epsilon² <H>_j/delta
       -> 2+lambda [2x²(3-2x²)/(2-x²)],
    epsilon^6 Var_j(H)/delta² -> 4(1-x²)/(2-x²).

At lambda0 the leading normalized mean is2 for every such x: its slow and
fast contributions compensate in that particular mean. The initial dressed
mean has rescaled limit4x². This selected mark can therefore lower the mean
energy when x²>1/2 at lambda0. That does not contradict the positive summed
initial power below; individual conditional changes and the full dissipative
energy balance are different quantities. No uniform normalized assertion is
made as |x| approaches the blocked boundary.

The same primitive paths give the slow-energy drifts

    <D_B*(D)> = -32n²(3-3u+u²)-16n²/C,
    <D_B*(E2)> = 96-128u+48u².                             (12)

The first identity agrees with the previously sealed effective finite-spin
calculation and is reconstructed here rather than assumed. The second can
be checked locally: a path using old destination o and marked edge j changes
E2 by2-2E_o+2r E_j. Summing its actual squared spin amplitudes on both affected
and unaffected centers yields (12). Initial D and E2 both equal4n².

Equations (7), (10)-(12) prove the uniform rescaled power formula

    [d<H>/dt at0]/(kappa K C)
       = F_lambda(u) + [-4u+lambda(96-112u+48u²)]/C
         +O(1/C),

    F_lambda(u)=72-72u+36u²
                -32(1-lambda)u(3-3u+u²).                  (13)

Here fixed positive delta,K,kappa are understood in the O(1/C) constant; the
explicit1/C term in (13) is known from the leading operator formula, whereas
the other1/C correction depends on higher microscopic coefficients. Keeping
the explicit term does not claim to know the full next asymptotic coefficient.

For n/S->x with |x|<=1, u->x². At lambda0,

    F_0(u)=72-168u+132u²-32u³,
    F_0'(u)=-24(4u-7)(u-1).

It decreases from72 to4 on[0,1]. Increasing lambda adds a nonnegative term.
Thus F_lambda(u)>=4 for all0<=u<=1 and0<=lambda<=1. In this supplied family,
the full leading microscopic initial power is positive even where the slow
D energy drift is negative. At fixed n the coefficient is72 for every lambda.
For the nonblocked selected mark and |x|<1, the leading variance coefficient
from (5) is4(1-x²)/(2-x²), rather than the earlier effective-target n^4 formula.
Those two variances refer to different Hamiltonians and limits.

## 6. Evidence, limits and preparation accounting

The fresh primitive path control uses no campaign builder. It checks rotor
stars of degrees1 through5, the cube, degree-two ring, finite spins1,2,5,20,100,
positive/negative circulation and blocked edges. It independently evaluates
jF²/2-FB and the local-F_a expression, and reconstructs all drift formulas.
Symbolic polynomial controls supplement the enumerated finite examples.

A second control constructs the complete721-state spin-one Gauss space of
K(2,4), including its N=6 sector and possible two-formation capacity. It checks
the exact R identity on every P column, constructs the canonical spectral
rotation from the full Hamiltonian, and directly measures the actual full-H
conditional moments and energy derivative. Both instruments, both electric
endpoints, two flux inputs and their coherent superposition are included.
Varying epsilon at fixed S tests the perturbation formulas with their slow
Q contribution. It is not a numerical S-to-infinity proof; uniformity follows
from the explicit fixed-graph norm and gap argument above.

The result is an initial microscopic power and actual first-event moment
theorem for a prepared dressed input. It gives neither a finite-time cube
energy accumulation theorem nor a reservoir construction or heat interpretation.
At high flux the initial system itself already has energy of order C. Any
finite-time supply inequality must account for that initial energy and the
subsequent dynamics. Clock constructions that approximate one-time channels
do not automatically reproduce this instantaneous derivative.

The compensation, electric family and dressed preparation remain supplied.
No spatial continuum, volume limit, preferred lambda, natural bath, preparation
mechanism or empirical identification is derived. Independent checking and
publication review are separate from formal retained/audit status.
